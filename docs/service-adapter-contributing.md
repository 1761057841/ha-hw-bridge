# 服务适配器贡献指南

一个**服务适配器**把华为 Profile 的一个 `serviceId`（`sid`）翻译成 Home Assistant 的
状态读取与服务调用。新增设备类型时，绝大多数工作只发生在这里。

## 适配器契约

每个适配器是一个模块，暴露一个单例 `ADAPTER`，实现 `business/adapters/api.py` 的
`ServiceAdapter` 协议：

```python
class ServiceAdapter(Protocol):
    service_id: str
    entity_domains: tuple[str, ...]      # UI 实体选择器接受的域
    entity_counts: tuple[int, ...] | None  # 多实体适配器的数量范围，单实体为 None

    def validate_service(self, service: ServiceRef) -> None: ...
    def validate_entities(self, entity_ids: tuple[str, ...]) -> None: ...
    async def read_state(self, hass, service, entity_ids) -> dict[str, object]: ...
    async def apply_command(self, hass, service, entity_ids, payload) -> None: ...
```

四条硬规则：

1. **contract 只吸收语义相同的差异**（枚举值、量程、步长、方向）。用配置把不同语义
   塞进同一个契约项是不允许的。
2. **HA 的调用方式留在 Python 里**。`contract` 不描述「调哪个服务」。
3. **不猜值**。未映射的云端值、不在量程内的读数，一律跳过并只告警一次，绝不透传，
   也绝不从别的字段推断。
4. **只读服务也实现 `apply_command`**，在里面做校验然后返回，保证命令路径不抛异常。

## 新增一个适配器

1. 在 `business/adapters/` 建 `<service_id>.py`，复制一个形态接近的现有适配器
   （只读标量 → `luminance.py`；枚举 → `status.py`；开合 → `opener.py`）。
2. 模块 docstring 里写清：默认契约来源（prodId + Profile 链接）、常见性、
   `已验证 / candidate / 未验证`、`contract` 每个键的含义。
3. 在 `business/adapters/registry.py` 里导入并登记。可选别名（例如
   `switch1/2/3`、`leftAction`）也在那里加。
4. 在 `strings.json` 与 `translations/zh-Hans.json` 的
   `config_subentries.child.step.child_entities.data` 里加 `entity_<sid>` 标签。
5. 在 `tests/test_adapters.py` 加用例：量程边界、契约校验、idle 行为、命令忽略路径。

## 验收（五步）

一个适配器只有走完这五步才算 `已验证`：

1. **单元**：`python -m unittest discover -s tests -t .` 全绿。
2. **包装**：用目标 Products 的 `prodId` 建一个自定义子设备，能成功 `batchBind`。
3. **上报**：在 App 里看到该服务的数据，且 `dataSync` 返回 `errcode=0`；
   HA 日志中没有 `unhandled value`。
4. **下发**：从 App 操作一次，HA 实体状态按预期变化；反向再操作一次 HA，App 同步。
5. **长期**：至少跑过一轮断线重连与 HA 重启，服务不丢、不重复注册。

未走完的步骤要在 docstring 里明确标成 `candidate` 或 `未验证`，
不要因为「字段对得上」就写成已验证。

## 常见坑

- **姿态/方向**：`opener` / `openLevel` 的 `invert` 必须以物理方向实测为准，
  不要按 Profile 的 desc 字面推断。
- **空 subProdId**：`known_fields_only: true` 时 `devInfo` 不发 `subProdId` 与 `setupType`，
  否则云端会以 15013 拒绝注册。
- **枚举越界**：云端收到未声明的枚举值会把**整个服务**丢掉（App 里该卡片整体消失），
  所以宁可不上报。
- **只读字段**：Profile 标 `R` 的字段收到写命令时静默忽略，不要报错。