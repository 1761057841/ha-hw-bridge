# HA HW Bridge

把一个 Home Assistant 实例变成一个**可以被华为智慧生活发现的虚拟父网关**，
再把 HA 里的实体投影成华为云上的子设备。

```
华为智慧生活 App
   │ UDP 5683 组播发现 → SPEKE(PIN) 握手 → CloudSetup 下发绑定信息
   ▼
core/pairing_runtime.py + core/speke.py        局域网配对
   ▼
core/cloud_runtime.py                          TLS 长连接（activate/login/heartbeat/GRS）
   ▼
business/child_manager.py                      子设备生命周期（batchBind/devInfoSync/dataSync）
   ▼
business/adapters/*.py  ⇄  ha_adapter.py       物模型 ⇄ HA 实体
```

## 功能

- 局域网配对：App 里选「添加网关」，手动输入 8 位 PIN，无需公网回调。
- 一条常驻云端会话同时承载多个子设备（上限 64 个/网关，最多 3 个网关）。
- 35 个华为服务适配器 + 按 serviceType 回退：`switch` / `brightness` / `cct` / `colour` / `temperature` /
  `humidity` / `airDetector` / `motor` / `openLevel` / `opener` / `hcho` / `alarm` /
  `alarmBell` / `battery` / `luminance` / `pir` / `targetDistance` / `gasSensor` /
  `mode` / `fan` / `cleanerRobot` / `status` / `action` / `pm25` /
  `childLockSwitch` / `lightSwitch` / `lightMode` / `colourMode` / `filterElement1-12` /
  `light` / `volume` / `gear` / `modeSetting` / `visitPoint1-12`。
- **厂商自定义 sid 自动回退**：Profile 里 `deviceSwitch` / `ledSwitch` /
  `leftOpener` / `alarmEvent` 这类自定义 sid 会按它声明的 `serviceType` 找到对应适配器，
  不再因为 sid 没登记而拒绝整台设备。sid → serviceType 对照表由
  `scripts/gen_service_id_map.py` 从 5926 个官方 Profile 生成（912 个 sid），
  不靠猜。
- 华为官方设备目录里有 **4415 台** 至少能投影一部分功能，**1101 台**可完全覆盖，
  完整清单见 [`docs/device-catalog.md`](docs/device-catalog.md)。
- 12 个预置产品模型（智控灯泡/床头灯/水壶/电饭煲/空调/窗帘…），
  也支持按 `prodId` 自定义。
- **摄像头**：开关机、拍照、巡航、本地存储、告警检测（人形/移动/声音/婴儿哭声/
  动物/车辆/越界/区域/陌生人/车牌…按字段分别上报）、预置位按钮。
  画面本身不经过本集成 —— 见下方「摄像头说明」。

## 摄像头说明

摄像头**可以添加**，但不能通过本集成看到画面。原因是协议层的硬限制，不是没做完：

华为物模型（Profile）里，摄像头只暴露**控制与告警**特性 —— 开关机、拍照、巡航、
预置位、各类告警标志位。**没有任何一个字段携带视频流地址**。

这一点是查证过的，不是推测：72 个摄像头 Profile 的全部 characteristic 里，
`url` 字段只出现在 `logReport` 服务中，语义是「日志上传路径」；
搜遍 rtsp / hls / webrtc / playUrl / streamUrl / onvif 全部无命中。

华为 App 能看画面，是因为它加载 **摄像头插件（uiType=PLUGIN，61/72 个摄像头）**，
视频流走的是另一套通道，不经过局域网子设备的物模型。

所以本集成对摄像头提供的是：

| 能力 | 绑定实体 | 说明 |
|---|---|---|
| 摄像开关 / 拍照 / 巡航 / 本地存储 / 静音 | `switch` / `light` / `fan` | 通断类 |
| 告警检测（人形、移动、声音、婴儿哭声、动物、车辆、越界、区域、陌生人、车牌…） | `binary_sensor` | 每个检测项单独绑一个，用契约 `field` 指定 |
| 预置位 1-12 | `button` | 按一次 → 云台转到该预置位 |

`alarmEvent` 一个服务下带多个检测标志位，所以同一个 sid 可以绑多个
`binary_sensor`，靠契约里的 `field` 区分。默认是通用的 `alarm`。

