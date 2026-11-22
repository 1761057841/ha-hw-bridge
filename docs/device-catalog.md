# 华为智慧生活设备目录（ver_202609_hmos）

目录共 **5977** 条，可读物模型 **5926** 个。

当前集成可投影 **4410** 台设备，服务完全覆盖 **1091** 台。

> `DeviceId` = `prodId`；`profile` 指向 `DeviceId/DeviceId.json`。
> 「可投影」= 至少一个服务能映射到 HA；「完全覆盖」= 除系统服务（update/netInfo/timer 等）外全部覆盖。


## 已支持的服务（serviceType）

| serviceType | HA 实体 | 说明 |
|---|---|---|
| `switch` | switch / light / fan / climate | 开关、电源、摄像开关、静音 |
| `brightness` | light | 亮度 |
| `cct` | light | 色温 |
| `colour` | light | 颜色 |
| `temperature` | sensor | 温度 |
| `humidity` | sensor | 湿度 |
| `airDetector` | sensor ×2 | 温度+湿度 |
| `pm25` | sensor | PM2.5 |
| `hcho` | sensor | 甲醛 |
| `gas` | sensor | 燃气 |
| `battery` | sensor | 电量 |
| `luminance` | sensor | 照度 |
| `pir` | binary_sensor | 有人/无人 |
| `status` | sensor | 状态枚举 |
| `targetDistance` | sensor | 目标距离 |
| `alarm` | binary_sensor | 告警（摄像头按 field 分项） |
| `alarmBell` | binary_sensor | 压力告警 |
| `motor` | cover | 开合 |
| `opener` | cover | 开合 |
| `openLevel` | number | 开合百分比 |
| `mode` | select | 模式 |
| `fan` | select | 风速 |
| `gear` | select | 档位/灵敏度 |
| `modeSetting` | number | 检测参数 |
| `action` | button | 动作 |
| `cleanerRobot` | vacuum | 扫地机 |
| `filterElement` | sensor | 滤芯寿命 |
| `light` | light | 电器灯具 |
| `volume` | number | 音量 |
| `visitPoint` | button | 摄像头预置位 |

## 设备清单

| prodId | 名称 | 可投影服务 | 缺服务 |
|---|---|---|---|
| `2QTT` | 箭牌智能浴霸 Pro | Motion-activatedNightLightSwitch, autoDrySwitch, autoLightSwitch, autoWarmWindSwitch, automaticWarmWindSwitch, cct, deodorization, drySwitch, fan, heat, humidity, humanSensingStatus, indicator, keyToneSwitch, lightSwitch, luminance, nightLightSwitch, status, sterilizationSwitch, switch, ventilationFan, ventilateSwitch, windSwitch | circulationTime, leftTime, lightOffDelayTime, radarSensingGear, startDryThreshold, stopDryThreshold, commonFaultDetection |
| `2SHD` | 箭牌智能雷达人感浴霸2 Pro | Motion-activatedNightLightSwitch, autoDrySwitch, autoLightSwitch, autoWarmWindSwitch, automaticWarmWindSwitch, brightness, cct, drySwitch, fan, heat, humanSensingStatus, humidity, indicator, keyToneSwitch, lightSwitch, luminance, nightLightSwitch, status, sterilizationSwitch, switch, ventilateSwitch, ventilationFan, windSwitch | circulationTime, leftTime, lightOffDelayTime, radarSensingGear, startDryThreshold, stopDryThreshold, commonFaultDetection |
| `2REC` | 美的智能空调 鸿蒙空气机Pro | ECOswitch, aiFreshair, airCleangear, airClean, co2Switch, fan, favoriteModeSwitch, freshAirSpeed, freshAirSwitch, keepHumidity, humidity, keyToneSwitch, intelligentClean, mode, modePTC, mildewProofswitch, switch, sterilization, sleepCurveSwitch, status, switchScreen, temperature | airConditioner, co2, favoriteMode, filterElement, sleepCurve, commonFaultDetection |
| `A3SM` | 美的立柜式空调T6 | airClean, automaticAirswitch, airCleangear, airSterilizationSwitch, calmSpellSwitch, fan, freshAirSpeed, freshAirSwitch, humidity, healthFunctionSwitch, keyToneSwitch, mode, keepHumidity, light, mildewProofswitch, sceneMode, oneTouchFreshAir, switch, switchPTC, switchScreen, sterilization, temperature | TVOC, airConditioner, commonFaultDetection |
| `2S7J` | 创维热泵洗烘一体机Pro | action, ambientLighting, careClothesMode, childLockSwitch, dryDegree, fsReminder, fsStatus, keypressSound, ldReminder, ldStatus, mode, proceduralMemory, rotateSpeedGear, smartDetergentDispensing, status, switch, tempSettingMode, tsmartDispenseMode, uvSterilization, wakeupInduction, washClothesMode | alarmTime, leftTime, preTimeEnd, remoteControlService, rinseTimes, washTime, washmachine, commonFaultDetection, wFforgetuinesRetieval, wFexecuteAferComplton |
| `2SHE` | 箭牌智能雷达人感浴霸焕新版 Pro | Motion-activatedNightLightSwitch, autoLightSwitch, autoWarmWindSwitch, automaticWarmWindSwitch, brightness, drySwitch, fan, heat, humanSensingStatus, humidity, indicator, keyToneSwitch, lightSwitch, luminance, nightLightSwitch, status, sterilizationSwitch, switch, ventilateSwitch, ventilationFan, windSwitch | circulationTime, leftTime, lightOffDelayTime, radarSensingGear, commonFaultDetection |
| `2Q6W` | 箭牌智能浴霸 | Motion-activatedNightLightSwitch, drySwitch, autoLightSwitch, autoWarmWindSwitch, humidity, deodorization, fan, keyToneSwitch, heat, nightLightSwitch, humanSensingStatus, indicator, lightSwitch, luminance, status, sterilizationSwitch, switch, ventilationFan, ventilateSwitch, windSwitch | circulationTime, leftTime, lightOffDelayTime, commonFaultDetection |
| `2R8R` | 承弦智能开窗器Pro 内开窗款 | action, actionSwitch, alarm, battery, antipinchMode, antipinchSwitch, changeDirection, childLockSwitch, lightSwitch, mode, opener, openStatus, silencer, soundSwitch, stroke, switch, switchSpeed, torque, stroke2, voiceSwitch | travel, travel2, commonFaultDetection |
| `2RH5` | 奥普浴霸MC07-Pro-HW | action, autoDrySwitch, autoLightSwitch, autoWarmWindSwitch, automaticWarmWindSwitch, brightness, deodorization, drySwitch, heat, indicator, lightSwitch, lightingMode, nightLightSwitch, sensitivity, status, switch, ventilateGear, ventilateSwitch, windMode, windSwitch | deodorizationFilter, devCustomInfo, inductionCondition, setWorkTime, commonFaultDetection |
| `2RNH` | 海雀双雀Pro摄像头 | alarmEvent, alarmEvent2, cruiseSwitch, cruiseSwitch2, localMode, shootSwitch, switch, videoSwitch, visitPoint1, visitPoint10, visitPoint11, visitPoint12, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6, visitPoint7, visitPoint8, visitPoint9 | commonFaultDetection |
| `2RW0` | 承弦智能开窗器 内开窗款 | action, actionSwitch, alarm, antipinchMode, antipinchSwitch, battery, changeDirection, childLockSwitch, lightSwitch, mode, openStatus, opener, silencer, soundSwitch, stroke, stroke2, switch, switchSpeed, torque, voiceSwitch | travel, travel2, commonFaultDetection |
| `2RYD` | 创明左右分控智能窗帘 静音大师 | action, changeDirection, favorate, followMode, leftAction, mode, handpullMode, leftOpener, handpullSwitch, speed, indicator, rightAction, manualspeedControl, opener, remoteControl, reverse, rightOpener, stroke, sync, syncSwitch | routeRuntime, commonFaultDetection |
| `2SG9` | 宝贝第一智能儿童安全座椅 智悦 | ISOFIXAlarmSwitch, ISOFIXStatus, alarm, antiTipingLegsStatus, babyInStatus, battery, beltStatus, beltSwitch, childLockSwitch, currentTemperature, fixedTemperature, gear, noForget, position, powerSupply, seatTiltAction, supportLegsAlarmSwitch, touchSwitch, volumeGear, welcomeModeSwitch | seatRotation, welcomeDirection, commonFaultDetection, exceptionInfo |
| `2SHF` | 箭牌智能雷达人感浴霸焕新版 | Motion-activatedNightLightSwitch, autoLightSwitch, autoWarmWindSwitch, brightness, drySwitch, fan, heat, humanSensingStatus, humidity, indicator, keyToneSwitch, lightSwitch, luminance, nightLightSwitch, status, sterilizationSwitch, switch, ventilateSwitch, ventilationFan, windSwitch | circulationTime, leftTime, lightOffDelayTime, radarSensingGear, commonFaultDetection |
| `A3TY` | 美的壁挂式空调T6 | ECOswitch, airClean, airCleangear, airSterilizationSwitch, automaticAirswitch, calmSpellSwitch, fan, freshAirSpeed, freshAirSwitch, healthFunctionSwitch, humidity, keepHumidity, keyToneSwitch, mode, oneTouchFreshAir, sterilization, switch, switchPTC, switchScreen, temperature | airConditioner, commonFaultDetection |
| `2OVU` | 国恒G6智能按摩椅 | airbagGear, autoMode, armSwitch, bacAction, heatGear, action, gravityMode, lbpMode, legSwitch, manuMode, massageGear, massmode, movementAction, shoulderAction, shoulderSwitch, soleGear, waistSwitch, switch, status | countDown, massTime, workingMode |
| `2PON` | 海雀智能摄像头 双雀Max 128GB | alarmEvent2, alarmEvent, visitPoint4, visitPoint3, visitPoint2, visitPoint1, shootSwitch, visitPoint9, switch, visitPoint8, videoSwitch, visitPoint7, visitPoint6, visitPoint5, cruiseSwitch2, cruiseSwitch, visitPoint12, visitPoint11, visitPoint10 | — |
| `2POO` | 海雀智能摄像头 双雀Max 64GB | alarmEvent2, alarmEvent, visitPoint4, visitPoint3, visitPoint2, visitPoint1, shootSwitch, visitPoint9, switch, visitPoint8, videoSwitch, visitPoint7, visitPoint6, visitPoint5, cruiseSwitch2, cruiseSwitch, visitPoint12, visitPoint11, visitPoint10 | — |
| `2RVB` | 宝贝第一智能儿童安全座椅 灵智 | ISOFIXAlarmSwitch, ISOFIXStatus, antiTipingLegsStatus, babyInStatus, battery, beltStatus, beltSwitch, childLockSwitch, currentTemperature, fixedTemperature, gear, noForget, position, powerSupply, seatTiltAction, supportLegsAlarmSwitch, volumeGear, touchSwitch, welcomeModeSwitch | seatRotation, welcomeDirection, commonFaultDetection |
| `2S6B` | 美的热泵洗烘一体机Pro | action, childLockSwitch, doorStatus, dryDegree, fsReminder, fsStatus, ldReminder, ldStatus, rotateSpeedGear, lbStatus, stains, switch, tempSettingMode, mode, smartDetergentDispensing, status, steam, tsmartDispenseMode, waterLevel | alarmTime, electric, preTimeEnd, rinseTimes, nightModeSetting, spinTime, leftTime, remoteControlService, waterConsumption, washTime, voiceAssist, washmachine, commonFaultDetection, completedParam, cloudProgramMirroring, odorGuard |
| `2S6C` | 美的热泵洗烘一体机 | action, childLockSwitch, doorStatus, dryDegree, fsReminder, fsStatus, lbStatus, ldReminder, ldStatus, switch, mode, rotateSpeedGear, smartDetergentDispensing, stains, status, steam, tempSettingMode, tsmartDispenseMode, waterLevel | alarmTime, electric, leftTime, nightModeSetting, preTimeEnd, waterConsumption, remoteControlService, rinseTimes, spinTime, voiceAssist, washTime, washmachine, commonFaultDetection, odorGuard, completedParam, cloudProgramMirroring |
| `24G9` | 健身电踏车D1 | commonMode1, commonMode2, commonMode3, commonMode4, commonMode5, commonMode6, commonMode7, commonMode8, commonMode9, commonMode10, commonMode11, commonMode12, commonMode13, commonMode14, commonMode15, commonMode16, commonMode17, commonMode18 | commonMode19 |
| `2JU1` | 箭牌智能坐便器AKB1332-HM | toiletMode, seatStatus, windGear, autoFlushing, autoMagicBubble, foamshieldSwitch, moveWash, lightSense, seatRing, toiletStatus, bigflushSwitch, nozzlePos, stop, cleaningSwitch, waterGear, seatGear, filpSwitch, gear | service |
| `2M6F` | 调湿模块-6恒 | tvoc, drainSwitch, abilityMode, switch, mode, faultDetection, anionSwitch, pm25, temperature, elapsedTimeMode2, childLockSwitch, PromptSwitch, elapsedTimeMode1, status, humidity, gear, waterGear | filterElement1, filterElement2, wind, capability, cleaningTime, time |
| `2R8S` | 承弦智能开窗器Pro 外开窗款 | action, actionSwitch, alarm, antipinchMode, antipinchSwitch, battery, childLockSwitch, lightSwitch, mode, opener, silencer, soundSwitch, stroke, switch, switchSpeed, torque, voiceSwitch | travel, commonFaultDetection |
| `2RW1` | 承弦智能开窗器 外开窗款 | action, actionSwitch, alarm, antipinchMode, antipinchSwitch, battery, childLockSwitch, lightSwitch, mode, opener, silencer, soundSwitch, stroke, switch, switchSpeed, torque, voiceSwitch | travel, commonFaultDetection |
| `2MIW` | 九牧智能魔镜 | aromaSwitch, lightMode, aromatherapyGear, aromatherapyMode, aromatherapyStatus, brightness, cct, temperature, humidity, flavorMode, defoggingMode, nightLightSwitch, motionSensingStatus, lightSwitch, nightLightMode, status | defoggingThreshold, personalizedSignature, commonFaultDetection |
| `2NU5` | 极米神灯 Sunlight | controlMode, rest, keystonemanual, volSwitch, menu, setting, focusing, home, switch, return, volume, brightness, cct, lightSwitch, systemMode, light | ProjectorSwitch, relBrightness, RESTART, FOCUS, FOCUSRIGHT, FOCUSLEFT |
| `2O0P` | 瑞尔特电子坐便器FE3 | toiletMode, seatStatus, autoFlushing, windGear, autoMagicBubble, foamshieldSwitch, footFeel, bigflushSwitch, moveWash, smallflushSwitch, cleaningSwitch, nozzlePos, waterGear, seatGear, stop, gear | more, aspirate |
| `2OZI` | 承弦开窗器T1 | actionSwitch, torque, defenceSwitch, battery, stroke, soundSwitch, switch, changeDirection, silencer, switchSpeed, opener, handStartSwitch, alarm, action, childLockSwitch, lightSwitch | commonFaultDetection, travel |
| `2P3N` | 720智能空气净化器3s增强版 | mode, fan, humidity, keyToneSwitch, pm25, lightSwitch, UVSwitch, faultDetection, screenSwitch, temperature, childLockSwitch, hcho, anionSwitch, monitoringSwitch, workStatus, switch | ambientLight, outdoorPM25, filterElement1, cmw, cav, ecoSetting, airQuality, capabilitySet |
| `2P3O` | 720智能空气净化器3增强版 | mode, fan, humidity, keyToneSwitch, pm25, lightSwitch, UVSwitch, faultDetection, screenSwitch, childLockSwitch, temperature, workStatus, monitoringSwitch, hcho, anionSwitch, switch | outdoorPM25, ambientLight, filterElement1, cav, cmw, airQuality, ecoSetting, capabilitySet |
| `2QJD` | 奥普浴霸FX-Pro-HW | action, autoWarmWindSwitch, automaticWarmWindSwitch, fan, indicator, deodorization, drySwitch, lightSwitch, nightLightSwitch, status, temperature, ventilateGear, ventilateSwitch, ventilationFan, windMode, windSwitch | leftTime, commonFaultDetection |
| `2QYF` | 奥普浴霸F3-Pro-HW | action, autoWarmWindSwitch, automaticWarmWindSwitch, deodorization, drySwitch, fan, heat, indicator, lightSwitch, nightLightSwitch, sceneMode, status, ventilateGear, ventilateSwitch, windMode, windSwitch | leftTime, commonFaultDetection |
| `2R3A` | 美菱洗衣机LRS9G120DIZ | action, childLockSwitch, doorLockSwitch, mode, intelligentFabricSoftenerDispensing, preTimeEndMode, nursingModel, rotateSpeedGear, presetSwitch, status, tempSettingMode, stains, tsmartDispenseMode, switch, temperatureTracking, washDrySwitch | electric, leftTime, operationCycles, rinseTimes, spinTime, washTime, waterConsumption, waterQuality, weatherMonitor, commonFaultDetection |
| `2RBO` | MEIPONT 风神之眼 鸿蒙真新风空调 | aiFreshair, switch, mode, co2Switch, fan, freshAirSpeed, freshAirSwitch, favoriteModeSwitch, switchScreen, keyToneSwitch, switchPTC, sceneMode, modePTC, temperature, sleepCurveSwitch, status | co2, favoriteMode, filterElement, electric, runtime, sleepCurve, commonFaultDetection |
| `2S2Q` | 720智能空气净化器5 | UVSwitch, anionSwitch, childLockSwitch, fan, faultDetection, hcho, humidity, keyToneSwitch, lightSwitch, mode, monitoringSwitch, pm25, screenSwitch, switch, temperature, workStatus | airQuality, ambientLight, capabilitySet, cav, cmw, ecoSetting, filterElement1, outdoorPM25 |
| `2S7K` | 创维热泵洗烘一体机 | action, careClothesMode, childLockSwitch, dryDegree, fsReminder, fsStatus, ldReminder, ldStatus, mode, proceduralMemory, rotateSpeedGear, smartDetergentDispensing, status, switch, tempSettingMode, tsmartDispenseMode | alarmTime, leftTime, preTimeEnd, remoteControlService, rinseTimes, washTime, washmachine, commonFaultDetection, wFforgetuinesRetieval, wFexecuteAferComplton |
| `2SB0` | 奥普热能环双氧浴霸Q360T5-Pro-HW | action, autoDrySwitch, autoLightSwitch, autoWarmWindSwitch, automaticWarmWindSwitch, deodorization, drySwitch, heat, lightSwitch, nightLightSwitch, sensitivity, status, ventilateGear, windMode, ventilateSwitch, windSwitch | devCustomInfo, inductionCondition, setWorkTime, commonFaultDetection |
| `2SH5` | 奥普Smart人感双氧浴霸S5-Pro+-HW | action, autoLightSwitch, autoWarmWindSwitch, automaticWarmWindSwitch, deodorization, drySwitch, heat, lightSwitch, nightLightSwitch, status, sensitivity, swingSwitch, ventilateGear, ventilateSwitch, windMode, windSwitch | devCustomInfo, inductionCondition, setWorkTime, commonFaultDetection |
| `A3RO` | 美的立柜式空调T3 | automaticAirswitch, airClean, airCleangear, fan, freshAirSpeed, freshAirSwitch, humidity, keyToneSwitch, mode, keepHumidity, sceneMode, oneTouchFreshAir, switch, switchPTC, temperature, switchScreen | airConditioner, commonFaultDetection |
| `A3W3` | 美的壁挂式空调50GT3 | ECOswitch, airClean, airCleangear, automaticAirswitch, calmSpellSwitch, fan, fastColdheat, freshAirSpeed, freshAirSwitch, humidity, keepHumidity, mode, oneTouchFreshAir, switch, switchPTC, temperature | airConditioner, commonFaultDetection |
| `A3XN` | 美的壁挂式空调空气机T3II | ECOswitch, airClean, airCleangear, automaticAirswitch, fan, freshAirSpeed, freshAirSwitch, healthFunctionSwitch, humidity, keepHumidity, mode, oneTouchFreshAir, sceneMode, switch, switchPTC, temperature | airConditioner, commonFaultDetection |
| `2GFX` | 九牧i90智能马桶ZD8930 | toiletMode, seatStatus, windGear, faultDetection, smallflushSwitch, moveWash, bigflushSwitch, seatRing, toiletStatus, wideWash, waterGear, seatGear, stop, filpSwitch, setting | deviceAlarm, filterElement, tStatus, toiletGear, control |
| `2I0F` | 东鹏智能马桶W8481 | toiletMode, autoFlushing, seatStatus, footFeel, faultDetection, seatRing, lightSense, cleaningSwitch, nozzlePos, waterGear, seatGear, filpSwitch, gear, dryGear, switch | PowerSaving, Move |
| `2M1E` | 九牧X90智能马桶ZD9830 | toiletMode, seatStatus, windGear, faultDetection, bigflushSwitch, moveWash, smallflushSwitch, seatRing, toiletStatus, wideWash, waterGear, seatGear, stop, filpSwitch, setting | deviceAlarm, filterElement, control, tStatus, toiletGear |
| `2MDC` | 多合一空调新风地暖温控器(开关型) | heaterTemperature, freshAirSwitch, heatermintempSet, acTemperature, antifreezingMode, freshAirMode, deviceFormSetting, heatermaxtempSet, acmintempSet, heaterSwitch, acmaxtempSet, faultDetection, temperature, freshAirFan, airFan | airKey, capabilitySet |
| `2MXP` | 九牧i60s智能马桶ZD6540 | toiletMode, seatStatus, windGear, faultDetection, smallflushSwitch, moveWash, bigflushSwitch, seatRing, toiletStatus, wideWash, waterGear, seatGear, stop, filpSwitch, setting | deviceAlarm, filterElement, control, toiletGear, tStatus |
| `2N91` | 佳普乐Pro6s智能马桶 | toiletMode, seatStatus, windGear, cheaningGear, smallflushSwitch, bigflushSwitch, seatRing, cleaningSwitch, dryingSwitch, waterGear, seatGear, stop, hipNozzlePos, filpSwitch, Switch | UserMode, nightled |
| `2O5E` | 佳普乐Pro3s智能马桶 | toiletMode, seatStatus, windGear, cheaningGear, smallflushSwitch, bigflushSwitch, seatRing, cleaningSwitch, dryingSwitch, waterGear, seatGear, stop, hipNozzlePos, filpSwitch, Switch | nightled, UserMode |
| `2PD7` | IAM智能消毒空气净化器X5增强版 | mode, fan, anionSwitch, humidity, childLockSwitch, hcho, eleKillSwitch, screenSwitch, keyToneSwitch, lightSwitch, monitoringSwitch, pm25, temperature, tvoc, switch | allergen, ambientLight, dailyPurifiedAir, cav, outdoorPM25, weight, filterElement4, filterElement5, ecoSetting, filterElement6, filterElement7, filterElement8, airQuality, outdoorPM10, pm10, timerTaskId, commonFaultDetection |
| `2PRF` | 720智能空气净化器 铂境Pro Max | anionSwitch, childLockSwitch, fan, faultDetection, humidity, keyToneSwitch, hcho, mode, indicator, monitoringSwitch, temperature, pm25, screenSwitch, switch, tvoc | airQuality, allergen, capabilitySet, cav, filterElement1, fragrance, fragranceInstall, outdoorPM25, voiceBroadcast, weight |
| `2Q0J` | 美菱洗衣机LRS9H120DIZ | action, childLockSwitch, heatTimeMode, mode, intelligentFabricSoftenerDispensing, preTimeEndMode, nursingModel, rotateSpeedGear, presetSwitch, status, tempSettingMode, stains, tsmartDispenseMode, switch, temperatureTracking | electric, leftTime, operationCycles, rinseTimes, spinTime, washTime, waterConsumption, waterQuality, weatherMonitor, commonFaultDetection |
| `2QIE` | 奥佳华按摩椅OG8598X | action, airbagMode, autoMode, backAction, heatGear, heatMode, lbpMode, legAction, manuMode, manuskillSwitch, massmode, soleSwitch, status, switch, commonMode | countDown, hairSystemMode, massTime, setSystemMode, commonFaultDetection |
| `2QNG` | AI飞碟 | switch, mode, switch1, switch2, switch3, switch4, brightness, switch5, switch6, switch7, switch8, usbSwitch1, usbSwitch2, usbSwitch3, usbSwitch4 | — |
| `2QYJ` | 奥普Smart线性浴霸 L2A-Air-HW | action, autoDrySwitch, autoWarmWindSwitch, autoWindSwitch, automaticWarmWindSwitch, deodorization, drySwitch, heat, lightSwitch, sensitivity, status, ventilateGear, ventilateSwitch, windMode, windSwitch | devCustomInfo, inductionCondition, setWorkTime, commonFaultDetection |
| `2RAU` | 立达信智能护眼吸顶灯 光之骄子Pro 65W | switch, brightness, cct, auxBrightness, auxCct, auxSwitch, donotDisturb, inductionSwitch, lightMode, localVoice, mainBrightness, nightModeSet, mainCct, mainSwitch, commonMemorySwitch | lightFormulaArray, preview, progressTurnOff, progressTurnOn, relBrightness, commonFaultDetection |
| `2RAV` | 立达信智能护眼吸顶灯 光之骄子Pro 85W | switch, brightness, cct, auxBrightness, auxCct, auxSwitch, donotDisturb, inductionSwitch, lightMode, mainBrightness, localVoice, nightModeSet, mainCct, mainSwitch, commonMemorySwitch | lightFormulaArray, preview, progressTurnOff, progressTurnOn, relBrightness, commonFaultDetection |
| `2RU5` | 720智能空气净化器 铂境Pro | anionSwitch, childLockSwitch, fan, faultDetection, humidity, keyToneSwitch, hcho, mode, indicator, monitoringSwitch, temperature, pm25, screenSwitch, switch, tvoc | airQuality, allergen, capabilitySet, cav, filterElement1, fragrance, fragranceInstall, outdoorPM25, weight |
| `2RVJ` | 箭牌洁净大师P60 Ultra | autoFlip, bigflushSwitch, hipNozzlePos, lightSwitcht, nightLight, offSeatAction, seatRing, seatStatus, smallflushSwitch, stop, toiletMode, toiletSeatCoverSwitch, toiletStatus, toiletSelfCleanSwitch, wideWashingRange | drySetting, favorite, filterElement, foamShield, seatHeating, toiletSelfClean, toiletSetting, washSetting, commonFaultDetection |
| `2RVR` | 奥普Smart线性浴霸GL21-Pro+-HW | action, autoDrySwitch, autoWarmWindSwitch, autoWindSwitch, automaticWarmWindSwitch, deodorization, drySwitch, heat, lightSwitch, sensitivity, status, ventilateGear, ventilateSwitch, windMode, windSwitch | devCustomInfo, inductionCondition, setWorkTime, commonFaultDetection |
| `2RWZ` | 奥普奥芯线性浴霸GL22-Pro+-HW | action, aircleanSwitch, autoDrySwitch, autoLightSwitch, autoWarmWindSwitch, automaticWarmWindSwitch, deodorization, drySwitch, heat, lightSwitch, status, ventilateGear, windMode, ventilateSwitch, windSwitch | devCustomInfo, setWorkTime, commonFaultDetection |
| `2SAX` | 奥普Smart线性浴霸L3B-Pro+-HW | action, autoDrySwitch, autoWarmWindSwitch, autoWindSwitch, automaticWarmWindSwitch, deodorization, drySwitch, heat, lightSwitch, sensitivity, status, ventilateGear, ventilateSwitch, windMode, windSwitch | devCustomInfo, inductionCondition, setWorkTime, commonFaultDetection |
| `A30G` | 箭牌健康检测马桶AKB1621-AHM | toiletMode, seatStatus, windGear, autoFlushing, moveWash, bigflushSwitch, toiletStatus, cleaningSwitch, nozzlePos, dryingSwitch, waterGear, seatGear, stop, gear, nightLight | favorite, massageClean, Urinalysis, getData |
| `A3W5` | 美的壁挂式空调T5 | ECOswitch, airClean, airCleangear, automaticAirswitch, calmSpellSwitch, fan, freshAirSpeed, freshAirSwitch, humidity, keepHumidity, mode, oneTouchFreshAir, switch, switchPTC, temperature | airConditioner, commonFaultDetection |
| `A3X6` | 美的立柜式空调空气机T5 | ECOswitch, airClean, automaticAirswitch, airCleangear, freshAirSpeed, fan, freshAirSwitch, humidity, mode, keepHumidity, oneTouchFreshAir, switch, switchPTC, sterilization, temperature | airConditioner, commonFaultDetection |
| `2B8J` | 720 全效空气净化器 1Pro | switch, mode, childLockSwitch, UVSwitch, anionSwitch, pm25, fan, temperature, humidity, faultDetection, light, lightSensor, keytoneSwitch, screenSwitch | cav, cmw, filterElement1 |
| `2MFE` | 多合一空调新风地暖温控器(协议型) | heaterTemperature, freshAirSwitch, heatermintempSet, acTemperature, antifreezingMode, freshAirMode, heatermaxtempSet, deviceFormSetting, acmintempSet, faultDetection, heaterSwitch, acmaxtempSet, freshAirFan, temperature | capabilitySet, airKey, reboot |
| `2ND6` | 好孩子智能汽车安全座椅CS8100 | ISOFIXStatus, battery, antiTipingLegsStatus, babyInStatus, beltStatus, calibrationSwitch, currentTemperature, fanMode, fixedTemperature, seatTiltAction, fixedTemperatureWind, noForget, horizontalTurnStatus, conttonpadStatus | welcomeDirection, seatRotation |
| `2NGC` | 720智能空气净化除湿一体机 | dehumidifyswitch, UVSwitch, mode, faultDetection, fan, temperature, childLockSwitch, humidity, battery, pm25, anionSwitch, lightSwitch, monitoringSwitch, switch | waterTank, cav, weight, ambientLight, filterElement1, dehumidify, airQuality, city, stbyMonitor, userInformations, continueDehumidifySwitch, userFunctions |
| `2NH2` | 松下空气净化器 | UVSwitch, mode, switch, fan, faultDetection, humidity, childLockSwitch, elapsedTimeMode, tvoc, hcho, pm25, darkSwitch, anionSwitch, temperature | filterElement6, filterElement7, TVOCsensitivity, HCHOsensitivity, sensorsensitivity |
| `2O8B` | 集控器 | acmaxtempSet, acmintempSet, chilledWaterSystemSwitch, fan, freshAirSwitch, freshAirmode, humidification, humidity, mode, outhomeSwitch, sceneMode, selfCleanswitch, switch, temperature | capabilityset, fault, filterElement, sensorsAirParam, windSpeedEx, commonFilterElement1 |
| `2OBL` | 松下空气净化器 F-PDY150C | UVSwitch, switch, mode, fan, faultDetection, humidity, childLockSwitch, elapsedTimeMode, tvoc, hcho, pm25, darkSwitch, anionSwitch, temperature | filterElement6, filterElement7, TVOCsensitivity, sensorsensitivity, HCHOsensitivity |
| `2ODE` | 松下空气净化器 F-PTY900C | UVSwitch, mode, switch, fan, faultDetection, humidity, temperature, childLockSwitch, elapsedTimeMode, tvoc, hcho, pm25, darkSwitch, anionSwitch | filterElement6, filterElement7, TVOCsensitivity, sensorsensitivity, HCHOsensitivity |
| `2OY9` | 杜亚智能开窗器 外开窗款 | actionSwitch, torque, battery, stroke, soundSwitch, mode, switch, silencer, switchSpeed, opener, action, childLockSwitch, lightSwitch, voiceSwitch | commonFaultDetection, travel |
| `2PHY` | 海雀智能摄像头 雀蛋Max 64GB | alarmEvent, visitPoint4, visitPoint3, visitPoint2, visitPoint1, localMode, strangerFaceAlarm, shootSwitch, switch, visitPoint6, videoSwitch, visitPoint5, cruiseSwitch, familiarFaceAlarm | funRecord |
| `2QYG` | 奥普浴霸Q360T5S-Air-HW | action, autoDrySwitch, autoLightSwitch, autoWarmWindSwitch, deodorization, drySwitch, heat, lightSwitch, nightLightSwitch, status, ventilateGear, ventilateSwitch, windMode, windSwitch | leftTime, commonFaultDetection |
| `2QYH` | 奥普浴霸MR007-HW | action, autoWarmWindSwitch, deodorization, drySwitch, heat, lightSwitch, lightingMode, nightLightSwitch, status, swingSwitch, ventilateGear, ventilateSwitch, windMode, windSwitch | leftTime, nightLightDelay, setWorkTime, commonFaultDetection |
| `2RNN` | 亚都空气净化器KJ520F-S520 | UVSwitch, anionSwitch, childLockSwitch, colourMode, fan, faultDetection, hcho, humidity, indicator, mode, keyToneSwitch, pm25, temperature, switch | filterElement6, preciseTvoc, timerTaskId |
| `2RNV` | 美菱干衣机100BI | action, childLockSwitch, doorLockSwitch, dryMode, mode, nursingMode, presetSwitch, silentSwitch, steamSwitch, sterilize, status, switch, washerDryerLinkage, washingMachineStatus | electric, heatTime, leftTime, preTimeEnd, operationCycles, preTimeStart, commonFaultDetection |
| `2ROD` | 路福梦享家Link9Pro | angleControl, backControl, backMassage, childLockSwitch, headControl, legControl, lieControl, lightSwitch, massageGear, massageMode, memoryControl4, memoryControl6, modeSelect, oneKeyMassage | rightWarmBedTime |
| `2RQO` | 立达信智能护眼吸顶灯 光之骄子标准款 | auxBrightness, auxCct, auxSwitch, brightness, cct, inchingSwitch, lightMode, localVoice, mainBrightness, mainCct, mainSwitch, nightModeSet, switch, commonMemorySwitch | lightFormulaArray, preview, progressTurnOff, progressTurnOn, relBrightness, commonFaultDetection |
| `2RVI` | 箭牌洁净大师P60 Pro | bigflushSwitch, hipNozzlePos, indicator, nightLight, offSeatAction, seatRing, seatStatus, smallflushSwitch, stop, toiletMode, toiletSeatCoverSwitch, toiletSelfCleanSwitch, toiletStatus, wideWashingRange | drySetting, favorite, filterElement, foamShield, seatHeating, toiletSelfClean, toiletSetting, washSetting, commonFaultDetection |
| `A3KX` | 林内燃气壁挂炉RG68系列 | antifreezeStatus, bathTemperature, faultDetection, flameStatus, heatSwitch, heatTemperature, heatingImmediatelySwitch, hotWaterSwitch, instantHeatSwitch, mode, switch, usuallyReservationSwitch, zeroColdMode, zeroColdSwitch | — |
| `A3MZ` | TCL 挂式空调 好空气版 | ECOswitch, calmSpellSwitch, co2Switch, freshAirSwitch, fan, keyToneSwitch, light, freshAirSpeed, mode, switch, switchPTC, temperature, softWindSwitch, switchScreen | commonFaultDetection |
| `A3OL` | TCL 柜式空调 好空气版 | automaticAirswitch, calmSpellSwitch, exAirSwitch, fan, freshAirSpeed, freshAirSwitch, keyToneSwitch, light, mode, selfCleanswitch, softWindSwitch, switch, switchPTC, temperature | commonFaultDetection |
| `ZG2K` | 智能开关 6键 | switch1, switch2, switch3, mode1, mode2, mode3, mode4, mode5, mode6, backlight, brightness, childLockSwitch, faultDetection, memorySwitch | button1, button2, button3, button4, button5, button6, reboot |
| `2CXF` | ANBUmini筋膜枪 | commonMode1, commonMode2, commonMode3, commonMode4, commonMode5, commonMode6, commonMode7, commonMode8, commonMode9, commonMode10, commonMode11, commonMode12, commonMode13 | — |
| `2D79` | LATITmini筋膜枪 | commonMode1, commonMode2, commonMode3, commonMode4, commonMode5, commonMode6, commonMode7, commonMode8, commonMode9, commonMode10, commonMode11, commonMode12, commonMode13 | — |
| `2FAR` | 协议新风 | controlStrategy, fan, pm25, faultDetection, dhswitch, temperature, humidity, mode, queryAction, status, supportDerVirtual, tvoc, switch | capabilityset, capability, co2, filterElement5, filterElement6, filterElement7, filterElement8, filterElement4, filterElement1, filterElement2, filterElement3, windSpeedEx |
| `2I0H` | 东鹏智能马桶W8491 | seatStatus, nozzlePos, faultDetection, moveWash, smallflushSwitch, bigflushSwitch, seatRing, lightSense, toiletStatus, cleaningSwitch, waterGear, seatGear, filpSwitch | AnionSwitch, Clean, Featured, Windtemp, watergage |
| `2JN5` | 720智能空气净化器 3s | UVSwitch, switch, mode, fan, faultDetection, childLockSwitch, humidity, pm25, anionSwitch, temperature, keytoneSwitch, screenSwitch, tvoc | cmw, cav, filterElement1, timerParaValue, stbyMonitor, restoreFactory |
| `2K16` | 箭牌智能坐便器AKB2130H-HM | toiletMode, seatStatus, autoFlushing, autoFlip, moveWash, seatRing, toiletStatus, lightSense, nozzlePos, toiletFlush, toiletTemperature, gear, stop | Wclean, pulseMassage, userMode |
| `2L8O` | 九牧JD174S多功能取暖器 | drySwitch, warmWindMode, odorsensingSwitch, temperature, humidity, windSwitch, swingSwitch, nightLightSwitch, ventilateSwitch, standbySwitch, lightSwitch, aircleanSwitch, status | airQualityGrade, ArefactionEnable, ArefactionSwitch, timePara, sleepSwitch, faultEvent |
| `2M9Q` | 科勒星朗智能座便器 | toiletMode, seatStatus, autoFlushing, autoFlip, bigflushSwitch, lightSense, seatRing, uvSwitch, toiletStatus, cleaningSwitch, seatGear, stop, filpSwitch | deviceAlarm, FrontWashSettings, RearWashSettings, longseat, FunctionSettings, HostInformation |
| `2N7A` | 九牧i30s智能马桶ZD6330 | toiletMode, seatStatus, windGear, faultDetection, smallflushSwitch, moveWash, bigflushSwitch, toiletStatus, wideWash, waterGear, seatGear, stop, setting | deviceAlarm, tStatus, toiletGear |
| `2OQL` | 智能马桶盖 | toiletMode, seatStatus, windGear, foamshieldSwitch, moveWash, lightSense, cleaningSwitch, nozzlePos, waterGear, seatGear, stop, gear, massage | more |
| `2OQO` | 希影智能投影仪Play10 | contFocus, controlMode, volSwitch, focusing, menu, home, setting, displaySwitch, volume, return, focusauto, powerSwitch, systemMode | countdown |
| `2OYJ` | 承弦开窗器P1 | actionSwitch, torque, battery, stroke, soundSwitch, mode, switch, silencer, switchSpeed, opener, action, childLockSwitch, lightSwitch | commonFaultDetection, travel |
| `2OZJ` | 承弦开窗器X1 | actionSwitch, torque, battery, stroke, soundSwitch, mode, switch, silencer, switchSpeed, opener, action, childLockSwitch, lightSwitch | commonFaultDetection, travel |
| `2PWM` | 华帝小恒星燃气热水器 | boostMode, cleanSwitch, ecoSwitch, flameStatus, gasElectricDoubleBreakSwitch, zeroColdSwitch, inchingSwitch, increaseCapacitySwitch, maintenanceStatus, status, switch, temperature, zeroColdTemperature | cleanCountdown, curGasCon, curWaterVol, recircTempTime, totalGas, totalWater, zeroColdTime, commonFaultDetection, allDayRecircTempSwitch, circulatingTemp, scheduledCold |
| `2Q24` | THINCO智能落地灯Pro | switch, brightness, auxBrightness, auxSecBrightness, auxSecSwitch, auxSwitch, childLockSwitch, cct, lightMode, lightAdaptionSwitch, mainBrightness, mainSwitch, nightModeSet | intelligentDimming, longTimeAlarm, lightFormulaArray, preLightFormulaArray, preview, remoteControlSearch, remoteControlStatus, progressTurnOn, remoteCtrlInfo, remoteCtrlMetering, remoteCtrlType, spectralData, seatOffLightSet, seatOnLightSet, strobeData, timeSync, usageRecord |
| `2Q8G` | 酷开空调KFR-35GWNAAA-N1 | calmSpellSwitch, exAirSwitch, fan, freshAirSwitch, keyToneSwitch, light, mode, sceneMode, softWindSwitch, sterilization, switch, switchPTC, temperature | — |
| `2Q8M` | 迈睿人体存在传感器Pro 电池版 | action, battery, checkResult, detectionPara, deviceSwitch, envNoiseMgmt, indicator, ledSwitch, pir, luminance, selfCheck, sensitivity, targetDistance | delayTime |
| `2QH9` | IAM智能净水器 鲲泽三合一 | waterOutletType, cycleSwitch, ecoMode, faultDetection, emptySwitch, temperature, childLockSwitch, rinseMode, noMoreOvernightWater, tempMode, status, refluxSwitch, water | city, inputTds, filterElement1, outputTds, filterElement2, machinePara |
| `2QQ4` | IAM智能消毒空气净化器X5 Ultra免换芯 | childLockSwitch, fan, hcho, humidity, keyToneSwitch, lightSwitch, mode, monitoringSwitch, pm25, screenSwitch, temperature, switch, tvoc | airQuality, allergen, ambientLight, cav, dailyPurifiedAir, ecoSetting, filterElement4, filterElement6, filterElement7, filterElement8, outdoorPM10, outdoorPM25, pm10, timerTaskId, weight, commonFaultDetection |
| `2QWL` | 佳普乐致慕智能浴霸 | action, autoWarmWindSwitch, drySwitch, fan, heat, keyToneSwitch, lightSwitch, nightLightSwitch, sceneMode, swingSwitch, timeGear, windSwitch, ventilateSwitch | circulationTime, devCustomInfo, inductionCondition, setWorkTime, windTime |
| `2QXY` | 鸿智烤箱 | action, leftDoorStatus, leftStatus, status, leftTemperature, lefthotWindSwitch, lightSwitch, mode, rightMode, rightDoorStatus, rightStatus, rightTemperature, righthotWindSwitch | leftRecipes, leftWorkTime, leftTime, rightRecipes, rightLeftTime, rightWorkTime, commonFaultDetection |
| `2QYL` | 奥普浴霸L10B-Pro-HW | action, autoWarmWindSwitch, autoWindSwitch, deodorization, drySwitch, heat, lightSwitch, status, swingSwitch, ventilateGear, ventilateSwitch, windMode, windSwitch | circulationTime, leftTime, windTime, commonFaultDetection |
| `2R40` | 路福智能床Link9Max | headControl, legControl, lightSwitch, massGear, massageSwitch, massageMode, massageTimer, modeSelect, oneKeyReset, nightLight, sleepHelperSwitch, status, sleepstatus | audioPlayer, getMemoryMode, time, commonFaultDetection |
| `2R96` | 一起玩eachone  天境全色域淡彩风扇灯 | brightness, lightMode, cct, fanMode, switch, fan, colour, switchFan, inchingSwitch, colourMode, onOffBeep, verticalSwitch, commonMemorySwitch | progressTurnOff, nightWakeup, progressSwitch, progressTurnOn |
| `2RJB` | 迈睿人体存在传感器 电池版 | action, battery, checkResult, detectionPara, deviceSwitch, envNoiseMgmt, indicator, ledSwitch, luminance, pir, selfCheck, sensitivity, targetDistance | delayTime |
| `2RK1` | 美的智能空调 鸿蒙全面风Pro | ECOswitch, fan, favoriteModeSwitch, intelligentClean, keyToneSwitch, mildewProofswitch, mode, modePTC, switch, sterilization, status, switchScreen, temperature | favoriteMode, commonFaultDetection |
| `2RUD` | 奥普美容舱浴霸MRGC2-HW | action, autoWarmWindSwitch, deodorization, drySwitch, heat, lightSwitch, lightingMode, status, swingSwitch, ventilateGear, ventilateSwitch, windMode, windSwitch | leftTime, nightLightDelay, setWorkTime, commonFaultDetection |
| `2S48` | 华帝小恒星燃气热水器 Pro | boostMode, cleanSwitch, ecoSwitch, gasElectricDoubleBreakSwitch, zeroColdSwitch, inchingSwitch, flameStatus, increaseCapacitySwitch, maintenanceStatus, status, switch, temperature, zeroColdTemperature | cleanCountdown, curGasCon, curWaterVol, energySaving, recircTempTime, totalGas, totalWater, zeroColdTime, commonFaultDetection, allDayRecircTempSwitch, scheduledCold, circulatingTemp |
| `2S4E` | 志高 271 系列 | ECOswitch, calmSpellSwitch, co2Switch, exAirSwitch, exhaustAirSpeed, favoriteModeSwitch, keyToneSwitch, light, mode, selfCleanswitch, switch, switchPTC, temperature | preTime, commonFaultDetection |
| `2SF8` | 智风盒 | backlight, childLockSwitch, fanSwitch, indicator, mode, switch, switch1, switch2, switch3, switch4, switch5, switch6, switch7 | — |
| `2SPN` | 夏普除湿机DW-V16HZ-W | UVSwitch, anionSwitch, childLockSwitch, drainSwitch, fan, humidity, indicator, keyToneSwitch, lightSwitch, mode, status, switch, temperature | waterTank, commonFaultDetection |
| `A1K2` | 灶蒸烤烹饪机JZT/Y-ZK60-X3.i | powerSwitch, totalWaterShortageStatus, kitchenVentSwitch, kitchenVentStatus, kitchenVentilatorGear, kitchenVentLight, workBurnerStatus, cabinetSwitch, cabinetMode, cabinetStatus, SteamOvenSwitch, SteamOvenWorkStatus, SteamOvenMode | TemperatureSensor1, QuickWarm, TankPlace, DoorSwitch, PushRod, RemainingTime, compoundInstruction |
| `A3W2` | 美的壁挂式空调T2 | ECOswitch, airSterilizationSwitch, automaticAirswitch, calmSpellSwitch, fan, humidity, keepHumidity, mode, oneTouchFreshAir, softWindSwitch, switch, switchPTC, temperature | airConditioner, commonFaultDetection |
| `A3XY` | 美的立柜式空调空气机T3Z | ECOswitch, automaticAirswitch, airSterilizationSwitch, fan, humidity, mode, keepHumidity, sceneMode, oneTouchFreshAir, switch, switchPTC, temperature, sterilization | airConditioner, commonFaultDetection |
| `A3YS` | 美的立柜式空调空气机T2 | ECOswitch, automaticAirswitch, airSterilizationSwitch, fan, humidity, mode, keepHumidity, sceneMode, oneTouchFreshAir, switch, switchPTC, temperature, sterilization | airConditioner, commonFaultDetection |
| `2GEM` | 箭牌智能坐便器AKB1331-HM | toiletMode, seatStatus, autoFlushing, autoFlip, moveWash, lightSense, seatRing, toiletStatus, nozzlePos, stop, toiletTemperature, gear | toiletSwitch, userMode, pulseMassage, Wclean |
| `2HA1` | 星云11KW交流充电桩 | commonMode1, commonMode2, commonMode3, commonMode4, commonMode5, commonMode6, commonMode7, commonMode8, commonMode9, commonMode10, commonMode11, commonMode12 | — |
| `2I1N` | 梦百合0压智能床L7 | massageMode, oneKeyReset, memoryControl1, headMassage, modeSelect, sleepstatus, massageTimer, headControl, legControl, pause, legMassage, lightSwitch | GetMemoryMode, BedData, SleepReport, runningstate, instructions |
| `2I3Y` | 探梦者智能电动漂移鞋 | LEDLightcolour2, LEDLightcolour1, speed, battery1, battery2, deviceSelftest, LEDLight1, standbyTime, LEDLight2, status, reset, gear | lockMechanism, mileage, status2, Lowpoweralarm, instructions, status1 |
| `2J4H` | 星云7kW交流充电桩 | commonMode1, commonMode2, commonMode3, commonMode4, commonMode5, commonMode6, commonMode7, commonMode8, commonMode9, commonMode10, commonMode11, commonMode12 | — |
| `2LGN` | 720智能空气净化器 3 | UVSwitch, switch, mode, fan, faultDetection, humidity, childLockSwitch, hcho, pm25, anionSwitch, keytoneSwitch, screenSwitch | cmw, cav, filterElement1, stbyMonitor, userInformations, userFunctions, city |
| `2MD0` | 720智能空气净化加湿一体机 | aromaSwitch, mode, faultDetection, fan, childLockSwitch, temperature, humidity, pm25, anionSwitch, lightSwitch, monitoringSwitch, switch | airQuality, cav, weight, filterElement1, filterElement2, ambientLight, filterElement3, stbyMonitor, userFunctions, city, userInformations |
| `2MZN` | 小豚当家室外摄像头T5 3K双摄版 | alarmEvent, familiarFaceAlarm, shootSwitch, visitPoint4, visitPoint3, visitPoint2, visitPoint1, switch, strangerFaceAlarm, visitPoint6, visitPoint5, videoSwitch | pushStatus |
| `2N0E` | 西顿4路单色温0-10V调光器(PLC) | switch, faultDetection, brightness, colourMode, brightness4, brightness3, brightness2, brightness1, switch4, switch3, switch2, switch1 | relBrightness, outputMask, onSetting, fadeTimeSetting4, fadeTimeSetting3, fadeTimeSetting2, fadeTimeSetting1, lightCurveSetting4, lightCurveSetting3, lightCurveSetting2, lightCurveSetting1, fadeTime4, fadeTime3, fadeTime2, fadeTime1 |
| `2N0G` | 西顿8路开关执行器(PLC) | switch, faultDetection, brightness, colourMode, switch2, switch4, switch8, switch3, switch1, switch7, switch5, switch6 | outputMask, onSetting |
| `2NEY` | meipont空调柜机 | strong, temperature, faultDetection, ECOswitch, sleeping, switch, mode, selfCleanswitch, freshAirgear, sweepVertical, sweepHorizon, light | PtcHeat |
| `2NF2` | meipont空调柜机 | strong, temperature, faultDetection, ECOswitch, sleeping, switch, mode, selfCleanswitch, freshAirgear, sweepVertical, sweepHorizon, light | PtcHeat |
| `2NJN` | meipont空调挂机 | strong, temperature, faultDetection, ECOswitch, sleeping, switch, mode, selfCleanswitch, freshAirgear, sweepVertical, sweepHorizon, light | PtcHeat |
| `2NTH` | meipont空调柜机 | strong, temperature, faultDetection, ECOswitch, sleeping, switch, mode, selfCleanswitch, freshAirgear, sweepVertical, sweepHorizon, light | PtcHeat |
| `2NTI` | meipont空调挂机 | strong, temperature, faultDetection, ECOswitch, sleeping, switch, mode, selfCleanswitch, freshAirgear, sweepVertical, sweepHorizon, light | PtcHeat |
| `2OVZ` | 海越净届M7集成生态空气机 | UVSwitch, aromaHESwitch, mode, faultDetection, temperature, humidity, drainSwitch, hcho, pm25, darkSwitch, anionSwitch, switch | countdown, autoClean, airQuality, anion, percentcontrol |
| `2PUP` | 爱路德智能床GC888 | headControl, headLegControl, headMassage, legControl, legMassage, lightSwitch, massageMode, massageTimer, memoryControl1, memoryControl2, memoryControl3, oneKeyReset | positionFunction, stopWorking, timingSetting, devStatus, runingMode |
| `2Q6K` | 长虹智能空调 灵犀之眼 | ECOswitch, fan, humidity, keyToneSwitch, mode, sceneMode, selfClean, switchPTC, switchScreen, switch, temperature, temperatureHumidityDualControl | electric, runtime, commonFaultDetection |
| `2QHO` | 海雀智能摄像头 雀蛋Pro 128GB | alarmEvent, cruiseSwitch, localMode, shootSwitch, switch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 | commonFaultDetection |
| `2QHP` | 海雀智能摄像头 雀蛋Pro 64GB | alarmEvent, cruiseSwitch, localMode, shootSwitch, switch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 | commonFaultDetection |
| `2QM8` | 幸福星AI智能养生舱 | energyWaveSwitch, farInfraredSwitch, grapheneGear, hatchMode, massageGear, negativeOxygenIonSwitch, ozoneSwitch, padTemperature, status, suspendedSwitch, switch, volume | leftCountDown, workTime, commonFaultDetection |
| `2QM9` | 华愈康AI智能睡眠舱 | bioenergySwitch, cellularSwitch, controlAction, downLiveTemperature, downTemperature, hatchMode, lightGear, musicGear, status, suspendedSwitch, upLiveTemperature, upTemperature | bloodOxygen, heartRate, leftCountDown, commonFaultDetection |
| `2R4K` | 海雀智能摄像头5s | alarmEvent, cruiseSwitch, shootSwitch, strangerFaceAlarm, switch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 | commonFaultDetection |
| `2RDR` | MEIPONT 风神之眼 柜机 | fan, favoriteModeSwitch, keyToneSwitch, mode, modePTC, sceneMode, sterilization, status, switch, switchPTC, switchScreen, temperature | electric, favoriteMode, runtime, commonFaultDetection |
| `2RFH` | 海雀智能摄像头5 4K版 | alarmEvent, cruiseSwitch, localMode, shootSwitch, switch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 | commonFaultDetection |
| `2RJ1` | 海雀智能摄像头雀蛋 | alarmEvent, cruiseSwitch, localMode, shootSwitch, switch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 | commonFaultDetection |
| `2RQE` | AI智能健康舱 | energyWaveSwitch, farInfraredSwitch, grapheneGear, hatchMode, massageGear, negativeOxygenIonSwitch, ozoneSwitch, padTemperature, status, suspendedSwitch, switch, volume | leftCountDown, workTime, commonFaultDetection |
| `A3B2` | 林内燃气热水器 | boostMode, switch, mode, faultDetection, temperature, zeroColdMode, zeroColdSwitch, ecoSwitch, antifreezeStatus, flameStatus, status, commonMode1 | — |
| `A3MJ` | 美的挂机空调YC1 | ECOswitch, automaticAirswitch, fan, keyToneSwitch, mode, preventStraightWindswitch, sweepHorizon, sweepVertical, switch, switchPTC, switchScreen, temperature | commonFaultDetection |
| `A3N1` | 华帝智能燃气壁挂炉 | switch, aIWarmSwitch, bathTemperature, boostMode, faultDetection, heatStatus, heatTemperature, heatingImmediatelySwitch, mode, productModel, status, zeroColdSwitch | — |
| `A3ND` | 美的中央空调双出风SS | calmSpellSwitch, switch, mode, fan, temperature, humidity, light, sceneMode, automaticAirswitch, switchScreen, tempControlMode, waterAndFanValveMode | hvacType, commonFaultDetection |
| `ZG1Q` | 华为全屋智能 调光驱动器 5路 单色温 恒压 100W | faultDetection, memorySwitch, switch1, switch2, switch3, switch4, switch5, brightness1, brightness2, brightness3, brightness4, brightness5 | powerCon, relBrightness1, relBrightness2, relBrightness3, relBrightness4, relBrightness5, fadeTime1, fadeTime2, fadeTime3, fadeTime4, fadeTime5, lightCurveSetting1, lightCurveSetting2, lightCurveSetting3, lightCurveSetting4, lightCurveSetting5, fadeTimeSetting1, fadeTimeSetting2, fadeTimeSetting3, fadeTimeSetting4, fadeTimeSetting5, outputMask |
| `ZG1W` | 智能开关 4键 | switch1, switch2, switch3, mode1, mode2, mode3, mode4, backlight, brightness, childLockSwitch, faultDetection, memorySwitch | button1, button2, button3, button4, reboot |
| `ZG2V` | 智能开关 奥斯陆(无线版) 6键 | switch1, switch2, switch3, mode1, mode2, mode3, mode4, mode5, mode6, childLockSwitch, faultDetection, memorySwitch | button1, button2, button3, button4, button5, button6, reboot |
| `ZG31` | 智能开关 都灵 4键 | switch1, switch2, switch3, mode1, mode2, mode3, mode4, backlight, brightness, childLockSwitch, faultDetection, memorySwitch | button1, button2, button3, button4, reboot, theme |
| `208B` | 叶绿体自发电无线门铃WiFi版 | switch1, switch2, switch3, switch4, switch5, switch6, switch7, switch8, commonExecution1, commonExecution2, volume | info, pairState, muteOpServ, devStateServ, curOpServ, pairInfoServ, bellServ |
| `213Y` | 西顿一拖四调光模块 | switch, switch1, switch2, switch3, switch4, brightness, brightness1, brightness2, brightness3, brightness4, brightness5 | — |
| `25R1` | 小豚当家室外摄像头 | switch, shootSwitch, cruiseSwith, videoSwitch, alarmEvent, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 | pushStatus |
| `27NV` | 箭牌浴霸 | aromaSwitch, warmWindGear, temperature, switch, windSwitch, sterilizationSwitch, autoWarmWindSwitch, nightLightSwitch, ventilateSwitch, standbySwitch, status | — |
| `28H5` | Q9S蒸烤一体智能语音集成灶 | kitchenVentilatorGear, kitchenVentStatus, SteamOvenLight, workBurnerStatus, totalWaterShortageStatus, kitchenVentSteaming, powerSwitch, SteamOvenSwitch, kitchenVentLight, SteamOvenMode, SteamOvenWorkStatus | SteamOvenWorkTime, kitchenVentRemainingTime, worktem, closedelay, topheat |
| `29FN` | 箭牌智能坐便器AKB1315-HM | toiletMode, seatStatus, autoFlushing, autoFlip, lightSense, seatRing, toiletStatus, nozzlePos, toiletFlush, toiletTemperature, gear | userMode, pulseMassage |
| `2DO5` | 麦瑞克筋膜枪 | commonMode1, commonMode2, commonMode3, commonMode4, commonMode5, commonMode6, commonMode7, commonMode8, commonMode9, commonMode10, commonMode11 | — |
| `2FAT` | 协议空调 | airChangeGear, airChangeSwitch, switch, controlStrategy, faultDetection, fan, humidity, lightSwitch, mode, panelLocation, temperature | capabilityset, airConditioner, capability, filterElement, preTime, windSpeedEx |
| `2GOX` | 希影智能投影仪H9 Pro | volSwitch, menu, home, controlMode, setting, switch, volume, return, focusing, focusauto, contFocus | system, countdown |
| `2GPQ` | 希影智能投影仪H2 Pro | volSwitch, menu, home, controlMode, setting, switch, volume, return, focusing, focusauto, contFocus | system, countdown |
| `2GS8` | 华为智选 宝贝第一智能儿童安全座椅 智初 | fanSwitch, battery, powerSupply, beltSwitch, fixedTemperatureWind, alarm, babyInStatus, fixedTemperature, currentTemperature, fanMode, ISOFIXAlarmSwitch | — |
| `2HGE` | 仁豪家居智能按摩椅 | switch, soleSwitch, action, autoMode, manuMode, heatMode, ppmMode, lbpMode, massGear, backAction, intenGear | devStatus |
| `2ICD` | 海雀智能摄像头2S 3K版 | switch, shootSwitch, cruiseSwith, videoSwitch, alarmEvent, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 | — |
| `2J6E` | 路福梦享家link | oneKeyReset, memoryControl5, memoryControl4, memoryControl1, memoryControl3, memoryControl2, headControl, modeSelect, lightSwitch, legControl, massage | resetMemory, yogaNumber, massageTime, lieTime, massageMode1 |
| `2K0M` | 希影智能投影仪L12 Pro | controlMode, volSwitch, focusing, menu, home, setting, switch, volume, focusauto, return, contFocus | countdown, system |
| `2K0Q` | 希影智能投影仪L12 Mini | controlMode, volSwitch, focusing, menu, home, setting, switch, volume, focusauto, return, contFocus | countdown, system |
| `2KFV` | 小豚室外摄像头 | cruiseSwitch, alarmEvent, shootSwitch, visitPoint4, visitPoint3, visitPoint2, visitPoint1, switch, visitPoint6, visitPoint5, videoSwitch | pushStatus |
| `2LB6` | 希影智能投影仪L12 Max | controlMode, volSwitch, focusing, menu, home, setting, switch, volume, focusauto, return, contFocus | system, countdown |
| `2LHB` | 箭牌智能坐便器AKB1101-HM | toiletMode, seatStatus, autoFlushing, moveWash, lightSense, toiletStatus, nozzlePos, toiletTemperature, stop, gear, toiletFlush | service |
| `2LIK` | 小豚当家室外摄像头3K版 | switch, shootSwitch, cruiseSwith, videoSwitch, alarmEvent, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 | pushStatus |
| `2LOY` | 海雀智能摄像头3i 2.5K版 | cruiseSwitch, shootSwitch, alarmEvent, switch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 | — |
| `2LPA` | 海雀智能摄像头3 4K版 | shootSwitch, alarmEvent, visitPoint4, visitPoint3, visitPoint2, visitPoint1, switch, visitPoint6, visitPoint5, videoSwitch, cruiseSwitch | — |
| `2LPJ` | 海雀智能摄像头3S 3K版 | cruiseSwitch, shootSwitch, alarmEvent, switch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 | — |
| `2LRO` | 希影智能投影仪H9 Max | controlMode, volSwitch, focusing, menu, home, setting, switch, volume, focusauto, return, contFocus | countdown, system |
| `2M6T` | 小豚当家智能摄像头 2 | cruiseSwitch, alarmEvent, shootSwitch, visitPoint4, visitPoint3, visitPoint2, visitPoint1, switch, visitPoint6, visitPoint5, videoSwitch | pushStatus |
| `2MLE` | IAM智能净化加湿一体机U7 | aromaSwitch, mode, fan, faultDetection, temperature, childLockSwitch, humidity, pm25, lightSwitch, monitoringSwitch, switch | cav, weight, ambientLight, filterElement1, filterElement2, machinePara |
| `2MLY` | 奇立智能投影仪H6 Pro | controlMode, volSwitch, focusing, menu, home, setting, switch, volume, focusauto, return, contFocus | countdown, system |
| `2MQI` | 希影H9 Max家庭K歌影院 | controlMode, volSwitch, focusing, menu, home, setting, switch, volume, focusauto, return, contFocus | system, countdown |
| `2MQT` | 希影智能投影仪H9 Pro第二代 | controlMode, volSwitch, focusing, menu, home, setting, switch, volume, focusauto, return, contFocus | countdown, system |
| `2MTN` | 华为智选 海雀智能摄像头3 4K版 64GB | cruiseSwitch, alarmEvent, visitPoint4, visitPoint3, visitPoint2, visitPoint1, visitPoint6, shootSwitch, visitPoint5, switch, videoSwitch | — |
| `2MUI` | 鸿蒙智选 海雀智能摄像头3 4K版 128GB | alarmEvent, cruiseSwitch, visitPoint4, visitPoint3, visitPoint2, visitPoint1, shootSwitch, visitPoint6, visitPoint5, switch, videoSwitch | — |
| `2N0F` | 西顿2路双色温0-10V调光器(PLC) | switch, faultDetection, brightness, colourMode, mode, cct2, brightness2, cct1, brightness1, switch2, switch1 | relBrightness, outputMask, onSetting, fadeTimeSetting2, lightCurveSetting2, fadeTimeSetting1, lightCurveSetting1, fadeTime2, fadeTime1 |
| `2N20` | 极米RS 10 Ultra | controlMode, volSwitch, keystoneauto, focusing, menu, setting, focusauto, home, volume, systemMode, return | ProjectorSwitch, FOCUSRIGHT, KPPOWER, VOLUMEDOWN, RESTART, FOCUS, POWER, VOLUMEPRESS, FOCUSLEFT, VOLUMEUP |
| `2NC3` | 梦百合0压智能床M3pro | massageMode, oneKeyReset, memoryControl1, modeSelect, memoryControl2, massageTimer, headControl, legControl, pause, legMassage, alarm | GetMemoryMode, runningstate, Relievestress, Massageintensity, instructions |
| `2ND9` | 小豚当家智能摄像头2 双频版 | cruiseSwitch, alarmEvent, shootSwitch, visitPoint4, visitPoint3, visitPoint2, visitPoint1, switch, visitPoint6, visitPoint5, videoSwitch | pushStatus |
| `2NNI` | 新风 | fan, faultDetection, temperature, tvoc, dbswitch, humidity, mode, pm25, controlStrategy, supportDerVirtual, switch | co2, capabilityset, filterElement4, filterElement1, filterElement2, filterElement3, windSpeedEx |
| `2NPA` | 海雀智能摄像头3Pro 4K双频版 | cruiseSwitch, alarmEvent, shootSwitch, visitPoint4, visitPoint3, visitPoint2, visitPoint1, switch, visitPoint6, visitPoint5, videoSwitch | areaFencing, numberIdentification |
| `2NRE` | 智能控制器-通用 | mode, switch, fan, freshAirSwitch, faultDetection, sterilization, temperature, sceneMode, humidity, chilledWaterSystemSwitch, humidification | capabilityset, commonFilterElement1, filterElement |
| `2NV5` | 亚都空气净化器KJ2000F-T20(Hi) | UVSwitch, switch, mode, faultDetection, temperature, humidity, childLockSwitch, hcho, pm25, anionSwitch, light | filterElement6, level, screen, sound, timing |
| `2O91` | 小豚当家室外摄像头 3K升级版 | alarmEvent, cruiseSwitch, visitPoint4, visitPoint3, visitPoint2, visitPoint1, shootSwitch, visitPoint6, switch, visitPoint5, videoSwitch | pushStatus |
| `2OAJ` | 海雀智能摄像头3i 3K版 128GB | cruiseSwitch, alarmEvent, shootSwitch, visitPoint4, visitPoint3, visitPoint2, visitPoint1, switch, visitPoint6, visitPoint5, videoSwitch | — |
| `2OBE` | 海雀智能摄像头3i 3K版 32GB | cruiseSwitch, alarmEvent, shootSwitch, visitPoint4, visitPoint3, visitPoint2, visitPoint1, switch, visitPoint6, visitPoint5, videoSwitch | — |
| `2OGU` | IAM智能宠物空气净化器U7 Pro | mode, fan, faultDetection, keyToneSwitch, childLockSwitch, collectSwitch, tvoc, screenSwitch, pm25, monitoringSwitch, switch | allergen, dailyPurifiedAir, outdoorPM25, cav, weight, filterElement1, airQuality, capabilitySet, machinePara |
| `2OK6` | 海雀智能摄像头3s 4K版 32GB | cruiseSwitch, alarmEvent, shootSwitch, visitPoint4, visitPoint3, visitPoint2, visitPoint1, switch, visitPoint6, visitPoint5, videoSwitch | — |
| `2OKA` | 海雀智能摄像头3s 4K版 64GB | cruiseSwitch, alarmEvent, shootSwitch, visitPoint4, visitPoint3, visitPoint2, visitPoint1, switch, visitPoint6, visitPoint5, videoSwitch | — |
| `2OT9` | 佳普乐致臻智能浴霸 | drySwitch, warmWindMode, odorsensingSwitch, temperature, action, windSwitch, ventilateSwitch, nightLightSwitch, lightSwitch, status, commonExecution1 | WindTime, CirculationTime, UserMode, WarmWindTime |
| `2OXZ` | 海雀智能摄像头5i 3K版 32GB | alarmEvent, visitPoint4, visitPoint3, visitPoint2, visitPoint1, switch, visitPoint6, visitPoint5, videoSwitch, cruiseSwitch, shootSwitch | — |
| `2OY0` | 海雀智能摄像头5i 3K版 64GB | alarmEvent, visitPoint4, visitPoint3, visitPoint2, visitPoint1, switch, visitPoint6, visitPoint5, videoSwitch, cruiseSwitch, shootSwitch | — |
| `2OY2` | 海雀智能摄像头5i 3K版 128GB | alarmEvent, visitPoint4, visitPoint3, visitPoint2, visitPoint1, switch, visitPoint6, visitPoint5, videoSwitch, cruiseSwitch, shootSwitch | — |
| `2PI5` | 海雀智能摄像头 雀蛋Max 128GB | cruiseSwitch, alarmEvent, shootSwitch, visitPoint4, visitPoint3, visitPoint2, visitPoint1, switch, visitPoint6, visitPoint5, videoSwitch | — |
| `2PYH` | 希影智能投影仪RS 80 Ultra | contFocus, controlMode, volSwitch, focusing, menu, home, setting, volume, return, focusauto, systemMode | ProjectorSwitch, countdown |
| `2Q0B` | 正尚4路WiFi开关 | backlight, memorySwitch, switch, switch1, switch2, switch3, switch4, mode3, mode1, mode2, mode4 | Pair, CleanPair |
| `2Q6U` | 亚都空气净化器KJ850F-T850(Hi) | UVSwitch, anionSwitch, childLockSwitch, faultDetection, hcho, humidity, indicator, mode, pm25, temperature, switch | filterElement6, preciseTvoc |
| `2QMI` | 佳普乐腾韵智联浴缸 | ShowerHeadSwitch, bubbleBathSetting, childLockSwitch, colourMode, gear, knobFunctionSwitch, self-cleaningStatus, status, switch, temperature, waterGear | devCustomInfo, durationOfWaterInflow, commonFaultDetection |
| `2R9O` | 海雀智能摄像头5i 4K版 | alarmEvent, cruiseSwitch, shootSwitch, switch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 | commonFaultDetection |
| `2RAP` | 云居时代AI智能开关 | switch, brightness, mode, switch1, switch2, switch3, switch4, switch5, switch6, switch7, switch8 | — |
| `2RAY` | 求知2pro-HM儿童安全座椅 | babyInStatus, battery, conttonpadStatus, currentTemperature, fanSwitch, fixedTemperatureWind, heatSwitch, musicPlay, supportLegsAlarmSwitch, switch, temperatureAlarmSwitch | commonFaultDetection |
| `2RIT` | 飞利浦空调速铂 | ECOswitch, fan, favoriteModeSwitch, light, mildewProofswitch, mode, sterilization, switch, switchPTC, switchScreen, temperature | commonFaultDetection |
| `2RKX` | 慕思智能床Pro H-DESIGN | backControl, childLockSwitch, legControl, memoryControl1, modeSelect, nightLight, oneKeyReset, pause, sleepHelperSwitch, status, sleepstatus | foldAngles, getMemoryMode, leftAutoAdjust, leftSoftHardness, patService, privacyPolicy, snoringIntervention, rightSoftHardness, rightautoAdjust, commonFaultDetection |
| `2RXX` | 海雀智能摄像头5Pro 4K全场景版 | alarmEvent, cruiseSwitch, shootSwitch, switch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 | commonFaultDetection |
| `2RZA` | 海雀智能摄像头 雀蛋S | alarmEvent, visitPoint4, visitPoint3, visitPoint2, visitPoint1, shootSwitch, visitPoint6, switch, videoSwitch, visitPoint5, cruiseSwitch | commonFaultDetection |
| `2S7H` | 佳普乐致雅智能浴霸Pro | action, autoWarmWindSwitch, drySwitch, heat, lightSwitch, keyToneSwitch, nightLightSwitch, sceneMode, status, windSwitch, ventilateSwitch | circulationTime, devCustomInfo, setWorkTime, windTime, warmWindTime |
| `2SDJ` | 恩仕AXENT.META云控智能浴缸 | childLockSwitch, colourMode, constantTemperatureSwitch, heat, massageSwitch, mode, reminderSwitch, self-cleaningStatus, status, switch, waterGear | durationOfWaterInflow, commonFaultDetection |
| `2SHH` | 亚都加湿器SZ700-G1(Hi) | UVSwitch, anionSwitch, autoCleanSwitch, childLockSwitch, colourMode, gear, humidity, keyToneSwitch, status, switch, temperature | ambientLight, timerTaskId, commonFaultDetection |
| `2SMN` | 飞利浦空调E-M9 | ECOswitch, fan, favoriteModeSwitch, light, mildewProofswitch, mode, sterilization, switch, switchPTC, switchScreen, temperature | commonFaultDetection |
| `2SPT` | 夏普除湿机DW-V6NZ-C | anionSwitch, childLockSwitch, drainSwitch, fan, humidity, keyToneSwitch, lightSwitch, mode, status, switch, temperature | waterTank, commonFaultDetection |
| `A3DJ` | 壁挂炉 | boostMode, mode, aIWarmSwitch, zeroColdSwitch, faultDetection, heatingImmediatelySwitch, bathTemperature, sterilizationMode, bathMode, switch, heatTemperature | — |
| `A3HP` | COLMOEVO竖挂二代挂机空调 | calmSpellSwitch, fan, freshAirSpeed, freshAirSwitch, keyToneSwitch, mode, sceneMode, sterilization, switch, switchPTC, temperature | — |
| `A3HY` | 方太智能制冷油烟机 | acMode, acSwitch, fan, gear, lightSwitch, lockSwitch, midFanSwitch, status, temperature, switch, ventilationSwitch | — |
| `A3KO` | A.O.史密斯洗碗机 | action, auxiliarySwitch, lowerAreaswitch, lowerRegionStatus, mode, powder, rinse, status, statusDoor, switch, upperRegionStatus | leftTime, commonFaultDetection |
| `A3KW` | 林内燃气壁挂炉G58系列 | antifreezeStatus, bathTemperature, faultDetection, flameStatus, heatingImmediatelySwitch, heatSwitch, heatTemperature, hotWaterSwitch, mode, instantHeatSwitch, switch | — |
| `A3MG` | 美的柜机空调N8KS1(1P) | ECOswitch, automaticAirswitch, fan, mode, preventStraightWindswitch, sweepHorizon, sweepVertical, switch, switchPTC, switchScreen, temperature | commonFaultDetection |
| `A3PO` | 美的壁挂式空调M5 | ECOswitch, automaticAirswitch, fan, keyToneSwitch, light, mode, sleepCurveSwitch, switch, switchPTC, switchScreen, temperature | commonFaultDetection |
| `A3Q5` | TCL风管机 新风版 | calmSpellSwitch, fan, freshAirSpeed, freshAirSwitch, keyToneSwitch, light, mode, softWindSwitch, switch, switchPTC, temperature | — |
| `A3V9` | 箭牌智联浴霸AQW11838 | autoWarmWindSwitch, drySwitch, heat, lightSwitch, nightLightSwitch, sterilizationSwitch, swingSwitch, ventilateGear, ventilateSwitch, windMode, windSwitch | circulationTime |
| `A3Z4` | 箭牌智能浴缸独立款Pro | colourMode, constantTemperatureSwitch, drainSwitch, gear, heat, massageSwitch, mode, skirtEdgeAmbientLightSwitch, status, waterGear, waterInletSwitch | devCustomInfo |
| `A45A` | 美的智能浴霸(常规交流无人感) | action, autoWarmWindSwitch, brightness, drySwitch, heat, lightSwitch, nightLightSwitch, sceneMode, swingSwitch, ventilateSwitch, windSwitch | commonFaultDetection |
| `A485` | 美的立柜式空调无风感FA2 | ECOswitch, automaticAirswitch, calmSpellSwitch, fan, humidity, mode, sceneMode, oneTouchFreshAir, switch, switchPTC, temperature | commonFaultDetection |
| `ZG0D` | 智能开关 3键 | switch1, switch2, switch3, mode1, mode2, mode3, backlight, brightness, childLockSwitch, faultDetection, memorySwitch | button1, button2, button3, reboot |
| `ZG0E` | 智能面板 | backlight, brightness, childLockSwitch, luminance, faultDetection, switch1, switch2, switch3, temperature, memorySwitch, screenSwitch | button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, button13, button14, button15, button16, button17, button18, button19, button20, display, DNDmode, obstructionDetected, reboot |
| `ZG11` | 智能开关 3键 | switch1, switch2, switch3, mode1, mode2, mode3, backlight, brightness, childLockSwitch, faultDetection, memorySwitch | button1, button2, button3, reboot |
| `ZG1V` | 智能开关 3键 | switch1, switch2, switch3, mode1, mode2, mode3, backlight, brightness, childLockSwitch, faultDetection, memorySwitch | button1, button2, button3, reboot |
| `ZG2U` | 智能开关 奥斯陆(无线版) 4键 | switch1, switch2, switch3, mode1, mode2, mode3, mode4, modeX, childLockSwitch, faultDetection, memorySwitch | button1, button2, button3, button4, reboot |
| `201T` | 小豚当家AI全彩摄像头 双频版 | switch, shootSwitch, videoSwitch, alarmEvent, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 | secSwitch |
| `20Y2` | 永林一拖四调光驱动 | switch, switch1, switch2, switch3, switch4, brightness, brightness1, brightness2, brightness3, brightness4 | — |
| `24E7` | 鸿蒙智选 720 全效空气净化器 2 | switch, pm25, mode, fan, UVSwitch, anionSwitch, screenSwitch, keytoneSwitch, childLockSwitch, faultDetection | filterElement1, cav, cmw, stbyMonitor, playMode |
| `269M` | 西马智能马桶 | switch, mode, waterTemp, intensity, heatGear, dryGear, nozzlePosition, deodorizeSwitch, faultDetection, massage | sound, eco, longSeatOPT, flush, hipTime, longSeat, womenTime, onSeat, autoFlush, led |
| `29X0` | 720 全效空气净化器 E420 | switch, UVSwitch, childLockSwitch, mode, fan, faultDetection, pm25, anionSwitch, screenSwitch, keytoneSwitch | cmw, cav, ota, filterElement1, stbyMonitor, offPm25Value, onPm25Value |
| `2CXO` | 路福梦享家 | headControl, legControl, headLegControl, lieControl, memoryControl1, memoryControl2, memoryControl3, memoryControl4, lightSwitch, massage | massageMode1, jbxw, czjyw, nzjs, amdjs, tbxw, mszt |
| `2GY5` | 欧普暖芯浴霸 | drySwitch, fan, temperature, windSwitch, timeGear, sceneMode, ventilateSwitch, autoWarmWindSwitch, standbySwitch, lightSwitch | leftTime, commonFaultDetection |
| `2IU6` | 西蒙四位智能场景开关 | mode1, mode2, mode3, mode4, switch1, switch2, switch3, switch4, deviceStatus, indicator | sceneButton1, sceneButton2, sceneButton3, sceneButton4, commonFaultDetection |
| `2LKK` | 德国朗乐福智能床 Max II | massageMode, oneKeyReset, backControl, memoryControl1, massageTimer, modeSelect, memoryControl2, sleepstatus, legControl, lightSwitch | Massagearea, Massagegear, GetMemoryMode, runningstate, BedData, SleepReport, Modeloop, lumbarsupport |
| `2LYP` | 720智能空气净化器3Pro | UVSwitch, mode, fan, faultDetection, humidity, childLockSwitch, hcho, pm25, monitoringSwitch, switch | airQuality, cav, weight, filterElement1, filterElement2, city, allergen, stbyMonitor, userFunctions, userInformations, voc |
| `2M6R` | 松下语音浴霸照明款 | drySwitch, warmWindMode, fan, action, timeGear, lightingMode, sterilizationSwitch, ventilateSwitch, nightLightSwitch, status | leftTime, commonFaultDetection, windKindSet, coolDrySwitch, windDirectionSet |
| `2M6Z` | 松下隐蔽式浴霸 | drySwitch, warmWindMode, fan, odorsensingSwitch, action, timeGear, lightingMode, sterilizationSwitch, ventilateSwitch, status | leftTime, commonFaultDetection, gasCheckHas, speakerSet, coolDrySwitch, windKindSet, windDirectionSet |
| `2MA6` | 松下空气净化消毒机 | switch, mode, fan, faultDetection, humidity, childLockSwitch, elapsedTimeMode, tvoc, pm25, disinfect | filterElement6, filterElement7, capabilitySet |
| `2MGX` | 佳普乐致尚智能浴霸 | drySwitch, warmWindMode, temperature, windSwitch, swingSwitch, ventilateSwitch, nightLightSwitch, lightSwitch, status, commonExecution1 | WindDirection, DevAction, UserMode, CirculationTime, WindTime, WarmWindTime |
| `2MIC` | 松下智能除湿机 | tvoc, switch, mode, faultDetection, anionSwitch, pm25, PromptSwitch, elapsedTimeMode1, humidity, gear | filterElement1, filterElement2, wind |
| `2MPM` | 小崧空气净化循环扇KN-6397W | fanSwitch, UVSwitch, purgeGear, switch, mode, fan, childLockSwitch, fanMode, pm25, lightSwitch | filterElement6, pm10current, pm1current |
| `2MQS` | 希影智能投影仪L12 Pro第二代 | controlMode, volSwitch, focusing, menu, home, setting, volume, return, focusauto, contFocus | ProjectorSwitch, system, countdown |
| `2MWA` | 友邦浴霸X7 | warmWindMode, temperature, action, windSwitch, sceneMode, swingSwitch, ventilateSwitch, brightness, lightSwitch, aircleanSwitch | — |
| `2MXI` | 侧装红外人体移动光照传感器 | luminance, lightCct, lightBrightness, pir, switchNightLight, selfCheck, configureSwitch1, sensitivity, nightlightSwitch1, configureSwitch2 | delayTime, commonFaultDetection, timeSync |
| `2N52` | 侧装红外人体移动光照传感器 | luminance, lightCct, lightBrightness, pir, switchNightLight, configureSwitch1, selfCheck, nightlightSwitch1, configureSwitch2, sensitivity | delayTime, commonFaultDetection, timeSync |
| `2NNH` | 空调 | updateData, switch, mode, fan, faultDetection, humidity, panelLocation, controlStrategy, temperature, waterAndFanValveMode | capabilityset, filterElement, preTime, windSpeedEx |
| `2NPB` | 海雀智能摄像头3Pro 4K 双频版 | alarmEvent, shootSwitch, visitPoint4, visitPoint3, visitPoint2, visitPoint1, switch, visitPoint6, visitPoint5, videoSwitch | — |
| `2OHL` | 箭牌电子安全水阀 | battery, waterTemperature, waterUseData, maxFlow, proSwitch, singleWater, status, waterDaily, waterLeakage, waterTime | abnormalAlarm, flowVelocity, inputTds, waterPressure |
| `2OKB` | 海雀智能摄像头3s 4K版 128GB | alarmEvent, shootSwitch, visitPoint4, visitPoint3, visitPoint2, visitPoint1, switch, visitPoint6, visitPoint5, videoSwitch | — |
| `2OKP` | 当贝投影X5 Ultra | controlMode, volSwitch, setting, rest, volume, focusauto, menu, systemMode, home, return | ProjectorSwitch |
| `2OKQ` | 当贝投影D6X | controlMode, volSwitch, setting, rest, volume, menu, systemMode, home, focusauto, return | ProjectorSwitch |
| `2OQC` | 希影智能投影仪H9 UItra | controlMode, volSwitch, focusing, menu, home, setting, volume, return, focusauto, contFocus | ProjectorSwitch, countdown, system |
| `2OQN` | 希影智能投影仪H9 UItra家庭K歌影院 | controlMode, volSwitch, focusing, menu, home, setting, volume, return, focusauto, contFocus | ProjectorSwitch, system, countdown |
| `2OQR` | 希影智能投影仪H9 Max第三代 | controlMode, volSwitch, focusing, menu, home, setting, volume, focusauto, return, contFocus | ProjectorSwitch, countdown, system |
| `2OWH` | 小豚当家室外摄像头5 4K版 | alarmEvent, visitPoint4, visitPoint3, visitPoint2, visitPoint1, shootSwitch, visitPoint6, switch, visitPoint5, videoSwitch | commonFaultDetection, pushStatus |
| `2PDM` | SMUI敏升智能床 | childLockSwitch, headControl, headMassage, legControl, legMassage, massageMode, massageTimer, modeSelect, oneKeyReset, status | positionSelect, time |
| `2PDQ` | KLST克丽斯汀悬浮云端智能床 | massageMode, childLockSwitch, headMassage, massageTimer, headControl, legControl, modeSelect, legMassage, oneKeyReset, status | positionSelect, time |
| `2PEL` | JYMC智能双色灯HM1 | auxBrightness, lightMode, auxSwitch, brightness, donotDisturb, cct, mainSwitch, switch, commonMode, commonMemorySwitch | progressSwitch |
| `2Q23` | THINCO智能落地灯 | switch, brightness, auxBrightness, auxSwitch, childLockSwitch, lightMode, lightAdaptionSwitch, mainBrightness, mainSwitch, nightModeSet | intelligentDimming, longTimeAlarm, progressTurnOn, remoteControlSearch, remoteControlStatus, remoteCtrlInfo, remoteCtrlMetering, remoteCtrlType, seatOffLightSet, seatOnLightSet, spectralData, strobeData, timeSync, usageRecord |
| `2Q2T` | MEIPONT智能空调 风神之眼 | switch, fan, switchScreen, keyToneSwitch, favoriteModeSwitch, switchPTC, sceneMode, mode, temperature, status | favoriteMode, electric, runtime, preTime, commonFaultDetection |
| `2Q61` | 纽恩泰空气能热泵 | switch, mode, coolWaterTemp, sceneMode, heatWaterTemp, humidity, inletTemperature, outWaterTemp, targetTemp, temperature | electric, commonFaultDetection |
| `2QCU` | 小豚当家室外4G摄像头 3K版 | alarmEvent, shootSwitch, switch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 | commonFaultDetection |
| `2QEF` | 三诺智能语音开关 | backlight, brightness, changeDirection, discovery, memorySwitch, mode1, mode2, switch1, switch2, childLockSwitch | autoScene, batchCmd, bluetooth, bt, button1, button2, capacity, clickedScene, commonFaultDetection, communication, connectDev, devList, deviceLabel, group1, group10, group11, group12, group13, group14, group15, group16, group17, group18, group19, group2, group20, group21, group22, group23, group24, group25, group3, group4, group5, group6, group7, group8, group9, groupControl, groupManage, hiBeaconSync, homeGatewayCap, hwaccount, lightLevel, lightRing, localCommand, manualScene, microphone, msgRsp, nearbyWakeup, netReconnection, preWakeUp, quietMode, reboot, sceneManage, sceneOperation, smartspeaker, speaker, speakerAlarm, speakerIfttt, speakerState, switchMap, voiceAssist, voiceAssistDevInfo, wakeUp, wakeupVerifyMode, homeBroadcast, deviceType, logEvent |
| `2QGA` | 小豚当家智能摄像头 鲸瞳Max | alarmEvent, shootSwitch, switch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 | commonFaultDetection |
| `2QKO` | 易慧家推拉驱动 | action, changeDirection, closeSpeed, handStartSwitch, lightSwitch, opener, silencer, stroke, switchSpeed, torque | lockMechanism, lockType, travel, commonFaultDetection |
| `2QN4` | 慕思智能床Pro | backControl, childLockSwitch, legControl, memoryControl1, modeSelect, nightLight, oneKeyReset, pause, sleepHelperSwitch, status | foldAngles, getMemoryMode, leftSoftHardness, patService, privacyPolicy, rightSoftHardness, snoringIntervention, commonFaultDetection |
| `2QNC` | 亚都智能加湿器SC700-SK071Pro(Hi) | UVSwitch, childLockSwitch, colourMode, gear, humidity, keyToneSwitch, mode, status, switch, temperature | timerTaskId, commonFaultDetection |
| `2QSH` | 佳普乐致煦智能浴霸 | action, autoWarmWindSwitch, drySwitch, heat, keyToneSwitch, lightSwitch, nightLightSwitch, sceneMode, ventilateSwitch, windSwitch | circulationTime, devCustomInfo, setWorkTime, windTime |
| `2R3H` | IAM智能宠物空气净化器U7 | mode, faultDetection, keyToneSwitch, childLockSwitch, tvoc, fan, screenSwitch, pm25, monitoringSwitch, switch | allergen, dailyPurifiedAir, outdoorPM25, cav, weight, filterElement1, airQuality, capabilitySet, timerTaskId, machinePara |
| `2RBD` | 小豚当家智能摄像头 鲸瞳4G版 | alarmEvent, shootSwitch, switch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 | commonFaultDetection |
| `2RCW` | 暖通网关MC5 OS | faultDetection, coldheatSwitch, gatewayAction, operation, rs485Switch, commonMode1, commonMemorySwitch1, commonMemoryControl1, commonExecution1, commonTask1 | 485NetInfo, acGroupList, acList, automaticGroup, backup, backupData, capabilityset, connectMode, ctlCapability, delay, diagnose, diagnosis, freshAirGroupList, freshAirList, generalGrouplist, generalList, heaterGroupList, heaterList, heaterProtocol, homeGatewayCap, offlineOta, port1protocolList, port2protocolList, reboot, timeZone, vrvProtocol, commonFaultDetection, commonFilterElement1 |
| `2RL7` | 慕思智能床Pro1.5m | backControl, childLockSwitch, legControl, memoryControl1, modeSelect, nightLight, oneKeyReset, pause, sleepHelperSwitch, status | foldAngles, getMemoryMode, leftSoftHardness, patService, privacyPolicy, rightSoftHardness, snoringIntervention, commonFaultDetection |
| `2RRO` | 小豚当家智能摄像头 鲸瞳 | alarmEvent, shootSwitch, switch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 | commonFaultDetection |
| `2SB5` | 小豚当家智能摄像头6 4K | alarmEvent, shootSwitch, switch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 | commonFaultDetection |
| `2SB7` | 小豚当家智能摄像头6 Pro 双摄 | alarmEvent, shootSwitch, switch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 | commonFaultDetection |
| `2SBH` | 暖通网关MC5 Lite | coldheatSwitch, faultDetection, gatewayAction, operation, rs485Switch, commonMode1, commonMemorySwitch1, commonMemoryControl1, commonExecution1, commonTask1 | 485NetInfo, acGroupList, acList, automaticGroup, backup, backupData, capabilityset, connectMode, ctlCapability, delay, diagnose, diagnosis, freshAirGroupList, freshAirList, generalGrouplist, generalList, heaterGroupList, heaterList, heaterProtocol, homeGatewayCap, offlineOta, port1protocolList, port2protocolList, reboot, timeZone, vrvProtocol, commonFilterElement1 |
| `2SFS` | 豪恩空气质量检测仪LH 368WF | battery, co2Alarm, co2AlarmSwitch, hchoAlarm, hchoAlarmSwitch, humidity, indicator, screenMode, sleepMode, temperature | co2, environment, commonFaultDetection, lowPowerMode |
| `2SHI` | 亚都加湿器SZ500-Y1(Hi) | UVSwitch, autoCleanSwitch, childLockSwitch, colourMode, gear, humidity, keyToneSwitch, status, switch, temperature | timerTaskId, commonFaultDetection |
| `2SLC` | MEIPONT智能空调 | switch, fan, favoriteModeSwitch, switchScreen, keyToneSwitch, switchPTC, sceneMode, mode, temperature, status | favoriteMode, electric, runtime, preTime, commonFaultDetection |
| `A2ZP` | 美的焕新风挂机 | heat, selfCleanswitch, freshAirgear, preventStraightWindswitch, switch, mode, calmSpellSwitch, ECOswitch, fan, freshAirSwitch | batchCmd, commonFaultDetection, visualization |
| `A2ZQ` | 美的焕新风挂机 | heat, selfCleanswitch, freshAirgear, switch, preventStraightWindswitch, mode, calmSpellSwitch, fan, ECOswitch, freshAirSwitch | batchCmd, commonFaultDetection, visualization |
| `A2ZR` | 美的焕新风柜机 | heat, selfCleanswitch, freshAirgear, preventStraightWindswitch, switch, mode, calmSpellSwitch, fan, ECOswitch, freshAirSwitch | batchCmd, commonFaultDetection, visualization |
| `A3E1` | 美的新风风管机 | windGear, calmSpellSwitch, switch, mode, fan, freshAirSwitch, temperature, sceneMode, freshAirgear, automaticAirswitch | — |
| `A3EU` | 方太智能灶蒸烤烹饪机 | kitchenVentilatorGear, SteamOvenLight, workBurnerStatus, gestureSwitch, temperature, totalWaterShortageStatus, kitchenVentSteaming, powerSwitch, SteamOvenMode, SteamOvenWorkStatus | SteamOvenWorkTime, kitchenVentRemainingTime, commonFaultDetection |
| `A3H1` | COLMOEVO柜机空调 | automaticAirswitch, switch, mode, fan, freshAirSwitch, sterilization, temperature, sceneMode, freshAirgear, switchPTC | — |
| `A3I8` | 方太智能集烹中心 | action, childLockSwitch, gear, leftStoveStatus, lightSwitch, midStoveStatus, rightStoveStatus, status, switch, temperature | cookTime, delayOff, commonFaultDetection, OvenWorkState, smartGrill |
| `A3JM` | 美的加湿器SZK-1Y80 Pro | airDry, autoCleanSwitch, fan, humidity, indicator, keyToneSwitch, lightSwitch, mode, status, switch | waterTank, commonFaultDetection |
| `A3KI` | 美的真暖空气源热泵Z1 | ECOswitch, switch, mode, coolWaterTemp, temperature, heatWaterTemp, keyToneSwitch, light, targetTemp, tempControlMode | — |
| `A3MK` | 华凌挂机空调N8HA1III(P) | ECOswitch, automaticAirswitch, fan, mode, preventStraightWindswitch, sweepVertical, switch, switchPTC, switchScreen, temperature | commonFaultDetection |
| `A3NC` | 美的风管机双出风SS | switch, mode, fan, temperature, humidity, light, sceneMode, automaticAirswitch, switchScreen, tempControlMode | hvacType, commonFaultDetection |
| `A3QD` | COLMO新象中央空调(M)X2 | calmSpellSwitch, switch, mode, fan, temperature, humidity, light, sceneMode, automaticAirswitch, sterilization | hvacType, commonFaultDetection |
| `A3QE` | COLMO新象中央空调(C)X2 | calmSpellSwitch, switch, mode, fan, temperature, humidity, light, sceneMode, automaticAirswitch, sterilization | hvacType, commonFaultDetection |
| `A3SY` | 美的燃气壁挂炉尊享ML1II | aIWarmSwitch, bathStatus, bathTemperature, ecoSwitch, heatStatus, heatSwitch, heatTemperature, hotWaterSwitch, instantHeatSwitch, switch | hotWaterPressure, commonFaultDetection |
| `A3VQ` | 美的空气源热泵真暖MAX | ECOswitch, switch, mode, keyToneSwitch, inletTemperature, light, outWaterTemp, targetTemp, tempControlMode, temperature | hvacType, commonFaultDetection |
| `A3WP` | COLMO睿极风管机A3 | calmSpellSwitch, switch, mode, temperature, fan, humidity, sceneMode, sterilization, switchPTC, switchScreen | airConditioner, hvacType, commonFaultDetection |
| `A3Z3` | 箭牌智能浴缸裙边款Pro | colourMode, constantTemperatureSwitch, drainSwitch, gear, heat, massageSwitch, mode, status, waterGear, waterInletSwitch | devCustomInfo |
| `A41Q` | 美的壁挂式空调风尊3 | ECOswitch, automaticAirswitch, fan, fastColdheat, favoriteModeSwitch, humidity, mode, switch, switchPTC, temperature | airConditioner, commonFaultDetection |
| `A439` | 美的壁挂式空调全面风Q2 | ECOswitch, automaticAirswitch, fan, humidity, mode, oneTouchFreshAir, sceneMode, switch, switchPTC, temperature | airConditioner, commonFaultDetection |
| `ZG1L` | 华为鸿蒙智家 智能开关 蒙德里安 | backlight, brightness, faultDetection, switch1, switch2, switch3, mode1, mode2, mode3, mode4 | button1, button2, button3, button4, DNDmode |
| `1088` | 美尔凯特 Z7浴室音乐暖空调 | switch, lightSwitch, lightMode, mode, temperature, swing, gear, currentTemperature, faultDetection | workTime, musicSwitch, leftTime |
| `163K` | 水爱智能盖板 | switch, mode, faultDetection, temperature, ECO, deodorization, light, stop, buzzer | warmbraw, Water, windwarm, cleaning, waterIntensity, spraynozzlePosition, jetcleaner |
| `173P` | 康美太香薰机 | switch, aromaSwitch, lightSwitch, lightMode, colourMode, colourMode, brightness, colour, faultDetection | aromaMode, delay |
| `210E` | 欧派嵌入式智能烤箱 | status, mode, action, lightSwitch, temperature, faultDetection, openStatus, preheat, childLock | workTime, setWorkTime, leftTime, ProbeTargetTemp, atuoRecipe, waterTank, probe, setSteam |
| `2186` | 欧派嵌入式智能蒸箱 | lightSwitch, status, action, mode, lackWater, gateState, temperature, faultDetection, childLock | workTime, setWorkTime, leftTime, autoRecipe |
| `2188` |  | acSwitch, acTemperature, acMode, acFan, freshAirSwitch, freshAirFan, heaterSwitch, heaterTemperature, backlightMode | — |
| `218B` |  | acSwitch, acTemperature, acMode, acFan, freshAirSwitch, freshAirFan, heaterSwitch, heaterTemperature, backlightMode | — |
| `22DH` | 爱特嘉智能即热饮水吧 2 | status, commonMode, rinseMode, washingStatus, childLockSwitch, temperature, tdsStatus, switch, faultDetection | setUpWater, machineTemp, outlet, dataWater, inputTds, location, sensorMode |
| `27QC` | 0-10V单色温调光器 | switch1, switch2, switch3, switch4, brightness1, brightness2, brightness3, brightness4, faultDetection | fadeTime1, fadeTime2, fadeTime3, fadeTime4 |
| `27QD` | 开关执行器 | switch1, switch2, switch3, switch4, switch5, switch6, switch7, switch8, faultDetection | — |
| `29H9` | 华梦智能控制器 | switch, switch1, switch2, switch3, switch4, switch5, switch6, switch7, switch8 | switch12, switch11, switch10, switch9 |
| `29Q3` | 箭牌智能毛巾架AKM011-HM | switch, disinfect, fan, windSwitch, nightlightSwitch, swingSwitch, drying, sensingSwitch, status | dryingTime, ota |
| `2AMM` | 欧派智能坐便器 | mode, waterTemp, heatGear, dryGear, faultDetection, massageSwitch, position, flushSwitch, lightSwitch | reciprocateSwitch, waterPressure, autoFlushSwitch, energySavingSwitch |
| `2BH9` | 新颐空气净化器 | switch, mode, childLockSwitch, anionSwitch, pm25, fan, temperature, humidity, faultDetection | filterElement1, timercounter |
| `2C74` | 仁豪家居三人位功能沙发 | headControl, legControl, massageMode, modeSelect, memoryControl1, memoryControl2, memoryControl3, memoryControl4, childlock | memorytips |
| `2HUS` | 万和燃气热水器YL5 | boostMode, switch, mode, faultDetection, temperature, zeroColdMode, zeroColdSwitch, status, ECO | totalWater, totalGas, curGas, curWater, appointment, dingshi, pretemp |
| `2I43` | 万和燃气热水器ML1 | boostMode, switch, mode, faultDetection, temperature, zeroColdMode, zeroColdSwitch, status, ECO | totalWater, totalGas, curGas, curWater, dingshi, appointment, pretemp |
| `2IUI` | 雅兰云电动床N030 | massageMode, oneKeyReset, angleControl, headMassage, modeSelect, headLegControl, legControl, legMassage, lightSwitch | backcalfControl |
| `2JCI` | A.O.史密斯彩钢双胆电热水器 | presetSwitch, sterilizationSwitch, switch, mode, faultDetection, instantHeatSwitch, temperature, status, increaseCapacitySwitch | leftTime |
| `2K1K` | 顾家智能电动床 | massageMode, oneKeyReset, angleControl, modeSelect, headControl, headLegControl, legControl, legMassage, lightSwitch | service |
| `2LFZ` | 乐德飞翼AI智能床垫A3 | oneKeyReset, childLockSwitch, memoryControl1, memoryControl3, sleepstatus, modeSelect, headControl, legControl, pause | mac, wakeUp, privacyStatement, bedCondition, siteSelection, sleepStatistics, rouseHeight, antiSnoring |
| `2LKM` | 德国朗乐福智能床 Pro II | massageMode, oneKeyReset, backControl, memoryControl1, modeSelect, memoryControl2, massageTimer, legControl, light | GetMemoryMode, Massagearea, runningstate, Massagegear, Modeloop |
| `2M5L` | 720智能空气净化器 3i | mode, fan, faultDetection, childLockSwitch, pm25, monitoringSwitch, switch, screenSwitch, keytoneSwitch | cmw, airQuality, cav, filterElement1, userInformations, stbyMonitor, city, userFunctions |
| `2M6H` | 智能控制器-6恒 | switch, mode, fan, faultDetection, temperature, humidity, sceneMode, selfCleanswitch, chilledWaterSystemSwitch | capability |
| `2M7T` | 松下智能除菌加湿器 | UVSwitch, switch, mode, faultDetection, humidity, childLockSwitch, elapsedTimeMode, status, gear | filterElement1 |
| `2M8K` | IAM智能消毒空气净化器X5 | switch, mode, fan, humidity, childLockSwitch, tvoc, hcho, pm25, anionSwitch | cav, weight, filterElement4, filterElement5, filterElement3, commonFaultDetection, machineSet, machinePara, outdoorPara |
| `2MGW` | 佳普乐致雅智能浴霸 | drySwitch, warmWindMode, temperature, windSwitch, ventilateSwitch, nightLightSwitch, lightSwitch, status, commonExecution1 | DevAction, WarmWindTime, WindTime, CirculationTime, UserMode |
| `2MHO` | 九牧智能晾衣机A6099 | airDry, disinfect, drying, action, lightSwitch, status, commonExecution1, position, workStatus | disinfectRemTime, airDryTime, dryRemTime, airDryRemTime, dryTime, systemFault |
| `2NQR` | 芝华仕智能沙发40116 | oneKeyReset, headControl, legControl, pause, lumbarControl, memoryControl1, memoryControl3, modeSelect, memoryControl2 | positionSelect, seatStatu, runState |
| `2NTK` | 智能控制器-6恒1代 | switch, mode, fan, temperature, faultDetection, humidity, sceneMode, selfCleanswitch, chilledWaterSystemSwitch | capability |
| `2O4K` | IAM智能净水器Pro | waterOutletType, faultDetection, temperature, childLockSwitch, rinseMode, water, noMoreOvernightWater, tempMode, status | city, inputTds, outputTds, filterElement2, filterElement1, machinePara |
| `2OKC` | meipont智能蒸烤箱 | presetSwitch, switch, temperature, action, status, lightSwitch, clean, sterilization, steam | recipes, setWorkTime, workTime, preTimeStart, leftTime, commonFaultDetection, WaterLevel, UpperRoast, barbecue, SteamRoast |
| `2OR6` | 创维酷开空调 | calmSpellSwitch, switch, mode, fan, sterilization, temperature, sceneMode, switchScreen, switchPTC | — |
| `2OV9` | 雅兰智能床AC-408 | backMassage, backControl, backLegControl, legMassage, modeSelect, lumbarControl, legControl, oneKeyReset, lightSwitch | devStatus, massageFrequency |
| `2P9E` | 欧井智能除湿机OJ-102E | airClean, mode, faultDetection, gear, humidity, anionSwitch, temperature, childLockSwitch, switch | countDown |
| `2PH0` | VIDON威动影K一体机 | deviceStatus, micVolume, musicPlay, mute, playStatus, soundMode, switch, systemMode, volume | interfaceControl |
| `2PRW` | 华歌智能影K功放CIC-MINI-7.2-MIC | audioSelection, volume, switch, channelTest, reset, saveConfig, surroundMode, userConfig, volSwitch | audioplayer, channelFine-tuning, inputSource, mediaKey, micGain |
| `2PRX` | 华歌智能影K功放CIC-MINI-5.1-MIC | audioSelection, channelTest, reset, saveConfig, surroundMode, switch, userConfig, volSwitch, volume | audioplayer, channelFine-tuning, inputSource, mediaKey, micGain |
| `2Q1M` | 正尚3路WiFi开关 | backlight, memorySwitch, switch, switch1, switch2, switch3, mode1, mode3, mode2 | CleanPair, Pair |
| `2Q3N` | 美菱606WQ7FG1冰箱 | aiEsSwitch, aiNrSwitch, aiSwitch, freezeSwitch, intelligentSwitch, inhibitPurineCabin, lightSwitch, photonSwitch, status | freezerFloat, featureMode, refrigeratorFloat, commonFaultDetection |
| `2Q3O` | 美菱618WQ7SG1冰箱 | aiEsSwitch, aiNrSwitch, aiSwitch, freezeSwitch, inhibitPurineCabin, intelligentSwitch, lightSwitch, photonSwitch, status | freezerFloat, featureMode, refrigeratorFloat, commonFaultDetection |
| `2QKP` | 易慧家平开驱动 | action, changeDirection, lightSwitch, opener, silencer, stroke, switchSpeed, torque, windowType | bottomTravel, travel, commonFaultDetection |
| `2QMO` | 荔子M6 Plus智能马桶 | deodorization, hipNozzlePos, indicator, keyToneSwitch, offSeatAction, seatStatus, stop, toiletGasketSwitch, toiletSeatCoverSwitch | drySetting, seatHeating, toiletSetting, washSetting |
| `2QN2` | 慕思智能床 | backControl, childLockSwitch, legControl, memoryControl1, modeSelect, nightLight, oneKeyReset, sleepHelperSwitch, status | foldAngles, getMemoryMode, patService, commonFaultDetection |
| `2R0U` | 奥普浴霸N50-HW | action, autoWarmWindSwitch, automaticWarmWindSwitch, deodorization, drySwitch, status, swingSwitch, ventilateSwitch, windSwitch | commonFaultDetection |
| `2R44` | 顾家AI智能床垫S8 | softHardnessSwitch, childLockSwitch, leftWarmBedTemperature, modeSelect, headAngle, lightSwitch, massageGear, legAngle, rightWarmBedTemperature | leftSoftHardness, leftWarmBedTime, positionSelect, rightSoftHardness, rightWarmBedTime |
| `2R46` | 一起玩eachone  天翼光辅光吸顶灯 | auxBrightness, auxSwitch, brightness, cct, inchingSwitch, lightMode, mainSwitch, switch, commonMemorySwitch | nightWakeup, progressTurnOff, progressSwitch, progressTurnOn |
| `2R5C` | 易慧家推拉驱动Y | action, changeDirection, closeSpeed, handStartSwitch, opener, silencer, stroke, switchSpeed, torque | lockMechanism, lockType, travel, commonFaultDetection |
| `2REH` | 一起玩eachone   天翼光漫反光吸顶灯 | auxBrightness, auxSwitch, brightness, cct, inchingSwitch, lightMode, mainSwitch, switch, commonMemorySwitch | nightWakeup, progressTurnOff, progressTurnOn, progressSwitch |
| `2RH9` | 一起玩eachone  雷达感应天境全色域吸顶灯 | brightness, cct, colour, colourMode, humanSensingStatus, inductionSwitch, lightMode, switch, commonMemorySwitch | checkTime, inductionCondition, inductionTime, lightFormulaArray, nightWakeup, progressSwitch, preLightFormulaArray, preview, progressTurnOff, progressTurnOn |
| `2RJ2` | 宝褓620精控床垫 | childLockSwitch, memoryControl1, memoryControl2, memoryControl4, memoryControl5, memoryControl6, modeSelect, pause, sleepstatus | leftSoftHardness, rightSoftHardness, commonFaultDetection |
| `2RLF` | 慕思智能床1.5m | backControl, childLockSwitch, legControl, memoryControl1, modeSelect, nightLight, oneKeyReset, sleepHelperSwitch, status | foldAngles, getMemoryMode, patService, commonFaultDetection |
| `2RTY` | IAM智能净水器 鲲泽二合一 | childLockSwitch, ecoMode, noMoreOvernightWater, refluxSwitch, status, tempMode, temperature, rinseMode, water | city, disclaimerStatus, filterElement1, filterElement2, inputTds, outputTds, commonFaultDetection |
| `2RZ9` | 德业除湿机DYD-Y26A3 | anionSwitch, childLockSwitch, drainSwitch, gear, humidity, mode, status, switch, temperature | waterTank, commonFaultDetection |
| `2S1K` | 一起玩eachone 天境幻彩吊灯 | auxSwitch, brightness, cct, colour, colourMode, lightMode, mainSwitch, switch, commonMemorySwitch | lightFormulaArray, nightWakeup, preLightFormulaArray, preview, progressSwitch, progressTurnOff, progressTurnOn |
| `2S1U` | 电小酷智能插排CP5-HW | childLockSwitch, indicator, memorySwitch, switch, switch1, switch2, switch3, switch4, usbSwitch1 | commonFaultDetection |
| `2S77` | 丝涟智眠智能床 | headControl, legControl, lightSwitch, massGear, massageMode, massageTimer, modeSelect, oneKeyReset, pause | — |
| `2SCK` | 宠尔顿智能舱 | btcSwitch, childLock, dryMode, intakeAirSwitch, lightSwitch, petRoom, sleepMode, switch, temperature | filterElement, commonFaultDetection, windSpeed, Brightness |
| `A0VY` | COLMO油烟机 | switch, gear, status, lightSwitch, hotcleanSwitch, gestureSwitch, smokeSwitch, steamingSwitch, faultDetection | — |
| `A2TZ` | 智汇云智能水壶 | presetSwitch, heatGear, warmSwitch, heatMode, switch, mode, temperature, status, water | warmDuration, preTimeStart, leftTime, currentTemp, power, boil, color |
| `A2ZS` | 美的焕新风柜机 | heat, selfCleanswitch, freshAirgear, switch, preventStraightWindswitch, mode, ECOswitch, fan, freshAirSwitch | batchCmd, commonFaultDetection, visualization |
| `A30W` | 九牧智能浴霸JD176S | drySwitch, warmWindMode, temperature, action, windSwitch, ventilateSwitch, nightLightSwitch, lightSwitch, status | leftTime, leftTimeWarm, leftTimeWind, leftTimeVen |
| `A37H` | TCL新风挂式空调 | windGear, ECOswitch, switch, mode, freshAirSwitch, temperature, sweepVertical, sweepHorizon, light | newWindECOSwitch, beepSwitch, softWind, newWindPercentage, sleep, PTC |
| `A3F7` | 方太智能清洗中心 | action, command, lowerAreaswitch, lowerRegionStatus, mode, status, switch, upperRegionStatus, workMode | leftTime, remainTime, commonFaultDetection |
| `A3G1` | COLMO新象新风中央空调F | switch, mode, fan, exAirSwitch, freshAirSwitch, exhaustAirSpeed, temperature, freshAirSpeed, automaticAirswitch | — |
| `A3G2` | COLMO新象新风中央空调 | switch, mode, fan, exAirSwitch, freshAirSwitch, exhaustAirSpeed, temperature, freshAirSpeed, automaticAirswitch | — |
| `A3J0` | 小天鹅中央空调客厅新风XF | switch, mode, fan, freshAirSwitch, exAirSwitch, exhaustAirSpeed, temperature, freshAirSpeed, automaticAirswitch | — |
| `A3JF` | 华帝智能燃气热水器 | boostMode, ecoSwitch, inchingSwitch, increaseCapacitySwitch, productModel, status, switch, temperature, zeroColdSwitch | commonFaultDetection |
| `A3KK` | 美的真享空气源热泵ZX1 | ECOswitch, switch, mode, coolWaterTemp, temperature, heatWaterTemp, keyToneSwitch, light, tempControlMode | — |
| `A3LE` | COLMO空气源热泵(M)T1 | switch, mode, coolWaterTemp, temperature, heatWaterTemp, keyToneSwitch, light, switchScreen, tempControlMode | — |
| `A3OK` | 美的加湿器SZK-U15 | airDry, fan, humidity, keyToneSwitch, lightSwitch, mode, status, pciSwitch, switch | ambientLight, waterTank, commonFaultDetection |
| `A3PK` | TCL风管机 | calmSpellSwitch, fan, keyToneSwitch, light, mode, softWindSwitch, switch, switchPTC, temperature | — |
| `A3Q2` | TCL中央空调 | calmSpellSwitch, fan, keyToneSwitch, light, mode, softWindSwitch, switch, switchPTC, temperature | — |
| `A3QM` | 美的壁挂式空调KS2 | ECOswitch, automaticAirswitch, fan, fastColdheat, lightSwitch, mode, switch, switchPTC, temperature | airConditioner, commonFaultDetection |
| `A3T2` | 美的燃气壁挂炉畅享MC2II | aIWarmSwitch, bathStatus, bathTemperature, ecoSwitch, heatStatus, heatSwitch, heatTemperature, hotWaterSwitch, switch | hotWaterPressure, commonFaultDetection |
| `A3VS` | 火星人集成灶M80BC03 | SteamOvenMode, SteamOvenSwitch, SteamOvenWorkStatus, action, kitchenVentLight, kitchenVentilatorGear, powerSwitch, temperature, workBurnerStatus | SteamOvenPreTimeEnd, SteamOvenWorkTime, kitchenVentRemainingTime, commonFaultDetection |
| `A3YH` | COLMO中央空调图灵Pro | calmSpellSwitch, switch, mode, temperature, fan, humidity, light, sceneMode, sterilization | airConditioner, hvacType, commonFaultDetection |
| `A43H` | 华凌中央空调DXHL | switch, mode, temperature, fan, sceneMode, automaticAirswitch, sterilization, switchPTC, waterAndFanValveMode | hvacType, commonFaultDetection |
| `A483` | 美的立柜式空调无风感W2 | ECOswitch, automaticAirswitch, fan, humidity, mode, sceneMode, switch, switchPTC, temperature | airConditioner, commonFaultDetection |
| `ZF0H` | 华为全屋智能 智能中控屏S2 | panelStatus, battery, volSwitch, discovery, panelMode, recoverConfigSwitch, micSwitch, faceEntryAuthorization, cameraSwitch | communication, speakerIfttt, undisturbMode, devList, addDevice, blueBroadcast, assistant, homeBroadcast |
| `ZG0C` | 智能开关 2键 | switch1, switch2, mode1, mode2, backlight, brightness, childLockSwitch, faultDetection, memorySwitch | button1, button2, reboot |
| `ZG0K` | 智能开关 (无线版) 3键 | switch1, switch2, switch3, mode1, mode2, mode3, childLockSwitch, faultDetection, memorySwitch | button1, button2, button3, reboot |
| `ZG0L` | 智能面板（无线版） | backlight, brightness, childLockSwitch, luminance, faultDetection, switch1, switch2, switch3, screenSwitch | button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, button13, button14, button15, button16, button17, button18, button19, button20, display, DNDmode, obstructionDetected, reboot |
| `ZG10` | 智能开关 2键 | switch1, switch2, mode1, mode2, backlight, brightness, childLockSwitch, faultDetection, memorySwitch | button1, button2, reboot |
| `ZG1U` | 智能开关 2键 | switch1, switch2, mode1, mode2, backlight, brightness, childLockSwitch, faultDetection, memorySwitch | button1, button2, reboot |
| `ZG2Q` | 迈腾智能开关 (无线版) 3键 | switch1, switch2, switch3, mode1, mode2, mode3, childLockSwitch, faultDetection, memorySwitch | button1, button2, button3, reboot |
| `ZG2T` | 智能开关 奥斯陆(无线版) 3键 | switch1, switch2, switch3, mode1, mode2, mode3, childLockSwitch, faultDetection, memorySwitch | button1, button2, button3, reboot |
| `ZG2Z` | 智能开关 威尼斯(无线版) 3键 | switch1, switch2, switch3, mode1, mode2, mode3, childLockSwitch, faultDetection, memorySwitch | button1, button2, button3, reboot |
| `ZG30` | 智能开关 都灵 2键 | switch1, switch2, mode1, mode2, backlight, brightness, childLockSwitch, faultDetection, memorySwitch | button1, button2, reboot, theme |
| `158X` | 欧派蒸烤一体机 | status, mode, lackWater, temperature, presetSwitch, lightSwitch, childLockSwitch, faultDetection | waterTankDoor, setWorkTime, leftTime, preTimeStart |
| `207S` | 领普三键零火开关MESH | switch, switch1, switch2, switch3, mode1, mode2, mode3, brightness | button1, button2, button3 |
| `20IU` | 小熊养生壶 | mode, action, status, temperature, warmSwitch, heatGear, presetSwitch, faultDetection | workTime, setWorkTime, preTimeStart, leftTime |
| `20K2` | 澳柯玛养生壶ADK-800S6 | switch, mode, status, temperature, presetSwitch, faultDetection, childLock, targetTemp | preTimeStart, leftTime, targetPower |
| `20L7` | 亚摩斯养生壶YSH08-15B | switch, mode, status, temperature, presetSwitch, faultDetection, childLock, targetTemp | preTimeStart, leftTime, targetPower |
| `20PY` | 亚摩斯挂机空调KFR-35GW | switch, mode, fan, faultDetection, clean, sleeping, light, targetTemp | timing, boostingHot, currentTemp |
| `20SA` | 亚摩斯柜机空调KFR-51LW | switch, mode, fan, faultDetection, clean, targetTemp, light, sleeping | boostingHot, timing, currentTemp |
| `21C1` | 帝王智能座便器 | mode, intensity, nozzlePosition, deodorizeSwitch, faultDetection, gear, clean, hot | online, RInggear, WaterTemperature, Light, lamp, display, Radar, ring, move, seat, Bigwater, smallwater |
| `27DO` | 心智悦新风控制器A1 | status, mode, switch, fan, pm25, tvoc, humidity, temperature | co2, filterElement1, cyclic |
| `28YI` | 帝源空气净化器 | switch, mode, fan, humidity, hcho, pm25, disinfect, temperature | commonFilterElement1, commonFilterElement2, timing |
| `29US` | 安博尔茶吧机 | status, childLockSwitch, faultDetection, commonMode1, commonMode2, commonMode3, commonMode4, commonMode5 | Refrigeration, KettleTemperature |
| `29VU` | 暖通网关MC3 OS | gatewayAction, acMasterSet, faultDetection, commonMode1, commonMemorySwitch1, commonMemoryControl1, commonExecution1, commonTask1 | heaterGroupList, acGroupList, heaterList, freshAirList, port1protocolList, freshAirGroupList, port2protocolList, vrvProtocol, acList, backupData, connectMode, backup, generalList, generalGrouplist, reboot, automaticGroup, commonFilterElement1 |
| `2B8I` | 720 全效空气净化器 1i | switch, mode, childLockSwitch, pm25, fan, faultDetection, keytoneSwitch, screenSwitch | cav, cmw, filterElement1, stbyMonitor |
| `2C6I` | 仁豪家居单人位功能沙发 | oneKeyReset, modeSelect, memoryControl1, memoryControl2, memoryControl3, memoryControl4, angleControl, childlock | MemoryTips |
| `2DRJ` | 澳萌破壁机 | switch, action, gear, status, cupStatus, presetSwitch, faultDetection, temp | preTimeStart, leftTime, modeB, modeA, holdingTemp, time, holdingTime |
| `2GIP` | A.O.史密斯燃气热水器零冷水系列 | boostMode, inletTemperature, switch, faultDetection, temperature, zeroColdMode, zeroColdSwitch, status | totalWater, totalGas, curWater, TimeFunction, gasStatus, statusOfMachine, TotalTime |
| `2H5I` | 亚都加湿器SZ700-TJK600(Hi) | switch, faultDetection, temperature, humidity, childLockSwitch, gear, water, light | sleep, anion, level, uv, dried, timing |
| `2HGB` | 意诺开关控制器 | switch1, switch2, switch3, switch4, switch5, switch6, switch7, switch8 | — |
| `2HIK` | 慕思FZZ1-002电动床 | oneKeyReset, headMassage, modeSelect, headLegControl, headControl, legControl, legMassage, lightSwitch | Stop |
| `2HK2` | 根元智能鞋柜 | switch, mode, brightness, childLock, temperature, action, gear, status | progress, commonFaultDetection, RemainTime, custom, shoeResearch, DoorState |
| `2HKE` | 亚都加湿器SZ1200-TK101(Hi) | switch, faultDetection, temperature, humidity, childLockSwitch, gear, water, light | level, uv, timing, sleep, anion, dried |
| `2HV1` | 舒福德智能床S300 | oneKeyReset, headMassage, modeSelect, massageTimer, headControl, legControl, pause, legMassage | deviceId, frequencyMsg, fallAsleep |
| `2IU8` | 西蒙三位智能场景开关 | mode1, mode2, mode3, switch1, switch2, switch3, indicator, deviceStatus | sceneButton1, sceneButton2, sceneButton3, commonFaultDetection |
| `2JB8` | 梦颜森林光合机 | skinMode, faultDetection, pm25, temperature, humidity, childLockSwitch, switch, light | huanjing, shouhou, pm25Report, pm10Report, pm25SetValue, airHumidityReport, temperatureReport, pm10 |
| `2K8A` | 霍尼韦尔空气净化器KJ1000F-P22W | UVSwitch, switch, mode, fan, childLockSwitch, tvoc, pm25, setting | filterElement2 |
| `2KFX` | 德业除湿机DYD-M45A3 | mode, faultDetection, anionSwitch, switch, temperature, humidity, gear, swingSwitch | CO, fanstate, frost |
| `2KUT` | 飞利浦智能眼部按摩器 | mode, temperature, battery, status, switch, gear, volume, massage | countdown, bredr |
| `2L0T` | 亚都空气净化器KJ1000G-T1000(Hi) | UVSwitch, switch, mode, childLockSwitch, hcho, pm25, anionSwitch, light | sleep, level, sound, timing, work |
| `2LBD` | 百朗亚利桑那200浴霸系列 | warmWindGear, odorsensingSwitch, windSwitch, sterilizationSwitch, swingSwitch, ventilateSwitch, nightLightSwitch, lightSwitch | radar, drytype, time |
| `2LBL` | 百朗亚利桑那280浴霸系列 | warmWindGear, odorsensingSwitch, windSwitch, sterilizationSwitch, swingSwitch, ventilateSwitch, nightLightSwitch, lightSwitch | radar, drytype, timeset |
| `2LHY` | 燃气热水器 | inletTemperature, switch, faultDetection, temperature, zeroColdMode, zeroColdSwitch, presetSwitch, status | totalGas, curGas |
| `2LRN` | 亚都加湿器SZ750-TJK800(Hi) | switch, faultDetection, temperature, humidity, childLockSwitch, gear, light, water | dried, uv, timing, level, lamp |
| `2M7Q` | 松下语音浴霸无照明款 | drySwitch, warmWindMode, fan, action, timeGear, sterilizationSwitch, ventilateSwitch, status | leftTime, commonFaultDetection, coolDrySwitch, windKindSet, windDirectionSet |
| `2MAX` | 达伦智能台灯3Pro | lightMode, switch, brightness, cct, colourMode, eyeSuggestion, mainSwitch, nightLightSwitch | delayOff, eyeRemind, nightMode, lightFormulas01, lightFormulas, lightStatus, lightFormulas02, runStactics, nightSwitch, lightFormulas03 |
| `2MDV` | 杜亚PLC版开合帘电机 尊享款H2 | changeDirection, switchSpeed, action, speed, opener, lightSwitch, faultDetection, selfCheck | placeMemory |
| `2MGJ` | 欧普天空之声音乐灯 | lightMode, mode, switch, colour, brightness, faultDetection, cct, memorySwitch | fadeTime, lightCurveSetting, lightSwigch2, rhythm, bgBrightness, fadeTimeSetting, lightSwitch1 |
| `2MU7` | JoinOne冷暖循环加湿器 | UVSwitch, switch, waterGear, mode, light, humidity, gear, humidification | remainAppoTime, remainWorkTime, reservation, fixedTime, atomization |
| `2MYX` | 西马智能马桶盖 | drySwitch, switch, intensity, mode, faultDetection, waterTemp, dryGear, massage | commonFilterElement1, cleanPosition, onSeat, sitSwitch, seatTemp, nozzleClear, sitTime, womenTime, hipTime, sound, led, eco |
| `2N0H` | 西顿2路MOS调光器(PLC) | switch, faultDetection, brightness, colourMode, brightness2, brightness1, switch2, switch1 | relBrightness, outputMask, onSetting, fadeTimeSetting2, fadeTimeSetting1, lightCurveSetting2, lightCurveSetting1, fadeTime2, fadeTime1 |
| `2NAL` | eachone一起玩智能风扇灯 | lightMode, fanMode, switch, switchFan, fan, brightness, cct, onOffBeep | progressTurnOff, progressTurnOn, countdownht, progressSwitchHF, binding, verticalswing |
| `2NGJ` | 新飞532L四门智能冰箱 | intelligentSwitch, refrigerateSwitch, switch, faultDetection, freezeSwitch, freezer, childLockSwitch, refrigerator | refrigerationRooClosed, transformingSetting |
| `2NHI` | 佳普乐致瑞智能厨房凉霸 | initial, water, switch, temperature, onOffBeep, lightSwitch, horizSweep, status | DevAction, userMode, windTime, circulationTime, windDirection |
| `2NRV` | 爱华仕智能音浪包 | battery, lightMode, loseSwitch, lightSceneMode, mode, lightSwitch, lightGear, sceneMode | audioplayer, speaker |
| `2NS8` | 舒福德智能床S300Pro二重奏 | oneKeyReset, backControl, modeSelect, massageTimer, backMassage, legControl, pause, legMassage | backBControl, backAControl, frequencyMsg, fallAsleep, deviceId |
| `2NZ0` | 九牧智能浴霸JD176P | drySwitch, warmWindMode, action, windSwitch, ventilateSwitch, nightLightSwitch, lightSwitch, status | leftTime, leftTimeWarmStrong, leftTimeWarm, leftTimeWind, leftTimeVen, temperatureCur |
| `2NZT` | 松下高级智能除菌加湿器 | UVSwitch, switch, mode, faultDetection, childLockSwitch, humidity, elapsedTimeMode, gear | filterElement1, filterElement2, devStatus, lightSet, nanoeX |
| `2O1H` | 芝华仕智能沙发30297 | oneKeyReset, headControl, legControl, pause, memoryControl1, memoryControl3, modeSelect, memoryControl2 | positionSelect, runState, seatStatu |
| `2O3P` | 月影自然光护眼吸顶灯 | lightMode, mainBrightness, auxBrightness, mainSwitch, faultDetection, cct, auxSwitch, switch | progressTurnOff, progressTurnOn |
| `2O6R` | 亚都加湿器SZM1100-V12(Hi) | switch, faultDetection, temperature, humidity, childLockSwitch, gear, heat, clean | lamp, timing, uv, dried, anion, level, state |
| `2OCQ` | 舒福德智能床S300Pro | oneKeyReset, backControl, modeSelect, massageTimer, backMassage, legControl, pause, legMassage | deviceId, fallAsleep, frequencyMsg |
| `2OEK` | 松下高级智能除菌加湿器 FE-16C4JD | UVSwitch, switch, mode, faultDetection, humidity, childLockSwitch, elapsedTimeMode, gear | filterElement1, filterElement2, devStatus, nanoeX, lightSet |
| `2OT7` | 艾力斯特按摩椅双芯大师M5X | healthMode, massageGear, ppmMode, status, pressureSwitch, soleSwitch, switch, voiceSwitch | Health, SitAdjustment, Other, State, BackIntensity, Timing, Manual, Bluetooth, Shoulder, Auto |
| `2OTA` | PGG腰部按摩仪W7 | mode, switch, vibrationIntensity, vibrationIntensityOff, vibrationModeOff, battery, hot, status | remainConnect, fault, pulse, remainTime |
| `2OYZ` | MEIPONT赫界智能挂机空调 | calmSpellSwitch, switch, mode, fan, temperature, sceneMode, switchPTC, light | electric, commonFaultDetection |
| `2P13` | 达伦智能台灯5i(双控版) | indicator, lightMode, auxBrightness, brightness, switch, mainSwitch, colourMode, auxSwitch | nightWakeup, toggleSwitch, timeSync, foldAngles, delayTurnoff, directlyConnected |
| `2P2E` | 瑞尔特电子坐便器SE2 | toiletMode, seatStatus, windGear, offSeatAction, waterGear, seatGear, stop, gear | washSetting, toiletSetting, seatHeating |
| `2PIJ` | 佳普乐睿享智能晾衣架 | airDry, disinfect, drying, action, lightBrightness, lightSwitch, status, commonExecution | disinfectRemTime, airDryTime, dryRemTime, airDryRemTime, disinfectTime, dryTime |
| `2PQ5` | THINCO智能台灯5Ultra | brightness, cct, childLockSwitch, lightAdaptionSwitch, lightMode, nightModeSet, remoteCtrPair, switch | lightFormulaArray, longTimeAlarm, preLightFormulaArray, preview, progressTurnOn, remoteControlSearch, seatOffLightSet, seatOnLightSet, timeSync, usageRecord |
| `2QBO` | 豪恩空气质量检测仪 | battery, hcho, heat, humidity, indicator, screenMode, sleepMode, temperature | co2, commonFaultDetection, moisture |
| `2QL5` | MEIPONT智能晾衣机(Pro) | action, airDry, disinfect, drying, lightBrightness, lightSwitch, status, commonExecution | airDryRemTime, airDryTime, disinfectRemTime, disinfectTime, dryRemTime, dryTime, lightRemTime, lightTime, commonFaultDetection |
| `2QVS` | 恩仕AXENT集成浴霸 | autoWarmWindSwitch, automaticWarmWindSwitch, drySwitch, lightSwitch, status, swingSwitch, ventilateSwitch, windSwitch | leftTime, setWorkTime, commonFaultDetection |
| `2QX3` | 冰虎车载冰箱 | battery, childLock, currentTemperature, gear, modeSelection, powerMode, powerSwitch, targetTemperature | powerCon, commonFaultDetection |
| `2RDK` | 一起玩eachone  全面屏雷达吸顶灯 | brightness, cct, humanSensingStatus, inductionSwitch, inchingSwitch, lightMode, switch, commonMemorySwitch | checkTime, inductionCondition, inductionTime, lightFormulaArray, nightWakeup, preview, preLightFormulaArray, progressSwitch, progressTurnOn, progressTurnOff |
| `2RM8` | 便携移动冰箱(车家两用) | battery, childLock, currentTemperature, deviceStatus, gear, modeSelection, powerSwitch, targetTemperature | powerCon, commonFaultDetection |
| `2RQ0` | 艺云 艺术画屏 | action, autoBrightness, brightness, mute, screenMode, status, switch, volume | autoPlay, backup, dataManagement, undisturbMode, commonFaultDetection |
| `2RQU` | ICF AI Max智能底床 | light, massGear, massageMode, massageSwitch, massageTimer, modeSelect, oneKeyReset, sleepstatus | foldAngles, snoringIntervention, time |
| `2RTG` | 一起玩eachone  太阳光天境灯 | brightness, cct, colour, colourMode, lightMode, radarControl, switch, commonMemorySwitch | lightFormulaArray, nightWakeup, progressSwitch, preLightFormulaArray, preview, progressTurnOff, progressTurnOn |
| `2RTX` | 小松鼠壁挂炉 | bathStatus, bathTemperature, flameStatus, heatStatus, heatTemperature, mode, switch, zeroColdMode | commonFaultDetection |
| `2RYM` | 力博得智能牙刷 博享 | areaSwitch, battery, gear, mode, spraySwitch, travelLock, voiceGuidance, workGuidance | brushingHistory, filterElement, setWorkTime |
| `2S06` | 亚都除湿机YD-C870G | childLockSwitch, gear, humidity, indicator, keyToneSwitch, mode, switch, temperature | dehumidify, delayOn, waterTank, commonFaultDetection |
| `2SIL` | 恒洁智能马桶R9-2 | offSeatAction, indicator, keyToneSwitch, lightSwitcht, massageMode, nightLight, seatStatus, smallflushSwitch | ambientLight, washSetting, drySetting, toiletSetting, seatHeating |
| `9MN1` | 华为公版马桶 | autoFlip, massageMode, offSeatAction, seatRing, seatStatus, stop, toiletSeatCoverSwitch, toiletStatus | disinfection, drySetting, foamShield, seatHeating, toiletSetting, washSetting, commonFaultDetection |
| `A0VV` | COLMO智能洗碗机 | status, switch, chidLockSwitch, doorSwitch, action, mode, temperature, faultDetection | leftTime, preLeftTime, softWater, bright, dry, air |
| `A1AE` | 取暖器HFW22ESA | switch, gear, mode, childLockSwitch, temperature, faultDetection, swingSwitch, humidifySwitch | temperatureControlSwitch, preTimeOn, preTimeOff, screenOffSwitch, buttonBeepSwitch |
| `A33I` | TCL挂式空调 | windGear, ECOswitch, switch, mode, temperature, sweepVertical, sweepHorizon, light | PTC, beepSwitch, windSpeedAutoSwitch, softWind, sleep |
| `A35Z` | Pro Base智能底床 | massageMode, oneKeyReset, sleepstatus, headAngle, massageTimer, lieControl, massageGear, legAngle | functionSwitch |
| `A38U` | ICF AI Pro智能底床 | massageMode, oneKeyReset, sleepstatus, massageTimer, headAngle, lieControl, massageGear, legAngle | functionSwitch |
| `A3GA` | 悦智(JOYMART)智能底床 | massageMode, oneKeyMassage, sleepstatus, headAngle, massageTimer, lieControl, massageGear, legAngle | — |
| `A3HZ` | 方太智能油烟机 | gear, intelligentCruiseControl, lightSwitch, gestureSwitch, lockSwitch, status, switch, ventilationSwitch | delayOff |
| `A3IG` | 悦智Pro(JOYMART PRO)智能底床 | massageMode, oneKeyMassage, sleepstatus, headAngle, massageTimer, lieControl, massageGear, legAngle | — |
| `A3KL` | 美的真省空气源热泵(D)S1 | ECOswitch, switch, temperature, heatWaterTemp, keyToneSwitch, light, targetTemp, tempControlMode | — |
| `A3L3` | A.O.史密斯燃气壁挂炉 | flameStatus, heatTemperature, inTemperature, inchingSwitch, machineSafeStatus, mode, switch, zeroColdMode | burningTime, hotWaterPressure, commonFaultDetection |
| `A3L4` | A.O.史密斯电热水器 | sterilizationSwitch, switch, mode, instantHeatSwitch, temperature, aiSwitch, status, increaseCapacitySwitch | commonFaultDetection |
| `A3LD` | 美的真省空气源热泵(S)S1 | ECOswitch, switch, temperature, heatWaterTemp, keyToneSwitch, light, targetTemp, tempControlMode | — |
| `A3N3` | 方太智能水槽净食机 | action, addMode, auxiliarySwitch, childLockSwitch, mode, status, switch, workMode | washLeftTime, commonFaultDetection |
| `A3N4` | 老板油烟机CGU2P-i1 | acMode, acSwitch, fan, gear, leftFanSwitch, lightSwitch, mode, switch | airQuality, delayOff, commonFaultDetection |
| `A3N7` | 老板一体机C80-i1 Pro | action, gear, mixMode, presetSwitch, status, switch, steamVolume, temperature | leftTime, preTimeStart, setWorkTime, commonFaultDetection |
| `A3NE` | 美的风管机酷省电KS | switch, mode, fan, temperature, light, sceneMode, automaticAirswitch, switchPTC | hvacType, commonFaultDetection |
| `A3OC` | 美的空气能热水器睿泉 | mode, faultDetection, highFlowSwitch, highTemperature, temperature, silentSwitch, status, switch | deviceType |
| `A3OF` | 美的加湿器SZK-U12 | airDry, fan, humidity, keyToneSwitch, lightSwitch, mode, status, switch | ambientLight, waterTank, commonFaultDetection |
| `A3OT` | 美的取暖器HPT28BR | childLockSwitch, gear, heatSwitch, indicator, keyToneSwitch, mode, switch, temperature | commonFaultDetection |
| `A3OY` | 美的除湿机CF54BSDA | anionSwitch, drainSwitch, gear, humidity, indicator, keyToneSwitch, mode, switch | delayOff, delayOn, commonFaultDetection |
| `A3PA` | 华帝智能电热水器 | aiSwitch, sterilizationSwitch, mode, autoPowerOffSwitch, status, switch, temperature, water | capacity, commonFaultDetection |
| `A3PD` | 箭牌智能坐便器AKE1208-P | autoFlip, bigflushSwitch, hipNozzlePos, seatRing, seatStatus, smallflushSwitch, toiletSeatCoverSwitch, toiletStatus | drySetting, foamShield, seatHeating, toiletSetting, washSetting |
| `A3PY` | 箭牌智能坐便器AKE1186-P | autoFlip, bigflushSwitch, hipNozzlePos, seatRing, seatStatus, smallflushSwitch, toiletSeatCoverSwitch, toiletStatus | drySetting, foamShield, seatHeating, toiletSetting, washSetting |
| `A3QC` | 华凌立柜式空调HE1II | ECOswitch, automaticAirswitch, fan, mode, sceneMode, switch, switchPTC, temperature | commonFaultDetection |
| `A3QU` | 美的立柜式空调KS2 | ECOswitch, automaticAirswitch, fan, mode, sceneMode, switch, switchPTC, temperature | commonFaultDetection |
| `A3QY` | 美的智能风扇灯 FY3 | brightness, cct, fan, fanMode, lightMode, switch, switchFan, verticalSwitch | — |
| `A3R9` | 方太智能净饮制冰机 | childLockSwitch, fullStopSwitch, iceSwitch, rinseMode, rinseSwitch, status, voiceSwitch, waterMode | rinseLeftTime, rinseTime, commonFaultDetection, commonFilterElement, commonFilterElement1 |
| `A3RS` | 华凌风管机HLU | switch, mode, fan, temperature, light, sceneMode, automaticAirswitch, switchPTC | hvacType, commonFaultDetection |
| `A3T1` | 美的燃气壁挂炉畅享MC2GII | antifreezeStatus, bathStatus, bathTemperature, ecoSwitch, heatStatus, heatSwitch, heatTemperature, switch | hotWaterPressure, commonFaultDetection |
| `A3T4` | 美的智能风扇灯 F5 | brightness, cct, fan, fanMode, lightMode, switch, switchFan, verticalSwitch | — |
| `A3TS` | 博世洗碗机 | action, addMode, lowerRegionStatus, mode, presetSwitch, status, switch, upperRegionStatus | leftTime, preTimeStart, commonFaultDetection |
| `A3TU` | 西门子 洗碗机 | action, addMode, lowerRegionStatus, mode, presetSwitch, status, switch, upperRegionStatus | leftTime, preTimeStart, commonFaultDetection |
| `A3X4` | 老板电器油烟机78 i7 | acMode, acSwitch, gear, gestureSwitch, lightSwitch, mode, status, switch | airQuality, delayOff |
| `A3Y5` | 卡萨帝指挥家双抽洗碗机 | action, command, lowerAreaswitch, lowerRegionStatus, mode, statusDoor, upperRegionStatus, workMode | dishwasher, statusDoorDN, remoteCtrAuthTypeDN, remoteCtrAuthTypeUP |
| `A40N` | 美的风管机酷省电Ultra | switch, mode, temperature, fan, humidity, sceneMode, sterilization, switchPTC | airConditioner, hvacType, commonFaultDetection |
| `A40Y` | 美的立柜式空调酷省电KS1(S1) | ECOswitch, automaticAirswitch, fan, mode, sceneMode, switch, switchPTC, temperature | commonFaultDetection |
| `A41P` | 美的壁挂式空调风尊II | ECOswitch, automaticAirswitch, fan, humidity, mode, switch, switchPTC, temperature | airConditioner, commonFaultDetection |
| `A43E` | 美的立柜式空调风尊3 | ECOswitch, automaticAirswitch, fan, mode, sceneMode, switch, switchPTC, temperature | airConditioner, commonFaultDetection |
| `A43F` | 美的立柜式空调全面风QM1 | ECOswitch, automaticAirswitch, fan, mode, sceneMode, switch, switchPTC, temperature | airConditioner, commonFaultDetection |
| `A448` | 美的除湿机CF30BDBP3N7DI | airClean, anionSwitch, fan, humidity, indicator, keyToneSwitch, mode, switch | dehumidity, delayOff, delayOn, commonFaultDetection |
| `A44A` | 美的除湿机CF14BSDK | anionSwitch, childLockSwitch, fan, humidity, indicator, keyToneSwitch, mode, switch | dehumidity, delayOff, delayOn, commonFaultDetection |
| `A46E` | 美的壁挂式空调酷省电KS2A | ECOswitch, automaticAirswitch, fan, fastColdheat, mode, switch, switchPTC, temperature | airConditioner, commonFaultDetection |
| `A46U` | 美的立柜式空调酷省电KS2 | ECOswitch, automaticAirswitch, fan, mode, sceneMode, switch, switchPTC, temperature | airConditioner, commonFaultDetection |
| `ZG0J` | 智能开关 (无线版) 2键 | switch1, switch2, mode1, mode2, modeX, childLockSwitch, faultDetection, memorySwitch | button1, button2, reboot |
| `ZG1P` | 华为全屋智能 调光驱动器 2路 双色温 恒压 100W | memorySwitch, brightness2, switch1, cct2, switch2, faultDetection, brightness1, cct1 | relBrightness1, fadeTimeSetting2, powerCon, fadeTime1, fadeTimeSetting1, fadeTime2, lightCurveSetting1, outputMask, lightCurveSetting2, relBrightness2 |
| `ZG2P` | 迈腾智能开关 (无线版) 2键 | switch1, switch2, mode1, mode2, modeX, childLockSwitch, faultDetection, memorySwitch | button1, button2, reboot |
| `ZG2S` | 智能开关 奥斯陆(无线版) 2键 | switch1, switch2, mode1, mode2, modeX, childLockSwitch, faultDetection, memorySwitch | button1, button2, reboot |
| `ZG2Y` | 智能开关 威尼斯(无线版) 2键 | switch1, switch2, mode1, mode2, modeX, childLockSwitch, faultDetection, memorySwitch | button1, button2, reboot |
| `112Q` | 踢脚线取暖器 | switch, gear, mode, childLock, temperature, currentTemperature, faultDetection | — |
| `122U` | 智能鞋柜Mini | status, action, mode, temperature, childLock, selfClean, faultDetection | workTime, stovingTemp, stovingWS, warmthTemp, warmthWS, purificationWS, sortStoving |
| `209D` | 亚摩斯养生壶YSH08-15C | switch, mode, status, temperature, presetSwitch, faultDetection, targetTemp | preTimeStart, leftTime |
| `20L5` | 亚摩斯养生壶YSH1258 | switch, mode, status, temperature, presetSwitch, faultDetection, targetTemp | preTimeStart, leftTime, targetPower |
| `20MB` | 维尔森智能新风机 | status, mode, switch, heatSwitch, fan, faultDetection, ledSwitch | filterElement1 |
| `20WI` | 亚摩斯足浴盆AS-FT78B | switch, mode, status, temperature, faultDetection, massage, targetTemp | workTime, leftTime, heating, timing, timingOn |
| `20Y3` | 永林一拖二色温驱动 | switch, switch1, switch2, cct1, cct2, brightness1, brightness2 | — |
| `20YO` | 亚摩斯空气净化器AS-JC261 | switch, mode, childLockSwitch, anionSwitch, pm25, fan, faultDetection | filterElement1 |
| `210Y` | 欧井除湿机 | switch, mode, humidity, temperature, childLockSwitch, gear, faultDetection | ION |
| `213Z` | 西顿一拖二调色模块 | switch, switch1, switch2, cct1, cct2, brightness1, brightness2 | — |
| `217Z` |  | humidity, temperature, switch, mode, fan, childLockSwitch, lightSwitch | filterElement |
| `21DB` | 云起雅赫地暖温控器 | switch, temperature, mode, lightSwitch, heatMode, memorySwitch, freezeSwitch | heatTimer |
| `21KR` | 华为智选 九阳智能恒温电水壶 | action, status, temperature, mode, lightSwitch, voiceSwitch, faultDetection | comMode, hotMode, warmDuration, saveTemperature, leftTime, preTime |
| `21ME` | ULTTY-空气净化冷暖风扇 | switch, onOffBeep, swing, sleepMode, autoMode, childLock, humidity | delay, commonFilterElement1, strongMode, Gear, uvcEn, setTemp, nowTemp, hotMode |
| `22BI` | 乐尔康按摩椅988C9 | switch, autoMode, manuMode, massGear, backAction, stop, heatSwitch | pressureState, remainingTime, workTime, soleAction, ppmAction, gravitySwitch, widthAction, manualAction, mechanicalAction |
| `22Q4` | 小豚室外摄像机 云台版 | switch, shootSwitch, videoSwitch, cruiseSwith, alarmEvent, visitPoint1, commonExecution1 | — |
| `22ZB` | 町米迷你破壁料理机 | switch, action, mode, status, presetSwitch, faultDetection, temperature | preTimeStart, leftTime, autokeepwarm |
| `2302` | 亚摩斯热浪足浴盆 | switch, mode, status, temperature, faultDetection, light, massage | leftTime, timing, surf |
| `2594` | 华为智选 海雀AI全景摄像头 2K版 | alarmEvent, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 | carmera |
| `25I9` | 奥佳华按摩椅 OG-8598Plus | switch, soleSwitch, action, autoMode, heatMode, legAction, backAction | Heat, DIY, AUTO, Customized |
| `25M5` | 仁豪家居智能电动床 | headControl, legControl, legMassage, headMassage, massageMode, massageTimer, modeSelect | — |
| `2622` | 松堡王国智能学习桌 | oneKeyReset, memoryControl1, memoryControl2, memoryControl3, memoryControl4, angleControl, childLock | hightRecommend |
| `26M6` | 光合美梦焕颜机 | switch, mode, childLockSwitch, pm25, temperature, faultDetection, light | pm10, airHumidity, pm25SetValue, pm25Report, pm10Report, airHumidityReport, temperatureReport |
| `27B2` | 心智悦新风机B1 | status, mode, switch, heatSwitch, fan, faultDetection, ledSwitch | filterElement1 |
| `27D0` | 心智悦新风机B2 | status, mode, switch, fan, pm25, faultDetection, ledSwitch | filterElement1, NAI, Heat0 |
| `27W8` | 0-10V双色温调光器 | switch1, brightness1, cct1, switch2, brightness2, cct2, faultDetection | — |
| `28OH` | 清易智慧无线洗地机 | status, switch, battery, sewageboxstate, cleanwaterboxstate, selfclean, commonMode1 | commonFilterElement1, commonFilterElement2, AllProperties, EveryDay, MachineState, DailyAverage, FanLevle, Fault, FactoryReset, DryConfig, Speaker |
| `28XQ` | 佳普乐G3-300A自动翻盖智能马桶 | mode, waterTemp, heatGear, drySwitch, dryGear, status, ECO | wPosition, nightled, seat, cover, smart, sitdown, hPosition, wintenty, hintenty, flush |
| `28XT` | 佳普乐G3-300N智能马桶 | mode, waterTemp, heatGear, drySwitch, dryGear, status, ECO | nightled, smart, sitdown, wPosition, hPosition, wintenty, hintenty, flush |
| `28XU` | 佳普乐G3-400N智能马桶 | waterTemp, heatGear, drySwitch, dryGear, mode, ECO, status | hintenty, flush, hPosition, wintenty, wPosition, smart, sitdown, nightled |
| `294I` | 法狮龙灵悦S智能浴霸 | warmWindGear, drySwitch, switch, temperature, windSwitch, ventilateSwitch, lightSwitch | setWorkTime, leftTime, commonFaultDetection, BYZT, LY |
| `296Z` | 施罗兰智能电动床 | headMassage, modeSelect, massageTimer, headControl, legControl, legMassage, lightSwitch | MassageFrequency |
| `29H0` | 宝贝第一耀至REX | switch, battery, powerSupply, alarm, temperature, fan, heat | hotTemp, PowerLimit, set |
| `2AOC` | 奥佳华7306 | switch, backAction, ppmMode, massGear, heatMode, manuMode, legAction | on, exclusive, AirPressure, time, Vibration, MovementWidth, classic, Intensity, ZeroGravity, KnockingSpeed, roller |
| `2BHE` | 空气堡智慧新风系统ZEN-300H | status, mode, switch, heatSwitch, fan, pm25, light | co2, filterElement1, filterElement2 |
| `2BN0` | 领普三键单火开关MESH | switch, switch1, switch2, switch3, mode1, mode2, mode3 | button1, button2, button3 |
| `2CVX` | 山本空气炸锅 | switch, action, status, temperature, faultDetection, start, temp | workTime, remainTime, recipe, time |
| `2CYO` | 摩摩哒智能按摩椅M635 | switch, autoMode, manuMode, ppmMode, massGear, position, heat | movementUP, movementDown, backUp, backDown, airIntensity, rollerSpeed, rollerMode, timing, range, zeroGravity |
| `2EKR` | 乐尔康按摩椅988N8 | switch, autoMode, manuMode, massGear, backAction, heatSwitch, stop | mechanicalAction, manualAction, widthAction, gravitySwitch, ppmAction, soleAction, workTime, remainingTime, pressureState |
| `2F8N` | 小鸭智玺泡泡卫智能马桶 | stop, toiletMode, toiletStatus, toiletTemperature, seatStatus, gear, massage | CleaningLocation, BubbleClean, AtuoFlush, Energy, HMI, WettingWall, Light, TurnCover, TurnLoop, SprinklerPositionDisplay, MoveClean, AutoDrying, Flushing |
| `2F8Q` | POSO LED射灯 | lightMode, switch, cct, brightness, colourMode, setting, status | — |
| `2F8R` | POSO筒灯 | lightMode, switch, brightness, cct, colourMode, status, setting | — |
| `2FAO` | 协议地暖 | mode, heatingCoolingMode, panelLocation, faultDetection, controlStrategy, switch, temperature | capabilityset |
| `2FNZ` | 长虹空调挂机 | switch, fan, mode, faultDetection, temperature, selfclean, ECO | outdoor, temper, electricalHeating, fresh |
| `2G3K` | 奥普浴霸QDP2826BHW-Pro | warmWindGear, drySwitch, switch, windSwitch, ventilateSwitch, standbySwitch, lightSwitch | leftTime, NightLight |
| `2G3W` | 纽曼便携式储能电源 | USBswitch, battery, lightmode, childlock, timedclosescreen, DCswitch, ACswitch | outputpower, inputpower, ConnectionStatus, userguidance, userDelaytime, userFault |
| `2G4N` | 海雀AI摄像头 云台超清版 2.5K | alarmEvent, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 | carmera |
| `2GAF` | 海雀AI全景摄像头 2.5K版 | alarmEvent, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 | carmera |
| `2GDG` | 海曼(HEIMAN)智能空气质量检测仪(甲醛) | temperature, humidity, battery, hcho, pm25, alarm, mute | tempHighS, humLowS, alarmTimeSet, alarmSwitchS, batteryS, tempLowS, humAlarmS, tempAlarmS, humHighS |
| `2GJN` | AUX-7600 | switch, autoMode, manuMode, ppmMode, massGear, backAction, heat | soleRoller, disptime, time, zero, airPressure |
| `2H6O` | KEKEN智能锁 P20 | lockState, lockStatus, lockMode, battery, alarm, openEvent, commonMode2 | tempPasswd, KeyData, User, UidKidTable, KeyManagement, UserManagement |
| `2HDN` | 灶蒸烤烹饪机JZT/Y-ZK60-01-X20.i | workBurnerStatus, faultDetection, totalWaterShortageStatus, powerSwitch, kitchenVentLight, SteamOvenMode, SteamOvenWorkStatus | kitchenVentRemainingTime, ModeAttribute, SetWorkTime, SetTemperature1, TemperatureSensor1 |
| `2HED` | 油烟机X20.i | mode, faultDetection, lightSwitch, lockSwitch, gear, switch, status | Ambientlight, LockScreen |
| `2HF2` | 长虹空调柜机 | faultDetection, switch, mode, fan, temperature, ECO, selfclean | electricalHeating, fresh, outdoor, temper, TemperandhumiControl, humidity1, dedusting |
| `2IAB` | 罗曼智能电动牙刷HT3pro | mode, initPosition, spraySwitch, battery, workGuidance, voiceGuidance, status | brushingHistory, personalizedservice, partitionreminder, workhour, OTA, brushstrength, Brushhead |
| `2IE0` | 九牧智能马桶ZS660H | stop, toiletMode, seatStatus, nozzlePos, gear, toiletTemperature, toiletFlush | SfunCtl, SsystemStatus, warnEvent, SwideWashingRange, SwomanPara, faultEvent |
| `2IEY` | 康宝牌XDZ45-HM1消毒柜 | switch, faultDetection, temperature, humidity, cabinetDoor, cabinetMode, status | cabinetRemainingTime, CleanTips, WarmingPlateTime |
| `2IHM` | 万家乐 燃气热水器 Z8L | switch, mode, faultDetection, temperature, zeroColdMode, zeroColdSwitch, status | totalGas, Ambient, orderTime, SingleParameter, cmdtype, Doubleboost |
| `2ISC` | 奥普浴霸QDP2826BHW | warmWindGear, drySwitch, switch, windSwitch, ventilateSwitch, standbySwitch, lightSwitch | leftTime, NightLight |
| `2IVP` | 佳普乐G5-300N智能马桶 | heatGear, drySwitch, mode, waterTemp, dryGear, ECO, status | flush, hintenty, wintenty, hPosition, wPosition, sitdown, smart, nightled |
| `2IVQ` | 佳普乐G5-400N智能马桶 | waterTemp, heatGear, drySwitch, dryGear, mode, ECO, status | flush, hintenty, wintenty, hPosition, wPosition, sitdown, smart, nightled |
| `2IVU` | 佳普乐G6-300N智能马桶 | waterTemp, heatGear, drySwitch, dryGear, mode, ECO, status | flush, wintenty, hintenty, hPosition, sitdown, wPosition, smart, nightled |
| `2IVV` | 佳普乐G6-400N智能马桶 | waterTemp, heatGear, drySwitch, dryGear, mode, ECO, status | flush, hintenty, wintenty, hPosition, wPosition, sitdown, smart, nightled |
| `2J6Y` | 达伦智能台灯3i | lightMode, switch, brightness, colourMode, indicator, mainSwitch, backlight | nightWakeup, toggleSwitch, record, fadeTime, lightStatus |
| `2JCH` | A.O.史密斯彩钢单胆电热水器 | switch, mode, faultDetection, instantHeatSwitch, temperature, status, increaseCapacitySwitch | Timing |
| `2JHL` | 智能升降桌AD2-HW | faultDetection, sedentaryrSwitch, childLock, HealthyNeckMode, action, memoryControl1, memoryControl2 | currentHeight, postureStandHeight, sedentaryTimeSet, postureSittingHeight, HealthyNeckHeight, HealthyNeckTime, sedentaryHeight |
| `2K0I` | 卡儿酷户外电源 | USBswitch, battery, lightmode, DCswitch, ACswitch, battery2, temperature | outputpower, inputpower, DC2output, USB2output, state, ACoutput, USB1output, DC1output, solarinput, DCinput, ACinput, endurance, chargingtime |
| `2K81` | 易百珑六键智能开关 | mode3, switch3, switch2, switch1, memorySwitch, mode2, mode1 | sceneButton1, sceneButton3, sceneButton2, sceneButton5, sceneButton4, sceneButton6, CleanPair, Pair, led |
| `2KWP` | 欧普智能灯带驱动器 - 75W | switch, colour, cct, brightness, faultDetection, colourMode, memorySwitch | fadeTime, subProduct, lightCurveSetting, fadeTimeSetting |
| `2KWQ` | 欧普智能灯带驱动器 - 240W | switch, colour, cct, brightness, faultDetection, colourMode, memorySwitch | fadeTime, lightCurveSetting, fadeTimeSetting, subProduct |
| `2L17` | 亚都除湿机YD-C1600Pro(Hi) | anionSwitch, temperature, childLockSwitch, humidity, switch, gear, light | sound, timing, state, level |
| `2L9U` | 亚都除湿机YD-C4000Pro(Hi) | anionSwitch, temperature, childLockSwitch, humidity, switch, gear, light | uv, timing, level, state |
| `2LHK` | 捷昌智能升降桌 | memoryControl4, faultDetection, action, memoryControl1, memoryControl3, memoryControl2, sedentaryReminder | currentHeight, patternJudgment, equipmentStatus |
| `2LTL` | 佳普乐P8-H00A壁挂自动翻盖智能马桶 | toiletMode, windGear, toiletStatus, dryingSwitch, waterGear, seatGear, ECO | seat, cover, nightmode, nightled, sitdown, smart, wPosition, wintenty, hPosition, flush, hintenty |
| `2LV7` | 亚都空气净化器KJ550F-T550(Hi) | UVSwitch, switch, mode, childLockSwitch, hcho, pm25, light | timing, work, sound, level |
| `2M60` | 除菌模块-6恒 | UVSwitch, switch, mode, faultDetection, fan, elapsedTimeMode, anionSwitch | filterElement1, filterElement2, filterElement3, capability, filterElement |
| `2MCG` | 亚都加湿器SZ400-TJK400(Hi) | switch, faultDetection, temperature, humidity, childLockSwitch, gear, water | level, dried |
| `2MMR` | 九牧轻智能马桶J11506 | seatStatus, faultDetection, smallflushSwitch, bigflushSwitch, toiletStatus, seatGear, setting | deviceAlarm |
| `2MTH` | 达伦智能台灯3i(双控版) | lightMode, switch, brightness, colourMode, backlight, indicator, mainSwitch | nightWakeup, toggleSwitch, currentTime, lightStatus, fadeTime |
| `2N1C` | 永艺智能升降桌Thea 680 | faultDetection, sedentaryrSwitch, childLock, action, HealthyNeckMode, memoryControl1, memoryControl2 | currentHeight, sedentaryHeight, HealthyNeckHeight, HealthyNeckTime, postureSittingHeight, postureStandHeight, sedentaryTimeSet |
| `2N8V` | 霍尼韦尔智能护眼吸顶灯U7 60W | lightMode, switch, brightness, cct, mainBrightness, auxBrightness, sleepMode | relCct, relBrightness, preLightFormulaArray, lightFormulaArray, preview, auxBrtSwitch, mainBrtSwitch, nightMode, previewStatus, wakeupMorning, nightModeSwitch, stateHold |
| `2NBL` | A.O.史密斯热泵热水器HPA-EZH系列 | mode, faultDetection, instantHeatSwitch, temperature, zeroColdSwitch, switch, status | TimerCircle, TimerHeat, AES |
| `2NEB` | meipont美邦燃气热水器 | switch, faultDetection, temperature, zeroColdMode, antifreezeStatus, flameStatus, status | priority |
| `2NF9` | 达伦智能台灯T1 | lightMode, switch, brightness, colourMode, eyeSuggestion, mainSwitch, childLock | wakeUp, directlyConnected, eyeRemind, runStactics, currentTime, lightStatus, delayOff |
| `2NGD` | 新飞445L四门智能冰箱 | intelligentSwitch, refrigerateSwitch, faultDetection, freezeSwitch, freezer, childLockSwitch, refrigerator | transformingSetting, refrigerationRooClosed |
| `2NGE` | 新飞450L对开门智能冰箱 | intelligentSwitch, refrigerateSwitch, faultDetection, freezeSwitch, freezer, childLockSwitch, refrigerator | refrigerationRooClosed |
| `2NGF` | 新飞467L四门智能冰箱 | intelligentSwitch, refrigerateSwitch, faultDetection, freezeSwitch, freezer, childLockSwitch, refrigerator | refrigerationRooClosed, transformingSetting |
| `2NGG` | 新飞467L四门变频冰箱 | intelligentSwitch, refrigerateSwitch, faultDetection, freezeSwitch, freezer, childLockSwitch, refrigerator | refrigerationRooClosed, transformingSetting |
| `2NGH` | 新飞470L四门智能冰箱Pro | intelligentSwitch, refrigerateSwitch, faultDetection, freezeSwitch, freezer, childLockSwitch, refrigerator | refrigerationRooClosed, transformingSetting |
| `2NGI` | 新飞470L四门智能冰箱 | intelligentSwitch, refrigerateSwitch, faultDetection, freezeSwitch, freezer, childLockSwitch, refrigerator | refrigerationRooClosed, transformingSetting |
| `2NGK` | 新飞535L对开门智能冰箱 | intelligentSwitch, refrigerateSwitch, faultDetection, freezeSwitch, freezer, childLockSwitch, refrigerator | refrigerationRooClosed |
| `2NGL` | 新飞615L对开门智能冰箱 | intelligentSwitch, refrigerateSwitch, faultDetection, freezeSwitch, freezer, childLockSwitch, refrigerator | refrigerationRooClosed |
| `2NIW` | 霍尼韦尔智能护眼落地灯U7 | lightMode, switch, brightness, cct, mainBrightness, auxBrightness, lock | preview, rhythms, lightFormula, lightforMode, nightAwake, wakeUpMorning, useTime, seatSensor, longTimeAlarm, lightAdaption, currentTime, prompt |
| `2NMZ` | 贝昂落地式循环扇 | switch, neIon, fan, temperature, mode, lock, lightSwitch | track, schedule, delayOff |
| `2NNL` | 地暖 | updateData, panelLocation, mode, faultDetection, controlStrategy, switch, temperature | capabilityset |
| `2NO6` | 极米RS 10 | controlMode, menu, home, setting, volume, return, focusauto | ProjectorSwitch, FOCUSRIGHT, FOCUSLEFT, RESTART, FOCUS |
| `2NOA` | 极米RS 10 Pro | controlMode, menu, setting, home, volume, return, focusauto | ProjectorSwitch, FOCUS, RESTART, FOCUSLEFT, FOCUSRIGHT |
| `2NQC` | meipont美邦空调柜机 | switch, mode, fan, temperature, humidity, ECO, selfclean | commonFaultDetection, dedusting, pmvTemper, outdoor, fresh, electricalHeating, TemperandhumiControl, upcomfortablewind, downcomfortablewind, Infinitewindspeed |
| `2NRH` | 早鱼热敷腰带 | heat, mode, hot, battery, switch, shock, alarm | countDown |
| `2NXG` | SleeponeAi智能电动床 | oneKeyReset, modeSelect, backMassage, headControl, legControl, legMassage, lightSwitch | devStatus, massageFrequency |
| `2NXM` | MEIPONT中央空调(WP) | switch, mode, fan, temperature, sceneMode, switchScreen, switchPTC | commonFaultDetection |
| `2O1M` | 霍尼韦尔智能护眼吸顶灯U7 120W | lightMode, switch, brightness, cct, mainBrightness, auxBrightness, sleepMode | relCct, relBrightness, preLightFormulaArray, lightFormulaArray, preview, auxBrtSwitch, mainBrtSwitch, nightMode, previewStatus, wakeupMorning, nightModeSwitch, stateHold |
| `2O35` | UCAT智能宠物烘干箱D1 PRO | btcSwitch, petRoom, childLock, temperature, dryMode, lightSwitch, switch | variety, settime |
| `2O6B` | 自然舒智能除醛净化器 | switch, mode, temperature, childLockSwitch, humidity, fanGear, pm25 | Countdown, airQuality, VOC, filterLifespan |
| `2O8W` | 极米 Play5 | controlMode, menu, setting, home, volume, return, focusauto | ProjectorSwitch, FOCUSRIGHT, FOCUSLEFT, RESTART, FOCUS |
| `2OAM` | eachone一起玩 智能石墨烯取暖器 | humidifyMode, humidifySwitch, mode, switch, swing, temperature, childLockSwitch | countdown, timeremaining |
| `2OBF` | 极米Z6X 第五代 | controlMode, menu, setting, home, volume, return, focusauto | ProjectorSwitch, FOCUSRIGHT, FOCUSLEFT, RESTART, FOCUS |
| `2OH1` | 酷轻松EMS腰带 | battery, mode, emsGear, hot, redLightSwitch, shock, switch | countDown, time, commonFaultDetection |
| `2OOR` | 智能热敷腰带 | heat, hot, hotSwitch, battery, massage, massageSwitch, alarm | countDown, time |
| `2OPH` | Novia | waterGear, status, massage, childLock, switch1, massageGear, light | temperature1, waterInjectionDuration, massageDuration |
| `2OQZ` | 哆啦A梦智能热敷腰带 | heat, hot, hotSwitch, battery, massage, massageSwitch, alarm | countDown, time |
| `2P12` | 达伦智能台灯5i | indicator, lightMode, auxBrightness, brightness, switch, mainSwitch, auxSwitch | nightWakeup, toggleSwitch, foldAngles, delayTurnoff |
| `2P5I` | 康茂智能调光灯带控制器 | brightness, cct, colour, colourMode, donotDisturb, lightMode, switch | — |
| `2P79` | 吉豪智能灯具 | auxBrightness, lightMode, auxSwitch, brightness, cct, mainSwitch, switch | progressSwitch, cctReverse |
| `2P8U` | 康丽根牌AVE-T3B型纯水机 | emptySwitch, switch, faultDetection, temperature, mode, noMoreOvernightWater, tempMode | dayPurifyWater, filterElement1, height, outputTds, output, outletWater, scaleTotal, waterFlows |
| `2PCJ` | 百得胜新风换气系统 | mode, temperature, humidity, pm25, switch, status, gear | airQuality, co2, filterElement1, outputWind, weight |
| `2PKD` | 新港柜体灯 | brightness, cct, colour, colourMode, donotDisturb, lightMode, switch | — |
| `2PYB` | 三思LED床头灯Pro | brightness, cct, colour, colourMode, lightMode, nightLightMode, switch | streamer |
| `2Q1N` | 正尚2路WiFi开关 | backlight, memorySwitch, switch, switch1, switch2, mode1, mode2 | Pair, CleanPair |
| `2Q9A` | 快速度调光器 | brightness, cct, colour, colourMode, donotDisturb, lightMode, switch | — |
| `2QAC` | 十亿智联智能灯带控制器 | brightness, cct, colour, colourMode, donotDisturb, lightMode, switch | — |
| `2QAM` | 格威特循环泵 | antifreezeSwitch, status, temperature, switch, timedCycleSwitch, zeroColdSwitch, waterFlowSwitch | backup, oneClickCycleTime, flowActivationTime, commonFaultDetection |
| `2QBR` | 九牧i60智能马桶ZD6450 | onSeatAction, faultDetection, offSeatAction, toiletStatus, seatStatus, stop, toiletLidStatus | drySetting, filterElement, foamShield, seatHeating, toiletSetting, washSetting |
| `2QCQ` | 杜亚智能窗帘 隐形大师 | action, changeDirection, directionalmode, favorate, mode, opener, switchSpeed | commonFaultDetection |
| `2QF4` | 颁芙净肤浴电热水器H7 | presetSwitch, switch, mode, autoPowerOffSwitch, temperature, aiSwitch, status | preTimeEnd, commonFaultDetection |
| `2QJQ` | RANTU ONE智能挂机空调 | fan, mode, sceneMode, switch, switchPTC, switchScreen, temperature | electric, commonFaultDetection |
| `2QL7` | RANTU ONE智能挂机空调R7 | fan, mode, sceneMode, switch, switchPTC, switchScreen, temperature | electric, commonFaultDetection |
| `2QL8` | RANTU ONE智能挂机空调M7 | fan, mode, sceneMode, switch, switchPTC, switchScreen, temperature | electric, commonFaultDetection |
| `2QL9` | MEIPONT智能挂机空调T1 | fan, mode, sceneMode, switch, switchPTC, switchScreen, temperature | electric, commonFaultDetection |
| `2QMC` | 箭牌智能花洒 | battery, circulationInsulationSwitch, coldWaterSwitch, status, switch2, screenSwitch, temperatureSetting | drainageDelay, commonFaultDetection |
| `2QO8` | A.O.史密斯燃气热水器零冷水系列JSQ31-DJSH | boostMode, inletTemperature, status, switch, temperature, zeroColdMode, zeroColdSwitch | curWater, totalGas, totalWater, commonFaultDetection, TimeFunction, TotalTime, gasStatus, statusOfMachine |
| `2QQQ` | eachone一起玩  人体存在平板灯 | brightness, cct, humanSensingStatus, inductionSwitch, lightMode, switch, commonMemorySwitch | checkTime, inductionCondition, inductionTime, lightFormulaArray, nightWakeup, preview, progressSwitch, preLightFormulaArray, toggleSwitch |
| `2QR6` | 蜂鸟物联开关PRO-4 | indicator, switch, switch1, switch2, switch3, switch4, commonMemorySwitch | — |
| `2QRI` | 三菱电机空调壁挂机ZC系列 | fan, keyToneSwitch, mode, humidity, softWindSwitch, switch, temperature | capabilityset, electric, commonFaultDetection |
| `2QTU` | 箭牌智能花洒 Pro | battery, circulationInsulationSwitch, coldWaterSwitch, status, switch2, screenSwitch, temperatureSetting | drainageDelay, commonFaultDetection |
| `2QUA` | 恩仕AXENT线性浴霸 | autoWarmWindSwitch, automaticWarmWindSwitch, drySwitch, status, swingSwitch, ventilateSwitch, windSwitch | leftTime, setWorkTime, commonFaultDetection |
| `2QUX` | RANTU ONE智能挂机空调S10 | fan, mode, sceneMode, switch, switchPTC, switchScreen, temperature | electric, commonFaultDetection |
| `2QUY` | RANTU ONE智能柜机空调 双出风 | fan, mode, sceneMode, switch, switchPTC, switchScreen, temperature | electric, commonFaultDetection |
| `2QUZ` | RANTU ONE 智能柜机空调 圆柜 | fan, mode, sceneMode, switch, switchPTC, switchScreen, temperature | electric, commonFaultDetection |
| `2QY9` | eachone一起玩 天境全色域吸顶灯 | brightness, cct, colour, colourMode, lightMode, switch, commonMemorySwitch | lightFormulaArray, nightWakeup, preLightFormulaArray, progressSwitch, preview, progressTurnOff, progressTurnOn |
| `2QYA` | 达伦智能台灯3Max | brightness, cct, lightMode, switch, mainSwitch, nightLightSwitch, eyeSuggestion | delayOff, lightFormulas02, nightMode, runStactics, lightStatus, lightFormulas01, eyeRemind, lightFormulas03, lightFormulas |
| `2R69` | 格丽思多功能茶饮机T-818 | switch, mode, keypressSoundSwitch, status, temperature, warmSwitch, heatGear | setWorkTime, leftTime, commonFaultDetection |
| `2R8O` | 一起玩eachone 天境全色域淡彩吸顶灯 | brightness, cct, colour, colourMode, lightMode, switch, commonMemorySwitch | lightFormulaArray, nightWakeup, progressSwitch, preLightFormulaArray, preview, progressTurnOff, progressTurnOn |
| `2RFB` | 佳普乐沁泽智联龙头 | coldWaterSwitch, inductionSwitch, mode, status, waterTime, switch, temperature | preSchedulingDuration |
| `2RHA` | 一起玩eachone  天境淡彩无缝贴装吸顶灯 | brightness, cct, colour, colourMode, lightMode, switch, commonMemorySwitch | lightFormulaArray, nightWakeup, preLightFormulaArray, progressSwitch, preview, progressTurnOff, progressTurnOn |
| `2RPF` | 索菲亚智能双色温灯H1 | brightness, cct, inchingSwitch, lightMode, remoteCtrPair, switch, commonMemorySwitch | progressSwitch |
| `2RRC` | MEIPONT智能柜机空调 霖界 | fan, mode, sceneMode, switch, switchPTC, switchScreen, temperature | electric, commonFaultDetection |
| `2RSN` | 喜临门呼呼智能床垫H300 | massageMode, memoryControl1, memoryControl2, memoryControl3, memoryControl4, memoryControl5, modeSelect | rightSoftHardness, commonFaultDetection |
| `2RUF` | 三菱电机空调壁挂机ZC16 | fan, keyToneSwitch, mode, humidity, softWindSwitch, switch, temperature | capabilityset, electric, commonFaultDetection |
| `2RUG` | 三菱电机空调壁挂机GZC16 | fan, keyToneSwitch, mode, humidity, softWindSwitch, switch, temperature | capabilityset, electric, commonFaultDetection |
| `2RW7` | 淮海新能源车辆QB15 | battery, drivingMode, lockSwitch, powerSwitch, seatSwitch, seekSwitch, status | commonFaultDetection |
| `2S5V` | 贝昂空气净化器KJ300F-P50(H) | childLockSwitch, fan, indicator, mode, pm25, screenSwitch, switch | autoClean |
| `2SCS` | 八益床垫X300 | headAngle, legAngle, memoryControl5, memoryControl6, modeSelect, oneKeyMassage, oneKeyReset | leftSoftHardness, positionSelect, rightSoftHardness, commonFaultDetection, leftHardness, rightBedHeatGear, leftBedHeatGear, rightHardness |
| `2SG4` | 箭牌智雨花洒2 Pro 宽域恒温版 | battery, circulationInsulationSwitch, coldWaterSwitch, switch2, screenSwitch, status, temperatureSetting | drainageDelay, commonFaultDetection |
| `A0Z7` | 西门子新风1 | status, switch, temperature, faultDetection, fanMode, childLock, systemMode | SleepMode, bypassStatus, filterAlarmStatus |
| `A1C3` | COLMO 图灵嵌入式蒸箱 | doorState, status, preheatStatus, waterBox, faultDetection, mode, action | setWorkTime |
| `A1C4` | COLMO 图灵嵌入式烤箱 | doorState, status, preheatStatus, waterBox, faultDetection, mode, action | setWorkTime |
| `A1QJ` | 美的PS3002W蒸烤箱 | action, faultDetection, mode1, doorState, preheatStatus, waterBox, childLockSwitch | setWorkTime, leftTime, status1, setTemperature |
| `A2LK` | 万和燃气采暖热水炉EU | switch, faultDetection, bathTemperature, flameStatus, heatTemperature, status, reset | Gas, appointment3, appointment2, appointment1, Heatconductionmode, Heatingmode, season, appointmenton2, appointmenton3, appointmenton1 |
| `A2P5` | COLMO洗碗机CDFB16G55 | switch, mode, faultDetection, temperature, action, status, doorSwitch | leftTime, bright, softwater |
| `A2ZU` | 美的机煌挂机 | heat, selfCleanswitch, preventStraightWindswitch, switch, fan, ECOswitch, mode | batchCmd, commonFaultDetection, visualization |
| `A2ZV` | 美的机煌挂机 | heat, selfCleanswitch, switch, ECOswitch, fan, mode, preventStraightWindswitch | batchCmd, commonFaultDetection, visualization |
| `A36V` | 万和燃气热水器STL88 | switch, faultDetection, temperature, zeroColdMode, bathMode, status, ECO | Manual, Oneshot, call, waterPressurization, pretemp |
| `A3BB` | 美的中央空调-卧室新风XF | mode, switch, fan, freshAirSwitch, temperature, freshAirgear, automaticAirswitch | — |
| `A3BC` | 美的中央空调-客厅新风XF | mode, switch, fan, freshAirSwitch, temperature, freshAirgear, automaticAirswitch | Exhaustswitch, Exhaustfan |
| `A3BD` | 酷风中央空调-卧室新风XF | mode, switch, fan, freshAirSwitch, temperature, freshAirgear, automaticAirswitch | — |
| `A3BE` | 酷风中央空调-客厅新风XF | mode, switch, fan, freshAirSwitch, temperature, freshAirgear, automaticAirswitch | Exhaustswitch, Exhaustfan |
| `A3DW` | COLMO水力模块 | automatic, switch, ECO, temperature, goOut, status, electricAuxiliaryHeat | — |
| `A3E3` | COLMO水力模块 | automatic, switch, ECO, temperature, goOut, status, electricAuxiliaryHeat | — |
| `A3E7` | 方太智能热水器 | inchingSwitch, boostMode, switch, temperature, changeLitresMode, bathMode, status | commonFaultDetection |
| `A3FQ` | 美的小型化全热交换新风机 | mode, exAirSwitch, exhaustAirSpeed, freshAirSpeed, freshAirSwitch, status, switch | — |
| `A3FX` | COLMO小型化全热交换新风机M | mode, exAirSwitch, exhaustAirSpeed, freshAirSpeed, freshAirSwitch, status, switch | — |
| `A3G5` | COLMO小型化全热交换新风机 | mode, exAirSwitch, exhaustAirSpeed, freshAirSpeed, status, freshAirSwitch, switch | — |
| `A3HU` | 美的风盘式中央空调T1 | switch, mode, fan, temperature, keyToneSwitch, automaticAirswitch, softWindSwitch | hvacType |
| `A3HW` | COLMO风盘式中央空调(M)T1 | switch, mode, fan, temperature, keyToneSwitch, automaticAirswitch, softWindSwitch | hvacType |
| `A3HX` | COLMO风盘式中央空调(C)T1 | switch, mode, fan, temperature, keyToneSwitch, automaticAirswitch, softWindSwitch | hvacType |
| `A3I7` | A.O.史密斯蒸烤一体机 | action, lackWater, mixMode, ovenMode, status, switch, temperature | leftTime, setWorkTime, commonFaultDetection |
| `A3IT` | COLMO冰箱CRBUS703NX1 | aiFfSwitch, aiSwitch, aiVersatileCabin, disinfectSwitch, iceMode, refrigerateSwitch, freshTemperature | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3IZ` | COLMO冰箱CRBUF708CT1A | aiFfSwitch, aiNutrientCabin, aiSwitch, disinfectSwitch, freezeSwitch, iceMode, refrigerateSwitch | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3J1` | 小天鹅中央空调卧室新风XF | switch, mode, fan, freshAirSwitch, temperature, freshAirSpeed, automaticAirswitch | — |
| `A3J2` | 小天鹅小型化全热交换新风机 | mode, exAirSwitch, exhaustAirSpeed, freshAirSpeed, status, freshAirSwitch, switch | — |
| `A3K4` | COLMO冰箱CRBUF708CT1AC星砂钢 | aiFfSwitch, aiNutrientCabin, aiSwitch, disinfectSwitch, freezeSwitch, iceMode, refrigerateSwitch | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3K5` | COLMO冰箱CRBUF708CT1AC熔幔岩 | aiFfSwitch, aiNutrientCabin, aiSwitch, disinfectSwitch, freezeSwitch, iceMode, refrigerateSwitch | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3K6` | COLMO冰箱CRBUF708CT1AC雪山岩 | aiFfSwitch, aiNutrientCabin, aiSwitch, disinfectSwitch, freezeSwitch, iceMode, refrigerateSwitch | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3K7` | COLMO冰箱CRBUF708CT1AC云璃白 | aiFfSwitch, aiNutrientCabin, aiSwitch, disinfectSwitch, freezeSwitch, iceMode, refrigerateSwitch | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3K8` | COLMO冰箱CRBUF708CT1AC量子灰 | aiFfSwitch, aiNutrientCabin, aiSwitch, disinfectSwitch, freezeSwitch, iceMode, refrigerateSwitch | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3KA` | COLMO冰箱CRBUF708CT1AC星云钢 | aiFfSwitch, aiNutrientCabin, aiSwitch, disinfectSwitch, freezeSwitch, iceMode, refrigerateSwitch | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3KB` | COLMO冰箱CRBUF708CT1H雪山岩 | aiFfSwitch, aiNutrientCabin, aiSwitch, disinfectSwitch, freezeSwitch, iceMode, refrigerateSwitch | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3KC` | COLMO冰箱CRBUF708CT1H星砂钢 | aiFfSwitch, aiNutrientCabin, aiSwitch, disinfectSwitch, freezeSwitch, iceMode, refrigerateSwitch | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3KD` | COLMO冰箱CRBUF708CT1H星云钢 | aiFfSwitch, aiNutrientCabin, aiSwitch, disinfectSwitch, freezeSwitch, iceMode, refrigerateSwitch | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3KE` | COLMO冰箱CRBUF708CT1H云璃白 | aiFfSwitch, aiNutrientCabin, aiSwitch, disinfectSwitch, freezeSwitch, iceMode, refrigerateSwitch | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3KF` | COLMO冰箱CRBUF708CT1H熔幔岩 | aiFfSwitch, aiNutrientCabin, aiSwitch, disinfectSwitch, freezeSwitch, iceMode, refrigerateSwitch | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3KG` | COLMO冰箱CRBUF708CT1H量子灰 | aiFfSwitch, aiNutrientCabin, aiSwitch, disinfectSwitch, freezeSwitch, iceMode, refrigerateSwitch | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3KY` | COLMO冰箱CRBUS703NX1星砂钢 | aiFfSwitch, aiSwitch, disinfectSwitch, aiVersatileCabin, iceMode, refrigerateSwitch, freshTemperature | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3KZ` | COLMO冰箱CRBUS703NX1量子灰 | aiFfSwitch, aiSwitch, disinfectSwitch, aiVersatileCabin, iceMode, refrigerateSwitch, freshTemperature | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3L0` | COLMO冰箱CRBUS703NX1星云钢 | aiFfSwitch, aiSwitch, aiVersatileCabin, disinfectSwitch, iceMode, refrigerateSwitch, freshTemperature | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3L1` | COLMO冰箱CRBUS703NX1云璃白 | aiFfSwitch, aiSwitch, disinfectSwitch, aiVersatileCabin, iceMode, refrigerateSwitch, freshTemperature | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3L2` | COLMO冰箱CRBUS703NX1雪山岩 | aiFfSwitch, aiSwitch, aiVersatileCabin, disinfectSwitch, iceMode, refrigerateSwitch, freshTemperature | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3L5` | A.O.史密斯燃气热水器FJS | boostMode, changeLitresMode, ecoSwitch, status, switch, temperature, zeroColdSwitch | curWaterVol, zeroColdTime, commonFaultDetection |
| `A3N6` | 老板洗碗机W76-i1 Pro | action, addMode, mode, presetSwitch, status, switch, statusDoor | leftTime, preTimeStart, commonFaultDetection |
| `A3NG` | 美的风管机乐享IV | switch, mode, fan, temperature, sceneMode, automaticAirswitch, switchPTC | hvacType, commonFaultDetection |
| `A3NQ` | 华帝智能洗碗机 | action, auxiliarySwitch, mode, rinse, rinseAid, status, switch | orderLeftTime, washLeftTime, commonFaultDetection |
| `A3O5` | 老板蒸烤一体机C9077A C5 | action, mixMode, presetSwitch, status, steamVolume, switch, temperature | preTimeStart, setWorkTime, workTime, commonFaultDetection |
| `A3OW` | 美的除湿机CF25BSDA | anionSwitch, gear, humidity, indicator, keyToneSwitch, mode, switch | delayOff, delayOn, commonFaultDetection |
| `A3P4` | 老板电器油烟机CG26X32 D3 | acSwitch, gear, leftFanSwitch, lightSwitch, mode, status, switch | airQuality, delayOff |
| `A3PQ` | 箭牌智能浴室柜QN-PRO | childLockSwitch, demisterSwitch, indicator, lightSwitcht, makeupLightGear, sensorDistanceGear, sensorLightGear | ambientLight |
| `A3Q4` | TCL天花机 | calmSpellSwitch, fan, keyToneSwitch, light, mode, switch, temperature | — |
| `A3QF` | 美的壁挂式空调KS1(S1) | ECOswitch, automaticAirswitch, fan, mode, switch, switchPTC, temperature | airConditioner, commonFaultDetection |
| `A3QI` | 嘉格纳洗碗机 | action, lowerRegionStatus, mode, presetSwitch, status, switch, upperRegionStatus | leftTime, preTimeStart, commonFaultDetection |
| `A3QK` | 美的壁挂式空调KS1(S4) | ECOswitch, automaticAirswitch, fan, mode, switch, switchPTC, temperature | airConditioner, commonFaultDetection |
| `A3QT` | 德业除湿机DYD-T22A3 | anionSwitch, childLockSwitch, gear, humidity, mode, switch, temperature | dehumidify, waterTank |
| `A3T5` | 老板电器油烟机CG8869 G30 | acMode, acSwitch, gear, lightSwitch, mode, status, switch | airQuality, delayOff |
| `A3U3` | 美的壁挂式空调KS1(S3) | ECOswitch, automaticAirswitch, fan, mode, switch, switchPTC, temperature | airConditioner, commonFaultDetection |
| `A3U4` | 美的壁挂式空调KS1(S2) | ECOswitch, automaticAirswitch, fan, mode, switch, switchPTC, temperature | airConditioner, commonFaultDetection |
| `A3VV` | 箭牌智联浴室柜XL | childLockSwitch, demisterSwitch, indicator, lightSwitcht, makeupLightGear, sensorDistanceGear, sensorLightGear | ambientLight |
| `A3YI` | COLMO中央空调一风口 | switch, mode, temperature, fan, humidity, sceneMode, sterilization | airConditioner, commonFaultDetection |
| `A3Z7` | 美的壁挂式空调风尊IIPro | ECOswitch, automaticAirswitch, fan, mode, switch, switchPTC, temperature | airConditioner, commonFaultDetection |
| `A40Z` | 美的立柜式空调酷省电KS1(S2) | ECOswitch, automaticAirswitch, fan, mode, switch, switchPTC, temperature | airConditioner, commonFaultDetection |
| `A410` | A.O.史密斯燃气壁挂炉V3 | flameStatus, heatTemperature, inTemperature, inchingSwitch, machineSafeStatus, mode, switch | burningTime, hotWaterPressure, commonFaultDetection |
| `A46F` | 美的壁挂式空调酷省电72GKS2 | ECOswitch, automaticAirswitch, fan, mode, switch, switchPTC, temperature | airConditioner, commonFaultDetection |
| `A46G` | 美的壁挂式空调酷省电N8KSU | ECOswitch, automaticAirswitch, fan, mode, switch, switchPTC, temperature | airConditioner, commonFaultDetection |
| `D0AM` | HUAWEI PixLab V1 | printerStatus, tonerStatus, copyJobStatus, supportCancelPrintJob, scanJobStatus, faultDetection, netStatus | printJobStatus, autoUpgradeTime, timeWindow, cancelPrintJob |
| `D0AW` | HUAWEI Inkjet Printer | printerStatus, tonerStatus, copyJobStatus, supportCancelPrintJob, scanJobStatus, faultDetection, netStatus | printJobStatus, autoUpgradeTime, timeWindow, cancelPrintJob |
| `ZF08` | 智能中控屏10.1英寸 | volSwitch, panelMode, ringLightSwitch, recoverConfigSwitch, temperature, humidity, discovery | blueBroadcast, roomsleeptime, devList, undisturbMode, addDevice, assistant, homeBroadcast |
| `ZF0A` | 智能中控屏6.6英寸 | volSwitch, panelMode, ringLightSwitch, recoverConfigSwitch, temperature, humidity, discovery | blueBroadcast, roomsleeptime, devList, undisturbMode, addDevice, assistant, homeBroadcast |
| `ZG0B` | 智能开关 1键 | switch1, mode1, backlight, brightness, childLockSwitch, faultDetection, memorySwitch | button1, reboot |
| `ZG0Z` | 智能开关 1键 | switch1, mode1, backlight, brightness, childLockSwitch, faultDetection, memorySwitch | button1, reboot |
| `ZG1T` | 智能开关 1键 | switch1, mode1, backlight, brightness, childLockSwitch, faultDetection, memorySwitch | button1, reboot |
| `0100` | 三思全彩灯泡灯组 | switch, brightness, colourMode, colour, cct, lightMode | delay |
| `1074` | 水母云全彩智能E27灯泡 | switch, brightness, colourMode, colour, cct, lightMode | lightNoisyWakeUp, lightGraduallyWakeUp, delay |
| `1075` | 水母云IP65智能LED筒灯 | switch, brightness, colourMode, colour, cct, lightMode | lightNoisyWakeUp, lightGraduallyWakeUp, delay |
| `1076` | 水母云智能吸顶灯 | switch, brightness, colourMode, colour, cct, lightMode | lightNoisyWakeUp, lightGraduallyWakeUp, delay |
| `107C` | 莱柏顿风扇LBT-F02 | mode, speed, onOffBeep, childLock, battery, connectStatus | binarySwitch, angle, handangle, onOffLight, preTime, endTime |
| `111Z` | 三思双色温灯泡 | switch, brightness, lightMode, colourMode, colourMode, cct | delay |
| `112O` | 亚摩斯养生壶 | switch, mode, command, status, currentTemperature, faultDetection | keepWarmTP, remWorkTime, heatpower, preTime, remPreTime, workTime, remWorkTime, cookInfo |
| `113J` | 海雀AI全景摄像头 | visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 | carmera, strangerFace, face1, face2, face3, face4, face5, face6, face7, face8, face9, face10 |
| `113T` | 柏翠蒸烤箱PE8289WT | status, mode, doorStatus, light, temperature, faultDetection | humidifier, startCommand, leftTime, cookInfo |
| `114Z` | 奥普浴霸QDP6020AHW | switch, lightSwitch, mode, temperature, currentTemperature, faultDetection | leftTime |
| `123M` | 电力魔方空气卫士 | switch, lightSwitch, brightness, temperature, humidity, faultDetection | airPurifying, filterElementReset, Eco, pm2p5 |
| `131F` | 小豚当家AI全彩摄像头 | visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 | carmera |
| `131N` | 生迪智能LED彩光灯泡 | switch, brightness, colourMode, colour, cct, lightMode | delay |
| `132Q` | 冠雅LED台灯 | switch, brightness, colourMode, cct, lightMode, commonMemorySwitch1 | — |
| `146I` | 三思智能筒灯 | switch, brightness, lightMode, colourMode, colour, cct | streamer, delay |
| `146M` | 华为智选 360智能扫地机2S | status, action, mode, gear, battery, faultDetection | curZone, availableZones, edgeElement, mainElement, strainerElement |
| `146N` | 华为智选 360智能扫地机2Pro | status, action, mode, gear, battery, faultDetection | curZone, availableZones, edgeElement, mainElement, strainerElement |
| `165U` | 贝昂无耗材空气净化器 | switch, mode, childLockSwitch, pm25, fan, clean | delay |
| `171I` | BYBLUE智能云台摄像头 | visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 | carmera |
| `172D` | POVOS奔腾加湿器 | switch, humidity, temperature, gear, faultDetection, mode | time |
| `172U` | POVOS奔腾加湿器 | switch, humidity, temperature, gear, faultDetection, mode | Time |
| `178M` | 海尔空气净化器KJ820F-N800C | switch, mode, childLockSwitch, anionSwitch, pm25, fan | filterElement1 |
| `178N` | 西顿风影彩光灯带 | switch, brightness, lightMode, colourMode, colourMode, colour | — |
| `202J` | 贝昂无耗材空气净化器 | switch, mode, childLockSwitch, pm25, fan, clean | delay |
| `204Z` | 四季沐歌M-HY902H-GG智能晾衣机 | action, status, airDry, disinfect, drying, lightSwitch | — |
| `207P` | 领普双键零火开关MESH | switch, switch1, switch2, mode1, mode2, brightness | button1, button2 |
| `208J` | 水母云唤醒灯 | switch, brightness, lightMode, colourMode, colour, cct | — |
| `20H9` | 晾品智能晾衣机 | action, status, airDry, disinfect, drying, lightSwitch | airDryRemTime, airDryTime, disinfectTime, disinfectRemTime, dryRemTime, dryTime |
| `20JM` | 欧派智能晾衣机 | action, status, airDry, disinfect, drying, lightSwitch | motorBlock |
| `20LA` | 三思LED床头灯 | switch, brightness, lightMode, colourMode, colour, cct | streamer, delay, yedengstatus, yedengsw |
| `20LK` | 三思智能全彩充电床头灯 | switch, brightness, lightMode, colourMode, colour, cct | streamer, delay, yedengsw, yedengstatus |
| `20LT` | 水母云智能全彩筒灯 | switch, brightness, lightMode, colourMode, colour, cct | streamer, delay |
| `20S7` | 亚摩斯净水器AS-RO075 | status, mode, childLockSwitch, temperature, faultDetection, waterLevel | filterElement1, filterElement2, output, input, manualMode |
| `20TL` | 贝昂无耗材空气净化器X7SH | switch, mode, childLockSwitch, pm25, fan, clean | delay, hcho1 |
| `20U5` | 索菲莉尔智能电动床300 | headControl, legControl, lieControl, massageMode, modeSelect, stop | helpSleep, msgTime, legMsg, headMsg |
| `211S` | 澳柯玛智能冰箱 | refrigerateSwitch, freezeSwitch, intelligentSwitch, refrigerator, freezer, faultDetection | coolingSwitch, variableTemper, VariableRoom1 |
| `2120` | 小豚当家智能云台摄像头 | visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 | carmera |
| `2168` | 亚都智能除湿机YD-C253BGWHi | switch, mode, humidity, temperature, childLockSwitch, gear | delay, state, sleep |
| `2178` | 亚都空气净化器KJ650F-P6PLUSHi | switch, mode, childLockSwitch, pm25, fan, light | filterElement1, countdown, sound |
| `218H` | 阳光照明灵睿智能灯泡RGBWC版 | switch, brightness, lightMode, colourMode, colour, cct | streamer, delay |
| `21AZ` | 海雀AI摄像头 云台超清版 | visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 | hwaccount, carmera, strangerFace, face1, face2, face3, face4, face5, face6, face7, face8, face9, face10 |
| `21BB` | 亚摩斯饮水机AS-WH22B | status, mode, childLockSwitch, faultDetection, sterilize, waterLevel | sterilizeOff, sterilizeOn |
| `21DU` | 水母云智能灯带 | switch, brightness, lightMode, colourMode, colour, cct | streamer, delay |
| `21FU` | 亚摩斯落地加湿器AS-V618 | switch, humidity, temperature, gear, faultDetection, mode | degerming, timing |
| `21OR` | A.O.史密斯壁挂炉 | switch, heatingSwitch, waterControl, mode, waterTemperature, faultDetection | heatingTemperature, heatingTimer, waterTimer |
| `21SZ` | 蓓慈足浴器BZ307B1 | switch, status, faultDetection, currentTemperature, temperature, massage | leftTime, setWorkTime |
| `21UO` | FSL智能彩光灯带 | switch, brightness, colourMode, colour, cct, commonMode1 | streamer, delay |
| `21YV` | 贝昂无耗材空气净化器MINI | switch, mode, childLockSwitch, pm25, fan, clean | delay |
| `2244` | 雷士满天星风扇灯 | switch, brightness, lightMode, colourMode, cct, lightswitch | delay, Fan, fanswitch |
| `224K` | 欧普智能幻彩灯带 | switch, brightness, lightMode, speed, colour, status | motion, modeName, effect, motionDetected |
| `2261` | 欧派智能晾衣机 | action, status, airDry, disinfect, drying, lightSwitch | motorBlock |
| `2262` | 长虹极简挂机 | switch, mode, fan, faultDetection, selfclean, ECO | outdoor, indoor, temper, electricalHeating, fresh |
| `2264` | 欧派智能声控晾衣机 | action, status, airDry, disinfect, drying, lightSwitch | motorBlock |
| `22EX` | 北欧夫人智能晾衣架 | action, status, airDry, disinfect, drying, lightSwitch | airDryRemTime, airDryTime, disinfectTime, disinfectRemTime, dryRemTime, dryTime |
| `22GN` | Soopu智能晾衣架 | action, status, airDry, disinfect, drying, lightSwitch | airDryRemTime, airDryTime, disinfectTime, disinfectRemTime, dryRemTime, dryTime |
| `22GO` | 指力大师按摩椅 | switch, soleSwitch, autoMode, manuMode, heatMode, massGear | legUp, backDown, zero, legDown, backUp |
| `23DZ` | 亚摩斯智能养生杯YSH08-10C | mode, action, status, temperature, heatGear, faultDetection | leftTime, holdTemp |
| `23RF` | 黑创智能晾衣机 | action, status, airDry, disinfect, drying, lightSwitch | motorblock |
| `242X` | 亚摩斯RGBCW灯带控制器 | switch, brightness, colourMode, colour, cct, lightMode | — |
| `2492` | 太太乐智能晾衣机 | action, status, airDry, disinfect, drying, lightSwitch | motorBlock |
| `24NG` | 奔腾剃须刀 | switch, status, mode, battery, temperature, clean | record, totalTime, errTips, type, paly |
| `25WT` | 华为智选 欧普智能床头台灯 | switch, brightness, lightMode, colour, whiteLightMode, colourLightMode | streamer, delay, nightWakeup, alarmSetting, dataStatistics |
| `26WG` | 帅康智能集成灶 | powerSwitch, workBurnerStatus, totalWaterShortageStatus, kitchenVentLight, SteamOvenMode, cleanMode | rightStoveOff, leftStoveOff, windSpeed |
| `273O` | 水母云智能天花灯 | switch, brightness, colourMode, colour, cct, lightMode | streamer, nightWakeup, progressTurnOn, progressTurnOff, backswitch, frontlight |
| `2754` | 智能晾衣机 | airDry, disinfect, drying, action, lightSwitch, status | airDryRemTime, airDryTime, disinfectTime, disinfectRemTime, dryRemTime, dryTime, commonFaultDetection |
| `27OD` | 小智K11 智能门锁 | lockState, lockMode, battery, alarm, openEvent, Volume | keyList, userlist, remoteResult, publicKey, remoteCode, remoteInfo |
| `27W5` | 侧装红外人体移动光照传感器 | switch, switch1, status, lightSwitch, brightness, cct | — |
| `2847` | 金凯瑞足浴盆 | mode, temperature, action, status, massage, light | leftTime, OneClickStart |
| `28I7` | 贝昂无耗材空气净化器 | switch, mode, fan, childLockSwitch, pm25, clean | — |
| `28XS` | 佳普乐G3-400A自动翻盖智能马桶 | mode, waterTemp, heatGear, drySwitch, dryGear, ECO | nightled, seat, cover, smart, sitdown, womannozzlePosition, hipnozzlePosition, woman2intensity, hip2intensity, flush |
| `294C` | 荣事达衣物护理机 | switch, action, mode, status, childLockSwitch, faultDetection | leftTime, pretime, gate, Water |
| `29F2` | 侧装红外人体移动光照传感器 | switch, switch1, status, lightSwitch, brightness, cct | — |
| `29X9` | 欧井智能除湿机OJ-223E | mode, faultDetection, humidity, childLockSwitch, switch, gear | commonFilterElement1, Temp, Purify, Countdown |
| `29Z4` | P40proXM自动翻盖智能坐便器 | switch, waterTemp, intensity, heatGear, dryGear, nozzlePosition | FaultAlarm, seatstatus, FlipFunction, WashMode, CustomFunction, Move |
| `29ZA` | P40proXL自动翻盖智能坐便器 | switch, waterTemp, intensity, nozzlePosition, heatGear, dryGear | Move, CustomFunction, WashMode, FlipFunction, seatstatus, FaultAlarm |
| `2A8C` | 电力魔方空气卫士PRO | switch, pm25, fan, temperature, humidity, faultDetection | cmw, LED |
| `2A9O` | 欧派智能声控晾衣机 | action, status, airDry, disinfect, drying, lightSwitch | motorBlock |
| `2AQ8` | 亚都空气净化器KJ550G-B5Hi | switch, mode, childLockSwitch, pm25, fan, light | filterElement1, sound, countdown |
| `2AVU` | 亚都空气净化器KJ650F-B6Hi | switch, mode, childLockSwitch, pm25, fan, light | filterElement1, sound, countdown |
| `2BB8` | 海雀智能摄像头S | visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 | hwaccount, carmera |
| `2BBH` | 鸿蒙智选 海雀智能摄像头Pro 32GB | visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 | hwaccount, carmera |
| `2BCC` | 荣泰按摩椅 | switch, soleSwitch, autoMode, manuMode, heatMode, massGear | backDown, backUp, legDown, legUp, zero |
| `2BEI` | 得邦A60蓝牙智能灯泡全彩版 | switch, brightness, lightMode, colourMode, colour, cct | — |
| `2BEJ` | 得邦A70蓝牙智能灯泡全彩版 | switch, brightness, colourMode, colour, cct, lightMode | — |
| `2BG1` | 哈尔斯真空电热水壶 | mode, action, status, temperature, warmSwitch, presetSwitch | warmDuration, preTimeStart, leftTime, commonFaultDetection, Others |
| `2BXP` | 觅石智能IH电饭煲3L | status, action, mode, warmSwitch, presetSwitch, faultDetection | warmDuration, workTime, setWorkTime, leftTime, preTimeEnd, YSP |
| `2C60` | 鸿蒙智选 海雀智能摄像头Pro 64GB | visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 | hwaccount, carmera |
| `2CBM` | 捷德韦尔RGB灯控盒 | switch, brightness, colourMode, colour, lightMode, commonMemorySwitch1 | progressSwitch, delay |
| `2COB` | 三思LED充电床头灯 | switch, brightness, lightMode, colourMode, colour, cct | streamer, yedengstatus, yedengsw |
| `2CPW` | 创维氛围灯 | switch, brightness, colourMode, colour, cct, lightMode | streamer |
| `2CXP` | BYBLUE智能云台摄像头超清版 | visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 | carmera |
| `2D59` | 黑创hrlchure智能晾衣机 | action, status, airDry, disinfect, drying, lightSwitch | — |
| `2D7S` | 三思智能筒灯 | switch, brightness, lightMode, colourMode, colour, cct | streamer |
| `2D7T` | 三思智能炫彩灯带 | switch, brightness, lightMode, colourMode, colour, cct | streamer |
| `2D80` | 华为智选 360智能扫地机2 | status, action, mode, gear, battery, faultDetection | curZone, availableZones, edgeElement, mainElement, strainerElement |
| `2DME` | 四路智能开关 | switch, switch1, switch2, switch3, switch4, backlight | — |
| `2DQQ` | 贝昂落地式循环扇 | switch, mode, temperature, speed, lock, light | lrwind, udwind, timingOff, timingOn |
| `2E3W` | 芝华仕按摩椅 | switch, autoMode, manuMode, position, speed, intensity | adjstatus, cancle, shoulder, movement, shank, sitting, ppm, back, leg, range, roller, timing, ble, voice |
| `2EM7` | BYBLUE智能云台摄像头2K版 | visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 | carmera |
| `2EW3` | 月影智能护眼台灯-新月 | switch, brightness, colourMode, cct, lightMode, rest | restime, auto, write, read, nlight, love |
| `2F2H` | FSL智影炫彩灯带-3米 | switch, brightness, colourMode, colour, commonMode1, commonMode2 | progressTurnOn, progressTurnOff, Create |
| `2FEC` | 金莱特智能空气净化器 | switch, mode, childLockSwitch, UVSwitch, fan, pm25 | ota, filterElement1, lightd |
| `2FEN` | 智能刀筷消毒烘干架 | mode, knifeShelfSwitch, presetSwitch, status, childLock, alarm | time, remainingTime |
| `2FJ3` | 贝昂落地式循环扇(鸿蒙版) | switch, mode, fan, light, temperature, lock | timingOn, timingOff |
| `2FJ4` | 贝昂台式循环扇 | switch, mode, fan, light, temperature, lock | timingOn, timingOff |
| `2FJW` | 海曼(HEIMAN)智能可燃气体探测器 | switchNightLight, selfCheck, silencer, faultDetection, preheat, alarm | gasSensorS, VolumeSetting, Language, AlarmType, handonoff |
| `2FJX` | 海曼(HEIMAN)智能空气质量检测仪(二氧化碳) | tempUnit, humAlarm, battery, faultDetection, alarm, tempAlarm | co2, humidityRH, temperatureC, humidityThreshold, temperatureThreshold, CO2Threshold, Metu, SilenceTime |
| `2G8J` | 熊二智能洗地机 | status, battery, sewageboxstate, cleanwaterboxstate, commonMode1, commonMode2 | workTime, commonFilterElement1, commonFaultDetection |
| `2H6F` | 天璇智能安全座椅 | heatGear, powerSupply, seatBattery, fanGear, ISOFIXStatus, bottomBattery | Angle, OTAUpgrade, direction, supportLeg, devicceStatus |
| `2HAK` | 希箭H1 HC半自动WiFi智能锁 | lockState, lockMode, battery, alarm, openEvent, Volume | keyList, remoteInfo, remoteCode, publicKey, remoteResult, userlist |
| `2HKO` | 空气炸锅D05 | action, switch, temperature, status, faultDetection, workStatus | workTime, recipes, FirmwareUpdate |
| `2HLQ` | 奥普浴霸QDP3622AHW | warmWindGear, drySwitch, windSwitch, ventilateSwitch, standbySwitch, lightSwitch | leftTime, NightLight |
| `2HQI` | 四季沐歌智能晾衣机H100S | action, airDry, disinfect, drying, status, lightSwitch | commonFaultDetection |
| `2HR9` | 西蒙四位智能开关 | switch, switch1, switch2, switch3, switch4, indicator | commonFaultDetection, switchStatus |
| `2HZC` | 海曼(HEIMAN)智能可燃气体报警器 | switchNightLight, preheat, silencer, faultDetection, selfCheck, alarm | handonoff, AlarmType |
| `2I2E` | 晾霸智能晾衣机 | airDry, disinfect, drying, action, lightSwitch, status | disinfectRemTime, airDryTime, dryRemTime, airDryRemTime, disinfectTime, dryTime |
| `2IN4` | 九阳太空智能空气炸锅 | presetSwitch, switch, faultDetection, temperature, status, start | recipes, setWorkTime, workTime, preTimeEnd, preTimeStart, leftTime, cookTimes, independentRecipes, degerming, startCloudMenu |
| `2IU9` | 西蒙二位智能场景开关 | mode1, mode2, switch1, switch2, indicator, deviceStatus | sceneButton1, sceneButton2, commonFaultDetection |
| `2IVN` | 佳普乐G5-300A自动翻盖智能马桶 | mode, waterTemp, heatGear, drySwitch, dryGear, ECO | flush, seat, cover, nightled, wintenty, sitdown, hPosition, wPosition, smart, hintenty |
| `2IVO` | 佳普乐G5-400A自动翻盖智能马桶 | mode, waterTemp, heatGear, drySwitch, dryGear, ECO | wintenty, hPosition, hintenty, smart, wPosition, sitdown, flush, nightled, seat, cover |
| `2IVS` | 佳普乐G6-300A自动翻盖智能马桶 | mode, waterTemp, heatGear, drySwitch, dryGear, ECO | wPosition, smart, wintenty, hPosition, nightled, sitdown, hintenty, cover, flush, seat |
| `2IVT` | 佳普乐G6-400A自动翻盖智能马桶 | mode, waterTemp, heatGear, drySwitch, dryGear, ECO | cover, nightled, flush, sitdown, seat, smart, wintenty, wPosition, hPosition, hintenty |
| `2JFY` | AM35智能百叶帘 | changeDirection, rotationAction, opener, action, directionalmode, commonMode1 | Limit, JointLevel, SBZT |
| `2JNF` | 贝昂空气净化器A5 | switch, mode, fan, childLockSwitch, pm25, clean | — |
| `2JRH` | 消毒柜ZTD100S-02-X20.i | switch, faultDetection, action, cabinetMode, cabinetDoor, status | cabinetRemainingTime |
| `2JXK` | 贝克巴斯垃圾处理器E60PRO | mode, faultDetection, start, reverse, status, gear | — |
| `2K26` | 喜德盛智能电助力自行车 | speed, powerSwitch, lockSwitch, autolockGear, cruiseSwitch, seekSwitch | commonFaultDetection, pushCarSwitch, calories, brebr, carbon, currentTime, electrogenesis, CurrentMileage, heartRate, cyclingMode, inspection, ridingExtra, statusOder, securityLock, ridingSwitch, powerIntensity, power, mileage, SOC, cyclingGear, chargingStatus, rateLimiting, unitsSetup, screenBacklightGear, callerIDswitch, cyclingNavigation, signalIntensity |
| `2K2D` | 科威德迩空气消毒机CD-EL30 | switch, mode, fan, pm25, childLockSwitch, volume | filterElement1, alarm1, time |
| `2K88` | 霍尼韦尔空气净化器KJ560F-P22R | UVSwitch, switch, mode, fan, pm25, tvoc | filterElement1, filterElement2 |
| `2KCI` | F20蒸烤一体机 | switch, lackWater, faultDetection, temperature, action, status | leftTime, preHeatPrg, dStat, runStat, ClnMode, aTime, typeMode, id, devMode, cGear1a, cUTemp1a, cSubMode1a, cTime1a |
| `2KD6` | 顾家功能沙发 | seatStatus, oneKeyReset, headLegControl, memoryControl1, memoryControl2, modeSelect | positionSelect, AfterSales |
| `2KF0` | 奥克斯智能门锁HM-620 | lockState, lockMode, battery, alarm, openEvent, Volume | keyList, userlist, remoteResult, publicKey, remoteCode, remoteInfo |
| `2KHB` | JWV12-A2洗碗机 | presetSwitch, switch, mode, faultDetection, action, status | preTimeStart, preTimeEnd, leftTime, runningstatus, funcmode, funcstep, washfinishstat, RemainingTimeD |
| `2KOY` | 梦幻极光 | switchSpeed, rotationAction, opener, rotationAngle, action, directionalmode | — |
| `2LGR` | 科威德迩空气消毒机CD-VHW | switch, mode, fan, faultDetection, light, status | filterElement1, allstatus, ATVOC, time, quality |
| `2LNI` | 易百珑双色温灯带 | lightMode, donotDisturb, switch, brightness, cct, colourMode | CustomPair, CleanPair2, ScenePair, CleanPair1 |
| `2LOJ` | 燃气壁挂炉 | switch, maintenanceStatus, faultDetection, coStatus, bathTemperature, heatTemperature | burningTime, Gas |
| `2LVK` | 易百珑RGBW灯带 | lightMode, donotDisturb, switch, colour, brightness, colourMode | CleanPair2, ScenePair, CustomPair, CleanPair1 |
| `2M5M` | 香百年智能香薰机Pro | autoConnect, battery, gear, mode, scent, switch | FirmwareUpdate, margin, numberofcycles, durationtime |
| `2M9H` | 云鲸智能拖扫一体机器人J3 | battery, mode, faultDetection, gear, action, status | robotBaseStatus, robotWorkingStatus, revokeDeviceAuth, narwalCmd |
| `2MKE` | ELECTA智能取暖器 | switch, mode, faultDetection, childLockSwitch, gear, temperature | Time |
| `2MKS` | 贝昂空气净化器X5S | switch, mode, fan, childLockSwitch, pm25, clean | hchoDensity |
| `2MMH` | 空气净化器KJ300G-M2 | switch, mode, fan, anionSwitch, screenSwitch, temperature | AirQuality, filtervalue, UVselect, humility, PM25Value |
| `2N1F` | PGG眼部按摩仪E6 | mode, battery, temperature, externalaudioSwitch, status, switch | audioplayer, bt.connection, music, countdownOff, hotCompress, atomization |
| `2N1L` | 极米RS 10 mini | controlMode, menu, home, setting, focusauto, return | POWER, VOLUMEPRESS, KPPOWER, RESTART, VOLUMEUP, VOLUMEDOWN, FOCUSLEFT, FOCUS, FOCUSRIGHT |
| `2N2I` | 慕思BCI1-028电动床 | oneKeyReset, backControl, modeSelect, sleepstatus, legControl, pause | positionSelect, leftBreath, leftHeart, secret, rightHeart, rightBreath |
| `2N2V` | 慧曼流光系列洗碗机B1max-4 | switch, mode, action, status, light, rinse | remainTime, doorOpen, errorTip, appointment, salt, modeFeature, curTemp |
| `2N59` | 晾霸智能晾衣机Q2烘干王 | airDry, disinfect, drying, action, lightSwitch, status | disinfectRemTime, airDryTime, dryRemTime, airDryRemTime, disinfectTime, dryTime |
| `2N5S` | 杜亚智能梦幻帘 | changeDirection, rotationAction, switchSpeed, opener, rotationAngle, action | — |
| `2N6O` | meipont美邦燃气热水器 | switch, faultDetection, temperature, antifreezeStatus, flameStatus, status | watercontrol, waterloop, waterboost |
| `2N8J` | 好太太智能晾衣机 1295H | airDry, disinfect, drying, action, lightSwitch, status | disinfectRemTime, airDryTime, dryRemTime, airDryRemTime, disinfectTime, dryTime, commonFaultDetection |
| `2N9C` | 优慧家零冷水燃气热水器HA168GR | inletTemperature, switch, faultDetection, temperature, status, preheat | totalWater, totalGas, burningTime, curWater, custom, pretask, boost |
| `2N9D` | 优慧家燃气热水器HB162G | inletTemperature, switch, faultDetection, temperature, status, lock | totalWater, totalGas, burningTime, curWater, custom |
| `2NBK` | A.O.史密斯热泵热水器HPA-DAH系列 | mode, faultDetection, instantHeatSwitch, temperature, switch, status | PumpCircle, Timer1, Timer2, AES |
| `2NDD` | meipont美邦燃气热水器 | switch, mode, faultDetection, temperature, flameStatus, status | priority, targetWater |
| `2NDN` | 根元净护刺客AP004 | switch, action, mode, status, faultDetection, lightMode | leftTime, curTime, timing5, timing4, timing3, timing2, timing1, turnLightOffDelay, ringLightCCT, pyroelectricState, chargeState, remianCapacity, ringLightBrightness |
| `2NOM` | 森森智能鱼缸控制器 | switch3, switch2, switch1, waterTemp, switch4, lightSwitch | phMonitor, commonFaultDetection |
| `2NZZ` | Hitick高速智能剃须刀7系 | mode, battery, status, clean, lock, motor | deviceVersion, unusual, knifereset, state, hibernate, charge, cleaningCompartment, drip |
| `2O45` | 菠萝斑马智能床 | oneKeyReset, childLockSwitch, memoryControl1, memoryControl3, memoryControl2, modeSelect | BackAngel, LegAngel, SnoringMonitor |
| `2O5D` | 优慧家燃气热水器HB132G | inletTemperature, switch, faultDetection, temperature, status, lock | totalWater, totalGas, burningTime, curWater, custom |
| `2O6G` | meipont智能洗衣机 | switch, mode, faultDetection, action, childLockSwitch, status | rinseTimes, leftTime, Watertemp, Intense, Turnpeed, Pretimeover, Prewash, Soak, Steam |
| `2O9P` | 云鲸智能扫拖一体机器人J5 | battery, mode, faultDetection, action, gear, status | zoneManagement, availableZones, commonFilterElement1, commonFilterElement2, commonFilterElement3, commonFilterElement4, robotWorkingStatus, narwalReport, getMap, narwalCmd, robotBaseStatus, reqToken, revokeDeviceAuth |
| `2O9R` | 华为悦彰家庭影院 | brightness, volume, commonMode, commonMode1, commonMode2, commonExecution | acousticsAbility2, playSource, stereo, stereoDeviceTest |
| `2OF2` | 物联网断路器AICB2C-3P | action, ctrl, proSwitch, proTemp, status, temp | count, curNeutral, phaseA, phaseB, phaseC, power, proOc, proOuv, totalForwardEnergy, commonFaultDetection |
| `2OH0` | 亚都加湿器SZ750-TJK800(Hi)Pro | switch, faultDetection, temperature, humidity, childLockSwitch, gear | lamp, state, dried, timing, anion, uv, level |
| `2OO5` | 璟睿UnitLink影音中控主机 | soundMode, mute, switch, volume, micVolume, sceneMode | interfaceControl, playControl, sceneEnable, micMute, ktvCtrl |
| `2OP8` | 唯妙智能影音控制主机全屋款 | soundMode, mute, switch, volume, micVolume, musicVolume | interfaceControl, playControl |
| `2OQ1` | 慧曼流光洗碗机 | switch, mode, action, status, rinse, light | remainTime, doorOpen, salt, curTemp, appointment, errorTip, modeFeature |
| `2OQ2` | 慧曼溢彩洗碗机 | switch, mode, action, status, rinse, light | curTemp, doorOpen, salt, errorTip, remainTime, appointment, modeFeature |
| `2OQA` | 玛格智能调光灯带控制器 | lightMode, donotDisturb, switch, cct, colour, brightness | Colorselect |
| `2OR1` | 科技热敷带T3 | heat, switch, mode, battery, massage, alarm | TemperatureGears, shutdown, BLEstatus, HotCompress, countdown |
| `2OW9` | MEIPONT飞凡智能挂机空调S10(Pro) | switch, mode, fan, temperature, sceneMode, light | commonFaultDetection, PtcHeat |
| `2OWZ` | BENERGIA制冰饮水机 | coolSwitch, faultDetection, iceSwitch, mode, status, temperature | currentTemp, iceMaking, output, tanklocation, waterTank |
| `2OY5` | 慧曼天女洗碗机 | switch, mode, action, status, rinse, light | doorOpen, curTemp, salt, errorTip, remainTime, appointment, modeFeature |
| `2OYR` | AiRELAXS芝华仕智能床 P1 | childLockSwitch, headControl, legControl, modeSelect, oneKeyReset, status | awaken |
| `2P4A` | 佳普乐星辰恒温智控花洒 | coldWaterSwitch, waterOutletSwitch, switch3, switch2, temperature, status | — |
| `2P6N` | IH 智能方煲 | action, faultDetection, presetSwitch, warmSwitch, mode, status | keptWarmTime, setWorkTime, leftTime, preTimeStart |
| `2PFB` | 元响智能音乐主机 | deviceStatus, mute, volume, systemMode, playStatus, switch | interfaceControl |
| `2PFV` | 小适智能剃须刀T3S | battery, mode, bladeStatus, status, switch, travelLock | bladeReset |
| `2PQ3` | THINCO智能台灯 5Pro | brightness, childLockSwitch, lightMode, lightAdaptionSwitch, nightModeSet, switch | lightFormulaArray, longTimeAlarm, preLightFormulaArray, preview, progressTurnOn, seatOffLightSet, seatOnLightSet, timeSync, usageRecord |
| `2PXZ` | 贝昂无耗材空气净化器X7PH | childLockSwitch, fanGear, hcho, mode, pm25, switch | autoClean |
| `2Q31` | 欧普照明SDL天辰吸顶灯 MX550 | brightness, cct, colour, colourMode, lightMode, switch | relBrightness, toggleSwitch, PowerUpStatus, WallSwitchSceneEn, InchingSwitch, FadeFunction, SunLightMode, ResetMode |
| `2Q39` | 欧普照明SDL天辰吸顶灯 MX900 | brightness, cct, colour, colourMode, lightMode, switch | relBrightness, toggleSwitch, PowerUpStatus, WallSwitchSceneEn, InchingSwitch, FadeFunction, SunLightMode, ResetMode |
| `2Q3A` | 欧普照明SDL天域晴空灯 | brightness, cct, colour, colourMode, lightMode, switch | relBrightness, toggleSwitch, PowerUpStatus, InchingSwitch, WallSwitchSceneEn, FadeFunction, SunLightMode, ResetMode |
| `2QJJ` | 多功能暖风机(杀菌烘干功能) | action, childLock, mode, status, switch, temperature | progress |
| `2QJV` | 奥马全嵌母婴冰箱520PLUS | flexiTempZone, freezeSwitch, intelligentSwitch, refrigerateSwitch, refrigerationSwitch, status | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `2QM2` | 恩仕AXENT.NOVIA挂墙智能坐便器 | autoFlip, massageMode, offSeatAction, seatStatus, stop, toiletStatus | drySetting, foamShield, seatHeating, toiletSetting, washSetting |
| `2QQL` | 恩仕AXENT.NOVIA落地智能坐便器 | autoFlip, massageMode, offSeatAction, seatStatus, stop, toiletStatus | drySetting, foamShield, seatHeating, toiletSetting, washSetting |
| `2QRH` | 三菱电机空调壁挂机LC系列 | fan, keyToneSwitch, mode, humidity, switch, temperature | capabilityset, electric, commonFaultDetection |
| `2QUI` | 奥马全嵌母婴冰箱520阿尔卑斯白 | flexiTempZone, freezeSwitch, intelligentSwitch, refrigerateSwitch, refrigerationSwitch, status | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `2QUJ` | 奥马全嵌母婴冰箱508Pro | flexiTempZone, freezeSwitch, intelligentSwitch, refrigerateSwitch, refrigerationSwitch, status | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `2QVT` | 恩仕AXENT.NOVIA暗装智能淋浴器 | coldWaterSwitch, mode, status, waterOutletSwitch, temperatureSetting, waterGear | commonFaultDetection |
| `2QYO` | 智能多功能煲 | action, mode, presetSwitch, realBladeStatus, status, temperature | leftTime, preTimeEnd, preTimeStart, recipes, setWorkTime, workTime, commonFaultDetection |
| `2R13` | RO反渗透加热一体净水机 | flushSwitch, mode, noMoreOvernightWater, status, tempMode, waterMode | filterElement1, filterElement2, commonFaultDetection |
| `2R3J` | eachone一起玩  智能吸顶灯B3 | brightness, cct, inchingSwitch, lightMode, switch, commonMemorySwitch | nightWakeup, progressSwitch, progressTurnOn, progressTurnOff |
| `2R61` | 佳普乐星泽智联淋浴花洒 | coldWaterSwitch, status, switch2, switch3, temperatureSetting, screenSwitch | commonFaultDetection |
| `2R63` | Hitick高速智能剃须刀7系Pro | battery, mode, bladeStatus, status, switch, travelLock | bladeClean, bladeReset, record, commonFaultDetection |
| `2R8A` | 物联网断路器AICB2C-2PB | action, ctrl, proSwitch, proTemp, status, temp | count, curNeutral, phaseA, power, proLeak, proOc, proOuv, totalForwardEnergy, commonFaultDetection |
| `2RCE` | 康茂多功能暖风机(杀菌烘干功能) | action, childLock, mode, status, switch, temperature | progress |
| `2RD9` | 格丽思便捷烧水杯G-C400 | hydrogenProduction, hydrogenProductionSwitch, lightMode, status, switch, temperature | commonFaultDetection |
| `2RF1` | 一起玩eachone   全面屏无边框吸顶灯 | brightness, cct, inchingSwitch, lightMode, switch, commonMemorySwitch | lightFormulaArray, nightWakeup, preview, progressSwitch, preLightFormulaArray, progressTurnOn, progressTurnOff |
| `2RFQ` | HWHL华伟宏亮智能吸顶灯 | auxBrightness, auxSwitch, brightness, cct, lightMode, switch | progressSwitch |
| `2RHC` | 一起玩eachone 自然光吸顶灯Max版 | brightness, cct, inchingSwitch, lightMode, switch, commonMemorySwitch | nightWakeup, progressTurnOn, progressSwitch, progressTurnOff |
| `2RKB` | 舒适暖宫带C5V3充电仓款 | battery, hot, hotSwitch, massage, massageSwitch, switch | countDown, time |
| `2RL5` | 台铃-罗马 | battery, lockSwitch, powerSwitch, seatSwitch, seekSwitch, status | mileage |
| `2RLA` | 台铃-黑鲨 | battery, lockSwitch, powerSwitch, seatSwitch, seekSwitch, status | mileage |
| `2RLG` | 台铃-封神 | battery, lockSwitch, powerSwitch, seatSwitch, seekSwitch, status | mileage |
| `2RLH` | 台铃-赤兔2025 | battery, lockSwitch, powerSwitch, seatSwitch, seekSwitch, status | mileage |
| `2RLX` | HWHL华伟宏亮智控星闪灯 | auxBrightness, auxSwitch, brightness, cct, lightMode, switch | progressSwitch |
| `2RNC` | 西顿照明T5无线RGBCW灯带照明驱动 | brightness, cct, colour, indicator, switch, commonMemorySwitch | fadeTimeSetting, lightCurveSetting, relBrightness, commonFaultDetection |
| `2RNU` | 贝昂空气净化器X5S V1 | childLockSwitch, fan, hcho, mode, pm25, switch | autoClean |
| `2RUH` | 三菱电机空调壁挂机LC16 | fan, keyToneSwitch, mode, humidity, switch, temperature | capabilityset, electric, commonFaultDetection |
| `2RVW` | 鸿蒙智选 云鲸JX扫地机器人 | action, battery, mode, faultDetection, gear, status | zoneManagement, availableZones, commonFilterElement1, commonFilterElement2, commonFilterElement3, commonFilterElement4, commonFilterElement5, commonFilterElement6, commonFilterElement7, reqToken, robotBaseStatus, getMap, revokeDeviceAuth, robotWorkingStatus, narwalReport, narwalCmd |
| `2RVX` | 鸿蒙智选 云鲸逍遥003扫地机器人 | action, battery, mode, faultDetection, gear, status | zoneManagement, availableZones, commonFilterElement1, commonFilterElement2, commonFilterElement3, commonFilterElement4, robotBaseStatus, reqToken, narwalReport, narwalCmd, robotWorkingStatus, revokeDeviceAuth, getMap |
| `2RYO` | 力博得智能冲牙器 博享 | battery, voiceGuidance, status, switch, mode, workGuidance | setWorkTime, applicatorTime, filterElement, cleaningRecord, commonFaultDetection |
| `2S2G` | 佳普乐宏尚智联毛巾架 | disinfect, drying, heat, indicator, nightlightSwitch, status | dryingLeftTime, dryingTime |
| `2S8V` | 贝昂无耗材空气净化器X7P(H) Pro | childLockSwitch, fan, hcho, mode, pm25, switch | autoClean |
| `2SHO` | 恩仕AXENT.META暗装智能淋浴器 | coldWaterSwitch, mode, temperatureSetting, waterGear, status, waterOutletSwitch | commonFaultDetection |
| `2SKV` | 捷德韦尔智能灯 | auxSwitch, brightness, cct, lightMode, switch, commonMemorySwitch | progressSwitch |
| `2SQL` | 诺克智能灯 | auxSwitch, brightness, cct, lightMode, switch, commonMemorySwitch | progressSwitch |
| `A06X` | 博世烘干机 | switch, action, mode, dryMode, status, doorLockSwitch | — |
| `A08L` | 美的智能冰箱 | switch, refrigerateSwitch, freezeSwitch, intelligentSwitch, refrigerator, freezer | — |
| `A091` | 博世冰箱 | switch, refrigerateSwitch, freezeSwitch, refrigerator, freezer, faultDetection | — |
| `A0KD` | 博世蒸汽烤箱 | switch, status, mode, action, temperature, faultDetection | workTime, setWorkTime, preTimeStart, leftTime |
| `A0KI` | 博世全自动咖啡机 | switch, mode, action, temperature, gear, status | currentOutlet |
| `A0VT` | COLMO净水机 | switch, status, mode, rinseMode, temperature, water | waterSpeed, filterElement1, filterElement2, filterElement3, commonFilterElement1, commonFaultDetection |
| `A0Z6` | 西门子空调1 | switch, mode, temperature, fan, faultDetection, childLock | deviceName, energy, SleepMode |
| `A12Z` | COLMO干衣机 | switch, action, mode, status, presetSwitch, faultDetection | preTimeEnd, leftTime |
| `A13C` | 方太蒸箱SCD48-M1A.i | switch, status, mode, lackWater, gateState, temperature | leftTime, WorkMode, WaterShortage, AppointmentFlag |
| `A1PI` | 小天鹅滚筒洗衣机 | switch, action, mode, status, faultDetection, presetSwitch | workTime, preTimeEnd, leftTime |
| `A1RH` | COLMO抽油烟机CXKCP924W-Z6 | mode, faultDetection, lightSwitch, gear, status, switch | — |
| `A1VR` | 小天鹅 TH100-H81WY 10公斤 热泵干衣机 | action, switch, mode, faultDetection, presetSwitch, status | leftTime, preTimeEnd, heatTime |
| `A1Z5` | JWV12-A6洗碗机 | switch, action, status, mode, temperature, addMode | leftTime, preTimeEnd, commonFaultDetection, modeSwitch, orderSwitch, timeSet, remainingTime, brightener, washingSalt |
| `A1ZG` | JWB12-B5洗碗机 | switch, action, status, mode, temperature, addMode | preTimeEnd, commonFaultDetection, remainingTime, timeSet, orderSwitch, washingSalt, brightener |
| `A2AS` | 美的 MH100-H10WY 10公斤 热泵干衣机 | switch, action, mode, status, presetSwitch, faultDetection | preTimeEnd, leftTime |
| `A2AT` | 小天鹅 TH100-H9WZ 10公斤 热泵干衣机 | switch, action, mode, status, presetSwitch, faultDetection | preTimeEnd, leftTime |
| `A2B3` | COLMO CLGS10CE-Z 10公斤 滚筒洗衣机 | switch, action, mode, status, faultDetection, presetSwitch | workTime, preTimeEnd, leftTime |
| `A2B4` | COLMO CLHS10CE-Z 10公斤 热泵干衣机 | action, switch, mode, faultDetection, presetSwitch, status | leftTime, preTimeEnd, heatTime |
| `A2EN` | COLMO抽油烟机CXSP927W-SS8 | mode, faultDetection, lightSwitch, gear, status, switch | — |
| `A2FY` | 小天鹅 10公斤 热泵干衣机 | presetSwitch, switch, mode, faultDetection, action, status | preTimeEnd, leftTime, heatTime |
| `A2GT` | 西门子嵌入式洗碗机 | switch, action, status, mode, temperature, faultDetection | lefttime1 |
| `A2GU` | 西门子半嵌入式洗碗机 | switch, action, status, mode, temperature, faultDetection | lefttime1 |
| `A2J4` | 美的暖风机HFX22AR1 | switch, temperature, mode, childLockSwitch, faultDetection, swingSwitch | tempCtrlSwitch, preTimeOff, screenOffSwitch, preTimeOn |
| `A2OA` | CXW-200-E6090H吸油烟机 | mode, lockSwitch, lightSwitch, gear, status, switch | commonFaultDetection, wacaStat, lockScreen, lockSwtich, delayedShutdown, lockStat, gearStat |
| `A2W0` | JWB19-B8洗碗机 | switch, mode, faultDetection, action, status, addMode | leftTime, washingSalt, brightener |
| `A2YO` | yeedi全能扫拖机器人CC | battery, cleanMode, action, status, vacuumGear, waterLevel | commonFaultDetection |
| `A30A` | 智汇云音乐律动灯 | switch, colour, brightness, colourMode, cct, mode | turnoffTime, turnonTime, rhythm, gradient |
| `A32V` | TCL新风柜式空调 | switchEco, mode, switchLight, temperature, switch, gear | horizontalWind, newWindPercentage, sleep, newWindECOSwitch, softWind, newWindSwitch, beepSwitch, verticalWind, windSpeedAutoSwitch, PTC |
| `A33H` | TCL柜式空调 | switchEco, mode, switchLight, temperature, switch, gear | PTC, windSpeedAutoSwitch, verticalWind, beepSwitch, softWind, sleep, horizontalWind |
| `A344` | 美的踢脚线取暖器 | switch, mode, temperature, gear, childLockSwitch, status | commonFaultDetection, preTimeOff, preTimeOn |
| `A3A4` | 美的抽油烟机 | lightSwitch, status, gear, linkageStatus, switch, workBurnerStatus | commonFaultDetection |
| `A3A6` | 美的净界星云风扇 | switch, mode, fan, onOffBeep, darkMode, status | waterions, delayOff, preOn |
| `A3A8` | 美的循环扇 | switch, mode, fan, onOffBeep, darkMode, status | preOn, delayOff |
| `A3AL` | COLMO图灵二代中央空调 | switch, mode, fan, temperature, humidity, automaticAirswitch | — |
| `A3B5` | 美的中央空调86T5 | switch, mode, ptcSwitch, fan, temperature, humidity | ptcEnable |
| `A3D0` | COLMO智能油烟机 | lightSwitch, status, gear, linkageStatus, switch, workBurnerStatus | commonFaultDetection |
| `A3DG` | 美的抽油烟机 | lightSwitch, status, gear, linkageStatus, switch, workBurnerStatus | commonFaultDetection |
| `A3DS` | COLMO睿极风管机 | switch, mode, fan, temperature, sceneMode, automaticAirswitch | — |
| `A3DX` | COLMO睿极风管机 | switch, mode, fan, temperature, sceneMode, automaticAirswitch | — |
| `A3EP` | 方太智能冰箱 | disinfectSwitch, intelligentSwitch, refrigerateSwitch, freezeSwitch, freezer, refrigerator | commonFaultDetection, dormancyPreservation, nitrogenFlushing, freezedRoom |
| `A3F4` | COLMO新风空调 | switch, mode, fan, freshAirSwitch, temperature, freshAirgear | — |
| `A3HS` | 方太智能消毒柜 | action, cabinetMode, cleaningSwitch, machineStatus, cabinetDoor, switch | cabinetRemainingTime, commonFaultDetection |
| `A3IR` | A.O.史密斯智能油烟机S系列 | lightSwitch, lockSwitch, gear, leftFanSwitch, rightFanSwitch, switch | commonFaultDetection |
| `A3JP` | COLMO冰箱CRBUF706NX1 | aiFfSwitch, aiSwitch, aiVersatileCabin, disinfectSwitch, iceMode, refrigerateSwitch | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3JQ` | COLMO冰箱CRBUS601X1 | aiSwitch, disinfectSwitch, freshTemperature, iceMode, refrigerateSwitch, status | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3JR` | COLMO冰箱CRBUK600DZ5 | disinfectSwitch, flexiTempCabin, freezeSwitch, iceMode, photonSwitch, refrigerateSwitch | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3JS` | COLMO冰箱CRBUF600X1 | aiFfSwitch, aiSwitch, aiVersatileCabin, disinfectSwitch, iceMode, refrigerateSwitch | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3JT` | COLMO冰箱CRBUF600AX1A | aiFfSwitch, aiSwitch, aiVersatileCabin, disinfectSwitch, iceMode, refrigerateSwitch | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3JV` | COLMO冰箱CRBUF518WHJ1 | disinfectSwitch, freezeSwitch, iceMode, lockNutrientCabin, photonSwitch, refrigerateSwitch | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3JW` | COLMO冰箱CRBUS517WHJ1 | disinfectSwitch, freezeSwitch, iceMode, lockNutrientCabin, photonSwitch, refrigerateSwitch | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3JZ` | COLMO冰箱CRBUK603MA2 | disinfectSwitch, flexiTempCabin, freezeSwitch, iceMode, photonSwitch, refrigerateSwitch | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3K0` | COLMO 冰箱 CRBUK603WQ2 | disinfectSwitch, flexiTempCabin, freezeSwitch, iceMode, photonSwitch, refrigerateSwitch | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3K1` | COLMO冰箱CRBUS531FDA6 | aiVersatileCabin, disinfectSwitch, freezeSwitch, iceMode, refrigerateSwitch, status | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3KR` | COLMO冰箱CRBUF706NX1云璃白 | aiFfSwitch, aiSwitch, aiVersatileCabin, disinfectSwitch, iceMode, refrigerateSwitch | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3KS` | COLMO冰箱CRBUF706NX1星砂钢 | aiFfSwitch, aiSwitch, aiVersatileCabin, disinfectSwitch, iceMode, refrigerateSwitch | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3KT` | COLMO冰箱CRBUF706NX1雪山岩 | aiFfSwitch, aiSwitch, aiVersatileCabin, disinfectSwitch, iceMode, refrigerateSwitch | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3KU` | COLMO冰箱CRBUF706NX1量子灰 | aiFfSwitch, aiSwitch, aiVersatileCabin, disinfectSwitch, iceMode, refrigerateSwitch | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3KV` | COLMO冰箱CRBUF706NX1星云钢 | aiFfSwitch, aiSwitch, aiVersatileCabin, disinfectSwitch, iceMode, refrigerateSwitch | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3LM` | COLMO冰箱CRBUF600X1星砂钢 | aiFfSwitch, aiSwitch, aiVersatileCabin, disinfectSwitch, iceMode, refrigerateSwitch | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3LN` | COLMO冰箱CRBUF518WHJ1镜岩灰 | disinfectSwitch, freezeSwitch, iceMode, lockNutrientCabin, photonSwitch, refrigerateSwitch | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3LO` | COLMO冰箱CRBUS517WHJ1镜岩灰 | disinfectSwitch, freezeSwitch, iceMode, lockNutrientCabin, photonSwitch, refrigerateSwitch | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3N9` | 能率热水器GQ-16D6AFEX | flameStatus, increaseCapacitySwitch, status, switch, temperature, zeroColdMode | totalGas, totalWater, commonFaultDetection |
| `A3OR` | 美的冷塔扇 | fan, indicator, mode, neIon, switch, water | commonFaultDetection |
| `A3PI` | 好太太智能晾衣机 | action, airDry, disinfect, drying, lightSwitch, status | airDryRemTime, airDryTime, disinfectRemTime, disinfectTime, dryRemTime, dryTime, commonFaultDetection |
| `A3PT` | Leader柜机 | exhaustAirSpeed, fan, freshAirSpeed, mode, switch, temperature | commonFaultDetection |
| `A3Q1` | 美的立柜式空调BF1 | automaticAirswitch, fan, mode, preventStraightWindswitch, switch, temperature | commonFaultDetection |
| `A3R3` | 德业除湿机DYD-E12A3 | childLockSwitch, gear, humidity, mode, switch, temperature | waterTank |
| `A3RJ` | 德业除湿机U20 Air | anionSwitch, childLockSwitch, humidity, mode, switch, temperature | dehumidify, waterTank |
| `A3RK` | 老板电器热水器HT8 i1 Pro | boostMode, mode, status, switch, temperature, zeroColdSwitch | commonFaultDetection |
| `A3RX` | 德业除湿机DYD-D50A3 | childLockSwitch, gear, humidity, mode, switch, temperature | dehumidify, waterTank |
| `A3SL` | 箭牌智联马桶 | bigflushSwitch, hipNozzlePos, seatRing, seatStatus, toiletSeatCoverSwitch, toiletStatus | drySetting, foamShield, seatHeating, toiletSetting, washSetting |
| `A3ST` | 博世8系T10双吸油烟机 | gear, gestureSwitch, lightSwitch, linkageStatus, status, switch | delayOff, commonFaultDetection |
| `A3T0` | 箭牌智联马桶Pro | autoFlip, bigflushSwitch, hipNozzlePos, nightLight, seatStatus, toiletStatus | drySetting, foamShield, seatHeating, toiletSetting, washSetting |
| `A3U6` | 美的智能风扇灯 FW3 | brightness, cct, fan, lightMode, switchFan, switch | — |
| `A3UJ` | 美的风管机星光IV | switch, mode, fan, temperature, sceneMode, switchPTC | airConditioner, hvacType, commonFaultDetection |
| `A3WO` | 能率热水器GQ-16K6AAFEX | flameStatus, mode, status, switch, temperature, zeroColdMode | totalGas, totalWater, commonFaultDetection |
| `A3ZM` | 博世壁挂式迷你洗衣机 | action, childLockSwitch, switch, mode, presetSwitch, status | leftTime, commonFaultDetection, finishinRelative |
| `A3ZQ` | 嘉格纳200 系列独立式干衣机 | action, childLockSwitch, mode, presetSwitch, status, switch | leftTime, preTimeEnd, commonFaultDetection |
| `A424` | 嘉格纳200 系列独立式洗衣机 | action, childLockSwitch, switch, mode, presetSwitch, status | leftTime, preTimeEnd, commonFaultDetection |
| `A429` | 石头智能扫拖机器人 | action, baseAction, battery, status, vacuumGear, waterLevel | — |
| `A43S` | 石头自清洁扫拖机器人 | action, baseAction, battery, status, vacuumGear, waterLevel | commonFaultDetection |
| `A46J` | 嘉格纳 200 系列壁挂式吸油烟机 | gear, gestureSwitch, lightSwitch, linkageStatus, status, switch | delayOff, commonFaultDetection, delayShutdownSetting |
| `D000` | HUAWEI PixLab X1 | printerStatus, tonerStatus, copyJobStatus, scanJobStatus, faultDetection, netStatus | printJobStatus |
| `D001` | HUAWEI PixLab B5 | printerStatus, tonerStatus, copyJobStatus, scanJobStatus, faultDetection, netStatus | printJobStatus |
| `D0AP` | HUAWEI Printer CV81-WDMSE | printerStatus, tonerStatus, copyJobStatus, scanJobStatus, faultDetection, netStatus | printJobStatus |
| `D0AR` | HUAWEI Printer CV81Z WDMp | printerStatus, tonerStatus, copyJobStatus, scanJobStatus, faultDetection, netStatus | printJobStatus |
| `D0AT` | HUAWEI Printer CV81 WDMa | printerStatus, tonerStatus, copyJobStatus, scanJobStatus, faultDetection, netStatus | printJobStatus |
| `D0AU` | HUAWEI QingYun J5 Series | printerStatus, tonerStatus, copyJobStatus, scanJobStatus, faultDetection, netStatus | printJobStatus |
| `ZG08` | 华为全屋智能灯带驱动器 | switch, colourMode, brightness, cct, colour, faultDetection | subProduct |
| `ZG0I` | 智能开关 (无线版) 1键 | switch1, mode1, modeX, childLockSwitch, faultDetection, memorySwitch | button1, reboot |
| `ZG0O` | 华为全屋智能 1路 RGBCW 恒压 100W | switch, colourMode, brightness, cct, colour, faultDetection | subProduct |
| `ZG2O` | 迈腾智能开关 (无线版) 1键 | switch1, mode1, modeX, childLockSwitch, faultDetection, memorySwitch | button1, reboot |
| `ZG2R` | 智能开关 奥斯陆(无线版) 1键 | switch1, mode1, modeX, childLockSwitch, faultDetection, memorySwitch | button1, reboot |
| `ZG2X` | 智能开关 威尼斯(无线版) 1键 | switch1, mode1, modeX, childLockSwitch, faultDetection, memorySwitch | button1, reboot |
| `0103` | 灯组 | switch, brightness, colourMode, colour, cct | — |
| `0104` | 灯组 | switch, brightness, colourMode, colour, cct | — |
| `0105` | 灯组 | switch, brightness, colourMode, colour, cct | — |
| `100z` | 三思全彩灯泡 | switch, brightness, colour, cct, lightMode | delay |
| `101q` | 得邦智能台灯 | switch, brightness, colour, cct, lightMode | delay |
| `1027` | 美的加湿器 | switch, humidity, temperature, gear, faultDetection | — |
| `105L` | Hue智能调光灯泡(彩灯) | switch, lightMode, brightness, colour, cct | — |
| `1070` | 奥普吸顶灯AX560 | switch, brightness, colourMode, cct, lightMode | — |
| `107E` | LOEIN 乐因智能香薰灯 | switch, lightMode, brightness, colour, faultDetection | lightSwtich, aromaSwtich, aromaMode |
| `1080` | 欧普智能灯具 | switch, brightness, colourMode, cct, lightMode | delay |
| `111F` | 三思双色温灯泡 | switch, brightness, lightMode, colourMode, cct | delay |
| `113P` | Yeelight彩光灯泡 | switch, lightMode, cct, brightness, colour | delay |
| `113S` | Yeelight彩光灯带 | switch, lightMode, cct, brightness, colour | delay |
| `116F` | 博乐落地灯_FOL01 | switch, brightness, cct, colourMode, lightMode | delay |
| `117L` | 亚都加湿器SC700-SK071ProHi | switch, humidity, gear, water, light | sound, timing |
| `121N` | 亚摩斯足浴盆AS-FT100B | mode, command, status, currentTemperature, temperature | leftTime, workTime, cookInfo, faultCode |
| `121Q` | 土豆双色智能灯 | switch, brightness, backlight, lightMode, cct | delay |
| `122O` | 艾美特移动地暖WD22-A1 | switch, childLockSwitch, temperature, faultDetection, screenSwitch | timing, state |
| `124R` | 鸿雁WIFIUSB智能排插 | switch, switch1, switch2, switch3, usbSwitch1 | protect, switchLock |
| `132S` | 亚都加湿器SZ300-JK361Hi | switch, humidity, gear, light, water | sound, Anion, timing |
| `134D` | 华为智选 欧普读写台灯 | switch, backlight, brightness, lightMode, cct | nightSwitch, delay |
| `134R` | U2C-智能护眼台灯-GD-TDW12B | switch, brightness, colourMode, cct, lightMode | delay |
| `145Z` | 达伦自然光台灯X3Pro | switch, brightness, colourMode, colour, cct | delay, NightLightSwitch, MainLightSwitch, RGBSwitch, ColourAutoChange, SleepMode |
| `156A` | 欧派油烟机 | switch, gear, mode, lightSwitch, faultDetection | stirFriedOff, delayOff, autoTurnOff |
| `166O` | 艾美特暖风机HPA21203R-H | switch, mode, childLockSwitch, temperature, screenSwitch | state, swayLeftRight, timing |
| `171W` | A.O.史密斯零冷水VJS系列 | switch, machineSafeStatus, waterControl, temperature, mode | burningStatus, loopStatus, gasSafeStatus, noColdWaterMode, noColdWater, boost, faultCode |
| `172M` | 三思智毅Pro护眼台灯 | switch, brightness, colourMode, cct, lightMode | reading, relax |
| `172O` | 安士宝智能奶瓶 | status, heat, battery, childLock, disinfect | currentTemp, heatTemp, disinfectRec |
| `174B` | 三思读写台灯 | switch, brightness, colourMode, cct, lightMode | tomatoClk, writing, reading, relax, loving |
| `174Z` | 净诺抗菌除醛空气净化器 | switch, childLockSwitch, anionSwitch, pm25, fan | cav, Auto, cmw1, Presskeytone, sleep, Killscreen, filterElement |
| `175J` | 艾美特移动地暖HD30-A9 | switch, mode, childLockSwitch, temperature, screenSwitch | state, heatingArea, timing |
| `175N` | 艾美特移动地暖HD25-A7 | switch, mode, childLockSwitch, temperature, screenSwitch | state, timing |
| `175Y` | 艾美特移动地暖D22 | switch, childLockSwitch, temperature, faultDetection, screenSwitch | state, timing |
| `178K` | 亚都加湿器SZ300-JK262Hi | switch, humidity, gear, light, water | Anion, timing, sound |
| `178L` | 海尔空气净化器KJ450F-M900A | switch, mode, childLockSwitch, pm25, fan | filterElement1 |
| `178O` | 西顿锋芒智能灯带 | switch, brightness, lightMode, colourMode, cct | — |
| `182Q` | Momax无线充护眼台灯 | switch, brightness, colourMode, cct, lightMode | tomatoClk, delay, EyeProtection |
| `183S` | 索菲莉尔智能电动床200 | headControl, legControl, lieControl, modeSelect, stop | — |
| `183W` | 三思读写台灯TD05 | switch, brightness, colourMode, cct, lightMode | tomatoClk, delay, loving, relax, writing, reading |
| `184O` | 博乐智能吸顶灯 | switch, brightness, lightMode, colourMode, cct | delay |
| `2000` | 欧普读写台灯3Pro | switch, brightness, colourMode, cct, lightMode | tomatoClk, nightWakeup |
| `200N` | 易百珑三路开关 | switch, memorySwitch, switch1, switch2, switch3 | Pair, CleanPair |
| `2026` | 蓓慈足浴器BZ528V1 | switch, mode, status, temperature, faultDetection | leftTime, Settime, SetTemperature, momo, Red |
| `203Q` | 阿特兰斯双线CCT控制器 | switch, brightness, colourMode, cct, lightMode | Match |
| `204I` | 蓓慈足浴器BZ525V1 | switch, mode, status, temperature, faultDetection | leftTime, surfHeating, setTime, setTemperature |
| `204L` | 亚都加湿器SC300-SK045ProHi | switch, humidity, childLockSwitch, gear, light | capacity, timing, sound |
| `206N` | 高盛达智能吸顶灯 | switch, brightness, lightMode, colourMode, cct | — |
| `207U` | 达伦21W吸顶灯C23NTHW | switch, brightness, lightMode, colourMode, cct | NightMode |
| `20B5` | 亚都空气净化器KJ350F-PT2000Hi | switch, childLockSwitch, pm25, fan, light | filterElement1, sound |
| `20BE` | 新风门窗 | status, mode, switch, heatSwitch, fan | filterElement1 |
| `20FB` | 亚摩斯电炖锅AS-WD40F | status, action, mode, presetSwitch, faultDetection | workTime, setWorkTime, leftTime, preTimeEnd, warmTime |
| `20GL` | 万和热水器S5系列 | switch, mode, status, temperature, faultDetection | TotalGas, ZCTempSet, TotalWater, zerocold, HotLabor, AffSetting, TotalAff, CurGas, InWTemp |
| `20HZ` | 达伦吸顶灯 | switch, brightness, colourMode, cct, lightMode | NightMode |
| `20IA` | 亚摩斯电饭煲AS-WF20S | status, action, mode, presetSwitch, faultDetection | workTime, leftTime, preTimeEnd, warmTime |
| `20IB` | 亚摩斯电饭煲AS-WF40SG | status, action, mode, presetSwitch, faultDetection | workTime, setWorkTime, leftTime, preTimeEnd, warmTime |
| `20K0` | 亚摩斯电饭煲AS-IHW40K | status, action, mode, presetSwitch, faultDetection | workTime, setWorkTime, leftTime, preTimeEnd, warmTime |
| `20KM` | 鸿雁WIFI智能排插 | switch, switch1, switch2, switch3, switch4 | protect, switchLock |
| `20PO` | 亚都智能恒湿加湿器045Pro(Hi)2.0 | switch, humidity, childLockSwitch, gear, light | capacity, sound |
| `20PX` | 亚摩斯降糖电饭煲AS-WFT30L | status, action, mode, presetSwitch, faultDetection | workTime, setWorkTime, leftTime, preTimeEnd, warmTime |
| `20Q0` | 柔光护眼圆盘台灯 | switch, brightness, colourMode, cct, lightMode | tomatoClk, delay, loving, writing, reading, relax |
| `20QC` | 亚摩斯电饭煲AS-IHW30H | status, action, mode, presetSwitch, faultDetection | workTime, setWorkTime, leftTime, preTimeEnd, warmTime |
| `20R2` | 海尔空气净化器KJ200F-M900A | switch, mode, childLockSwitch, pm25, fan | filterElement1 |
| `20RG` | 威诺华智能灯泡 | switch, brightness, colourMode, cct, lightMode | — |
| `20VY` | 亚摩斯智能筒灯 | switch, brightness, colourMode, cct, lightMode | — |
| `20Y9` | 好太太智能晾衣机HP-D204-2BS | action, airDry, disinfect, drying, lightSwitch | airDryRemTime, airDryTime, dryRemTime, dryTime, commonFaultDetection |
| `2151` | 圆和四路智能开关 | switch, switch1, switch2, switch3, switch4 | — |
| `2155` | 施铂智能恒温电热水壶 | mode, status, temperature, warmSwitch, faultDetection | watime, warmswitch1, boolwater, warmtime |
| `215H` | 施铂智能加湿器 | switch, humidity, childLockSwitch, gear, faultDetection | commonFilterElement1, AUTO, Water, MOTO, FanMode, BEE, SLEEP |
| `215O` | 触控四开零火开关 | switch, switch1, switch2, switch3, switch4 | — |
| `218D` | 西门子微蒸烤一体机 | switch, status, mode, childLock, faultDetection | control, devDoor, localFood, favorite, leftTime |
| `218J` | 亚摩斯电压力锅AS-YDG503Z | mode, action, status, presetSwitch, faultDetection | food, workTime, setWorkTime, preTimeStart, leftTime, pression |
| `21BV` | 新风水地暖温控器 | freshAirSwitch, heatSwitch, childLockSwitch, fan, temperature | — |
| `21EP` | JW空气检测A型 | temperature, humidity, pm25, hcho, tvoc | co2, pm10 |
| `21GG` | JW空气检测B型 | temperature, humidity, pm25, hcho, tvoc | co2 |
| `21GV` |  | switch, mode, temperature, fan, discovery | — |
| `21JC` | 阳光照明灵睿智能灯泡调光调色版 | switch, brightness, colourMode, cct, lightMode | delay |
| `21JD` | 阳光照明灵睿智能灯泡RGBW版 | switch, brightness, lightMode, colourMode, colour | streamer, delay, coolwhitemode |
| `21Q0` | 欧普智能筒灯 | switch, brightness, colourMode, cct, commonMemorySwitch1 | — |
| `21UN` | 三思LED吸顶灯 | switch, brightness, lightMode, colourMode, cct | delay |
| `21W4` | 瑞晶四关 | switch, switch1, switch2, switch3, switch4 | — |
| `21Y4` | 雷士简韵圆形卧室灯 | switch, brightness, lightMode, colourMode, cct | delay |
| `21YB` | 雷士叠影方形客厅灯 | switch, brightness, lightMode, colourMode, cct | delay |
| `220J` | 雷士智能灯带 | switch, brightness, lightMode, colourMode, cct | delay |
| `221W` |  | switch, switch1, switch2, switch3, switch4 | — |
| `2223` | 雷士简韵方形卧室灯 | switch, brightness, lightMode, colourMode, cct | delay |
| `2225` | 雷士简韵方形客厅灯 | switch, brightness, lightMode, colourMode, cct | delay |
| `2229` | 雷士柠梦圆形小卧室灯 | switch, brightness, lightMode, colourMode, cct | delay |
| `222B` | 雷士满天星圆形卧室灯 | switch, brightness, lightMode, colourMode, cct | delay |
| `222C` | 雷士柠梦圆形卧室灯 | switch, brightness, lightMode, colourMode, cct | delay |
| `222D` | 雷士柠梦方形卧室灯 | switch, brightness, lightMode, colourMode, cct | delay |
| `222E` | 雷士柠梦方形客厅灯 | switch, brightness, lightMode, colourMode, cct | delay |
| `223Y` | 西顿芳华落地灯 | switch, brightness, backlight, lightMode, cct | select, Kcurve |
| `226X` | 阳光照明皓翼大三防灯 | switch, brightness, lightMode, colourMode, cct | delay |
| `2274` | 阳光照明至简方形客厅灯 | switch, brightness, lightMode, colourMode, cct | delay |
| `2275` | 阳光照明至简方形卧室灯 | switch, brightness, lightMode, colourMode, cct | delay |
| `2276` | 阳光照明至简圆形卧室灯 | switch, brightness, lightMode, colourMode, cct | delay |
| `22S4` | 町米智能电磁炉 | switch, status, mode, heatGear, faultDetection | — |
| `22S8` | 佳仁按摩椅 | switch, ppmMode, backAction, intenGear, hot | remainTime, manuMode1, qiya, time |
| `22V8` | 澳柯玛智能茶吧机 | switch, status, temperature, faultDetection, childLockSwitch | targettemperature, warm, intake, incubator, soakingtime, collectiontime, coldwater |
| `22YZ` | 台灯 | switch, brightness, colourMode, cct, lightMode | PIR |
| `231P` | Kyvol及悦空气炸锅 | switch, action, status, temperature, presetSwitch | workTime, preTimeStart, leftTime, commonFaultDetection, QuickRecipe, CookMode |
| `23WO` | 亚摩斯极境开关四键 | switch, switch1, switch2, switch3, switch4 | — |
| `23XJ` | X1Max蒸汽米汤饭煲 | status, action, mode, presetSwitch, faultDetection | workTime, leftTime, preTimeEnd, settime |
| `24TT` | 欧普Balance读写台灯 | switch, brightness, colourMode, cct, lightMode | tomatoClk, nightWakeup, rhythm, delayclose |
| `24YC` | 奥佳华按摩枕 OG2210 | switch, stop, mode, heat, alarm | time, KnockingSpeed, electricity, suspend, surTime |
| `2588` | 三加三维智能幻彩灯带 | switch, brightness, colourMode, colour, lightMode | — |
| `25BG` | 得力保管箱 | switch, lockStatus, lockState, battery, alarms | events |
| `25FO` | 三加三维智能筒射灯 | switch, brightness, colourMode, cct, lightMode | — |
| `25ND` | 得力保管箱 | switch, lockStatus, lockState, battery, alarms | events |
| `25NE` | 得力保管箱 | switch, lockStatus, alarms, lockState, battery | events |
| `25NG` | 得力保管箱 | switch, lockState, alarms, battery, lockStatus | events |
| `25NI` | 得力保管箱 | switch, battery, lockStatus, alarms, lockState | events |
| `25NJ` | 得力保管箱 | switch, lockState, lockStatus, alarms, battery | events |
| `25UT` | 得途智能护眼吸顶灯 | switch, brightness, colourMode, cct, lightMode | — |
| `262Y` | DoHome 幻彩蜂巢拼接灯 | switch, brightness, colour, cct, mode | lighting, music |
| `264S` | 雷士智能吸顶灯 | switch, brightness, colourMode, cct, lightMode | — |
| `274F` | 领普三键墙壁开关 | switch, switch1, switch2, switch3, brightness | — |
| `279R` | POVOS奔腾上加水加湿器 | switch, humidity, temperature, gear, faultDetection | time |
| `27NX` | WTT智能晾衣架 | action, airDry, disinfect, drying, lightSwitch | commonFaultDetection |
| `27PM` | 鸿雁智能排插(四位分控) | switch, switch1, switch2, switch3, switch4 | — |
| `2895` | 雅洁3D人脸自动锁F1 | lockState, lockMode, battery, alarm, openEvent | userkeyList, tonguebadAlarm, pryAlarm, hijackAlarm, systemlockAlarm, event |
| `289K` | 皇鼎智能门锁VE06W | lockState, lockStatus, lockMode, alarm, openEvent | faultCode, UserList, BatteryLevel |
| `28HA` | I7智能门锁 | lockState, lockStatus, battery, alarm, openEvent | faultCode, defenseMode, userLists, Records |
| `28SL` | 智能贝壳镜 | switch, status, mode, battery, brightness | — |
| `28WH` | RND可折叠电动滑板车F16 | switch, speed, light, lock, temperature | distance, electric, running, shutdown, unit, Power, cruise, state |
| `291J` | 澳柯玛智能电热水器B116 | switch, mode, temperature, faultDetection, sterilize | cutcapacity, frequency, prestart, preswitch, workstate, code, PowerSaving |
| `292G` | 香之君便携咖啡机 | mode, action, switch, currentTemperature, setting | exceptionReporting, devicePower, history, timedReminders, deviceAppoint, deviceState |
| `29AF` | MPE太空椅 | switch, modeSelect, headControl, legControl, lightSwitch | footControl, Memoryheight, heightControl |
| `29BE` | 澳柯玛智能电热水器B115 | switch, mode, temperature, faultDetection, sterilize | CapacityIncrease, code, PowerSaving, preswitch, Cleanup, workstate, prestart, cutcapacity |
| `29DH` | 澳柯玛智能电热水器W118 | switch, mode, temperature, faultDetection, sterilize | preswitch, frequency, Cleanup, code, cutcapacity, workstate, prestart |
| `29HQ` | MOLONEY莫洛尼电壁炉 | switch, gear, mode, temperature, faultDetection | firehigh, CanelTimer, CountDown, CBedLight, BurningSound |
| `29QR` | 三加三维智能三色 | switch, brightness, colourMode, cct, lightMode | — |
| `29U7` | 智能烘干毛巾架 | switch, disinfect, drying, temperature, autoMode | commonFaultDetection, wind, time |
| `29WV` | 绿克扫拖一体机HS1 | status, action, mode, remoteControl, deviceStatus | edgeElement, hepaElement, rollElement, commonFaultDetection, scheduleService, path, musicPackage, startClean, areaSetting, cleanRecord, ossSN, mapService |
| `2A0F` | 好太太智能晾衣机HP-D204-6BS | action, airDry, disinfect, drying, lightSwitch | airDryRemTime, airDryTime, dryRemTime, dryTime, commonFaultDetection |
| `2A0X` | 博世微蒸烤一体机 | switch, status, mode, childLock, faultDetection | control, devDoor, localFood, favorite, leftTime |
| `2A96` | 清易智慧扫拖机器人 | status, action, mode, deviceStatus, remoteControl | edgeElement, hepaElement, rollElement, commonFaultDetection, mapService, cleanRecord, startClean, areaSetting, musicPackage, path, ossSN, scheduleService, sensor |
| `2AA3` | 欧派洗碗机 | switch, action, status, mode, faultDetection | RemainingTimer, Temperature |
| `2AE3` |  | switch, mode, temperature, fan, childLockSwitch | — |
| `2AE4` |  | switch, mode, temperature, fan, childLockSwitch | — |
| `2AJO` | Paulmann-Finn-Smart吸顶灯 | switch, brightness, lightMode, colourMode, cct | delay |
| `2AJX` | Paulmann-Diskette-Pro-Smart吸顶灯 | switch, brightness, lightMode, colourMode, cct | delay |
| `2AKM` | 华艺凝玛吸顶灯 | switch, brightness, lightMode, colourMode, cct | delay |
| `2AM3` | 乐喝净饮机 | mode, status, temperature, presetSwitch, faultDetection | preTimeStart, leftTime, commonFilterElement1, commonFilterElement2, TR, MiddleOfWater, BoilTea, Wash, Caudle, KeepWarm, MaxOfWater, HeatUpWater, MinOfWater, DrinkWaterToday |
| `2ANO` | 鸿雁三路智能开关模块 | switch, switch1, switch2, switch3, indicator | — |
| `2APC` | 雷士满天星方形客厅灯 | switch, brightness, lightMode, colourMode, cct | delay |
| `2APF` | 雷士叠影方形卧室灯 | switch, brightness, lightMode, colourMode, cct | delay |
| `2APH` | 雷士满天星方形卧室灯 | switch, brightness, lightMode, colourMode, cct | delay |
| `2APM` | 雷士叠影圆形卧室灯 | switch, brightness, lightMode, colourMode, cct | delay |
| `2APN` | 雷士叠影圆形小卧室灯 | switch, brightness, lightMode, colourMode, cct | delay |
| `2AQD` | 达伦自然光吸顶灯Z3Pro | switch, brightness, lightMode, colourMode, cct | natural, nightmode, lampswitch |
| `2AU9` | 鸿雁智能灯带 | switch, brightness, colourMode, lightMode, cct | progressSwitch, delay |
| `2AVV` | 亚都空气净化器KJ450G-B4Hi | switch, childLockSwitch, pm25, fan, light | filterElement1, sound |
| `2AWI` | 万家乐燃气热水器16LX7 | switch, mode, temperature, faultDetection, heat | gesture, orde, pressurize, cruiseSterilization |
| `2B63` | 捷德韦尔两线式可调光调色灯控盒 | switch, brightness, colourMode, cct, lightMode | delay |
| `2B7O` | Paulmann-Konig-Smart餐吊灯CCT | switch, brightness, lightMode, colourMode, cct | delay |
| `2BB0` | 华为智选 欧普智能吸顶灯24W | switch, brightness, cct, sleeping, lightMode | location, timeMelody, wakeUp, wallSwitch1, wallSwitch2, wallSwitch3, delay |
| `2BB2` | 华为智选 欧普智能吸顶灯48W | switch, brightness, cct, sleeping, lightMode | location, timeMelody, wakeUp, wallSwitch1, wallSwitch2, wallSwitch3, delay |
| `2BEG` | 得邦A60蓝牙智能灯泡调光调色版 | switch, brightness, colourMode, lightMode, cct | — |
| `2BEH` | 得邦A70蓝牙智能灯泡调光调色版 | switch, brightness, colourMode, lightMode, cct | — |
| `2BEK` | 智能筒灯 | switch, brightness, colourMode, lightMode, cct | — |
| `2BEL` | 智能光源模组 | switch, brightness, colourMode, cct, lightMode | — |
| `2BEN` | 星空版悸动客厅吸顶灯 | switch, brightness, colourMode, lightMode, cct | — |
| `2BEO` | 星空版悸动卧室吸顶灯 | switch, brightness, colourMode, lightMode, cct | — |
| `2BEV` | FSL蓝牙彩光灯带 | switch, brightness, colourMode, colour, cct | — |
| `2BFM` | 享睡智能音乐睡眠灯 | switch, brightness, colour, lightMode, sleepMode | tomatoClk, progressTurnOn, progressTurnOff, getAlarmList, LampDevStatus, clockSleep, timeSetSync, timeStyle, alarmPreview, playMusic, setAlarm |
| `2BFP` | 智能护眼台灯 | switch, brightness, colourMode, cct, lightMode | — |
| `2BGM` | 三雄极光Pak智能筒灯 | switch, brightness, colourMode, cct, lightMode | — |
| `2BMZ` | 领普双键单火开关MESH | switch, switch1, switch2, mode1, mode2 | button1, button2 |
| `2BNH` | 达伦自然光吸顶灯D3 | switch, brightness, colourMode, cct, lightMode | lampswitch, natural, nightmode |
| `2BNN` | 华为智选 欧普智能台灯 2S | switch, backlight, brightness, lightMode, cct | studyMode, nightWakeup, lightStatistics, delay |
| `2C1E` | 小质即热饮水机 | status, mode, childLockSwitch, faultDetection, waterLevel | currentOutlet |
| `2C1N` | 小狗擦地吸尘器T12 Duke Rinse WIFI | status, battery, faultDetection, commonTask1, switch1 | workTime, leftTime, commonFilterElement1, commonFilterElement2, shiftmode1 |
| `2C88` | 西蒙中央空调温控器Daikin | switch, mode, temperature, fan, faultDetection | BackLightLevel |
| `2C89` | 西蒙中央空调温控器Gree | switch, mode, temperature, fan, faultDetection | BackLightLevel |
| `2C8A` | 西蒙中央空调温控器Mitsubishi | switch, mode, temperature, fan, faultDetection | BackLightLevel |
| `2C8B` | 西蒙中央空调温控器Toshiba | switch, mode, temperature, fan, faultDetection | BackLightLevel |
| `2C8D` | 西蒙中央空调温控器Midea | switch, mode, temperature, fan, faultDetection | BackLightLevel |
| `2CCL` | 金鱼音乐智能电动牙刷 | battery, status, mode, spraySwitch, lockMode | setWorkTime, brushingHistory, brushHeader, restDays, music |
| `2DCA` | HEIMAN智能红外光照度传感器 | status, battery, sensitivity, luminance, temperAlarm | motionDetected, delayTime |
| `2DDK` | 科西逸尔无叶风扇 | switch, mode, fan, onOffBeep, lock | reserveStart, timedOff, anion, shake, screenLight |
| `2DGO` | 水母云智能双色筒灯 | switch, brightness, colourMode, cct, lightMode | — |
| `2DMD` | 三路智能开关 | switch, switch1, switch2, switch3, backlight | — |
| `2DPH` | 达伦吸顶灯C21CTHW | switch, brightness, lightMode, colourMode, cct | delay, NightMode |
| `2DPI` | 达伦吸顶灯C217THW | switch, brightness, lightMode, colourMode, cct | delay, NightMode |
| `2DWC` | 水母云智能双色灯带 | switch, brightness, colourMode, cct, lightMode | — |
| `2DYF` | 亚摩斯多功能电压力锅AS-YDG253Z | mode, action, status, presetSwitch, faultDetection | food, workTime, preTimeStart, leftTime, settime |
| `2E4A` | 熊小夕便携式奶茶机 | mode, status, stirMode, temperature, commonMemorySwitch1 | remainingTime, Milktea, healthtea, Boilwater |
| `2E4V` | 爱莱克特智能擦地机 | status, action, mode, battery, water | getclean, dryorwet, setwater, cleansum, faultwaring, find, cleantime, cswitch, wakeup, setclean, setHz, sethear |
| `2ELR` | 小狗擦地吸尘器 | status, battery, faultDetection, commonExecution1, switch1 | workTime, leftTime, commonFilterElement1, commonFilterElement2, shiftmode1 |
| `2ENI` | 亚摩斯星耀开关四键 | switch, switch1, switch2, switch3, switch4 | — |
| `2ENX` | 得途智能护眼吸顶灯 | switch, brightness, colourMode, cct, lightMode | — |
| `2EO8` | 熠世华彩情景灯 | switch, brightness, colourMode, cct, lightMode | — |
| `2EP5` | 达伦36W吸顶灯C33NTHW | switch, brightness, lightMode, colourMode, cct | NightMode |
| `2EXA` | MINI关节按摩仪 | switch, stop, hot, gear, mode | WorkStatus, ElectricQuantity, WorkCountdown, vibrate |
| `2EXO` | 三思LED吸顶灯 24W | switch, brightness, lightMode, colourMode, cct | — |
| `2EZR` | 亚摩斯睿雅零火开关三键 | switch, switch1, switch2, switch3, brightness | — |
| `2F6R` | 达伦智能台灯3 | switch, brightness, brightness, lightMode, indicator | nightWakeup, progressTurnOff, tomatoClk1, lightStatus, fadeTime, tomatoClk4, tomatoClk2, tomatoClk3, record |
| `2F6S` | 帝王S2闪耀智能坐便器 | toiletMode, toiletTemperature, seatStatus, nozzlePos, gear | WindTemperature, ThePrimaryRadar, Rinse, RadarInduction, Deodorization, NozzleCleaning, LightControl, Flip, TurnOver, MobileCleaning |
| `2F85` | 耶鲁智能门锁YMK819 | lockState, lockMode, battery, alarm, openEvent | keyList, tempPasswd, userlist, remoteInfo |
| `2F87` | 耶鲁智能门锁YMK919 | lockState, lockMode, battery, alarm, openEvent | keyList, tempPasswd, userlist, remoteInfo |
| `2FD0` | 博顿物联四开 | switch, switch1, switch2, switch3, switch4 | — |
| `2FEG` | 无线智能洗地吸尘器 | battery, sewageboxstate, cleanwaterboxstate, selfclean, status | commonFaultDetection, Function, AutoTimes, AutoDuration, StrongDuration, StrongTimes, StandDuration, StandardTimes, CycleCount, BootTimes, CharginTime, DischargeTime, WaterPump, MainMotor, RollBrush |
| `2FGH` | 宝贝第一灵悦JOY | switch, battery, powerSupply, alarm, temperature | ConstantTemperatureWind, NaturalWind, PowerLimit |
| `2FW5` | 吉豪智能吊灯 | switch, brightness, colourMode, cct, lightMode | — |
| `2FXH` | 九牧M9智能浴缸 | mode, temperature, status, switch, waterLevel | commonFaultDetection, countDown, paraSet |
| `2FY4` | 洒拖派 0 Pro 自动擦窗机 | status, action, mode, deviceStatus, volume | commonFaultDetection, statusA, voicePack, windowSide, waterSpray |
| `2G19` | 达伦自然光夜灯 蓝牙版 | battery, switch, brightness, colourMode, lightMode | Reconnect, DeviceStatus, ChargingMode, LightSensingSwitch, DelayLightOff |
| `2G4X` | 索菲莉尔 智能电动床 Mbed 001 | oneKeyReset, headControl, legControl, modeSelect, stop | — |
| `2G9V` | 耶鲁智能门锁YMK829 | lockState, lockMode, battery, alarm, openEvent | keyList, tempPasswd, userlist, remoteInfo |
| `2G9W` | 耶鲁智能门锁YMK929 | lockState, lockMode, battery, alarm, openEvent | keyList, tempPasswd, userlist, remoteInfo |
| `2GD7` | 凯迪仕智能锁HK700-F | lockState, lockMode, battery, alarm, openEvent | lastActionTime, keyArray, userlist, publicKey, remoteCode, remoteResult, remoteInfo, morefunction, alarmstatus |
| `2HB1` | 多功能射频胶原蛋白仪 | skinMode, battery, status, switch, gear | btstatus, Report, Time, remainingtime |
| `2HDO` | 嵌洗JBCD15E-X20.i | switch, status, mode, temperature, faultDetection | leftTime |
| `2HR8` | 西蒙三位智能开关 | switch, switch1, switch2, switch3, indicator | commonFaultDetection, switchStatus |
| `2HUA` | 德施曼智能门锁R7H | lockState, lockMode, battery, alarm, openEvent | lastActionTime, keyArray, lockdefense, Hijacking, userlist, errorCode, remoteInfo, remoteResult, remoteCode, publicKey, upgradeMode, enableState |
| `2HVI` | 九联智能门锁 | lockState, lockMode, battery, alarm, openEvent | keyList, userlist, remoteResult, publicKey, remoteInfo, remoteCode, errorCode, upgradeMode |
| `2HYH` | 8859浴用加热器-足浴器 | mode, faultDetection, temperature, action, switch | setWorkTime, leftTime, temperatures, ozone, bubble |
| `2HZE` | 海曼(HEIMAN)智能烟雾报警器 | battery, silencer, selfCheck, temperAlarm, alarm | alarmtype |
| `2I5Q` | 飞利浦智能台式净饮机 | faultDetection, water, status, rinseMode, outWaterTemp | outputTds, output, inputTds, filterElement1, WinterMode, filterReset, BoilingPoint, SmartTempSet, SmartOutletSet, InputTemp, Warning |
| `2I67` | 左点砭石按摩器 | switch, status, heat, mode, battery | usage, guide, time, vibrat, remainTime |
| `2I8T` | 家用智能中央电暖对流取暖器AHR4146ZS | mode, childLockSwitch, gear, temperature, switch | OSD, runTime |
| `2I92` | 博凡保险箱 | lockStatus, openMode, battery, alarms, lockState | — |
| `2IBH` | 驰球珍柜保险箱 | lockStatus, openMode, alarmEvent, connectionStatus, battery | — |
| `2IKH` | 皇鼎智能门锁VE08W | lockState, lockStatus, lockMode, alarm, openEvent | faultCode, UserList, BatteryLevel |
| `2IKT` | 九牧智能灯镜 | lightMode, switch, cct, brightness, status | commonFaultDetection |
| `2IRH` | CRMCR卡唛卡诺II智能保管箱 | lockStatus, openMode, alarmEvent, connectionStatus, battery | historyrecord, SetTime, PW, CID, FP |
| `2ISS` | 根元嵌入式衣物护理机 | switch, action, mode, status, faultDetection | leftTime, timing |
| `2IWD` | 西蒙弈系列超薄吸顶灯 | lightMode, switch, brightness, colourMode, sleepMode | progressTurnOn, colorTemperature |
| `2J05` | 锐亿电动牙刷 | mode, initPosition, battery, workGuidance, gear | more, Record, remaining, state |
| `2J24` | 电动剃须刀 | mode, battery, status, rest, lock | btConnection, usetime, remaining, surplusCount, bladeCleanTime |
| `2JFH` | MPE智能床垫 | oneKeyReset, modeSelect, headLegControl, headControl, legControl | — |
| `2JFZ` | AM35智能卷帘 | changeDirection, opener, action, directionalmode, commonMode1 | Limit, JointLevel, SBZT |
| `2JHB` | 黑白生活智能筋膜枪U51 | mode, battery, gear, switch, status | Remainingtime, Videointroduction, worktime |
| `2JJ9` | 智能梦幻帘 | changeDirection, rotationAction, opener, rotationAngle, action | — |
| `2JJG` | 趣丸悬浮剃须刀 | mode, battery, status, commonMode1, commonMode2 | record, time, commonFilterElement1, DevStatus, NTP, endurance |
| `2JK9` | 虎牌北辰床头保管箱 | lockStatus, openMode, alarms, battery, lockState | — |
| `2JTK` | CRMCR卡唛卡诺II智能保管箱-抽柜版 | lockStatus, openMode, alarmEvent, connectionStatus, battery | FP, CID, PW, SetTime, historyrecord |
| `2JTL` | CRMCR卡唛卡诺II智能保管箱-抽柜无线充版 | lockStatus, openMode, alarmEvent, connectionStatus, battery | FP, CID, PW, SetTime, historyrecord |
| `2JZ4` | VOC大屏猫眼人脸锁 | lockState, lockMode, battery, alarm, openEvent | publicKey, userlist, upgradeMode, remoteCode, remoteResult, remoteInfo, errorCode, keyArray |
| `2JZX` | 山岭智能马桶 | toiletMode, seatStatus, autoFlushing, autoFlip, lightSense | func, washTemp, dryTemp, washPos, washWater, sensingRange, powerSaving, seatTemp |
| `2K0T` | 德施曼智能门锁Q30 | lockState, lockMode, battery, alarm, openEvent | lastActionTime, errorCode, upgradeMode, userlist, remoteInfo, lockdefense, keyArray, publicKey, Hijacking, remoteCode, enableState, remoteResult |
| `2K3T` | 晴天Mico | seekSwitch, lockSwitch, powerSwitch, faultDetection, autolockGear | — |
| `2K5B` | 大拿电动剃须刀 | mode, battery, status, switch, speed | time, Faultalarm, ResetShaverHead, others, worktime, SpeedAdjustment, searchequipment, Bassmode, userrecord, safetylock |
| `2K72` | VOC大屏猫眼人脸锁K9Plus | lockState, lockMode, battery, alarm, openEvent | subBattery, publicKey, remoteCode, userlist, remoteInfo, upgradeMode, remoteResult, errorCode, keyArray |
| `2K73` | VOC猫眼智能门锁X11i | lockState, lockMode, battery, alarm, openEvent | keyArray, remoteCode, errorCode, publicKey, userlist, upgradeMode, remoteResult, remoteInfo |
| `2K7Y` | 杜亚智能窗帘 DH11 | changeDirection, switchSpeed, opener, action, battery | capacity, commonFaultDetection |
| `2K8I` | 黑白生活智能筋膜枪U52 | mode, battery, gear, switch, status | afterservice, Remainingtime, worktime, Videointroduction |
| `2KCT` | 等静压智能床垫 | oneKeyReset, faultDetection, modeSelect, headControl, legControl | AfterSales, RightControl, LeftControl |
| `2KD9` | 正泰五孔智能插座 | switch, childLockSwitch, indicator, memorySwitch, faultDetection | power, electric |
| `2KE3` | 九联全自动智能门锁 | lockState, lockMode, battery, alarm, openEvent | upgradeMode, remoteInfo, publicKey, remoteResult, errorCode, remoteCode, userlist, keyArray |
| `2KE4` | 九联3D人脸识别智能门锁 | lockState, lockMode, battery, alarm, openEvent | keyArray, userlist, remoteCode, errorCode, remoteResult, publicKey, remoteInfo, upgradeMode |
| `2KH6` | CXW-200-J6058吸油烟机 | mode, faultDetection, lightSwitch, status, switch | remainCloseMin, runTim, lBReTl, lBStatl, lBStatr, steamWash |
| `2KJ9` | 顾家功能单椅 | seatStatus, oneKeyReset, headLegControl, memoryControl1, modeSelect | AfterSales |
| `2KQI` | 希箭IOT智能镜柜 | lightMode, defoggingSwitch, brightness, lightSwitch, workStatus | — |
| `2KR9` | 斯诺德凯奇Mini筋膜枪 | mode, battery, gear, switch, status | Introduction, worktime, Lefttime, afterservice |
| `2KWO` | 欧普智能射灯筒灯驱动器 - 6W | switch, cct, brightness, faultDetection, memorySwitch | fadeTime, subProduct, lightCurveSetting, fadeTimeSetting |
| `2KWR` | 欧普智能射灯筒灯驱动器 - 25W | switch, cct, brightness, faultDetection, memorySwitch | fadeTime, fadeTimeSetting, subProduct, lightCurveSetting |
| `2KXU` | 霍尼韦尔门窗传感器 | luminance, battery, temperAlarm, alarmSwitch, doorContact | reminder, commonFaultDetection |
| `2KY4` | 霍尼韦尔家用可燃气体探测器 | preheat, silencer, selfCheck, alarm, gasSensor | commonFaultDetection |
| `2L2P` | 凡家智能暖腹腰带 | alarm, light, heat, mode, status | ota, power, cuTemperature, countdown, unit |
| `2L4O` | 西顿巴赫PLC磁吸灯 | switch, cct, brightness, faultDetection, memorySwitch | fadeTime, fadeTimeSetting, lightCurveSetting |
| `2L63` | 欧普智能台灯3Pro | lightMode, switch, brightness, cct, colourMode | defMode2, defMode3, defMode1, studyRemind, lightConfig1, defMode4, lightConfigReset, runStactics, lightConfig2, delayOff, seatSensor, modeDefine |
| `2LBT` | 心智悦环境控制器K1 | memorySwitch, faultDetection, temperature, humidity, mode1 | filterElement, airKey, airswitch, heatingswitch, freshairswitch, HCHO, CO2, PM25, fan1 |
| `2LBW` | 科西无叶风扇A4-H | mode, fan, onOffBeep, switch, childLock | timeOff, LARangle, anion, restScreen, startTime |
| `2LQA` | 友通多功能空气检测仪 | tvoc, temp, hcho, pm25, alarmSwitch | co2, pm10, humi, commonFaultDetection, ytFault, brightness01, clock, report |
| `2LTE` | 摩申电动剃须刀MTR307 | mode, battery, switch, status, speed | time, safetylock, userrecord, Bassmode, searchequipment, SpeedAdjustment, worktime, ResetShaverHead, Faultalarm |
| `2LX8` | 良品主义智能电动剃须刀 | status, workStatus, workMode, alarm, lock | instruction, ota, cutterTime, power, worktime |
| `2M9X` | 舒福德 智能床 Mbed 001 | oneKeyReset, modeSelect, headControl, legControl, stop | — |
| `2MD4` | SJSW智能筒射灯 | lightMode, switch, brightness, cct, switch1 | fade |
| `2MDD` | 小适智能剃须刀 | mode, battery, status, motor, lock | charge, unusual, state, knifereset |
| `2MGL` | 创明智能百叶帘 | changeDirection, switchSpeed, rotationAction, opener, action | — |
| `2MGM` | 易百珑四键智能开关 | switch1, switch2, memorySwitch, mode2, mode1 | sceneButton1, sceneButton2, sceneButton3, sceneButton4, led, CleanPair, Pair |
| `2MGS` | 华米元情景灯 | lightMode, switch, brightness, cct, switch1 | fade |
| `2MH0` | 吉豪智能吸顶灯 | lightMode, switch, brightness, cct, auxSwitch | fade, mainLight, auxLight |
| `2MN7` | 霍尼韦尔智能台灯X5 | lightMode, switch, brightness, colourMode, lock | lightFormula, useTime, seatSensor, nightAwake, longTimeAlarm, lightforMode, wakeUpMorning, lightAdaption |
| `2MNT` | 膳魔师智能保温杯Pro 弹盖款 | waterVolume, battery, targetTemperature, currentTemperature, status | canvasData5, canvasData4, privacyStatus, privacySta, canvasData3, canvasData2, canvasConfig, canvasData, Goal, waterWeeksIntake, drinkTarget, drinkIntake, canvasData1, myHashCode, drinkRemind |
| `2MPT` | 佳普乐舒樾智能方镜柜 | sterilizeSwitch, makeupLightGear, demisterSwitch, aromatherapyGear, switch | sterilizeTime, atmosphereLightSwitch, Beep, demisterTime, Temperature, makeupLightPercentage, Humidity |
| `2MXH` | 吸顶式红外人体移动光照传感器 | luminance, pir, switchNightLight, selfCheck, configureSwitch1 | delayTime, commonFaultDetection, luminanceReportSetting |
| `2N06` | 以内洗地机Z5Pro | cleanwaterboxstate, battery, sewageboxstate, selfclean, status | workTime |
| `2N0S` | 永艺智能撑腰椅Flow 660 | sedentaryReminder, LongSitState, battery, SitState, ChargeState | sedentaryTime, SetTimeIncrease, RemindCout, RemindTime, LongSitStop, RemindInterval |
| `2N2Q` | A.O.史密斯净热一体机 | temperature, faultDetection, water, status, heatingSwitch | inputTds, outputTds, filterElement1, filterElement2, totalPurifyWater, addWaterMode, waterLevelStatus, keepWarmMode |
| `2N2U` | 方太油烟机CXW-358-01-X20.i | mode, lightSwitch, status, switch, gear | LockScreen, Ambientlight |
| `2N3T` | 欧普PLC磁吸轨道灯 | switch, brightness, faultDetection, cct, memorySwitch | fadeTime, fadeTimeSetting, lightCurveSetting, relBrightness |
| `2N4A` | 云鲸智能拖扫一体机器人J4 | battery, mode, faultDetection, action, status | commonFilterElement1, commonFilterElement2, commonFilterElement3, commonFilterElement4, getMap, reqToken, narwalCmd, robotBaseStatus, robotWorkingStatus, revokeDeviceAuth |
| `2N5A` | 晾霸智能晾衣机Q1 | airDry, drying, action, lightSwitch, status | airDryTime, dryRemTime, airDryRemTime, dryTime |
| `2N5R` | 新博孚梦幻帘 | rotationAction, opener, rotationAngle, action, directionalmode | — |
| `2N5T` | 杜亚智能齐平卷帘 | changeDirection, opener, syncAction, action, syncOpener | — |
| `2N9B` | 优慧家燃气热水器HA241 | inletTemperature, switch, faultDetection, temperature, status | totalWater, totalGas, burningTime, curWater, custom |
| `2NA1` | 小适智能剃须刀Ai501 | mode, battery, status, motor, lock | time, state, deviceVersion, hibernate, unusual, charge, knifereset |
| `2NAA` | 永艺智能撑腰椅Flow 600 | sedentaryReminder, LongSitState, battery, ChargeState, SitState | sedentaryTime, LongSitStop, RemindInterval, SetTimeIncrease, RemindTime, RemindCout |
| `2NAB` | 永艺智能撑腰椅Act 280 | sedentaryReminder, LongSitState, battery, ChargeState, SitState | sedentaryTime, RemindCout, RemindTime, SetTimeIncrease, RemindInterval, LongSitStop |
| `2NAC` | 永艺智能撑腰椅Act 260 | sedentaryReminder, LongSitState, battery, ChargeState, SitState | sedentaryTime, SetTimeIncrease, LongSitStop, RemindTime, RemindInterval, RemindCout |
| `2NCL` | 梦百合0压智能床 | oneKeyReset, memoryControl1, modeSelect, headControl, legControl | GetMemoryMode |
| `2NI0` | 佳普乐沁源感应给皂龙头 | waterTime, temperature, coldWaterSwitch, autoWaterSwitch, switch | soapTime, interval |
| `2NLQ` | meipont美邦燃气热水器 | switch, faultDetection, temperature, flameStatus, status | injection, currentgas, currentwater, overgas, overwater, seasons, function, watercapacity, conversion |
| `2NLR` | meipont燃气热水器 | switch, faultDetection, temperature, flameStatus, status | overgas, injection, currentgas, watercapacity, function, overwater, currentwater, conversion, seasons |
| `2NX2` | 智能色温吸顶灯 | lightMode, switch, cct, brightness, commonMemorySwitch | cleverSwitch, Togglecct, ChangeTime |
| `2NXL` | GOHOLITE智能护眼灯GS20 | lightMode, brightness, mainBrightness, auxBrightness, switch | nightWakeup, progressTurnOff |
| `2O31` | 威仕达百叶帘WSERD24 | changeDirection, switchSpeed, rotationAction, opener, action | — |
| `2O4L` | 添眠止鼾枕 | snoringStatus, pillowStatus, antiGear, detectGear, switchLED | pillowActive, pillowMode, sensorReset |
| `2O5A` | 膳魔师智能保温杯Pro 旋盖款 | waterVolume, battery, currentTemperature, status, targetTemperature | waterDayIntake, myHashCode, Goal, privacySta |
| `2O9E` | RADLIT智能灯 | lightMode, switch, colour, brightness, cct | GradientDuration, Phantomcolorvariablespeed, ColorfulLightingMode |
| `2O9H` | eachone一起玩 智能加湿器 | switch, waterGear, humidity, gear, lightmode | countdown, remainingtime |
| `2ODK` | 亚都加湿器SZ550-DZ5(Hi) | switch, faultDetection, humidity, childLockSwitch, gear | display, state, anion, level, timing, dried |
| `2OE7` | 松下智能筒射灯 | lightMode, donotDisturb, brightness, cct, switch | progressSwitch, nightWakeup |
| `2OE8` | 松下智能明装筒射灯 | lightMode, donotDisturb, brightness, cct, switch | progressSwitch, nightWakeup |
| `2OE9` | 松下智能灯带控制装置 | lightMode, donotDisturb, brightness, cct, switch | nightWakeup, progressSwitch |
| `2OJL` | eachone一起玩 智能加湿器 | switch, waterGear, humidity, gear, lightmode | countdown, remainingtime |
| `2ONW` | 亚都加湿器SC280-QL080(Hi) | switch, faultDetection, humidity, childLockSwitch, gear | sleep, state, lamp, timing, uv, level |
| `2OPI` | 提升窗HY | action, childLock, light, lightSwitch, winScreen | — |
| `2OT2` | 膳美师轻食破壁机 | mode, action, status, deviceSwitch, selfClean | leftTime, preTimeStart, findDevice, workRecord |
| `2OWF` | eachone一起玩 智能吸顶灯 | lightMode, cct, brightness, switch, commonMemorySwitch1 | nightWakeup, progressTurnOff, progressTurnOn |
| `2P2M` | 智能便携富氢水杯 | battery, currentTemperature, hydrogenProductionSwitch, intelligentCleaning, status | electrolyticConcentration, commonFaultDetection |
| `2P39` | 口袋咖啡机 | action, battery, brewingMode, stallProtection, temperature | cups, time, commonFaultDetection |
| `2P6X` | 佳普乐Realm智能马桶R5A | offSeatAction, toiletStatus, seatStatus, stop, toiletLidStatus | washSetting, drySetting, disinfection, foamShield, favorite, seatHeating, toiletSetting |
| `2P70` | 佳普乐Realm智能马桶R6A | offSeatAction, toiletStatus, seatStatus, stop, toiletLidStatus | washSetting, drySetting, disinfection, foamShield, favorite, seatHeating, toiletSetting |
| `2PI8` | DL深度调光情景灯Plus | lightMode, donotDisturb, cct, brightness, switch | toggleSwitch, nightWakeup, progressSwitch, progressTurnOff, progressTurnOn |
| `2PIE` | DL深度调光情景灯 | brightness, cct, donotDisturb, lightMode, switch | nightWakeup, progressTurnOff, progressTurnOn, progressSwitch, toggleSwitch |
| `2Q1O` | 正尚1路WiFi开关 | backlight, memorySwitch, switch, switch1, mode1 | Pair, CleanPair |
| `2Q3B` | 欧普照明SDL炫彩灯带 | brightness, cct, colour, colourMode, switch | relBrightness, toggleSwitch, PowerUpStatus, DynamicMode, DynamicModeColor6, DynamicModeColor3, DynamicModeColor2, DynamicModeColor1, DynamicModeColor5, DynamicModeColor4, FadeFunction, SunLightMode, StaticCctTransition, PixelCount, ResetMode, DynamicCctTransition |
| `2Q4G` | SORONTEK智能面板 | switch3, switch2, switch1, switch, switch4 | — |
| `2Q4H` | SORONTEK智能双色温灯 | brightness, cct, colourMode, lightMode, switch | progressSwitch |
| `2Q5C` | 力博得智能电动牙刷5Pro | battery, gear, mode, voiceGuidance, workGuidance | brushingHistory, customPlan, filterElement, polishElement, setWorkTime |
| `2QAP` | 智能儿童眼部按摩器 | childlockSwitch, gear, globalVolume, hotcompressTemperature, mode | — |
| `2QBF` | 苏泊尔小厨宝E07-UH01 | ecoSwitch, status, sterilizationSwitch, switch, temperature | commonFaultDetection |
| `2QL4` | MEIPONT智能冰箱437(Pro) | flexiTempZone, freezeSwitch, intelligentSwitch, refrigerateSwitch, status | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `2QP8` | 朗润阳光灯 | brightness, cct, donotDisturb, lightMode, switch | progressSwitch |
| `2QR4` | eachone一起玩   智能吸顶灯 | brightness, cct, lightMode, switch, commonMemorySwitch | nightWakeup, progressTurnOff, progressTurnOn |
| `2QR5` | eachone一起玩  智能吸顶灯 | brightness, cct, lightMode, switch, commonMemorySwitch | nightWakeup, progressTurnOff, progressTurnOn |
| `2QSZ` | 九牧智能晾衣机LA7002 | action, fadeSwitch, lightSwitch, status, silencer | limit, commonFaultDetection |
| `2QTJ` | MEIPONT智能剃须刀 磐石 | battery, bladeStatus, mode, status, travelLock | bladeClean, bladeReset, commonFaultDetection |
| `2R3W` | Ai智能电动晾衣机 | action, airDry, disinfect, drying, lightSwitch | — |
| `2R6Z` | 第E眠智能床垫灵境S001 | lieControl, lumbarControl, massageGear, massageTimer, softHardnessSwitch | positionSelect |
| `2R8X` | 立达信云上吊灯Pro | brightness, cct, lightMode, switch, commonMemorySwitch | relBrightness, commonFaultDetection |
| `2RBF` | 智能大西施锅 | action, mode, presetSwitch, status, warmSwitch | leftTime, preTimeStart, warmDuration |
| `2RCU` | 暖通网关MC5 PLUS | coldheatSwitch, faultDetection, gatewayAction, operation, rs485Switch | 485NetInfo, acGroupList, acList, automaticGroup, backup, backupData, capabilityset, connectMode, ctlCapability, delay, diagnose, diagnosis, freshAirGroupList, freshAirList, generalGrouplist, generalList, heaterGroupList, heaterList, heaterProtocol, homeGatewayCap, offlineOta, port1protocolList, port2protocolList, reboot, timeZone, vrvProtocol |
| `2RFM` | 朗泽吸顶灯 | brightness, cct, donotDisturb, lightMode, switch | progressSwitch |
| `2RFN` | 朗润吸顶灯 | brightness, cct, donotDisturb, lightMode, switch | progressSwitch |
| `2RFO` | 朗明吸顶灯 | brightness, cct, donotDisturb, lightMode, switch | progressSwitch |
| `2RGT` | 十亿智联智能橱柜灯 | brightness, colour, colourMode, donotDisturb, switch | — |
| `2RGV` | 十亿智联橱柜灯 | brightness, colour, colourMode, donotDisturb, switch | — |
| `2RH2` | 灵馨橱柜灯Lx-1 | brightness, cct, donotDisturb, lightMode, switch | — |
| `2RH3` | 灵馨橱柜灯Lx-2 | brightness, cct, donotDisturb, lightMode, switch | — |
| `2RH4` | 灵馨吸顶灯Lx-3 | brightness, cct, donotDisturb, lightMode, switch | — |
| `2RI2` | 百吉兴吸顶灯BJX-1 | brightness, cct, donotDisturb, lightMode, switch | — |
| `2RI4` | 百吉兴吸顶灯BJX-2 | brightness, colour, colourMode, donotDisturb, switch | — |
| `2RIJ` | 百吉兴橱柜灯BJX-3 | brightness, cct, donotDisturb, lightMode, switch | — |
| `2RJY` | 禅念智能双色吸吊灯 | auxSwitch, brightness, cct, colourMode, switch | progressSwitch |
| `2RN8` | lipro护眼吸顶灯E2 | brightness, cct, lightMode, switch, commonMemorySwitch | progressSwitch |
| `2RNA` | 西顿照明T5无线磁吸灯照明驱动 | brightness, cct, indicator, switch, commonMemorySwitch | fadeTimeSetting, lightCurveSetting, relBrightness, commonFaultDetection |
| `2RND` | 西顿照明T5无线灯带照明驱动 | brightness, cct, indicator, switch, commonMemorySwitch | fadeTimeSetting, lightCurveSetting, relBrightness, commonFaultDetection |
| `2RNE` | 西顿照明T5无线筒射灯照明驱动 | brightness, cct, indicator, switch, commonMemorySwitch | fadeTimeSetting, lightCurveSetting, relBrightness, commonFaultDetection |
| `2RNS` | 贝昂无耗材空气净化器X3(H) V1 | childLockSwitch, fan, mode, pm25, switch | autoClean |
| `2ROF` | 西顿照明T5无线明装筒射灯照明驱动 | brightness, cct, indicator, switch, commonMemorySwitch | fadeTimeSetting, lightCurveSetting, relBrightness, commonFaultDetection |
| `2S5N` | 奥马智能冰箱五门零嵌 | ecoMode, freezeSwitch, flexiTempZone, iceMode, status | commonFaultDetection, fridgeGear, freezerGear |
| `2S63` | 佳普乐沁澜智联龙头 | coldWaterSwitch, status, switch, temperature, waterTime | preSchedulingDuration |
| `2S7G` | 佳普乐P8-H00A+壁挂自动翻盖智能马桶 | autoFlip, offSeatAction, seatStatus, stop, toiletLidStatus | drySetting, favorite, seatHeating, toiletSetting, washSetting |
| `2SKJ` | 佳普乐沁沐智联龙头 | coldWaterSwitch, status, switch, temperature, waterTime | preSchedulingDuration |
| `9MZO` | 智控养生壶 | mode, status, switch, temperature, warmSwitch | — |
| `9MZU` | 智控壁挂炉 | bathTemperature, heatSwitch, heatTemperature, status, switch | — |
| `9MZV` | 智控烟机 | gear, lightSwitch, mode, status, switch | — |
| `A002` | 美的智能空调系列 | switch, mode, temperature, fan, faultDetection | delay |
| `A06W` | 博世洗衣机 | switch, action, mode, status, doorLockSwitch | — |
| `A07D` | 智能空调 | switch, mode, temperature, fan, faultDetection | delay |
| `A0NW` | 智能四通道开关 | switch, switch1, switch2, switch3, switch4 | — |
| `A0OM` | 智能四通道插座 | switch, switch1, switch2, switch3, switch4 | — |
| `A0OW` | 律动灯带 | switch, brightness, colourMode, colour, cct | — |
| `A0OY` | 五色灯 | switch, brightness, colourMode, colour, cct | — |
| `A0PT` | 国美电暖器 | switch, gear, mode, childLockSwitch, temperature | Display, Auto |
| `A0TG` | 海信日立空调 | switch, mode, temperature, fan, faultDetection | modeAuto, windAuto |
| `A11H` | 九阳破壁机 | action, status, cupStatus, clean, temperature | capacity, leftTime, commonFaultDetection, menuCode |
| `A11T` | 九阳蒸汽饭煲 | status, pause, clean, start, stop | commonFaultDetection, startCloud, continue, leftTimes |
| `A1B3` | COLMO滚筒洗衣机 | switch, action, mode, status, presetSwitch | preTimeEnd, leftTime |
| `A1B4` | COLMO洗干一体机 | switch, action, mode, status, presetSwitch | preTimeEnd, leftTime |
| `A1BJ` | 美的MRO899-1500橱下式净水机 | water, faultDetection, status, heatSwitch, rinseSwitch | filterElement1, purifiedWaterTDS, rawWaterTDS |
| `A1CM` | 美的洗物机 | switch, action, status, mode, faultDetection | — |
| `A1F9` | 万和燃气热水器LS3 | switch, mode, status, temperature, faultDetection | zerocold |
| `A1H3` | 冰箱CRBS613AC-A8 | refrigerateSwitch, freezeSwitch, refrigerator, freezer, flexzone | — |
| `A1I8` | 万和燃气热水器YL5 | switch, mode, status, temperature, faultDetection | temRange, zerocold |
| `A1K9` | 美的冰箱BCD-437WFGPZM(E) | faultDetection, refrigerateSwitch, freezeSwitch, refrigerator, freezer | storagePower |
| `A1KB` | 美的冰箱BCD-509WSGPZM(E) | faultDetection, refrigerateSwitch, freezeSwitch, refrigerator, freezer | storagePower |
| `A1KE` | 美的冰箱BCD-600WKGPZM(E) | faultDetection, refrigerateSwitch, freezeSwitch, refrigerator, freezer | storagePower |
| `A1KM` | 万和燃气热水器LS3 | switch, mode, status, temperature, faultDetection | zerocold |
| `A1L2` | 九阳智能空气炸锅VF999 | action, status, temperature, stop, start | workTime, devStatus, downloadMenu, startCloud, changeCookParams |
| `A1OA` | 烤箱KQD62F-M1A.i | switch, status, presetSwitch, lightSwitch, temperature | workTime, leftTime, compoundInstruction |
| `A1PF` | 小天鹅洗烘一体机 | switch, action, mode, status, presetSwitch | preTimeEnd, leftTime |
| `A1PG` | 小天鹅滚筒洗衣机 | switch, action, mode, status, presetSwitch | preTimeEnd, leftTime |
| `A1PH` | 小天鹅洗烘一体机 | switch, action, mode, status, presetSwitch | preTimeEnd, leftTime |
| `A1PK` | 美的滚筒洗衣机 | switch, action, mode, status, presetSwitch | preTimeEnd, leftTime |
| `A1PL` | 美的洗烘一体机 | switch, action, mode, status, presetSwitch | preTimeEnd, leftTime |
| `A1S7` | 海尔智能洗衣机 | switch, action, mode, status, faultDetection | preTimeEnd, leftTime, returnStandby |
| `A1XG` | TCL-AC | switch, temperature, ECO, targetTemperature, workMode | newWindPercentage, windSpeedPercentage, windSpeedAutoSwitch, newWindSwitch, newWindECOSwitch, newWindAutoSwitch, windDirection, softWind, PTC, beepSwitch, sleep, screen |
| `A2BB` | 捷渡行车记录仪 | crashSensitivity, volume, micSwitch, timelapseSwitch, faultDetection | — |
| `A2BC` | 捷渡行车记录仪(后视镜) | crashSensitivity, volume, micSwitch, timelapseSwitch, faultDetection | — |
| `A2GQ` | 西门子干衣机 | switch, mode, faultDetection, status, action | leftTime |
| `A2GR` | 西门子对开门冰箱 | refrigerateSwitch, freezeSwitch, refrigerator, freezer, faultDetection | — |
| `A2GS` | 西门子多门冰箱 | refrigerateSwitch, freezeSwitch, refrigerator, freezer, faultDetection | fresh1, fresh |
| `A2GV` | 西门子洗干一体机 | action, mode, status, childLockSwitch, faultDetection | lefttime1 |
| `A2IE` | CXW-200-J6052H吸油烟机 | mode, lightSwitch, gear, status, switch | commonFaultDetection, lockStat, lockSwtich, gearStat, lockScreen, delayedShutdown |
| `A2IX` | 美的电磁炉C22-506 | mode, heatGear, status, switch, temperature | time |
| `A2IZ` | 美的空气炸锅MF-KZS3503XM | action, status, temperature, targetTemp, mode | workTime, leftTime, pauseTime |
| `A2NJ` | 小天鹅 10公斤 洗干一体机 | switch, action, mode, status, presetSwitch | preTimeEnd, leftTime |
| `A2NL` | 小天鹅 10公斤 滚筒洗衣机 | switch, action, mode, status, presetSwitch | preTimeEnd, leftTime |
| `A2PO` | ZC3i燃气热水器 | switch, mode, faultDetection, temperature, status | StronRichWater, funcswit2, totalWater, totalGas, iwaterTmp, highTempUnlock |
| `A2Q2` | 万和电热水器X2 | switch, mode, faultDetection, temperature, status | hotwater, SetTemp, SetPower, appointmenttime, poweroff |
| `A2U1` | TE5i燃气热水器 | switch, mode, faultDetection, temperature, status | funcswit2, highTempUnlock, waterTotal, iwaterTmp, gasTotal |
| `A2U2` | TW7i燃气热水器 | switch, mode, faultDetection, temperature, status | waterTap, cycle, heating, gasTotal, Selfclean, iwaterTmp, waterfallBath, waterTotal, highTempUnlock |
| `A2UY` | ZH8i燃气热水器 | switch, mode, faultDetection, temperature, status | iwaterTmp, gasTotal, highTempUnlock, waterTotal, waterfallBath, heating, cycle |
| `A2V7` | 彩灯 | switch, colour, brightness, cct, colourMode | — |
| `A2VX` | DDF50-YP07i电热水器 | switch, faultDetection, temperature, status, powerMode | aiBath, wPswitch, waterQuality, cTVolume, bacSwitch |
| `A2VZ` | JWV13-A6S洗碗机 | switch, mode, action, status, addMode | leftTime, commonFaultDetection, brightener, washingSalt |
| `A2WF` | SJ62燃气热水器 | switch, mode, faultDetection, temperature, status | aiWash, interrupt, highTempUnlock, waterTotal, waterfallBath, iwaterTmp, Selfclean, gasTotal, cycle, heating, waterTap |
| `A2WW` | DDF60-YP07i电热水器 | switch, faultDetection, temperature, status, powerMode | aiBath, bacSwitch, cTVolume, waterQuality, wPswitch |
| `A2WX` | DDF70-YP07i电热水器 | switch, faultDetection, temperature, status, powerMode | wPswitch, bacSwitch, aiBath, waterQuality, cTVolume |
| `A2X5` | SJ61燃气热水器 | switch, mode, faultDetection, temperature, status | tempRange, waterTap, cycle, gasTotal, heating, Selfclean, highTempUnlock, iwaterTmp, waterfallBath, aiWash, waterTotal, interrupt |
| `A2X6` | ST61燃气热水器 | switch, mode, faultDetection, temperature, status | tempRange, waterTap, Selfclean, waterTotal, heating, gasTotal, cycle, waterfallBath, iwaterTmp, highTempUnlock, interrupt, aiWash |
| `A2X7` | SS62燃气热水器 | switch, mode, faultDetection, temperature, status | tempRange, cycle, waterTap, gasTotal, heating, waterfallBath, interrupt, waterTotal, Selfclean, highTempUnlock, aiWash, iwaterTmp |
| `A2Y0` | 松下壁挂ERV | switch, mode, fan, pm25, preStatus | filterElement4, filterElement1, filterElement2, filterElement3, commonFaultDetection, holM, leftTime |
| `A31J` | COLMO图灵中央空调 | heat, switch, mode, fan, automaticAirswitch | — |
| `A328` | GW8i燃气热水器 | switch, mode, faultDetection, temperature, status | tempRange, waterTotal, highTempUnlock, cycle, heating, iwaterTmp, Selfclean, gasTotal, waterfallBath, waterTap |
| `A32D` | COLMO新象中央空调 | heat, switch, mode, fan, automaticAirswitch | — |
| `A32E` | COLMO风管机 | heat, switch, mode, fan, automaticAirswitch | customhumidity, Dry |
| `A33D` | 美的中央空调-理想家LX | heat, switch, mode, fan, automaticAirswitch | — |
| `A33S` | 美的中央空调-领航者LH | heat, switch, mode, fan, automaticAirswitch | — |
| `A33U` | 美的中央空调-超薄轻音TS | heat, switch, mode, fan, automaticAirswitch | — |
| `A36E` | 美的中央空调-设计家SJ | heat, switch, mode, fan, automaticAirswitch | — |
| `A36P` | 美的中央空调-玲珑LL | heat, switch, mode, fan, automaticAirswitch | — |
| `A37I` | 美的加湿器SZK-1Y80 | switch, mode, humidity, gear, workStatus | commonFaultDetection, dry, waterRemain, closeTime, openTime, voice |
| `A37M` | 美的风管机-乐享LX | heat, switch, mode, fan, automaticAirswitch | — |
| `A37O` | 美的风管机-星光科技XGKJ | heat, switch, mode, fan, automaticAirswitch | — |
| `A37P` | 美的风管机-星光XG | heat, switch, mode, fan, automaticAirswitch | — |
| `A38G` | 美的风管机-悦享YX(2)2 | mode, switch, fan, temperature, automaticAirswitch | — |
| `A38H` | 美的风管机-悦享YX(1)3 | mode, switch, fan, temperature, automaticAirswitch | — |
| `A38I` | 美的风管机-设计家SJ(1) | mode, switch, fan, temperature, automaticAirswitch | — |
| `A38M` | 添眠止鼾枕 | snoringStatus, detectGear, pillowStatus, antiGear, switchLED | deviceControl |
| `A38O` | 美的风管机-颐享iX(3) | mode, switch, fan, temperature, automaticAirswitch | — |
| `A39I` | 美的中央空调-理想家LX2 | mode, switch, fan, temperature, automaticAirswitch | — |
| `A39X` | COLMO风管机-CA38ZN8A2 | mode, switch, fan, temperature, automaticAirswitch | Dry, customhumidity |
| `A39Y` | 美的风管机-乐享LX(1)3 | mode, switch, fan, temperature, automaticAirswitch | — |
| `A39Z` | 美的风管机-星光旗舰XGQ(1)3 | mode, switch, fan, temperature, automaticAirswitch | — |
| `A3A0` | 美的风管机-星光时尚XG(1)3 | mode, switch, fan, temperature, automaticAirswitch | — |
| `A3A1` | 美的风管机-雅境YJ(1)3 | mode, switch, fan, temperature, automaticAirswitch | — |
| `A3AG` | 美的风管机-梦想家MX(1) | mode, switch, fan, temperature, automaticAirswitch | — |
| `A3AH` | 美的风管机-梦想家MXP(1) | mode, switch, fan, temperature, automaticAirswitch | — |
| `A3AK` | COLMO睿极中央空调 | switch, mode, fan, temperature, automaticAirswitch | — |
| `A3AO` | ICF AI Classic智能底床 | oneKeyReset, sleepstatus, headAngle, lieControl, legAngle | — |
| `A3B7` | 美的中央空调-空气梦想家MX | mode, switch, fan, temperature, automaticAirswitch | — |
| `A3B8` | 美的中央空调-星光XGpro | mode, switch, fan, temperature, automaticAirswitch | — |
| `A3B9` | 美的中央空调-雅境YJ | mode, switch, fan, temperature, automaticAirswitch | — |
| `A3BN` | 小佩智能宠物厕所 | boxState, catStatus, childLock, cleanMode, clean | data |
| `A3CG` | 美的智能干衣机 | switch, mode, faultDetection, action, status | leftTime |
| `A3CJ` | COLMO智能干衣机 | switch, mode, faultDetection, action, status | leftTime |
| `A3CM` | COLMO智能洗衣机 | switch, mode, faultDetection, action, status | leftTime |
| `A3DK` | COLMO图灵中央空调 | switch, mode, fan, temperature, automaticAirswitch | — |
| `A3DQ` | COLMO新象中央空调 | switch, mode, fan, temperature, automaticAirswitch | — |
| `A3DR` | COLMO睿极中央空调 | switch, mode, fan, temperature, automaticAirswitch | — |
| `A3DV` | 小佩智能喂食器SOLO | foodStatus, childLock, battery, action, status | perWeight |
| `A3DZ` | 美的中央空调 | switch, mode, fan, temperature, automaticAirswitch | — |
| `A3E0` | 美的风管机 | switch, mode, fan, temperature, automaticAirswitch | — |
| `A3E2` | 美的水力模块 | automatic, switch, temperature, goOut, status | — |
| `A3FW` | 美的风管机 | switch, mode, fan, temperature, automaticAirswitch | — |
| `A3FY` | COLMO厨卫中央空调 | switch, mode, fan, temperature, automaticAirswitch | — |
| `A3FZ` | COLMO 复式洗衣机 | action, faultDetection, mode, status, switch | leftTime, washerdoubleType |
| `A3G0` | COLMO厨卫中央空调 | switch, mode, fan, temperature, automaticAirswitch | — |
| `A3G3` | COLMO新象中央空调 | switch, mode, fan, temperature, automaticAirswitch | — |
| `A3GM` | 美的中央空调 | switch, mode, fan, temperature, automaticAirswitch | — |
| `A3GN` | 美的风管机 | switch, mode, fan, temperature, automaticAirswitch | — |
| `A3GT` | COLMO新象中央空调 | switch, mode, fan, temperature, automaticAirswitch | — |
| `A3H2` | 华凌中央空调HL | switch, mode, fan, temperature, automaticAirswitch | — |
| `A3H3` | 华凌风管机HL1 | switch, mode, fan, temperature, automaticAirswitch | — |
| `A3H4` | 华凌风管机HL | switch, mode, fan, temperature, automaticAirswitch | — |
| `A3H5` | 小天鹅风管机SW1 | switch, mode, fan, temperature, automaticAirswitch | — |
| `A3H8` | 小天鹅中央空调LW | switch, mode, fan, temperature, automaticAirswitch | — |
| `A3H9` | 美的风管机SS | switch, mode, fan, temperature, automaticAirswitch | — |
| `A3IW` | 美的中央空调SS | switch, mode, fan, temperature, automaticAirswitch | — |
| `A3J8` | 美诺智能洗碗机 | action, mode, productModel, status, switch | filterElement1, filterElement2, filterElement3, leftTime, commonFaultDetection |
| `A3JU` | COLMO冰箱CRBUS601X1A | aiSwitch, disinfectSwitch, freshTemperature, iceMode, refrigerateSwitch | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3JY` | COLMO冰箱CRBUF452NA2 | aiSwitch, disinfectSwitch, freezeSwitch, inhibitPurineCabin, refrigerateSwitch | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3K3` | 小天鹅风管机LW | switch, mode, fan, temperature, automaticAirswitch | — |
| `A3KN` | COLMO水系统中央空调C-T1-副本1 | switch, mode, fan, temperature, automaticAirswitch | commonFaultDetection |
| `A3L9` | 方太智能嵌隐升降油烟机 | gear, gestureSwitch, lightSwitch, status, switch | delayOff |
| `A3MM` | 美诺智能蒸炉 | action, mode, status, switch, temperature | leftTime, commonFaultDetection |
| `A3MN` | 美诺蒸微一体机 | action, mixMode, status, switch, temperature | leftTime, commonFaultDetection |
| `A3MO` | 美诺微烤一体机 | action, mixMode, status, switch, temperature | leftTime, commonFaultDetection |
| `A3NU` | 华帝智能油烟机 | gear, lightSwitch, status, switch, workBurnerStatus | commonFaultDetection |
| `A3NV` | 方太智能集成净洗中心 | action, addMode, mode, status, switch | leftTime, commonFaultDetection |
| `A3NY` | COLMO冰箱CRBUF532A2A | aiSwitch, disinfectSwitch, freezeSwitch, iceMode, refrigerateSwitch | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3O0` | 小佩双翼猫厕所P9905 | boxState, catStatus, childLock, clean, cleanMode | data |
| `A3O3` | COLMO冰箱CRBUS533A2A | aiSwitch, disinfectSwitch, freezeSwitch, iceMode, refrigerateSwitch | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3O9` | 美的除湿机N7DO1 | anionSwitch, gear, humidity, mode, switch | delayOff, delayOn, commonFaultDetection |
| `A3OD` | 美的空气能热水器天悦 | mode, faultDetection, temperature, status, switch | deviceType |
| `A3QR` | 箭牌智能毛巾架AKS22GGSP | childLockSwitch, drying, heat, mode, switch | dryingLeftTime, dryingTime |
| `A3R4` | COLMO冰箱CRBUF522C3 | aiSwitch, disinfectSwitch, freezeSwitch, iceMode, refrigerateSwitch | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3R5` | COLMO冰箱CRBUF520C2 | aiSwitch, disinfectSwitch, freezeSwitch, iceMode, refrigerateSwitch | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3SD` | 老板洗碗机ZXW80 S2U | action, mode, switch, statusDoor, status | filterElement1, filterElement2, leftTime, commonFaultDetection |
| `A3U8` | 嘉格纳Expressive 艺境系列全自动意式咖啡机 | mode, brewingMode, action, status, switch | commonFaultDetection |
| `A3Y3` | 卡萨帝光年洗碗机 | action, mode, status, switch, statusDoor | remoteControlService |
| `A43Y` | 嘉格纳臻境系列咖啡机 | mode, brewingMode, action, status, switch | commonFaultDetection |
| `A44N` | 方太智能油烟机F5 | gear, gestureSwitch, lightSwitch, status, switch | delayOff, commonFaultDetection, remoteAuth |
| `A44O` | 方太智能油烟机JCD18TA | gear, lightSwitch, gestureSwitch, status, switch | delayOff, commonFaultDetection, remoteAuth |
| `A44P` | 方太智能油烟机JR01T | gear, gestureSwitch, lightSwitch, status, switch | delayOff, commonFaultDetection, remoteAuth |
| `A451` | 欧瑞博空调 | fan, humidity, mode, switch, temperature | commonFaultDetection |
| `A45I` | 方太智能油烟机V1 | gear, lightSwitch, gestureSwitch, status, switch | delayOff, commonFaultDetection, remoteAuth |
| `ZG0F` | 华为全屋智能 AI超感传感器 | luminance, switch, backlight, faultDetection, action | devLocation, basicFence, userFence1, userFence2, userFence3, userFence4, userFence5, userFence6, basicFenceEvent, userFenceEvent1, userFenceEvent2, userFenceEvent3, userFenceEvent4, userFenceEvent5, userFenceEvent6, reboot |
| `ZG1M` | AI辅助康养传感器 | luminance, switch, backlight, faultDetection, action | devLocation, basicFence, userFence1, userFence2, userFence3, userFence4, userFence5, userFence6, basicFenceEvent, userFenceEvent1, userFenceEvent2, userFenceEvent3, userFenceEvent4, userFenceEvent5, userFenceEvent6, reboot |
| `ZG1Y` | AI超感传感器 | luminance, switch, backlight, faultDetection, action | devLocation, basicFence, userFence1, userFence2, userFence3, userFence4, userFence5, userFence6, basicFenceEvent, userFenceEvent1, userFenceEvent2, userFenceEvent3, userFenceEvent4, userFenceEvent5, userFenceEvent6, reboot |
| `ZG1Z` | AI超感传感器 Lite | luminance, switch, backlight, faultDetection, action | devLocation, basicFence, userFence1, userFence2, userFence3, userFence4, userFence5, userFence6, basicFenceEvent, userFenceEvent1, userFenceEvent2, userFenceEvent3, userFenceEvent4, userFenceEvent5, userFenceEvent6, reboot |
| `ZG38` | AI睡眠传感器 | luminance, switch, backlight, faultDetection, action | devLocation, basicFence, userFence1, userFence2, userFence3, userFence4, userFence5, userFence6, basicFenceEvent, userFenceEvent1, userFenceEvent2, userFenceEvent3, userFenceEvent4, userFenceEvent5, userFenceEvent6, reboot |
| `ZGE0` | 华为网络录像机NVR800-A02-16P | switch, shootSwitch, cruiseSwith, videoSwitch, alarmEvent | pushStatus |
| `0107` | 灯带组 | switch, brightness, colour, lightMode | — |
| `100m` | 嵌入式电蒸箱 | switch, temperature, steam, faultDetection | — |
| `101L` |  | switch, switch1, switch2, switch3 | delay |
| `101r` | 得邦智能吸顶灯 | switch, brightness, cct, lightMode | delay |
| `101s` | 美的清羽智能风扇FTS30 | switch, fan, temperature, faultDetection | delay, delay |
| `103O` | 欧普香薰助眠灯 | switch, brightness, colour, faultDetection | aroma |
| `103P` | 欧普网关OPLYWG | discovery, switch, brightness, colour | voice, location, groupControl, favorite, groupManage, groupDevList, breathiLight |
| `104M` | 欧普智能灯带OPDD | switch, mode, brightness, colour | relativeDelay |
| `104X` | 柏翠电烤箱PE5389WH | temperature, upTemperature, downTemperature, faultDetection | oven |
| `1054` | 瑞晶吊灯RAL-1 | switch, cct, brightness, colour | — |
| `1056` | 瑞晶灯带RAL-3 | switch, cct, brightness, colour | — |
| `105G` |  | switch, switch1, switch2, switch3 | delay |
| `105H` |  | switch, switch1, switch2, switch3 | delay |
| `105T` | YeeLight彩灯 | switch, mode, brightness, faultDetection | relativeDelay |
| `1062` | 飞比彩灯NZCW125W-H1 | switch, mode, brightness, colour | relativeDelay |
| `106I` | 迈迪加Nox音乐床头灯SN902W | switch, brightness, colour, nightLight | sleepAid, alarmClock , handControl, wirelessaudio |
| `1077` | 云水母智能护眼台灯 | switch, brightness, cct, lightMode | lightNoisyWakeUp, lightGraduallyWakeUp, delay |
| `1082` | 小熊养生壶YSH-A15U6 | mode, command, status, currentTemperature | keepWarmTime, keepWarmTP, warmOnoff, workState, heatpower, preTime, remPreTime, workTime, remWorkTime, faultCode |
| `110J` | 云梦 | headLegControl, lieControl, childlock, reset | memoryControl, leisureControl |
| `111T` | 佛山照明智能吸顶灯ZNQP-9W | switch, brightness, colourMode, cct | — |
| `112S` | 东屋静脉锁V8 | discovery, alarm, battery, volume | counterLockStatus, event, keyList, controller |
| `114K` | 亚摩斯IH电磁电饭煲AS-IHW40Y | mode, start, status, faultDetection | warm, preTimeEnd, workTime, leftTime, warmDuration, cookInfo |
| `114M` | 奥普智能晾衣机D6 | action, airDry, drying, lightSwitch | — |
| `121P` | 亚摩斯IH电压力锅AS-YDG502H | switch, mode, command, status | currentPressure, preTime, workTime, leftTime, warmDuration, cookInfo, faultCode |
| `128P` | nimova智能护眼台灯Pro | switch, brightness, lightMode, cct | delay |
| `130O` | A.O.史密斯燃气热水器 | switch, machineSafeStatus, temperature, mode | burningStatus, loopStatus, gasSafeStatus, noColdWaterMode, noColdWater, boost, reserveTimer, faultCode |
| `131B` | 莱克智能循环扇 | switch, mode, speed, onOffBeep | speedPercent, angleMenu, onOffLight, autoOff, delay |
| `132Z` | A.O.史密斯甲醛净化器800C+/700C | switch, childLock, brightness, workMode | detection, windSpeed, modeActive, countdown, PM25, formaldehyde, gasLevel, windCount, filter1, filter2, filter3, filterNet, faultCode |
| `133H` | 电热水器 | switch, mode, status, temperature | instantHeating, aes, maxCapacity, reserveTimer, faultCode |
| `133L` | FSL智颖吸顶灯 | switch, brightness, colourMode, cct | delay, NightlightMode |
| `133M` | FSL智能双色灯泡 | switch, brightness, colourMode, cct | delay |
| `133O` | FSL智能调光调色筒灯 | switch, brightness, colourMode, cct | — |
| `135S` | 流光开关一联 | switch, lightMode, colour, backlight | memoryState |
| `137W` | A.O.史密斯热泵热水器HPA-EZ系列 | switch, mode, status, temperature | instantHeating, aes, pumpCycleTimer, singleCycle, faultCode |
| `138O` | 空调控制器 | switch, mode, currentTemperature, targetTemperature | wind |
| `138Q` | 迷你水暖机 | switch, gear, mode, faultDetection | — |
| `144F` | 南方家居智能电动床 | legMassage, headMassage, massageTimer, modeSelect | massageTimerSec, reportData, realData, AlarmClock, Resetpositon, MotorAction, Savepositon, ControlheadLeg, ControlLeg, ControlHead |
| `146Z` | 亚摩斯扫地机AS-X5E | status, action, mode, powerswitch | commonFaultDetection, modeswitch, box, suction, power, worktime, area |
| `148T` | 木林森睿智系列LED台灯 | switch, brightness, colourMode, lightMode | tomatoClk |
| `153E` | 领普三键墙壁开关 | switch, switch1, switch2, switch3 | led |
| `154E` | 漾美无线充智能台灯 | switch, brightness, colourMode, lightMode | — |
| `154F` | 三思LED天花灯 | switch, brightness, lightMode, colourMode | delay |
| `155A` | A.O.史密斯甲醛净化器455C-FH | switch, childLock, brightness, workMode | detection, windSpeed, modeActive, countdown, PM25, formaldehyde, gasLevel, windCount, filter1, filter2, filter3, faultCode |
| `155C` | A.O.史密斯甲醛净化器400C-FH | switch, childLock, brightness, workMode | windSpeed, modeActive, PM25, formaldehyde, filter1, filter2, filter3, faultCode |
| `155F` | FSL智薄卧室灯 | switch, brightness, colourMode, cct | delay |
| `170E` | 雷士护眼灯 | switch, backlight, brightness, rest | countdown, autoAdjust |
| `171X` | A.O.史密斯ESC系列 | switch, machineSafeStatus, temperature, mode | burningStatus, gasSafeStatus, faultCode |
| `175M` | 艾美特移动地暖D22-A | switch, childLockSwitch, temperature, screenSwitch | timing, state |
| `181K` | 艾美特移动地暖WD22-A4 | switch, childLockSwitch, temperature, screenSwitch | state, timing |
| `187D` | 欧普暖芯浴霸 HWE6102i | switch, lightSwitch, mode, temperature | leftTime, setWorkTime |
| `188X` | MPE休闲床 | headControl, legControl, mode1, mode2 | footControl, TV, antiSnore, zeroGravity, flat, head, foot, lamp |
| `2008` | 欧普炫彩床头灯 | switch, brightness, colour, mode | templateSet6, templateSet5, templateSet4, templateSet3, templateSet2, templateSet1, templateSave, sleep, elantra |
| `200D` | A.O.史密斯甲醛净化器455C+ | switch, childLock, brightness, workMode | detection, windSpeed, modeActive, countdown, PM25, formaldehyde, gasLevel, windCount, filter1, filter2, filter3, filterNet, faultCode |
| `2019` | 烁为汽车氛围灯 | switch, brightness, model, lightswitch | atmospherebrightness, contourbrightness, customcolor, lightcolor |
| `202K` | 小熊智能加湿器 | switch, humidity, gear, faultDetection | TimingShutdown, BactericidalFunction, TargetHumidity |
| `202Z` | 三思智能LED球泡灯 | switch, brightness, lightMode, colourMode | delay |
| `203U` | 12W恒流调光调色驱动 | switch, brightness, colourMode, cct | — |
| `203X` | 24W恒流调光调色驱动 | switch, brightness, colourMode, cct | — |
| `204B` | 60W恒压调光调色驱动 | switch, brightness, colourMode, cct | — |
| `204E` | 120W恒压调光调色驱动 | switch, brightness, colourMode, cct | — |
| `20CL` | 12W双色温射灯调光驱动器套装 | switch, brightness, cct, faultDetection | — |
| `20CN` | 15W双色温射灯调光驱动器套装 | switch, brightness, cct, faultDetection | — |
| `20CS` | 智汇云三位轻触开关面板 | switch, switch1, switch2, switch3 | delay |
| `20FM` | 海令调色调光器 | switch, colourMode, colour, brightness | — |
| `20I0` | 华为智选 欧普智能台灯Pro | switch, brightness, lightMode, cct | studyMode, studyResult, nightMode, delay |
| `20ID` | 星团智能驱蚊器 | switch, workStatus, mode, switchLight | timeRemaining, once |
| `20KX` | HEIMAN空气质量检测仪 | temperature, humidity, pm25, hcho | noise, Identify, Istempc, Language, Disturb, TemperatureThr, power, AlarmState, HumidityThr |
| `20PN` | FIVE智能刀筷砧板杀菌架 | cabinetSwitch, cabinetMode, cabinetStatus, alarm | TargetTime, Lock, LeftTime, CustTime |
| `20QZ` | 欧派油烟机 | gear, mode, lightSwitch, faultDetection | power |
| `20SM` | 欧派油烟机 | gear, mode, lightSwitch, faultDetection | power |
| `20TB` | 美菱茶吧机 | switch, status, faultDetection, heat | curtemp, warm, heattemp, WaterHealthPot, WaterKettle |
| `20TJ` | 易百珑双路开关 | switch, memorySwitch, switch1, switch2 | Pair, CleanPair |
| `20TN` | 亚摩斯料理破壁机AS-PB60B | action, gear, status, faultDetection | workTime, leftTime, timingSwitch, timing, stirAction, stirWorkTime, modeRecipes |
| `20XC` | 控客-肖邦水地暖面板 | switch, mode, temperature, childLockSwitch | — |
| `20XI` | 控客-肖邦电地暖面板 | switch, mode, temperature, childLockSwitch | — |
| `20YQ` | 亚摩斯电水壶AS-CP071 | switch, status, temperature, faultDetection | workMd |
| `20YY` | 智能充气宝 | switch1, start, mode, status | commonFaultDetection, time, times, pressureBAR, pressurePSI, led, pressure, power |
| `20ZJ` | 智能恒温水壶 | mode, status, temperature, presetSwitch | preTimeStart, PowerSwitch, time, PoweroffMemory, LongBoiling, WaterMonitoring, TemperatureAdjustment, Chlorine |
| `214Q` | 智能颈椎按摩仪 | switch, intensity, mode, heat | power, leftTime, countdown |
| `215N` | 触控三开零火开关 | switch, switch1, switch2, switch3 | — |
| `215V` | 智能环境盒子 | temperature, humidity, pm25, luminance | — |
| `2165` | 中央空调智能网关 | switch, mode, temperature, fan | — |
| `216L` | HEIMAN智能门窗传感器 | doorEvent, status, battery, temperAlarm | — |
| `216S` | HEIMAN智能水浸报警器 | alarm, battery, iceAlarm, silencer | — |
| `216X` | 亚摩斯加湿器AS-V22Q | switch, gear, faultDetection, light | timing |
| `217K` | 开关智能控制器3型 | switch, switch1, switch2, switch3 | — |
| `2180` |  | opener, mode, action, status | — |
| `218A` | 西顿24W防蚊虫快装智能吸顶灯 | switch, brightness, lightMode, cct | — |
| `218E` | 西顿30W防蚊虫快装智能吸顶灯 | switch, brightness, lightMode, cct | — |
| `218F` | 西顿40W防蚊虫快装智能吸顶灯 | switch, brightness, lightMode, cct | — |
| `2196` | 圆和三路智能开关 | switch, switch1, switch2, switch3 | — |
| `219L` | 脉冲颈椎智能按摩仪 | switch, voiceSwitch, mode, heat | commonFaultDetection, strength |
| `21AN` | 汇优尚品A6智能牙刷 | battery, mode, position, status | filterElement, brushingHistory, brushScore, brushLead, moreSetting, time |
| `21BA` | 超声波清洗机 | switch1, mode, start, status | commonFaultDetection, power, times |
| `21D9` |  | status, gas, action, sensitivity | — |
| `21DA` |  | hcho, status, action, sensitivity | — |
| `21DG` | 云起奇点开关模块PRO三联 | switch, switch01, switch02, switch03 | memoryState |
| `21DJ` |  | luminance, temperature, humidity, battery | — |
| `21EJ` | JW智能开关4键型 | switch1, switch2, switch3, switch4 | — |
| `21EM` | JW智能空调 | switch, mode, temperature, fan | — |
| `21GC` | 艾美特空气循环扇CA23-AD37 | switch, mode, fan, onOffBeep | timing |
| `21GH` | JW空气检测C型 | temperature, humidity, hcho, tvoc | co2 |
| `21GI` | JW空气检测D型 | temperature, humidity, pm25, hcho | — |
| `21LS` | 欧普读写台灯SE | switch, brightness, colourMode, lightMode | tomatoClk, delay |
| `21VG` | FSL智影炫彩灯带-2米 | switch, brightness, commonMode1, commonMode2 | progressTurnOn, progressTurnOff, Create |
| `220K` |  | switch, mode, temperature, fan | — |
| `221P` |  | switch, mode, temperature, fan | — |
| `221V` |  | switch, switch1, switch2, switch3 | — |
| `2265` | 凯迪仕智能门锁HK600 | lockState, lockMode, lockStatus, battery | lastActionTime, lockAlarm, event, keyList, faultCode |
| `227T` | 亚摩斯睿雅零火开关双键 | switch, switch1, switch2, brightness | — |
| `22CL` | 澳柯玛H-power高能瞬热电热水器M101 | switch, mode, temperature, faultDetection | state, linertemperature, flow |
| `22EB` | 松堡王国儿童智能电动床 | headControl, legControl, massageTimer, modeSelect | — |
| `22F2` | 蓓慈足浴器BZ312V1 | switch, status, temperature, faultDetection | Gushing, Red, temper |
| `22GR` | 澳柯玛智能电热水器C707H | switch, mode, temperature, faultDetection | state, setmode, preStart, prSwitch, breakdown |
| `22GW` | 汇优尚品电动牙刷A6 | battery, mode, status, position | setWorkTime, filterElement, brushingHistory, time |
| `22HW` | 亚摩斯嵌入式射灯 | switch, brightness, colourMode, cct | — |
| `22QW` | 澳柯玛智能电热水器B808H | switch, mode, temperature, faultDetection | state, prestart, powerdown, frequency |
| `22RZ` | 澳柯玛智能燃气热水器13S005H | switch, mode, temperature, faultDetection | preswitchtwo, preswitchone, code, pretimetwo, pretimeone, WaterInjection, waterpump, Zerocoldwater, airflow, wateryield, antifreezing, flow, draughtfan, flame, promotion |
| `22S6` | 御芳华按摩仪 | switch, workStatus, model, switch1 | electricity, worktime, Time, stage |
| `22SL` | 奥佳华颈肩按摩器 | switch, stop, alarm, heat | surTime, suspend, electricity, KnockingSpeed, classic, time |
| `22YK` | 亚摩斯智能踢脚线取暖器 | switch, gear, childLockSwitch, temperature | timingOn, timingOff |
| `22YV` | 澳柯玛智能电热水器A022H | switch, mode, temperature, faultDetection | state, Residualhotwater, Latemorningbath, Pointsare, prestart, Frequencywashing |
| `230Z` | 萨瓦尼智能门H1 | lockState, lockStatus, battery, alarms | alarmStatu, events |
| `23DS` | 倍轻松智能艾灸盒 | switch, temperature, battery, gear | commonFaultDetection, countdown |
| `23RO` | 欧普智能吸顶灯 | switch, brightness, colourMode, cct | — |
| `23RP` | 欧普智能吸顶灯 | switch, brightness, colourMode, cct | — |
| `23RQ` | 欧普智能吸顶灯 | switch, brightness, colourMode, cct | — |
| `23W2` | ACEMATIC灯光模块 | switch, switch1, switch2, switch3 | — |
| `2487` | 空气质量检测仪 | temperature, humidity, hcho, alarm | tempHEnable, tempLEnable, humHEnable, humLEnable, lightpower, lightdelaytime, displaymode |
| `248K` | 控客-肖邦四路灯控面板 | switch1, switch2, switch3, switch4 | — |
| `24DE` | 万达康健身律动机 | video, speed, mode, switch2 | eTime, eCalorie, changeSpeed, cal, time, data, changeTime, music, turn |
| `24R6` | 华督桌面即热饮水机 | status, childLockSwitch, faultDetection, temp | currentOutlet, ONOFF, WaterVolume |
| `24RF` | 澳柯玛智能燃气热水器S011H | switch, mode, temperature, faultDetection | code, draughtfan, flame, WaterInjection, flow, wateryield, promotion |
| `24RG` | 澳柯玛智能燃气热水器S012H | switch, mode, temperature, faultDetection | code, flow, draughtfan, promotion, flame |
| `24T6` | 澳柯玛智能燃气热水器16S005H | switch, mode, temperature, faultDetection | preswitchtwo, preswitchone, pretimetwo, pretimeone, code, promotion, antifreezing, flame, WaterInjection, airflow, waterpump, wateryield, Zerocoldwater, draughtfan, flow |
| `253M` | ZTK纯净加湿器 | switch, humidity, childLockSwitch, gear | capacity, Anion, Sound, Light |
| `25BD` | 爱特嘉智能即热饮水机AH-103 | status, waterMode, temperature, faultDetection | outlet, currentOutlet |
| `25BN` | 香百年智能香薰机 | autoConnect, switch, mode, battery | commonFilterElement1, Intensity, numberofcycles, recommend, manual, durationtime |
| `25DF` | 华督桌面即热饮水机 | status, childLockSwitch, faultDetection, temp | currentOutlet, WaterVolume, ONOFF |
| `25G8` | 美森导入导出焕颜美容仪 | switch, status, battery, skinMode | F008, F007, F006, F005, F004, F003, F002 |
| `25J6` | 59S UVC LED紫外线消毒杀菌柜 | cabinetSwitch, cabinetMode, cabinetStatus, workMode | EquipmentStatus, abnormalTip, counts, powerDisplay, finish |
| `25KG` | 思麦耳降噪会议麦克风音箱 | switch, volume, battery1, mute | — |
| `25KW` | 虎牌保险箱 | switch, lockStatus, lockState, alarms | batter, events |
| `2657` | 清易智慧集尘扫拖机器人H40 PLUS | deviceStatus, action, mode, remoteControl | edgeElement, hepaElement, rollElement, commonFaultDetection, scheduleService, path, musicPackage, sensor, startClean, areaSetting, cleanRecord, ossSN, mapService |
| `2661` | MAXHUB 会议全向麦音箱 | switch, battery, status, toneMode | userManual, microphone, volumeControl, electricity, noiseReduction |
| `26JA` | 虎牌酷博保险箱 | battery, alarms, lockState, lockStatus | events |
| `26M7` | 得途BBQ智能空气炸锅 | action, status, temperature, presetSwitch | recipes, workTime, preTimeEnd, preTimeStart, leftTime, Devicestatus, customizemode |
| `26U1` | 酷轻松石墨烯气囊支撑腰带 | switch, mode, temperature, heat | remaining, workstatus, timerlabel |
| `26YS` | 好易点智能晾衣机消毒款 | action, status, disinfect, lightSwitch | disinfectRemTime, commonFaultDetection |
| `279E` | 雅乐思电磁炉 | switch, status, mode, temperature | powergear, determine, time1 |
| `27OA` | 博思迪美容仪 | switch, status, gear, model | Lowbatterywarning, firmwareupdate, bluetooth |
| `27QE` | MOS调光器 | switch1, switch2, brightness1, brightness2 | fadeTime1, fadeTime2 |
| `27SC` | 领普双键墙壁开关 | switch, switch1, switch2, brightness | — |
| `280A` | 小益H7智能门锁 | lockState, alarm, openEvent, Volume | faultCode, KeyListA, GetKeyInfo, PwdOperationRes, DeleteOperation, NFCencryption, VerfiyMode, BatteryA, UserOperation |
| `286J` | LeveTop温感美妆蛋 | battery, switch, gear, status | rejuvenateeyes, ultramicropenetration, deepcleaning, currentmoderecord |
| `28AH` | 智能颈枕按摩器 | switch, voiceSwitch, gear, model | tempSwitch, leftTime, power |
| `28TR` | OES按摩椅 | switch1, speed, position, heat | devState, automaticMassage, manualMassage, automaticAirPressure, manualAirPressure, powerRating, backrest, time, part, fixedPoint, zeroGravity, width, scrollWheel |
| `291T` | 飞利浦直流变频循环扇ACR3142CF | switch, mode, fan, temperature | angleAutoLROnOff, RunTime, OSD |
| `292D` | 飞利浦直流变频循环扇ACR3144CF | switch, mode, fan, temperature | angleAutoLROnOff, angleAutoAllOnOff, childLockOnOff, RunTime |
| `292H` | 飞利浦直流塔扇ACR3144TF | switch, mode, fan, temperature | angleAutoLROnOff, anionOnOff, RunTime |
| `295G` | TCL智爱台灯 | switch, colourMode, cct, lightMode | progressSwitch, brightnes, Switchintelligent, CountdownOff, countdowntime |
| `296V` | LAICA牌KE9402系列净饮机 | status, waterMode, childLockSwitch, lightswitch | outletWater, currentTemp, cupcheck, Devicerrow, soundswitch, brewtime, temperatureadjust, cupadjust, menuchoose |
| `299H` | 九牧i4Pro智能马桶ZD7420 | switch, setting, gear, status | WarnEvent, faultEvent, control |
| `29EP` | 蓓慈X4V智能剃须刀 | switch, status, mode, battery | time, commonFaultDetection, TXSD, TXSJ, SYSJ, LJZT, CZDT, CZJL, JCSM, TXXZS, LXS |
| `29IR` | 梦百合0压智能床 | oneKeyReset, modeSelect, headControl, legControl | Operatinginstructions, GetMemoryMode, Customgear |
| `29MJ` | 护腰美姿椅 | switch, mode, currentTemperature, temperature | time, timeRemaining |
| `29V2` | 万家乐燃气热水器16TX8 | switch, presetSwitch, temperature, faultDetection | orderTime, cmdtype, Doubleboost, Heatparameter |
| `2A8P` | sraum4路开关面板 | switch1, switch2, switch3, switch4 | scene4, scene3, scene2, scene1 |
| `2A9A` | D-Controls面板 | switch1, switch2, switch3, switch4 | — |
| `2AA5` | FSL调光调色吸顶灯-72W | switch, brightness, colourMode, cct | delay |
| `2AB5` | ACEMATIC智能液晶面板 | switch, switch1, switch2, switch3 | — |
| `2AJH` | 瑞美燃气容积式热水器 | switch, status, temperature, faultDetection | settemperature, hotwatercirculation, timing2, timing1, smartfunctions, energysavingfunction, instantfunction |
| `2AJR` | 瑞美商用电热水器 | switch, status, temperature, faultDetection | timing2, energysavingfunction, powerregulation, timing1 |
| `2AJY` | Paulmann单色温智能灯 | switch, brightness, lightMode, colourMode | delay |
| `2AN9` | 鸿雁三键智能开关U2 | switch1, switch2, switch3, indicator | — |
| `2ANJ` |  | switch, mode, temperature, fan | — |
| `2ANP` | 德姆勒取暖器 | switch, childLockSwitch, temperature, backlight | HeaterGear, ENDTIME |
| `2AO1` | 美菱550L冰箱 | refrigerateSwitch, freezeSwitch, intelligentSwitch, faultDetection | ColdTemp, HolidyMode, SensorCold, SensorFreeze, ColdOffMode, FreezeTemp |
| `2AO4` | 美菱503L冰箱 | refrigerateSwitch, freezeSwitch, intelligentSwitch, faultDetection | FreezeTemp, SensorFreeze, ColdOffMode, SensorCold, SensorAttemper, HolidyMode, ColdTemp, AttemperOffMode, AttemperTemp |
| `2AOR` | FSL儿童卧室灯-海星 | switch, brightness, colourMode, cct | delay |
| `2AOS` | FSL智薄客厅灯 | switch, brightness, colourMode, cct | — |
| `2AOY` | 鸿雁双路智能开关模块 | switch, switch1, switch2, indicator | — |
| `2ASU` | 慕派AA级智能护眼台灯 | switch, brightness, colourMode, lightMode | tomatoClk |
| `2AW2` | 智能恒温水壶-高配 | mode, status, temperature, presetSwitch | preTimeStart, WaterMonitoring, time, Chlorine, LongBoiling, PoweroffMemory, PowerSwitch, TemperatureAdjustment |
| `2AW4` | usmile星光智能声波电动牙刷 | status, battery, mode, intensity | score, brushingHistory , brushHeadLife, direction, startPositon, splashProof, LED, time |
| `2AW5` | usmile-U悦智能声波电动牙刷 | status, battery, mode, intensity | score, brushingHistory , brushHeadLife, direction, startPositon, splashProof, LED, handheldAwaken, time |
| `2AWX` |  | switch, mode, temperature, fan | — |
| `2BB3` | 华为智选 欧普智能吸顶灯128W | switch, brightness, cct, lightMode | location, timeMelody, wallSwitch1, wallSwitch2, wallSwitch3, delay |
| `2BE5` | 麦乐克门窗开关传感器 | doorEvent, status, battery, temperAlarm | — |
| `2BE9` | 麦乐克声光报警器 | switch, lightSwitch, temperAlarm, volume | alamTime |
| `2BES` | FSL蓝牙调光调色吸顶灯 | switch, brightness, colourMode, cct | — |
| `2BET` | FSL蓝牙调光调色筒灯 | switch, brightness, colourMode, cct | — |
| `2BEU` | FSL蓝牙调光调色球泡 | switch, brightness, colourMode, cct | — |
| `2BFE` | 东东阅读台灯 | switch, brightness, colourMode, lightMode | tomatoClk |
| `2BGN` | 三雄极光Pak智能吸顶灯 | switch, brightness, cct, lightMode | — |
| `2BGU` | 沙漠鱼智能台灯 | switch, brightness, cct, lightMode | — |
| `2BOS` |  | switch, mode, temperature, fan | — |
| `2BS9` | FSL智趣UFO吸顶灯 | switch, brightness, colourMode, cct | delay |
| `2BSN` | 水母云炫昼智能插座夜灯 | switch, memorySwitch, backlight, faultDetection | power, delay, consumption, NightLightBrightness, NightLightSwitch |
| `2BSZ` | FSL智贝吸顶灯 | switch, brightness, colourMode, cct | delay |
| `2BWB` | 欧派油烟机 | switch, gear, mode, lightSwitch | — |
| `2C40` | 2He小夜喵智能照明消毒灯 | colourMode, lightMode, battery, UVSwitch | lightbright, batteryStatus, LEDSwitch |
| `2C7X` | 西蒙四位智能开关 | switch1, switch2, switch3, switch4 | BackLightMode |
| `2C87` | 西蒙新风开关 | switch, fan, temperature, faultDetection | FilterScreenFuction, FilterScreenPeriod, BypassSwitchFunction, BypassSwitchMode, BackLightLevel |
| `2CA6` | ACEMATIC空调模块 | switch, mode, temperature, fan | — |
| `2CCK` | ACEMATIC色温灯 | switch, brightness, colourMode, cct | — |
| `2CP2` | DBH智能肌肉按摩仪 | switch, battery, status, action | queryinfo, fgMode, workTime |
| `2CPF` | 仁豪家居功能床 | headControl, legControl, massageTimer, modeSelect | — |
| `2CQF` |  | switch1, switch2, backlightMode, switch | — |
| `2CQU` | 9W双色温射灯驱动器 | switch, brightness, cct, faultDetection | — |
| `2CQV` | 卡赫智能净水器1000G | switch, status, water, faultDetection | inputTds, outputTds, filterElement1, filterElement2, filterElement3, contWater |
| `2CYS` | 朗思智能锁 | lockState, lockMode, battery, alarm | event, faultCode |
| `2D6F` | 双色温灯带驱动器 | switch, brightness, cct, faultDetection | — |
| `2D9M` | 一维生活功夫椅 | switch, autoMode, intensity, heat | airIntensity, airMode, ManualMode, time, Pause, MassageArea, PositionAdjustment, KneadAndRoll |
| `2DCY` | 华为智选 杜亚智能窗帘 | action, opener, reverse, mode | faultCode, manualSwitch, calibrate, memoryControl, favorite |
| `2DDV` | 即眠睡眠仪 1s PRO | switch, commonExecution1, commonExecution2, commonExecution3 | F005, F004, F003, F002 |
| `2DEK` | 皇泰肩带按摩仪 | switch, heat, speed, mode | leftTime, countdown, direction |
| `2DMC` | 二路智能开关 | switch, switch1, switch2, backlight | — |
| `2DSD` | 拉孚三路智能开关 | switch, switch1, switch2, switch3 | — |
| `2DU2` | 华为智选 MPE智能床 | headControl, legControl, headLegControl, modeSelect | — |
| `2DXC` | 龙泉智家三路墙壁开关 | switch, switch1, switch2, switch3 | — |
| `2E3I` | 爱特嘉3L智能速热饮水机 | status, waterMode, temperature, faultDetection | outlet, currentOutlet |
| `2ENH` | 亚摩斯星耀开关三键 | switch, switch1, switch2, switch3 | — |
| `2EXV` | 达伦自然光吸顶灯S3 Pro | switch, brightness, colourMode, lightMode | nightmode, natural, lampswitch |
| `2EZU` | 亚摩斯睿雅单火开关三键 | switch, switch1, switch2, switch3 | — |
| `2F0K` | ERNTE智能料理盒 | status, action, presetSwitch, commonMode1 | workTime, leftTime, preTimeStart, CurrentTemp, settemp |
| `2F7Q` | 绿田创T5锂电洗车机 | status, battery, mode, connectionStatus | faultCode, ProductIntroduction, UsageLog |
| `2F8A` | 绿田勃朗宁B4锂电洗车机 | status, battery, mode, connectionStatus | faultCode, ProductIntroduction, UsageLog |
| `2F8B` | 绿田路飞L2智能充气泵 | status, mode, faultDetection, connectionStatus | currentAirPressure, XSZY |
| `2FC2` | 造梦者新风机 | switch, fan, childLockSwitch, light | filterElement1, filterElement2, filterElement3, filterElement4, sound |
| `2FCZ` | 博顿物联三开 | switch, switch1, switch2, switch3 | — |
| `2FRJ` | 九牧i80智能马桶ZD8710 | stop, toiletMode, seatStatus, setting | control, tStatus, toiletGear, warnEvent, faultEvent |
| `2FRK` | 九牧P50挂墙智能马桶ZD8621 | stop, toiletMode, seatStatus, setting | faultEvent, warnEvent, toiletGear, control, tStatus |
| `2FS0` | 箭牌智能浴缸 | temperature, status, switch, gear | WaterInlet |
| `2FSN` | 720智能多效除味器 | switch, childLockSwitch, mode, lightSensor | roomArea, cumulativetime, bright |
| `2G35` | 光谱嫩肤仪 | switch, status, workMode, battery2 | state, lowbattery |
| `2G5Z` | 西蒙睿极智能吸顶灯 | switch, colourMode, lightMode, sleepMode | progressTurnOn, brightne, colorTemperature |
| `2GCE` | 美邦空调 MAC35V3YHR | switch, mode, temperature, faultDetection | ScreenDisplay, Disinfection, Economy, PtcHeat, StrongMode, Horizontal, Vertical, Wind, Sleep |
| `2GCF` | VHV驱蚊香薰落地灯 | switch, light, gas, status | laser, level, errorCode, timerOperate, list, touchLight, wifiLight, mosquito |
| `2GD2` | 奥佳华按摩沙发OG-5008Plus | autoMode, lbpMode, swing, status | Airmassage, Time, movementadjust, Airintensity, zerogravity, Strengthadjust, Faultcode, backadjust, action1, ManualMode |
| `2GEB` | 燃气传感器 | silencer, selfCheck, alarm, gasSensor | commonFaultDetection |
| `2GKB` | 得力保管箱鸿晖系列 | battery, alarms, lockState, lockStatus | events |
| `2GKC` | 迈德斯特E系列护理床 | oneKeyReset, modeSelect, headControl, legControl | backWarning, System, bedpanWarning, turnWarning, legWarning, Lock, Time, Tilt, Memory2, Bedpan, Memory4, Memory3, Memory1, AutoRoll |
| `2GKE` | 虎牌博瑞保管箱 | battery, alarms, lockStatus, lockState | events |
| `2GKF` | 虎牌炫彩保管箱 | battery, lockStatus, alarms, lockState | events |
| `2GKG` | 美森智能电动理容器 | mode, battery, switch, status | AvailableTime, FirmwareUpgrade, TotalTimes |
| `2GKH` | 美森智能吸发理发器 | mode, battery, status, switch | CutterheadRemaining, CutterHeadAlarm, FirmwareUpgrade, AvailableTime, ResetCutterHead, TotalTimes, SafeLok |
| `2GKM` | 罗曼智能儿童牙刷HK3 | spraySwitch, battery, workGuidance, voiceGuidance | brushingHistory, Brushhead, use, OTA, guidesetting, dutstatus, workmode, partitionreminder, brushstrenght, workhours |
| `2GRN` | 择柔(ZR)智能声波电动牙刷 | mode, initPosition, spraySwitch, gear | filterElement, setWorkTime, brushingHistory, BatteryLevel, LeftTime, WorkState |
| `2GRX` | 智能防漏宝 | valveStatus, waterUseData, waterTemperature, switch | commonFilterElement1, commonFaultDetection, DirectorOfMeasurement, DateStatistics, ParameterSetting |
| `2GSJ` | 达伦阿拉丁神灯 | switch, controlKey, light, position | focus, volume1, digitalzoom, correct |
| `2GTD` | 虎牌尊虎保险箱 | battery, lockStatus, alarms, lockState | events |
| `2GUY` | 小充嗨跑交流充电桩 | switch, chgMode, chaState, lock | driveStu, chgTim, chgGun, chgBK, chgStu, delete, faultStatus, chgPar, chgLog, Status |
| `2GV0` | 小充嗨跑交流充电桩 | switch, chgMode, chaState, lock | chgTim, chgGun, chgBK, chgStu, faultStatus, chgPar, delete, chgLog, Status |
| `2GV1` | 小充嗨跑交流充电桩 | switch, chgMode, chaState, lock | Status, chgLog, chgPar, delete, faultStatus, chgStu, chgGun, chgBK, chgTim |
| `2GVO` | 狄耐克智能三路开关面板 | switch, switch1, switch2, switch3 | — |
| `2H57` | 鲜芒情景灯 | lightMode, switch, cct, brightness | progressTurnOff, nightWakeup, progressTurnOn, toggleSwitch |
| `2H7W` | RND M1电动滑板车 | battery, status, mode, lock | bt.connection, shutdown1, update1, currentspeed, Themileage, unit, Cruisecontrol, Powerstart |
| `2H9J` | 商贤智能取暖器S8 | switch, childLockSwitch, temperature, heat | heatmain, mytimer, fire |
| `2HCI` | 艾芬达电热毛巾架 | switch, mode, temperature, reset | ota, consumepower, weektime, power, cumulativeduration, timing |
| `2HJH` | 凌度4G记录仪 | commonTask1, commonTask2, commonTask3, commonTask4 | connectState |
| `2HR4` | 轨迹三人位 | seatStatus, oneKeyReset, headLegControl, modeSelect | Controlmode, positionSelect, commonFaultDetection, Lock, MemorySet, Guide |
| `2HR7` | 西蒙二位智能开关 | switch, switch1, switch2, indicator | commonFaultDetection, switchStatus |
| `2HUZ` | 唯妙智能影音控制主机 | soundMode, switch, home, mute | playControl, microphone, back, music, hybrid, direction, ok |
| `2HW4` | 虎牌尚悦保险箱 | battery, lockState, alarms, lockStatus | events |
| `2HY5` | 因硕智能锁F1 | lockState, battery, alarm, openEvent | keyList, publicKey, remoteInfo, remoteCode, remoteResult, erroralarm, prvdooralarm, userlist |
| `2HY6` | 因硕智能锁T07 | lockState, battery, alarm, openEvent | keyList, publicKey, remoteInfo, remoteCode, remoteResult, erroralarm, prvdooralarm, userlist |
| `2HYV` | 金莱特多功能户外灯 | battery, light, mode, switch | — |
| `2I22` | 南威G款锂电角磨机 | battery, lock, speed, mode | switchR, upkeep, workTimer |
| `2I4I` | 可拆卸晾衣架踢脚线AHR4146WKS | childLockSwitch, gear, temperature, switch | timing, OSD |
| `2I8S` | 直流变频石墨烯踢脚线AHR5244KS | childLockSwitch, gear, temperature, switch | ReserveLeftTime, OSD |
| `2I9W` | 美菱552冰箱 | faultDetection, freezeSwitch, intelligentSwitch, refrigerateSwitch | freezerFloat, refrigeratorFloat, ColdOffMode, HolidyMode |
| `2IFB` | 艾主人智能洗地机 | status, battery, model, selfclean | commonFilterElement1, commonFilterElement2, commonFaultDetection, FirmwareUpgrade, Reconnect, VoiceSwitch |
| `2INR` | 艾家智能三位开关 | switch, switch1, switch2, switch3 | switchStatus, lightness |
| `2IUA` | 超人智能门锁Q5-RM | lockState, battery, alarm, openEvent | keyArray, userlist, remoteInfo, remoteResult, remoteCode, publicKey |
| `2IUB` | 西蒙一位智能场景开关 | mode1, switch1, indicator, deviceStatus | sceneButton1, commonFaultDetection |
| `2IVC` | 贝昂智能取暖器H3 | switch, faultDetection, gear, childLockSwitch | Shake, TimingOff |
| `2IVI` | 贝昂智能取暖器H5 | switch, gear, childLockSwitch, faultDetection | Shake, Screen, TimingOff |
| `2IVW` | 左点智能蒲团 | reset, temp, mode, connectStatus | open, play, close, mugwort, remainTime |
| `2IWN` | 朗威智能剃须刀 | mode, battery, status, switch | btConnection, userecord, deviceTime, bladeUseTime, bladeCleanTime, clearMode, shavSpeed, runTime |
| `2IWO` | 洒拖派 0 自动擦窗机 | status, action, mode, deviceStatus | commonFaultDetection, waterSpray, windowSide, statusA |
| `2IWW` | 智能门 JinLY | lockState, lockStatus, battery, openEvent | faultCode, tempPasswd, publicKey, encryptedText, tempPasswd2 |
| `2J1U` | 奥克斯剃须刀 | mode, battery, status, lock | btConnection, highTemp, bladeUseTime, bladeClean, bladeCleanTime, surplusTime, surplusCount |
| `2J3X` | A.O.史密斯净热一体机 | temperature, water, status, heatingSwitch | inputTds, outputTds, filterElement1, filterElement2, totalPurifyWater, faultDetection1, waterLevelStatus, keepWarmMode, addWaterMode |
| `2J7P` | 杜亚智能百叶 | changeDirection, rotationAction, opener, action | — |
| `2J8Z` | 企一照明RGB灯带蓝牙驱动 | colour, switch, brightness, colourMode | relBrightness, toggleSwitch, commonFaultDetection |
| `2JLF` | gb SMART智能安抚摇床 | status, gear, volume, speed | usage, knowledge, time, cryingSwitch, nightSwitch, music |
| `2JMD` | 无叶电吹风 | mode, temperature, speed, status | currentSpeed, RealTemp |
| `2JMX` | 轨迹单人位 | seatStatus, oneKeyReset, headLegControl, modeSelect | Controlmode, positionSelect, commonFaultDetection, MemorySet, Guide, Lock |
| `2JO1` | 电小酷智能转换插座 | indicator, switch, memorySwitch, childLockSwitch | power, electric, commonFaultDetection, ProtectionSwitch, ChargingProtection |
| `2JPT` | 美森智能电动修足器 | workStatus, gear, battery, status | useTime, workingMode, workingTimes |
| `2K89` | 霍尼韦尔空气净化器KJ460F-J21SW | switch, mode, fan, pm25 | filterElement1, filterElement2 |
| `2KDA` | 正泰三孔智能插座 | switch, indicator, memorySwitch, faultDetection | electric, power |
| `2KEK` | simon玻璃材质10A五孔智能插座面板 | indicator, switch, memorySwitch, faultDetection | power, electric, IndicatorMode |
| `2KEL` | simon玻璃材质16A三孔智能插座面板 | switch, indicator, faultDetection, memorySwitch | power, electric, IndicatorMode |
| `2KGW` | 班弗智能锁7000A | lockState, battery, alarm, openEvent | publicKey, userlist, remoteCode, remoteInfo, remoteResult, keyArray |
| `2KH3` | 班弗智能锁8000A | lockState, battery, alarm, openEvent | publicKey, userlist, remoteCode, remoteInfo, remoteResult, keyArray |
| `2KH4` | 班弗智能锁9000A | lockState, battery, alarm, openEvent | publicKey, userlist, remoteCode, remoteInfo, remoteResult, keyArray |
| `2KJ0` | KAMAI灯 | lightMode, switch, cct, brightness | progressTurnOff, nightWakeup, toggleSwitch, progressTurnOn |
| `2KKW` | 嘿码智能剃须刀 | status, alarm, workMode, workStatus | worktime, cleanTime, cutterTime, ota, power, version |
| `2KPG` | 天智星 | switchSpeed, opener, action, directionalmode | — |
| `2KXR` | 霍尼韦尔红外人体移动光照传感器 | luminance, battery, mode, sensitivity | reminder, motionDetected, commonFaultDetection |
| `2KXS` | 霍尼韦尔红外和超声波双鉴人体移动光照传感器 | luminance, battery, mode, sensitivity | reminder, motionDetected, commonFaultDetection |
| `2L8N` | 锐亿智能剃须刀RS393 | mode, battery, status, lock | seekDevice, bladeCleanTime, bladeCongestion, bladeUseTime, dataenv, surplusCount, surplusTime |
| `2L8U` | 立达信元梦吸顶灯 | lightMode, switch, cct, brightness | lamplightMode |
| `2L8W` | 立达信云上吊灯 | lightMode, switch, cct, brightness | lamplightMode |
| `2L9O` | 奥莱敏控人体传感器 | luminance, lightBrightness, switchNightLight, sensitivity | alarmTime, motionDetected, pirs |
| `2LAD` | meipont空调挂机 | switch, mode, temperature, faultDetection | Wind, Horizontal, Sleep, Vertical, Economy, StrongMode, PtcHeat, Disinfection, ScreenDisplay |
| `2LAI` | 锐亿智能剃须刀RS293 | mode, battery, status, lock | bladeUseTime, bladeCleanTime, bladeCongestion, seekDevice, dataenv, surplusTime, surplusCount |
| `2LC9` | 鸿蒙智选 小豚当家室外摄像头 4G版 | switch, shootSwitch, videoSwitch, alarmEvent | lteService, pushStatus |
| `2LHX` | 厨下净水 | mode, faultDetection, temperature, status | inputTds, outputTds, filterElement1, filterElement2, totalPurifyWater |
| `2LIW` | 贝克巴斯智能水龙头 | waterTemperature, waterUseData, switch, status | velocity, downDistance, pairingStatus, clear, rightDistance, leftDistance, effluent, reconfigure, onOff, leftFunc, pullStatus |
| `2LIZ` | 达伦阿拉丁神灯X30 Pro | switch, controlKey, light, position | digitalzoom, focus, volume1, correct |
| `2LLE` | meipont空调挂机 | switch, mode, temperature, faultDetection | ScreenDisplay, Disinfection, Vertical, PtcHeat, Horizontal, StrongMode, Wind, Sleep, Economy |
| `2LP1` | 海雀智能摄像头3Pro 4K版 128GB | shootSwitch, alarmEvent, switch, videoSwitch | — |
| `2LYO` | 松下洗衣机 XQG100-V19R | switch, mode, childLockSwitch, status | leftTime, commonFaultDetection, newStatus, newAction |
| `2M6W` | 创明智能卷帘 | changeDirection, switchSpeed, opener, action | — |
| `2M78` | 欧瑞氏2000W暖风机 | temperature, gear, switch, swing | commonFaultDetection, timers, workingStatus |
| `2MAS` | 锐亿剃须刀RS166 | status, workStatus, alarm, lock | Records, version, power, ota, cutterTime, cleanTime, remainTime, remainNumber |
| `2MC1` | SJSW三色灯 | lightMode, switch, brightness, cct | fade |
| `2ME0` | 奥科PLC版开合帘电机时尚款 | changeDirection, switchSpeed, opener, action | commonFaultDetection, placeMemory |
| `2MEN` | 力博得智能牙刷3 Pocket | mode, battery, workGuidance, voiceGuidance | setWorkTime, deviceLock, hardware, deviceColor, brushHistory, brushDay |
| `2MFF` | 佛山照明智能插座 | indicator, switch, faultDetection, childLockSwitch | electric, power |
| `2MFX` | 创明智能百叶帘-TP35 | changeDirection, rotationAction, opener, action | — |
| `2MGV` | 吉豪X5智能筒射灯 | lightMode, switch, brightness, cct | fade |
| `2MIQ` | 艾优智能剃须刀 | status, bladeStatus, workMode, workStatus | syncTime, findDevices, currentElectricity, alrmPrompt, bladeCleaning, hota |
| `2MJD` | 红外万能遥控中心 | fanSwitch, indicatorSwitch, fanMode, status | backup, mediaKey, batchCmd, projectorKey, rcList, mediaKey1, mediaKey2, matchedCap, mediaKey3, airKey, TVKey, purifierKey, speakerKey, STBKey, delay1, customKey |
| `2MKA` | 杜亚智能百叶-PLC款 | changeDirection, rotationAction, opener, action | — |
| `2MLD` | 红外转发器 | indicatorSwitch, fanMode, fanSwitch, status | backup, batchCmd, mediaKey, projectorKey, rcList, mediaKey1, mediaKey2, matchedCap, mediaKey3, airKey, TVKey, purifierKey, speakerKey, STBKey, customKey, delay1 |
| `2MNJ` | 四合一空气质量检测仪 | temperature, humidity, switchNightLight, pm25 | co2, reportSetting, pm10 |
| `2MNU` | 佳普乐宏尚智能毛巾架 | disinfect, temperature, nightlightSwitch, drying | dryingTime, dryingLeftTime |
| `2MO0` | 锐亿剃须刀RS 399B | status, lock, alarm, workStatus | find, remainTime, cleanTime, remainNumber, cutterTime, ota, version, power, Records |
| `2MOU` | 心智悦环境控制器C1 | humidity, switch, temperature, faultDetection | airKeyGear, airKeyMode |
| `2MPF` | 礼意久久暖腰带柴犬款 | switch, hot, battery, alarm | CurrentTemperature, countdown, shake, shutdown, BLEstatus |
| `2MRT` | meipont空调柜机 | switch, mode, temperature, faultDetection | Wind, PtcHeat, Sleep, Vertical, StrongMode, Economy, Horizontal, Disinfection, ScreenDisplay |
| `2MVH` | meipont美邦空调挂机 | switch, mode, temperature, faultDetection | ScreenDisplay, Disinfection, Economy, PtcHeat, Wind, Sleep, Vertical, Horizontal, StrongMode |
| `2MVJ` | meipont美邦空调挂机 | switch, mode, temperature, faultDetection | ScreenDisplay, Disinfection, PtcHeat, Economy, Vertical, Horizontal, StrongMode, Wind, Sleep |
| `2MXG` | 家用可燃气体探测器 | silencer, selfCheck, alarm, gasSensor | commonFaultDetection |
| `2MXV` | Dual智能料理微波炉DIK02-HW | childLockSwitch, action, status, temperature | doorOpen, cook, appointment, addDelay, fire |
| `2MZW` | 智能控制器-盛和 | switch, mode, fan, sceneMode | commonFilterElement1, filterElement |
| `2N09` | 米芙拉浴室取暖器加热毛巾架一体机 | mode, temperature, windSwitch, drying | commonFaultDetection |
| `2N38` | 美菱509WPU9CZX冰箱 | faultDetection, freezeSwitch, iceMode, intelligentSwitch | featureMode, freezerFloat, refrigeratorFloat |
| `2N53` | 嘿码护发高速吹风机 | mode, temperature, speed, status | — |
| `2N5I` | 创明智能PLC梦幻帘 | rotationAction, opener, rotationAngle, action | — |
| `2N5X` | 快轮智能电动滑板车1s | battery, switch, gear, action | finddevice, momentInfo, motorLock, devCmd, paraSet, eventInfo, devInfo, deviceTime |
| `2N63` | 电动智能窗HC86PY | childLock, action, lock, windowOpener | — |
| `2N7I` | 月光星球暖腹腰带 | light, massage, heat, battery | usetime |
| `2NBY` | meipont美邦空调挂机 | switch, mode, temperature, faultDetection | Vertical, Economy, Sleep, Wind, ScreenDisplay, Horizontal, Disinfection, PtcHeat, StrongMode |
| `2ND3` | 传感器-盛和 | tvoc, temp, hcho, pm25 | co2, pm10, humi |
| `2NNO` | 正泰智能五孔插座 | switch, indicator, memorySwitch, faultDetection | power, electric |
| `2NRD` | dynacare涡轮六叶剃须刀 | mode, battery, status, bladeStatus | time, screenAnimation, history, resetTime, shavingSpeed, duration |
| `2NSM` | 箭牌智能浴缸AQH1782TQ-HM | switch, status, switch1, massage | gear1, targettemperature |
| `2NSO` | 箭牌智能浴缸ANH1782TQ-HM | switch, status, switch1, massage | gear1, targettemperature |
| `2NVF` | 森瑞智能百叶 | changeDirection, rotationAction, opener, action | SBZT |
| `2NVP` | 推拉窗HY | childLock, action, lock, windowOpener | — |
| `2NX3` | 倍益康便携式深层肌肉按摩仪 | action, battery, gear, workStatus | btconnection, commonFaultDetection, revolution, countdown, otaUpgrade |
| `2NX4` | 倍益康超迷你肌肉按摩器 | action, battery, gear, workStatus | btconnection, commonFaultDetection, otaUpgrade, countdown, revolution |
| `2NXA` | Jeep智能剃须刀J1H | status, faultDetection, speed, clean | bleStatus, cutterTime, worktime, electricity, ota |
| `2O0E` | usmile智能电动牙刷U7 | mode, battery, workStatus, voiceSwitch | tlock, expert, firmwareUpdate, record, life, smart, resetFactory, brushing, setTime, brushingState |
| `2O10` | usmile智能电动牙刷U7 Pro | mode, battery, voiceSwitch, workStatus | record, brushingState, tlock, setTime, resetFactory, firmwareUpdate, expert, archive, brushing, life |
| `2O2O` | 水母云智能磁吸轨道灯T1 | lightMode, brightness, cct, switch | fade |
| `2O34` | 威仕达百叶帘WSVM24 | rotationAction, opener, action, speed | commonFaultDetection, night, day, limit, pair |
| `2O5Q` | WYC 智能热敷腰带 | switch, hot, alarm, temperature | shutdown, baterry, countdown, shake, BLEstatus |
| `2O8R` | 佳文智能调光调色灯 | lightMode, switch, cct, brightness | fadeTime |
| `2O8Z` | 智能富氢蒸茶壶 | status, warmSwitch, temperature, alarm | steamTimeLeft, boilMode, steamMode, qingTimeLeft, qingMode |
| `2O9M` | eachone一起玩 智能立式护眼学习灯 | lightMode, switch, brightness, cct | — |
| `2OIB` | 小青芒千分比深度调光线性灯 | lightMode, switch, brightness, cct | memoryswitch, countdown, Ontime, offtime |
| `2OJQ` | 电小酷智能转换插座 | indicator, switch, memorySwitch, childLockSwitch | power, electric, commonFaultDetection, ProtectionSwitch, ChargingProtection |
| `2OJR` | 暖通网关 MC5 Pro | faultDetection, gatewayAction, rs485Switch, operation | 485NetInfo, acGroupList, acList, automaticGroup, backup, backupData, connectMode, ctlCapability, delay, diagnose, diagnosis, freshAirGroupList, freshAirList, generalGrouplist, generalList, heaterGroupList, heaterList, heaterProtocol, homeGatewayCap, port1protocolList, offlineOta, port2protocolList, reboot, timeZone, vrvProtocol |
| `2OS3` | 水母云智能磁吸轨道灯T2 | lightMode, brightness, cct, switch | fade |
| `2OS6` | 水母云智能磁吸轨道灯T3 | lightMode, brightness, cct, switch | fade |
| `2OYH` | 吉豪晶漾智能灯具 | lightMode, brightness, cct, switch | progressSwitch |
| `2P7W` | 保温电热水壶 | heatMode, mode, temperature, status | commonFaultDetection |
| `2P9M` | 异形不锈钢壶 | warmSwitch, mode, temperature, status | — |
| `2P9N` | 智能电热水壶-XK981Z | warmSwitch, mode, status, temperature | — |
| `2PG7` | 焕醒大功率推白剃须刀 | battery, bladeStatus, status, travelLock | bladeReset |
| `2PI3` | 吉豪智能筒射灯 | brightness, cct, lightMode, switch | progressSwitch |
| `2PIR` | 吉豪一帘幽梦智能灯具 | brightness, cct, lightMode, switch | progressSwitch |
| `2PIS` | 吉豪星辰智能灯具 | brightness, cct, lightMode, switch | progressSwitch |
| `2Q3F` | 三思插座小夜灯 | indicator, lightBrightness, lightSwitch, switch | — |
| `2Q41` | 吉豪西江月智能灯具 | brightness, cct, lightMode, switch | progressSwitch |
| `2Q9F` | 埠威充气泵搭电一体机 | mode, battery, status, lightMode | airPressure, commonFaultDetection |
| `2QM7` | 佳普乐Realm智能马桶R1A | autoFlip, offSeatAction, seatStatus, toiletStatus | disinfection, foamShield, seatHeating, toiletSetting |
| `2QN9` | 火焰山多功能智能取暖桌 | action, childLockSwitch, gear, status | delayOff, multiWarmer |
| `2QP2` | 佳普乐Realm智能马桶R5N | hipNozzlePos, offSeatAction, seatStatus, stop | disinfection, drySetting, favorite, foamShield, seatHeating, toiletSetting, washSetting |
| `2QQM` | 恩仕AXENT.Lite全智能坐便器 | massageMode, offSeatAction, seatStatus, stop | drySetting, seatHeating, toiletSetting, washSetting |
| `2QQO` | 恩仕AXENT.Lite轻智能坐便器高配版 | autoFlip, offSeatAction, seatStatus, toiletStatus | foamShield, seatHeating, toiletSetting |
| `2QUH` | 奥马法式平嵌冰箱 | freezeSwitch, intelligentSwitch, refrigerateSwitch, status | featureMode, freezerFloat, refrigeratorFloat, commonFaultDetection |
| `2QWE` | 智能门铃HY | irMode, switch, toneMode, volume | overstayTime, commonFaultDetection |
| `2QXU` | 欧派克全景幕控制器 | action, backLight, reminderSwitch, workStatus | — |
| `2QZR` | 欧普单路开关执行器PLC | indicator, buzzer, memorySwitch, switch | backup, commonFaultDetection |
| `2R4G` | 寐MINE智能冥想音乐助眠枕 | battery, musicMode, switch, volume | countDown |
| `2RC9` | 名豆之约智能插座10A 2代 | childLockSwitch, indicator, switch, commonMemorySwitch | electric, power, commonFaultDetection |
| `2RCL` | 名豆之约智能插座16A 2代 | childLockSwitch, indicator, switch, commonMemorySwitch | electric, power, commonFaultDetection |
| `2RCO` | 名豆之约智能通断器 2代 | jogMode, indicator, switch, commonMemorySwitch | timeSet |
| `2RDU` | 蒙奇奇暖宫腰带 | battery, heat, mode, shock | countDown |
| `2RI3` | 欧普单路开关执行器WIFI | buzzer, indicator, memorySwitch, switch | backup, commonFaultDetection |
| `2RMF` | FLYX智能往复式剃须刀 | battery, bladeStatus, searchDevice, status | bladeClean, bladeReset, btConnection, speedDetection, commonFaultDetection |
| `2RNB` | 西顿照明T5无线单色温筒射灯照明驱动 | brightness, indicator, switch, commonMemorySwitch | fadeTimeSetting, lightCurveSetting, relBrightness, commonFaultDetection |
| `2RU7` | 友望智能高速吹风机Pro | mode, temperature, speed, status | hairDryer, commonFaultDetection |
| `2RUP` | 达伦智能台灯 大想 | brightness, eyeSuggestion, lightMode, switch | delayTurnoff, fadeTime, lightFormulaArray, preLightFormulaArray, preview, usageRecord |
| `2RUX` | 车载香氛机 | autoConnect, gear, scent, switch | filterElement, filterElement02, filterElement03, commonFaultDetection |
| `2RZS` | VITH专研智能电动牙刷 Pro Max | battery, mode, voiceGuidance, workGuidance | brushingHistory, customPlan, filterElement, polishElement |
| `2S1R` | 名豆之约智能插座基础款10A | childLockSwitch, indicator, memorySwitch, switch | — |
| `2S1V` | 电小酷智能插座CP1-HW-B | childLockSwitch, indicator, memorySwitch, switch | commonFaultDetection |
| `2S4O` | 智能红外光热坐垫 | massageMode, mode, switch, temperature | commonFaultDetection |
| `2S5M` | 左点智能扫振电动牙刷 | battery, mode, travelLock, workStatus | brushingHistory, filterElement, setWorkTime, commonFaultDetection, resetLifeTime, checkIn, record, smart, hisRecord |
| `2SD7` | 车载摄像头 | battery, silencer, switch, videoSwitch | cameraInfo, connectDev, wifi, commonFilterElement |
| `2SEY` | 三菱电机空调壁挂机AC系列 | fan, mode, switch, temperature | capabilityset, commonFaultDetection |
| `2SFZ` | 恒洁电热毛巾架LMP835-03E-SN | dryingGear, heat, status, switch | dryingLeftTime, dryingTime, commonFaultDetection |
| `8003` | 智能台灯 | switch, backlight, brightness, lightMode | nightSwitch, nightWakeup, delay |
| `9MTJ` | 智控夜灯 | brightness, cct, status, switch | — |
| `9MTR` | 智控水壶 | mode, status, switch, temperature | commonFaultDetection |
| `9MXO` | 智控空调 | fan, mode, switch, temperature | — |
| `9MZK` | 智控洗衣机 | action, mode, status, switch | leftTime |
| `9MZL` | 智控茶具 | mode, warmSwitch, temperature, status | outlet |
| `9MZQ` | 智控咖啡机 | action, mode, status, switch | time |
| `9MZY` | 智控直饮机 | mode, status, temperature, waterMode | outletWater, waterPurifier |
| `A054` | 飞利浦加湿器HU4908 | switch, humidity, gear, faultDetection | — |
| `A08G` | 美的智能电风扇 | switch, mode, fan, connectStatus | — |
| `A0CO` | 美的波轮洗衣机 | switch, action, mode, status | leftTime |
| `A0CP` | 格力智能空调 | switch, mode, temperature, fan | — |
| `A0CQ` | 美的滚筒洗衣机 | switch, action, mode, status | leftTime |
| `A0E0` | 海尔智能空调 | switch, mode, temperature, fan | — |
| `A0GR` | 蒸烤箱 | remoteSwitch, gateSwitch, status, preStatus | hotStatus |
| `A0MJ` | 智能3D气流风管式温湿平衡型3D气流风管式温湿平衡型 | switch, mode, temperature, fan | commonFaultDetection, choiceOfColdAndHot, fan2, fan1 |
| `A0MK` | 超薄风管式温湿平衡型 | switch, mode, temperature, fan | commonFaultDetection, choiceOfColdAndHot |
| `A0ML` | 衣帽间防潮嵌入式标准式 | switch, mode, temperature, fan | commonFaultDetection, choiceOfColdAndHot, fan1 |
| `A0MM` | 智能3D气流风管式新风净化型3D气流风管式新风净化型 | switch, mode, temperature, fan | commonFaultDetection, fresh3D, fan2, fan1, choiceOfColdAndHot |
| `A0MN` | 超薄风管式新风净化型 | switch, mode, temperature, fan | commonFaultDetection, fresh3D, choiceOfColdAndHot |
| `A0MO` | 智能3D气流风管式PM2.5净化型3D气流风管式PM2.5净化型 | switch, mode, temperature, fan | commonFaultDetection, fan2, choiceOfColdAndHot, fan1 |
| `A0MP` | 超薄风管式PM2.5净化型超薄风管式标准型 | switch, mode, temperature, fan | commonFaultDetection, choiceOfColdAndHot |
| `A0MQ` | 智能3D气流风管式标准型3D气流风管式标准型 | switch, mode, temperature, fan | commonFaultDetection, fan1, choiceOfColdAndHot |
| `A0MR` | 超薄风管式大容量型 | switch, mode, temperature, fan | commonFaultDetection, choiceOfColdAndHot |
| `A0MS` | 卫浴用嵌入式标准型 | switch, mode, temperature, fan | commonFaultDetection, ventilation, choiceOfColdAndHot, fan1 |
| `A0MT` | 高耐久厨房用嵌入式标准型 | switch, mode, temperature, fan | commonFaultDetection, fan1, choiceOfColdAndHot |
| `A0MU` | 客厅向 | switch, mode, temperature, fan | commonFaultDetection, fan1, choiceOfColdAndHot |
| `A0MV` | 客厅向高级面板 | switch, mode, temperature, fan | commonFaultDetection, choiceOfColdAndHot, fan2, fan1 |
| `A0N7` | 智汇云RGB模块 | switch, brightness, colourMode, colour | — |
| `A0NQ` | 奥克斯空调 | switch, mode, temperature, fan | healthy, sleep, screen, supportHeat, eco |
| `A0OK` | 智能三通道插座 | switch, switch1, switch2, switch3 | — |
| `A0OR` | 智能三通道开关 | switch, switch1, switch2, switch3 | — |
| `A0OX` | 冷暖双色调光灯 | switch, brightness, colourMode, cct | — |
| `A0QP` | 美的蒸烤料理炉 | doorState, status, mode, action | — |
| `A0RD` | 单向气流嵌入式 | switch, mode, temperature, fan | commonFaultDetection, fan1, choiceOfColdAndHot |
| `A0RE` | 智能感知环绕气流嵌入式 | switch, mode, temperature, fan | commonFaultDetection, choiceOfColdAndHot, fan1 |
| `A0RG` | 环绕气流嵌入式 | switch, mode, temperature, fan | commonFaultDetection, fan1, choiceOfColdAndHot |
| `A0RH` | 中静压风管式 | switch, mode, temperature, fan | commonFaultDetection, choiceOfColdAndHot |
| `A0RI` | 自由静压风管式 | switch, mode, temperature, fan | commonFaultDetection, choiceOfColdAndHot |
| `A0RJ` | 内藏落地式 | switch, mode, temperature, fan | commonFaultDetection, choiceOfColdAndHot |
| `A0RK` | 明装落地式 | switch, mode, temperature, fan | commonFaultDetection, choiceOfColdAndHot |
| `A0RL` | 挂壁式 | switch, mode, temperature, fan | commonFaultDetection, fan1, choiceOfColdAndHot |
| `A0RV` | 九阳豆浆机 | switch, status, action, steam | commonFaultDetection, drink, iswarm, capacity, leftTime1 |
| `A0S7` | 安吉尔-净水设备 | switch, status, water, faultDetection | inputTds, outputTds, filterElement1, filterElement2, filterElement3, filterElement4, startWash |
| `A0TN` | 奥克斯空调 | switch, mode, temperature, fan | supportHeat, screen, sleep, eco, healthy |
| `A0UC` | 霍尼韦尔智能控制空调 | switch, mode, temperature, fan | — |
| `A0VG` | 海尔智能冰箱 | refrigerator, freezer, faultDetection, humanSensingStatus | vtRoom, intelligenceMode, dailyStatus, travelMode, speedFreezerStatus, quickFreezingMode, quickRefrigeratingMode, refrigeratorTemperatureC, freezerTemperatureC, vtRoomTemperature |
| `A0XN` | 帅康智慧健康烹饪空间 | switch, gear, lightSwitch, faultDetection | airQuality, cookConnect, yanshiguanji, youzao, zuozao, fengsuiyandong, qingxi |
| `A0YZ` | 西门子开关 | switch, switch1, switch2, switch3 | — |
| `A10E` | 九阳破壁机 | status, start, stop, cleanMode | commonFaultDetection, leftTimes, cupWarn |
| `A14C` | 九阳高速破壁调理机 | status, start, clean, stop | commonFaultDetection, startCloud, like, warmTime, leftTimes |
| `A1AF` | 美的净化器 | switch, mode, childLockSwitch, pm25 | hosting, openTime, closeTime |
| `A1AG` | 破壁机MJ-PB10P345 | action, mode, status, cupStatus | preTimeEnd, leftTime |
| `A1B5` | 美的冰箱 | refrigerateSwitch, freezeSwitch, refrigerator, freezer | — |
| `A1BR` | 美的燃气热水器 | switch, status, temperature, faultDetection | noCold, inWaterTemp |
| `A1BT` | 美的JSQ34-18HV燃气热水器 | switch, status, temperature, faultDetection | inWaterTemp, noCold |
| `A1BU` | 美的抽油烟机 | switch, gear, lightSwitch, faultDetection | — |
| `A1EW` | COLMO除湿机 | switch, mode, humidity, gear | — |
| `A1FS` | 九阳无涂层蒸汽电饭煲 | status, clean, stop, start | devStatus, pauseContinue |
| `A1H6` | 九阳智能养生壶 | status, faultDetection, stop, start | warmDuration, resetHoldingTemperature, devStatus |
| `A1HR` | 美的冰箱BCD-519WSGPZM(Q) | refrigerateSwitch, freezeSwitch, refrigerator, freezer | — |
| `A1HT` | 美的冰箱BCD-440WFGPZM(Q) | refrigerateSwitch, freezeSwitch, refrigerator, freezer | — |
| `A1JD` | 油烟机CXW-258-X10.i | switch, gear, mode, lightSwitch | Liftingposition |
| `A1KF` | 华凌冰箱BCD-239WTPZH | refrigerateSwitch, freezeSwitch, refrigerator, freezer | — |
| `A1KG` | 华凌冰箱BCD-398WFPZH | refrigerateSwitch, freezeSwitch, refrigerator, freezer | — |
| `A1KI` | 美的冰箱BCD-601WKPZM(E) | refrigerateSwitch, freezeSwitch, refrigerator, freezer | storagePower |
| `A1RM` | 美的CXW-260-B83S抽油烟机 | switch, gear, lightSwitch, faultDetection | — |
| `A1TW` | 华凌冰箱BCD-498WSPZH | refrigerateSwitch, freezeSwitch, refrigerator, freezer | — |
| `A1W2` | 九阳无涂层蒸汽电饭煲 | status, clean, stop, start | commonFaultDetection, pauseContinue, remainingTime, riceCup, progress |
| `A1Y2` | JSQ30-i12151-16家用燃气热水器 | switch, mode, temperature, ECO | commonFaultDetection, highTempUnlock, Poweroff, totalGas, totalWater, iwaterTmp |
| `A1YA` | 颁芙叠影系列烟机 | switch, mode, faultDetection, clean | manualClean, lightSwitch2, voice, gesture, sensorLight, autoClean, setTimer |
| `A1YJ` | 无滚布洗地机QX-V6.i-H | status, battery, sewageboxstate, cleanwaterboxstate | commonFaultDetection, VoiceMode, SelfCleanSwitch, VoiceVolume, WorkMode |
| `A1YT` | COLMO燃气热水器JSQ30-CE216-Z | switch, status, faultDetection, temp | noCold, inWaterTemp, gasLiftPrecent |
| `A1YU` | COLMO燃气热水器JSQ30-CE116 | switch, status, faultDetection, temperature | inWaterTemp, noCold |
| `A2AA` | JSQ30-i12152-16家用燃气热水器 | switch, mode, temperature, ECO | commonFaultDetection, highTempUnlock, totalWater, totalGas, iwaterTmp, Poweroff |
| `A2AB` | JSQ30-i12153-16家用燃气热水器 | switch, mode, temperature, ECO | commonFaultDetection, highTempUnlock, Poweroff, iwaterTmp, totalGas, totalWater |
| `A2GD` | 万和电热水器Q9D1 | switch, mode, status, temperature | commonFaultDetection, Book3Time, Book3, Book2Time, Book2, Book1Time, Book1, gears, SetPower, autopoweroff, ModeFlag, SetTemp, WaterTankTemp, WaterFresh, WaterRemainTime |
| `A2GN` | 西门子洗衣机 | action, mode, status, faultDetection | lefttime1 |
| `A2H3` | JSQ24-i12151-13家用燃气热水器 | mode, switch, temperature, ECO | commonFaultDetection, totalGas, iwaterTmp, totalWater, Poweroff, highTempUnlock |
| `A2H4` | JSQ24-i12152-13家用燃气热水器 | mode, switch, temperature, ECO | commonFaultDetection, highTempUnlock, iwaterTmp, totalGas, Poweroff, totalWater |
| `A2H5` | JSQ24-i12153-13家用燃气热水器 | switch, mode, temperature, ECO | commonFaultDetection, Poweroff, totalGas, iwaterTmp, highTempUnlock, totalWater |
| `A2I4` | 美的冰箱BCD-472WSPZM(E) | refrigerateSwitch, freezeSwitch, refrigerator, freezer | storagePower |
| `A2IU` | 美的电饭煲MB-HS408 | status, action, mode, faultDetection | keptWarmTime, leftTime, currentFun |
| `A2IV` | 美的电饭煲MB-HS508 | status, mode, faultDetection, action | keptWarmTime, leftTime, currentFun |
| `A2J3` | 美的踢脚线HDW22EVA1 | switch, gear, temperature, faultDetection | buttonBeepSwitch, preTimeOff, preTimeOn |
| `A2JM` | 智能三通道机械开关 | switch, switch1, switch2, switch3 | — |
| `A2NY` | 万和电热水器Q9D1 | switch, mode, status, temperature | commonFaultDetection, SetTemp, Book2Time, WaterTankTemp, Book3, gears, SetPower, Book1, Book2, Book1Time, WaterFresh, ModeFlag, WaterRemainTime, Book3Time, autopoweroff |
| `A2OZ` | TH7i燃气热水器 | switch, faultDetection, temperature, status | waterTap, StronRichWater, iwaterTmp, waterfallBath, cycle, Selfclean, totalWater, heating, totalGas, highTempUnlock |
| `A2P7` | KEKEN 商业锁F20 | lockState, lockStatus, lockMode, battery | ROOM |
| `A2PV` | KEKEN 商业锁P10 | lockState, lockStatus, lockMode, battery | ROOM |
| `A2PW` | KEKEN 商业锁P20 | lockState, lockStatus, lockMode, battery | ROOM |
| `A2Q4` | 万家乐燃气热水器零冷水系列 | switch, temperature, zeroColdSwitch, status | — |
| `A2TV` | 智汇云摄像头 | switch, shootSwitch, videoSwitch, alarmEvent | push |
| `A2TY` | 智汇云梦幻帘电机 | rotationAction, opener, rotationAngle, action | oper |
| `A2UA` | COLMO净水CWHO-RB117 | faultDetection, status, rinseSwitch, heatSwitch | outputTds, filterElement1 |
| `A2UZ` | CXW-200-E6090HS吸油烟机 | lightSwitch, gear, status, switch | commonFaultDetection, otcStat, otcSwitch, gearStat, lockStat, delayedShutdown, lockScreen, wacaStat |
| `A2VA` | COLMO冰箱CRBF620AD-A6 | freezeSwitch, freezer, refrigerateSwitch, refrigerator | — |
| `A2VB` | COLMO冰箱CRBS615AD-A6 | freezeSwitch, freezer, refrigerateSwitch, refrigerator | — |
| `A2VE` | SJ60燃气热水器 | switch, faultDetection, temperature, status | heating, cycle, waterfallBath, gasTotal, iwaterTmp, waterTotal, highTempUnlock |
| `A2VV` | 18QC1i燃气壁挂炉 | switch, faultDetection, status, heatSwitch | totalWater, eneMode, heatTemp, bathTemp, iwaterTmp, totalGas |
| `A2WY` | DDF50-BH04i电热水器 | switch, faultDetection, temperature, status | cTVolume, waterQuality, devMode, bacSwitch, aiBath, wPswitch |
| `A2X1` | DDF60-BH04i电热水器 | switch, faultDetection, temperature, status | wPswitch, aiBath, bacSwitch, waterQuality, cTVolume, devMode |
| `A2X2` | DDF50-BH03i电热水器 | switch, faultDetection, temperature, status | wPswitch, cTVolume, devMode, waterQuality, aiBath, bacSwitch |
| `A2X3` | DDF60-BH03i电热水器 | switch, faultDetection, temperature, status | waterQuality, aiBath, bacSwitch, devMode, cTVolume, wPswitch |
| `A2YI` | 美的嵌入式厨房空调 | switch, mode, fan, temperature | batchCmd, commonFaultDetection, dry, quickFryCenterPoint, visualization, quickFry, prepareFood |
| `A2ZZ` | 美的吸顶式厨房空调 | switch, mode, fan, temperature | batchCmd, commonFaultDetection, dry, prepareFood, quickFry, quickFryCenterPoint, visualization |
| `A30V` | COLMO全热交换新风机-GC1 | mode, speed, status, switch | — |
| `A31L` | COLMO全热交换新风机-GC1(2) | mode, speed, status, switch | — |
| `A32R` | 美的智能取暖器 | switch, temperature, gear, status | commonFaultDetection, preTimeOn, preTimeOff, buttonBeepSwitch |
| `A340` | 欧派智能磁吸轨道灯P24 | switch, brightness, faultDetection, cct | MasterPowerStatus, MasterLightMode, MasterLightType |
| `A341` | 欧派智能CW色温灯P21 | switch, brightness, faultDetection, cct | MasterPowerStatus, MasterLightMode, MasterLightType |
| `A342` | 欧派智能CW柜体灯带P25 | switch, brightness, faultDetection, cct | MasterLightMode, MasterLightType |
| `A343` | 欧派智能CW天花灯带P26 | switch, brightness, faultDetection, cct | MasterPowerStatus, MasterLightMode, MasterLightType |
| `A39C` | COLMO冰箱CRBUT406J-A1 | refrigerateSwitch, freezeSwitch, freezer, refrigerator | featureMode |
| `A3A5` | COLMO抽油烟机 | lightSwitch, status, switch, gear | commonFaultDetection |
| `A3AJ` | COLMO全热交换新风机-CAX500GC1(2) | mode, speed, status, switch | — |
| `A3AY` | 方太Y系列智能油烟机 | mode, lightSwitch, status, switch | commonFaultDetection, DelayTime, CtlUpDown, UpDownLock, definedFanGear |
| `A3BS` | 方太智能洗碗机 | switch, mode, action, status | leftTime, commonFaultDetection, preSet |
| `A3C4` | 小佩智能双子星喂食器 | action, battery, petStatus, status | feederPortion, powerSource, food2, food1 |
| `A3CK` | COLMO冰箱 | refrigerateSwitch, freezeSwitch, freezer, refrigerator | commonFaultDetection |
| `A3CR` | COLMO洗碗机 | statusDoor, action, switch, status | filterElement1, filterElement2, keepLeftTime, dryLeftTime, orderLeftTime, washLeftTime, commonFaultDetection |
| `A3D3` | 美的洗碗机 | statusDoor, action, switch, status | filterElement1, filterElement2, keepLeftTime, dryLeftTime, orderLeftTime, washLeftTime, commonFaultDetection |
| `A3DE` | COLMO挂机空调 | switch, mode, fan, temperature | — |
| `A3DF` | COLMO柜机空调 | switch, mode, fan, temperature | — |
| `A3DM` | 美的燃气热水器 | switch, temperature, zeroColdSwitch, status | commonFaultDetection |
| `A3DN` | COLMO燃气热水器 | switch, temperature, zeroColdSwitch, status | commonFaultDetection |
| `A3DT` | COLMO二代新风机 | mode, speed, status, switch | — |
| `A3DU` | COLMO一代新风机 | mode, speed, status, switch | — |
| `A3E6` | 海信智能空调 | switch, mode, fan, temperature | — |
| `A3E8` | 海信智能中央空调 | switch, mode, fan, temperature | — |
| `A3EB` | COLMO燃气热水器 | switch, temperature, zeroColdSwitch, status | commonFaultDetection |
| `A3EC` | 美的燃气热水器 | switch, temperature, zeroColdSwitch, status | commonFaultDetection |
| `A3EK` | 海信智能空调 | switch, mode, fan, temperature | — |
| `A3EX` | COLMO柜机空调 | switch, mode, fan, temperature | — |
| `A3EY` | COLMO柜机空调 | switch, mode, fan, temperature | — |
| `A3F2` | 海信智能室温控制器 | switch, mode, fan, temperature | — |
| `A3FN` | 美的一代全热交换新风机 | mode, speed, status, switch | — |
| `A3FP` | 美的二代全热交换新风机 | mode, speed, status, switch | — |
| `A3GJ` | 格力浴享系列中央空调 | switch, mode, fan, temperature | — |
| `A3GK` | 格力中央地暖空调 | switch, mode, fan, temperature | — |
| `A3GO` | 格力舒享系列中央空调 | switch, mode, fan, temperature | — |
| `A3GS` | 格力智能中央空调 | switch, mode, fan, temperature | — |
| `A3HD` | A.O.史密斯智能油烟机 | gear, lightSwitch, lockSwitch, switch | commonFaultDetection |
| `A3J7` | 美诺智能洗衣机 | action, mode, productModel, status | filterElement3, filterElement4, leftTime, commonFaultDetection |
| `A3JD` | 美诺蒸烤一体机 | action, mixMode, status, switch | leftTime, commonFaultDetection |
| `A3JE` | 美诺智能油烟机 | gear, lightSwitch, status, switch | commonFaultDetection |
| `A3JI` | 美诺智能烤箱 | mode, status, switch, temperature | leftTime, oven, commonFaultDetection |
| `A3JX` | COLMO冰箱CRBUK600IQ2 | disinfectSwitch, flexiTempCabin, freezeSwitch, refrigerateSwitch | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3KH` | 美的柜机空调T6 | fan, mode, switch, temperature | commonFaultDetection |
| `A3KJ` | 美诺智能暖碟机 | mode, status, switch, temperature | leftTime, commonFaultDetection |
| `A3LW` | 一拖一中央空调 | fan, mode, switch, temperature | — |
| `A3NN` | 九阳0涂层电饭煲 | action, mode, presetSwitch, status | food, leftTime, preTimeEnd, workTime, commonFaultDetection |
| `A3OE` | 智能晾衣架D35WMAX | action, lightBrightness, lightSwitch, status | commonFaultDetection |
| `A3PS` | Leader挂机 | fan, mode, switch, temperature | commonFaultDetection |
| `A3RA` | 美的壁挂式空调通用 | fan, mode, switch, temperature | commonFaultDetection |
| `A3RC` | 美的立柜式空调通用 | fan, mode, switch, temperature | commonFaultDetection |
| `A3RD` | 美的智能晾衣架 | action, lightBrightness, lightSwitch, status | dryRack, commonFaultDetection |
| `A3RZ` | 好太太智能晾衣架 | action, lightBrightness, lightSwitch, status | commonFaultDetection |
| `A3S0` | 海信挂机空调 | switch, mode, fan, temperature | — |
| `A3SS` | 嘉格纳200 系列升降式吸油烟机 | gear, lightSwitch, status, switch | delayOff, commonFaultDetection |
| `A3U5` | 嘉格纳Vario 400 系列酒柜61cm | alarm, bottomShelftemp, middleShelftemp, temperature | commonFaultDetection |
| `A3UA` | 嘉格纳Expressive 艺境系列蒸汽烤箱左侧铰链 | childLockSwitch, lackWater, status, switch | leftTime, oven, commonFaultDetection |
| `A3US` | 嘉格纳Expressive 艺境系列蒸汽烤箱 | childLockSwitch, lackWater, status, switch | leftTime, ovenSteamer, commonFaultDetection |
| `A3VP` | 能率热水器GQ-16K3AAFEX | flameStatus, status, switch, temperature | totalGas, totalWater, commonFaultDetection |
| `A3W0` | 老板蒸烤一体机CQ01 i1 | lightSwitch, status, switch, temperature | leftTime, ovenSteamer, commonFaultDetection |
| `A3WU` | 方太智能烤箱(智能屏) | childLockSwitch, lightSwitch, status, temperature | leftTime, oven, commonFaultDetection |
| `A3XK` | 老板蒸烤一体机C98A D3P | lightSwitch, status, switch, temperature | leftTime, ovenSteamer, commonFaultDetection |
| `A3ZI` | 嘉格纳200 系列电磁灶80cm | childLockSwitch, heatGear, mode, status | heating, commonFaultDetection |
| `A3ZU` | 海尔小红花系列冰箱 | aiFfSwitch, aiVersatileCabin, iceMode, refrigerateSwitch | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A400` | 海尔冰箱BCD-548WGHTDC9FSU1 | aiFfSwitch, aiNutrientCabin, aiVersatileCabin, refrigerateSwitch | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A403` | 海尔云溪冰箱 | aiFfSwitch, aiNutrientCabin, aiVersatileCabin, refrigerateSwitch | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A404` | 海尔seeker冰箱 | aiFfSwitch, aiFpSwitch, intelligentSwitch, refrigerateSwitch | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A40I` | 卡萨帝两门冰箱 | aiEsSwitch, aiFpSwitch, freezeSwitch, refrigerateSwitch | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A40R` | TCL冰箱标准款 | childLockSwitch, freezeSwitch, refrigerateSwitch, refrigerationSwitch | freezerFloat, refrigeratorFloat |
| `A41H` | 老板蒸烤一体机C98A G2 | lightSwitch, status, switch, temperature | leftTime, ovenSteamer, commonFaultDetection |
| `A420` | 卡萨帝酒柜JC-260WGCHND7U1(DZ) | bottomShelftemp, humidity, middleShelftemp, temperature | commonFaultDetection |
| `A42F` | 海尔小红花十字门冰箱 | aiFfSwitch, aiNutrientCabin, aiVersatileCabin, refrigerateSwitch | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A42I` | 奥克斯空调家用挂机 | fan, mode, switch, temperature | commonFaultDetection, sleep, healthy, screen, eco, supportHeat |
| `A42J` | 奥克斯空调家用柜机 | fan, mode, switch, temperature | commonFaultDetection, supportHeat, sleep, screen, eco, healthy |
| `A44B` | 美的除湿机CF24BDN7DY | anionSwitch, humidity, mode, switch | delayOff, delayOn, commonFaultDetection |
| `A450` | 欧瑞博热水器 | faultDetection, status, switch, temperature | commonFaultDetection |
| `ZF0L` | 华为全屋智能 智能中控屏 MINI | panelMode, volSwitch, recoverConfigSwitch, micSwitch | roomsleeptime, undisturbMode, homeBroadcast |
| `ZF0O` | 华为全屋智能 智能中控屏 MINI | panelMode, volSwitch, recoverConfigSwitch, micSwitch | roomsleeptime, undisturbMode, homeBroadcast |
| `ZF0P` | 华为全屋智能 智能中控屏 MINI | panelMode, volSwitch, recoverConfigSwitch, micSwitch | roomsleeptime, undisturbMode, homeBroadcast |
| `ZG07` | 华为全屋智能射灯筒灯驱动器 | switch, brightness, cct, faultDetection | subProduct |
| `ZG0G` | 华为全屋智能射灯筒灯驱动器 - 12W | switch, brightness, cct, faultDetection | subProduct |
| `ZG0M` | 华为全屋智能射灯筒灯驱动器 - 9W | switch, brightness, cct, faultDetection | subProduct |
| `ZG0N` | 华为全屋智能射灯筒灯驱动器 - 12W | switch, brightness, cct, faultDetection | subProduct |
| `ZG1H` | 华为全屋智能射灯筒灯驱动器 - 9W | switch, brightness, cct, faultDetection | subProduct |
| `ZG1I` | 华为全屋智能射灯筒灯驱动器 - 12W | switch, brightness, cct, faultDetection | subProduct |
| `ZGA0` | 华为摄像机D2150-10-LI-SV | switch, shootSwitch, videoSwitch, alarmEvent | capability |
| `ZGA1` | 华为摄像机D3250-10-SIU | switch, shootSwitch, videoSwitch, alarmEvent | capability |
| `ZGA3` | 华为摄像机HS-CAM-201 | switch, shootSwitch, videoSwitch, alarmEvent | capability |
| `ZGA4` | 华为摄像机HS-CAM-301 | switch, shootSwitch, videoSwitch, alarmEvent | capability |
| `ZGA5` | 华为摄像机HS-CAM-302 | switch, shootSwitch, videoSwitch, alarmEvent | capability |
| `ZGA7` | 华为摄像机HS-CAM-601 | switch, shootSwitch, videoSwitch, alarmEvent | capability |
| `ZGB1` | 华为摄像机HS-CAM-202 | switch, shootSwitch, videoSwitch, alarmEvent | capability |
| `ZGB2` | 华为摄像机HS-CAM-203 | switch, shootSwitch, videoSwitch, alarmEvent | capability |
| `ZGB3` | 华为摄像机HS-CAM-205 | switch, shootSwitch, videoSwitch, alarmEvent | capability |
| `ZGB4` | 华为摄像机HS-CAM-303 | switch, shootSwitch, videoSwitch, alarmEvent | capability |
| `ZGB5` | 华为摄像机HS-CAM-305 | switch, shootSwitch, videoSwitch, alarmEvent | capability |
| `ZGE1` | 华为网络录像机HS-NVR-801 | switch, shootSwitch, videoSwitch, alarmEvent | capability |
| `0102` | 灯组 | switch, brightness, cct | — |
| `0106` | 灯组 | switch, brightness, cct | — |
| `100I` | 电烤箱（调试） | temperature, gear, faultDetection | oven, workFlow |
| `100Y` | 奥克斯柜机 | switch, temperature, faultDetection | airConditioner, wind, turbo |
| `100Z` | 奥克斯挂机 | switch, temperature, faultDetection | airConditioner, wind, turbo |
| `100q` | 老板油烟机 | switch, gear, connectStatus | kitchenVentilator, stoveSwitch |
| `1012` | 艾美特电风扇 | switch, fan, faultDetection | delay |
| `101O` | 720空气净化器KJ420F-EP420 | switch, temperature, faultDetection | airPurifying, pm2p5, wind, filterElement |
| `101P` | 720空气净化器KJ420F-EP350 | switch, temperature, faultDetection | airPurifying, pm2p5, wind, filterElement |
| `101S` | 欧普罗迪智能灯 | switch, brightness, lightMode | delay |
| `101x` | 美的智能空调 | switch, temperature, faultDetection | airConditioner, wind, turbo |
| `101z` | 美的风扇 | switch, fan, faultDetection | — |
| `1023` | 电烤箱 | upTemperature, downTemperature, faultDetection | oven, workFlow |
| `1026` | 美的空气净化器 | switch, temperature, faultDetection | airPurifying, pm2p5, wind |
| `103H` | 老板蒸汽炉 | switch, temperature, faultDetection | steamoven |
| `103I` | 720空气净化器KJ800F-EP800 | switch, temperature, faultDetection | airPurifying, pm2p5, wind, filterElement |
| `103U` | 欧普蓝牙射灯OPLYSD | switch, brightness, faultDetection | relativeDelay |
| `103U` | 欧普蓝牙射灯OPLYSD | switch, brightness, faultDetection | relativeDelay |
| `103Y` | 国投主控3路开关3LA | switch01, switch02, switch03 | — |
| `1041` |  | switch, temperature, faultDetection | airConditioner, wind |
| `104O` | 品多智能指纹门锁M1 | battery, discovery, faultDetection | smartLock, lockAlarm, account, event |
| `104T` | Wulian智尚三路开关 | switch01, switch02, switch03 | — |
| `1052` | 瑞晶空调RAC-2 | switch, temperature, faultDetection | airConditioner, wind |
| `1055` | 瑞晶筒灯RAL-2 | switch, cct, brightness | — |
| `105S` | YeeLight白灯 | switch, brightness, faultDetection | delay |
| `105W` | TPLink彩灯 | switch, mode, brightness | relativeDelay |
| `110Q` | 亚都加湿器SC175-S040Hi | switch, gear, light | Sound, timing |
| `110S` | 亚都加湿器SC175-SK040ProHi | switch, humidity, gear | timing, Sleep, sound, Anion |
| `113N` | Yeelight白光灯泡 | switch, lightMode, brightness | delay |
| `113O` | Yeelight色温灯泡 | switch, cct, brightness | delay |
| `113Q` | Yeelight护眼台灯 | switch, brightness, lightMode | delay |
| `113V` | Yeelight吸顶灯 | switch, lightMode, brightness | delay |
| `114O` | 奥普智能晾衣机D8 | action, status, lightSwitch | — |
| `115Q` | HDL地暖 | switch, temperature, mode | — |
| `121C` | 海令智能开关面板 | switch01, switch02, switch03 | — |
| `121D` | 海令智能开关面板 | switch01, switch02, switch03 | switch04 |
| `122C` | 人体红外4合1传感器 | luminance, humidity, workMode | motionSensor, Temperature |
| `122Y` | 三位免零线智能开关 | switch01, switch02, switch03 | switchLable01, switchLable02, switchLable03 |
| `123S` | SONOFF TX3C 智能墙壁开关 | switch1, switch2, switch3 | switchOn, switchOff, delay, powerLight, hideSwitch, startup1, startup2, startup3, pulseSwitch1, pulseLength1, pulseSwitch2, pulseLength2, pulseSwitch3, pulseLength3 |
| `124U` | 正泰智能插座 | switch, memorySwitch, faultDetection | power, consumption, timerInfo, delay |
| `131R` | 火鸡温感电磁炉 | status, mode, faultDetection | heatpower, recipe |
| `131Y` | 青稞智能锁_Q7 | lockState, lockMode, battery | prePowerSwitch, heartBeat, lastActionTime, lockAlarm, event, userList, keyList, publicKey, remoteCode, remoteResult, remoteCode, faultCode |
| `134V` | 凯迪仕智能门锁 | lockState, lockMode, battery | lastActionTime, lockAlarm, event, keyList, faultCode |
| `135K` | 红日吸油烟机JE7316i | switch, gear, mode | LEDLightSwitch, Delayshudown |
| `135V` | 流光开关三联 | switch01, switch02, switch03 | lightMode01, lightMode02, lightMode03, colour01, colour02, colour03, backlight01, backlight02, backlight03, memoryState |
| `137E` | 弩牌智能无叶风扇 | switch, mode, onOffBeep | speedPercent, autoOff |
| `140K` | 控客三路灯光面板 | switch01, switch02, switch03 | — |
| `143X` | MINI颈部按摩仪 | commonMode1, stop, heat | lowerElec, charge, fault, voice, strength, power |
| `146C` | 公牛智能插座-GN-Y201H | switch, memorySwitch, backlight | delay |
| `148M` | 正泰快充智能插排 | switch, memorySwitch, faultDetection | power, consumption, delay |
| `151H` | 欧普延系列蓝牙控制盒 | switch, brightness, cct | — |
| `157Z` | 威廷智能三开Wi-Fi | switch1, switch2, switch3 | — |
| `162X` | 卡赫智能净水器WPD60-P | status, childLockSwitch, faultDetection | inputTds, outputTds, filterElement1, filterElement2, filterElement3, TotalWater, VolumPerCup, Temp |
| `164B` | 智能三开开关 | switch1, switch2, switch3 | — |
| `164M` | 平头熊三键开关WIFI | switch1, switch2, switch3 | — |
| `174F` | 安吉尔净水器 | switch, status, faultDetection | filterElement1, filterElement2, filterElement3, Outputquality, Inputquality, Outputtemperature, Waterquantity, Flush |
| `178Z` | 奥普浴霸QDP2826AHW | mode, lightSwitch, swingSwitch | leftTime, NightLight |
| `181T` | 碧云泉家用净水机U35 | status, temperature, faultDetection | purifyWater, filterElement1, filterElement2, attemperation, QuantifyWater |
| `181U` | 碧云泉家用净水器R302D | status, temperature, faultDetection | inputTds, outputTds, purifyWater, filterElement1, filterElement2, filterElement3, attemperation, QuantifyWater |
| `183E` | 噼啪智能三开开关 | switch1, switch2, switch3 | — |
| `186X` | 欧派煤气灶 | status, heatGear, faultDetection | autoTurnOff |
| `2014` | 麦乐克门窗传感器 | doorEvent, status, battery | TamperAlarm |
| `201E` | 麦乐克温湿度传感器 | temperature, humidity, battery | — |
| `203O` | 白色零火线三路灯控面板超薄 | switch01, switch02, switch03 | — |
| `204J` | 倍觅智能驱蚊器 | switch, mode, workStatus | circular, batteryindicator, moodLight, time |
| `204O` | 蓓慈BA502V1护眼仪 | switch, mode, volume | airPressureOnOff, lefttime, workstatus, tempSwtich, musicSwtich, vibratingOnOff |
| `2053` | 百斯腾温润速热暖风机 | switch, gear, childLockSwitch | delay |
| `205O` | VOC智能门锁 | lockState, lockMode, battery | lastActionTime, lockAlarm, event, keyList, publicKey, remoteCode, remoteResult, remoteCode, faultCode |
| `205Q` | 四季沐歌M-HY900Z-GG智能晾衣机 | action, status, lightSwitch | — |
| `2074` | 威仕达天玑星 | mode, opener, operation | — |
| `207A` | 博乐宝净饮机B16 | status, childLockSwitch, faultDetection | filterElement1, rinseMode1, outletWater, watertypestate, capmodestate |
| `207N` | 领普单键零火开关MESH | switch, mode1, brightness | button1 |
| `208Y` | 酷轻松石墨烯发热暖脚宝 | switch, heat, temperature | timerlabel, workstatue |
| `20BQ` | 天智星 | mode, opener, operation | — |
| `20DG` | 永林双色调光器 | switch, cct, brightness | — |
| `20ED` | 艾优智能电动牙刷-宝可梦 | status, battery, mode | brushingHistory, custom, time, Brushingmode |
| `20F6` | 智能温感变频静音风扇 | switch, mode, fan | OSC, Light |
| `20FI` | 海令冷暖调光器 | switch, cct, brightness | — |
| `20FS` | 华为智选 火火兔智能早教故事机 | switch, musicPlay, volume | earLight, faceLight |
| `20GM` | 艾美特空气循环扇FA23-AD17 | switch, mode, fan | timing |
| `20J0` | 云腾 | headControl, legControl, commonMemoryControl1 | commonMemoryControl2, commonMemoryControl3, commonMemoryControl4, commonMemoryControl5, commonMemoryControl6, commonMemoryControl7, commonMemoryControl8, MemoryKeyTips, RightMode, LeftMode, ChildLock |
| `20JS` | 霍夫曼开合帘 | mode, opener, opener | — |
| `20KL` | 麒盛科技智能床 | headControl, legControl, lieControl | FootMassage, HeadMassage, AngleMode, MassageMode, ubb |
| `20MH` | 八键场景面板尊享版 | switch1, switch2, backlightMode | — |
| `20NY` | 亚摩斯风扇AS-FS12D | switch, mode, fan | timing, snaking |
| `20P8` | 奥普浴霸炫彩 | mode, lightSwitch, swingSwitch | leftTime, NightLight |
| `20PV` | 锐点智能盒 | switch, brightness, cct | — |
| `20QK` | 摩根调色温灯 | switch, brightness, cct | — |
| `20QV` | 四键场景面板时尚版 | switch1, switch2, backlightMode | — |
| `20QW` | 四键场景面板尊享版 | switch1, switch2, backlightMode | — |
| `20R1` | 四键场景面板尊享版 | switch1, switch2, backlightMode | — |
| `20R3` | 四键场景面板尊享版 | switch1, switch2, backlightMode | — |
| `20R4` | 四键场景面板尊享版 | switch1, switch2, backlightMode | — |
| `20R7` | 六键场景面板尊享版 | switch1, switch2, backlightMode | — |
| `20R9` | 六键场景面板尊享版 | switch1, switch2, backlightMode | — |
| `20RE` | 六键场景面板尊享版 | switch1, switch2, backlightMode | — |
| `20RH` | 八键场景面板时尚版 | switch1, switch2, backlightMode | — |
| `20RJ` | 八键场景面板尊享版 | switch1, switch2, backlightMode | — |
| `20RM` | 八键场景面板时尚版 | switch1, switch2, backlightMode | — |
| `20RT` | 八键场景面板时尚版 | switch1, switch2, backlightMode | — |
| `20RX` | 八键场景面板尊享版 | switch1, switch2, backlightMode | — |
| `20S0` | 八键场景面板时尚版 | switch1, switch2, backlightMode | — |
| `20S1` | 八键场景面板尊享版 | switch1, switch2, backlightMode | — |
| `20S4` | 艾优智能剃须刀 | commonMemorySwitch1, mode, speed | Reset, prompt, Cleaningcutting, Cuttinghead, smartmode, time, nowbetty |
| `20S9` | 八键场景面板尊享版 | switch1, switch2, backlightMode | — |
| `20SC` | 八键场景面板尊享版 | switch1, switch2, backlightMode | — |
| `20SD` | 八键场景面板尊享版 | switch1, switch2, backlightMode | — |
| `20TG` | 欧派净水器 | status, faultDetection, commonTask1 | outputTds, filterElement1, filterElement2 |
| `20TK` | 易百珑单路开关 | switch, memorySwitch, switch1 | CleanPair, Pair |
| `20U3` | GPWELL胶囊咖啡机 | switch, temp, reset | currentOutlet, commonFaultDetection, status2, Star, cupChoose, cupVolume |
| `20UC` | 领普双键墙壁开关 | switch, switch1, switch2 | led |
| `20X9` | 脊安适按摩器G6 | switch, connectStatus, mode | batteryLevel, heatLevel, remainTime, massageTime, strength |
| `20XW` | 控客-星空三路灯控面板 | switch1, switch2, switch3 | — |
| `20YD` | 控客-环境传感器 | temperature, humidity, battery | illumination |
| `20YS` | 控客-声光报警器 | switch, volume, battery | — |
| `20ZG` | 青稞智能锁_N5H | lockState, lockMode, battery | prePowerSwitch, heartBeat, lastActionTime, lockAlarm, event, userList, keyList, publicKey, remoteCode, remoteResult, remoteCode, faultCode |
| `211L` | 壹指盾Q6H指静脉智能锁 | lockState, lockMode, battery | heartbeatTime, lastActionTime, lockAlarm, event, userList, publicKey, remoteCode, remoteResult, remoteInfo |
| `213X` | 西顿调色模块 | switch, cct, brightness | — |
| `214V` | 智汇云二位轻触开关面板 | switch, switch1, switch2 | delay |
| `2157` | 九赞猫咪智能保温杯 | battery, temperature, connectStatus | alarmTime1 |
| `215E` | 西顿恒压调色模块 | switch, cct, brightness | — |
| `215M` | 触控双开零火开关 | switch, switch1, switch2 | — |
| `215S` | 智能门窗磁 | doorEvent, status, battery | — |
| `216U` | HEIMAN智能烟雾报警器 | alarm, battery, selfCheck | — |
| `2173` | 小嘀全自动智能锁Q3H | lockState, lockMode, battery | lastActionTime, lockAlarm, event, keyList, faultCode |
| `217L` | 开关智能控制器2型 | switch, switch1, switch2 | — |
| `217R` | 控客-肖邦三路灯光面板 | switch01, switch02, switch03 | — |
| `2182` |  | doorEvent, status, battery | — |
| `21A8` | HEIMAN智能一氧化碳报警器 | alarm, battery, selfCheck | — |
| `21B6` | 圆和二路智能开关 | switch, switch1, switch2 | — |
| `21CE` | 亚摩斯果蔬净化机AS-FV09D | switch, status, mode | remainTime |
| `21DF` | 云起奇点开关模块PRO二联 | switch, switch01, switch02 | memoryState |
| `21DH` |  | doorEvent, status, battery | — |
| `21EQ` |  | switch, mode, fan | filterElement |
| `21F9` | 艾优智能电动牙刷 | status, battery, mode | Brushingmode, custom, time, brushingHistory |
| `21FD` | 艾优智能电动牙刷-故宫 | status, battery, mode | Brushingmode, custom, time, brushingHistory |
| `21G6` | 超广角自然风风扇 | switch, mode, fan | endTime |
| `21GM` | JW智能开关3键型 | switch1, switch2, switch3 | — |
| `21LA` | 永林恒压色温驱动 | switch, cct, brightness | — |
| `21LH` | 米立3路智能开关面板 | switch1, switch2, switch3 | — |
| `21M7` | 德姆勒智能电风扇 | switch, mode, fan | Angle, BackLight, end |
| `21OU` | 公牛WiFi智能插座基础V3版 | switch, memorySwitch, backlight | delay |
| `21RL` | 华为智选 德施曼智能门锁 | lockState, lockMode, battery | lockDefense, enableState, upgradeMode, heartbeatTime, lastActionTime, lockAlarm, event, keyList, keyOperate, publicKey, remoteCode, remoteResult, remoteInfo, remoteEnable, faultCode |
| `21RM` | 华为智选 德施曼智能门锁Pro | lockState, lockMode, battery | lockDefense, enableState, upgradeMode, heartbeatTime, lastActionTime, lockAlarm, event, keyList, keyOperate, publicKey, remoteCode, remoteResult, remoteInfo, remoteEnable, faultCode |
| `21SE` | 调色温灯带（灯带调光器） | switch, brightness, cct | — |
| `21TW` | 鸿蒙智选 达伦智能台灯2 | switch, brightness, lightMode | nightSwitch, studyMode, studyResult, delay |
| `21V7` | 瑞晶湿度控制器 | switch, humidity, gear | — |
| `21V9` | 瑞晶冷热源一体机 | switch, mode, temperature | — |
| `21VA` | 瑞晶壁挂炉 | switch, temperature, mode | — |
| `21VV` | 雷士护眼台灯-银河 | switch, brightness, rest | delay, Auto, Autodimming, RestTime, nlight |
| `21W3` | 瑞晶色温灯 | switch, brightness, cct | — |
| `21WG` | 雷士护眼台灯-云光 | switch, brightness, commonMode1 | delay |
| `21XN` | 瑞晶门窗感应器 | doorEvent, status, battery | — |
| `21YH` | 瑞晶智能门锁 | doorState, alarm, doorEvent | — |
| `21ZU` | 蓓慈BA502E1护眼仪 | switch, volume, mode | vibratingOnOff, tempSwtich, musicSwtich, airPressureOnOff, lefttime, workstatus |
| `221U` |  | switch, switch1, switch2 | — |
| `221Z` |  | doorEvent, battery, alarm | keyList |
| `2220` |  | doorEvent, battery, alarm | keyList |
| `224A` |  | switch, brightness, cct | — |
| `224D` |  | switch, brightness, cct | — |
| `224J` | 觅石智能加湿器 | switch, humidity, childLockSwitch | delay, DDJY, DWTJ, QSTS |
| `224M` |  | temperature, humidity, pm25 | pm10 |
| `224Q` |  | switch, fan, pm25 | — |
| `227R` | 亚摩斯睿雅单火开关双键 | switch, switch1, switch2 | — |
| `22C1` | 同屏器 | switch, action, volume | overscan, player, hdmiMode |
| `22C5` | 本博按摩枕 | switch, hot, mode | countdown, speedRegulation, timeLeft |
| `22DT` | 捷昌智能橱柜 | status, commonMemoryControl1, ctrl | commonFaultDetection, currentheight |
| `22E2` | 八键场景面板时尚版 | switch1, switch2, backlightMode | — |
| `22E3` | 八键场景面板尊享版 | switch1, switch2, backlightMode | — |
| `22ER` | 吸顶式温湿度传感器 | switch, temperature, humidity | tempReportSetting, humidityReportSetting |
| `22HQ` | 美森智能声波牙刷 | battery, mode, gear | setWorkTime, filterElement, brushingHistory, F003, F002, F001 |
| `22II` | 格林盈璐无雾加湿器 | switch, speed, status | FilterLife, HumidityS, Level, Time, KeepHumi |
| `23FM` | 亚摩斯智能推窗器 | action, opener, reverse | level |
| `23QV` | ACEMATIC地暖模块 | switch, mode, temperature | — |
| `23SW` | 波可龙高速电吹风 | status, mode, connectStatus | recommend, question, guid, windSpeed |
| `23VV` | VOC智能保管箱 | lockState, lockStatus, battery | heartbeatTime, lastActionTime, lockAlarm, event, keyList, publicKey, remoteCode, remoteResult, remoteInfo, faultCode |
| `23WL` | 亚摩斯极境开关双键 | switch, switch1, switch2 | — |
| `242T` | 格林盈璐无雾加湿器 | switch, status, speed | KeepHumi, Time, Level, HumidityS, FilterLife |
| `2458` | 欧浦立智能门锁 | lockState, battery, alarm | event |
| `248F` | 石将军智能门锁 | lockState, battery, alarm | event |
| `2491` | 当贝投影X3 | switch, controlKey, volume | — |
| `2493` | 当贝投影X3Pro | switch, controlKey, volume | — |
| `249F` | 格里维尔高端智能门锁 | lockState, battery, alarm | event |
| `24AE` | 波可龙智能加湿器 | switch, humidity, childLockSwitch | QSTS, DWTJ, DDJY |
| `24B3` | 卷发器-罗曼智能小芭蕾 | switch, battery, workStatus | commonFaultDetection, rollDegree, workTime |
| `24EN` | 华督小型即热饮水机 | status, childLockSwitch, faultDetection | currentOutlet, WaterVolume, Temp, ONOFF |
| `24GR` | 吉米康智能眼部按摩仪 | switch, status, gear | commonFaultDetection, Electricity, Voice, SoothingMode, VitalityMode, SleepMode, SyntaxicMode |
| `24HE` | Evoyo三路开关小模块 | switch1, switch2, switch3 | — |
| `24HS` | 坚果投影仪J10S | switch, setting, home | input, focusing1, focusing2, up, menubutton, turndown, down, left, OK, turnup, right, back |
| `24HT` | 坚果投影仪G9S | switch, setting, home | turndown, focusing1, right, input, OK, back, focusing2, up, left, down, menubutton, turnup |
| `24M5` | 捷昌智能中岛电机 | ctrl, commonMemoryControl1, status | commonFaultDetection, currentheight |
| `24PV` | 亦生堂臂式电子血压计 | switch, commonMemorySwitch1, status | pressure, pulse, lowPressure, highPressure, privacyStatement, measure, statistics, electricValue, historyData |
| `24S5` | 得小烯 烯时代 石墨烯发热无线按摩眼罩 GSee2 | status, massage, heat | Remainingtime, UsageRecord, Realtimetemperature, electric, Heatingswitch, Massageswitch |
| `24S7` | 得小烯 烯时代 石墨烯发热无线按摩眼罩 GSee3 | status, massage, heat | UsageRecord, Realtimetemperature, Remainingtime, electric, Heatingswitch, Massageswitch |
| `24S9` | 得小烯 烯时代 石墨烯发热无线按摩护颈 GNeck2 | status, massage, heat | UsageRecord, Realtimetemperature, Remainingtime, electric, Heatingswitch, Massageswitch |
| `24SB` | 得小烯 烯时代 石墨烯发热无线按摩护颈 GNeck3 | status, massage, heat | UsageRecord, Realtimetemperature, Remainingtime, electric, Heatingswitch, Massageswitch |
| `253V` | 康风车载/便携空气净化器 | switch, lightswitch, windspeed | filterElement |
| `25OS` | 探梦者智能电动滑板车 L1 MAX | switch, lightMode, speed | firmwareUpgrade, lowPower, speedControl, color, speedUnit, VehicleSelfCheck, Unlocked, StepLight, RestoringFactory, Electricity, Headlight, startupSetting, WorkStatus, cruise, totalMileage, Locked, TheMileage |
| `25P4` | 北通智能游戏手柄 | commonMemorySwitch1, light, sensitivity | iOSReporting, calibrating, Turbo, userDefinedButtons, quantity, keymap, vibration |
| `25PZ` | 探梦者智能电动滑板车 L1 PRO | switch, lightMode, speed | RestoringFactory, VehicleSelfCheck, speedUnit, speedControl, cruise, startupSetting, color, StepLight, Headlight, totalMileage, TheMileage, Electricity, Locked, Unlocked, WorkStatus |
| `25UP` | 青稞智能锁N5C | lockState, lockMode, battery | prePowerSwitch, heartBeat, lastActionTime, lockAlarm, event, userList, keyList, publicKey, remoteCode, remoteResult, remoteInfo, faultCode |
| `2625` | 纯麦家庭KTV混音器 | Volume, reverb, AudioMode | Mic2Volume, Mic1Volume, InputMode |
| `26LT` | 卡唛电子指纹智能保管箱 | battery, openMode, doorStatus | SetTime, chipid, PW, FP, historyrecord |
| `26S6` | 金卡智能燃气报警器 | sensitivity, mute, status | commonFault, Valveswitch, test, meterconnect, Gasvalue, testresult |
| `26TX` | 酷轻松石墨烯发热护膝 | switch, heat, temperature | Remind, Message, Mode, time, timerlabel, workstatus |
| `26VH` | 创维智能足浴盆 | switch, action, temperature | setWorkTime, leftTime, WorkingCondition |
| `27QM` | 红外幕帘传感器 | switch, alarm, faultDetection | alarmReportSetting |
| `27W6` | 吸顶式红外人体移动光照传感器 | switch, status, luminance | — |
| `27WB` | 超静音窗帘电机 SE | action, opener, faultDetection | dryContactSetting |
| `27ZQ` | 食具消毒柜 | switch, cabinetMode, cabinetStatus | Lefttime, Worktime, Auto |
| `283L` | 品多智能锁H2 | lockState, lockMode, battery | erroralarm, prvdooralarm, upgradeMode, publicKey, remoteCode, remoteResult, remoteInfo, keyList, lockAlarm, event |
| `283O` | UBOT温湿度计Mini | temperature, humidity, battery | timeHumidity, timeTemperature, time, lowestHumidity, highesHumidity, lowestTemperature, highesTemperature, temperatureUnit |
| `2881` | 嘟比恒温暖奶器 | status, mode, targetTemperature | CurrentTemperature, DisinfectionTime, MainSwitch, pattern, MakeAnAppointment, Exceptionprompt, Nightight |
| `28BF` | 无线续航自然风风扇 | switch, mode, fan | endTime |
| `28IO` | 予智生活智能冲牙器 | battery, mode, workGuidance | applicatorTime, cleaningRecord, commonFaultDetection, batteryAvailable, deviceLock, instructions, devicestate, moreSettings, CVTStrengthDef, pulseStrengthDef, verycoolStrengthDef, softStrengthDef |
| `28QS` | 博思迪洁面仪 | switch, status, mode | Lowbatterywarning, firmwareupdate, Reversesetting, state |
| `28SX` | 小K士智能猫眼门锁 | lockState, lockMode, battery | lockAlarm, event, keyList, publicKey, remoteCode, remoteResult, remoteInfo, remoteInfo, code1, code2, code3, code4, code5, upgradeMode, imagePack0, imagePack1, imagePack2, imagePack3, imagePack4, imagePack5 |
| `28T5` | 小K士智能门锁 | lockState, lockMode, battery | lockAlarm, event, keyList, publicKey, remoteCode, remoteResult, remoteInfo, remoteInfo, code1, code2, code3, code4, upgradeMode |
| `28UT` | 精臣标签打印机D110 | switch, printerStatus, faultDetection | printParameter, connection, PrintableCounts, PrintedCounts, instructions, mall, rfid, textfield, preview, alignment, copies, offset, effect, print |
| `28Z2` | 联邦米尼智能按摩单椅 | switch, angleControl, faultDetection | Airbagmassage, HeatingMode, Home, Seatposition, monitorednobody, messagetimecountdown |
| `295D` | 奥佳华按摩椅OG7306Pro | switch, action, autoMode | type, Faultcode, legadjustment, backadjustment, footroller, heating, times, Zerogravity, vibration, customize |
| `298K` | 联邦米尼智能温灸单椅 | switch, angleControl, faultDetection | BackDown, BackUp, HeatingMode, Home, Seatabnormal, monitorednobody |
| `299C` | VOC猫眼可视门锁 | lockState, lockMode, battery | lockAlarm, event, keyList, publicKey, remoteCode, remoteResult, remoteInfo, remoteInfo, code1, code2, code3, code4, code5, upgradeMode, imagePack0, imagePack1, imagePack2, imagePack3, imagePack4, imagePack5 |
| `299N` | 澳柯玛智能燃气热水器16H101 | switch, temperature, faultDetection | TeasonThermal, booster, promotion, flame, draughtfan, flow, antifreezing, wateryield, airflow, Zerocoldwater, waterpump, code |
| `29E9` | 海德 FG309HW 热敷筋膜枪 | speed, switch, heat | mytimer, gearL, running, electricity |
| `29IB` | 安吉尔 A8 Pro | switch, status, faultDetection | inputTds, outputTds, filterElement1, filterElement2, filterElement3, totalPurifyWater |
| `29SC` | 行走助力机器人 | mode, switch, volume | ota, report, remainBattery, walkSteps, SaveOrRecovery, force |
| `29YN` | VOC猫眼可视门锁T6i | lockState, lockMode, battery | keyList, remoteResult, publicKey, lockAlarm, userlist, event, errorCode, remoteInfo, remoteCode, upgradeMode |
| `29YQ` | 24W双色温恒流控制装置 | switch, brightness, cct | — |
| `2A1E` | 掌航智能门锁 | lockState, battery, alarm | event |
| `2A22` | eue魔力贴四驱版 | switch, status, model | time, strength, part |
| `2A26` | eue头部按摩器 | switch, battery, mode | strength |
| `2A8Q` | sraum3路开关面板 | switch1, switch2, switch3 | scene4, scene3, scene2, scene1 |
| `2A8U` | 三星SHP-P60 | doorState, lockMode, alarm | event, faultCode |
| `2AAL` | 艾特三键开关 | switch1, switch2, switch3 | — |
| `2AB2` | 青稞智能锁_A7H | lockState, lockMode, battery | prePowerSwitch, heartBeat, lastActionTime, lockAlarm, event, userList, keyList, publicKey, remoteCode, remoteResult, remoteCode, faultCode |
| `2ABM` | 酷轻松石墨烯腿部按摩器 | switch, temperature, heat | reminder, workstate, timelabel, pat, timer4DeviceOff |
| `2ABU` | 永林色温驱动 | switch, cct, brightness | — |
| `2ACA` | 酷轻松石墨烯真丝围脖 | switch, heat, temperature | timerlabel, workstate |
| `2ACV` | 开合帘 | mode, opener, opener | — |
| `2AD0` | 西顿24W调色模块 | switch, cct, brightness | — |
| `2ADG` | 酷轻松智能热敷包 | switch, heat, temperature | timelabel, workstatue |
| `2AM5` | LUFTRUM多功能循环扇 | switch, fan, commonMemorySwitch1 | filterElement1, commonFaultDetection, countdown, Shake, workmode |
| `2AN7` | 鸿雁DLT调光开关U2 | switch, cct, brightness | — |
| `2AP0` | 鸿雁双键智能开关U2 | switch1, switch2, indicator | — |
| `2AR1` | 调色温灯（照明调光器） | switch, brightness, cct | — |
| `2AVX` | 三思青春版台灯 | switch, brightness, colourMode | tomatoClk, delay |
| `2B2H` | 晾品智能晾衣机HW70 | action, status, lightSwitch | — |
| `2B31` | 左点智能足蒸器Z8 | switch, action, volume | — |
| `2B5A` | MixSwitch超级智能开关-三开 | switch1, switch2, switch3 | — |
| `2BB1` | 凯迪仕智能锁HK300 main | lockState, lockMode, battery | lastActionTime, lockAlarm, event, keyList, publicKey, remoteCode, remoteResult, remoteCode, faultCode |
| `2BDI` | 吸顶式毫米波人体存在光照传感器 | switch, status, luminance | — |
| `2BDX` | OOYEE高速无叶吹风机 | commonMemorySwitch1, temperature, windspeed | — |
| `2BDZ` | 吸顶式PM2.5三合一传感器 | switch, temperature, humidity | PM2.5, PM10 |
| `2BE8` | 麦乐克无线温湿度传感器 | temperature, humidity, battery | — |
| `2BFK` | FSL智感小夜灯 | status, battery, brightness | motionDetected, online, Lm, NightLightMode, time, Light |
| `2BGD` | 欧普智能射灯 | switch, brightness, commonMemorySwitch1 | — |
| `2BGL` | 三雄极光Pak智能射灯 | switch, brightness, lightMode | — |
| `2BOF` | 堡丽调色温灯（照明调光器） | switch, brightness, cct | — |
| `2BOI` |  | switch, brightness, cct | — |
| `2BOK` | 堡丽调色温灯带（灯带调光器） | switch, brightness, cct | — |
| `2BOT` |  | switch, fan, pm25 | — |
| `2BP9` | 德施曼人脸识别智能锁RH700 | lockState, lockMode, battery | lastActionTime, lockAlarm, event, keyList, publicKey, remoteCode, remoteResult, remoteCode, remoteEnable, faultCode |
| `2BRC` | 瑞莱克斯按摩椅 | switch, autoMode, manuMode | commonFaultDetection, Width, ROLLERS, Intensity, FOOTREST, SHOULDER, ARMS, AirBag, Speed, Intervalselection, Heat, PositionAdjustment, ZeroG |
| `2BVY` | 阳光照明插电感应夜灯 | status, switch, lightmode | motionDetected |
| `2BX8` | 飞利浦智能锁DDL603E | lockState, lockMode, battery | lastActionTime, lockAlarm, event, keyList, publicKey, remoteCode, remoteResult, remoteCode, faultCode |
| `2BXX` | 叶绿体自发电无线门铃WiFi版 | volume, commonExecution1, commonExecution2 | ringList, curRingId, ringObj |
| `2C5J` | 凯迪仕晾衣机 | action, status, lightSwitch | — |
| `2C5N` | 堡丽开合帘 | mode, opener, opener | — |
| `2C65` | 左点智能膝部按摩器 | switch, hot, massage | lowbattery, shake |
| `2C7W` | 西蒙三位智能开关 | switch1, switch2, switch3 | BackLightMode |
| `2C86` | 西蒙地暖温控器 | switch, temperature, faultDetection | ValveState, LowTemperatureProtect, BackLightLevel, SceneMode |
| `2CK1` | 叶绿体单火三路墙壁开关 | switch1, switch2, switch3 | — |
| `2CMV` | 坚果G9 | switch, home, setting | turndown, turnup, menubutton, focusing1, focusing2, back, OK, up, down, left, right, input |
| `2COX` | 坚果投影仪J10 | switch, setting, home | turndown, turnup, up, down, focusing2, menubutton, left, right, back, input, OK, focusing1 |
| `2CP3` | 小智智能锁K8 | lockState, battery, alarm | event, lastActionTime |
| `2CP9` | 仁豪家居电动巴士门 | oneKeyReset, massageMode, brightness | midJoinOpen, midRightOpen, midLeftOpen, sideJoinOpen, sideRightOpen, sideLeftOpen, openDirection, openTimes, autoClosed, doorstatus |
| `2CPZ` | 超静音开合帘电机尊享版 | action, opener, faultDetection | — |
| `2CQ0` | 标准开合帘电机时尚版 | action, opener, faultDetection | — |
| `2CTI` | 仁豪家居功能床 | modeSelect, angleControl, childlock | Emergencystop |
| `2CTK` | VOC智能门锁X20 | lockState, lockMode, battery | lastActionTime, lockAlarm, event, keyList, publicKey, remoteCode, remoteResult, remoteCode, faultCode |
| `2CTL` | VOC智能门锁X11 | lockState, lockMode, battery | lastActionTime, lockAlarm, event, keyList, publicKey, remoteCode, remoteResult, remoteCode, faultCode |
| `2CTN` | 艾优智能电动牙刷 | status, battery, mode | brushingHistory, time, custom, Brushingmode |
| `2CUQ` | 麦乐克无线烟感传感器 | alarm, battery, temperAlarm | commonFaultDetection |
| `2CV3` | 四键场景面板时尚版 | switch1, switch2, backlightMode | — |
| `2CV5` | 六键场景面板时尚版 | switch1, switch2, backlightMode | — |
| `2CV7` | 四键场景面板尊享版 | switch1, switch2, backlightMode | — |
| `2CV9` | 六键场景面板尊享版 | switch1, switch2, backlightMode | — |
| `2CVB` | 八键场景面板尊享版 | switch1, switch2, backlightMode | — |
| `2CVI` | 三键智能开关面板时尚版 | switch1, switch2, switch3 | — |
| `2CVS` | 凯胜头部按摩器 | switch, shock, temperature | Airpressure, Music, DIYmode, Profitablemodel, sleepmode, Vitalitymode, Comfortmode, Currentbattery, remainingtime |
| `2CVT` | 领普窗帘电机 | action, opener, reverse | calibration |
| `2CYN` | 华为智选 VOC智能门锁S | lockState, lockMode, battery | lastActionTime, lockAlarm, event, keyOperate, keyList, publicKey, remoteCode, remoteResult, remoteInfo, faultCode |
| `2CYR` | SID超人智能门锁 | lockState, lockStatus, alarm | event, faultCode |
| `2D50` | Mynt智能香薰机 | switch, lightSwitch, colour | autochange, atomization |
| `2D82` | 卡赫智能净水器800G | switch, status, faultDetection | inputTds, outputTds, filterElement1, filterElement2, filterElement3, purifyWater, contWater |
| `2DA4` | VOC智能门锁X6 | lockState, lockMode, battery | lastActionTime, lockAlarm, event, keyList, publicKey, remoteCode, remoteResult, remoteCode, faultCode |
| `2DC9` | HEIMAN智能人体移动传感器 | status, battery, temperAlarm | motionDetected |
| `2DDT` | 李文智能锁 LW-701 | lockState, battery, alarm | event, lastActionTime |
| `2DEN` | 李文智能锁 LW-703 | lockState, battery, alarm | event, lastActionTime |
| `2DES` | 9W单色温射灯调光驱动器 | switch, brightness, faultDetection | — |
| `2DF5` | 艾诗摩尔儿童全自动口腔清洁器 | status, battery, sterilize | toothbrush, night, morning |
| `2DFV` | 无线地面清洗机 | status, battery, water | workTime |
| `2DGK` | 推窗机 | action, opener, faultDetection | — |
| `2DMA` | 一路智能开关 | switch, switch1, backlight | — |
| `2DMK` | 力博得智能声波牙刷 悦沁 | battery, status, mode | brushingHistory, audioSwitch, weekHistorys, setTmie, brushSettings, modes, brushingHistorys, brushStart, postHistorys, guide |
| `2DNR` | 酷轻松颈部固定器 | switch, temperature, heat | workstatue, timerlabel |
| `2DNS` | 酷轻松石墨烯热敷眼罩 | switch, heat, temperature | timerlabel, workstatue |
| `2DO9` | 酷轻松石墨烯发热真丝眼罩 | switch, temperature, heat | workstatue, timerlabel |
| `2DOB` | 酷轻松石墨烯发热真丝肩颈宝 | switch, workStatus, temperature | countdown, setGear, setTimer |
| `2DOC` | 酷轻松石墨烯发热真丝颈带 | switch, workStatus, temperature | countdown, setGear, setTimer |
| `2DPA` | 酷轻松石墨烯发热休闲马甲 | switch, heat, temperature | timerlabel, workstatue |
| `2DSE` | 拉孚二路智能开关 | switch, switch1, switch2 | — |
| `2DV1` | 三键智能开关面板尊享版 | switch1, switch2, switch3 | — |
| `2DVN` | 小益智能门锁 | lockState, battery, alarm | event, faultCode, setVolume |
| `2DXB` | 龙泉智家二路墙壁开关 | switch, switch1, switch2 | — |
| `2DYZ` | 美森剃须理容套装 | switch, commonExecution1, commonTask1 | commonFilterElement1, F006, F005, f010, f007, f001 |
| `2DZ1` | 美森电动手刮刀 | switch, commonMode1, commonExecution1 | F003, F001, f008 |
| `2E0P` | 攀高智能腰腹部按摩仪 | switch, battery, gear | State, Time, HEAT, MODE |
| `2E4R` | 多功能按摩椅 | switch, mode, speed | UpDown, Zero, foot, Heating, Pressurepattern, Strength, Intensity, remainingTime, massageDuration |
| `2EJ8` | 罗曼智能电动冲牙器-HS10 | workStatus, initPosition, mode | commonFaultDetection, realTimeGuide, moreSet, workTime, strength, betteryleft |
| `2EJA` | 罗曼智能电动冲牙器-HS8 | workStatus, initPosition, mode | commonFaultDetection, moreSet, realTimeGuide, batteryLeft, workTime, strength |
| `2ELE` | Kandao Meeting Pro 360视频会议机 | switch, videoSwitch, volume | id, videoMode, micStatus |
| `2EMN` | 多功能按摩椅 | switch, speed, mode | Heating, foot, Zero, Strength, Intensity, UpDown, Pressurepattern, massageDuration, remainingTime |
| `2ENG` | 亚摩斯星耀开关双键 | switch, switch1, switch2 | — |
| `2EWQ` | MINE 灵动日光镜 | model, colour, brightness | gradualChange, breath, autoInduction, ElectricQuantity, WorkStatus, on |
| `2EYM` | 酷轻松多功能羽绒毯 | switch, heat, temperature | timerlabel, workstatue |
| `2EZQ` | VOC全自动门锁 | lockState, lockMode, battery | enableState, lastActionTime, lockAlarm, event, keyOperate, keyList, publicKey, remoteCode, remoteResult, remoteInfo, faultCode |
| `2EZS` | VOC全自动门锁T10 | lockState, lockMode, battery | heartbeatTime, lastActionTime, lockAlarm, event, keyList, publicKey, remoteCode, remoteResult, remoteInfo, faultCode |
| `2EZT` | VOC全自动人脸门锁 | lockState, lockMode, battery | enableState, lastActionTime, lockAlarm, event, keyOperate, keyList, publicKey, remoteCode, remoteResult, remoteInfo, faultCode |
| `2F2A` | VOC全自动门锁T10 Face | lockState, lockMode, battery | heartbeatTime, lastActionTime, lockAlarm, event, keyList, publicKey, remoteCode, remoteResult, remoteInfo, faultCode |
| `2F2I` | 拜尔智能电动牙刷 | battery, mode, spraySwitch | setWorkTime, filterElement, brushingHistory, F002, F001 |
| `2F5F` | 四键场景面板尊享版 | switch1, switch2, backlightMode | — |
| `2F5G` | 四键场景面板时尚版 | switch1, switch2, backlightMode | — |
| `2F5U` | 亚摩斯智能循环扇 | switch, mode, fan | anion, timingOff, timingOn |
| `2F7F` | 品仕乐立式吹风机B1DHW | switch, hairDrierStatus, hairDrierMode | Servicesupport, Windtemperature, FanSpeed |
| `2FAN` | HIFI智能音乐盒 | enableStatus, volume, Switch | sigInterface, channel, noiseReduction, SoundFieldAdjustment, SXS, EQNumber, MixVolume |
| `2FBR` | 茶吧机 | status, childLockSwitch, faultDetection | KettleTemp, Insulationswitch, Waterintakeswitch, soakingtime, Heatingswitch, thermoregulation, Waterintaketime |
| `2FCX` | 博顿物联二开 | switch, switch1, switch2 | — |
| `2FG9` | 万家乐油烟机W8 | switch, gear, lightSwitch | Working, PourOil, cleanOnOff, CustomMode, AntiBackflow, DelayedShutdown, Cruise, SmokeLinkState, Ventilate, Runtime |
| `2FIO` | 小适智能电动剃须刀 | switch, mode, status | Alarm, Service, Cleaning, UsingTime, Intelligent, NormalMode, ShavingSpeed, ShavingTime, CurrentPower, Class, Feedback, Upgrade |
| `2FJ5` | 贝昂落地式循环扇 | switch, mode, fan | timingOff, timingOn |
| `2FM4` | 智能家居驱蚊器 | reset, brightness, mode | otaupgrade, remaintime, remainliquid, timeoff, connectstate |
| `2FNT` | 电动平衡车 C1 | speed, battery1, status | delicacy, speedControl, ledControl, encyclopedia, instructions, curMils, totalMil |
| `2FQZ` | MSN智能微电波美眼仪 | battery, gear, status | GearAdjustment, BatteryLevel, AvailableTime, TotalTime, TotalTimes, WorkingHours, Vibrate, Reconnect |
| `2G3X` | 真空吸尘器 | status, mode, battery | filterElement |
| `2G8V` | HYUNDAI现代电动牙刷 | cleanMode, massageMode, status | commonFaultDetection, leftBattary, gears, sensitiveMode, whiteMode |
| `2GB1` | 温湿度传感器 | battery, temperature, humidity | commonFaultDetection |
| `2GB4` | 红外人体移动光照传感器 | luminance, pir, battery | commonFaultDetection |
| `2GE8` | 烟雾传感器 | battery, silencer, alarm | smokeSensor, commonFaultDetection |
| `2GIT` | 万播投影仪T6 Max | volSwitch, switch, controlKey | jvolume, jfocusing |
| `2GKL` | MSN智能射频美眼仪 | battery, gear, status | Vibrate, Reconnect, TotalTime, BatteryLevel, TotalTimes, WorkingHours, AvailableTime |
| `2GKV` | 美森智能专业理发器 | mode, battery, status | ResetCutterHead, CutterHeadAlarm, Reconnect, AvailableTime, TotalTimes, RemainingDaysCutterHead |
| `2GR9` | 小黄蜂智能冲牙器 T1 | switch, mode1, gear | adjust, memory, pattern, state |
| `2GSG` | 康夫KF-3149多功能负离子吹风机 | mode, switch, status | Introduction, UserDefineName, UserDefineMode, Gear |
| `2GVK` | 狄耐克智能二路开关面板 | switch, switch1, switch2 | — |
| `2GWT` | 迈德斯特单电机升降桌 | sedentaryrSwitch, childLock, action | commonHeight, currentHeight, condition, FaultAndDetection, Heightsetting |
| `2GYL` | 大华可燃气体探测器JT-DH-HY-GA4FA-OL | silencer, selfCheck, gasSensor | commonFaultDetection, Warm, GasControl, SensorError, RelayControl |
| `2H09` | 卿刻智能门锁T5 | lockState, battery, openEvent | — |
| `2H15` | 卡唛电子指纹智能保管箱45HW | battery, openMode, doorStatus | FP, chipid, PW, SetTime, historyrecord |
| `2H16` | 卡唛电子指纹智能保管箱60HW | battery, openMode, doorStatus | FP, chipid, PW, SetTime, historyrecord |
| `2H17` | 卡唛电子指纹智能保管箱80HW | battery, openMode, doorStatus | FP, PW, chipid, SetTime, historyrecord |
| `2H18` | 卡唛电子指纹智能保管箱100HW | battery, openMode, doorStatus | FP, PW, chipid, SetTime, historyrecord |
| `2H4H` | 智小金智能柜内灯电源驱动 | switch, brightness, colourMode | — |
| `2H5T` | Yours智能负离子电吹风 | mode, switch, status | Time, Custom, Children, Haircare, Upgrade |
| `2H5U` | 净颜温感洁面仪 | switch, status, mode | batteryLevel, Remaining, Upgrade, Vibrating, TimeSet, Records |
| `2H5Z` | 映趣电动剃须刀MOCHA S | mode, switch, status | manipulate, history, NetworkStatus, BatteryLevel, Cleanfunction |
| `2H8W` | 音乐炫彩氛围灯 | mode, brightness, powerswitch | SUDU, savemode, explore, definecolour, OnoffLine, statemode |
| `2HAG` | 康佳按摩椅KZ-RH8900 | switch, autoMode, status | Leg, TimeSurplus, RiseDrop, Hot, Timer, Roll, shoulderarms, Zero, AirbagAuto, heacushion |
| `2HB9` | 得力多功能无线吸尘器 | alarm, battery, status | suction, lastTime, cumulativeTime, deviceControl |
| `2HBZ` | 酷轻松石墨烯热敷颈托 | gear, mode, temperature | workstatus, timing, remainder |
| `2HDF` | 绿克手持吸拖一体机HW1 | status, battery, selfclean | WaterSprayVolume, Suction, RollerBrushAirDrying, VolumeAdjusting, WorkingMode, fault |
| `2HJS` | 开能牌CF-12EYT1型中央净水机 | faultDetection, status, waterVolume | wateSpeed, dailyWaterVolume, deviceControl |
| `2HLV` | 小充嗨跑交流充电桩 | switch, chgMode, chaState | chargingLock, chargingDuration, chargingLog, deviceTime, chargingGun, chargingBook, ChargingStatistics, faultStatus, delete, chargingStatus |
| `2HMR` | 磨脚器 | mode, battery, switch | report, duration, history, personalnumber, time, severtime, userecord, remainingTime, personalCustom |
| `2HOB` | 酷轻松石墨烯智能睡袋 | gear, temperature, mode | remainder, workstatus |
| `2HOH` | 酷轻松石墨烯智能按摩靠枕 | temperature, mode, gear | message, remainder, workstatus, timing |
| `2HOI` | 酷轻松石墨烯智能按摩腰靠 | mode, temperature, gear | message, remainder, workstatus, timing |
| `2HOK` | 酷轻松石墨烯热敷按摩颈枕 | Switch, temperature, mode | LowPower, HotReminder, heating, workstatus, remainder, currentbattery |
| `2HOL` | 酷轻松石墨烯智能发热坐垫 | gear, temperature, mode | timing, workstatus, remainder |
| `2HRE` | 西蒙16A三孔智能插座 | switch, faultDetection, childLockSwitch | power, electric, IndicatorMode |
| `2HRF` | 西蒙10A五孔智能插座 | switch, faultDetection, childLockSwitch | power, electric, IndicatorMode |
| `2HYW` | 时生便携式电源 | battery, powerswitch, switch | outputpower, inputpower, commonFaultDetection, timingshutdown, RestTime, ShutdownRestTime, PVPower |
| `2I49` | 蒸汽清洁机 | status, switch, faultDetection | steamswitch |
| `2I5A` | 舒元AS-8883足疗机 | switch, sync, massage | ota, firmware, customMode, workTime, cdRemain, cdTotal, heating, air |
| `2I5C` | MSN智能电吹风 | mode, status, Volume | Warning, Upgrade, windSpeed, speeds, Anion, Gear, time |
| `2I7C` | 欧普蓝牙Mesh双色温灯带驱动 | switch, brightness, cct | toggleSwitch, commonFaultDetection |
| `2I7K` | 欧普蓝牙Mesh双色温筒射灯驱动 | switch, brightness, cct | toggleSwitch, commonFaultDetection |
| `2IEX` | 锐亿剃须刀373A | mode, battery, status | experience, deviceTime, userTime, grade, userecord, seekDevice, frequency, implemented |
| `2IF0` | 锐亿剃须刀373B | mode, battery, status | btConnection, userTime, deviceTime, implemented, userecord, seekDevice, frequency |
| `2IGA` | 万播投影仪WB-T3 | volSwitch, switch, controlKey | jfocusing, jvolume |
| `2IHJ` | SmartCurtain | opener, action, stroke | — |
| `2IK3` | 企一照明筒射灯驱动设备(蓝牙) | switch, cct, brightness | relBrightness, toggleSwitch, commonFaultDetection |
| `2IK7` | 企一照明低压双色温灯带蓝牙驱动 | switch, cct, brightness | relBrightness, toggleSwitch, commonFaultDetection |
| `2INP` | 艾家智能二位开关 | switch2, switch1, switch | lightness, switchStatus |
| `2IY0` | 奥特威智能窗帘 | opener, action, stroke | — |
| `2J1Y` | 檬丝眼部按摩仪 | switch, heatSwitch, mode | Status, BGM, timeSet |
| `2J33` | 火火兔智能早教故事机 H1S | action, switch, childLock | Music, timedTask, custom, batteryStatus, earLight |
| `2J7W` | 飞利浦膝盖按摩器PPM3102L | switch, workMode, waterTemp | Warning, deviceSatus, batteryLevel, message, Intensity, myCollection, OTAUpgrade, Remaining, temper |
| `2JBN` | 健诺德腰腹按摩器 | switch, hot, mode | electricity, connect, RemainingTime, countdown, strength, voice |
| `2JC9` | 欧普蓝牙mesh双色温磁吸灯驱动 | switch, brightness, cct | toggleSwitch, commonFaultDetection |
| `2JDD` | 欧普WiFi双色温驱动 | brightness, cct, switch | commonFaultDetection |
| `2JDK` | 智能椅SC-0004 | sedentaryReminder, battery, faultDetection | sedentaryTime, ota, seated, sitTime, sitPosture, sedentaryReminderMode, lengthofwaistsupport, SmartWaistMode, switchingfrequency, seatingtime, ManualMode, chargeStatus, eventTime, EquipmentStatus |
| `2JK2` | 杜亚智能卷帘 | changeDirection, opener, action | — |
| `2JLE` | gb SMART便携制冷包 | status, workStatus, temperature | temperatureRecord, knowledge, instructions, cool, equipmentStatus |
| `2JMN` | 暖通网关 | gatewayAction, faultDetection, operation | acList, heaterList, freshAirList, acGroupList, port1protocolList, heaterGroupList, freshAirGroupList, port2protocolList, 485NetInfo, vrvProtocol, connectMode, backupData, backup, generalList, generalGrouplist, reboot, automaticGroup, offlineOta |
| `2JMP` | 暖通网关 | gatewayAction, faultDetection, operation | acList, heaterList, freshAirList, acGroupList, port1protocolList, heaterGroupList, freshAirGroupList, port2protocolList, 485NetInfo, vrvProtocol, backupData, connectMode, backup, generalList, generalGrouplist, automaticGroup, offlineOta |
| `2JOO` | 锐亿剃须刀RS392 | battery, switch, status | History4, Currenttime, History3, Report, History2, History1, Applications, Introduction, Gear, Finddevices, Power |
| `2JP5` | 贝琪B321数码电子钢琴 | mode, speed, volume | Service, Deviceswitch, Beatvolume, practiceHistory, practice, metronome |
| `2JQE` | HCK哈士奇赛博朋克冰吧SC-98ZZAS | childLockSwitch, light, temp | Warning, Quickcoolingmode, door2, service, door, power |
| `2JS6` | 可移式LED灯具 | switch, brightness, mode | countdown, colorTemp |
| `2JTR` | 公牛智能转换插座GN-Y201HJ | indicator, switch, memorySwitch | power, electric, commonFaultDetection |
| `2JYH` | 健诺德云朵暖宫宝 | light, massage, battery | ota, alert, countdown, warm, state |
| `2K2I` | 宝宝巴士点读笔G3 | battery, volume, deviceStatus | PrivacyStatement, Aftersalesservice, MP3mode, connectedWIFI, currentplay, isBindAccount, resultCode, Logonstatus, batterylevel, WIFIinfo, playadjust, selectsong, songlist, Scheduleadjustment, WIFIconnect, AccountInformation, deviceinformation |
| `2K4Z` | FUNSNAP Capture 2云台 | battery, mode, status | lowbattery |
| `2KCQ` | 空间卫士健康空气智慧管家01 | switch, pm25, model | filterElement06, filterElement05, filterElement04, filterElement03, filterElement02, filterElement01, anion, FragranceTime, hotline, intelligent, ventilation, lamp, density, timing |
| `2KFI` | 酷轻松石墨烯热敷按摩支撑护腰带 | mode, battery, status | Shutdown, suspend, service, Timedshutdown, Vibrationgear, Thermoregulation, Timeremaining, CurrentTEMP |
| `2KLE` | 哈尔斯智能水杯  恒温暖暖杯 | battery, currentTemperature, connectStatus | drinkTemperature, usbState, constTempTimeAlready, constTempTime, constTempTimeSwitch, findCupState, hotState, buzzerSwitch, customTemperature, hotMode, hasSetHeatTemp |
| `2KY3` | 霍尼韦尔独立式感烟火灾探测报警器 | battery, silencer, alarm | smokeSensor, commonFaultDetection |
| `2L0A` | 荣康摩杰座按摩椅RK2001S | switch, action, autoMode | videoDisplay, autoAdjustment, manualAdjustment, postureAlignment, shoulDertest, afterSales, equipmentStatus, workingHours |
| `2L3K` | 酷轻松石墨烯压力腿套 | massageGear, deviceStatus, deviceSwitch | Battery1, service, Thermoregulation, timedShutdown, deviceMode, workStat |
| `2L4T` | 创明智能卷帘 | opener, action, directionalmode | rotation |
| `2L52` | 携住取电 | doorContact, switch, status | — |
| `2LAN` | 哈尔斯智能水杯 茶水分离款 | battery, currentTemperature, connectStatus | canvasData5, canvasData3, canvasData4, canvasData2, canvasData1, canvasConfig, config, drinkTemperature, brewTime, teaOrder, drinkRemind, teaMode, brewCount, currentTea |
| `2LF3` | FUNSNAP Capture 5云台 | battery, status, mode | lowbattery |
| `2LG4` | 智能塔扇 | fan, battery, switch | endTime, Standby, Swing |
| `2LJO` | Mate 60系列环闪保护壳 | switch, brightness, workStatus | control, firmwareUpgrade, sceneLightEffect, specialSet, colorTemperature |
| `2LJP` | Mate 60系列环闪保护壳 | switch, brightness, workStatus | control, firmwareUpgrade, specialSet, sceneLightEffect, colorTemperature |
| `2LK5` | 摩申高速吹风机MH08 | mode, speed, status | allstatus, fault, worktime, rspeed |
| `2LP7` | 友通甲醛检测仪 | temp, hcho, alarmSwitch | humi, commonFaultDetection, clock, brightness01, report |
| `2LYW` | 松下干衣机 NH-VH102FP | mode, childLockSwitch, status | leftTime, commonFaultDetection, newAction, newStatus, newSwitch |
| `2LZ9` | 纯麦智能点唱机K2 | Volume, reverb, AudioMode | — |
| `2M4E` | 九牧轻智能丝雨置物恒温淋浴器 | coldWaterSwitch, status, waterTemp | commonFaultDetection, devStatus |
| `2M8M` | 哈尔斯智能泡茶杯 | battery, currentTemperature, status | customTeaList, checkedTea, clock, drinkRemind |
| `2MDA` | BYXAS智能按摩暖腰带 | switch, alarm, hot | shutdown, countdown, BLEstatus, shake, BAT |
| `2MEK` | WYC智能暖腰带 | switch, hot, alarm | CurrentTemperature, baterry, shake, countdown, BLEstatus, shutdown |
| `2MGK` | 杜亚智能窗帘 | switchSpeed, opener, action | Direction |
| `2MH8` | 易百珑一键智能开关 | switch1, memorySwitch, mode1 | sceneButton1, Pair, led, CleanPair |
| `2MIG` | 光照传感器 | luminance, battery, switchNightLight | delayTime, commonFaultDetection |
| `2MNC` | 佳普乐宏臻智能毛巾架 | dryingGear, mode, drying | KeySoundReminder, BathMode, TimingMode |
| `2MQ8` | 莱轻松揉腹仪 | switch, emsGear, status | moxibustion, emsMode, kneadMode, batteryView, fomentTemperature, timedFuntion |
| `2MUB` | SORONTEK 智能双色射灯 | lightMode, switch, brightness | coolwarm |
| `2MX1` | 北斗浮雕地球仪 | mode, brightness, switch | ChargeStatus, Battery |
| `2MXF` | 独立式光电感烟火灾探测报警器 | silencer, alarm, selfCheck | smokeSensor, commonFaultDetection |
| `2N1J` | 智掂LED光疗面罩 | status, mode, action | commonFaultDetection, alertService, firmware, plan, remain, workRecord |
| `2N7Z` | subnado水下推进器PP11011 | mode, speed, workStatus | fault, protection, leftDevice, rightDevice, rapidRemian, otaUpdate, deviceNum, deviceVersion, record |
| `2N8I` | 好太太智能晾衣机 1156H | action, lightSwitch, status | commonFaultDetection |
| `2N8Z` | 俏美人热敷护腰带 | switch, alarm, hot | BLEstatus, countdown, baterry, CurrentTemperature, shutdown, shake |
| `2NF5` | 吸顶式温湿度传感器 | heat, humidity, switchNightLight | reportSetting |
| `2NFE` | 香百年智能离子净化香氛机 | switch, mode, volume | commonFaultDetection, devInfo, electric, connectInfo, consumable, debus, auto, ion, lamp, cycle, car, concentration |
| `2NGR` | 智能充气泵 | status, mode, light | state, pumpfinish, charge, unit, syncCurrentData, setPressure, error |
| `2NHB` | eachone一起玩智能循环扇 | switch, mode, fan | Countdownshutdown |
| `2NK0` | FUNSNAP CM8云台 | battery, followMode, status | lowbattery |
| `2NM6` | 麦瑞克MR-2365颈肩按摩器 | mode, gear, status | commonFaultDetection, batteryLevel, Lefttime, HotCompress, Shutdown, VideoIntroduction |
| `2NMD` | 云康宝筋膜枪CM40F | action, battery, mode | btconnection, countDown, speedOn, time |
| `2NME` | 森森智能鱼缸 | colour, waterTemp, lightSwitch | commonFaultDetection, feed, changewater, filter |
| `2NRQ` | 酷轻松石墨烯腰部支撑按摩器 | workStatus, mode, massage | lowpower, remainTime, bleStatus, ota, syncTime, firmware, electricity, inflation, inflationTime, heating, countdown |
| `2NS7` | 三思智能护眼吸顶灯HC60 | switch, brightness, cct | — |
| `2NTC` | 倍益康压缩靴 | switch, status, mode | errorTip, prefer, higherOrder, massageTime, pressure, electricity |
| `2NV3` | 森瑞智能窗帘 | changeDirection, opener, action | SBZT |
| `2NVI` | 森瑞双生日夜帘 | action, nightAction, opener | nightOpener, SBZT |
| `2NX5` | 倍益康可变振幅深层肌肉按摩仪 | action, battery, workStatus | btconnection, commonFaultDetection, strength, amplitude, revolution, countdown, otaUpgrade |
| `2NYJ` | 美菱503WPU9CDZX冰箱 | intelligentSwitch, faultDetection, freezeSwitch | featureMode, freezerFloat, refrigeratorFloat |
| `2O05` | 开合帘电机 | changeDirection, opener, action | — |
| `2O2D` | 贵品百叶GL | rotationAction, opener, action | suitablePoint |
| `2O30` | 威仕达卷帘WSERD30 | changeDirection, opener, action | — |
| `2O65` | 便携电动剃须刀 | battery, status, bladeStatus | time, power, batteryCycles, history, duration, resetTime |
| `2O8J` | 倍益康水杯式保健制氧机 | workStatus, gear, mode | buttonSound, shutDown, workTime, molecular, filterCotton, pulse, upgrade, plain, deviceVersion, batteryLevel, oxygen, fault |
| `2O9K` | 海雀智能摄像头3i 3K版 64GB | shootSwitch, switch, videoSwitch | — |
| `2ODZ` | 造化万物热敷按摩仪 | switch, temp, battery | vibrate, countdown |
| `2OG1` | 梵吉尼香氛机S5 | switch, faultDetection, mode | SprayDuration, ResidualVolume, IntervalDuration, TotalConsumption |
| `2ONX` | 狄耐克可视对讲门口机 | faultDetection, tamperAlarm, otherrAlarm | userData, doorbellRecord, openDoorRecord |
| `2OPO` | 星闪温湿度传感器 | battery, temperature, humidity | commonFaultDetection |
| `2OST` | 艾诺华智能猫砂盆 | clean, deviceStatus, alarm | resetRoller, empty |
| `2OYN` | 承弦雨水传感器S1 | battery, switch, sensitivity | rainFall |
| `2P0W` | 皇家惠人水暖毯HRS53 | switch, mode, temperature | commonFaultDetection |
| `2P43` | 佳普乐宏岚智联毛巾架 | temperature, drying, status | dryingTime, dryingLeftTime |
| `2P44` | 佳普乐宏瑞智联毛巾架 | temperature, drying, status | dryingTime, dryingLeftTime |
| `2P8F` | 良信智能断路器NDB5E-80 | ctrl, faultDetection, status | curNeutral, electric, electricC, electricB, electricA, rcFunction, poles |
| `2PIC` | Core Max全景相机 | mode, photo, video | — |
| `2PJM` | 哈尔斯智能咖啡杯 星闪版 | battery, currentTemperature, waysOfDrinking | waterDayIntake |
| `2PUL` | 贝昂智能电风扇 | switch, mode, fan | orderOn, endTime |
| `2PY3` | 九牧Z300旋转电热毛巾架 | childLockSwitch, mode, temperature | dryingTime, dryingLeftTime, commonFaultDetection |
| `2Q3X` | 双色温吸顶灯24W | brightness, cct, switch | — |
| `2Q3Y` | 双色温吸顶灯36W | brightness, cct, switch | — |
| `2Q3Z` | 三思智能球泡灯13W | switch, brightness, cct | — |
| `2Q45` | 电亿秒智能插座 CH1 | indicator, memorySwitch, switch | electric, power |
| `2Q7M` | 三思智能球泡灯8W | brightness, cct, switch | — |
| `2Q7V` | 三思智能球泡灯18W | brightness, cct, switch | — |
| `2QB1` | 正泰智能计量器ZTEM01 | backlight, emulate, faultDetection | backup, electric, restart, totalElectricity |
| `2QME` | 星飞菱投影幕吊架控制器 | action, backLight, workStatus | travelCompensation, travelTime |
| `2QQB` | BOW星闪触控折叠键盘 | battery, capsLock, keyboardLock | — |
| `2QVX` | 恩仕AXENT.NOVIA智能浴室镜 | colourMode, demisterSwitch, status | dryingTime, sterilizeTime |
| `2QWO` | 雷神牌等离子体车载消毒机 | windspeed, pm25, switch | definiteTime, filterElement, tvoc2 |
| `2R0N` | 恩仕AXENT暗装电热毛巾架 | drying, heat, status | dryingLeftTime, dryingTime, commonFaultDetection |
| `2R0O` | 福临门控制器 | action, backLight, switch | height, travelCompensation |
| `2R5H` | 正泰智能计量器ZTEM01 Pro | backlight, emulate, faultDetection | backup, electric, hisPower1, hisPower2, hisPower3, hisPower4, hisPower5, hisPower6, realTimePower, restart, rtPower1, rtPower2, rtPower3, rtPower4, rtPower5, rtPower6, secPower, totalElectricity |
| `2R8Y` | 立达信米来吊灯Pro | brightness, switch, commonMemorySwitch | relBrightness, commonFaultDetection |
| `2RE4` | simon玻璃材质16A智能三孔插 | indicator, switch, memorySwitch | electric, power, commonFaultDetection |
| `2RE5` | simon玻璃材质10A智能五孔插 | indicator, switch, memorySwitch | electric, power, commonFaultDetection |
| `2RE6` | simon塑料材质16A智能三孔插 | indicator, switch, memorySwitch | electric, power, commonFaultDetection |
| `2RE7` | simon塑料材质10A智能五孔插 | indicator, switch, memorySwitch | electric, power, commonFaultDetection |
| `2RE8` | simon金属材质16A智能三孔插 | indicator, switch, memorySwitch | electric, power, commonFaultDetection |
| `2RE9` | simon金属材质10A智能五孔插 | indicator, switch, memorySwitch | electric, power, commonFaultDetection |
| `2RHX` | 旭格平开窗驱动 | action, openStatus, switchSpeed | bottomTravel, travel |
| `2RHY` | 贝克洛电动平推窗控制器 | action, openStatus, opener | lockMechanism, commonFaultDetection |
| `2RJ9` | 贝克巴斯超级感应净水龙头 | inductionSwitch, switch, waterSwitch | faucetElement, outletWater, outletWater1, outputTds, commonFaultDetection |
| `2RKZ` | 恩仕AXENT暗装电热浴巾架 | drying, heat, status | dryingLeftTime, dryingTime, commonFaultDetection |
| `2RMK` | 杜亚智能雨水传感器 | battery, sensitivity, switch | rainFall, commonFaultDetection |
| `2RP6` | 唯斯特姆食物垃圾处理器 | mode, start, status | processingcapacity, workTime, commonFaultDetection |
| `2RQY` | 欧雅系列洗衣机 | action, mode, status | leftTime, commonFaultDetection |
| `2RUI` | 王力机器人门X60 Pro-H | doorEvent, lockStatus, messagePush | doorKeyOperate, event |
| `2RWE` | 欧雅系列洗烘一体机 | action, mode, status | leftTime, commonFaultDetection |
| `2RY8` | 良信智能断路器NDB5EL-80 | ctrl, faultDetection, status | curNeutral, electric, electricC, electricB, electricA, poles, rcFunction |
| `2S0H` | 杜亚智能窗帘C5 | switchSpeed, opener, action | Direction |
| `2S0Z` | 贝克洛电动推拉控制器 | action, openStatus, opener | lockMechanism, commonFaultDetection |
| `2S2F` | 友望智能活水自清洁剃须刀 | battery, searchDevice, status | bladeClean, bladeReset, btConnection, razor, time, workingTime, commonFaultDetection, dryingTime |
| `2S3R` | 哈尔斯智能焖泡杯 星闪纯钛版 | battery, findCup, temperature | drinkDisturb, drinkRemindArray, healthRemindArray, userData, commonFaultDetection, canvasData1, customTeaList, canvasData3, lightColor, canvasData4, canvasConfig, checkedTea, canvasData2, canvasData5 |
| `2S3X` | 哈尔斯智能焖茶壶 星闪纯钛版 | battery, findCup, temperature | drinkDisturb, drinkRemindArray, healthRemindArray, userData, waterRemind, commonFaultDetection, canvasData5, canvasConfig, customTeaList, canvasData3, lightColor, checkedTea, canvasData4, canvasData1, canvasData2 |
| `2S8M` | 良信智能断路器NDB5E-40 | ctrl, faultDetection, status | curNeutral, electric, electricC, electricB, electricA, rcFunction, poles |
| `2S8N` | 良信智能断路器NDB5EL-40 | ctrl, faultDetection, status | curNeutral, electric, electricC, electricB, electricA, rcFunction, poles |
| `2SK3` | 公牛智能五孔轨道适配器 | indicator, switch, switch1 | electric, power, commonFaultDetection |
| `9MTL` | 智控床头灯 | brightness, cct, switch | — |
| `9MTW` | 智控电饭煲 | action, status, switch | cooker, leftTime, commonFaultDetection |
| `9MU7` | 智控灯泡 | brightness, cct, switch | — |
| `9MY5` | 智控窗帘 | leftAction, leftOpener, opener | — |
| `9MYJ` | 智控炸锅 | action, status, temperature | leftTime, recipes, workTime |
| `9MZT` | 智控电磁炉 | mode, status, switch | — |
| `A0CX` | 美的智能电热水器 | switch, status, temperature | capacity, leftTime |
| `A0D8` | 康佳智能电视 | switch, volSwitch, volume | channel, sigInterface |
| `A0GS` | 洗碗机 | switch, action, faultDetection | — |
| `A0NT` | 智能双通道插座 | switch, switch1, switch2 | — |
| `A0OQ` | 智能双通道开关 | switch, switch1, switch2 | — |
| `A0R1` | 大金转角新风 | switch, mode, fan | commonFaultDetection |
| `A0S2` | 大金新风系统 | mode, switch, fan | commonFaultDetection |
| `A0SQ` | 美的净水机 | status, rinseSwitch, faultDetection | inputTds, outputTds, purifyWater, filterElement1, filterElement2 |
| `A0TY` | 美的电热水器 | switch, status, temperature | commonFilterElement1 |
| `A0VZ` | 美的电热水器 | switch, status, temperature | commonFilterElement1 |
| `A0Y0` | 方太油烟机EM52.i | switch, gear, lightSwitch | — |
| `A0Z2` | 西门子开关 | switch, switch1, switch2 | — |
| `A104` | 阿尔法蛋故事机Z1 | switch, musicPlay, volume | LS202, L803, L901, L3901, L1201, L701 |
| `A10Y` | 美的智能取暖器 | switch, temperature, faultDetection | preTime, orderTime, cleanTimer |
| `A122` | 苏泊尔小C主厨料理机 | switch, mode, status | recipes, leftTime, addToDevice, toCooking, cookingSpeed, cookingFire, cookingPressure, cookingTime, cookingTemperature, cookingStatus, cookingType |
| `A15V` | 美的管线机 | status, water, germicidalSwitch | outlet, germicidalDuration |
| `A1AH` | 美的电饭煲 | status, action, mode | keptWarmTime, leftTime, currentFun |
| `A1AZ` | 美的家用空调 | switch, mode, temperature | — |
| `A1B0` | 美的家用空调 | switch, mode, temperature | — |
| `A1BM` | 美的电热水器 | switch, status, temperature | leftTime |
| `A1EI` | HOPE Music Pad 3S | volume, commonExecution1, commonExecution2 | playControl, playModel |
| `A1EV` | 美的家用空调 | switch, mode, temperature | — |
| `A1EX` | COLMO空调 | switch, mode, temperature | — |
| `A1EY` | COLMO空调 | switch, mode, temperature | — |
| `A1IM` | DDF60-i14029储水式电热水器 | switch, mode, temperature | commonFaultDetection, cTVolume, wPswitch, orderSwitch, statu |
| `A1IY` | 远红外IH电饭煲 | workStatus, machineStatus, currentTemperature | smartRecipe, machineSavedRecipesID, recipeID, riceChoice, texture, appointmentTime, setTime, onOffCancel, holdingTime, leftworkTime |
| `A1JS` | JSQ30-16JH61i家用供热水燃气快速热水器 | switch, mode, temperature | commonFaultDetection, highTempUnlock, totalGas, totalWater, iwaterTmp, cycle, waterfallBath, heating |
| `A1KV` | 九阳铁釜IH电饭煲 | status, start, stop | commonFaultDetection, remainingTime, startCloud, progress |
| `A1L9` | 九阳IH炭钢釜液晶智能电饭煲 | status, stop, start | leftTime, commonFaultDetection, progress, lastFuncCode |
| `A1NZ` | DDF60-YH05i储水式电热水器 | switch, mode, temperature | commonFaultDetection, statu, orderSwitch, wPswitch, cTVolume |
| `A1RQ` | 美的CXW-260-B87抽油烟机 | switch, gear, faultDetection | — |
| `A1SI` | COLMO橱下式净水机CWRC800-B139 | status, faultDetection, rinseSwitch | filterElement1, filterElement2, purifiedWaterTDS, rawWaterTDS |
| `A1SV` | 不用手洗多功能破壁机 | status, clean, stop | commonFaultDetection, commonMenu, startHealth, currentCapacity, currentFuncCode |
| `A1WN` | 九阳免手洗破壁机L12-Y951 | status, stop, start | devStatus, finshReport |
| `A1Y7` | JSQ24-13ZH6i家用供热水燃气快速热水器 | switch, mode, temperature | commonFaultDetection, highTempUnlock, Selfclean, heating, cycle, totalGas, waterfallBath, iwaterTmp, totalWater |
| `A1Y8` | JSQ30-16ZH6i家用供热水燃气快速热水器 | switch, mode, temperature | commonFaultDetection, highTempUnlock, totalGas, heating, totalWater, Selfclean, cycle, waterfallBath, iwaterTmp |
| `A1Y9` | JSQ34-18ZH6i家用供热水燃气快速热水器 | switch, mode, temperature | commonFaultDetection, highTempUnlock, iwaterTmp, cycle, totalGas, waterfallBath, Selfclean, heating, totalWater |
| `A2D8` | COLMO橱下式净水机CWRC800-B106 | status, faultDetection, rinseSwitch | filterElement1, filterElement2 |
| `A2F7` | 颁芙叠影系列燃气热水器 | switch, status, mode1 | commonFilterElement1, commonFaultDetection, SetAff, temRange, zerocold, zerocold2, waterPressurization, temperatureSet, call |
| `A2IL` | 方太油烟机EM52.i | lightSwitch, gear, switch | — |
| `A2IR` | 方太油烟机CXW-358-Z8T | lightSwitch, gear, switch | airQuality, DelayTime, GestureState, AirHouseMode |
| `A2IW` | 美的电压力锅MY-C552N | mode, action, status | leftTime, commonFaultDetection |
| `A2J2` | 美的全自动破壁机 | action, mode, status | leftTime, commonFaultDetection, currentFun, cupType |
| `A2J6` | 美的电蒸锅 MZ-ZGS352012 | action, mode, status | commonFaultDetection, remainTime, waterStatus, pauseTime |
| `A2J7` | 美的电炖锅 MD-DGS4011 | mode, action, status | leftTime, commonFaultDetection, currentFun, mouthfeel |
| `A2JL` | 智能双通道机械开关 | switch, switch1, switch2 | — |
| `A2MG` | 新日电动车4G锂电版 | lockSwitch, powerSwitch, seatSwitch | commonFaultDetection, remainingMileage, SOC, packageStatus |
| `A2ML` | 厦讯科技智能水表 | waterConsumptionForYesterday, waterMeterReading, status | — |
| `A2NE` | KEKEN 智能开关3键 | switch3, switch2, switch1 | backlight2 |
| `A2OG` | 新日电动车4G铅酸版 | lockSwitch, powerSwitch, seatSwitch | commonFaultDetection, packageStatus, SOC |
| `A2OP` | 智汇云温湿度传感器 | heat, temperature, humidity | — |
| `A2PS` | 脉冲式蓝牙热水表DN25 | waterConsumptionForYesterday, status, waterMeterReading | — |
| `A2PT` | 脉冲式蓝牙热水表DN20 | waterConsumptionForYesterday, status, waterMeterReading | — |
| `A2QK` | 脉冲式蓝牙水表DN20 | waterConsumptionForYesterday, status, waterMeterReading | — |
| `A2QL` | 脉冲式NB水表DN15 | waterConsumptionForYesterday, status, waterMeterReading | — |
| `A2QM` | 脉冲式NB水表DN25 | waterConsumptionForYesterday, status, waterMeterReading | — |
| `A2QN` | 脉冲式NB水表DN20 | waterConsumptionForYesterday, status, waterMeterReading | — |
| `A2QO` | 光电直读水表DN15 | waterConsumptionForYesterday, status, waterMeterReading | — |
| `A2QP` | 光电直读水表DN20 | waterConsumptionForYesterday, status, waterMeterReading | — |
| `A2QQ` | 光电直读水表DN25 | waterConsumptionForYesterday, status, waterMeterReading | — |
| `A2QT` | 脉冲式蓝牙水表DN25 | waterConsumptionForYesterday, status, waterMeterReading | — |
| `A2QW` | NB大口径水表 | waterConsumptionForYesterday, status, waterMeterReading | — |
| `A2QX` | 光电直读大口径水表 | waterConsumptionForYesterday, status, waterMeterReading | — |
| `A2QY` | 脉冲式蓝牙热水表DN15 | waterConsumptionForYesterday, status, waterMeterReading | — |
| `A2QZ` | 脉冲式NB热水表DN15 | waterConsumptionForYesterday, status, waterMeterReading | — |
| `A2R0` | 光电直读热水表DN15 | waterConsumptionForYesterday, status, waterMeterReading | — |
| `A2R1` | 脉冲式NB热水表DN20 | waterConsumptionForYesterday, status, waterMeterReading | — |
| `A2R2` | 脉冲式NB热水表DN25 | waterConsumptionForYesterday, status, waterMeterReading | — |
| `A2R3` | 光电直读热水表DN20 | waterConsumptionForYesterday, status, waterMeterReading | — |
| `A2R4` | 光电直读热水表DN25 | waterConsumptionForYesterday, status, waterMeterReading | — |
| `A2R8` | NB大口径热水表 | waterConsumptionForYesterday, status, waterMeterReading | — |
| `A2R9` | 光电直读大口径热水表 | waterConsumptionForYesterday, status, waterMeterReading | — |
| `A2TN` | 脉冲式蓝牙水表DN15 | waterConsumptionForYesterday, status, waterMeterReading | — |
| `A2U3` | 14QC1i燃气壁挂炉 | switch, faultDetection, heatSwitch | totalGas, totalWater, eneMode, iwaterTmp, bathTemp, heatTemp |
| `A2UR` | 万家乐燃气热水器普通恒温系列 | switch, temperature, status | — |
| `A2UT` | 万家乐电热水器 | switch, temperature, status | — |
| `A2VM` | 色温灯 | switch, brightness, cct | — |
| `A2W8` | KEKEN 电动窗帘C10 | opener, action, reverse | calibration |
| `A30B` | 智汇云冷暖调光灯 | switch, brightness, cct | turnoffTime, turnonTime |
| `A30K` | 九牧智能毛巾架9340015 | temperature, drying, status | dryingTime, dryingLeftTime, commonFaultDetection, order3, order2, order1 |
| `A30L` | 美的扫地机V10 | battery, cleanMode, action | — |
| `A30M` | 美的扫地机V12 | battery, cleanMode, action | — |
| `A32Q` | COLMO地暖 | temperature, status, switch | Convenientfeatures |
| `A333` | 美的地暖 | temperature, status, switch | Convenientfeatures |
| `A33C` | 方太油烟机CXW-358-Z8T | lightSwitch, gear, switch | airQuality, DelayTime, GestureState, AirHouseMode |
| `A33L` | 美的扫地机V12(白) | battery, cleanMode, action | — |
| `A364` | 欧派智能三位开关P33 | switch3, switch2, switch1 | — |
| `A368` | 欧派智能C单色柜灯带P23 | switch, brightness, faultDetection | MasterLightType, MasterLightMode |
| `A36L` | 科沃斯扫地机器人 | battery, action, status | — |
| `A373` | 美的扫地机W20(彩箱) | battery, cleanMode, action | — |
| `A374` | 美的扫地机V12(彩箱) | battery, cleanMode, action | — |
| `A375` | 美的扫地机W20(黑) | battery, cleanMode, action | — |
| `A37U` | COLMO 洗衣扫拖空间站-机器人 | battery, cleanMode, action | — |
| `A37V` | 小天鹅双囍站-机器人 | battery, cleanMode, action | — |
| `A389` | 小天鹅双囍站-机器人(第二代) | battery, cleanMode, action | — |
| `A3A3` | 美的灵眸扫地机器人 W20 Pro | cleanMode, battery, action | — |
| `A3A7` | 美的灵眸扫地机器人V13 | cleanMode, battery, action | — |
| `A3AT` | 美的灵眸扫地机器人 | cleanMode, battery, action | — |
| `A3C5` | 油烟机 | status, switch, gear | — |
| `A3CS` | COLMO电热水器 | switch, temperature, status | commonFaultDetection |
| `A3CT` | COLMO燃气热水器 | switch, temperature, status | commonFaultDetection |
| `A3D4` | 美的燃气热水器 | switch, temperature, status | commonFaultDetection |
| `A3EA` | COLMO燃气热水器 | switch, temperature, status | commonFaultDetection |
| `A3ED` | 美的燃气热水器 | switch, temperature, status | commonFaultDetection |
| `A3F3` | 海信智能水温控制器 | switch, mode, temperature | — |
| `A3GC` | 美的单向流新风机 | freshAirSpeed, status, switch | — |
| `A3GY` | 格力至尊型户式机 | switch, mode, temperature | — |
| `A3IK` | 倍世中央净水机 | flushSwitch, rinseMode, status | cleanTime |
| `A3J9` | 美诺智能干衣机 | action, mode, status | leftTime, commonFaultDetection |
| `A3JA` | 美诺智能冰箱 | freezeSwitch, refrigerateSwitch, status | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3MR` | 格力新风净化机(60ab) | freshAirSpeed, mode, switch | — |
| `A3N0` | 澳柯玛冰箱507 | freezeSwitch, intelligentSwitch, refrigerateSwitch | freezerFloat, refrigeratorFloat |
| `A3NT` | 华帝智能蒸烤箱 | action, status, switch | leftTime, commonFaultDetection |
| `A3R2` | 嘉格纳蒸箱 | lackWater, status, switch | leftTime, steamer, commonFaultDetection |
| `A3RY` | 安吉尔J3402-ROB120H | flushSwitch, switch, water | filterElement1, filterElement2, commonFaultDetection |
| `A3SA` | 嘉格纳 冰箱 | freezeSwitch, refrigerateSwitch, status | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3TA` | 西门子 冰箱 | freezeSwitch, refrigerateSwitch, status | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3TH` | 博世 冰箱 | freezeSwitch, refrigerateSwitch, status | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3U9` | 小佩饮水机P4117 | childLock, machineStatus, operation | statistics |
| `A3VL` | 嘉格纳Vario 400 系列灶具38cm | heatGear, status, mode | heating |
| `A3WG` | 嘉格纳Expressive 艺境系列微波烤箱右侧铰链 | childLockSwitch, status, switch | leftTime, oven, commonFaultDetection |
| `A3WS` | 滨特尔牌CF300型中央净水机 | flushSwitch, mode, status | cleanTime, cycleVolume, filterElement2, rinseMoment, rinseTime, waterSpeed, waterPurifier |
| `A3WX` | 嘉格纳Expressive 艺境系列烤箱左侧铰链 | childLockSwitch, status, switch | leftTime, oven, commonFaultDetection |
| `A3X0` | 嘉格纳Minimalistic臻境系列蒸汽烤箱碳晶黑 | childLockSwitch, status, switch | leftTime, oven, commonFaultDetection |
| `A3X1` | 博世御器Z4炫彩大屏蒸烤一体机 | childLockSwitch, status, switch | leftTime, ovenSteamer, commonFaultDetection |
| `A3X2` | 嘉格纳Expressive 艺境系列微波烤箱左侧铰链 | childLockSwitch, status, switch | leftTime, oven, commonFaultDetection |
| `A3X7` | 海尔法式冰箱 | aiFfSwitch, intelligentSwitch, refrigerateSwitch | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3X9` | 安吉尔S7 800 | flushSwitch, switch, water | filterElement1, filterElement2, commonFaultDetection |
| `A3XA` | 嘉格纳Expressive 艺境系列烤箱 | childLockSwitch, status, switch | leftTime, ovenSteamer, commonFaultDetection |
| `A3XM` | 卡萨帝光年油烟机 | gear, lightSwitch, switch | — |
| `A3XQ` | 卡萨帝揽光蒸烤箱 | childLockSwitch, status, switch | leftTime, ovenSteamer, remoteControlService, bakeTime |
| `A3XT` | 安吉尔 E-Tech鲜热一体机 | flushSwitch, switch, water | filterElement1, filterElement2, commonFaultDetection |
| `A3XU` | 安吉尔 M5 600 | flushSwitch, switch, water | filterElement1, commonFaultDetection |
| `A3XV` | 安吉尔 M7 Home Pro 800(末端) | flushSwitch, switch, water | filterElement1, filterElement2, commonFaultDetection |
| `A3XW` | 安吉尔 Q7 1000 | flushSwitch, switch, water | filterElement1, filterElement2, commonFaultDetection |
| `A3XX` | 安吉尔 Q3 600 | flushSwitch, switch, water | filterElement1, filterElement2, commonFaultDetection |
| `A3Y0` | 西门子玄晶Pro蒸烤一体机60厘米 | childLockSwitch, status, switch | leftTime, oven, commonFaultDetection |
| `A3Y1` | 卡萨帝指挥家油烟机 | gear, lightSwitch, switch | — |
| `A3Y2` | 卡萨帝致境油烟机 | gear, lightSwitch, switch | — |
| `A3YM` | 滨特尔牌SF270 型软水机 | mode, status, softerenMode | filterElement2, hardness, rewaterTime, waterSpeed, totalWorkTime, waterPurifier |
| `A3YN` | 滨特尔牌SF300 型软水机 | mode, status, softerenMode | filterElement2, hardness, rewaterTime, totalWorkTime, waterSpeed, waterPurifier |
| `A3YP` | 西门子玄晶Pro蒸烤一体机45厘米 | childLockSwitch, status, switch | leftTime, oven, commonFaultDetection |
| `A3YV` | 西门子studioLine蒸箱 | childLockSwitch, status, switch | leftTime, oven, commonFaultDetection |
| `A3YW` | 西门子玄晶Pro蒸箱 | childLockSwitch, status, switch | leftTime, oven, commonFaultDetection |
| `A3YZ` | 西门子studioLine烤箱 | childLockSwitch, status, switch | leftTime, oven, commonFaultDetection |
| `A3Z5` | 博世极匠Pro蒸烤一体机60厘米 | childLockSwitch, status, switch | leftTime, oven, commonFaultDetection |
| `A3Z8` | 博世极匠Pro蒸烤一体机45厘米 | childLockSwitch, status, switch | leftTime, oven, commonFaultDetection |
| `A3Z9` | 博世accentLine天工蒸箱 | childLockSwitch, status, switch | leftTime, steamer, commonFaultDetection |
| `A3ZB` | 博世极匠Pro蒸箱 | childLockSwitch, status, switch | leftTime, steamer, commonFaultDetection |
| `A3ZC` | 博世accentLine天工烤箱 | childLockSwitch, status, switch | leftTime, oven, commonFaultDetection |
| `A3ZE` | 博世极匠Pro烤箱 | childLockSwitch, status, switch | leftTime, oven, commonFaultDetection |
| `A3ZX` | 海尔冰箱BCD-630WGHFD1BRWU1 | aiFfSwitch, intelligentSwitch, refrigerateSwitch | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3ZZ` | 海尔麦浪冰箱 | aiFfSwitch, aiNutrientCabin, aiVersatileCabin | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A401` | 海尔十字门冰箱 | aiFfSwitch, intelligentSwitch, refrigerateSwitch | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A407` | 卡萨帝冰箱BCD-620WGCFDM4L8U1 | aiFfSwitch, aiFpSwitch, refrigerateSwitch | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A408` | 卡萨帝冰箱BCD-520WGCFDM4WKU1 | aiFfSwitch, freezeSwitch, switch | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A41X` | 安吉尔集成设备(末端)H3770-R2 a | flushSwitch, switch, water | filterElement1, filterElement2, commonFaultDetection |
| `A41Y` | 安吉尔集成设备(末端)H3770-R2 b | flushSwitch, switch, water | filterElement1, filterElement2, commonFaultDetection |
| `A42A` | 嘉格纳臻境系列蒸箱 | childLockSwitch, status, switch | leftTime, oven, commonFaultDetection |
| `A42B` | 嘉格纳艺境系列嵌入式电烤箱 | childLockSwitch, status, switch | leftTime, oven, commonFaultDetection |
| `A42C` | 嘉格纳艺境系列嵌入式紧凑型蒸烤一体机 | childLockSwitch, status, switch | leftTime, oven, commonFaultDetection |
| `A42D` | 海尔山茶花冰箱 | aiFfSwitch, aiNutrientCabin, aiVersatileCabin | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A43T` | 箭牌轻智能浴缸AL1787SQ | drainSwitch, heat, waterInletSwitch | — |
| `A44Q` | 嘉格纳Minimalistic 曜岩黑系列 | childLockSwitch, status, switch | leftTime, oven, commonFaultDetection |
| `A44Z` | 欧瑞博新风 | fan, mode, switch | airQuality, co2, commonFaultDetection |
| `A454` | 卡萨帝指挥家烤箱 | childLockSwitch, status, switch | leftTime, oven, remoteControlService, bakeTime |
| `A456` | 卡萨帝指挥家蒸箱 | childLockSwitch, status, switch | leftTime, remoteControlService, steamer, bakeTime |
| `A457` | 卡萨帝致境烤箱 | childLockSwitch, status, switch | leftTime, oven, remoteControlService, bakeTime |
| `A46K` | 嘉格纳艺境系列嵌入式烤箱右开门 | childLockSwitch, status, switch | leftTime, oven, commonFaultDetection |
| `A46W` | 海尔冰箱BCD-578WGHFD1BYAU1 | aiEsSwitch, aiFfSwitch, aiFpSwitch | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A46Y` | 嘉格纳艺境系列嵌入式蒸烤一体机左开门 | childLockSwitch, status, switch | leftTime, oven, commonFaultDetection |
| `A472` | 嘉格纳臻境系列烤箱60cm | childLockSwitch, status, switch | leftTime, oven, commonFaultDetection |
| `ZG13` | 调光调色智能灯 | switch, brightness, cct | fadeTime, relBrightness |
| `ZG15` | 调光调色床头灯 | switch, brightness, cct | fadeTime, relBrightness |
| `ZG17` | 调光调色灯带 | switch, brightness, cct | fadeTime, relBrightness |
| `ZG23` | 可视对讲底盒 | luminance, status, switch | cfgNet, clickedScene, deviceLabel, diagnose, dryContact1, dryContact2, dryContact3, dryContact4, dryContact5, hwaccount, lcdattr, luminanceReportSetting, pageInfo, plcSubSystem, reboot, reportSceneId, responseSetting, scurity, subScene, txPower |
| `ZG2F` | 调光调色吊灯 | switch, brightness, cct | fadeTime, relBrightness |
| `ZG2G` | 调光调色射灯 | switch, brightness, cct | fadeTime, relBrightness |
| `ZG2H` | 调光调色筒灯 | switch, brightness, cct | fadeTime, relBrightness |
| `ZG2I` | 调光调色吸顶灯 | switch, brightness, cct | fadeTime, relBrightness |
| `ZG2J` | 调光调色磁吸灯 | switch, brightness, cct | fadeTime, relBrightness |
| `0101` | 灯组 | switch, brightness | — |
| `100E` | 控客Wi-Fi智能插座 | switch, indicator | delay, timerID |
| `100J` | 杜亚电动开窗机DJ56TSWH | motor, openLevel | — |
| `100K` | 杜亚电动窗帘DT76TV/WH | motor, openLevel | — |
| `100l` | 方太智能油烟机 | switch, gear | kitchenVentilator |
| `100n` | 方太智能电烤箱 | switch, temperature | oven |
| `100s` | 美的音乐热水器 | switch, temperature | elecHeater, music |
| `1016` | 烟雾传感器 | smoke, battery | — |
| `1017` | 燃气泄漏传感器 | smoke, battery | — |
| `101E` | 紧急按钮 | pushButton, battery | — |
| `101M` | 超薄三 | cleanerRobot, faultDetection | cleanRecord, edge, hepa, roll |
| `101h` | 杜亚电动窗帘DT806TV/WH | motor, openLevel | — |
| `101j` | 杜亚电动卷帘DM35F/WH | motor, openLevel | — |
| `101t` | 超薄三 | cleanerRobot, faultDetection | cleanRecord, edge, hepa, roll |
| `101u` | 小天鹅洗衣机 | switch, faultDetection | washer |
| `101v` | 公牛WiFi智能插座2代 | switch, powerSupply | delay, timerID |
| `1021` | Libratone ZIPP MINI 无线音响 | battery, faultDetection | Music |
| `1022` | Libratone ZIPP音响 | battery, faultDetection | Music |
| `1025` | 美的空气净化器 | switch, faultDetection | airPurifying, pm2p5, wind |
| `103G` | 生迪Wi-Fi智能球泡灯W11-C21 | switch, brightness | delay |
| `103K` | 美的智能吸尘器VR1716 | cleanerRobot, faultDetection | cleanRecord, edge, hepa, roll |
| `103L` | 美的智能吸尘器VR1717 | cleanerRobot, faultDetection | cleanRecord, edge, hepa, roll |
| `103S` | 欧普蓝牙开关OPLYKG | battery, faultDetection | button |
| `103T` | 欧普蓝牙筒灯OPLYTD | switch, brightness | relativeDelay |
| `103X` | 国投主控2路开关2LA | switch01, switch02 | — |
| `103Z` | 国投一路调光1LT | switch, brightness | — |
| `1044` |  | motor, openLevel | — |
| `1047` | 国投紧急按钮SOS | pushButton, battery | — |
| `1049` |  | switch, temperature | elecHeater, music |
| `104B` | 国投温湿度传感器THC | airDetector, battery | — |
| `104S` | Wulian智尚二路开关 | switch01, switch02 | — |
| `104W` | 汉德森Wi-Fi信号放大吸顶灯 | switch, brightness | delay |
| `1051` | 瑞晶新风RAC-1 | switch, faultDetection | freshAir, wind |
| `1053` | 瑞晶地暖RAC-3 | switch, temperature | floorHeating |
| `1057` | 瑞晶布帘RAL-4 | motor, openLevel | — |
| `1058` | 瑞晶纱帘RAL-5 | motor, openLevel | — |
| `105A` | 杜亚电动窗帘DH3 | motor, openLevel | — |
| `105B` | 杜亚电动窗帘DH5 | motor, openLevel | — |
| `105C` | 杜亚电动窗帘DH7 | motor, openLevel | — |
| `105K` | 飞利浦HUE网桥 | discovery, faultDetection | — |
| `105O` | 小米多功能网关 | discovery, faultDetection | — |
| `105Q` | 小米门窗传感器 | cct, battery | doorSensor |
| `105V` | TPLink白灯 | switch, brightness | — |
| `105X` | LIFX 彩灯 | switch, brightness | relativeDelay |
| `1064` | 飞比门磁传感器NDOS107G-M2 | cct, battery | doorSensor |
| `1065` | 飞比烟雾传感器NSMF106W-M2 | smoke, battery | — |
| `1067` | 飞比智能窗帘TZT2118W-T1 | motor, openLevel | — |
| `1069` | 顺舟门窗磁SZ09-(05) | cct, battery | doorSensor |
| `106A` | 顺舟燃气报警SZ09-(02) | smoke, battery | — |
| `106D` | 顺舟窗帘电机SZ09-(18) | motor, openLevel | — |
| `106E` | 顺舟烟雾传感器SZ09-(11) | smoke, battery | — |
| `107M` | 空气堡智慧新风系统NEX-360H | heat, airDetector | freshAir, screen, hepa, mediumFilter, primaryFilter, ozoneFilter, faultCode, devOta |
| `108Q` | 西睿空气检测蓝盒子 | airDetector, battery | PM25LevelRange, HCHOLevelRange |
| `108R` | 西睿空气检测红盒子 | airDetector, battery | PM25LevelRange |
| `108T` | 720全效空气净化器 | switch, faultDetection | airPurifying, pm2p5, wind, filterElement |
| `108U` |  | switch, faultDetection | airPurifying, wind, filterElement |
| `108X` | 公牛WiFi智能插座（基础V2版） | switch, powerSupply | delay, timerID |
| `112F` | 博泰智能插座SK505W | switch, backlight | delay, timerID |
| `113D` | 豪恩温湿度传感器 | airDetector, battery | — |
| `113E` | 豪恩多功能网关 | discovery, light | alertor, bell, voiceMessage, prompt, devOta |
| `113L` | 汇泰龙智能指纹锁 | lockStatus, battery | keyOperate, keyList, userList, publicKey, tempCode, doorbell, lockEvent, lockAlarm, wakeup, settingSwitch |
| `115M` | HDL灯光控制器 | switch, brightness | — |
| `115O` | HDL空调 | switch, temperature | airConditioner, wind |
| `115U` | 空气堡智慧新风系统ZEN-160H | heat, airDetector | freshAir, screen, faultCode |
| `117Q` | A-OK智能开合帘电机 | mode, opener | reversing |
| `118H` | 箭牌智能坐便器 | setting, switch | device_status, usermodel, warning, deviceupdate, netinfo |
| `120N` | 海令智能温湿度传感器 | airDetector, battery | — |
| `120Q` | 海令智能烟感报警器 | smoke, battery | — |
| `120Y` |  | motor, openLevel | — |
| `121B` | 海令智能开关面板 | switch01, switch02 | — |
| `122D` | 调光控制盒 | switch, brightness | — |
| `122W` | 品多智能指纹门锁H1 | battery, discovery | smartLock, lockAlarm, account, event, faultcode |
| `122X` | 二位免零线智能开关 | switch01, switch02 | switchLable01, switchLable02 |
| `123E` | 一位免零线调光开关 | switch, brightness | switchLable |
| `123R` | SONOFF TX2C 智能墙壁开关 | switch1, switch2 | switchOn, switchOff, delay, powerLight, hideSwitch, startup1, startup2, pulseSwitch1, pulseLength1, pulseSwitch2, pulseLength2 |
| `133P` | FSL单色智能天花灯 | switch, brightness | delay |
| `134F` | 祝眠白噪音暖光灯 | switch, brightness | delay, WindSpeed, FanSwitch |
| `135U` | 流光开关二联 | switch01, switch02 | lightMode01, lightMode02, colour01, colour02, backlight01, backlight02, memoryState |
| `137J` | 祈禧智能即热饮水吧YR-25C208 | switch, deviceStatus | setUpWater, dataWater, waterCond, filterElement, breakdown |
| `138F` | 大宇电风扇 | mode, speed | binarySwitch, swayLeftRight, onOffLight, endTime |
| `138S` | 微虎个人冷风扇 | mode, speed | binarySwitch, consumables |
| `140B` | CM智能窗帘电机 | mode, opener | Setting |
| `140F` | 控客智睿主机 | disSwitch, discovery | — |
| `140J` | 控客二路灯光面板 | switch01, switch02 | — |
| `141R` | 杜亚智能百叶DM25 | opener, sunSwitch | tilt, schedule |
| `141W` | 杜亚智能百叶DM35 | opener, sunSwitch | tilt, schedule |
| `152F` | 平头熊移动插座(WIFI) | switch, backlight | delay |
| `153Y` | 平头熊智能窗帘电机 | mode, opener | Curtainzfz, Curtainjz |
| `155V` | 欧派纯水机 | status, faultDetection | outputTds, filterElement1, filterElement2, filterElement3, filterElement4 |
| `157Y` | 威廷智能双开Wi-Fi | switch1, switch2 | — |
| `162L` | 创明智能窗帘 | mode, opener | Changedirection, EnHandtomove |
| `163O` | 窗帘电动轨道 | mode, opener | — |
| `163S` | 维尔森VERSON智能窗帘 | action, opener | — |
| `164A` | 智能双开开关 | switch1, switch2 | — |
| `164E` | 达伦护眼台灯T1 | switch, brightness | delay, classroom, WIFIledSwitch |
| `164V` | 力博得智能声波牙刷 星芒 | status, mode | brushingHistory , misicState, brushScore, brushDay |
| `170W` | 720 全效空气净化器 S(C400) | switch, faultDetection | airPurifying, pm2p5, wind, filterElement |
| `171Y` | 阿乐乐可模方插座智能家居 | switch, memorySwitch | delay |
| `174O` | 平头熊智能86插座 | switch, backlight | delay |
| `175S` | 平头熊二键开关WIFI | switch1, switch2 | — |
| `175U` | 奥普浴霸轻智 | mode, lightSwitch | leftTime, NightLight |
| `177T` | VANOW智能办公杯 | battery, temp | reminder, charge, lightTime, tds |
| `178F` | 居意电动窗帘 | mode, opener | State |
| `182Z` | 达伦护眼台灯 | switch, brightness | delay, classroom |
| `183D` | 噼啪智能双开开关 | switch1, switch2 | — |
| `200G` | 麦乐克紧急按钮 | pushButton, battery | button |
| `200P` | 麦乐克烟雾传感器 | alarm, battery | Error, TamperAlarm |
| `200T` | 麦乐克人体传感器 | status, battery | motionDetected |
| `200Y` | 麦乐克水浸传感器 | alarm, battery | — |
| `2025` | 酷轻松石墨烯手部按摩仪 | switch, workStatus | Heating, GenderSelection, Mode, Battery, workingTime |
| `202O` | 长虹8809浴用加热器_足浴器 | switch, massage | commonFaultDetection, stayTime, ozone, bubble, operateTemperature, temperatureDIY, leftTimeDIY |
| `202U` | 长虹8818浴用加热器_足浴器 | switch, massage | commonFaultDetection, countdown, surf, operateTemperature, modelDIY, temperatureDIY, leftTimeDIY |
| `2035` | 卡赫智能净水器 600G | switch, status | inputTds, outputTds, purifyWater, filterElement1, filterElement2, filterElement3, contWater |
| `203I` | 鸿雁智能插座 | switch, backlight | delay, protect, switchLock |
| `203M` | MPE三人沙发S005 | legControl, modeSelect | — |
| `203N` | 铂金系列白色零火线双路灯控面板 | switch01, switch02 | — |
| `204U` | 便携式深层肌肉按摩仪 | switch, gear | commonFaultDetection, LifeTimer, CountDown, Power |
| `205U` | JoinOne亲肤暖雾加湿器 | switch, faultDetection | Timer |
| `206A` | 立久佳跑步机 | switch, intensity | tempo |
| `206P` | 欧智通-智能吸顶灯 | switch, brightness | — |
| `208K` | 左点小艾3代智能艾灸盒 | switch, commonMode1 | partingmode, keylock, conventionalmode, Timesetting, Lowbattery, hotmode, Temperaturesetting, timeremaining, comfortablemode, dumpenergy, screenswitch |
| `208Z` | 酷轻松智能发热手套 | switch, targetTemperature | workstatue, Temperature, workingTime |
| `2091` | 酷轻松石墨烯发热围巾 | switch, heat | timerlabel, temprature, workstatue |
| `2094` | 松堡王国儿童智能安睡枕 | status, battery | led, Power, RealtimeRR, RealtimeHR |
| `20BB` | 希影智能投影仪L12 | switch, volume | arrow, system |
| `20C0` | 云康宝筋膜枪 | switch, gear | informationdisplay, realtimestatus, Timing |
| `20DF` | 永林单色调光器 | switch, brightness | — |
| `20DJ` | 博联智能插座SP4-HL | switch, memorySwitch | — |
| `20FL` | 新日电动车F5 | switch, alarm | OTA, remainEle, powStatus, remainKm, carLock, openSeat, NFC, diagnosis |
| `20FN` | 海令单路调光器 | switch, brightness | — |
| `20G4` |  | mode, opener | — |
| `20GO` | 摩根调光灯 | switch, brightness | — |
| `20GQ` | 360扫地机器人X90 | status, action | — |
| `20HW` | 达伦自然光护眼台灯 | switch, brightness | delay, classroom |
| `20J6` | 咪呵智能窗帘电机 | mode, opener | Curtainzfz, Curtainjz |
| `20J7` | 米亚智能窗帘电机 | mode, opener | Curtainzfz, Curtainjz |
| `20K5` | 控客紧急呼叫按钮 | pushButton, battery | — |
| `20L1` |  | mode, opener | — |
| `20Q8` | AD999筋膜枪 | gear, connectionStatus | commonFaultDetection, UseTutorial, dataStatistics, LifeTimer, Power, CountDown |
| `20SL` | 欧派燃气灶 | switchLeft, switchRight | fireLeft |
| `20SY` | 奥克斯筋膜枪 | start, gear | commonFaultDetection |
| `20UF` | 立久佳跑步机 | switch, intensity | tempo |
| `20VD` | MPE单人沙发 | headControl, legControl | M1, M2, remember |
| `20VG` | MPE三人沙发 | headControl, legControl | M1, M2, remember |
| `20XP` | 控客-星空双路灯控面板 | switch1, switch2 | — |
| `20Y8` | 控客-星空双路窗帘面板 | mode01, mode02 | — |
| `20YT` | 控客-烟雾报警器 | alarm, battery | commonFaultDetection, dismantle |
| `20ZB` | MBH跑步机 | switch, speed | dist, kcal |
| `20ZS` | 控客-双路灯控模块 | switch1, switch2 | — |
| `210D` | 左点颈椎按摩仪 | switch, commonMode1 | — |
| `2133` | Dual料理烧烤微波炉 | childlock, doorStatus | myPreTimeStart, weight, myPresetSwitch, combo, recipes, defrost, grill, microwave, playSwitch, workaction, myWorkTime, workstatus, turnRemind |
| `2136` | 左点腰椎按摩器 | switch, commonMode1 | Lowbattery, dumpenergy, timeremaining, Timesetting, Hotcompressgear, Strengthofgear, Massagemode, Pressthemode, Kneadingmode |
| `213W` | 西顿调光模块 | switch, brightness | — |
| `2141` | 西马智能便盖 | massage, waterLevel | filterLeftlife, eco, onSeat, longSeat, nozzleSelf, washMode, led, sound, longSeatOPT, seatLevel, womenTime, warn, hipTime, power, nozzlePostion, waterPress |
| `215D` | 西顿恒压调光模块 | switch, brightness | — |
| `215R` | 紧急按钮 | pushButton, battery | — |
| `215U` | 漏水检测器 | alarm, battery | — |
| `2162` | 智能窗帘电机 | mode, opener | — |
| `2164` | 触控双路窗帘电机控制面板 | mode, outMode | — |
| `216C` | Dual料理微波炉 | childlock, doorStatus | weight, myPresetSwitch, myPreTimeStart, recipes, defrost, microwave, playSwitch, workaction, myWorkTime, workstatus |
| `2174` | HEIMAN智能燃气报警器 | alarm, selfCheck | commonFaultDetection |
| `217Q` | 控客-肖邦二路灯光面板 | switch01, switch02 | — |
| `217U` |  | mode01, mode02 | — |
| `2184` | HEIMAN智能紧急按钮 | pushButton, battery | — |
| `219G` | FSL智曜读写台灯 | switch, brightness | tomatoClk, delay |
| `21A1` |  | alarm, faultDetection | — |
| `21B7` | 单键智能开关面板时尚版 | switch, backlightMode | — |
| `21B8` | 单键智能开关面板尊享版 | switch, backlightMode | — |
| `21BF` | 圆和一路智能开关 | switch, switch1 | — |
| `21BM` | 云起水浸感应器 | status, battery | — |
| `21DD` |  | mode, opener | — |
| `21DI` |  | battery, luminance | motionDetected |
| `21EA` | 觅石超声波清洗机 | switch, commonMode1 | — |
| `21ED` | JW智能照明调光灯 | switch, brightness | — |
| `21ER` | JW智能地暖 | switch, temperature | — |
| `21G9` | JW门磁 | doorEvent, status | — |
| `21GJ` | JW空气检测E型 | temperature, humidity | — |
| `21GL` | JW智能开关2键型 | switch1, switch2 | — |
| `21JB` | 阳光照明灵睿智能灯泡调光版 | switch, brightness | delay |
| `21JH` | 新日电动车XC3 | switch, alarm | OTA, remainEle, diagnosis, powStatus, carLock, remainKm |
| `21JP` | 西顿杀菌厨卫灯 | switch, lightMode | — |
| `21LB` | 永林恒压调光驱动 | switch, brightness | — |
| `21LE` | 米立2路窗帘控制面板 | mode1, mode2 | — |
| `21LG` | 米立2路智能开关面板 | switch1, switch2 | — |
| `21LK` | 米立紧急报警按钮 | pushButton, battery | — |
| `21LL` | 米立红外探测器 | battery, tamperAlarm | motionDetected |
| `21LO` | 欧普智能紫外杀菌灯 | switch, commonMode1 | delay, commonFaultDetection, TimeLeft |
| `21LY` | 平头熊智能卷帘电机 | action, opener | rotation, calibration |
| `21M4` | 酷轻松石墨烯智能艾灸仪 | switch, targetTemperature | Battery, Temperature, workingTime |
| `21NQ` | sraum智能家居网关 | switch, discovery | — |
| `21NZ` | A.O.史密斯中央净水机 | status, faultDetection | purifyWater, flushTime, useTime, waterSpeed, filterElement |
| `21OA` | A.O.史密斯反渗透净水机 | status, faultDetection | purifyWater, flushTime, useTime, waterSpeed, filterElement |
| `21P0` | 中菱智能卷帘电机 | action, opener | rotation, calibration |
| `21P1` | 致尚智能窗帘电机 | mode, opener | Curtainjz, Curtainzfz |
| `21PC` | 调光灯（照明调光器） | switch, brightness | — |
| `21PQ` | 水浸传感器 | status, battery | — |
| `21PR` | 烟雾传感器 | smoke, battery | — |
| `21Q8` | 科创者智能窗帘电机 | mode, opener | Curtainzfz, Curtainjz |
| `21SD` | RGB调色灯带（灯带调光器） | switch, colour | — |
| `21SF` | RGBW调色灯带（灯带调光器） | switch, colour | — |
| `21U1` | 孩视宝智能面加环读写台灯 | switch, brightness | TimedReminder, CurrentColorTempurature, CurrentBrightness, SmartLight, NaturalSleep, NightlightMode, cctmode |
| `21U2` | 孩视宝智能长条形落地灯 | switch, brightness | NaturalSleep, FragmentPractice, FocusOnPractice |
| `21UK` | 达伦自然光台灯T3 Pro | switch, brightness | WithSleepMode, AutoAMode, ColorTempStep, WIFIledSwitch, classroom |
| `21US` | 鸿雁16A智能插座 | switch, backlight | delay, switchLock, protect |
| `21UZ` | 慕村智能水离子高速吹风机S1 | commonMemorySwitch1, windspeed | Customcontrol, airtemperature, hairclassroom, Muchwindscene, Usefirstthree, Moderatehaircare, Personalityadaptation, Usetime |
| `21V4` | 瑞晶空气净化器 | switch, fan | — |
| `21V8` | 瑞晶四合一传感器 | temperature, humidity | PM2.5, CO2 |
| `21VX` | 瑞晶亮度感应器 | luminance, battery | — |
| `21W2` | 瑞晶调光灯 | switch, brightness | — |
| `21WF` | 雷士护眼台灯-米娜 | switch, brightness | delay, Breaks, RestTime |
| `21X9` | 海盐电热热敷垫 | switch, status | realtime, control |
| `21XI` | 瑞晶红外探测器 | battery, status | motionDetected |
| `21XM` | 瑞晶水浸探测器 | alarm, battery | — |
| `21XP` | 瑞晶报警器 | switch, battery | — |
| `21XQ` | 瑞晶烟雾探测器 | alarm, battery | — |
| `21XW` | 水立洁净水器 | status, faultDetection | filterElement1, filterElement2, filterElement3 |
| `21YX` | 瑞晶背景音乐 | switch, Volume | SoundChannel, CutOver, Play |
| `21Z6` | P50 Pro环闪保护壳 | switch, brightness | Devicestatus, Oneclicklight, Callflash, Colortemperature, Entertainmentlighting, Firmwareupdate, conectstatue |
| `220W` | 智能毛巾烘干机 | switch, temperature | WorkTimer, Mode, WorkState, TimeCountDown, TimeFormat |
| `2212` | REMAC+86型嵌入式网关 | discovery, alarm | alertor, devOta |
| `221F` |  | opener, mode | — |
| `221H` |  | mode1, mode2 | curtain1, curtain2 |
| `221J` |  | switch, temperature | — |
| `221O` |  | alarm, battery | — |
| `221Q` |  | alarm, battery | — |
| `221R` |  | switch, fan | — |
| `223W` | 鸿蒙智选儿童智能牙刷 | status, mode | — |
| `2241` | 杜亚智能窗帘HL1 | mode, opener | commonFaultDetection |
| `224B` |  | switch, brightness | — |
| `224C` |  | switch, brightness | — |
| `224R` |  | switch, temperature | — |
| `225B` | i-Respix-等离子甲醛清除机 | switch, commonMode1 | Led |
| `226H` | 门磁 | doorEvent, status | — |
| `227U` | 亚摩斯睿雅零火开关单键 | switch, brightness | — |
| `22C7` | 本博按摩枕 | switch, mode | countdown, vibrationMassage, warmCompress, speedRegulation, remainingTime |
| `22CX` | 新日电动车F3 | switch, alarm | OTA, NFC, diagnosis, remainKm, remainEle, openSeat, carLock, powStatus |
| `22D5` | 捷昌智能窗帘 | action, opener | — |
| `22G4` | 新日电动车MIKU1 | switch, alarm | diagnosis, carLock, powStatus, OTA, remainKm, remainEle |
| `22G5` | 新日电动车K2 | switch, alarm | remainKm, remainEle, carLock, OTA, diagnosis, powStatus |
| `22H8` | 新日电动车XO2 | switch, alarm | carLock, remainEle, powStatus, diagnosis, remainKm, OTA |
| `22RG` | 北冥小鱼智能跳绳S1 | mode, battery | count, calorie, ID, time |
| `22VM` | 亚摩斯智能立式暖风机 | switch, gear | timingOff, snaking |
| `22ZK` | Evoyo水浸传感器 | alarm, battery | — |
| `22ZV` | Evoyo一路调光器小模块 | switch, brightness | — |
| `22ZX` | Evoyo窗帘电机 | action, opener | — |
| `22ZZ` | Evoyo烟雾传感器 | alarm, battery | — |
| `2300` | Evoyo门窗传感器 | status, battery | — |
| `2305` | 长虹1588浴用加热器-足浴器 | switch, massage | commonFaultDetection, countdown, leftTimeDIY, temperatureDIY, modelDIY, operateTemperature, changeModel |
| `23EH` | 颈椎按摩枕 | switch, hot | save, torce, pattern, time |
| `23GN` | 新日电动车GF6 | switch, alarm | powStatus, NFC, openSeat, carLock, remainKm, diagnosis, remainEle, OTA |
| `23VR` | 新日电动车FN3 | switch, alarm | remainKm, remainEle, OTA, NFC, carLock, openSeat, diagnosis, powStatus |
| `241B` | 长虹8558浴用加热器_足浴器 | switch, massage | commonFaultDetection, leftTimeDIY, countdown, changeModel, operateTemperature, modelDIY, temperatureDIY |
| `241D` | 达伦自然光台灯T3 RS | switch, brightness | classroom |
| `2434` | 怀里智能浴宝 | switch, temperature | DSTime, WDSet, DSFUNC, XDFUNC, HWFUNC, QNFUNC, LFFUNC |
| `246B` | 赋安烟感报警器 | alarm, battery | commonFaultDetection, remoteOperate, remoteEnable, tamper, pollute, smokeState |
| `2477` | 贝克巴斯食物垃圾处理器 | mode, switch | conserve, Reverse |
| `247A` | 唱多多小精灵麦克风MINI | volume, battery | electricity, Unconnected, Connected, Connecting, UsageScenarios, snowflake, MusicVolume, TrebleBass, Mutevoice, Specialeffects, Electronic, Reverb, Noise, TrebleBass1, VoiceVolume |
| `247H` | 卷发器-罗曼智能小花卷 | switch, workStatus | commonFaultDetection, workTime, rollDegree |
| `247P` | 电吹风VC精华智能款 | status, mode | CustomerService, motorspeed, Airshow, Drynessratedisplay, temperaturedisplay, UsingRecord, VCUsingTime |
| `247U` | 万播投影仪 | controlKey, volSwitch | — |
| `24B1` | 直发梳-罗曼智能小青梳 | switch, workStatus | commonFaultDetection, tempSet, workTime |
| `24DM` | 亚摩斯读写台灯 | switch, brightness | tomatoClk, progressTurnOff |
| `24FQ` | 新日电动车UF3 | alarm, switch | diagnosis, NFC, carLock, powStatus, remainKm, remainEle, OTA |
| `24G6` | 新日电动车QM2 | switch, alarm | diagnosis, NFC, OTA, remainEle, carLock, powStatus, remainKm |
| `24HL` | FOOXMET智能温控围巾 | switch, temperature | commonFaultDetection, tempDown |
| `24ND` | 720净饮一体机 | faultDetection, childLock | inputTds, outputTds, commonFilterElement1, temp1, FilterLife, uvEn, cleanPeriod, cleanEn, ledOffTime, speaker, cup, winter |
| `24NE` | 希影智能投影仪H9 | switch, volume | arrow, system |
| `24NF` | 希影智能投影仪P8 | switch, volume | arrow, system |
| `24RX` | 物生物H-think云想保温杯 | sterilize, battery | alarmTime1, more, signed, find, nodisturbance, TDS, intake, watertemp, drinkwaterTarget, drinkwaterHistory, smartreminds, temperatureArea |
| `24T9` | OES按摩枕 | switch, mode | remainingTime, speedRegulation, warmCompress, vibrationMassage, cuntdown |
| `24WB` | FOOXMET智能温控马甲 | switch, temperature | commonFaultDetection, tempDown |
| `24WC` | FOOXMET 智能温控裤 | switch, temperature | commonFaultDetection, tempDown |
| `24WD` | FOOXMET智能温控服 | switch, temperature | commonFaultDetection, tempDown |
| `24X6` | 赋安燃气报警器 | alarm, volume | commonFaultDetection, remoteOperate, sensorState, concn |
| `24YL` | 全向麦克风 | switch, standbyTime | abnormalPrompt, speakerVolume, batteryLevel, micMute, devicePromptTone, denoise |
| `2591` | SHOEKONG智能运动包 | ChargeState, switch | TaskLeftTime, RemainingCapacity, zipperStatus, SetMode, SetUvSate, WorkTime, GetAllStatus, RingLampBrightness |
| `25B7` | 三耐科智能擦窗机器人 | switch, mode | devState |
| `25BF` | MPE乳胶枕 | status, battery | power, led, realtimeRR, realtimeHR |
| `25BR` | 沃荷智能枕 | status, battery | power, led, realtimeRR, realtimeHR |
| `25BS` | 斯尼恩智能枕 | status, battery | RealtimeRR, RealtimeHR, power, led |
| `25DD` | 富光智联保温杯 | battery, temp | reminder, lightTime, charge, tds |
| `25EN` | 达伦自然光台灯T3E | switch, brightness | classroom, WIFIledSwitch |
| `25GH` | 亚摩斯窗帘电机WiFi版 | action, opener | — |
| `25H8` | 俞福智能枕 | status, battery | power, led, realtimeRR, realtimeHR |
| `25HQ` | 九阳智能商务保温杯 | battery, temp | lightTime, charge, reminder, find, tds |
| `25NF` | VSITOO轻巧抑菌智能保温杯 青春版 | temp, battery | charge, reminder, tds, lightTime |
| `25PN` | 皇家惠人智能水暖毯 | switch, commonMode1 | commonFaultDetection, timeCTRL, temperatureCTRL, display |
| `25US` | 音络全向麦克风 | switch, mute | BatteryStatus, voiceminus, voiceplus |
| `261F` | Freya床头灯 | switch, brightness | Sleep, WakeUp, Piano |
| `264A` | 飞利浦会议麦克风PSE0500 | switch, micMode | ConnectionStatus, Instructionsforuse, Volumeadjustment |
| `264B` | 飞利浦会议麦克风PSE0540Pro | switch, micMode | ConnectionStatus, Instruction, Volumeadjustment, Electricity |
| `26FB` | 暖桌宝 | switch, temperature | Sedentarytone, Sedentaryremindertime, Drinkingtone, watertime |
| `26G2` | 捷昌智能百叶帘电机 | action, opener | openerAngle |
| `27GC` | 哈鹰H10 | switch, commonMode1 | commonFaultDetection, Zerostart, Cruise, Speed, Mileagetotal, Headlight, Mileage, Battery |
| `27M1` | 创维宝马系列冰箱 | refrigerator, freezer | Cooler, Mode, RefrigeratorSwitch |
| `27NI` | 阳光博鸿读写台灯 | switch, brightness | — |
| `27XN` | MARTUBE暖桌宝 | switch, temperature | watertime, Drinkingtone, Sedentaryremindertime, Sedentarytone |
| `27XR` | 紫外杀菌灯 | switch, childlock | workstatus, uvtimemode, uvtimeleft |
| `284J` | 电吹风VC精华二代(智能款) | status, mode | VCreset, vcTime, airVolume, dryingRate, temperatureShow, motorSpeed |
| `285N` | 暖宫腰带 | switch, temperature | Vibrationgear |
| `28DY` | 博孚梦幻帘 | action, opener | dimmer |
| `28UW` | 洒拖F7智能拖地吸尘器 | status, battery | workTime, leftTime, filterElement, chargLeftTime, landLight, waterSpray, module, voice |
| `28Y8` | 大鱼智能电动车 | speed, lock | cruise, unitswitching, batterystatues, singlemileage, initiatingmode, changepassword, totalmileage, headlightswitch, speedset, selftestdata |
| `2900` | 觅泛QM23迷你筋膜枪 | battery, gear | devicestat, battalarm, chargstat, usetime |
| `2924` | 萌动温控器 | switch, status | tempHeat, tempCool, disTemp, fanMod |
| `2934` | 大一指纹保管箱 | battery, lockState | event, rmRes, lockAlarm |
| `29AS` | 赛诺多效护颈智能枕 | status, battery | HR, realtimeRR, power, led |
| `29DT` | 小适负离子电吹风(智能款) | status, mode | Upgrade, Feedback, Service, Class, MotorSpeed, AirVolume, AnionTotal |
| `29DV` | 小适恒温电吹风(智能款) | mode, status | Temp, Dryingrate, AirVolume, Class, AnionTotal, MotorSpeed, Service, Upgrade, Feedback |
| `29F4` | 红外幕帘传感器 | switch, alarm | — |
| `29I9` | 乐歌电动升降桌ET223 | action, childLockSwitch | commonFaultDetection, heightfour, heightthree, reporthight, heighttwo, ctrlhight, month, day, heightone, line |
| `29LH` | HUAWEI Mate50 Pro 环闪保护壳 | workStatus, brightness | colorTemperature, control, sceneLightEffect, specialSet, firmwareUpgrade |
| `29LI` | HUAWEI Mate50 环闪保护壳 | workStatus, brightness | colorTemperature, specialSet, sceneLightEffect, firmwareUpgrade, control |
| `29M4` | 未来侍酒师智能品酒礼盒套装 | faultDetection, status | commonFilterElement1, commonFilterElement2, power, resettime |
| `29MD` | 智能饮水机 | faultDetection, temperature | output, currentTemp, ChildLock, workstatus, orderwater, daypower, daywater, TapOn |
| `29SM` | 智能电动水阀 | switch, faultDetection | rotation |
| `29T9` | 智能电动水阀 | switch, faultDetection | rotation |
| `29UP` | 攀高智能颈椎按摩仪 | switch, battery | remindWindow, state, Time, Heat, Level, Mode |
| `29UZ` | 九牧智能浴霸 | Switch, temperature | commonFaultDetection, control |
| `29VT` | 暖通网关MH2 OS | gatewayAction, faultDetection | acList, heaterList, freshAirList, port1protocolList, acGroupList, heaterGroupList, freshAirGroupList, port2protocolList, 485NetInfo, vrvProtocol, connectMode, backupData, backup, generalList, generalGrouplist, reboot, automaticGroup |
| `29X5` | 欧井智能除湿机OJ-136E | switch, childLockSwitch | commonFaultDetection, SetDUM, Countdown, SetSpeed, Purify, Temp, HUM, SetMode |
| `29X8` | 欧井智能除湿机OJ-211E | switch, childLockSwitch | commonFaultDetection, SetDUM, Countdown, SetSpeed, Purify, Temp, HUM, setMode |
| `29XC` | 欧井智能除湿机OJ-501E | switch, childLockSwitch | commonFilterElement1, commonFaultDetection, Countdown, SetDUM, Temp, SetSpeed, SetMode, HUM, Purify |
| `2A00` | 背景音乐主机 | switch, colour | — |
| `2A07` | 艾特智能网关 | switch, discovery | — |
| `2A1U` | 凯胜颈椎按摩器 | switch, gear | Methodsthelength, methods, Hotcompress, DIY, Againstthpattern, Acupuncturemodel, Scrappingmode, automaticmode, currentpower, hottemperature, resttime |
| `2A8L` | sraum1路窗帘面板 | switch1, switch2 | close, open, scene4, scene3, scene2, scene1 |
| `2A8R` | sraum2路开关面板 | switch1, switch2 | scene4, scene3, scene2, scene1 |
| `2AAK` | 艾特双键开关 | switch1, switch2 | — |
| `2AAY` | VSITOO不锈钢智能保温杯 | temp, battery | TDS, charge, lightTime, reminder |
| `2ABJ` | 艾特四键情景面板 | switch1, switch2 | scenes |
| `2ABT` | 永林调光驱动 | switch, brightness | — |
| `2ACH` | 晚安智能床垫 | status, action | bedStatus, sleep |
| `2ACW` | 推窗器 | action, opener | — |
| `2ACY` | 卷帘 | action, opener | — |
| `2ACZ` | 卷帘（高扭矩版） | action, opener | — |
| `2ADE` | VSITOO智能商务保温杯 | temp, battery | alarmTime1, tds, charge, lightTime |
| `2ADR` | 酷轻松石墨烯智能睡眠枕 | status, heat | InterferenceSwitch, Respiratory, SleepReport, Power, Internet, Body, statue, Rate, Strength |
| `2AE0` |  | switch, brightness | fadeTime |
| `2AE7` |  | pushButton, battery | — |
| `2AE9` |  | alarm, battery | — |
| `2AK2` | 艾特门磁传感器 | doorEvent, status | — |
| `2AK8` | 艾特新风控制器 | switch, fan | — |
| `2ALB` | 飞利浦反渗透净水机-AUT2016 | status, faultDetection | outputTds, filterElement1, filterElement2, FilterReset2, ResetRecord1, Rinsefunction, ResetRecord0, FilterReset1 |
| `2AN8` | 鸿雁门窗传感器B款 | doorEvent, status | — |
| `2ANH` | 杜亚智能窗帘DT270 | mode, opener | commonFaultDetection |
| `2ANI` |  | switch, fan | — |
| `2ANK` |  | switch, temperature | — |
| `2ANZ` | 领普单键单火开关MESH | switch, mode1 | button1 |
| `2AOQ` | 杜亚智能窗帘DH6 | mode, opener | — |
| `2AOZ` | 鸿雁单路智能开关模块 | switch, indicator | — |
| `2AP1` | 鸿雁单键智能开关U2 | switch1, indicator | — |
| `2AQO` | 鸿蒙智选 智能台灯2i | switch, brightness | — |
| `2AQZ` | 调光灯带（灯带调光器） | switch, brightness | — |
| `2ARO` | Sleepace享睡RestOn智能睡眠监测器 | status, workStatus | smartscene, historyData, environment, features, tur, realData |
| `2ASS` | 创明智能窗帘 | mode, opener | workmode, workstatus |
| `2AT0` | 倍轻松眼部按摩器 | switch, hot | firmware, awakemode, sleepmode, workmode, music, timing, eyesightmode, diastolicmode, cyclemode |
| `2AU0` | 致尚智能卷帘电机 | action, opener | rotation, calibration |
| `2AUJ` | 嘟嘟智能插座 | switch, backlight | electric, delay, TotalPower, power |
| `2AV0` | 米亚智能卷帘电机 | action, opener | rotation, calibration |
| `2AWD` | 飞利浦反渗透净水机-AUT2116 | status, faultDetection | outputTds, filterElement1, filterElement2, ResetRecord1, ResetRecord0, Rinsefunction, FilterReset2, FilterReset1 |
| `2AWE` | 飞利浦反渗透净水机-AUT3016 | status, faultDetection | outputTds, filterElement1, filterElement2, ResetRecord0, Rinsefunction, ResetRecord1, FilterReset1, FilterReset2 |
| `2AWF` | 飞利浦反渗透净水机-AUT3116 | status, faultDetection | outputTds, filterElement1, filterElement2, ResetRecord1, ResetRecord0, Rinsefunction, FilterReset2, FilterReset1 |
| `2AX0` | 创明智能窗帘 | action, opener | rotation, LimitSet |
| `2B2R` | FSL智搏读写台灯 | switch, brightness | tomatoClk, delay, progressTurnOff |
| `2B4B` | 探梦者智能滑板车 | commonMemorySwitch1, speed | morefunction, checkcar, speedunite, speedstall, cruise, color, TextView, StraingMethod, steplight, carlamp, totalstrip, Thistrip, Batteryleve, lockon, lockoff |
| `2B59` | MixSwitch超级智能开关-二开 | switch1, switch2 | — |
| `2B8L` | 优家明创智能毛巾机 | switch, temperature | TimeCountDown, WorkTimer, TimeFormat, Mode, WorkState |
| `2B92` | 凯胜眼部按摩器 | switch, switch | — |
| `2BDD` | 单色温灯带调光驱动器 | switch, brightness | — |
| `2BDP` | 壁挂式水浸传感器套装 | switch, alarm | — |
| `2BE6` | 麦乐克红外人体移动传感器 | status, battery | motionDetected |
| `2BE7` | 麦乐克水浸传感器 | alarm, battery | — |
| `2BF3` | 门磁传感器套装 | switch, status | — |
| `2BN4` | 映趣剃须刀 | switch, mode | NetworkStatus, history, CleanRemind, BatteryLevel |
| `2BOE` | 堡丽调光灯（照明调光器） | switch, brightness | — |
| `2BOG` |  | switch, brightness | — |
| `2BOH` |  | switch, brightness | — |
| `2BOJ` | 堡丽调光灯带（灯带调光器） | switch, brightness | — |
| `2BOL` | 堡丽RGB调色灯带（灯带调光器） | switch, colour | — |
| `2BON` | 堡丽RGBW调色灯带（灯带调光器） | switch, colour | — |
| `2BOU` |  | switch, temperature | — |
| `2BRM` | 奥佳华颈椎按摩仪 | switch, heat | time, voice, strength, classic, surTime, suspend |
| `2BT5` | 一维香薰机 | switch, luminance | atomization, time |
| `2BV9` | 乐骑智能儿童滑板车 | switch, commonExecution1 | statistic |
| `2BVL` | 噼啪智能窗帘电机 | mode, opener | Curtainzfz, Curtainjz |
| `2C4Z` | MBH ST跑步机 | switch, speed | dist, incline, kcal |
| `2C5P` | 堡丽卷帘 | action, opener | — |
| `2C5Q` | 堡丽卷帘（高扭矩版） | action, opener | — |
| `2C5R` | 堡丽开窗器 | action, opener | — |
| `2C7V` | 西蒙二位智能开关 | switch1, switch2 | BackLightMode |
| `2C82` | 西蒙10A智能插座 | switch, faultDetection | power, electric, BackLightMode |
| `2C83` | 西蒙二位智能窗帘开关 | mode01, mode02 | opener01, opener02, CurtainDirection2, MotorConfig2, MotorConfig1, CurtainDirection1 |
| `2C85` | 西蒙二位智能调光开关 | switch1, switch2 | LedPosition2, LedPosition1, BackLightMode |
| `2CDL` | ACEMATIC新风模块 | switch, fan | — |
| `2CDN` | ACEMATIC调光灯 | switch, brightness | — |
| `2CJR` | 杜亚智能窗帘 | mode, opener | commonFaultDetection |
| `2CK0` | 叶绿体单火二路墙壁开关 | switch1, switch2 | — |
| `2CL5` | ACEMATIC音乐主机 | volume, musicPlay | — |
| `2CMK` | 艾多智能窗帘电机 | mode, opener | Curtainjz, Curtainzfz |
| `2CPV` | 法洁奥电动牙刷 Marble-01 | status, mode | NA6, NA5, NA4, NA3, NA2, NA1, NA |
| `2CQ8` | 吸顶式温湿度传感器 | temperature, humidity | tempReportSetting, humidityReportSetting |
| `2CQG` | 吸顶式红外人体移动传感器 | switch, status | — |
| `2CQH` | 吸顶式毫米波人体存在传感器 | switch, status | — |
| `2CTW` | 三思智能厨卫灯 | switch, brightness | — |
| `2CUG` | 喜临门智能健康枕 | status, workStatus | commonFaultDetection, realData, historyData, devVersion, devInfo, batteryInfo, updateSelf |
| `2CUS` | 麦乐克紧急按钮传感器 | pushButton, battery | — |
| `2CVH` | 双键智能开关面板时尚版 | switch1, switch2 | — |
| `2CY1` | 达伦自然光台灯T3 | switch, brightness | delay, WIFIledSwitch, classroom |
| `2CY2` | 达伦自然光台灯T3X | switch, brightness | delay, WIFIledSwitch, classroom |
| `2CZA` | MBH T跑步机 | switch, speed | kcal, dist |
| `2D53` | 精油温灸仪 | switch, temp | time, oil, BAT, HOT, EMS |
| `2D6C` | 画法几何两栖生态懒人鱼缸Pro | switch, light | feed, pump, common |
| `2D7A` | 博孚WiFi智能窗帘 | action, opener | — |
| `2DAC` | RGBW灯带调光驱动器 | switch, colour | — |
| `2DAD` | 名豆之约10A智能插座 | switch, faultDetection | realPower, electricity, chargingProtect, ElectricalProtect |
| `2DAE` | 名豆之约16A智能插座 | switch, faultDetection | realPower, electricity |
| `2DB8` | 双键86底盒开关模块 | switch1, switch2 | — |
| `2DC2` | 婴觅智能杀菌牙刷杯架 | disinfect, battery | disinfectStatus, record, warning, timing |
| `2DCB` | HEIMAN智能声光报警器 | switch, battery | alamTime |
| `2DDA` | 荣泰筋膜枪G31 | operation, mode | Battery, RPM, TIME, swtih |
| `2DDQ` | MPE三人沙发S006 | legControl, modeSelect | — |
| `2DDU` | 木有故事-小鸟智能灯 | switch, commonMode1 | color, bright |
| `2DF1` | DB913筋膜枪 | switch, gear | commonFaultDetection, UseTutorial, dataStatistics, CountDown, LifeTimer, Power |
| `2DF2` | BOBOT博宝特洗地机 | status, battery | workTime, cleanWater, sewage |
| `2DF9` | 艾诗摩尔润眼按摩仪 | mode, heat | commonFilterElement1, commonFilterElement2, commonFaultDetection, electricity, spray |
| `2DFA` | 艾诗摩尔便携式洗手仪 | workMode, mode | commonFilterElement1, commonFaultDetection, record, power |
| `2DG7` | SMOOKY筋膜枪 | switch, mode | Battery, RPM, countdown, swtich |
| `2DGG` | 达伦护眼台灯T2 | switch, brightness | delay, WIFIledSwitch, classroom |
| `2DQM` | MOK PLANET智能音乐伴眠枕 | status, workStatus | features, historyData, alarmCfg, tur, smartBt, realData, batteryInfo, updateSelf, aidmusic |
| `2DQU` | 仁豪家居智能枕 | status, battery | power, led, RealtimeRR, RealtimeHR |
| `2DRC` | 汇优尚品射频美容仪 | mode, gear | Instructions, switchStatus, remainTime |
| `2DRM` | 计客智能四子棋 | switch, battery | game, intro |
| `2DS0` | MOK PLANET智能健康枕 | status, workStatus | features, tur, realData, historyData, batteryInfo |
| `2DSB` | 拉孚一路智能开关 | switch, switch1 | — |
| `2DSC` | 四季沐歌智能马桶 | waterTemp, ECO | hipWash, womanWash, Dry, NozzleLocation, WaterGage, FanTemp, SeatTemp, ManAuto, WomanAuto, seatState, Forth, MuteMode, NightLight, OneKeyStop, LeaveSeatFlushing, Flushing, cleanRod |
| `2DV0` | 双键智能开关面板尊享版 | switch1, switch2 | — |
| `2DWQ` | 唱多多小雪人麦克风 | volume, battery | electricity, UsageScenarios, MusicVolume, VoiceVolume, Electronic, TrebleBass1, Specialeffects, Reverb, Noise, Mutevoice, TrebleBass, snowflake |
| `2DZO` | 奥克斯筋膜枪 | start, gear | commonFaultDetection |
| `2E3A` | 长虹8519浴用加热器-足浴器 | switch, massage | commonFaultDetection, countdown, leftTimeDIY, temperatureDIY, operateTemperature |
| `2E3B` | 长虹968足浴盆 | switch, massage | commonFaultDetection, leftTimeDIY, temperatureDIY, modelDIY, operateTemperature, countdown, changeModel |
| `2E3G` | 捷昌智能卷帘 | action, opener | — |
| `2E4F` | 飞乐思智能暖宫带 | switch, temperature | Fault, MODE, TIME, TEMP |
| `2E4J` | 烯时代石墨烯发热多功能暖宫带 | hot, powerswitch | ele |
| `2EJY` | 艾优儿童电动牙刷 | battery, mode | BrushingRecord, time, custom, Brushingmode |
| `2EN1` | 自动卷发器 | temp, status | commonFaultDetection, usageCount, usageTimeB, usageTimeA, time, curlsB, curlsA, intentTemp |
| `2EOI` | 律动机 | switch, mode | RecommendedGameplay, Bluetoothstatus, Voiceswitch, quantityheat, Timeremaining, Rhythmtime, timecontrl, Volumecontrol, Musicswitch, Music, Gear |
| `2F4N` | SHOEKONG智能运动包 | switch, ChargeState | RingLampBrightness, RemainingCapacity, TaskLeftTime, GetAllStatus, WorkTime, SetUvSate, SetMode, UVprotection |
| `2FHB` | 领普单键墙壁开关 | switch, brightness | — |
| `2FM9` | 友通 PM2.5检测仪 | pm25, temp | ota, commonFaultDetection, Unit, tempF, brightness01, AQI, PM10, humi |
| `2FPI` | 嘉嘉旺智能取暖茶几A330 | switch, mute | workstatus, countDown, timing, lowerGear, upperGear, fall, rise, energySaving |
| `2FSO` | 沃乐智能口袋筋膜枪蓝牙版 | gear, switch | Lowbatteryalert, Devicecharge, Totalrecord, Record, Partselection, Workstatus |
| `2G1W` | 富光梦想家智能办公杯 | battery, currentTemperature | alarmTime1, alarmTime7, alarmTime8, btConnection, alarmTime12 |
| `2G56` | 杜亚智能卷帘 | opener, action | rotation |
| `2G7S` | 氢稳富氢水杯 | battery, currentTemperature | UsageLog, Hydrogenwatertime, Customrepetition, synchronizationtime, Hydrogenproductionvalue, Hydrogenwatermeter, Hydrogencompletion, Settingstotakeeffect, Equipmentswitch, Lowpoweralarm, Atmospherelightswitch, Drinkwaterreminder, Timetoreport, repetitionfrequency, Glasslookup, Todaythecumulative, alarmTime1 |
| `2GB5` | 水浸传感器 | warterAlarm, battery | commonFaultDetection |
| `2GBJ` | 佳仁筋膜枪 | model, switch | electricity |
| `2GE7` | 门窗传感器 | doorContact, battery | commonFaultDetection |
| `2GOR` | 汉印标签打印机Q2 | printerStatus, faultDetection | printParameter, printcopies, size, connect, paper, information, kwh, Status |
| `2GVP` | 转换器(狄耐克智能插座) | switch, childLockSwitch | — |
| `2GX0` | 乐歌电动升降桌ET114 | action, childLockSwitch | commonFaultDetection, day, heighttwo, month, heightone, ctrlhight, heightfour, reporthight, heightthree, line |
| `2GXO` | AI生态枕 | battery, status | led, power, realtimeRR, HR |
| `2GYR` | Poputar 智能吉他 | mode, status | tuning, practice, learning, chord, interactive |
| `2GYT` | 皓刻电动牙刷 | mode, battery | brushingHistory, Reconnect, DeviceStatus, BatteryLevel, RemainingDaysOfBrushHead, WorkTimSetting |
| `2H4A` | 酷轻松石墨烯多功能护膝 | switch, model | Lowbattery, RemainingHours, CurrentTemperature, VibrationGear, temperatureGear, countdown, button |
| `2H4C` | 酷轻松石墨烯降温冰感防晒空调服 | gear, mode | timing, workHours, pauseState, kaiguan |
| `2H4Y` | 香百年畅享智能香薰机 | mode, switch | autoStart, near, fragSetting2, fragSetting1, margin2, margin1, timing, cycles, density, fragrance, electricity |
| `2H68` | 格林盈璐暖风机GL002 | switch, mode | Remaining, countdown, shake |
| `2H72` | 智能矫姿精灵2 | connectStatus, reminderMode | tilt, isShowTips, postureSet, powerShow, postureCorrectionCourse, myPosture, sedentary, delay |
| `2H9E` | 金莱特便携干衣胶囊 | mode, switch | — |
| `2HAH` | 康佳按摩椅KZ-RH6687 | switch, ppmMode | VibSwitch, heacushion, AirbagAuto, connect, Zero, Roll, shoulderarms, Timer, Hot, RiseDrop, Leg, TimeSurplus |
| `2HC2` | 得力智能闹钟 | humidity, temperature | devicestatus, Alarmswitch, Alarmsetting, Ringtonevolume, Snoozetimes, Timeformat, Backlightbrightness |
| `2HJ2` | 康佳按摩椅KZ-RH6699 | switch, autoMode | RiseDrop, Leg, TimeSurplus, Hot, shoulderarms, Roll, Timer, connect, Zero, AirbagAuto, heacushion, VibSwitch |
| `2HJP` | 酷轻松智能热敷包 | switch, model | temperatureGear, TimeOff, RemainingHours, CurrentTemperature, button |
| `2HKW` | 智能按摩椅AM | switch, autoMode | ConnectionStatus, BackRest, Countdown, PressureRegulation, CalfBladder, AutomaticAirBag, shoulderarms, Headhipsac, footkneading, Hipmassage, modeselection, waistmassage, backmalaxation, velocity, zerog, Backautomatically, Theremainingtime, Constanttemperatureapply |
| `2HM0` | 黑白生活智能筋膜枪 | speed, status | Remainingtime, gears, Videointroduction, Lowbatteryprompt, worktime |
| `2HPC` | iSuke智能枕 | battery, status | led, power, realtimeRR, HR |
| `2HQ6` | 城市轻骑智能闪盔 | brightness, switch | Light, LED, Autooff, autoon, bat |
| `2HR5` | 西蒙一位智能开关 | switch, indicator | commonFaultDetection, switchStatus |
| `2HTH` | 启源智能调光 | switch, status | Brigness, Name, OpenOClose, LightName, LampB, LightStatu |
| `2HZW` | 电热毯(酷轻松智能电热毯) | status, lock | err, userSet, synchronization, attribute, sleepSet |
| `2I17` | 莱轻松智能护膝按摩器 | switch, status | commonFaultDetection, timedFuntion, fomentTemperature, massageStall, batteryView |
| `2I3G` | 梦百合0压智能枕 | battery, sleepstatus | wifi, MianOTA, SleepReport, Snoring, deviceState, PillowData, notice |
| `2IAU` | 美菱511冰箱 | faultDetection, intelligentSwitch | freezerFloat, refrigeratorFloat, QuickFreeze, ColdOffMode, QuickFreeTime, AttemperMode, DeepFreeze |
| `2IFL` | 正牛智能电吹风 | mode, status | ConnectStatus, second, minute, Modelshow, Testsareshown |
| `2IJ4` | 摩托车头盔对讲耳机 | FMSwitch, status | Selfbattery, Team, VoiceSet, FmList, FM, Music, Power |
| `2IK5` | 企一照明可调角阅读灯 | switch, brightness | relBrightness, toggleSwitch, commonFaultDetection |
| `2INT` | 艾家智能四位场景面板 | luminance, deviceStatus | sceneButton1, sceneButton2, sceneButton3, sceneButton4 |
| `2INU` | 艾家智能六位场景面板 | deviceStatus, luminance | sceneButton1, sceneButton2, sceneButton3, sceneButton4, sceneButton5, sceneButton6 |
| `2IRF` | 米多全能水洗机A8 Pro | battery, status | workTime, cleantime, totalTime, erro, seclean |
| `2IX9` | 科技暖腰带 | switch, alarm | BLEstatus, countdown, baterry, shutdown, HotCompress, VibrateMode, CurrentTemperature, TemperatureGears, frenquency |
| `2IXD` | 舒适暖腰带 | switch, alarm | BLEstatus, countdown, shutdown, Vibratemode, HotCompress, baterry, CurrentTemperature |
| `2J1T` | 智能洗地机2202 | status, commonExecution4 | devicealarm, rollerbrushlifealarm, filterlifealarm, filterlife, rollerbrushlife, sewageboxstatus, batterystatus, workmode, voiceset, Cleanreminder, timingselfclean, cleandata2, cleanwaterboxstatus, workstatus, cleandata3 |
| `2J2C` | 无尽之窗窗帘机 | opener, action | — |
| `2J40` | A.O.史密斯中央净水机WF25G2 | faultDetection, status | dayPurifyWater, waterSpeed, filterElement1, totalPurifyWater, flushTime, useTime |
| `2J41` | A.O.史密斯中央软水机S20G2 | faultDetection, status | totalWater, waterSpeed, filterElement1, dayWater, remakeTime, useTime |
| `2J42` | A.O.史密斯反渗透净水机R1200BN1 | faultDetection, status | filterElement1, filterElement2, totalPurifyWater, purifyWater, useTime, suggestCount |
| `2J46` | 水享智能阀CZC20 | switch, status | record, reEnergizingState, protection, valveLight, netLight |
| `2J7L` | 水享手动辅助智能阀CZC20S | switch, status | record, netLight, valveLight, reEnergizingState |
| `2J7Y` | 飞利浦足浴按摩器PPM3305F | waterTemp, workMode | temper, Remaining, OTAUpgrade, Atmosphere, surfing, messageSet, coundown, deviceSatus |
| `2J8E` | Meli1折叠锂电车 | mode, switch | forbidden, level, Consumption, warningmessage, distance, autosleep, safetylock, state, selfinspection, odometer |
| `2J8I` | 智能窗 JinLY | opener, action | devicestatue |
| `2J9V` | 十字勋章智能运动健身包 | status, sterilize | commonFaultDetection, Finder, Battery, Tone, PowerSwitch |
| `2JAR` | 欧普蓝牙Mesh单色温灯带驱动 | switch, brightness | toggleSwitch, commonFaultDetection |
| `2JN0` | 三合一拖地机 | status, battery | commonFaultDetection, cleanselfStrongSet, handheldStrongSet, aspirationStrongSet, cleanStrongSet, consumables, aspirationNormalSet, HandheldNormalSet, cleanNormalSet, control, WorkPm, DevMode, cleanselfNormalSet |
| `2JNB` | 莱轻松智能暖宫宝 | status, hot | wave, batt |
| `2JOG` | 按摩椅RSM6 | switch, autoMode | Countdown, BackRest, PressureRegulation, ConnectionStatus, AutomaticAirBag, velocity, shoulderarms, zerog, Hipmassage, Constanttemperatureapply, Headhipsac, backmalaxation, modeselection, waistmassage, footkneading, Backautomatically, Theremainingtime, CalfBladder |
| `2JOJ` | VSITOO智能手冲咖啡壶 | switch, temp | commonFaultDetection, heating, workState |
| `2JOZ` | 柏曼智能双色灯 | switch, brightness | rhythm, timing, countdown, nodeInfo, colorTem, profile |
| `2JR2` | sayrelances智能剃须刀 | status, gear | score, lowPowerAlarm, devicestatus, quantity, workingHours |
| `2JXZ` | 飞利浦按摩披肩PPM3212N | switch, mode | Instructions, heating, Remaining, OTAUpgrade, Intensity, CountdownOff, batteryLevel, deviceSatus, Warning |
| `2K1E` | 科爱元素小面包砭石按摩器智能版 | battery, mode | Service, learningvideo, learningchoice, Switchoff, btstatus, Report, compress, lefttime, timedown, exposure, pressure, suck |
| `2K36` | 青越千分比深度调光线性灯 | switch, brightness | offtime, Ontime, tempvalue, countdown, memoryswitch |
| `2KL7` | 哈尔斯智能水杯 弹盖款(升级版) | battery, currentTemperature | waterDayIntake, config, drinkWarn, drinkTemperature, drinkRemind, drinkTarget, canvasData3, canvasData1, canvasData2, canvasConfig, tempRemind, waterHoursIntake, canvasData4, canvasData5, waterWeeksIntake, drinkDisturb, drinkWeekTarget, darkWeekTarget |
| `2KL8` | 哈尔斯智能水杯 旋盖款(升级版) | battery, currentTemperature | drinkTarget, waterHoursIntake, drinkRemind, drinkDisturb, drinkWeekTarget, waterWeeksIntake, canvasData3, canvasData5, canvasData4, canvasData1, config, canvasData2, tempRemind, canvasConfig, drinkWarn, drinkTemperature |
| `2KLC` | 哈尔斯智能咖啡杯 | battery, currentTemperature | coffe, totalCount, clockIn |
| `2KVN` | 香百年畅享智能香薰机Pro | mode, switch | instruction, hotline, margin2, near, Report, margin1, fragrance, electricity, FirmwareUpdate, autoStart, density, fragSetting2, timing, fragSetting1, cycles |
| `2KXT` | 霍尼韦尔水浸传感器 | waterAlarm, battery | commonFaultDetection |
| `2KZR` | 杜亚智能升降器 DH13 | opener, action | — |
| `2L0L` | 携住温控 | mode, temperature | airKey |
| `2L40` | 美颜枕(4D智能版) | battery, sleepstatus | HR, realtimeRR, power, led |
| `2L53` | 携住红外遥控器XZB-HWZFQ-3.0 | GATT, mode | rcList, projectorKey, airKey, TVKey, STBKey, matchedCap, hchoElement |
| `2L5N` | 智能暖宫腰带 | massage, waterTemp | Switchs, CountDownOff, OTAUpgrade, heating, batteryLevel, deviceSatus, Warning |
| `2L5W` | 高德智感智能温感传感器 | commonMode1, gestureSwitch | queryRelated, firstTime, roomInfo, tempDistribution, inductionRecord, temperatureSwitch, humanRecogni, backgroundMT |
| `2L7K` | iNO care 垂直律动机M50 | pause, gear | today, health, current, login, user, loginAlarm, record, countdownoff, connect, ota |
| `2L8V` | 立达信米来单头吊灯 | switch, brightness | — |
| `2LD6` | 惠尔顿AI前置过滤器 | mode, temp | commonFaultDetection, charge, waterValve, drain, DailyWaterLog, CareReminder, fortify, batteryLevel, waterConsumption, dayUseRecord, console, flow |
| `2LHV` | 中央净水 | faultDetection, status | dayPurifyWater, waterSpeed, filterElement1, totalPurifyWater, flushTime |
| `2LHW` | 中央软水 | faultDetection, status | totalWater, waterSpeed, filterElement1, dayWater, remakeTime |
| `2LQ1` | 友通空气质量检测仪 | temp, pm25 | humi, aqi, pm10, commonFaultDetection, report, brightness01, clock |
| `2LX0` | 礼意久久舒适暖腰带双面款 | switch, alarm | shutdown, BLEstatus, countdown, baterry, Vibratemode, CurrentTemperature, HotCompress |
| `2MEH` | 施柏阁开合帘电机SMC800H | opener, action | commonFaultDetection, PasswordSetting, RestoreFactory, Motordirection |
| `2MEJ` | 施柏阁管状电机SMR602H | opener, action | commonFaultDetection, JogButton, Travelsettings, Motordirection, RestoreFactory, PasswordSetting |
| `2MFH` | 智能彩屏暖宫宝W5 | temp, massage | Connectionstatus, CustomTime, CancelTime, time1, RemainingTime |
| `2MJW` | 欧普PLC转干接点扩展器 | outageMemory, faultDetection | dryContact7, dryContact8, dryContact5, dryContact6, dryContact3, dryContact4, dryContact1, dryContact2 |
| `2MJX` | 欧普PLC转干接点控制器 | outageMemory, faultDetection | dryContactFunc7, dryContactFunc8, dryContactFunc5, dryContactFunc6, dryContactFunc3, dryContactFunc4, dryContactFunc1, dryContactFunc2, dryContact7, dryContact8, dryContact5, dryContact6, dryContactFunc18, dryContactFunc19, dryContactFunc20, dryContact3, dryContact4, dryContact1, dryContact2, dryContactFunc16, dryContactFunc17, dryContactFunc14, dryContactFunc15, dryContactFunc12, dryContactFunc13, dryContactFunc10, dryContactFunc11, dryContactFunc9 |
| `2MMM` | 嵌饮机 | faultDetection, childLockSwitch | inputTds, outputTds, filterElement1, filterElement2, totalPurifyWater, customProgram |
| `2MN2` | 爱莱克特高速吹风机EL280 | mode, status | information |
| `2MQB` | 摩申高速吹风机MH03 | mode, status | worktime, fault, rspeed, allstatus |
| `2MU2` | 昔马智能电动剃须刀 | mode, status | statusa, batteryState, shaverState |
| `2MXK` | 侧装水浸传感器 | waterAlarm, silencer | — |
| `2N28` | 智能语音哑铃 | mode, status | fault, userInfo, partner, language, ExerciseLog, devInfo, courseDetail, voice, OTA, electric |
| `2N2A` | 智能俯卧撑平板撑训练器 | status, mode | duvstatus, partner, electric, OTA, voice, courseDetail, exerciseTime, exerciseNum, devInfo, ExerciseLog |
| `2N2B` | 智能调节哑铃 | mode, status | Upgrade, partner, electric, OTA, courseDetail, voice, devInfo, userInfo, ExerciseLog |
| `2N2R` | A.O.史密斯反渗透净水机R1200H | faultDetection, status | filterElement1, filterElement2, totalPurifyWater, purifyWater, suggestCount, useTime |
| `2N8D` | 空间卫士健康空气智慧管家01 | switch, model | filterElement06, FragranceTime, anion, filterElement02, hotline, filterElement03, filterElement04, filterElement01, filterElement05, PM, lamp, ventilation, density, intelligent, timing |
| `2NIH` | 暖心睡眠仪 | battery, switch2 | Devicestatus, gear2, warn, rate |
| `2NK6` | 外奇智能壁挂风扇F18 | nightLight, gear | countdownOff, shake, remainingTime, fault, deviceVersion, batteryLevel |
| `2NPI` | 研森便携式咖啡机YK-0105C | action, clean | commonFaultDetection, state, info, watertemp |
| `2NU1` | 摩申高速吹风机MH02PRO | mode, status | allstatus, rspeed, fault, worktime |
| `2NVQ` | 天窗HY | action, windowOpener | — |
| `2NVS` | 三思智能植物生长灯R0260 | switch, brightness | — |
| `2NXN` | 美菱茶吧机MC-13BH | status, faultDetection | status1, ST110, ID261, ID266, ID256, ST20, ID259, ID260, ID263, ID272, status2, ID264, ID258, ID262, ID257 |
| `2NXQ` | 酷轻松石墨烯气囊膝腿按摩仪 | hot, workStatus | ota, countdown, pressure, charging, deviceMode, bleStatus, electricity, remainTime |
| `2O2B` | 贵品开合帘GT50 | opener, action | suitablePoint |
| `2O2C` | 贵品卷帘GJ | opener, action | suitablePoint |
| `2O2L` | 美菱茶吧机MC-13H | status, faultDetection | ID260, ST20, ST110, ID266, status2, ID272, ID257, ID259, ID258, ID262, status1, ID263, ID256, ID264 |
| `2O3G` | 信社擦窗机器人 | status, action | ErrorCode, StartStop, WaySetting, WaterMode, clearMode, WheelClear, Manual |
| `2O43` | 威仕达双子星开合帘WSCMXJ | opener, action | left, right, openspeed, Motormanual, swap, controller, calibration |
| `2O62` | 哈尔斯智能水杯 G5 | battery, currentTemperature | waterDayIntake, drinkDisturb, config, healthRemind, drinkRemind |
| `2O6F` | 柏曼智能节律灯 | switch, brightness | countdown, rhythm, colorTem, timing, nodeInfo, profile |
| `2O7G` | 光照传感器 | luminance, battery | commonFaultDetection |
| `2ODW` | 涂趣智慧盒 | volume, switch | MicVolume, MusicVolume, Modeselect, HifiScene, HifiKey, MUTE |
| `2OFW` | 安吉尔全屋大水量净水器J3539-ROC120 | switch, emptySwitch | dayPurifyWater, filterElement1, filterElement2, filterElement3, inputTds, commonFaultDetection |
| `2OFX` | 安吉尔净水器J3303-ROB60 | switch, emptySwitch | dayPurifyWater, filterElement1, filterElement2, inputTds, commonFaultDetection |
| `2OH2` | 酷轻松石墨烯颈部固定器 | hot, workStatus | commonFaultDetection, electricity, deviceMode, pressure, remainTime, countdown, charging, bleStatus, ota |
| `2OI8` | 哈尔斯智能泡茶杯星闪版 | battery, currentTemperature | takeMedicineRemind, drinkRemind, customTeaList, checkedTea |
| `2ONM` | BOW折叠智能触控蓝牙键盘 | capsLock, battery | — |
| `2OUG` | CZC25系列智能漏水保护阀 | switch, status | commonFaultDetection, valveLight, protection, netLight, reEnergizingState, record |
| `2OUW` | 艾有舒随身灸 | status, battery | commonFaultDetection, devSwitch, windSpeed, workTime |
| `2P74` | 恒洁智能马桶R10 | seatStatus, offSeatAction | washSetting, drySetting, toiletSetting, seatHeating |
| `2PDY` | BOXLAMP星空灯 | brightness, switch | meteor, speedOn, starrySky |
| `2PGE` | BOXLAMP星空灯(ProMax) | brightness, switch | starrySky, meteor, speedOn |
| `2PGT` | 研坤牌消毒液制造机 | status, switch | workTime |
| `2PMV` | LCE712B/C智能坐便器 | seatStatus, toiletStatus | toiletSetting, drySetting, seatHeating, washSetting |
| `2PV1` | 哈尔斯智能泡茶杯 星闪纯钛版 | battery, currentTemperature | checkedTea, customTeaList |
| `2PXQ` | 三思智能厨卫灯Pro | brightness, switch | — |
| `2QQI` | 智能植物灯 | brightness, switch | — |
| `2QQN` | 恩仕AXENT.Lite轻智能坐便器 | offSeatAction, seatStatus | seatHeating, toiletSetting |
| `2QWK` | BOXLAMP星空灯(星闪版) | brightness, switch | meteor, speedOn, starrySky |
| `2QY5` | 尚美源牌QY-NF型纳滤净水设备 | status, switch | outputTds, totalPurifyWater, waterSpeed, commonFaultDetection |
| `2QZG` | BOXLAMP星空灯ProMax(星闪版) | brightness, switch | meteor, speedOn, starrySky |
| `2RCP` | 恩仕AXENT.NOVIA明装轻智能淋浴器 | coldWaterSwitch, status | — |
| `2RHS` | 净水控制盒 Sinkfusion A01 | flushSwitch, status | outputTds, totalPurifyWater, waterSpeed, commonFaultDetection |
| `2RL8` | 海雀智能门铃5 | alarmEvent, battery | commonFaultDetection |
| `2RLB` | 海雀智能门铃5Max | alarmEvent, battery | commonFaultDetection |
| `2RMS` | 西顿照明T5无线地脚灯 | nightLightMode, switch | — |
| `2S4N` | DCE735C智能坐便器 | seatStatus, toiletStatus | toiletSetting, drySetting, seatHeating, washSetting |
| `2S9F` | 享界电动车顶帐篷G9 | light, temp | commonFaultDetection, tentControl, Status, Location |
| `9MZW` | 智控燃气灶 | workBurnerGear, workBurnerStatus | currentGasConsumption |
| `A065` | 长虹电视 | switch, volSwitch | — |
| `A07B` | TCL智能电视 | switch, volSwitch | — |
| `A094` | 创维电视 | switch, volSwitch | — |
| `A0DA` | 布谷智能破壁机 | status, action | — |
| `A0DF` | 布谷智能取暖器 | switch, temperature | — |
| `A0MD` | 智汇云窗帘电机 | mode, opener | — |
| `A0NG` | 智汇云调光面板 | switch, brightness | — |
| `A0OV` | 单色球泡灯 | switch, brightness | — |
| `A0R0` | 大金除湿机 | switch, mode | commonFaultDetection |
| `A0RO` | 大金地暖 | switch, temperature | commonFaultDetection, silent, choiceOfColdAndHot |
| `A0SJ` | 加湿器SCK-3A40FW | switch, humidity | windSpeed, closeTime |
| `A0UO` | 霍尼韦尔智能控制窗帘 | action, opener | — |
| `A0UQ` | 霍尼韦尔智能控制新风 | switch, fan | — |
| `A0UR` | 霍尼韦尔智能控制地暖 | switch, temperature | — |
| `A0UT` | 霍尼韦尔智能控制调光 | switch, brightness | — |
| `A0Z4` | 西门子开关 | switch, switch1 | — |
| `A106` | 西门子窗帘 | mode01, mode02 | — |
| `A1NX` | JSQ30-16JW6i家用供热水燃气快速热水器 | switch, temperature | commonFaultDetection, totalGas, waterfallBath, totalWater, iwaterTmp, cycle, heating |
| `A1XQ` | HD-RO-27/A5净水机 | switch, status | outputTds, filterElement1, filterElement2, commonFaultDetection, waterPurMode, purWater, washing |
| `A2AC` | 统帅L3运动空调 | switch, temperature | windSpeed, windDirectionHorizontal, windDirectionVertical, operationMode, freshWindSpeed |
| `A2IB` | 华凌空调 | switch, mode | temperature2, temperature1 |
| `A2ID` | 华凌空调 | switch, mode | temperature2, temperature1 |
| `A2IY` | 美的多头灶MC-DZC2201 | status, switch | commonFaultDetection, relationOperation, relationTemperature, relationGear |
| `A2K1` | CT-UNITE 智能物联网水表 | battery, waterMeterReading | — |
| `A2L9` | 智汇云智能门锁 | lockState, openEvent | — |
| `A2LA` | 智汇云门磁传感器 | doorContact, temperAlarm | remove |
| `A2LM` | 智汇云温控器 | switch, temperature | airCtrl |
| `A2LW` | 温湿度传感器 | temperature, humidity | — |
| `A2LZ` | 智汇云燃气传感器 | alarm, gasSensor | fault, alert |
| `A2M0` | 智汇云烟雾传感器 | temperAlarm, alarm | remove, alert |
| `A2ND` | KEKEN 智能开关2键 | switch2, switch1 | backlight2 |
| `A2TW` | 智汇云窗帘电机 | opener, action | oper |
| `A2VL` | 白灯 | switch, brightness | — |
| `A2WS` | 智汇云温控器 | switch, temperature | airKey |
| `A362` | 欧派智能窗帘电机P41 | opener, action | RangeConfig1, CurrentPositionState1 |
| `A36A` | 欧派智能二位开关P32 | switch2, switch1 | — |
| `A3BM` | 方太智能燃气灶具 | action, status | — |
| `A3CP` | 老板蒸烤一体机 | action, status | — |
| `A3CQ` | 燃气灶 | action, status | — |
| `A3CU` | COLMO净水器 | rinseMode, status | outputTds, commonFaultDetection |
| `A3CV` | COLMO净饮机 | childLockSwitch, status | outputTds, commonFaultDetection |
| `A3CX` | COLMO中央净水器 | rinseMode, status | waterSpeed, commonFaultDetection |
| `A3CY` | COLMO前置过滤器 | rinseMode, status | waterSpeed, commonFaultDetection |
| `A3CZ` | COLMO软水机 | mode, status | waterSpeed, filterElement1, commonFaultDetection |
| `A3D5` | 美的净饮机 | childLockSwitch, status | commonFaultDetection |
| `A3D7` | 美的软水机 | mode, status | waterSpeed, filterElement1, commonFaultDetection |
| `A3D9` | 美的中央净水器 | rinseMode, status | waterSpeed, commonFaultDetection |
| `A3DD` | 美的净水器 | rinseMode, status | commonFaultDetection |
| `A3DP` | 老板洗碗机 | action, status | — |
| `A3E5` | 方太智能净水机 | rinseMode, status | filterElement2, filterElement3, cleanTime, commonFaultDetection |
| `A3F1` | 海信智能新风机 | fan, switch | — |
| `A3FA` | 美的微蒸烤一体机 | action, status | leftTime |
| `A3FB` | 美的净水器 | heatSwitch, status | commonFaultDetection |
| `A3FS` | COLMO蒸烤箱 | action, status | leftTime |
| `A3G6` | 美的智能冰箱 | freezeSwitch, refrigerateSwitch | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3GP` | 格力热水发生器 | switch, temperature | — |
| `A3GQ` | 格力地暖转接器 | switch, temperature | — |
| `A3HB` | 格力新风净化机 | freshAirSpeed, switch | — |
| `A3HC` | 格力新风净化机(60a3) | freshAirSpeed, switch | — |
| `A3I3` | 澳柯玛冷柜 | freezeSwitch, intelligentSwitch | freezerFloat |
| `A3IM` | 倍世中央软水机 | mode, status | filterElement1, remainWater, commonFaultDetection |
| `A3IO` | 倍世厨下净水机 | flushSwitch, status | filterElement1, filterElement2 |
| `A3KP` | 美诺智能冷藏箱 | refrigerateSwitch, status | refrigeratorFloat, commonFaultDetection |
| `A3KQ` | 美诺智能冷冻箱 | freezeSwitch, status | freezerFloat, commonFaultDetection |
| `A3LI` | A.O.史密斯软水机 | regenerateSwitch, status | cleanTime, filterElement1, totalWater, waterSpeed, commonFaultDetection |
| `A3LP` | A.O.史密斯中央净水器 | flushSwitch, status | cleanTime, filterElement1, totalPurifyWater, waterSpeed, commonFaultDetection |
| `A3NP` | 九阳智能全自动破壁机器人 | cupStatus, status | blender, leftTime, commonFaultDetection |
| `A3QH` | 嘉格纳冰箱 | freezeSwitch, refrigerateSwitch | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A3R1` | 嘉格纳烤箱 | status, switch | leftTime, oven, commonFaultDetection |
| `A3RM` | 九阳变频轻音破壁机B7 | cupStatus, status | blender, leftTime, commonFaultDetection |
| `A3RN` | 九阳变频轻音破壁机B5 | cupStatus, status | blender, leftTime, commonFaultDetection |
| `A3RR` | 九阳变频破壁机PB-UL5B8P | cupStatus, status | blender, leftTime, commonFaultDetection |
| `A3RT` | 美的智慧电饭煲 | action, status | cooker, leftTime, commonFaultDetection |
| `A3SK` | 九阳变频破壁机PB-UL5B80 | cupStatus, status | blender, leftTime, commonFaultDetection |
| `A3W1` | 嘉格纳Vario 400 系列酒柜45.7cm | bottomShelftemp, temperature | commonFaultDetection |
| `A3XO` | 美的智能电压力锅 | action, status | cooker, leftTime, commonFaultDetection |
| `A3YD` | 嘉格纳Expressive艺境系列烹饪暖碟抽屉 | status, switch | leftTime, oven, commonFaultDetection |
| `A3Z2` | 西门子蒸玲珑抽屉蒸箱 | switch, status | leftTime, oven, commonFaultDetection |
| `A3ZF` | 博世蒸如意抽屉蒸箱 | switch, status | leftTime, oven, commonFaultDetection |
| `A3ZO` | 嘉格纳Minimalistic臻境系列烹饪暖碟抽屉 | switch, status | leftTime, oven, commonFaultDetection |
| `A3ZS` | 海尔冰箱BCD-502WGHFDGCFSU1 | aiFfSwitch, intelligentSwitch | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A405` | 卡萨帝两门冰箱(黑) | aiFfSwitch, aiFpSwitch | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A409` | 卡萨帝冰箱BCD-562WGCFDM4DUU1 | aiFfSwitch, switch | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A40C` | 卡萨帝冰箱BCD-580WGCFDA4H7U1(DZ) | aiFfSwitch, intelligentSwitch | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A40D` | 卡萨帝冰箱BCD-512WLCMDAGGDU1 | aiFfSwitch, aiFpSwitch | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A40E` | 卡萨帝十字门冰箱 | aiFfSwitch, freezeSwitch | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A40O` | 九阳不用手洗破壁机Y9 | cupStatus, status | blender, leftTime, commonFaultDetection |
| `A411` | 卡萨帝冰箱BCD-385WLCC2M4H7U1 | aiFfSwitch, intelligentSwitch | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A41C` | 九阳变频轻音破壁机B5-B | cupStatus, status | blender, leftTime, commonFaultDetection |
| `A427` | 卡萨帝冰箱BCD-580WGCTDA4H7U1 | aiFfSwitch, intelligentSwitch | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A44Y` | 欧瑞博地暖 | heat, switch | commonFaultDetection |
| `O0BY` | 斯百瑞家用无创呼吸机如意系列 | mode, status | time, epap, wet, usageTime, historicalData, capa, airLeakage, realtimeData, ipap, heartRate, bloodOxygen, comf, starttime |
| `O0FY` | 斯百瑞新如意无创呼吸机B80 | mode, status | time, heater, wet, capa, ps, riseTime, ipap, epap, comf, starttime |
| `O0FZ` | 斯百瑞新如意无创呼吸机C60 | mode, status | time, capa, wet, comf, starttime |
| `O0G0` | 斯百瑞新如意无创呼吸机T30 | mode, status | time, capa, wet, starttime, RampTime, historicalData, ipap, epap, riseTime, comf, heater, airLeakage, usageTime, rampStart, realtimeData |
| `O0G1` | 斯百瑞新如意无创呼吸机T80 | mode, status | time, realtimeData, capa, starttime, epap, airLeakage, riseTime, historicalData, RampTime, ipap, usageTime, heater, wet, comf |
| `T100` | HUAWEI MateView | volume, brightness | whiteList, deviceMgr, protectEye, mic |
| `V0EK` | 虚拟智慧屏 | switch, volume | — |
| `ZF0D` | 全屋音乐系统 | systemState, systemPlayState | systemInfo, restart, systemPlay, hwaccount, playTask1, playTask2, playTask3, playTask4, playTask5, playTask6, playTask7, playTask8, playTask9, zone1, zone2, zone3, zone4, zone5, zone6, zone7, zone8, zone9, zone10, zone11, zone12, zone13, zone14, zone15, zone16, zone17, zone18, zone19, zone20, zone21, speaker1, speaker2, speaker3, speaker4, speaker5, speaker6, speaker7, speaker8, speaker9, speaker10, speaker11, speaker12, speaker13, speaker14, speaker15, speaker16, speaker17, speaker18, speaker19, speaker20, speaker21, thirdStorage |
| `ZG14` | 调光智能灯 | switch, brightness | fadeTime, relBrightness |
| `ZG16` | 调光床头灯 | switch, brightness | fadeTime, relBrightness |
| `ZG18` | 调光灯带 | switch, brightness | fadeTime, relBrightness |
| `ZG1F` | 华为鸿蒙智家 智能MINI | faultDetection, battery | — |
| `ZG1K` | 华为鸿蒙智家 智能MINI Pro | faultDetection, battery | rotationMode, wakeup |
| `ZG2A` | 调光吊灯 | switch, brightness | fadeTime, relBrightness |
| `ZG2B` | 调光磁吸灯 | switch, brightness | fadeTime, relBrightness |
| `ZG2C` | 调光射灯 | switch, brightness | fadeTime, relBrightness |
| `ZG2D` | 调光筒灯 | switch, brightness | fadeTime, relBrightness |
| `ZG2E` | 调光吸顶灯 | switch, brightness | fadeTime, relBrightness |
| `ZG2M` | AI超感传感器 Air | luminance, backlight | — |
| `ZG2W` | 智控旋钮 | faultDetection, battery | rotation |
| `0070` | Sound X | discovery | hwaccount, speakerState, smartspeaker, audioplayer, BTIdle |
| `1006` | 欧普全彩空间情景灯 | light | — |
| `1007` | 欧普幻彩明辉 | light | — |
| `100C` | 破壁免滤豆浆机 | faultDetection | beanCooker, timeToFinished |
| `100S` | 柏翠静音面包机PE9600 | faultDetection | breadCooker, babyLock |
| `100d` | 欧普智能灯具 | light | — |
| `100w` | 美的电饭煲4005XM | faultDetection | riceCooker |
| `100y` | 净美仕空气净化器 | switch | pm2p5, wind |
| `1011` | BroadLink智能插座 | switch | delay, timerID |
| `1013` | 报警盒子 | discovery | — |
| `1014` | 门窗开关传感器 | battery | doorSensor |
| `1015` | 四键摇控器 | battery | keyEvent |
| `101A` | 中控主机 | mode | — |
| `101C` | 华为智选 欧普读写台灯 | light | — |
| `101F` | 人体感应 | battery | motionSensor |
| `101N` | 720环境宝 | airDetector | — |
| `101T` | 格兰仕智能微波炉 | faultDetection | microwaveOven |
| `101V` | 安朗杰西勒奇指纹锁-SC系列 | battery | smartLock, lockAlarm, account, event |
| `101g` | 红外探测器 | battery | motionSensor |
| `101w` | 净美仕空气净化器 | switch | pm2p5, wind |
| `101y` | 美的空气净化器 | switch | airPurifying, pm2p5, vocDetector, wind |
| `1028` | 汇泰龙云锁 | battery | smartLock, lockAlarm, account, event |
| `103J` | 声光报警器 | battery | alertor |
| `103M` | 九阳高速破壁调理机Y15S | faultDetection | joyoung, timeToFinished |
| `103Q` | 欧普蓝牙门磁OPLYMC | battery | doorSensor |
| `103R` | 欧普蓝牙红外OPLYHW | battery | motionSensor |
| `103W` | 国投主控1路开关1LA | switch | — |
| `1042` | 国投电动燃气开关MTS | battery | gasValve |
| `1043` |  | switch | — |
| `1045` |  | battery | doorSensor |
| `104A` | 国投二氧化碳传感器CO2 | airDetector | — |
| `104C` | 国投PM2.5传感器PMX | airDetector | — |
| `104D` | 国投光照传感器LUX | luminance | — |
| `104E` | 中控主机 | discovery | — |
| `104I` | 美的电饭煲MB-FB40Star701 | faultDetection | riceCooker |
| `104K` | 美的养生壶GE1502 | faultDetection | healthPot |
| `104N` | 安朗杰西勒奇指纹锁-SE系列 | battery | smartLock, lockAlarm, account, event |
| `104P` | 九阳炒菜机器人J7 | faultDetection | cook |
| `104Q` | Wulian网关(02增强型) | discovery | — |
| `104R` | Wulian智尚一路开关 | switch | — |
| `104U` |  | openLevel | — |
| `104Y` | 九阳空气炸锅KL-50G1 | faultDetection | cook |
| `1050` | 瑞晶六合一空气检测器RAD-1 | airDetector | — |
| `105D` | 易百珑单路多功能接收器ERC309-H | switch | delay |
| `105I` |  | switch | delay |
| `105M` | 欧瑞博智能插座S30c | switch | delay, timerID |
| `105R` | 小米人体传感器 | battery | motionSensor |
| `105Y` | 奥普新风机1035AR | tvoc | freshAir, pm2p5, co2 |
| `1061` | 飞比网关FGD87T0-NPHM | discovery | — |
| `1063` | 飞比人体传感器NBOT106W-M2 | battery | motionSensor |
| `1068` | 顺舟智能网关SZ09-GW-02 | discovery | — |
| `106B` | 顺舟人体红外感应SZ09-(04) | battery | motionSensor |
| `106F` | 顺舟西勒奇门锁SZ09-(19)-320C  | battery | smartLock, lockAlarm, account, event |
| `106K` |  | battery | motionSensor |
| `107J` | 遥看小苹果 | controlKey | ledOnoff, deviceList, cmdList |
| `107V` | Sonoff basic wifi智能开关 | switch | startup, delay |
| `107W` | Sonoff POW R2电量监测wifi开关 | switch | startup, energyConsumtion, historyConsumption, alarmType, powerProtect, onceStatistics, delay |
| `108M` | 西睿空气检测仪底座 | airDetector | cube, city, screenSetting, airQualityReminder |
| `110E` | 华为智选 火火兔智能早教故事机 | switch | timedTask, music, earLight, faceLight, custom |
| `111W` | 宠物智能喂食器 | status | feedMode, meals, copies, totalCopies, feedTime, faultInfo |
| `113C` | 豪恩人体传感器 | battery | motionSensor |
| `113G` | SONOFF TX1C 智能墙壁开关 | switch1 | delay, powerLight, startup1, pulseSwitch1, pulseLength1 |
| `114N` | 布朗壁挂式新风机 | faultDetection | device_status, filter_status, filter_control |
| `115P` | HDL新风 | switch | freshAir |
| `115S` | HDL空气质量传感器 | pm25 | — |
| `116I` | 华为智选 iateey智能即热饮水吧 | deviceStatus | setUpWater, dataWater, waterUsage, machineTemp, breakdown, softWareBug |
| `116O` | 海令智能家庭网关 | discovery | — |
| `116X` | HDL窗帘 | openLevel | — |
| `120P` | 海令智能门磁传感器 | battery | doorSensor |
| `120T` |  | battery | motionSensor |
| `121A` | 海令智能开关面板 | switch | — |
| `121W` | 一位免零线智能开关 | switch | switchLable |
| `122E` | 继电器模块 | switch | power |
| `122T` | 智能二三极插座 | switch | switchLable01, switchLable02 |
| `123J` | 罗格朗墙面网关 | discovery | devOta |
| `123K` | 一位智能窗帘开关 | motor | curtainLable |
| `124Y` | 即来智能插座C0102 | switch | delay, powerLight, timerID |
| `128B` | 便携式深层肌肉按摩仪 | gear | UsageCounter, CountDown, LifeTimer, Power |
| `134B` | 通力蓝牙网关 | light | bluetoothnode, devOta |
| `140H` | 控客一路灯光面板 | switch | — |
| `140V` | 窗帘控制器 | motor | — |
| `140W` | 窗帘控制器 | motor | — |
| `140X` | 开关回路控制器 | switch | — |
| `140Y` | 开关回路控制器 | switch | — |
| `141Z` | 杜亚智能窗帘DH3 | opener | schedule |
| `144R` | 杜亚智能卷帘DM25 | opener | schedule |
| `144S` | 杜亚智能卷帘DM35 | opener | schedule |
| `151J` | 蓝牙情景面板（双键） | battery | button, buttonName |
| `151K` | 蓝牙情景面板（四键） | battery | button, buttonName |
| `151L` | 蓝牙情景面板（六键） | battery | button, buttonName |
| `152S` | 艾沃家用净水器 | status | inputTds, outputTds, purifyWater, filterElement1, filterElement2 |
| `153R` | 力博得智能牙刷·智悦 | voiceSwitch | brushingHistory, brushDay |
| `156U` | 小圆智能红外遥控器 | controlKey | ledOnoff, deviceList, cmdList |
| `157I` | 酷轻松石墨烯发热护膝 | switch | — |
| `157X` | 威廷智能单开Wi-Fi | switch | delay |
| `162W` | 卡赫智能吸尘器 | battery | workRecord, WorkMethod, Error, VacuumStatus, leftTime, ChildLock, filterElement |
| `163Q` | 智能单开开关 | switch1 | — |
| `167U` | Gimbal Pro-L7B-Pro | switch | — |
| `168M` | 三思智能面板开关 | switch | yedengstatus, yedengsw |
| `174W` | 多功能按摩脚机HiLink版 | switch | Intensity, Heat, WorkMode |
| `175R` | 平头熊一键开关WIFI | switch1 | — |
| `176I` | 极米投影仪H3S | switch | FOCUS, VOLUMEPRESS, FOCUSLEFT, FOCUSRIGHT, FOCUSAUTO, MOVEHOME, MENU, HOME, BACK, VOLUMEDOWN, VOLUMEUP, DPADCENTER, DPADRIGHT, DPADLEFT, DPADDOWN, DPADUP, KPPOWER, RESTART, POWER |
| `176Y` | 极米投影仪RS PRO 2 | switch | FOCUS, VOLUMEPRESS, FOCUSLEFT, FOCUSRIGHT, FOCUSAUTO, MOVEHOME, MENU, HOME, BACK, VOLUMEDOWN, VOLUMEUP, DPADCENTER, DPADRIGHT, DPADLEFT, DPADDOWN, DPADUP, KPPOWER, RESTART, POWER |
| `181W` | 噼啪智能单开开关 | switch | delay |
| `182J` | 云起智慧中心 | discovery | — |
| `183F` | 噼啪智能插座 | switch | delay |
| `183N` | 天博智-智点点T91 | switch | DeviceContro0012, DeviceState0006, DeviceControl0010, DeviceControl0011, DeviceState0009, DeviceWiFiSet0013, DeviceState0008, DeviceContro0013 |
| `186J` | 灵鹦魔盒 | light | hourMode, countdown, screenlight, music |
| `188B` | 威廷智能插座 | switch | delay |
| `188O` | 易跑Y5筋膜枪 | speed | gearshow, usertime, Gears, onoff |
| `2001` | YESOUL野小兽智能健腹轮 | battery | Disconnecttips, ClassPart, Pause, StartSports, Sporttype, calorie, Devicestatus, worktime, CumulativeValue, count |
| `201V` | 领普三键无线开关MESH | battery | button1, button2, button3 |
| `201Y` | 领普双键无线开关MESH | battery | button1, button2 |
| `201Z` | 领普单键无线开关MESH | battery | button1 |
| `203F` | YESOUL野小兽筋膜枪 | switch | Stall, TimeRemaining |
| `206F` | 西顿舍见Mesh智能网关 | discovery | devList, addDevice, groupControl, groupManage, group1, group2, group3, group4 |
| `2078` | 雅观智能网关-AKH1002 | discovery | — |
| `2082` | 白色零火线单路灯控面板超薄 | switch | — |
| `20C1` | 未来小七机器人 | switch | — |
| `20F5` |  | mode | — |
| `20F7` | 永林锐系列主机面板 | discovery | devOta |
| `20FH` | 海令中控主机 | switch | devOta |
| `20GX` | 领普单键零火墙壁开关 | switch | led |
| `20I8` | 摩根智能主机 | reset | clickedScene, sceneRelation |
| `20K4` | 控客10A智能插座 | switch | — |
| `20K7` | 控客16A智能插座 | switch | — |
| `20K8` | 控客推窗器面板 | mode | — |
| `20KA` |  | mode | — |
| `20KB` | 控客SOS紧急呼叫面板 | pushButton | — |
| `20KC` | 控客快捷面板 | battery | buttonName |
| `20PU` | 华为智选 iateey智能即热饮水吧 | deviceStatus | setUpWater, dataWater, waterUsage, machineTemp, breakdown, softWareBug |
| `20QN` | 荣泰蜘蛛侠摩舒枕 | switch | Workinghours, LEVLE, MODE, Time, Heat |
| `20S2` | 艾优智能电吹风 | commonMemorySwitch1 | — |
| `20SP` | 控客-灵悦主机 | discovery | sceneRelation |
| `20SV` | eefit元气通二代 | switch | — |
| `20SX` | 亚摩斯Mesh网关 | discovery | autoSceneList, LsceneList |
| `20UZ` | 立久佳跑步机 | switch | distance, calorie, heartrate, duration, tempo |
| `20XK` | 控客-星空单路灯控面板 | switch | — |
| `20XL` | 杰诺无线清洗机 | mode | electric, cumulativeTime, AbnormalPrompt |
| `20Y5` | 控客-星空单路窗帘面板 | mode | — |
| `20YI` | 控客-人体红外传感器 | battery | motionDetected |
| `20YL` | 小恬空气灭菌加湿器 | switch | ST, SMODE, SL, Level, WAT, COV, WT |
| `20Z0` | 控客-燃气报警器 | alarm | commonFaultDetection |
| `20Z9` | 控客-红外幕帘探测器 | battery | motionDetected, dismantle |
| `20ZE` | 觅石智能剃须刀 | modeSelect | electric, frequency, cleanRemind, totalTime |
| `211G` | 阿尔法蛋智能词典笔S | battery | ota, otareport, statistic, dict, rdp |
| `212L` | 单键智能开关面板尊享版 | backlightMode | — |
| `213R` | 西顿六键PLC网关面板 | discovery | devOta |
| `214X` | 智汇云一位轻触开关面板 | switch | delay |
| `215F` | 清易无线吸尘器 | status | commonFilterElement1, commonFilterElement2, commonFaultDetection, powersetting, worktime, area, calorie, batterylevel, cleanmark, offscreentime |
| `215K` | 智能服务器 | discovery | productid, devOta |
| `215L` | 触控单开零火开关 | switch | — |
| `215T` | 可燃气体探测器 | alarm | — |
| `2160` | 红外幕帘探测器 | battery | motionDetected |
| `2161` | 红外人体探测器 | battery | motionDetected |
| `2163` | 触控单路窗帘电机控制面板 | mode | — |
| `216J` | Olybo智能电动牙刷 | voiceSwitch | brushingHistory, brushDay |
| `217M` | 开关智能控制器1型 | switch | — |
| `217P` | 控客-肖邦一路灯光面板 | switch | — |
| `217T` |  | mode | — |
| `217V` | 控客-肖邦10A智能插座 | switch | — |
| `217W` | 控客-肖邦16A智能插座 | switch | — |
| `2181` |  | battery | motionDetected |
| `2191` | HEIMAN智能情景开关 | battery | sceneState |
| `219N` | ENO智能水杯 | temperature | alarmTime1, drinkwaterHistory, blessing, waterclock, count |
| `219P` | 酷轻松石墨烯气囊支撑腰带 | switch | — |
| `219V` | 爱特嘉智能速热开水机 | deviceStatus | dataWater, setUpWater |
| `21B2` | 单键智能开关面板尊享版 | switch | — |
| `21DC` |  | discovery | num |
| `21DE` | 云起奇点开关模块PRO一联 | switch | memoryState |
| `21DO` | HEIMAN燃气报警器 | alarm | Alarmthreshold, Language, PERIOD, VolumeSetting, Sensorselftest, Robot, Mute, equipmentStatus |
| `21EI` | JW智能照明开关灯 | switch | — |
| `21ES` | JW智能窗帘A型 | mode | — |
| `21ET` | JW中控主机 | disSwitch | — |
| `21G7` | JW光照检测器 | luminance | — |
| `21GK` | JW智能开关1键型 | switch | — |
| `21GN` | JW红外人体感应 | battery | motionDetected |
| `21GX` | 达阔电蚊香 | switch | commonFilterElement1, Mode |
| `21HL` | 锐亿剃须刀 | commonMemorySwitch1 | guide, record, currentcapacity, frequency, time, state |
| `21I3` | 三思插座小夜灯 | switch | delay, yedengsw, yedengstatus |
| `21LC` | 米立多合一网关 | switch | devOta |
| `21LD` | 米立1路窗帘控制面板 | mode | — |
| `21LF` | 米立1路智能开关面板 | switch | — |
| `21M5` | 赤兔Air1智能跑步机 | switch | speedtiao, po, distance, time, kcal |
| `21MO` | 酷轻松石墨烯发热真丝暖腹宝 | switch | — |
| `21MT` | 艾谱保险箱 | switch | lockstate, bp, ar, oo |
| `21N2` | 欧普智能网关 | switch | — |
| `21OQ` | A.O.史密斯中央软水机 | faultDetection | useTime, filterElement, purifyWater |
| `21P8` | 全屋中控主机Lite | reset | autoScene, manualScene, clickedScene |
| `21P9` | 开关灯（底盒开关控制器） | switch | — |
| `21PG` | 触点开关 | switch | — |
| `21PH` | 人体移动传感器 | status | — |
| `21PJ` | 紧急按钮 | pushButton | — |
| `21PS` | 燃气传感器 | alarm | — |
| `21SR` | 开关卷帘 | action | — |
| `21TS` | 狄耐克智能插座 | switch | — |
| `21TX` | 西顿开关控制模块 | switch | — |
| `21V0` | 慕村蒸汽负离子卷直发器H1 | commonMemorySwitch1 | Useyourtime, characterdesigns, Modellingtime, Rapidmodelling, Essentialoilhaircare, Modellingtemperature, Modellingoftheclassroom |
| `21V2` | 瑞晶智能开关 | switch1 | — |
| `21V5` | 慕村红外护发直发梳T1 | commonMemorySwitch1 | Scenerecommendation, UsageHistory, FirmwareUpgrade, Cumulativeuse, Modellingtemperature, Modellingoftheclassroom, Modellingtime, Personalizeddesign, QuickStyles, Accumulatedtime, CryogenicHairCare |
| `21VY` | 瑞晶开关灯 | switch | — |
| `21W8` | 瑞晶智能调节器 | SetVal | — |
| `21W9` | 友宏智能跳绳 | mode | countRecord, versionNumber, record, level |
| `21WL` | 大拿便携冲牙器 | switch | tip, record, Usethebible, Gumtypes, Massagemode, Gentlemode, standardmodel, Efimode, electricity, Usingthelength, waterpressure |
| `21XA` | 瑞晶开合帘 | mode | — |
| `21XE` | 瑞晶百叶帘 | mode | — |
| `21XF` | 瑞晶卷帘 | action | — |
| `21XK` | 瑞晶燃气探测器 | alarm | — |
| `21XO` | 瑞晶紧急按钮 | pushButton | — |
| `220F` | 全屋中控主机Pro | disSwitch | clickedScene |
| `220N` | 人体存在传感器 | status | — |
| `2219` | 艾谱灵镜保管箱 | switch | lockstate, bp, ar, oo |
| `221G` |  | mode | — |
| `221K` |  | battery | motionDetected |
| `221M` |  | switch | — |
| `221S` |  | pushButton | — |
| `221T` |  | switch | — |
| `221X` |  | switch | electric, reverseTimes |
| `221Y` |  | switch | electric, reverseTimes |
| `2221` |  | switch | — |
| `2246` |  | switch | — |
| `2247` |  | switch | — |
| `224O` |  | switch | — |
| `2254` | 盯盯拍智能语音车载支架 | commonMode1 | — |
| `2269` | 瑞晶安防控制器 | switch | Disarm, devOta |
| `227Q` | 光传感器 | luminance | — |
| `227S` | 亚摩斯睿雅单火开关单键 | switch | — |
| `22DN` | IPL光子嫩肤脱毛仪 | mode | directionUse, Icing, Outgoing, gears, FlashRecording, LengthDepilation |
| `22DS` | 力博得智能声波牙刷2 冰山款 | status | brushingHistory, brushSettings, audioSwitch, brushingHistorys, batterys, brushScore, brushDay, clear, misicState |
| `22G1` | E.keyco牌HX-E12-D型反渗透净水器 | switch | Totalnetwater, statu, Flushingcontrol, Alarm, Singlewateryield, PurewaterTDS, watertemperature, Totalwastewater, Cartridgelife, Cartridgelife2 |
| `22GT` | 眠虫纯石墨烯暖宫腰带 | switch | State, Video, Fault, LEVEL, MassageTime, Gear, HeatTime, TEMP, ON |
| `22I7` | 杰诺无线清洗机 | mode | AbnormalPrompt, cumulativeTime, electric |
| `22IA` | 洁云无线清洗机 | mode | AbnormalPrompt, cumulativeTime, electric |
| `22IK` | 格林盈璐灭蚊器GM965TP | switch | Time |
| `22QS` | 艾优智能电吹风 | commonMemorySwitch1 | Msdryhair, Mendryhair, Childrenmodel, Gearselection, time, smartdryhair |
| `22R4` | 适居之家智能沙发 | reset | Locationmemory, Mode, lieflat, Backdown, Backup, Stepdown, Stepup |
| `22R5` | 适居之家智能沙发椅 | reset | Stepup, Stepdown, Backup, Backdown, lieflat, Mode, Locationmemory |
| `22UM` | 力博得智能冲牙器 S1 | gear | setWorkTime, filterElement, brushingHistory, batterys, Oralirrigatorguidelines, remainTimes, rushingHistory, modes, slowstartSwitch, guideSiwtch, toppleOverSwitch, deviceLock, brushDay |
| `22VN` | 格林盈璐灭蚊器GM929A | switch | Time |
| `22ZO` | 怡可智能保温杯 | temperature | drinkwaterhistory, blessing, waterclock, count |
| `22ZY` | Evoyo燃气传感器 | alarm | — |
| `2301` | Evoyo吸顶式人体传感器 | status | — |
| `23BZ` | 乐尔康全身按摩垫 | switch | Timing, HotCompress, Speed, Mode, BackMassage, NeckMassage |
| `23C0` | 乐尔康按摩枕 | switch | Timing, HotCompress, Speed, Mode |
| `23C1` | 乐尔康按摩垫 | switch | Timing, HotCompress, Speed, Mode |
| `23FC` | 亚摩斯智能家具控制器 | action | — |
| `23GJ` | 澳柯玛智慧冰箱 | faultDetection | roomTarget, roomTemp, refrigeratorMode |
| `23GX` | 澳柯玛智慧冰箱 | faultDetection | refrigeratorMode, roomTarget, roomTemp |
| `23R9` | 智能健身折叠单车T1 | switch | kwh, theKm, always, dataBody, theCal |
| `23XE` | 计客超级魔方i2 | battery | history, rotate, connect, intro |
| `240B` | 奥科智能开合帘电机 | action | UseDefaults, resversal |
| `240W` | 单键86底盒开关模块 | switch | — |
| `246O` | 康佳智能筋膜枪F2 | switch | LEVEL, value, ReTime, TIME, Speed, workstate |
| `24BT` | 极米投影仪Play X Home | switch | FOCUS, VOLUMEPRESS, FOCUSLEFT, FOCUSRIGHT, FOCUSAUTO, MOVEHOME, MENU, HOME, BACK, VOLUMEDOWN, VOLUMEUP, DPADCENTER, DPADRIGHT, DPADLEFT, DPADDOWN, DPADUP, KPPOWER, RESTART, POWER |
| `24BU` | 极米投影仪New Z8X | switch | FOCUS, VOLUMEPRESS, FOCUSLEFT, FOCUSRIGHT, FOCUSAUTO, MOVEHOME, MENU, HOME, BACK, VOLUMEDOWN, VOLUMEUP, DPADCENTER, DPADRIGHT, DPADLEFT, DPADDOWN, DPADUP, KPPOWER, RESTART, POWER |
| `24BV` | 极米投影仪New Z6X | switch | FOCUS, VOLUMEPRESS, FOCUSLEFT, FOCUSRIGHT, FOCUSAUTO, MOVEHOME, MENU, HOME, BACK, VOLUMEDOWN, VOLUMEUP, DPADCENTER, DPADRIGHT, DPADLEFT, DPADDOWN, DPADUP, KPPOWER, RESTART, POWER |
| `24BZ` | 极米投影仪New Z6 | switch | FOCUS, VOLUMEPRESS, FOCUSLEFT, FOCUSRIGHT, FOCUSAUTO, MOVEHOME, MENU, HOME, BACK, VOLUMEDOWN, VOLUMEUP, DPADCENTER, DPADRIGHT, DPADLEFT, DPADDOWN, DPADUP, KPPOWER, RESTART, POWER |
| `24DJ` | 亚摩斯智能转换插 | switch | — |
| `24H9` | 欢喜滑板车X8 | switch | commonFaultDetection, StartMode, ScooterCruise, Lights, DrivingMode, TotalMileage, Mileage, Battery, RealTimeSpeed |
| `24J6` | FOOXMET智能温控外套 | switch | commonFaultDetection, DeviceState, ZoneTemptureSet, ZoneATempture, ZoneBTempture, ZoneCTempture |
| `24LC` | FOOXMET智能温控裤子 | switch | commonFaultDetection, DeviceState, ZoneBTempture, ZoneCTempture, ZoneTemptureSet, ZoneATempture |
| `24MJ` | 北冥小鱼智能体脂秤C1 | connectStatus | Measurement, user, desc, report |
| `24MT` | 人教畅读智能笔 | battery | studyInfo, registerInfo, verifyCode |
| `24MV` | 月球车运动版 | switch | commonFaultDetection, Universe, AvoidObstacle, DoStunt1, ShowBattery, Building, LeftRightWheel, ConnectStatus, LightColors, UpdownWheel, DoStunt2 |
| `24O9` | 乐骑智能电动滑板车 | mode | function, FirmwareUpdate, CurrentAverageVelocity, CurrentSpeed, connect, Battery, TotalDistance, Bluetooth, Mileage1, Mileage2, Cyclingtime |
| `24QN` | 鼎宏智能按摩椅 | switch | Lamp, Backlift, Heating, Footroller, Pressure, Manualmode, Mode, Zerogravity, Adjustment, Time, Status |
| `24WU` | VSITOO智能车载电热杯 | temp | commonFaultDetection, workState, heating |
| `250I` | Populele智能尤克里里 | status | chord, tuning, learning, practice, interactive |
| `251D` | 康佳智能筋膜枪F5 | switch | LEVEL, value, Speed, ReTime, TIME, workstate |
| `251E` | 康佳智能筋膜枪F3 | switch | LEVEL, workstate, ReTime, Time, Speed, value |
| `253F` | 奥克斯智能按摩椅 | switch | HipGasbag, BodyGasbag, LegGasbag, ModeSelect, ShoulderGasbag, BackLift, MassageTime, Workstatus, BalloonStrength, MassageIntensity, Manualmode, WaistMuggy, AutoModeSelect, SoleRoller |
| `2562` | 专业会议宝 | switch | abnormalPrompt, batteryLevel, stanbyTime, voiceLight, devicePromptTone, speakerVolume, micMute, denoise |
| `256C` | 盯盯拍智慧中控屏 | commonMode1 | — |
| `2570` | 新日电动摩托车GF6 | alarm | OTA, diagnosis, remainEle, remainKm, carLock, openSeat, NFC, powStatus |
| `2571` | 新日电动自行车FN3 | alarm | powStatus, diagnosis, openSeat, carLock, NFC, OTA, remainEle, remainKm |
| `257L` | 智能会议宝 | switch | abnormalPrompt, denoise, micMute, speakerVolume, devicePromptTone, voiceLight, stanbyTime, batteryLevel |
| `259L` | 巢居全新360度取暖器N4 | switch | CHILDLOCK, voice, timing, Lightcolor, Currenttemperature, Lightinducedsleep, Modeselection, purify |
| `25A4` | 巢居全新360度取暖器N3 | switch | Modeselection, Lightinducedsleep, purify, Lightcolor, timing, CHILDLOCK, voice, Currenttemperature |
| `25C7` | 新日电动自行车XC3 | alarm | carLock, powStatus, diagnosis, remainKm, remainEle, OTA |
| `25CX` | 折叠足浴器 | switch | interrupted, TargetTemperature, Timing, Healthy, Comfortable, WarmingFeet, Sleep, RedLight |
| `25EB` | 盯盯拍车载智慧屏S50 | commonMode1 | — |
| `25EK` | 冰点光子嫩肤脱毛仪 | switch | Outgoing, LengthDepilation, FlashRecording, depilationMode, gears, Icing, directionUse |
| `25ER` | listeneer倾听者M3 | battery | filemeta, summary, file, plan, list, link, Status |
| `25EU` | 迈德斯特电动升降桌 | commonExecution1 | commonFaultDetection, Reminder, ChildLockSwitch, height |
| `25HA` | 德沃福无线清洗机 | mode | AbnormalPrompt, cumulativeTime, electric |
| `25HN` | 儿童安全座椅 | speed | anquan, kaiguan, shui, deng, yin |
| `25I8` | 领普mesh网关 | discovery | devList, addDevice, groupControl, groupManage, group1, group2, group3, group4 |
| `25IB` | 格沵随身智能保温杯 | commonMemorySwitch1 | tip, temperaturerange, Findcups, Reminddrinking, Bettylow |
| `25IP` | Helmetphone智能头盔 | switch | led, bat, TimingOff, VA, NewSong, prev, Up, Down, Play, right, turn, Light |
| `25J9` | Airwheel 智能骑行箱 | speed | commonFaultDetection, batteryView, deviceControl, mileage, totalMileage, power, time, voltage |
| `25JA` | 电动滑板车X6 | commonMode1 | lockMechanism, FirmwareUpdate, TotalTrip, TRIP, RealTimeSpeed, Battery, ClearKey, StartMode, ScooterCruise, Lights, DrivingMode, Lock |
| `25K2` | 远程辅导机LHW02-C3 | switch | register, rssi, reminder, homework |
| `25KE` | 小彼恩WIFI点读笔 | deviceStatus | deviceImage, bookReadNum, volumeCtrl, audioPaly, totalReadTime, boughtBook, pilotLamp, deviceName, todayReadTime, bookSelect, diskManageBtn, batteryStatus, userLogin |
| `25KU` | Airwheel 智能跟随行李箱 | speed | commonFaultDetection, power, totalMileage, batteryView, deviceControl, mileage, time, voltage |
| `25NR` | 希诺智能保温杯 | status | FirmwareUpdate, remind, watertemperature |
| `25ON` | 天博智-智点点T90 | switch | DeviceState0006, DeviceContro0012, DeviceContro0013, DeviceState0009, DeviceState0008, DeviceControl0010, DeviceWiFiSet0013, DeviceControl0011 |
| `25OQ` | Airwheel 智能骑行箱 | speed | commonFaultDetection, batteryView, totalMileage, time, mileage, deviceControl, power, voltage |
| `25OT` | 探梦者电动自行车F8 | speed | Exception, speedContr, checkcar, cruise, startMethod, carlamp, totalTrip, thisTrip, electricity, speedUnit, lockonoff, RestoringFactory |
| `25Q4` | 苏泊尔智能物联保温杯 | temp | remind, power, TDS, restScreen |
| `264R` | 爱贝丽智能童车 | status | firmwareUP, Travelrecord, Trackdetails, Statistics, WiFi, electricity |
| `26H0` | 创维智能足浴盆 | switch | DeviceStatus, Massage, TargetTemp, Timing, CurrentTemperature, RemainingDuration |
| `26U0` | 酷轻松石墨烯腰带 | switch | Remind, Message, Mode, workstate, frontLevel, frontRealTemperature, backRealTemperature, bakeLevel, timerlabel |
| `2796` | 好来喜电动童车 | lock | DeviceHota, Parking, rockingCar, atmosphereLamp, headlight, lightControl, gearChange, vehicleControl |
| `27UW` | 外研通智能扫读笔 | battery | studyInfo, registerInfo, verifyCode |
| `27VH` | 家用燃气报警器 | silencer | commonFaultDetection, DeviceSelfCheck, RecordsQuery, RemoteControl, PeripheralStatus, TemperatureValue, CoValue, CGC |
| `283H` | HD 接收机 | volume | source, AUDIOINPUT, MUTE, VIDEOINPUT, STANDBY |
| `283T` | FSL智能插座 | switch | — |
| `285U` | Airwheel 智能骑行箱 | speed | commonFaultDetection, hardwareFunction, deviceControl, time, voltage, power, totalMileage, mileage, batteryView |
| `287W` | Sway N Fit摇摆健身机 | switch | InstallationVideo, profile, music, data, Calories, exerciseDuration, PrivacyAgreement, workouts, TutorialVideo |
| `28A6` | 720冰箱除味器智联版 | battery | moreset, connectstate, workmode |
| `28C9` | SMOOKY智能筋膜枪Y10 | video | Updates, times, Status, MODE, RPM, TIME, LEVEL, ON |
| `28E9` | 凯丰电子厨房秤 | switch | unit, tare |
| `28EB` | 杜克ES2智能厨房秤 | peel | foodWeight, unit, state, Save, History, Subtract, Accumulate |
| `28FA` | 凯丰电子厨房秤 | switch | unit, tare |
| `28RD` | 名豆之约通断器 | switch | — |
| `28UA` | 得途 烯时代 石墨烯发热无线按摩眼罩 GSee2 | switch | SetTemperature, MassageMode, RemindWindow, Record, Mode, SetTimer, DeviceStatus, Timer, Temperature, Remind, Power |
| `28UD` | 得途 烯时代 石墨烯发热无线按摩护颈GNeck2 | switch | DeviceStatus, Temperature, Power, Timer, Remind, Mode, SetTemperature, MassageMode, Record, SetTimer, RemindWindow |
| `28UF` | 得途 烯时代 石墨烯发热无线按摩眼罩 GSee3 | switch | Power, Remind, DeviceStatus, Timer, Temperature, Mode, SetTimer, MassageMode, Record, RemindWindow, SetTemperature |
| `28UG` | 得途 烯时代 石墨烯发热无线按摩护颈GNeck3 | switch | RemindWindow, Record, SetTimer, MassageMode, SetTemperature, Mode, Remind, Power, Timer, Temperature, DeviceStatus |
| `28VG` | 电动滑板车G1 | switch | electricquantity, backlitSettings, Gears, singleMileage, FirmwareUpdate, currentSpeed, OurProducts, ConnectionStatus, AlarmInformation, cruiseControl, speedUnit, totalMileage, ProductInformation, RestoreFactorySettings, headlight, PrivacyAgreement |
| `28VP` | 柯璐斯雾化加湿器 | alarm | JS, WH, DS, BS, WL, LD, TS, WS |
| `290K` | MT1 Neo 智能骑行头盔 | switch | autoon, right, turn, Autooff, led, bat |
| `2957` | 万象智能数显保温杯 | temperature | lowbattterywarning, lookup, Temperatureunit, homepage, Moresettings, temperaturerange, interval, state, Battery, frequency, Regularreminder |
| `295A` | UKA智能保温杯 | temperature | lowpower, Electricity, Customtea, scentedtea, state, Lowtemperature, blacktea, GreenTea, doubleclick, WaterTime |
| `2968` | 安视睿智能监测枕 | sleepstatus | realmsg, sleepDataB, sleepDataA |
| `2969` | OFEIS智能飞力士棒 | model | totalcalories, Lowbatterywarning, frequency, Amplitude, kcal, COUNT, Bodydata, Electricity, PowerSwitch |
| `2982` | 名豆之约智能插座10A | switch | protectTimer, electricity, protect, powerElectricity |
| `2983` | 名豆之约智能插座16A | switch | electricity, powerElectricity |
| `298C` | 艾力斯特按摩椅R2S | switch | nID, Other, SitAdjustment, Intensity3D, Bluetooth, VoiceControl, Shoulder, Timing, Collector, Recommend, Manual, Auto, State |
| `2999` | 5G通信壳 | switch | — |
| `29BA` | 舍见智能插座 | switch | — |
| `29BZ` | S1智慧出行头盔 | switch | TrackAlarm, LED, VoiceControl, Autooff, autoon, Light, bat |
| `29CV` | BH60SE Neo智能骑行头盔 | switch | autoon, right, turn, Autooff, led, bat |
| `29DY` | 飞科智能剃须刀FS892 | status | Upgrade, Remaining, Lifespan, connect, Class, Records, Using |
| `29Q4` | POSO场景面板 | switch | scene6, scene5, scene4, scene3, scene2, scene1 |
| `29SW` | 麦瑞克9D1S筋膜枪 | commonMode1 | QDTZ, DCDL, SYZD, DWTJ |
| `29TS` | 万达康智能哑铃 | battery | sportmode, devicestatus, userdata, paraset, sportdata, eqweight, otaupdate |
| `29XA` | 欧井智能除湿机OJ-128E | switch | commonFaultDetection, SetDUM, Countdown, SetMode, HUM, Temp |
| `29XD` | 欧井智能除湿机OJ-550EP | switch | commonFaultDetection, SetDUM, Countdown, SetSpeed, Purify, Temp, HUM, SetMode |
| `2A8S` | sraum1路开关面板 | switch | scene4, scene3, scene2, scene1 |
| `2AAJ` | 艾特单键开关 | switch1 | — |
| `2AB4` | 万达康随动收腹机 | reset | Count2AB4, times, power |
| `2AB6` | 万达康仰卧划船机 | reset | WonderCore2, power, times, Count2AB6 |
| `2AB7` | 0压智能枕 | status | privacy, shake, bodyMove, respiratoryRate, heartRate, electric |
| `2ABO` | 永林PLC网关面板 | discovery | devOta |
| `2ACB` | 领普自发电无线门铃 | volume | selectmusic, selectkey, playmusic, bellstatus, bellops, keysettings |
| `2ACX` | 百叶帘 | action | openerAngle |
| `2AD1` | 自清洁无线擦地吸尘器 ONE X | status | commonFilterElement1, commonFilterElement2, commonFaultDetection, screenbright, cleanarea, cleanmark, screenctrl, calorie, powersetting, worktime, batterylevel |
| `2AED` |  | battery | button1, button2, button3, button4 |
| `2AK0` | 艾特燃气报警器 | alarm | — |
| `2AK1` | 艾特紧急按钮 | pushButton | — |
| `2AK4` | 艾特人体红外传感器 | status | — |
| `2AK5` | 艾特插座 | switch | — |
| `2AK6` | 艾特窗帘控制器 | mode | — |
| `2AK9` | 全创拉力绳 | switch | personInfo, sportInfo, heartRate, calorie, exerciseCount, durationTime |
| `2AKA` | 全创蝴蝶绳 | switch | personInfo, sportInfo, heartRate, calorie, exerciseCount, durationTime |
| `2AKB` | 全创健腹轮 | switch | personInfo, sportInfo, heartRate, calorie, exerciseCount, durationTime |
| `2AKC` | 全创跳绳 | switch | personInfo, heartRate, calorie, exerciseCount, durationTime |
| `2AKD` | 全创哑铃 | switch | personInfo, sportInfo, heartRate, calorie, exerciseCount, durationTime |
| `2AKH` | SDBO斯迪博智能电动牙刷 | commonMode1 | F006, F005, F004, F003, F002, F001 |
| `2ANU` | VSITOO智能马克杯 | temp | reminder, heating |
| `2AO8` | 鸿雁智能主机III型 | switch | devOta |
| `2API` | 晶讯mesh网关 | discovery | devList, addDevice, groupControl, group1, group2, group3, group4 |
| `2AQA` | 锐亿电动牙刷 | commonMode1 | currentcapacity, oscillatorstrength, record, Startingbrushing, morefeature, state, frequency |
| `2AS7` | 锐亿理发器 | switch | — |
| `2ATT` |  | switch | — |
| `2AUX` | H2OFLOSS惠齿智能冲牙器 | commonMode1 | F006, F005, F004, F002, F001 |
| `2AWL` | 锐亿剃须刀 | switch | state, record, time, function, implemented, frequency, currentcapacity |
| `2AWN` | 华为智选 JIMMY 智能手持无线吸尘器 1S | tips | — |
| `2B3F` | 天博智-科学队长3 | switch | DeviceControl110, DeviceState102, DeviceState000103, DeviceState0000104, DeviceControl000109, DeviceControl000108, DeviceContol000107, DeviceControl000106, DeviceState000105 |
| `2B49` | 探梦者智能电动滑板车 | switch | — |
| `2B4N` | 倍轻松空气按摩颈枕 | switch | firmware, siestamode, travelmode, necksmode, hotswitch, timing, nourishingmode, neckmode, activatingmode |
| `2B58` | MixSwitch超级智能开关-一开 | switch | — |
| `2B5B` | MixSwitch超级智能情景开关 | battery | — |
| `2B5N` | 智能药盒 | switch | — |
| `2B6J` | 长虹足浴盆 | switch | — |
| `2B6R` | KUS筋膜枪 | switch | — |
| `2B7W` | 百普瑞智能便携电热水壶 | switch | watertemperature, Targettemperature, state |
| `2BBW` | MixPad S超级智能开关 | discovery | ota |
| `2BDJ` | 求助按钮面板尊享版 | pushButton | — |
| `2BGF` | 欧普蓝牙MESH面板-双键 | battery | — |
| `2BGG` | 欧普蓝牙MESH面板-四键 | battery | — |
| `2BNR` | 浪木T98型茶吧机 | speed | — |
| `2BO4` | 堡丽全屋中控主机 | reset | autoScene, manualScene, clickedScene |
| `2BO5` | 堡丽触点开关 | switch | — |
| `2BO6` | 堡丽开关卷帘 | action | — |
| `2BO7` |  | switch | — |
| `2BO9` | 堡丽开关灯（底盒开关控制器） | switch | — |
| `2BOO` | 堡丽人体存在传感器 | status | — |
| `2BOQ` | 堡丽人体移动传感器 | status | — |
| `2BOV` |  | switch | — |
| `2BOZ` | 堡丽紧急按钮 | pushButton | — |
| `2BPG` | 318智能运动头盔 | switch | testMode, goMode, turnMode, thisTime, totalTime, ledLevel, keyBattery, breakSwitch, helmetBattery |
| `2BQ0` | 华为智选 JIMMY 智能手持无限吸尘器 | tips | — |
| `2BQI` | 瑞晶智能中控主机 | discovery | devList, addDevice, commonFaultDetection |
| `2BRA` | 阳光照明智能杀菌灯 | switch | delay, bat, time, state |
| `2BRG` | 嵌入式大气式灶 | switchLeft | FireLeft |
| `2BRR` | ACEMATIC边缘AI主机 | discovery | — |
| `2BSM` | 瑞晶智能家居网关EASY-HOMECLEVER | discovery | — |
| `2BV8` | 乐骑智能成人滑板车 | commonMemorySwitch1 | — |
| `2BVW` | 关阀门机械手套装 | switch | — |
| `2BWA` | tinyho按摩筋膜枪RELAX | switch | — |
| `2BYA` | 锦绣盒智能网关 | discovery | devList, addDevice, groupControl, group1, group2, group3, group4 |
| `2C1I` | 冰感美肤脱毛仪 | commonMemorySwitch1 | poweroff, Lcemassage, Pulsenumber, poweron, Workinghours, Conuousflash, Singleflash, Remainingnumberofpulse |
| `2C2W` | SMOOTH-XS | commonExecution1 | — |
| `2C5O` | 堡丽百叶帘 | action | openerAngle |
| `2C75` | FSL智能插座 | switch | — |
| `2C7J` | 罗莱热敷舒适枕 | commonTask1 | — |
| `2C7T` | 雅观智能网关 | discovery | — |
| `2C7U` | 西蒙一位智能开关 | switch1 | BackLightMode |
| `2C84` | 西蒙一位智能调光开关 | switch1 | LedPosition, BackLightMode |
| `2C91` | 觅泛MINi筋膜枪 | battery | Usetime, Gear, Workingstatus |
| `2C97` | 锐亿剃须刀 | switch | — |
| `2CAB` | 大拿涡轮六叶剃须刀 | commonMemorySwitch1 | recommended, Morefunctions, Usingtherecord, Cuttingheadwhen, Shavingspeed, Shavingtime, electricity |
| `2CAG` | 大拿电动理发器 | commonMemorySwitch1 | Directexperience, Usingtherecord, Adultmode, Suctionsendmodel, Childrensmodel, time, electricity |
| `2CDJ` | ACEMATIC窗帘电机 | mode | — |
| `2CJU` | MINI肌肉按摩器 | gear | commonFaultDetection, UsageCounter, Power, LifeTimer, CountDown |
| `2CJW` | 叶绿体一键情景面板 | battery | — |
| `2CJX` | 叶绿体二键情景面板 | battery | — |
| `2CJY` | 叶绿体三键情景面板 | battery | — |
| `2CJZ` | 叶绿体单火一路墙壁开关 | switch1 | — |
| `2CM5` | 斯波阿斯儿童篮球机 | switch | pinglv, sudu |
| `2CN1` | 英尔健筋膜枪 | switch | — |
| `2CNX` | 喜临门助眠音乐枕 | commonExecution1 | — |
| `2COA` | 智能蒸汽眼罩 | switch | — |
| `2CUR` | 麦乐克燃气泄漏传感器 | alarm | commonFaultDetection |
| `2CUT` | 智能矫姿精灵 | switch | — |
| `2CUZ` | 吸顶式燃气传感器套装 | alarm | — |
| `2CV0` | 吸顶式烟雾传感器套装 | alarm | — |
| `2CVF` | 单键智能开关面板时尚版 | switch | — |
| `2CVY` | 南方家居智能护颈枕 | status | — |
| `2CXR` | VANOW智能水杯 | temperature | alarmTime1, drinkStatus, lastTime, time, wish |
| `2D4Z` | 360儿童安全座椅 | switch | gequ, deng, yin, feng |
| `2D56` | 亿健智能筋膜枪 | switch | — |
| `2D5Y` | 锐亿剃须刀373 | switch | record, function, state, Time, frequency, Currentcapacity |
| `2D7W` | 三思杀菌台灯 | switch | SterilizationTime, ChildLock |
| `2D84` | yahushi牙护士智能声波电动牙刷 | commonMode1 | F006, F005, F004, F002, F001 |
| `2D87` | yahushi牙护士智能冲牙器 | commonMode1 | F006, F005, F004, F003, F002, F001 |
| `2DAL` | 万达康 SlideFit健身滑板 | reset | times, WonderCodeSlideFit, power, WonderCoreSlideFit |
| `2DAP` | 万达康轻巧版六合一健腹机 | reset | WonderCodeSmart1, times, power |
| `2DAR` | 万达康收腹机 | reset | WonderCore2, WonderCode2, times, power |
| `2DD4` | 远程智能陪读机 | switch | rssi, register, reminder, homework |
| `2DDZ` | 外研通智能笔 | battery | verifyCode, registerInfo, studyInfo |
| `2DE0` | Gimbal Pro-L7C-Pro | switch | — |
| `2DE5` | 小恬次氯酸钠发生器 | switch | workInfo |
| `2DEX` | 壁挂式声光报警器套装 | switch | — |
| `2DFT` | 便携智能剃须刀 | switch | tip, Cleantip, electricity, Shavingtime, Shavingspeed, Cuttingheadwhen, Usingtherecord, Morefunctions, recommended |
| `2DGH` | 极米投影仪H3 | switch | FOCUS, VOLUMEPRESS, FOCUSLEFT, FOCUSRIGHT, FOCUSAUTO, MOVEHOME, MENU, HOME, BACK, VOLUMEDOWN, VOLUMEUP, DPADCENTER, DPADRIGHT, DPADLEFT, DPADDOWN, DPADUP, KPPOWER, RESTART, POWER |
| `2DGU` | 梦洁睡眠监测枕 | battery | — |
| `2DNV` | 维尔森香薰助眠枕 | status | — |
| `2DO1` | 求助按钮面板时尚版 | pushButton | — |
| `2DO4` | 讯飞智能录音笔H1 | commonMode1 | SendToH1Device |
| `2DPK` | YASI雅玺便捷式冲牙器-大奶瓶 | commonMode1 | F006, F005, F004, F003, F002, F001 |
| `2DPO` | YASI雅玺便捷式冲牙器-水晶石 | commonMode1 | F006, F005, F004, F003, F002, F001 |
| `2DPP` | YASI雅玺便捷式冲牙器-太空舱 | commonMode1 | F001, F002, F003, F004, F005, F006 |
| `2DPY` | 艾诗摩尔健发梳 | mode | UsageRecord, EMS, power, days, Status, clear, time |
| `2DQG` | 特美刻智能玻璃杯 | temp | drinkwater, power |
| `2DQX` | 汇优尚品黑头铲 | commonMode1 | — |
| `2DR8` | 力速筋膜枪 | gear | commonFaultDetection, star |
| `2DRA` | Maketec磁控动感单车 | speed | tip, electric, mileage, Stepped, totalKal |
| `2DRB` | 汇优尚品可视化吸黑头仪 | commonMode1 | — |
| `2DRL` | 计客超级魔方i3 | battery | history, intro, rotate |
| `2DU1` | 不锈钢真空保温杯 | temperature | alarmTime1, Currenttemperature, loss, count |
| `2DU6` | 呼噜圈智能喉部脉冲止鼾器 | battery | Sensitivity, SleepReport, delay, Connected, interference |
| `2DUZ` | 单键智能开关面板尊享版 | switch | — |
| `2DZU` | 奥克斯动感单车 | speed | TotalSportNum, tip, electric, mileage, totalKal, Stepped |
| `2E0K` | BMC呼吸机 | switch | TreatPressure, AVGPressure, Pressure95, AHI, AI, HI, CAI, AvgLeak, Leak95, LeakTime |
| `2E1I` | VANOW智能玻璃杯 | temperature | alarmTime1, drinkStatus, lastTime, drinkwaterHistory, wish, time |
| `2E1J` | VANOW智能泡茶玻璃杯 | temperature | alarmTime1, drinkStatus, lastTime, drinkwaterHistory, wish, time |
| `2E1K` | VANOW智能泡茶杯 | temperature | alarmTime1, drinkStatus, lastTime, drinkwaterHistory, wish, time |
| `2E3O` | 金稻负离子电吹风 | commonMode1 | Shift |
| `2E4M` | 苏泊尔智能物联保温杯 | temp | power, restScreen, TDS, remind |
| `2E5V` | 易跑Y3筋膜枪 | speed | gearshow, time, Gears, onoff |
| `2EJ1` | VANOW茶水分离智能杯 | temperature | alarmTime1, drinkStatus, lastTime, wish, drinkwaterHistory |
| `2EJP` | SKG智能颈椎按摩仪 | mode | collection, ModeLib, Voice, BatteryPower, EmsLevel, heatLevel |
| `2EKT` | 乐骑智选滑板车 | commonMode1 | Speed, Light, Help, Batty, Mode, BettyLow, Lock, StartMethod, CruiseControl, MoreFunction, TotalTrip, SpeedUnit, RemainingMileage, RidingRecord |
| `2EL0` | 火鸡智能刀架 | disinfect | report, State, Settingtime, Sterilization |
| `2ELY` | 龙泉智家一路墙壁开关 | switch | — |
| `2EN3` | 俏蜻蜓便携式灭蚊灯 | mode | time, Powerstate |
| `2EPG` | 优创生活智能跳绳 | switch | sportMode, maximalJump, stopCount, avgSpeed, calorie, sportTime, sportCount, device, sportHistory |
| `2EWN` | 盯盯拍智慧后视镜S5 | commonMode1 | — |
| `2EY7` | 昕科智能电蚊香 | mode | Surplus, TimerOFF, Powerstate, Environmentalspace, TimerON |
| `2F01` | 凯胜眼部按摩器 | switch | WDTJ, QY, ZD, RF, MS, RFWD, SYSJ, DCDL |
| `2F2Z` | 汗马动感单车 | speed | tip, electric, TotalSportNum, mileage, totalKal, Stepped |
| `2F7D` | 凯胜眼部美容仪 | switch | ZDJW, EMS, ZDSF, ZDLD, DCDL, SYSJ, RFWD, MS, RF, WDTJ |
| `2F9X` | Gimbal Pro L9pro | battery | gimbalFollowMode |
| `2FJT` | SKG 按摩腰带 Hi-W7 | switch | collection, SceneMode, customMode, EmsLevel, BattPower, HeatLevel, MasgTimer, massageKeyLock |
| `2FOH` | IWARM 智能温控外套 | switch | commonFaultDetection, deviceMode, HeatingState, deviceControl, temperatureView |
| `2FPO` | 电动自行车D1 Pro | mode | AutomaticHeadlight, PrivacyAgreement, Maintenance, SafeDriving, ClearData, BacklightIntensity, UserWeight, FitnessRoute, ElectronicBrake, PowerLevel, Automatically, Headlights, Lock, SpeedGears, SingleMileage, SingleCalorie, CurrentSpeed, SteppedFrequency |
| `2FRG` | 新日小风雅Q3 | alarm | powStatus, NFC, diagnosis, carLock, remainEle, remainKm, openSeat, OTA |
| `2FRH` | 新日Q5 22版 | alarm | openSeat, OTA, remainEle, carLock, NFC, diagnosis, powStatus |
| `2FRI` | 新日QA1 2.0 | alarm | powStatus, NFC, diagnosis, remainEle, OTA, carLock |
| `2FTN` | 好来喜电动童车SX2028 | lock | gearChange, vehicleControl, headlight, atmosphereLamp, lightControl, rockingCar, Parking, DeviceHota |
| `2FTO` | 好来喜电动童车SX2118 | lock | lightControl, gearChange, headlight, vehicleControl, rockingCar, atmosphereLamp, Parking, DeviceHota |
| `2FTP` | 好来喜电动童车SX1938 | lock | DeviceHota, lightControl, rockingCar, atmosphereLamp, Parking, headlight, gearChange, vehicleControl |
| `2FTR` | 好来喜电动童车SX1818 | lock | DeviceHota, Parking, rockingCar, lightControl, headlight, atmosphereLamp, vehicleControl, gearChange |
| `2FTT` | 好来喜电动童车SX1888 | lock | DeviceHota, Parking, rockingCar, headlight, atmosphereLamp, lightControl, gearChange, vehicleControl |
| `2FTU` | 好来喜电动童车SX2088 | lock | vehicleControl, gearChange, lightControl, headlight, atmosphereLamp, rockingCar, Parking, DeviceHota |
| `2FTV` | 好来喜电动童车SX1928 | lock | vehicleControl, gearChange, headlight, lightControl, atmosphereLamp, rockingCar, Parking, DeviceHota |
| `2FTW` | 好来喜电动童车SX1918 | lock | DeviceHota, rockingCar, Parking, lightControl, headlight, atmosphereLamp, vehicleControl, gearChange |
| `2FTY` | 好来喜电动童车SX2018A | lock | gearChange, vehicleControl, headlight, atmosphereLamp, lightControl, Parking, rockingCar, DeviceHota |
| `2FUV` | 极米吸顶灯投影 L1 | light | POWER1, MENU1, HOME1, RESTART, DPADLEFT, DPADUP, DPADDOWN, VOLUMEUP, DPADCENTER, DPADRIGHT, BACK, VOLUMEDOWN, VOLUMEPRESS, FOCUS, FOCUSLEFT, MOVEHOME, FOCUSRIGHT |
| `2FVQ` | 万达康智能呼啦圈 | battery | fitnessclass, music, sportdata, sportmode, devicestatus, userdata, otaupdate |
| `2G2P` | 飞乐思黑洞安睡眼罩 | switch | Remind, Upgrade, Reset, Mode, Timer, NowTemp, DeviceState, TimeSet, Light, TEMP |
| `2GOQ` | 艾力斯特按摩椅R6S | switch | Health, Recommend, State, Auto, Manual, Collector, Timing, Shoulder, VoiceControl, SitAdjustment, Bluetooth, nID, Other |
| `2GOT` | 富林家用制氧机FL100CW | switch | ota, historyData, deviceState, flowRate, currentRecord, setCountdown, setFlowRate, countdown, totalWorktime, currentWorktime, realtimeData |
| `2GQ2` | AIHOME真丝热敷眼罩 | switch | commonFaultDetection, tempertureView, heatState, temperatureSet |
| `2GR0` | 艾力斯特按摩椅V5 | switch | Manual, Other, nID, BackIntensity, Bluetooth, VoiceControl, SitAdjustment, Timing, Shoulder, Collector, Health, Recommend, Auto, State |
| `2GR6` | 仁豪家居智能儿童桌 | action | MemoryStation, SaveStation, RunStation, ShowHight |
| `2GUE` | 仁豪家居升降办公桌 | action | currentHeight, Station, SaveMemory, commonMemory |
| `2GVI` | 狄耐克智能一路开关面板 | switch | — |
| `2H1E` | 值米下巴按摩器 | battery | privacy, TurnoverTimes, delayed, dataMonitoring, SnoreNumber, MassageNumber, SleepTime, ScoreDegree, MassageScore, SleepScore, SnoringDuration, MassageIntensity |
| `2H38` | 凯胜眼部按摩器 | switch | SYSJ, DCDL, RFWD, QY, MS, ZD, RF, WDTJ |
| `2H4L` | SKG Hi-K3 倍护3 | switch | VoicePacket, VoiceAnnouncements, collection, SceneMode, BattPower, Countdown, HeatLevel, EmsLevel, customMode |
| `2H6G` | 便携式气压按摩系统 | switch | Preferences, Recommended, Strength, Alarm, BetteryLevel, Countdown, Specification, connect, Personal, MassageMode |
| `2HC4` | 电动自行车M1 | gear | upgrade, vehicleinformation, vehiclestate, headlight, electricquantity, cycling, connectionstatus, meter, gears, information |
| `2HO0` | 上谷智能往复式剃须刀 | status | btConnection, UseTime, BatteryLevel, SmartLock, AfterGuide |
| `2HSK` | FOOXMET智能温控裤 | switch | commonFaultDetection, tempertureView, deviceMode, heatingState, deviceControl |
| `2HSL` | FOOXMET智能温控腰包 | switch | commonFaultDetection, heatingState, tempertureView, deviceControl, deviceMode |
| `2HTE` | FOOXMET智能温控马甲 | switch | commonFaultDetection, deviceMode, heatingState, tempertureView, deviceControl |
| `2HTN` | 智能剃须刀2130 | status | AbnormalLowBattery, BluetoothStatus, DevCharge, DevVbatt, WorkStatus |
| `2I10` | 莱轻松智能暖宫腰带 | switch | commonFaultDetection, timedFuntion, messageStall, fomentTemperature, batteryView |
| `2I2M` | 超迷你肌肉按摩器 | Switch | Revolutions, MassageMode, connect, Personal, Specification, BetteryLevel, Countdown, Alarm, Recommended |
| `2I3R` | 酷轻松石墨烯发热时尚马甲 | model | continuityMode, rearStatus, RearTEMP, FrontTEMP, rearHeating, workstatus, timing, frontHeating, RemainingHours |
| `2I4E` | 5G通信壳 618 | switch | — |
| `2I8R` | 木林森智联车载氧吧 | switch | Lowpoweralarm, Equipmentstatus, PM2D5, timeSync, CronJob, powerState, anion, O3switch, fanSpeed |
| `2I91` | FOOXMET智能温控围巾 | switch | commonFaultDetection, deviceMode, tempertureView, deviceControl, heatingState |
| `2I93` | 智能喉部脉冲按摩器 | switch | FaultAlarm, Batterydisplay, InterventionIntensity, Connected, Interventiondelay, SleepReport, Sensitivity |
| `2I9O` | 华为智选 哈尔斯智能水杯 弹盖款 | currentTemperature | canvasData5, canvasData4, canvasData3, canvasData2, canvasData1, canvasData, canvasConfig, darkWeekTarget, drinkRemind, startTimes, drinkTargetDefault, drinkTarget, myHashCode, waterWeeksIntake, drinkIntake, drinkTemperature |
| `2IAV` | 电子安全水阀 | waterUseData | flowVelocity, tds, deviceAlarm |
| `2ICL` | Smooky智能呼啦圈 | workStatus | totalTime, notice, Record, bodyData, currentExpend, Mode, Switch1, Battery, CAL, currentContinueCount, interruptTimes, instantaneousSpeed, TIME, COUNT |
| `2IFF` | 香百年后视镜智能香薰机 | Switch | Bluetoothstatus, Instruction, Collection, Kinds, Anion, Strength, Loop, AromaSelect, Residue |
| `2IGO` | 欧普蓝牙Mesh小夜灯 | switch | toggleSwitch, commonFaultDetection |
| `2IHC` | 爱华仕智能花朵箱 | status | Led |
| `2INC` | 智能空调控制器 | temperature | airSwitch, airKey |
| `2INL` | 艾家智能一位开关 | switch | lightness |
| `2IRM` | 燃动智能单杠 | battery | paraset, historicaldata, fitness, userdata, sportdata, sportmode, devicestatus, otaupdate |
| `2ISY` | 澳莱克林商务直饮机 | status | timerset, filterstatus, faultprompt, watertemperature, dts, afterservice |
| `2IXY` | 惠尔顿智转PRO MAX | battery | SupportLegStatus, SeatStatus, RotationStatus, Buckle, RightISOFIXstatus, LeftISOFIXstatus |
| `2IYK` | 十字勋章智能通勤背包 | sterilize | commonFaultDetection, PowerSwitch, Tone, Finder, Battery |
| `2IYO` | 十字勋章智能差旅扩展背包 | sterilize | Finder, PowerSwitch, Tone, Battery, Status |
| `2IYP` | 十字勋章智能商务扩展背包 | sterilize | Status, Battery, Tone, PowerSwitch, Finder |
| `2IYS` | 十字勋章智能时尚通勤背包 | sterilize | Finder, PowerSwitch, Tone, Battery, Status |
| `2IZ0` | 十字勋章智能抗菌旅行箱 | sterilize | commonFaultDetection, Status, LedColors, Battery, Tone, LedMode, LedLum, PowerSwitch, LightEffects |
| `2IZ1` | 十字勋章智能合金行李箱 | sterilize | commonFaultDetection, PowerSwitch, Tone, Battery, Status |
| `2IZ3` | 5G通信壳 658 | switch | — |
| `2IZ4` | 5G通信壳 688 | switch | — |
| `2J34` | VTT智能筋膜枪 | switch | workstate, TIME, ReTime, Speed, value |
| `2J37` | 酷轻松石墨烯简约款马甲 | model | RemainingHours, frontHeating, timing, FrontTEMP, rearHeating, workstatus, rearStatus, RearTEMP, continuityMode |
| `2J90` | 艾力斯特按摩椅S730H | switch | Other, nID, SitAdjustment, Bluetooth, VoiceControl, Shoulder, Timing, Manual, Collector, State, Auto, Recommend |
| `2JBL` | LINKY健康拐杖 | workStatus | btConnection, alertMessage, useInfo, instruction, course, sportTarget, database, averageJitter, averageSports, averageBearing, power |
| `2JDF` | 拉维莱特智慧酒柜LT-1270AW1 | temperature | commonFaultDetection, Connection, Mode, Door |
| `2JFK` | FOOXMET智能温控外套 | switch | commonFaultDetection, tempertureView, deviceControl, heatingState, deviceMode |
| `2JG4` | FOOXMET智能温控披肩 | switch | commonFaultDetection, heatingState, deviceControl, tempertureView, deviceMode |
| `2JGU` | FOOXMET智能温控背包 | switch | commonFaultDetection, deviceControl, tempertureView, heatingState, deviceMode |
| `2JH9` | 波司登智能温控科技羽绒服 | switch | commonFaultDetection, heatingState, tempertureView, deviceControl, deviceMode |
| `2JHA` | 波司登智能温控科技羽绒马甲 | switch | commonFaultDetection, deviceMode, deviceControl, tempertureView, heatingState |
| `2JLB` | gb SMART儿童座椅通风垫 | mode | close, devDesc, timeOff, wind, devStatus, connectstatus |
| `2JOK` | VSITOO智能咖啡电子秤 | battery | stage, sec, min, preWater1, preWater0, weight, preWeight, charge |
| `2JRM` | PXN方向盘 | light | state, general, response, params, ShifterMapping, PedalMapping, PanelMapping |
| `2JTZ` | 盯盯拍车载智慧屏Pro | commonMode1 | — |
| `2JUA` | 邮差 | switch | vehicleDiag, remainBattery, batteryTemp, autoLock, saddleOpen, Locked, remainingMileage, voiceBroadcast, derviceStatus |
| `2JVR` | SMK石墨烯智能护具 | switch | RemainingHours, EquipmentStatus, button, CurrentTemperature, level, TIME, Gear, TEMP, MODE |
| `2JVZ` | 巢居全新360度取暖器N3-C2200HA | switch | CHILDLOCK, voice, Currenttemperature, Lightinducedsleep, purify, Lightcolor, Modeselection, timing |
| `2JYT` | 一米大流量智能净水器600X | status | filterElement1, filterElement2, filterElement3, totalPurifyWater, commonFaultDetection, Cleaning, pureWater, rawWaterTDS |
| `2JZI` | 乐维熺红外理疗仪S01 | switch | aftersaleservice, devicestatus, Countdown, Gear |
| `2K32` | EraClean世净超声波清洗机 | Switch | UserG, Status, AbnormalPrompt, SemiAutomatic, Clear, Sterilization, WorkTime |
| `2K3K` | 贝氪智能托腰椅C1 | battery | sedentaryTime, BeepTips, ChairStatus, RunMode, Version, Bat, Pressure |
| `2K5N` | 智能清洗一体机 | battery | WaterYield, WaterPressure, Instructions, Gear, ChildLock, BatteryLife |
| `2KLD` | 哈尔斯智能水杯 便捷电热杯 | currentTemperature | HotMode, HotState, ConstantTemperature, FindCup, Update, ConnectStatus, Temperature, Buzzer |
| `2KPT` | 麦瑞克9Dmini筋膜枪 | commonMode1 | GZZT, DWTJ, SYZD, DCDL, QDTZ |
| `2KPV` | 5G通信壳 698 | switch | — |
| `2KUO` | 智能蒸汽护眼仪Pro | model | Afterservice, WhiteNoise, Meditation, EyeCare, showUseTime, VOL, promptTone, temperture, strength, powerShow, bleStatus |
| `2KVG` | 行李官智能除菌旅行箱 | sterilize | Status, Battery, Tone, PowerSwitch, Finder |
| `2L5L` | 嘿码智能剃须刀BC9000 | status | Lock, AlarmMessage, OuterCluter, Speed, Worktime, CleanTime, CutterTime, WorkMode, WorkStatus, Ota, Power, Version |
| `2L5P` | 智能加热护膝 | switch | Warning, DeviceSatus, CurrentTemp, BatteryLevel, Heating, Massage, OTAUpgrade, CountDownOff |
| `2L5Z` | 爱里森电子琴 | status | yinse, jiezou, song, jiepai, jiaoxue, led |
| `2L8I` | 物联网水表 | waterMeterReading | hotline |
| `2LMH` | 根元智能运动包 | switch | Mode, LightingDelay, batteryState, RemainingCapacity, WorkTime, leftTime, lightingState, RingLampBrightness |
| `2LR3` | iSteady XE Kit | battery | ModeSwitch, RockerControl |
| `2LRK` | 博芬智能酒柜BF-1900AU1 | temperature | number, commonFaultDetection |
| `2LWB` | 酷轻松石墨烯智能护膝仪 | workMode | Count, tempSetting, Temp, Massage, Elec, Remaining, myCollection, Warning, connect, ota, tlv |
| `2LX2` | 在鸿学生终端 | battery | turningOffScreen |
| `2M4P` | 台铃YO兔 | switch | Status, voiceBroadcast, saddleOpen, remainingMileage, Locked, derviceStatus, remainBattery |
| `2M4T` | 台铃XTM2.0 | switch | remainBattery, derviceStatus, Locked, remainingMileage, saddleOpen, voiceBroadcast, Status |
| `2M4U` | 台铃狂飙60超能版KS | switch | remainBattery, derviceStatus, Locked, remainingMileage, saddleOpen, Status, voiceBroadcast |
| `2M68` | 值米智能下巴按摩器 | battery | SleepingPositionData, SleepDataStatistics, SleepingPosition, SleepQuality, SnoringDuration, MassageIntensity, SnoreNumber, SleepTime, SleepScore, MassageScore, delayed, privacy, MassageNumber, dataMonitoring, TurnoverTimes, ScoreDegree |
| `2M7Y` | 良品主义智能热敷腰带 | switch | AlarmMessage, WorkStatus, Ota, LastTime, Vibrate, Heating, Power, Countdown |
| `2M8O` | 舒怡温润床垫 | switch | aboutchange, currenttemp, settemp, longvave, modechange, oldmode, time |
| `2MDH` | 台铃-标兵2.0 | switch | voiceBroadcast, Status, saddleOpen, remainingMileage, Locked, derviceStatus, remainBattery |
| `2MDI` | 台铃-劲风EB | switch | Status, voiceBroadcast, saddleOpen, remainingMileage, Locked, derviceStatus, remainBattery |
| `2MDJ` | 台铃-周末 | switch | voiceBroadcast, Status, saddleOpen, remainingMileage, Locked, derviceStatus, remainBattery |
| `2MDK` | 台铃-塞北 | switch | voiceBroadcast, Status, saddleOpen, Locked, remainingMileage, derviceStatus, remainBattery |
| `2MDN` | 台铃-夺冠EB | switch | Status, voiceBroadcast, saddleOpen, remainingMileage, Locked, derviceStatus, remainBattery |
| `2MDO` | 台铃-潮达 | switch | Status, voiceBroadcast, saddleOpen, remainingMileage, Locked, derviceStatus, remainBattery |
| `2MDP` | 台铃-天鹅 | switch | voiceBroadcast, Status, saddleOpen, remainingMileage, Locked, derviceStatus, remainBattery |
| `2MDQ` | 台铃-未莱 | switch | voiceBroadcast, Status, saddleOpen, remainingMileage, Locked, derviceStatus, remainBattery |
| `2MDR` | 台铃-T300 | switch | voiceBroadcast, Status, saddleOpen, remainingMileage, Locked, remainBattery, derviceStatus |
| `2MDS` | 台铃-摩术 | switch | voiceBroadcast, Status, saddleOpen, remainingMileage, Locked, derviceStatus, remainBattery |
| `2MDT` | 台铃-追风EB | switch | Status, saddleOpen, voiceBroadcast, remainingMileage, derviceStatus, Locked, remainBattery |
| `2MJZ` | SKG颈椎按摩仪G7系列2代豪华款 | Volume | timing, shutdown, SdVoice, redSwitch, BatteryPower, VbMode, pulseMode, heatLevel, ELevel |
| `2MLN` | 思创泓一制氧机 | Switch | InformationReport, WorkTime, Gear, Batteryalarm, Battery, Information, Status |
| `2MPD` | 家用制氧机H-601L | switch | workRecord, onetime, Control, time, oxygenflow, oxygen |
| `2MWB` | 云康宝肩颈按摩仪CMN10C | switch | Information, SetData |
| `2MXT` | 嘿码智能剃须刀BC8010 | status | CleanTime, WorkMode, Version, CutterTime, Worktime, Power, Ota, WorkStatus, AlarmMessage, Speed, Lock |
| `2N1I` | 艾力斯特M6按摩椅 | switch | Other, SitAdjustment, Timing, State, Collector, VoiceControl, Auto, Shoulder, Bluetooth, BackIntensity, Manual |
| `2N44` | 嘿码智能剃须刀BC3000 Pro | status | AlarmMessage, Speed, Lock, CutterTime, Ota, Worktime, WorkStatus, Power, Version, WorkMode, CleanTime, OuterCluter |
| `2N8T` | 嘿码智能剃须刀BC8200 | status | Ota, Lock, AlarmMessage, Speed, WorkStatus, Worktime, Power, CutterTime, CleanTime, WorkMode, Version |
| `2NBO` | 根元托特包 | switch | leftTime, lightingState, RingLampBrightness, RemainingCapacity, WorkTime, LightingDelay, Mode, batteryState |
| `2NF7` | 艾菲斯智能热敷腰带WarmBelt100 | currentTemperature | temperatureMode, alarmTime, timeDown, lowBattery, targetVibration, batteryLevel |
| `2NMI` | 暖通协议网关B39 | faultDetection | heaterGroupList, acGroupList, heaterList, heaterProtocol, freshAirList, port1protocolList, backup, port2protocolList, freshAirGroupList, diagnosis, vrvProtocol, acList, backupData, connectMode, reboot, homeGatewayCap |
| `2NMJ` | 暖通协议网关B39W | faultDetection | heaterGroupList, acGroupList, heaterList, heaterProtocol, freshAirList, backup, port1protocolList, port2protocolList, freshAirGroupList, diagnosis, vrvProtocol, acList, connectMode, backupData, reboot, homeGatewayCap |
| `2O6X` | 霹雳仔智能运动包 | switch1 | WorkTime, leftTime, LightingDelay, Mode, lightingState, RingLampBrightness, RemainingCapacity, batteryState |
| `2O6Y` | 霹雳仔托特包 | switch1 | leftTime, WorkTime, LightingDelay, Mode, batteryState, RemainingCapacity, RingLampBrightness, lightingState |
| `2O8H` | 禾佳舒暖腰带 | currentTemperature | alarmTime, temperatureMode, timeDown, targetVibration, batteryLevel, lowBattery |
| `2OCP` | 若瀑负氧离子机H2 | switch | countdown, totaltime, airQuality, commonFaultDetection, screen, changefilter |
| `2OD1` | 厨余垃圾处理器 | mode | EqReversal, EqGear, EqStart |
| `2OFY` | 安吉尔全屋Mini软水机S3561-F08 | mode | totalWater, remainWater, waterSpeed, filterElement1, inputTds, outputTds, rewaterTime, dayWater, waterPressure, commonFaultDetection |
| `2OSI` | 神通猫筋膜枪 | battery | timedShutdown, workSwitch, countdown, vibrationGear, overCurrentAlarm |
| `2OU9` | 哈尔斯智能水杯 弹盖款2 | battery | waterHoursIntake, drinkTarget, drinkRemind, config, drinkWeekTarget, waterDayIntake, drinkDisturb, drinkWarn, darkWeekTarget, canvasData3, canvasData1, canvasData2, canvasData5, canvasData4, healthRemind, canvasConfig |
| `2OZT` | 怡口牌S82ECM型软水机 | status | totalWorkTime, totalWater, remainWater, waterSpeed, cleanTime, dayWater, commonFaultDetection |
| `2OZV` | 怡口牌ERO162C型反渗透直饮水机 | status | totalWorkTime, dayPurifyWater, filterElement1, filterElement2, totalPurifyWater, commonFaultDetection |
| `2OZW` | 怡口牌EUF205-2型直饮净水机 | status | totalWorkTime, dayPurifyWater, filterElement1, filterElement2, totalPurifyWater, commonFaultDetection |
| `2P5P` | 怡口牌S82WHF型净水机 | status | totalWorkTime, dayPurifyWater, waterSpeed, cleanTime, totalPurifyWater, commonFaultDetection |
| `2QSS` | LCQ690A电控一体机 | seatStatus | foamShield, seatHeating, toiletSetting, washSetting |
| `2QY4` | 尚美源牌QY-UF型超滤净水机 | temperature | filterElement2, outputTds, totalPurifyWater |
| `2RPW` | 大疆云台Osmo Mobile 9 | battery | commonFaultDetection |
| `2RWS` | 中弘暖通网关 B19-H5 | faultDetection | acGroupList, acList, backup, backupData, connectMode, diagnosis, freshAirGroupList, freshAirList, heaterGroupList, heaterList, heaterProtocol, homeGatewayCap, port1protocolList, port2protocolList, reboot, vrvProtocol |
| `2S0N` | 鸿蒙智选 桌面精灵 | switch | commonFaultDetection |
| `2S98` | Awnlux电动车边帐W5530M | light | awning, 车载侧边天幕, commonFaultDetection, add |
| `9MTM` | 智控压力传感器 | alarmBell | — |
| `9MTV` | 智控灭蚊器 | switch | — |
| `9MTX` | 智控断路器 | switch | electric |
| `9MZR` | 智控微波炉 | status | microWave |
| `A001` | 古北WiFi智能插座 | switch | delay, timerID |
| `A073` | 美的智能电饭煲 | status | — |
| `A0DO` | 插座 | switch | — |
| `A0EQ` | 布谷智能扫拖机器人 | status | — |
| `A0GO` | 智能便座 | switch | — |
| `A0GP` | 智能便座PL40 | switch | — |
| `A0KC` | 车辆 | drivingStatus | staticInfo, mileage, hvac, allWindows, doorRear, windowRoofTop1, carLock, carLocating, ignition |
| `A0MC` | 智汇云智能开关 | switch | — |
| `A0N8` | 智汇云智能插座 | switch | — |
| `A0NN` | 智能单通道插座 | switch | — |
| `A0NV` | 智能窗帘 | opener | — |
| `A0OP` | 智能单通道开关 | switch | — |
| `A0UB` | 霍尼韦尔智能控制灯光 | switch | — |
| `A0ZF` | 西门子门窗磁1 | doorEvent | batteryInfo |
| `A107` | 西门子窗帘 | mode01 | — |
| `A108` | 西门子三孔插座1 | switch | — |
| `A10T` | 西门子五孔插座1 | switch | — |
| `A10U` | 西门子五孔插座1 | switch | — |
| `A147` | 汉印智能打印机 | printerStatus | — |
| `A1BW` | 美的净水机 | water | filterElement1, filterElement2 |
| `A2EE` | 净水器 JYW-R782 | status | commonFaultDetection, resetData, filterElementDataPcp, filterElementDataRoc |
| `A2FS` | FC9 OS洗地机 | status | selfcleanswicth, controlVoice, plugStatus, batteryRatio, runMode |
| `A2JK` | 智能单通道机械开关 | switch | — |
| `A2JN` | ZB单通道开关 | switch | — |
| `A2JO` | 恒温恒湿智能开关 | switch | — |
| `A2K7` | 净热一体式反渗透净水机 JYW-RF689s | status | commonFaultDetection, waterPattern, offOn, filterElement, resetData |
| `A2L4` | 智汇云智能开关 | switch | — |
| `A2L6` | 智汇云智能空开 | switch | kwh, limit, devStatus |
| `A2LV` | 门窗传感器 | doorContact | — |
| `A2M1` | 智汇云溢水传感器 | warterAlarm | — |
| `A2M3` | 智汇云紧急按钮 | pushButton | button |
| `A2M4` | 智汇云插卡取电 | cardStatusReport | cardStatus |
| `A2M5` | 智汇云窗帘模块 | action | — |
| `A2MF` | 智汇云机械阀 | valveStatus | — |
| `A2N2` | KEKEN 智能开关1键 | switch1 | backlight2 |
| `A2PP` | 壁挂式单相电表 | volume | Thismonth, Lastmonth, state |
| `A2RL` | 导轨式单相电表4P | volume | Thismonth, Lastmonth, state |
| `A2RT` | 博芬智能酒柜BF1900 | temperature | number, ota |
| `A2TR` | 导轨式单相电表2P | volume | state, Lastmonth, Thismonth |
| `A2WB` | 智汇云智能开关 | switch | — |
| `A2WK` | 智汇云智能开关 | switch | — |
| `A2WL` | 智汇云智能开关 | switch | — |
| `A2WM` | 智汇云轨道式开关 | switch | — |
| `A36B` | 欧派智能一位开关P31 | switch1 | — |
| `A3CW` | COLMO管线机 | childLockSwitch | commonFaultDetection |
| `A3D6` | 美的管线机 | childLockSwitch | commonFaultDetection |
| `A3DB` | 美的净水器 | status | outputTds, commonFaultDetection |
| `A3DC` | 美的茶吧机 | status | commonFaultDetection |
| `A3DH` | 美的净饮机 | status | commonFaultDetection |
| `A3DL` | 美的饮水机 | childLockSwitch | commonFaultDetection |
| `A3FG` | 美的蒸烤一体机 | status | leftTime, ovenSteamer, commonFaultDetection |
| `A3IY` | 老板燃气灶 | workBurnerStatus | — |
| `A3OP` | 美的智能饭煲 | status | cooker, leftTime, commonFaultDetection |
| `A3P3` | 方太智能燃气灶 | workBurnerStatus | — |
| `A3WN` | 滨特尔牌EZ2000型反渗透净水机 | water | filterElement1, filterElement2, outputTds |
| `A3WW` | 安吉尔S3769-F08 b | regenerateSwitch | dayWater, filterElement1, inputTds, outputTds, remainWater, rewaterTime, totalWater, waterPressure, waterSpeed, commonFaultDetection |
| `A3YA` | 安吉尔M7 Home Pro 800(预处理) | switch | filterElement1, filterElement2, totalPurifyWater, commonFaultDetection |
| `A3YC` | 安吉尔M7 Home 800(预处理) | switch | filterElement1, filterElement2, totalPurifyWater, commonFaultDetection |
| `A3YJ` | 舒达AI智适应床垫 | sleepstatus | leftSoftHardness, positionSelect, rightSoftHardness, commonFaultDetection |
| `A3YO` | 滨特尔牌EZ4000型反渗透净水机 | water | filterElement1, filterElement2, outputTds |
| `A402` | 海尔冰箱BCD-617WGHTDB9VBU1 | aiFfSwitch | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A40A` | 卡萨帝冰箱BCD-518WGCFDMGWUU1 | aiFfSwitch | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A40B` | 卡萨帝冰箱BCD-550WGCFDMGDEU1 | aiFfSwitch | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A40H` | 卡萨帝冰箱BCD-540WGCTDMGDEU1 | aiFfSwitch | freezerFloat, refrigeratorFloat, commonFaultDetection |
| `A412` | 卡萨帝指挥家燃气灶 | workBurnerStatus | — |
| `A41A` | 卡萨帝指挥家品字燃气灶 | workBurnerStatus | — |
| `A41T` | 安吉尔净软一体机JC3739-4H | regenerateSwitch | dayWater, filterElement1, filterElement2, hardness, remainWater, rewaterTime, totalWater, waterPressure, waterSpeed, commonFaultDetection |
| `A41U` | 安吉尔净软一体机JC3738-4H | regenerateSwitch | dayWater, filterElement1, filterElement2, hardness, remainWater, rewaterTime, totalWater, waterPressure, waterSpeed, commonFaultDetection |
| `A41V` | 安吉尔净软一体机JC3736-2H | regenerateSwitch | dayWater, filterElement1, filterElement2, hardness, remainWater, rewaterTime, totalWater, waterPressure, waterSpeed, commonFaultDetection |
| `A41W` | 安吉尔净软一体机JC3735-2H | regenerateSwitch | dayWater, filterElement1, filterElement2, hardness, remainWater, rewaterTime, totalWater, waterPressure, waterSpeed, commonFaultDetection |
| `A42U` | 卡萨帝致境燃气灶 | workBurnerStatus | — |
| `A42V` | 卡萨帝指挥家三头燃气灶 | workBurnerStatus | — |
| `K1C7` | 华为路由TC7206 | switch | — |
| `K1C8` | 华为移动路由Pro | switch | — |
| `K1D5` | 华为随行WiFi 3 Pro | switch | — |
| `K1D6` | 华为随行WiFi 3 | switch | — |
| `K1D7` | 华为全屋智能 智能主机 EZ（网线版） | switch | — |
| `K1DL` | 5G CPE 5 | switch | — |
| `K1EU` | 随行WiFi | switch | — |
| `K1F5` | HUAWEI 4G CPE 5 | switch | — |
| `K1F6` | HUAWEI 4G CPE 5 | switch | — |
| `K1F7` | HUAWEI CPE 5R | switch | — |
| `K1FF` | 华为随行WiFi 5 | switch | — |
| `K1FN` | 华为随行WiFi 5 | switch | — |
| `K1FO` | HUAWEI 4G Mobile WiFi 5 | switch | — |
| `K1FV` | 5G Mobile WiFi Pro 5 | switch | — |
| `K1FX` | 华为全屋智能 分布式路由 M1 子路由 | switch | — |
| `K1GA` | 华为随行WiFi 5 eSIM | switch | — |
| `KW02` | 华为智能门锁Pro | lockStatus | networkConnectState, doorBattery, catEyeBattery, lockAlarm, temporaryCipher, alarmEventSetting, catEyeSetting, securitySetting, volumeSetting, keyCards, ciphers, faces, fingers, watchs, walletKeys, event, users |
| `KW03` | 华为智能门锁 | lockStatus | networkConnectState, doorBattery, catEyeBattery, lockAlarm, temporaryCipher, alarmEventSetting, catEyeSetting, securitySetting, volumeSetting, keyCards, ciphers, faces, fingers, watchs, walletKeys, event, users |
| `KW38` | 华为智能门锁 SE 猫眼版 | lockStatus | networkConnectState, doorBattery, catEyeBattery, lockAlarm, temporaryCipher, alarmEventSetting, catEyeSetting, securitySetting, volumeSetting, keyCards, ciphers, faces, fingers, watchs, walletKeys, event, users |
| `KW4X` | 华为智能门锁 SE | lockStatus | networkConnectState, doorBattery, catEyeBattery, lockAlarm, temporaryCipher, alarmEventSetting, catEyeSetting, securitySetting, volumeSetting, keyCards, ciphers, faces, fingers, watchs, walletKeys, event, users |
| `KW57` | 华为智能门锁E311 | lockStatus | networkConnectState, doorBattery, catEyeBattery, lockAlarm, temporaryCipher, alarmEventSetting, catEyeSetting, securitySetting, volumeSetting, keyCards, ciphers, faces, fingers, watchs, walletKeys, event, users |
| `KW58` | 华为智能门锁E310 | lockStatus | networkConnectState, doorBattery, catEyeBattery, lockAlarm, temporaryCipher, alarmEventSetting, catEyeSetting, securitySetting, volumeSetting, keyCards, ciphers, faces, fingers, watchs, walletKeys, event, users |
| `KW59` | 华为智能门锁E211 | lockStatus | networkConnectState, doorBattery, catEyeBattery, lockAlarm, temporaryCipher, alarmEventSetting, catEyeSetting, securitySetting, volumeSetting, keyCards, ciphers, faces, fingers, watchs, walletKeys, event, users |
| `KW5A` | 华为智能门锁E210 | lockStatus | networkConnectState, doorBattery, catEyeBattery, lockAlarm, temporaryCipher, alarmEventSetting, catEyeSetting, securitySetting, volumeSetting, keyCards, ciphers, faces, fingers, watchs, walletKeys, event, users |
| `KW5J` | 华为智能门锁 Plus | lockStatus | networkConnectState, doorBattery, catEyeBattery, lockAlarm, temporaryCipher, alarmEventSetting, catEyeSetting, securitySetting, volumeSetting, keyCards, ciphers, faces, fingers, watchs, walletKeys, event, users |
| `KW5L` | 华为智能门锁 2 Pro | lockStatus | networkConnectState, doorBattery, catEyeBattery, lockAlarm, temporaryCipher, alarmEventSetting, catEyeSetting, securitySetting, volumeSetting, keyCards, ciphers, faces, fingers, watchs, walletKeys, event, users |
| `KW5M` | 华为智能门锁 2 | lockStatus | networkConnectState, doorBattery, catEyeBattery, lockAlarm, temporaryCipher, alarmEventSetting, catEyeSetting, securitySetting, volumeSetting, keyCards, ciphers, faces, fingers, watchs, walletKeys, event, users |
| `KW5N` | 华为智能门锁 2 Ultra | lockStatus | networkConnectState, doorBattery, catEyeBattery, lockAlarm, temporaryCipher, alarmEventSetting, catEyeSetting, securitySetting, volumeSetting, keyCards, ciphers, faces, fingers, watchs, walletKeys, event, users |
| `KW5O` | 华为智能门锁 2尊享版 | lockStatus | networkConnectState, doorBattery, catEyeBattery, lockAlarm, temporaryCipher, alarmEventSetting, catEyeSetting, securitySetting, volumeSetting, keyCards, ciphers, faces, fingers, watchs, walletKeys, event, users |
| `KW5P` | 华为智能门锁 X1 | lockStatus | networkConnectState, doorBattery, catEyeBattery, lockAlarm, temporaryCipher, alarmEventSetting, catEyeSetting, securitySetting, volumeSetting, keyCards, ciphers, faces, fingers, watchs, walletKeys, event, users |
| `KW5Q` | 华为智能门锁E220 | lockStatus | networkConnectState, doorBattery, catEyeBattery, lockAlarm, temporaryCipher, alarmEventSetting, catEyeSetting, securitySetting, volumeSetting, keyCards, ciphers, faces, fingers, watchs, walletKeys, event, users |
| `KW5R` | 华为智能门锁 M2 | lockStatus | networkConnectState, doorBattery, catEyeBattery, lockAlarm, temporaryCipher, alarmEventSetting, catEyeSetting, securitySetting, volumeSetting, keyCards, ciphers, faces, fingers, watchs, walletKeys, event, users |
| `KW5S` | 华为智能门锁L20(C100) | lockStatus | networkConnectState, doorBattery, catEyeBattery, lockAlarm, temporaryCipher, alarmEventSetting, catEyeSetting, securitySetting, volumeSetting, keyCards, ciphers, faces, fingers, watchs, walletKeys, event, users |
| `KW5U` | 华为智能门锁 X1 | lockStatus | networkConnectState, doorBattery, catEyeBattery, lockAlarm, temporaryCipher, alarmEventSetting, catEyeSetting, securitySetting, volumeSetting, keyCards, ciphers, faces, fingers, watchs, walletKeys, event, users |
| `KW5V` | 华为智能门锁 E320 | lockStatus | networkConnectState, doorBattery, catEyeBattery, lockAlarm, temporaryCipher, alarmEventSetting, catEyeSetting, securitySetting, volumeSetting, keyCards, ciphers, faces, fingers, watchs, walletKeys, event, users |
| `KW5W` | 华为智能门锁 2 Pro 尊享版 | lockStatus | networkConnectState, doorBattery, catEyeBattery, lockAlarm, temporaryCipher, alarmEventSetting, catEyeSetting, securitySetting, volumeSetting, keyCards, ciphers, faces, fingers, watchs, walletKeys, event, users |
| `KW5X` | 华为智能门锁 2 Pro 悦享版 | lockStatus | networkConnectState, doorBattery, catEyeBattery, lockAlarm, temporaryCipher, alarmEventSetting, catEyeSetting, securitySetting, volumeSetting, keyCards, ciphers, faces, fingers, watchs, walletKeys, event, users |
| `M0B5` | HUAWEI WATCH Buds | switch | — |
| `M0BW` | HUAWEI WATCH GT Cyber | switch | — |
| `M0C5` | HUAWEI WATCH GT Cyber | switch | — |
| `M0C6` | HUAWEI WATCH GT Cyber | switch | — |
| `M0DC` | HUAWEI WATCH FIT 3 | sleepStatus | — |
| `RX01` | HUAWEI 蓝牙鼠标 | switch | — |
| `RX08` | HUAWEI 无线鼠标 | switch | — |
| `RX09` | HUAWEI 蓝牙鼠标 第二代 | switch | — |
| `RX0A` | HUAWEI 蓝牙鼠标 第二代 | switch | — |
| `RX0G` | HUAWEI 高键程智能键盘 | switch | — |
| `RX1B` | HUAWEI 蓝牙鼠标 第二代 | switch | — |
| `RX1C` | HUAWEI 无线鼠标 第二代 | switch | — |
| `RX1E` | 华为星芒鼠标 | switch | — |
| `RX1G` | 华为星跃鼠标 GT | switch | — |
| `RX1L` | 华为星跃鼠标 SE版本 | switch | — |
| `RX1M` | 华为星跃鼠标 SE悦享版 | switch | — |
| `RX1N` | TBD | switch | — |
| `RX1O` | TBD | switch | — |
| `RX1P` | TBD | switch | — |
| `RX1X` | TBD | switch | — |
| `RX1Y` | TBD | switch | — |
| `RX21` | TBD | switch | — |
| `RX24` | TBD | switch | — |
| `T10X` | HUAWEI MateBook Pro S | workMode | — |
| `T153` | HUAWEI MateBook D 14 | workMode | — |
| `T1AF` | HUAWEI MateBook 14s | workMode | — |
| `T1AG` | HUAWEI MateBook 13s | workMode | — |
| `T1AH` | HUAWEI MateBook X Pro | workMode | — |
| `T1AL` | HUAWEI MateBook 14 | workMode | — |
| `T1AN` | HUAWEI MateBook D 16 | workMode | — |
| `T1AO` | HUAWEI MateBook 16s | workMode | — |
| `T1AS` | HUAWEI MateStation S | workMode | os, cpu, memory, wifi, bluetooth |
| `V0EJ` | 虚拟电子白板 | switch | inputSource |
| `X007` | HUAWEI Sound | discovery | hwaccount, speakerState, smartspeaker, audioplayer, BTIdle |
| `X0A0` | Sound X | discovery | hwaccount, speakerState, smartspeaker, audioplayer, bluetoothnode, BTIdle |
| `X0A2` | 华为AI音箱 2e | discovery | hwaccount, speakerState, smartspeaker, audioplayer, bluetoothnode, BTIdle |
| `X0A3` | HUAWEI Sound Joy | discovery | hwaccount, speakerState, smartspeaker, audioplayer, bluetoothnode, BTIdle |
| `X0A5` | HUAWEI Sound SE | discovery | hwaccount, speakerState, smartspeaker, audioplayer, bluetoothnode, BTIdle |
| `ZCA2` | AI眼镜 | battery | — |
| `ZF01` | 华为全屋智能 智能主机 | switch | clickedScene, devOta |
| `ZF02` | 华为全屋智能 智能主机 | switch | clickedScene, devOta |
| `ZF0B` | 华为全屋智能 智能主机SE | switch | clickedScene, devOta |
| `ZF0C` | 华为全屋智能 智能主机SE | switch | clickedScene, devOta |
| `ZF0J` | 华为全屋智能 智能主机 Lite | switch | — |
| `ZF0M` | 华为鸿蒙智家 智能主机 X2 Pro | switch | clickedScene, devOta |
| `ZF0N` | 华为鸿蒙智家 智能主机 X2 Pro | switch | clickedScene, devOta |
| `ZF0Q` | 华为鸿蒙智家 智能主机 EZ 2 | switch | devOta |
| `ZF0R` | 华为鸿蒙智家 智能主机 X2 | switch | clickedScene, devOta |
| `ZG0H` | 华为全屋智能 蓝牙网关 | discovery | devList, addDevice, bluetooth |
| `ZG0P` | 门磁 | doorContact | — |
| `ZG0Q` | 紧急按钮 | pushButton | — |
| `ZG0R` | 吊灯 | switch | — |
| `ZG0S` | 智能照明 | switch | — |
| `ZG0T` | 床头灯 | switch | — |
| `ZG0U` | 磁吸灯 | switch | — |
| `ZG0V` | 灯带 | switch | — |
| `ZG0W` | 射灯 | switch | — |
| `ZG0X` | 筒灯 | switch | — |
| `ZG0Y` | 吸顶灯 | switch | — |
| `ZG19` | 门铃 | bellSwitch | — |
| `ZG1A` | 红外幕帘传感器 | status | — |
| `ZG1B` | 水浸传感器 | waterAlarm | — |
| `ZG1C` | 烟雾传感器 | alarm | — |
| `ZG1D` | 燃气传感器 | alarm | — |
| `ZG1G` | 干接点开关 | switch | — |
| `ZG1N` | 清理开关 | switch | — |
| `ZG1O` | 勿扰开关 | switch | — |
| `ZG1R` | 家居设备 | switch | — |
| `ZG1X` | 虚拟投影仪开关 | switch | — |
| `ZG2L` | AI超感传感器 Air（WiFi版） | luminance | — |