要看画面，继续用华为智慧生活 App，或摄像头厂商自己的 App。想在 HA 里看画面，
需要的是厂商的 RTSP/ONVIF 地址，那是另一条路，和本集成无关。

## 安装

**方式一（推荐）：HACS**

1. HACS → 集成 → 右上角 ⋮ → 自定义存储库。
2. URL 填 `https://github.com/1761057841/ha-hw-bridge`，类别选「集成」。
3. 在 HACS 里搜索 **HA HW Bridge** 并下载。
4. 重启 Home Assistant。

**方式二：手动**

1. 把仓库里的 `custom_components/ha_hw_bridge/` 整个目录拷到 `config/custom_components/ha_hw_bridge/`
   （**目录名必须与 `manifest.json` 的 `domain` 一致**，否则 HA 找不到集成）。
2. 重启 Home Assistant。
3. 设置 → 设备与服务 → 添加集成 → **HA HW Bridge**。
4. 选择用于配对的 IPv4 网卡（必须与手机在同一局域网）。
5. 打开华为智慧生活 → 添加网关 → 输入通知里给出的 8 位 PIN。
6. 在集成页面的设备上点「添加子设备」，选产品模型 → 选服务 → 绑定 HA 实体。

> 从旧版 `migrate` 上来的网关：添加集成时会出现「复用已配对的网关序列号」选项，
> 选中旧序列号即可免配对接管，详见下一节。

## 从旧版本（oneconnect_bridge）升级

集成原名 `oneconnect_bridge`。改名后 HA 会把它当成另一个集成，旧的配置项无法使用。
新版内置了迁移支持：

- 添加集成时，如果检测到旧域名的配对材料，会出现「复用已配对的网关序列号」选项。
  选中旧序列号即可继续使用原来的云端身份（无需重新配对）。
- 复用旧序列号时，旧配置项里的子设备会被自动重建到新配置项，保留原 `subentry_id`，
  因此存储目录与云端子设备 ID 都不变。
- 旧目录 `.storage/oneconnect_bridge/` 只被**复制**、不会删除，可留作备份。

之后在旧配置项上删除即可（旧的集成代码已不存在，删除不会触发云端注销）。

## 子设备配置

子设备只从 UI 读取，**不再支持 mapping.yaml**。旧版的 `mapping.yaml` 导入入口已删除，
已有子设备请用上面的迁移路径带过来。

每个子设备保存的内容：

| 字段 | 说明 |
|---|---|
| `key` | 16 位十六进制，首次添加时生成，永不随改名变化 |
| `prod_id` / `sub_prod_id` / `device_type` / `manufacturer` / `model` | 华为产品身份 |
| `protocol_type` / `setup_type` / `known_fields_only` | 设备描述字段开关 |
| `room` | 房间名（可空） |
| `services[]` | `{st, sid, contract}` |
| `bindings[]` | `{sid, entities[]}` |

`contract` 用于吸收 Profile 之间的差异（枚举值、量程、步长、方向）。HA 的调用方式
固定在适配器代码里，不通过配置表达——详见 `docs/service-adapter-contributing.md`。

## 排障

- 网关设备下的「在线」`binary_sensor` 会显示阶段：`pairing` / `registering` /
  `online` / `offline` / `error`，`attributes.phase` 是同名字符串。
- 集成选项里可以打开「记录云端协议轨迹」，会写入
  `.storage/ha_hw_bridge/gateways/<serial>/cloud/trace.json`（含完整帧的 base64，
  敏感信息都在里面，排障后请关闭）。
- 「重新加载子设备配置」按钮等价于重新编译并应用一次计划，不需要重启 HA。

## 测试

适配器与计划编译不依赖 HA 运行时，可以直接跑：

```bash
python -m unittest discover -s tests -t tests
```

`tests/test_integration_stub.py` 用一套轻量 HA 桩验证 `async_setup_entry`、
子设备增删更新、旧域名接管这些跨模块路径。桩只在没装 Home Assistant 时生效，
真机上这些用例会自动跳过。

## 许可与来源

本项目源自 `xiasi0/ha-oneconnect-bridge` 的私有协议实现，协议字段来自真实抓包。
使用的华为云接口与物模型属于华为，仅供个人在自有设备上做本地集成。