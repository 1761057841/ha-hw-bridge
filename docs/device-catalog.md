# 华为智慧生活设备目录（ver_202609_hmos）

目录共 **5926** 个可读设备档案（线上清单 5977 条，51 个在 CDN 上拒绝访问）。

其中 **3816 个** 至少有一个服务能被当前集成投影到 Home Assistant，
**649 个** 的服务可以被完全覆盖。

> 判断依据：`DeviceId` 即华为 `prodId`；`profile` 字段指向 `DeviceId/DeviceId.json`。

> 「完全覆盖」= 该设备除系统服务（update/netInfo/timer 等，不需要投影）外的全部服务都有适配器。


## 能投影的设备（按可用服务数排序）

| prodId | 名称 | 型号 | 类型ID | 可用服务 | 缺服务 |
|---|---|---|---|---|---|
| `2NGC` | 720智能空气净化除湿一体机 | CS50-KJ300 | 013 | battery, childLockSwitch, fan, humidity, lightSwitch, mode, pm25, switch, temperature | UVSwitch, airQuality, ambientLight, anionSwitch, cav, city, continueDehumidifySwitch, dehumidify, dehumidifyswitch, faultDetection, filterElement1, monitoringSwitch, stbyMonitor, userFunctions, userInformations, waterTank, weight |
| `2P3N` | 720智能空气净化器3s增强版 | KJ520F-E520 | 013 | childLockSwitch, fan, hcho, humidity, lightSwitch, mode, pm25, switch, temperature | UVSwitch, airQuality, ambientLight, anionSwitch, capabilitySet, cav, cmw, ecoSetting, faultDetection, filterElement1, keyToneSwitch, monitoringSwitch, outdoorPM25, screenSwitch, workStatus |
| `2P3O` | 720智能空气净化器3增强版 | KJ620F-E620 | 013 | childLockSwitch, fan, hcho, humidity, lightSwitch, mode, pm25, switch, temperature | UVSwitch, airQuality, ambientLight, anionSwitch, capabilitySet, cav, cmw, ecoSetting, faultDetection, filterElement1, keyToneSwitch, monitoringSwitch, outdoorPM25, screenSwitch, workStatus |
| `2PD7` | IAM智能消毒空气净化器X5增强版 | KJ800F-X5 | 013 | childLockSwitch, fan, hcho, humidity, lightSwitch, mode, pm25, switch, temperature | airQuality, allergen, ambientLight, anionSwitch, cav, commonFaultDetection, dailyPurifiedAir, ecoSetting, eleKillSwitch, filterElement4, filterElement5, filterElement6, filterElement7, filterElement8, keyToneSwitch, monitoringSwitch, outdoorPM10, outdoorPM25, pm10, screenSwitch, timerTaskId, tvoc, weight |
| `2QQ4` | IAM智能消毒空气净化器X5 Ultra免换芯 | KJ1000F-X5 | 013 | childLockSwitch, fan, hcho, humidity, lightSwitch, mode, pm25, switch, temperature | airQuality, allergen, ambientLight, cav, commonFaultDetection, dailyPurifiedAir, ecoSetting, filterElement4, filterElement6, filterElement7, filterElement8, keyToneSwitch, monitoringSwitch, outdoorPM10, outdoorPM25, pm10, screenSwitch, timerTaskId, tvoc, weight |
| `2RNN` | 亚都空气净化器KJ520F-S520 | KJ520F-S520 | 013 | childLockSwitch, colourMode, fan, hcho, humidity, mode, pm25, switch, temperature | UVSwitch, anionSwitch, faultDetection, filterElement6, indicator, keyToneSwitch, preciseTvoc, timerTaskId |
| `2S2Q` | 720智能空气净化器5 | KJ620F-E620 | 013 | childLockSwitch, fan, hcho, humidity, lightSwitch, mode, pm25, switch, temperature | UVSwitch, airQuality, ambientLight, anionSwitch, capabilitySet, cav, cmw, ecoSetting, faultDetection, filterElement1, keyToneSwitch, monitoringSwitch, outdoorPM25, screenSwitch, workStatus |
| `2MD0` | 720智能空气净化加湿一体机 | SZM1200 | 013 | childLockSwitch, fan, humidity, lightSwitch, mode, pm25, switch, temperature | airQuality, ambientLight, anionSwitch, aromaSwitch, cav, city, faultDetection, filterElement1, filterElement2, filterElement3, monitoringSwitch, stbyMonitor, userFunctions, userInformations, weight |
| `2MLE` | IAM智能净化加湿一体机U7 | SZM2000-U7 | 013 | childLockSwitch, fan, humidity, lightSwitch, mode, pm25, switch, temperature | ambientLight, aromaSwitch, cav, faultDetection, filterElement1, filterElement2, machinePara, monitoringSwitch, weight |
| `2NH2` | 松下空气净化器 | F-153C4PJD | 013 | childLockSwitch, fan, hcho, humidity, mode, pm25, switch, temperature | HCHOsensitivity, TVOCsensitivity, UVSwitch, anionSwitch, darkSwitch, elapsedTimeMode, faultDetection, filterElement6, filterElement7, sensorsensitivity, tvoc |
| `2OBL` | 松下空气净化器 F-PDY150C | F-PDY150C | 013 | childLockSwitch, fan, hcho, humidity, mode, pm25, switch, temperature | HCHOsensitivity, TVOCsensitivity, UVSwitch, anionSwitch, darkSwitch, elapsedTimeMode, faultDetection, filterElement6, filterElement7, sensorsensitivity, tvoc |
| `2ODE` | 松下空气净化器 F-PTY900C | F-PTY900C | 013 | childLockSwitch, fan, hcho, humidity, mode, pm25, switch, temperature | HCHOsensitivity, TVOCsensitivity, UVSwitch, anionSwitch, darkSwitch, elapsedTimeMode, faultDetection, filterElement6, filterElement7, sensorsensitivity, tvoc |
| `2PRF` | 720智能空气净化器 铂境Pro Max | KJ1800F-S20 | 013 | childLockSwitch, fan, hcho, humidity, mode, pm25, switch, temperature | airQuality, allergen, anionSwitch, capabilitySet, cav, faultDetection, filterElement1, fragrance, fragranceInstall, indicator, keyToneSwitch, monitoringSwitch, outdoorPM25, screenSwitch, tvoc, voiceBroadcast, weight |
| `2R8R` | 承弦智能开窗器Pro 内开窗款 | BWN4PYH | 02C | action, alarm, battery, childLockSwitch, lightSwitch, mode, opener, switch | actionSwitch, antipinchMode, antipinchSwitch, changeDirection, commonFaultDetection, openStatus, silencer, soundSwitch, stroke, stroke2, switchSpeed, torque, travel, travel2, voiceSwitch |
| `2R8S` | 承弦智能开窗器Pro 外开窗款 | BWP4PYH | 02C | action, alarm, battery, childLockSwitch, lightSwitch, mode, opener, switch | actionSwitch, antipinchMode, antipinchSwitch, commonFaultDetection, silencer, soundSwitch, stroke, switchSpeed, torque, travel, voiceSwitch |
| `2RU5` | 720智能空气净化器 铂境Pro | KJ1500F-S15 | 013 | childLockSwitch, fan, hcho, humidity, mode, pm25, switch, temperature | airQuality, allergen, anionSwitch, capabilitySet, cav, faultDetection, filterElement1, fragrance, fragranceInstall, indicator, keyToneSwitch, monitoringSwitch, outdoorPM25, screenSwitch, tvoc, weight |
| `2RW0` | 承弦智能开窗器 内开窗款 | BWN4PYH | 02C | action, alarm, battery, childLockSwitch, lightSwitch, mode, opener, switch | actionSwitch, antipinchMode, antipinchSwitch, changeDirection, commonFaultDetection, openStatus, silencer, soundSwitch, stroke, stroke2, switchSpeed, torque, travel, travel2, voiceSwitch |
| `2RW1` | 承弦智能开窗器 外开窗款 | BWP4PYH | 02C | action, alarm, battery, childLockSwitch, lightSwitch, mode, opener, switch | actionSwitch, antipinchMode, antipinchSwitch, commonFaultDetection, silencer, soundSwitch, stroke, switchSpeed, torque, travel, voiceSwitch |
| `2SHD` | 箭牌智能雷达人感浴霸2 Pro | ASW007HM-T | 035 | brightness, cct, fan, humidity, lightSwitch, luminance, status, switch | Motion-activatedNightLightSwitch, autoDrySwitch, autoLightSwitch, autoWarmWindSwitch, automaticWarmWindSwitch, circulationTime, commonFaultDetection, drySwitch, heat, humanSensingStatus, indicator, keyToneSwitch, leftTime, lightOffDelayTime, nightLightSwitch, radarSensingGear, startDryThreshold, sterilizationSwitch, stopDryThreshold, ventilateSwitch, ventilationFan, windSwitch |
| `2SPN` | 夏普除湿机DW-V16HZ-W | DW-V16HZ-W | 09B | childLockSwitch, fan, humidity, lightSwitch, mode, status, switch, temperature | UVSwitch, anionSwitch, commonFaultDetection, drainSwitch, indicator, keyToneSwitch, waterTank |
| `2SPT` | 夏普除湿机DW-V6NZ-C | DW-V6NZ-C | 09B | childLockSwitch, fan, humidity, lightSwitch, mode, status, switch, temperature | anionSwitch, commonFaultDetection, drainSwitch, keyToneSwitch, waterTank |
| `217Z` |  | KK-FA-D11W | 030 | childLockSwitch, fan, humidity, lightSwitch, mode, switch, temperature | filterElement |
| `27DO` | 心智悦新风控制器A1 | RZXK-A1 | 030 | fan, humidity, mode, pm25, status, switch, temperature | co2, cyclic, filterElement1, tvoc |
| `28YI` | 帝源空气净化器 | Y-DY-870 | 013 | fan, hcho, humidity, mode, pm25, switch, temperature | commonFilterElement1, commonFilterElement2, disinfect, timing |
| `2B8J` | 720 全效空气净化器 1Pro | KJ800F-S800 | 013 | childLockSwitch, fan, humidity, mode, pm25, switch, temperature | UVSwitch, anionSwitch, cav, cmw, faultDetection, filterElement1, keytoneSwitch, light, lightSensor, screenSwitch |
| `2BH9` | 新颐空气净化器 | KJ420G-A02 | 013 | childLockSwitch, fan, humidity, mode, pm25, switch, temperature | anionSwitch, faultDetection, filterElement1, timercounter |
| `2FAR` | 协议新风 | MC3-Air | 030 | fan, humidity, mode, pm25, status, switch, temperature | capability, capabilityset, co2, controlStrategy, dhswitch, faultDetection, filterElement1, filterElement2, filterElement3, filterElement4, filterElement5, filterElement6, filterElement7, filterElement8, queryAction, supportDerVirtual, tvoc, windSpeedEx |
| `2JN5` | 720智能空气净化器 3s | KJ500F-E500A | 013 | childLockSwitch, fan, humidity, mode, pm25, switch, temperature | UVSwitch, anionSwitch, cav, cmw, faultDetection, filterElement1, keytoneSwitch, restoreFactory, screenSwitch, stbyMonitor, timerParaValue, tvoc |
| `2LGN` | 720智能空气净化器 3 | KJ600F-E600s | 013 | childLockSwitch, fan, hcho, humidity, mode, pm25, switch | UVSwitch, anionSwitch, cav, city, cmw, faultDetection, filterElement1, keytoneSwitch, screenSwitch, stbyMonitor, userFunctions, userInformations |
| `2LYP` | 720智能空气净化器3Pro | KJ820F-S820 | 013 | childLockSwitch, fan, hcho, humidity, mode, pm25, switch | UVSwitch, airQuality, allergen, cav, city, faultDetection, filterElement1, filterElement2, monitoringSwitch, stbyMonitor, userFunctions, userInformations, voc, weight |
| `2M6F` | 调湿模块-6恒 | MC3-TS1 | 09B | childLockSwitch, humidity, mode, pm25, status, switch, temperature | PromptSwitch, abilityMode, anionSwitch, capability, cleaningTime, drainSwitch, elapsedTimeMode1, elapsedTimeMode2, faultDetection, filterElement1, filterElement2, gear, tvoc, waterGear, wind |
| `2M8K` | IAM智能消毒空气净化器X5 | KJ800F-X5 | 013 | childLockSwitch, fan, hcho, humidity, mode, pm25, switch | anionSwitch, cav, commonFaultDetection, filterElement3, filterElement4, filterElement5, machinePara, machineSet, outdoorPara, tvoc, weight |
| `2MIW` | 九牧智能魔镜 | AC3115-148C-1 | 04A | brightness, cct, humidity, lightMode, lightSwitch, status, temperature | aromaSwitch, aromatherapyGear, aromatherapyMode, aromatherapyStatus, commonFaultDetection, defoggingMode, defoggingThreshold, flavorMode, motionSensingStatus, nightLightMode, nightLightSwitch, personalizedSignature |
| `2NV5` | 亚都空气净化器KJ2000F-T20(Hi) | KJ2000F-T20(Hi) | 013 | childLockSwitch, hcho, humidity, mode, pm25, switch, temperature | UVSwitch, anionSwitch, faultDetection, filterElement6, level, light, screen, sound, timing |
| `2OY9` | 杜亚智能开窗器 外开窗款 | KC1 | 02C | action, battery, childLockSwitch, lightSwitch, mode, opener, switch | actionSwitch, commonFaultDetection, silencer, soundSwitch, stroke, switchSpeed, torque, travel, voiceSwitch |
| `2OYJ` | 承弦开窗器P1 | BWP1YH | 02C | action, battery, childLockSwitch, lightSwitch, mode, opener, switch | actionSwitch, commonFaultDetection, silencer, soundSwitch, stroke, switchSpeed, torque, travel |
| `2OZI` | 承弦开窗器T1 | BWT1YH | 02C | action, alarm, battery, childLockSwitch, lightSwitch, opener, switch | actionSwitch, changeDirection, commonFaultDetection, defenceSwitch, handStartSwitch, silencer, soundSwitch, stroke, switchSpeed, torque, travel |
| `2OZJ` | 承弦开窗器X1 | BWX1YH | 02C | action, battery, childLockSwitch, lightSwitch, mode, opener, switch | actionSwitch, commonFaultDetection, silencer, soundSwitch, stroke, switchSpeed, torque, travel |
| `2Q6U` | 亚都空气净化器KJ850F-T850(Hi) | KJ850F-T850(Hi) | 013 | childLockSwitch, hcho, humidity, mode, pm25, switch, temperature | UVSwitch, anionSwitch, faultDetection, filterElement6, indicator, preciseTvoc |
| `2QNC` | 亚都智能加湿器SC700-SK071Pro(Hi) | SC700-SK071Pro(Hi) | 052 | childLockSwitch, colourMode, humidity, mode, status, switch, temperature | UVSwitch, commonFaultDetection, gear, keyToneSwitch, timerTaskId |
| `2QTT` | 箭牌智能浴霸 Pro | AQW002HM-T | 035 | cct, fan, humidity, lightSwitch, luminance, status, switch | Motion-activatedNightLightSwitch, autoDrySwitch, autoLightSwitch, autoWarmWindSwitch, automaticWarmWindSwitch, circulationTime, commonFaultDetection, deodorization, drySwitch, heat, humanSensingStatus, indicator, keyToneSwitch, leftTime, lightOffDelayTime, nightLightSwitch, radarSensingGear, startDryThreshold, sterilizationSwitch, stopDryThreshold, ventilateSwitch, ventilationFan, windSwitch |
| `2R96` | 一起玩eachone  天境全色域淡彩风扇灯 | HDF42C10 | 114 | brightness, cct, colour, colourMode, fan, lightMode, switch | commonMemorySwitch, fanMode, inchingSwitch, nightWakeup, onOffBeep, progressSwitch, progressTurnOff, progressTurnOn, switchFan, verticalSwitch |
| `2SHE` | 箭牌智能雷达人感浴霸焕新版 Pro | AEW006HM-T | 035 | brightness, fan, humidity, lightSwitch, luminance, status, switch | Motion-activatedNightLightSwitch, autoLightSwitch, autoWarmWindSwitch, automaticWarmWindSwitch, circulationTime, commonFaultDetection, drySwitch, heat, humanSensingStatus, indicator, keyToneSwitch, leftTime, lightOffDelayTime, nightLightSwitch, radarSensingGear, sterilizationSwitch, ventilateSwitch, ventilationFan, windSwitch |
| `2SHF` | 箭牌智能雷达人感浴霸焕新版 | AEW005HM-T | 035 | brightness, fan, humidity, lightSwitch, luminance, status, switch | Motion-activatedNightLightSwitch, autoLightSwitch, autoWarmWindSwitch, circulationTime, commonFaultDetection, drySwitch, heat, humanSensingStatus, indicator, keyToneSwitch, leftTime, lightOffDelayTime, nightLightSwitch, radarSensingGear, sterilizationSwitch, ventilateSwitch, ventilationFan, windSwitch |
| `ZG0E` | 智能面板 | OSLO-SP6 | A16 | brightness, childLockSwitch, luminance, switch1, switch2, switch3, temperature | DNDmode, backlight, button1, button10, button11, button12, button13, button14, button15, button16, button17, button18, button19, button2, button20, button3, button4, button5, button6, button7, button8, button9, display, faultDetection, memorySwitch, obstructionDetected, reboot, screenSwitch |
| `0100` | 三思全彩灯泡灯组 | C21BB-QE27-10W-RGB/30-80-W | 01B | brightness, cct, colour, colourMode, lightMode, switch | — |
| `1074` | 水母云全彩智能E27灯泡 | BRO-16565 | 01B | brightness, cct, colour, colourMode, lightMode, switch | lightGraduallyWakeUp, lightNoisyWakeUp |
| `1075` | 水母云IP65智能LED筒灯 | RLO-4W465 | 01B | brightness, cct, colour, colourMode, lightMode, switch | lightGraduallyWakeUp, lightNoisyWakeUp |
| `1076` | 水母云智能吸顶灯 | BLO-51565 | 01B | brightness, cct, colour, colourMode, lightMode, switch | lightGraduallyWakeUp, lightNoisyWakeUp |
| `131N` | 生迪智能LED彩光灯泡 | W11-C23 | 01B | brightness, cct, colour, colourMode, lightMode, switch | — |
| `146I` | 三思智能筒灯 | C22DL-IQ3-7W | 01B | brightness, cct, colour, colourMode, lightMode, switch | streamer |
| `173P` | 康美太香薰机 | 1522YN | 04C | brightness, colour, colourMode, lightMode, lightSwitch, switch | aromaMode, aromaSwitch, faultDetection |
| `208J` | 水母云唤醒灯 | BM-00-S | 01B | brightness, cct, colour, colourMode, lightMode, switch | — |
| `20LA` | 三思LED床头灯 | C22RL-CN-7W-RGB | 01B | brightness, cct, colour, colourMode, lightMode, switch | streamer, yedengstatus, yedengsw |
| `20LK` | 三思智能全彩充电床头灯 | C22RL-FN-6W-RGB | 01B | brightness, cct, colour, colourMode, lightMode, switch | streamer, yedengstatus, yedengsw |
| `20LT` | 水母云智能全彩筒灯 | RLO-DLS | 01B | brightness, cct, colour, colourMode, lightMode, switch | streamer |
| `218H` | 阳光照明灵睿智能灯泡RGBWC版 | BPZ600-840-7WZ | 01B | brightness, cct, colour, colourMode, lightMode, switch | streamer |
| `21DU` | 水母云智能灯带 | Lightstrip-S | 01B | brightness, cct, colour, colourMode, lightMode, switch | streamer |
| `242X` | 亚摩斯RGBCW灯带控制器 | AS-KZQ01H | 01B | brightness, cct, colour, colourMode, lightMode, switch | — |
| `273O` | 水母云智能天花灯 | CL320-A5 | 01B | brightness, cct, colour, colourMode, lightMode, switch | backswitch, frontlight, nightWakeup, progressTurnOff, progressTurnOn, streamer |
| `27W5` | 侧装红外人体移动光照传感器 | BL5016R | 03E | brightness, cct, lightSwitch, status, switch, switch1 | — |
| `29F2` | 侧装红外人体移动光照传感器 | BL5018R | 03E | brightness, cct, lightSwitch, status, switch, switch1 | — |
| `2BEI` | 得邦A60蓝牙智能灯泡全彩版 | BPZ600-865E27/DRGBHW | 01B | brightness, cct, colour, colourMode, lightMode, switch | — |
| `2BEJ` | 得邦A70蓝牙智能灯泡全彩版 | BPZ1050-865E27/DTGTSHW | 01B | brightness, cct, colour, colourMode, lightMode, switch | — |
| `2COB` | 三思LED充电床头灯 | C22RL-FN-6W-RGB | 01B | brightness, cct, colour, colourMode, lightMode, switch | streamer, yedengstatus, yedengsw |
| `2CPW` | 创维氛围灯 | NL-Q20-SW | 01B | brightness, cct, colour, colourMode, lightMode, switch | streamer |
| `2D7S` | 三思智能筒灯 | C22DL-IQ2R5-3W-RGB | 01B | brightness, cct, colour, colourMode, lightMode, switch | streamer |
| `2D7T` | 三思智能炫彩灯带 | C21SL-S01 | 01B | brightness, cct, colour, colourMode, lightMode, switch | streamer |
| `2F8Q` | POSO LED射灯 | PTT91207M | 111 | brightness, cct, colourMode, lightMode, status, switch | setting |
| `2F8R` | POSO筒灯 | PTD5053S | 111 | brightness, cct, colourMode, lightMode, status, switch | setting |
| `2FAT` | 协议空调 | MC3-Ac | 012 | fan, humidity, lightSwitch, mode, switch, temperature | airChangeGear, airChangeSwitch, airConditioner, capability, capabilityset, controlStrategy, faultDetection, filterElement, panelLocation, preTime, windSpeedEx |
| `2GDG` | 海曼(HEIMAN)智能空气质量检测仪(甲醛) | WS2AQ-H | 006 | alarm, battery, hcho, humidity, pm25, temperature | alarmSwitchS, alarmTimeSet, batteryS, humAlarmS, humHighS, humLowS, mute, tempAlarmS, tempHighS, tempLowS |
| `2HK2` | 根元智能鞋柜 | RS-FT-1L | 065 | action, brightness, mode, status, switch, temperature | DoorState, RemainTime, childLock, commonFaultDetection, custom, gear, progress, shoeResearch |
| `2MA6` | 松下空气净化消毒机 | F-JPW50C | 013 | childLockSwitch, fan, humidity, mode, pm25, switch | capabilitySet, disinfect, elapsedTimeMode, faultDetection, filterElement6, filterElement7, tvoc |
| `2MGJ` | 欧普天空之声音乐灯 | MX550-D75PLC-01 | 112 | brightness, cct, colour, lightMode, mode, switch | bgBrightness, fadeTime, fadeTimeSetting, faultDetection, lightCurveSetting, lightSwigch2, lightSwitch1, memorySwitch, rhythm |
| `2MPM` | 小崧空气净化循环扇KN-6397W | KN-6397W | 013 | childLockSwitch, fan, lightSwitch, mode, pm25, switch | UVSwitch, fanMode, fanSwitch, filterElement6, pm10current, pm1current, purgeGear |
| `2N0E` | 西顿4路单色温0-10V调光器(PLC) | SYPH-CTD041000 | 11A | brightness, colourMode, switch, switch1, switch2, switch3 | brightness1, brightness2, brightness3, brightness4, fadeTime1, fadeTime2, fadeTime3, fadeTime4, fadeTimeSetting1, fadeTimeSetting2, fadeTimeSetting3, fadeTimeSetting4, faultDetection, lightCurveSetting1, lightCurveSetting2, lightCurveSetting3, lightCurveSetting4, onSetting, outputMask, relBrightness, switch4 |
| `2N0F` | 西顿2路双色温0-10V调光器(PLC) | SYPH-CTD021000 | 11A | brightness, colourMode, mode, switch, switch1, switch2 | brightness1, brightness2, cct1, cct2, fadeTime1, fadeTime2, fadeTimeSetting1, fadeTimeSetting2, faultDetection, lightCurveSetting1, lightCurveSetting2, onSetting, outputMask, relBrightness |
| `2N0G` | 西顿8路开关执行器(PLC) | SYPH-CKG081000 | 11A | brightness, colourMode, switch, switch1, switch2, switch3 | faultDetection, onSetting, outputMask, switch4, switch5, switch6, switch7, switch8 |
| `2NNI` | 新风 | B39FA | 030 | fan, humidity, mode, pm25, switch, temperature | capabilityset, co2, controlStrategy, dbswitch, faultDetection, filterElement1, filterElement2, filterElement3, filterElement4, supportDerVirtual, tvoc, windSpeedEx |
| `2O6B` | 自然舒智能除醛净化器 | ZA-02 | 013 | childLockSwitch, humidity, mode, pm25, switch, temperature | Countdown, VOC, airQuality, fanGear, filterLifespan |
| `2OVZ` | 海越净届M7集成生态空气机 | M7 | 013 | hcho, humidity, mode, pm25, switch, temperature | UVSwitch, airQuality, anion, anionSwitch, aromaHESwitch, autoClean, countdown, darkSwitch, drainSwitch, faultDetection, percentcontrol |
| `2P5I` | 康茂智能调光灯带控制器 | KM-PWM10-5CH | 118 | brightness, cct, colour, colourMode, lightMode, switch | donotDisturb |
| `2PCJ` | 百得胜新风换气系统 | SXFDK305 | 030 | humidity, mode, pm25, status, switch, temperature | airQuality, co2, filterElement1, gear, outputWind, weight |
| `2PKD` | 新港柜体灯 | XG1001 | 222 | brightness, cct, colour, colourMode, lightMode, switch | donotDisturb |
| `2PYB` | 三思LED床头灯Pro | C22RL-CN-7W-RGB-W-HM | 10E | brightness, cct, colour, colourMode, lightMode, switch | nightLightMode, streamer |
| `2Q31` | 欧普照明SDL天辰吸顶灯 MX550 | MX550-D100-BLE-01 | 226 | brightness, cct, colour, colourMode, lightMode, switch | FadeFunction, InchingSwitch, PowerUpStatus, ResetMode, SunLightMode, WallSwitchSceneEn, relBrightness, toggleSwitch |
| `2Q39` | 欧普照明SDL天辰吸顶灯 MX900 | MX900-D260-BLE-01 | 226 | brightness, cct, colour, colourMode, lightMode, switch | FadeFunction, InchingSwitch, PowerUpStatus, ResetMode, SunLightMode, WallSwitchSceneEn, relBrightness, toggleSwitch |
| `2Q3A` | 欧普照明SDL天域晴空灯 | LDP01065TT02 | 226 | brightness, cct, colour, colourMode, lightMode, switch | FadeFunction, InchingSwitch, PowerUpStatus, ResetMode, SunLightMode, WallSwitchSceneEn, relBrightness, toggleSwitch |
| `2Q6W` | 箭牌智能浴霸 | AQW001HM-T | 035 | fan, humidity, lightSwitch, luminance, status, switch | Motion-activatedNightLightSwitch, autoLightSwitch, autoWarmWindSwitch, circulationTime, commonFaultDetection, deodorization, drySwitch, heat, humanSensingStatus, indicator, keyToneSwitch, leftTime, lightOffDelayTime, nightLightSwitch, sterilizationSwitch, ventilateSwitch, ventilationFan, windSwitch |
| `2Q9A` | 快速度调光器 | SC-01 | 222 | brightness, cct, colour, colourMode, lightMode, switch | donotDisturb |
| `2QAC` | 十亿智联智能灯带控制器 | HM1001 | 222 | brightness, cct, colour, colourMode, lightMode, switch | donotDisturb |
| `2QNG` | AI飞碟 | XC08 | 1FF | brightness, mode, switch, switch1, switch2, switch3 | switch4, switch5, switch6, switch7, switch8, usbSwitch1, usbSwitch2, usbSwitch3, usbSwitch4 |
| `2QY9` | eachone一起玩 天境全色域吸顶灯 | HF-HM-TJD-011 | 112 | brightness, cct, colour, colourMode, lightMode, switch | commonMemorySwitch, lightFormulaArray, nightWakeup, preLightFormulaArray, preview, progressSwitch, progressTurnOff, progressTurnOn |
| `2R8O` | 一起玩eachone 天境全色域淡彩吸顶灯 | HF-HM-TJD-014 | 112 | brightness, cct, colour, colourMode, lightMode, switch | commonMemorySwitch, lightFormulaArray, nightWakeup, preLightFormulaArray, preview, progressSwitch, progressTurnOff, progressTurnOn |
| `2RAP` | 云居时代AI智能开关 | RSDM-0416 | 1FF | brightness, mode, switch, switch1, switch2, switch3 | switch4, switch5, switch6, switch7, switch8 |
| `2REC` | 美的智能空调 鸿蒙空气机Pro | KFR-35G/HWR7 | 012 | fan, humidity, mode, status, switch, temperature | ECOswitch, aiFreshair, airClean, airCleangear, airConditioner, co2, co2Switch, commonFaultDetection, favoriteMode, favoriteModeSwitch, filterElement, freshAirSpeed, freshAirSwitch, intelligentClean, keepHumidity, keyToneSwitch, mildewProofswitch, modePTC, sleepCurve, sleepCurveSwitch, sterilization, switchScreen |
| `2RH9` | 一起玩eachone  雷达感应天境全色域吸顶灯 | HF-AI-TJD-014 | 112 | brightness, cct, colour, colourMode, lightMode, switch | checkTime, commonMemorySwitch, humanSensingStatus, inductionCondition, inductionSwitch, inductionTime, lightFormulaArray, nightWakeup, preLightFormulaArray, preview, progressSwitch, progressTurnOff, progressTurnOn |
| `2RHA` | 一起玩eachone  天境淡彩无缝贴装吸顶灯 | HF-XD1048-Y3 | 112 | brightness, cct, colour, colourMode, lightMode, switch | commonMemorySwitch, lightFormulaArray, nightWakeup, preLightFormulaArray, preview, progressSwitch, progressTurnOff, progressTurnOn |
| `2RNU` | 贝昂空气净化器X5S V1 | KJ500F-X5S V1 | 013 | childLockSwitch, fan, hcho, mode, pm25, switch | autoClean |
| `2RTG` | 一起玩eachone  太阳光天境灯 | HF-AI-TJD-011 | 112 | brightness, cct, colour, colourMode, lightMode, switch | commonMemorySwitch, lightFormulaArray, nightWakeup, preLightFormulaArray, preview, progressSwitch, progressTurnOff, progressTurnOn, radarControl |
| `2RZ9` | 德业除湿机DYD-Y26A3 | DYD-Y26A3 | 09B | childLockSwitch, humidity, mode, status, switch, temperature | anionSwitch, commonFaultDetection, drainSwitch, gear, waterTank |
| `2S1K` | 一起玩eachone 天境幻彩吊灯 | HF-HM-TJD-013 | 21E | brightness, cct, colour, colourMode, lightMode, switch | auxSwitch, commonMemorySwitch, lightFormulaArray, mainSwitch, nightWakeup, preLightFormulaArray, preview, progressSwitch, progressTurnOff, progressTurnOn |
| `2S8V` | 贝昂无耗材空气净化器X7P(H) Pro | KJ1000F-X7P(H) Pro | 013 | childLockSwitch, fan, hcho, mode, pm25, switch | autoClean |
| `2SF8` | 智风盒 | SC001 | 1FF | childLockSwitch, mode, switch, switch1, switch2, switch3 | backlight, fanSwitch, indicator, switch4, switch5, switch6, switch7 |
| `2SHH` | 亚都加湿器SZ700-G1(Hi) | SZ700-G1(Hi) | 052 | childLockSwitch, colourMode, humidity, status, switch, temperature | UVSwitch, ambientLight, anionSwitch, autoCleanSwitch, commonFaultDetection, gear, keyToneSwitch, timerTaskId |
| `2SHI` | 亚都加湿器SZ500-Y1(Hi) | SZ500-Y1(Hi) | 052 | childLockSwitch, colourMode, humidity, status, switch, temperature | UVSwitch, autoCleanSwitch, commonFaultDetection, gear, keyToneSwitch, timerTaskId |
| `A30A` | 智汇云音乐律动灯 | ZHY-MP007 | 119 | brightness, cct, colour, colourMode, mode, switch | gradient, rhythm, turnoffTime, turnonTime |
| `A3I8` | 方太智能集烹中心 | CXW-358-02-X20Pro AI | 274 | action, childLockSwitch, lightSwitch, status, switch, temperature | OvenWorkState, commonFaultDetection, cookTime, delayOff, gear, leftStoveStatus, midStoveStatus, rightStoveStatus, smartGrill |
| `A3JM` | 美的加湿器SZK-1Y80 Pro | SZK-1Y80 Pro | 052 | fan, humidity, lightSwitch, mode, status, switch | airDry, autoCleanSwitch, commonFaultDetection, indicator, keyToneSwitch, waterTank |
| `A3OF` | 美的加湿器SZK-U12 | SZK-U12 | 052 | fan, humidity, lightSwitch, mode, status, switch | airDry, ambientLight, commonFaultDetection, keyToneSwitch, waterTank |
| `A3OK` | 美的加湿器SZK-U15 | SZK-U15 | 052 | fan, humidity, lightSwitch, mode, status, switch | airDry, ambientLight, commonFaultDetection, keyToneSwitch, pciSwitch, waterTank |
| `ZG0L` | 智能面板（无线版） | OSLO-BP6 | A16 | brightness, childLockSwitch, luminance, switch1, switch2, switch3 | DNDmode, backlight, button1, button10, button11, button12, button13, button14, button15, button16, button17, button18, button19, button2, button20, button3, button4, button5, button6, button7, button8, button9, display, faultDetection, obstructionDetected, reboot, screenSwitch |
| `0103` | 灯组 |  | 01B | brightness, cct, colour, colourMode, switch | — |
| `0104` | 灯组 |  | 01B | brightness, cct, colour, colourMode, switch | — |
| `0105` | 灯组 |  | 01B | brightness, cct, colour, colourMode, switch | — |
| `100z` | 三思全彩灯泡 | C21BB-QE27-10W-RGB/30-80-W | 01B | brightness, cct, colour, lightMode, switch | — |
| `101q` | 得邦智能台灯 | DKL100900102 | 01B | brightness, cct, colour, lightMode, switch | — |
| `105L` | Hue智能调光灯泡(彩灯) | SMS-01-LUX | 01B | brightness, cct, colour, lightMode, switch | — |
| `1070` | 奥普吸顶灯AX560 | AX560-198X0.2+72X0.2-TT-02金-3000K/4000K-馨圆 | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `1080` | 欧普智能灯具 | CB-RGBW-dearwe | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `1088` | 美尔凯特 Z7浴室音乐暖空调 | SH90603780AA | 035 | lightMode, lightSwitch, mode, switch, temperature | currentTemperature, faultDetection, gear, leftTime, musicSwitch, swing, workTime |
| `111F` | 三思双色温灯泡 | C21BB-TE27-18W-D | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `111Z` | 三思双色温灯泡 | C21BB-TE27-13W-D | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `113P` | Yeelight彩光灯泡 | color | 01B | brightness, cct, colour, lightMode, switch | — |
| `113S` | Yeelight彩光灯带 | stripe | 01B | brightness, cct, colour, lightMode, switch | — |
| `116F` | 博乐落地灯_FOL01 | FL-01 | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `123M` | 电力魔方空气卫士 | JA-001 | 013 | brightness, humidity, lightSwitch, switch, temperature | Eco, airPurifying, faultDetection, filterElementReset, pm2p5 |
| `132Q` | 冠雅LED台灯 | LA-H312 | 046 | brightness, cct, colourMode, lightMode, switch | commonMemorySwitch1 |
| `134R` | U2C-智能护眼台灯-GD-TDW12B | GD-TDW12B | 046 | brightness, cct, colourMode, lightMode, switch | — |
| `145Z` | 达伦自然光台灯X3Pro | X3 Pro | 046 | brightness, cct, colour, colourMode, switch | ColourAutoChange, MainLightSwitch, NightLightSwitch, RGBSwitch, SleepMode |
| `158X` | 欧派蒸烤一体机 | KWS220-sk638 | 024 | childLockSwitch, lightSwitch, mode, status, temperature | faultDetection, lackWater, leftTime, preTimeStart, presetSwitch, setWorkTime, waterTankDoor |
| `165U` | 贝昂无耗材空气净化器 | X3(H) | 013 | childLockSwitch, fan, mode, pm25, switch | clean |
| `172M` | 三思智毅Pro护眼台灯 | C22RL-TD08-W | 046 | brightness, cct, colourMode, lightMode, switch | reading, relax |
| `174B` | 三思读写台灯 | C22RL-TD03 | 046 | brightness, cct, colourMode, lightMode, switch | loving, reading, relax, tomatoClk, writing |
| `178L` | 海尔空气净化器KJ450F-M900A | KJ450F-M900A | 013 | childLockSwitch, fan, mode, pm25, switch | filterElement1 |
| `178M` | 海尔空气净化器KJ820F-N800C | KJ820F-N800C | 013 | childLockSwitch, fan, mode, pm25, switch | anionSwitch, filterElement1 |
| `178N` | 西顿风影彩光灯带 | CEGB5050F-60(hilink) | 01B | brightness, colour, colourMode, lightMode, switch | — |
| `178O` | 西顿锋芒智能灯带 | CEGB2835F-60(hilink) | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `182Q` | Momax无线充护眼台灯 | QL8SH | 046 | brightness, cct, colourMode, lightMode, switch | EyeProtection, tomatoClk |
| `183W` | 三思读写台灯TD05 | C22RL-TD05 | 046 | brightness, cct, colourMode, lightMode, switch | loving, reading, relax, tomatoClk, writing |
| `184O` | 博乐智能吸顶灯 | MP03H-WR | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `2000` | 欧普读写台灯3Pro | MT001-13.5SF | 046 | brightness, cct, colourMode, lightMode, switch | nightWakeup, tomatoClk |
| `202J` | 贝昂无耗材空气净化器 | X7(H) | 013 | childLockSwitch, fan, mode, pm25, switch | clean |
| `203Q` | 阿特兰斯双线CCT控制器 | S135H.BI | 01B | brightness, cct, colourMode, lightMode, switch | Match |
| `206N` | 高盛达智能吸顶灯 | MX-LED060FWJ/473-J | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `207S` | 领普三键零火开关MESH | Q4D-BLE-W3(HW) | 005 | brightness, switch, switch1, switch2, switch3 | button1, button2, button3, mode1, mode2, mode3 |
| `207U` | 达伦21W吸顶灯C23NTHW | DL-C23NTHW | 01B | brightness, cct, colourMode, lightMode, switch | NightMode |
| `20HZ` | 达伦吸顶灯 | DL-CLW-1 | 01B | brightness, cct, colourMode, lightMode, switch | NightMode |
| `20Q0` | 柔光护眼圆盘台灯 | C22RL-TD06 | 046 | brightness, cct, colourMode, lightMode, switch | loving, reading, relax, tomatoClk, writing |
| `20R2` | 海尔空气净化器KJ200F-M900A | KJ200F-M900A | 013 | childLockSwitch, fan, mode, pm25, switch | filterElement1 |
| `20RG` | 威诺华智能灯泡 | A60-8W | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `20TL` | 贝昂无耗材空气净化器X7SH | X7S(H) | 013 | childLockSwitch, fan, mode, pm25, switch | clean, hcho1 |
| `20VY` | 亚摩斯智能筒灯 | AS-L20H | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `20Y2` | 永林一拖四调光驱动 | PLH-LB4X40-40-XL12 | 044 | brightness, switch, switch1, switch2, switch3 | brightness1, brightness2, brightness3, brightness4, switch4 |
| `20YO` | 亚摩斯空气净化器AS-JC261 | AS-JC261 | 013 | childLockSwitch, fan, mode, pm25, switch | anionSwitch, faultDetection, filterElement1 |
| `210E` | 欧派嵌入式智能烤箱 | KWS330-K908 | 024 | action, lightSwitch, mode, status, temperature | ProbeTargetTemp, atuoRecipe, childLock, faultDetection, leftTime, openStatus, preheat, probe, setSteam, setWorkTime, waterTank, workTime |
| `210Y` | 欧井除湿机 | OJ-123E | 09B | childLockSwitch, humidity, mode, switch, temperature | ION, faultDetection, gear |
| `213Y` | 西顿一拖四调光模块 | SWP01-QL-7W-14 | 044 | brightness, switch, switch1, switch2, switch3 | brightness1, brightness2, brightness3, brightness4, brightness5, switch4 |
| `2168` | 亚都智能除湿机YD-C253BGWHi | YD-C253BGW(Hi) | 09B | childLockSwitch, humidity, mode, switch, temperature | gear, sleep, state |
| `2178` | 亚都空气净化器KJ650F-P6PLUSHi | KJ650F-P6PLUS(Hi) | 013 | childLockSwitch, fan, mode, pm25, switch | countdown, filterElement1, light, sound |
| `2186` | 欧派嵌入式智能蒸箱 | ST50-S908 | 022 | action, lightSwitch, mode, status, temperature | autoRecipe, childLock, faultDetection, gateState, lackWater, leftTime, setWorkTime, workTime |
| `21JC` | 阳光照明灵睿智能灯泡调光调色版 | BPZ600-840-7WZ | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `21JD` | 阳光照明灵睿智能灯泡RGBW版 | BPZ600-840-7WZ | 01B | brightness, colour, colourMode, lightMode, switch | coolwhitemode, streamer |
| `21KR` | 华为智选 九阳智能恒温电水壶 | K15ED-W580 | 09A | action, lightSwitch, mode, status, temperature | comMode, faultDetection, hotMode, leftTime, preTime, saveTemperature, voiceSwitch, warmDuration |
| `21UN` | 三思LED吸顶灯 | C22PL-HC-36W-W | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `21UO` | FSL智能彩光灯带 | FSL-DD-RGBTW | 01B | brightness, cct, colour, colourMode, switch | commonMode1, streamer |
| `21Y4` | 雷士简韵圆形卧室灯 | WHXD24W/F-03 | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `21YB` | 雷士叠影方形客厅灯 | NVX108-5 | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `21YV` | 贝昂无耗材空气净化器MINI | MINI | 013 | childLockSwitch, fan, mode, pm25, switch | clean |
| `220J` | 雷士智能灯带 | WHDD24V-01 | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `2223` | 雷士简韵方形卧室灯 | WHXD36W/F-03 | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `2225` | 雷士简韵方形客厅灯 | NX108/G1-002 | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `2229` | 雷士柠梦圆形小卧室灯 | NX024/G1-003 | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `222B` | 雷士满天星圆形卧室灯 | WHXD24F/G-06 | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `222C` | 雷士柠梦圆形卧室灯 | WHXD36W/F-03 | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `222D` | 雷士柠梦方形卧室灯 | NX048/T3-003 | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `222E` | 雷士柠梦方形客厅灯 | NX108/G1-012 | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `2244` | 雷士满天星风扇灯 | WY36-24-8006 | 01B | brightness, cct, colourMode, lightMode, switch | Fan, fanswitch, lightswitch |
| `224K` | 欧普智能幻彩灯带 | LED-RGB strip-HWZX-SP | 01B | brightness, colour, lightMode, status, switch | effect, modeName, motion, motionDetected, speed |
| `226X` | 阳光照明皓翼大三防灯 | MX1012-LED24 | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `2274` | 阳光照明至简方形客厅灯 | MX4246-LED9×12 | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `2275` | 阳光照明至简方形卧室灯 | MX4002-LED24-1x2 | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `2276` | 阳光照明至简圆形卧室灯 | MX9054-LED24 | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `22YZ` | 台灯 | LETD04 | 046 | brightness, cct, colourMode, lightMode, switch | PIR |
| `22ZB` | 町米迷你破壁料理机 | YDD01H | 0D2 | action, mode, status, switch, temperature | autokeepwarm, faultDetection, leftTime, preTimeStart, presetSwitch |
| `24E7` | 鸿蒙智选 720 全效空气净化器 2 | KJ600F-E600 | 013 | childLockSwitch, fan, mode, pm25, switch | UVSwitch, anionSwitch, cav, cmw, faultDetection, filterElement1, keytoneSwitch, playMode, screenSwitch, stbyMonitor |
| `24NG` | 奔腾剃须刀 | PQ9211 | 170 | battery, mode, status, switch, temperature | clean, errTips, paly, record, totalTime, type |
| `24TT` | 欧普Balance读写台灯 | MT001-13.5SF | 046 | brightness, cct, colourMode, lightMode, switch | delayclose, nightWakeup, rhythm, tomatoClk |
| `2588` | 三加三维智能幻彩灯带 | 12mm-60D-RGBW | 01B | brightness, colour, colourMode, lightMode, switch | — |
| `25FO` | 三加三维智能筒射灯 | SJSW-TD168 | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `25UT` | 得途智能护眼吸顶灯 | DT-XDD50 | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `262Y` | DoHome 幻彩蜂巢拼接灯 | S001 | 11F | brightness, cct, colour, mode, switch | lighting, music |
| `264S` | 雷士智能吸顶灯 | WHXD120W/F-03 | 112 | brightness, cct, colourMode, lightMode, switch | — |
| `26M6` | 光合美梦焕颜机 | D150-PSS | 271 | childLockSwitch, mode, pm25, switch, temperature | airHumidity, airHumidityReport, faultDetection, light, pm10, pm10Report, pm25Report, pm25SetValue, temperatureReport |
| `274F` | 领普三键墙壁开关 | Q3S-HW-W3 | 005 | brightness, switch, switch1, switch2, switch3 | — |
| `27D0` | 心智悦新风机B2 | RZBD-Z120A | 030 | fan, mode, pm25, status, switch | Heat0, NAI, faultDetection, filterElement1, ledSwitch |
| `28I7` | 贝昂无耗材空气净化器 | KJ300F-X3(H) | 013 | childLockSwitch, fan, mode, pm25, switch | clean |
| `28SL` | 智能贝壳镜 | BMD023 | 0F1 | battery, brightness, mode, status, switch | — |
| `294C` | 荣事达衣物护理机 | YHJ-300PZR(B) | 1B7 | action, childLockSwitch, mode, status, switch | Water, faultDetection, gate, leftTime, pretime |
| `29H0` | 宝贝第一耀至REX | R542C | 0DF | alarm, battery, fan, switch, temperature | PowerLimit, heat, hotTemp, powerSupply, set |
| `29QR` | 三加三维智能三色 | SJSW-Smart lamp | 118 | brightness, cct, colourMode, lightMode, switch | — |
| `29X0` | 720 全效空气净化器 E420 | KJ400F-E420 | 013 | childLockSwitch, fan, mode, pm25, switch | UVSwitch, anionSwitch, cav, cmw, faultDetection, filterElement1, keytoneSwitch, offPm25Value, onPm25Value, screenSwitch, stbyMonitor |
| `2A8C` | 电力魔方空气卫士PRO | JA-002S | 013 | fan, humidity, pm25, switch, temperature | LED, cmw, faultDetection |
| `2AE3` |  | KK-FC-D21W | 012 | childLockSwitch, fan, mode, switch, temperature | autoOff |
| `2AE4` |  | KK-XK-MD11 | 012 | childLockSwitch, fan, mode, switch, temperature | autoOff |
| `2AJO` | Paulmann-Finn-Smart吸顶灯 | E1267 | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `2AJX` | Paulmann-Diskette-Pro-Smart吸顶灯 | E1045 | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `2AKM` | 华艺凝玛吸顶灯 | hw001 | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `2APC` | 雷士满天星方形客厅灯 | NX112/T3-007 | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `2APF` | 雷士叠影方形卧室灯 | WHXD64F/G-01 | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `2APH` | 雷士满天星方形卧室灯 | NX032/T3-004 | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `2APM` | 雷士叠影圆形卧室灯 | WHXD62F/G-01 | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `2APN` | 雷士叠影圆形小卧室灯 | WHXD46F/G-01 | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `2AQ8` | 亚都空气净化器KJ550G-B5Hi | KJ550G-B5(Hi) | 013 | childLockSwitch, fan, mode, pm25, switch | countdown, filterElement1, light, sound |
| `2AQD` | 达伦自然光吸顶灯Z3Pro | Z3 Pro | 01B | brightness, cct, colourMode, lightMode, switch | lampswitch, natural, nightmode |
| `2AU9` | 鸿雁智能灯带 | ZGD4-0800-200 | 01B | brightness, cct, colourMode, lightMode, switch | progressSwitch |
| `2AVU` | 亚都空气净化器KJ650F-B6Hi | KJ650F-B6(Hi) | 013 | childLockSwitch, fan, mode, pm25, switch | countdown, filterElement1, light, sound |
| `2B63` | 捷德韦尔两线式可调光调色灯控盒 | JD7.30.001 | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `2B7O` | Paulmann-Konig-Smart餐吊灯CCT | E1303 | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `2B8I` | 720 全效空气净化器 1i | KJ350F-C350 | 013 | childLockSwitch, fan, mode, pm25, switch | cav, cmw, faultDetection, filterElement1, keytoneSwitch, screenSwitch, stbyMonitor |
| `2BEG` | 得邦A60蓝牙智能灯泡调光调色版 | BPZ500-865E27/DTGTSHW | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `2BEH` | 得邦A70蓝牙智能灯泡调光调色版 | BPZ1520-865E27/DTGTSHW | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `2BEK` | 智能筒灯 | DNL401052W | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `2BEL` | 智能光源模组 | RPC1001 | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `2BEN` | 星空版悸动客厅吸顶灯 | CLL1058108 | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `2BEO` | 星空版悸动卧室吸顶灯 | CLL105803625 | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `2BEV` | FSL蓝牙彩光灯带 | FSL-BLE-RGBDD | 01B | brightness, cct, colour, colourMode, switch | — |
| `2BFP` | 智能护眼台灯 | DKL1026 | 046 | brightness, cct, colourMode, lightMode, switch | — |
| `2BGM` | 三雄极光Pak智能筒灯 | PAK560396 | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `2BHE` | 空气堡智慧新风系统ZEN-300H | ZEN-300H | 030 | fan, mode, pm25, status, switch | co2, filterElement1, filterElement2, heatSwitch, light |
| `2BNH` | 达伦自然光吸顶灯D3 | D3 | 01B | brightness, cct, colourMode, lightMode, switch | lampswitch, natural, nightmode |
| `2CBM` | 捷德韦尔RGB灯控盒 | JC7.28.001 | 01B | brightness, colour, colourMode, lightMode, switch | commonMemorySwitch1, progressSwitch |
| `2DGO` | 水母云智能双色筒灯 | HT-DL-CW | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `2DPH` | 达伦吸顶灯C21CTHW | DL-C21CTHW | 01B | brightness, cct, colourMode, lightMode, switch | NightMode |
| `2DPI` | 达伦吸顶灯C217THW | DL-C217THW | 01B | brightness, cct, colourMode, lightMode, switch | NightMode |
| `2DWC` | 水母云智能双色灯带 | Lightstrip-CW | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `2ENX` | 得途智能护眼吸顶灯 | DT-XDD30 | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `2EO8` | 熠世华彩情景灯 | HC-XD-068 | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `2EP5` | 达伦36W吸顶灯C33NTHW | DL-C33NTHW | 01B | brightness, cct, colourMode, lightMode, switch | NightMode |
| `2EW3` | 月影智能护眼台灯-新月 | MT0072-1T | 046 | brightness, cct, colourMode, lightMode, switch | auto, love, nlight, read, rest, restime, write |
| `2EXO` | 三思LED吸顶灯 24W | C22PL-HC-24W-W | 01B | brightness, cct, colourMode, lightMode, switch | — |
| `2EZR` | 亚摩斯睿雅零火开关三键 | ZJ-KG37H | 005 | brightness, switch, switch1, switch2, switch3 | — |
| `2FEC` | 金莱特智能空气净化器 | KN-6393 | 013 | childLockSwitch, fan, mode, pm25, switch | UVSwitch, filterElement1, lightd |
| `2FW5` | 吉豪智能吊灯 | DMB9246 180W | 21E | brightness, cct, colourMode, lightMode, switch | — |
| `2G19` | 达伦自然光夜灯 蓝牙版 | N3S | 21F | battery, brightness, colourMode, lightMode, switch | ChargingMode, DelayLightOff, DeviceStatus, LightSensingSwitch, Reconnect |
| `2IKT` | 九牧智能灯镜 | AM2464-738C-1 | 04A | brightness, cct, lightMode, status, switch | commonFaultDetection |
| `2JB8` | 梦颜森林光合机 | D150-PSS-K0 | 271 | childLockSwitch, humidity, pm25, switch, temperature | airHumidityReport, faultDetection, huanjing, light, pm10, pm10Report, pm25Report, pm25SetValue, shouhou, skinMode, temperatureReport |
| `2JNF` | 贝昂空气净化器A5 | KJ500F-A5 | 013 | childLockSwitch, fan, mode, pm25, switch | clean |
| `2K2D` | 科威德迩空气消毒机CD-EL30 | CD-EL30 | 013 | childLockSwitch, fan, mode, pm25, switch | alarm1, filterElement1, volume |
| `2K8A` | 霍尼韦尔空气净化器KJ1000F-P22W | KJ1000F-P22W | 013 | childLockSwitch, fan, mode, pm25, switch | UVSwitch, filterElement2, setting, tvoc |
| `2KUT` | 飞利浦智能眼部按摩器 | PPM7303E | 32A | battery, mode, status, switch, temperature | bredr, countdown, gear, massage, volume |
| `2KWP` | 欧普智能灯带驱动器 - 75W | OP-IFSVH0750024H5-01 | 226 | brightness, cct, colour, colourMode, switch | fadeTime, fadeTimeSetting, faultDetection, lightCurveSetting, memorySwitch, subProduct |
| `2KWQ` | 欧普智能灯带驱动器 - 240W | OP-IFSVH2400024H5-01 | 226 | brightness, cct, colour, colourMode, switch | fadeTime, fadeTimeSetting, faultDetection, lightCurveSetting, memorySwitch, subProduct |
| `2L0T` | 亚都空气净化器KJ1000G-T1000(Hi) | KJ1000G-T1000(Hi) | 013 | childLockSwitch, hcho, mode, pm25, switch | UVSwitch, anionSwitch, level, light, sleep, sound, timing, work |
| `2L63` | 欧普智能台灯3Pro | MT001YH-15SX | 046 | brightness, cct, colourMode, lightMode, switch | defMode1, defMode2, defMode3, defMode4, delayOff, lightConfig1, lightConfig2, lightConfigReset, modeDefine, runStactics, seatSensor, studyRemind |
| `2LNI` | 易百珑双色温灯带 | ERC2302-HM | 118 | brightness, cct, colourMode, lightMode, switch | CleanPair1, CleanPair2, CustomPair, ScenePair, donotDisturb |
| `2LV7` | 亚都空气净化器KJ550F-T550(Hi) | KJ550F-T550(Hi) | 013 | childLockSwitch, hcho, mode, pm25, switch | UVSwitch, level, light, sound, timing, work |
| `2LVK` | 易百珑RGBW灯带 | ERC2305K-HM | 118 | brightness, colour, colourMode, lightMode, switch | CleanPair1, CleanPair2, CustomPair, ScenePair, donotDisturb |
| `2M5L` | 720智能空气净化器 3i | KJ400F-C400i | 013 | childLockSwitch, fan, mode, pm25, switch | airQuality, cav, city, cmw, faultDetection, filterElement1, keytoneSwitch, monitoringSwitch, screenSwitch, stbyMonitor, userFunctions, userInformations |
| `2M6H` | 智能控制器-6恒 | MC3-ZK1 | 012 | fan, humidity, mode, switch, temperature | capability, chilledWaterSystemSwitch, faultDetection, sceneMode, selfCleanswitch |
| `2M7T` | 松下智能除菌加湿器 | FE-KFW06C01 | 052 | childLockSwitch, humidity, mode, status, switch | UVSwitch, elapsedTimeMode, faultDetection, filterElement1, gear |
| `2MAX` | 达伦智能台灯3Pro | DL-32WS | 046 | brightness, cct, colourMode, lightMode, switch | delayOff, eyeRemind, eyeSuggestion, lightFormulas, lightFormulas01, lightFormulas02, lightFormulas03, lightStatus, mainSwitch, nightLightSwitch, nightMode, nightSwitch, runStactics |
| `2MD4` | SJSW智能筒射灯 | SJSW-TD169 | 111 | brightness, cct, lightMode, switch, switch1 | fade |
| `2MGS` | 华米元情景灯 | HMY-118 | 112 | brightness, cct, lightMode, switch, switch1 | fade |
| `2MKS` | 贝昂空气净化器X5S | KJ500F-X5S | 013 | childLockSwitch, fan, mode, pm25, switch | clean, hchoDensity |
| `2N0H` | 西顿2路MOS调光器(PLC) | SYPH-CTK020200 | 11A | brightness, colourMode, switch, switch1, switch2 | brightness1, brightness2, fadeTime1, fadeTime2, fadeTimeSetting1, fadeTimeSetting2, faultDetection, lightCurveSetting1, lightCurveSetting2, onSetting, outputMask, relBrightness |
| `2N1F` | PGG眼部按摩仪E6 | E6 | 32A | battery, mode, status, switch, temperature | atomization, audioplayer, bt.connection, countdownOff, externalaudioSwitch, hotCompress, music |
| `2NAL` | eachone一起玩智能风扇灯 | HJ-HM-FSD-001 | 114 | brightness, cct, fan, lightMode, switch | binding, countdownht, fanMode, onOffBeep, progressSwitchHF, progressTurnOff, progressTurnOn, switchFan, verticalswing |
| `2NDN` | 根元净护刺客AP004 | RS-AP004 | 1B7 | action, lightMode, mode, status, switch | chargeState, curTime, faultDetection, leftTime, pyroelectricState, remianCapacity, ringLightBrightness, ringLightCCT, timing1, timing2, timing3, timing4, timing5, turnLightOffDelay |
| `2NMZ` | 贝昂落地式循环扇 | FZS2-SF3 Pro | 029 | fan, lightSwitch, mode, switch, temperature | delayOff, lock, neIon, schedule, track |
| `2NNH` | 空调 | B39AC | 012 | fan, humidity, mode, switch, temperature | capabilityset, controlStrategy, faultDetection, filterElement, panelLocation, preTime, updateData, waterAndFanValveMode, windSpeedEx |
| `2NQC` | meipont美邦空调柜机 | MAC72V1N9SR | 012 | fan, humidity, mode, switch, temperature | ECO, Infinitewindspeed, TemperandhumiControl, commonFaultDetection, dedusting, downcomfortablewind, electricalHeating, fresh, outdoor, pmvTemper, selfclean, upcomfortablewind |
| `2NRE` | 智能控制器-通用 | MC3-ZK-T | 012 | fan, humidity, mode, switch, temperature | capabilityset, chilledWaterSystemSwitch, commonFilterElement1, faultDetection, filterElement, freshAirSwitch, humidification, sceneMode, sterilization |
| `2NTK` | 智能控制器-6恒1代 | MC3-ZK-6H1 | 012 | fan, humidity, mode, switch, temperature | capability, chilledWaterSystemSwitch, faultDetection, sceneMode, selfCleanswitch |
| `2O6G` | meipont智能洗衣机 | WM10R-M55 | 015 | action, childLockSwitch, mode, status, switch | Intense, Pretimeover, Prewash, Soak, Steam, Turnpeed, Watertemp, faultDetection, leftTime, rinseTimes |
| `2O8B` | 集控器 | MC3-ZKQ-TY | 346 | fan, humidity, mode, switch, temperature | acmaxtempSet, acmintempSet, capabilityset, chilledWaterSystemSwitch, commonFilterElement1, fault, filterElement, freshAirSwitch, freshAirmode, humidification, outhomeSwitch, sceneMode, selfCleanswitch, sensorsAirParam, windSpeedEx |
| `2O9E` | RADLIT智能灯 | RD-HM | 118 | brightness, cct, colour, lightMode, switch | ColorfulLightingMode, GradientDuration, Phantomcolorvariablespeed |
| `2OGU` | IAM智能宠物空气净化器U7 Pro | KJ600F-U7 Pro | 013 | childLockSwitch, fan, mode, pm25, switch | airQuality, allergen, capabilitySet, cav, collectSwitch, dailyPurifiedAir, faultDetection, filterElement1, keyToneSwitch, machinePara, monitoringSwitch, outdoorPM25, screenSwitch, tvoc, weight |
| `2OKC` | meipont智能蒸烤箱 | MZK-T30 | 024 | action, lightSwitch, status, switch, temperature | SteamRoast, UpperRoast, WaterLevel, barbecue, clean, commonFaultDetection, leftTime, preTimeStart, presetSwitch, recipes, setWorkTime, steam, sterilization, workTime |
| `2OQA` | 玛格智能调光灯带控制器 | KM-PWM10-5CH | 226 | brightness, cct, colour, lightMode, switch | Colorselect, donotDisturb |
| `2P9E` | 欧井智能除湿机OJ-102E | OJ-102E | 09B | childLockSwitch, humidity, mode, switch, temperature | airClean, anionSwitch, countDown, faultDetection, gear |
| `2PQ5` | THINCO智能台灯5Ultra | DL-58WS | 046 | brightness, cct, childLockSwitch, lightMode, switch | lightAdaptionSwitch, lightFormulaArray, longTimeAlarm, nightModeSet, preLightFormulaArray, preview, progressTurnOn, remoteControlSearch, remoteCtrPair, seatOffLightSet, seatOnLightSet, timeSync, usageRecord |
| `2PXZ` | 贝昂无耗材空气净化器X7PH | KJ1000F-X7P(H) | 013 | childLockSwitch, hcho, mode, pm25, switch | autoClean, fanGear |
| `2Q0J` | 美菱洗衣机LRS9H120DIZ | LRS9H120DIZ | 015 | action, childLockSwitch, mode, status, switch | commonFaultDetection, electric, heatTimeMode, intelligentFabricSoftenerDispensing, leftTime, nursingModel, operationCycles, preTimeEndMode, presetSwitch, rinseTimes, rotateSpeedGear, spinTime, stains, tempSettingMode, temperatureTracking, tsmartDispenseMode, washTime, waterConsumption, waterQuality, weatherMonitor |
| `2Q24` | THINCO智能落地灯Pro | DL-68WF | 10F | brightness, cct, childLockSwitch, lightMode, switch | auxBrightness, auxSecBrightness, auxSecSwitch, auxSwitch, intelligentDimming, lightAdaptionSwitch, lightFormulaArray, longTimeAlarm, mainBrightness, mainSwitch, nightModeSet, preLightFormulaArray, preview, progressTurnOn, remoteControlSearch, remoteControlStatus, remoteCtrlInfo, remoteCtrlMetering, remoteCtrlType, seatOffLightSet, seatOnLightSet, spectralData, strobeData, timeSync, usageRecord |
| `2Q2T` | MEIPONT智能空调 风神之眼 | MAC35V1P80HR | 012 | fan, mode, status, switch, temperature | commonFaultDetection, electric, favoriteMode, favoriteModeSwitch, keyToneSwitch, preTime, runtime, sceneMode, switchPTC, switchScreen |
| `2Q3B` | 欧普照明SDL炫彩灯带 | OP-RE-CBX-LS-SIGB-01 | 226 | brightness, cct, colour, colourMode, switch | DynamicCctTransition, DynamicMode, DynamicModeColor1, DynamicModeColor2, DynamicModeColor3, DynamicModeColor4, DynamicModeColor5, DynamicModeColor6, FadeFunction, PixelCount, PowerUpStatus, ResetMode, StaticCctTransition, SunLightMode, relBrightness, toggleSwitch |
| `2Q4H` | SORONTEK智能双色温灯 | SR-TH-020-10W | 21D | brightness, cct, colourMode, lightMode, switch | progressSwitch |
| `2Q6K` | 长虹智能空调 灵犀之眼 | KFR-35GW/ZDVTW1-R1 | 012 | fan, humidity, mode, switch, temperature | ECOswitch, commonFaultDetection, electric, keyToneSwitch, runtime, sceneMode, selfClean, switchPTC, switchScreen, temperatureHumidityDualControl |
| `2Q8M` | 迈睿人体存在传感器Pro 电池版 | MH3 Pro | 01A | action, battery, luminance, pir, targetDistance | checkResult, delayTime, detectionPara, deviceSwitch, envNoiseMgmt, indicator, ledSwitch, selfCheck, sensitivity |
| `2QJD` | 奥普浴霸FX-Pro-HW | FX-Pro-HW | 035 | action, fan, lightSwitch, status, temperature | autoWarmWindSwitch, automaticWarmWindSwitch, commonFaultDetection, deodorization, drySwitch, indicator, leftTime, nightLightSwitch, ventilateGear, ventilateSwitch, ventilationFan, windMode, windSwitch |
| `2QJJ` | 多功能暖风机(杀菌烘干功能) | XG2001 | 065 | action, mode, status, switch, temperature | childLock, progress |
| `2QMI` | 佳普乐腾韵智联浴缸 | WB2TY-01N | 297 | childLockSwitch, colourMode, status, switch, temperature | ShowerHeadSwitch, bubbleBathSetting, commonFaultDetection, devCustomInfo, durationOfWaterInflow, gear, knobFunctionSwitch, self-cleaningStatus, waterGear |
| `2QRH` | 三菱电机空调壁挂机LC系列 | MSZ-LC12VFL | 012 | fan, humidity, mode, switch, temperature | capabilityset, commonFaultDetection, electric, keyToneSwitch |
| `2QRI` | 三菱电机空调壁挂机ZC系列 | MSZ-ZC12VFL | 012 | fan, humidity, mode, switch, temperature | capabilityset, commonFaultDetection, electric, keyToneSwitch, softWindSwitch |
| `2R3A` | 美菱洗衣机LRS9G120DIZ | LRS9G120DIZ | 015 | action, childLockSwitch, mode, status, switch | commonFaultDetection, doorLockSwitch, electric, intelligentFabricSoftenerDispensing, leftTime, nursingModel, operationCycles, preTimeEndMode, presetSwitch, rinseTimes, rotateSpeedGear, spinTime, stains, tempSettingMode, temperatureTracking, tsmartDispenseMode, washDrySwitch, washTime, waterConsumption, waterQuality, weatherMonitor |
| `2R3H` | IAM智能宠物空气净化器U7 | KJ600F-U7 | 013 | childLockSwitch, fan, mode, pm25, switch | airQuality, allergen, capabilitySet, cav, dailyPurifiedAir, faultDetection, filterElement1, keyToneSwitch, machinePara, monitoringSwitch, outdoorPM25, screenSwitch, timerTaskId, tvoc, weight |
| `2RBO` | MEIPONT 风神之眼 鸿蒙真新风空调 | MAC35V1M80HR | 012 | fan, mode, status, switch, temperature | aiFreshair, co2, co2Switch, commonFaultDetection, electric, favoriteMode, favoriteModeSwitch, filterElement, freshAirSpeed, freshAirSwitch, keyToneSwitch, modePTC, runtime, sceneMode, sleepCurve, sleepCurveSwitch, switchPTC, switchScreen |
| `2RCE` | 康茂多功能暖风机(杀菌烘干功能) | KM-NFJ-001 | 065 | action, mode, status, switch, temperature | childLock, progress |
| `2RDR` | MEIPONT 风神之眼 柜机 | MAC72V1P80SR | 2F9 | fan, mode, status, switch, temperature | commonFaultDetection, electric, favoriteMode, favoriteModeSwitch, keyToneSwitch, modePTC, runtime, sceneMode, sterilization, switchPTC, switchScreen |
| `2RH5` | 奥普浴霸MC07-Pro-HW | MC07-Pro-HW | 035 | action, brightness, lightSwitch, status, switch | autoDrySwitch, autoLightSwitch, autoWarmWindSwitch, automaticWarmWindSwitch, commonFaultDetection, deodorization, deodorizationFilter, devCustomInfo, drySwitch, heat, indicator, inductionCondition, lightingMode, nightLightSwitch, sensitivity, setWorkTime, ventilateGear, ventilateSwitch, windMode, windSwitch |
| `2RJB` | 迈睿人体存在传感器 电池版 | MH3 | 01A | action, battery, luminance, pir, targetDistance | checkResult, delayTime, detectionPara, deviceSwitch, envNoiseMgmt, indicator, ledSwitch, selfCheck, sensitivity |
| `2RK1` | 美的智能空调 鸿蒙全面风Pro | KFR-72L/HWR3 | 2F9 | fan, mode, status, switch, temperature | ECOswitch, commonFaultDetection, favoriteMode, favoriteModeSwitch, intelligentClean, keyToneSwitch, mildewProofswitch, modePTC, sterilization, switchScreen |
| `2RNS` | 贝昂无耗材空气净化器X3(H) V1 | KJ300F-X3(H) V1 | 013 | childLockSwitch, fan, mode, pm25, switch | autoClean |
| `2RNV` | 美菱干衣机100BI | LRS9D100BI | 0D7 | action, childLockSwitch, mode, status, switch | commonFaultDetection, doorLockSwitch, dryMode, electric, heatTime, leftTime, nursingMode, operationCycles, preTimeEnd, preTimeStart, presetSwitch, silentSwitch, steamSwitch, sterilize, washerDryerLinkage, washingMachineStatus |
| `2RUF` | 三菱电机空调壁挂机ZC16 | MSZ-ZC16VFL | 012 | fan, humidity, mode, switch, temperature | capabilityset, commonFaultDetection, electric, keyToneSwitch, softWindSwitch |
| `2RUG` | 三菱电机空调壁挂机GZC16 | MSZ-GZC16VFL | 012 | fan, humidity, mode, switch, temperature | capabilityset, commonFaultDetection, electric, keyToneSwitch, softWindSwitch |
| `2RUH` | 三菱电机空调壁挂机LC16 | MSZ-LC16VFL | 012 | fan, humidity, mode, switch, temperature | capabilityset, commonFaultDetection, electric, keyToneSwitch |
| `2S06` | 亚都除湿机YD-C870G | YD-C870G | 09B | childLockSwitch, humidity, mode, switch, temperature | commonFaultDetection, dehumidify, delayOn, gear, indicator, keyToneSwitch, waterTank |
| `2S1U` | 电小酷智能插排CP5-HW | CP5-HW | 01E | childLockSwitch, switch, switch1, switch2, switch3 | commonFaultDetection, indicator, memorySwitch, switch4, usbSwitch1 |
| `2S5V` | 贝昂空气净化器KJ300F-P50(H) | KJ300F-P50(H) | 013 | childLockSwitch, fan, mode, pm25, switch | autoClean, indicator, screenSwitch |
| `2S6B` | 美的热泵洗烘一体机Pro | MDH12F200 | 015 | action, childLockSwitch, mode, status, switch | alarmTime, cloudProgramMirroring, commonFaultDetection, completedParam, doorStatus, dryDegree, electric, fsReminder, fsStatus, lbStatus, ldReminder, ldStatus, leftTime, nightModeSetting, odorGuard, preTimeEnd, remoteControlService, rinseTimes, rotateSpeedGear, smartDetergentDispensing, spinTime, stains, steam, tempSettingMode, tsmartDispenseMode, voiceAssist, washTime, washmachine, waterConsumption, waterLevel |
| `2S6C` | 美的热泵洗烘一体机 | MDH12F100 | 015 | action, childLockSwitch, mode, status, switch | alarmTime, cloudProgramMirroring, commonFaultDetection, completedParam, doorStatus, dryDegree, electric, fsReminder, fsStatus, lbStatus, ldReminder, ldStatus, leftTime, nightModeSetting, odorGuard, preTimeEnd, remoteControlService, rinseTimes, rotateSpeedGear, smartDetergentDispensing, spinTime, stains, steam, tempSettingMode, tsmartDispenseMode, voiceAssist, washTime, washmachine, waterConsumption, waterLevel |
| `2S7J` | 创维热泵洗烘一体机Pro | XQG130-CZ2YDHT | 015 | action, childLockSwitch, mode, status, switch | alarmTime, ambientLighting, careClothesMode, commonFaultDetection, dryDegree, fsReminder, fsStatus, keypressSound, ldReminder, ldStatus, leftTime, preTimeEnd, proceduralMemory, remoteControlService, rinseTimes, rotateSpeedGear, smartDetergentDispensing, tempSettingMode, tsmartDispenseMode, uvSterilization, wFexecuteAferComplton, wFforgetuinesRetieval, wakeupInduction, wakeupInductionEnableSetting, washClothesMode, washTime, washmachine |
| `2S7K` | 创维热泵洗烘一体机 | XQG130-CZ1YDHT | 015 | action, childLockSwitch, mode, status, switch | alarmTime, careClothesMode, commonFaultDetection, dryDegree, fsReminder, fsStatus, ldReminder, ldStatus, leftTime, preTimeEnd, proceduralMemory, remoteControlService, rinseTimes, rotateSpeedGear, smartDetergentDispensing, tempSettingMode, tsmartDispenseMode, wFexecuteAferComplton, wFforgetuinesRetieval, washTime, washmachine |
| `2SDJ` | 恩仕AXENT.META云控智能浴缸 | T360 | 297 | childLockSwitch, colourMode, mode, status, switch | commonFaultDetection, constantTemperatureSwitch, durationOfWaterInflow, heat, massageSwitch, reminderSwitch, self-cleaningStatus, waterGear |
| `2SLC` | MEIPONT智能空调 | MAC35V1P7HR | 012 | fan, mode, status, switch, temperature | commonFaultDetection, electric, favoriteMode, favoriteModeSwitch, keyToneSwitch, preTime, runtime, sceneMode, switchPTC, switchScreen |
| `A0KD` | 博世蒸汽烤箱 | HSG656XS7W | 024 | action, mode, status, switch, temperature | faultDetection, leftTime, preTimeStart, setWorkTime, workTime |
| `A0KI` | 博世全自动咖啡机 | CTL636ES6W | 0B9 | action, mode, status, switch, temperature | currentOutlet, gear |
| `A0OW` | 律动灯带 |  Smart light strip | 01B | brightness, cct, colour, colourMode, switch | — |
| `A0OY` | 五色灯 | Smart light | 01B | brightness, cct, colour, colourMode, switch | — |
| `A0VV` | COLMO智能洗碗机 | CDB412 | 078 | action, mode, status, switch, temperature | air, bright, chidLockSwitch, doorSwitch, dry, faultDetection, leftTime, preLeftTime, softWater |
| `A1Z5` | JWV12-A6洗碗机 | JWV12-A6 | 078 | action, mode, status, switch, temperature | addMode, brightener, commonFaultDetection, leftTime, modeSwitch, orderSwitch, preTimeEnd, remainingTime, timeSet, washingSalt |
| `A1ZG` | JWB12-B5洗碗机 | JWB12-B5 | 078 | action, mode, status, switch, temperature | addMode, brightener, commonFaultDetection, orderSwitch, preTimeEnd, remainingTime, timeSet, washingSalt |
| `A2GT` | 西门子嵌入式洗碗机 | SJ656X26JC | 078 | action, mode, status, switch, temperature | faultDetection, lefttime1 |
| `A2GU` | 西门子半嵌入式洗碗机 | SJ558S06JC | 078 | action, mode, status, switch, temperature | faultDetection, lefttime1 |
| `A2P5` | COLMO洗碗机CDFB16G55 | CDFB16G55 | 078 | action, mode, status, switch, temperature | bright, doorSwitch, faultDetection, leftTime, softwater |
| `A2V7` | 彩灯 | RGBCW | 119 | brightness, cct, colour, colourMode, switch | — |
| `A344` | 美的踢脚线取暖器 | HDY22TH | 06A | childLockSwitch, mode, status, switch, temperature | commonFaultDetection, gear, preTimeOff, preTimeOn |
| `A3AL` | COLMO图灵二代中央空调 | CAKWxZN1C1-9(2)/CACxZN1C1-8(2) | 012 | fan, humidity, mode, switch, temperature | automaticAirswitch |
| `A3B5` | 美的中央空调86T5 | KJR-86T5/BK | 2FA | fan, humidity, mode, switch, temperature | ptcEnable, ptcSwitch |
| `A3HY` | 方太智能制冷油烟机 | CXW-358-LC15-A1.i | 021 | fan, lightSwitch, status, switch, temperature | acMode, acSwitch, gear, lockSwitch, midFanSwitch, ventilationSwitch |
| `A3MM` | 美诺智能蒸炉 | DG7240 C | 022 | action, mode, status, switch, temperature | commonFaultDetection, leftTime |
| `A3N3` | 方太智能水槽净食机 | JBID6E-04-X20Max | 078 | action, childLockSwitch, mode, status, switch | addMode, auxiliarySwitch, commonFaultDetection, washLeftTime, workMode |
| `A3NC` | 美的风管机双出风SS | KFR-75T2/B3-SS(1)IV | 2FA | fan, humidity, mode, switch, temperature | automaticAirswitch, commonFaultDetection, hvacType, light, sceneMode, switchScreen, tempControlMode |
| `A3ND` | 美的中央空调双出风SS | MJV-28T2/P-SS | 2FA | fan, humidity, mode, switch, temperature | automaticAirswitch, calmSpellSwitch, commonFaultDetection, hvacType, light, sceneMode, switchScreen, tempControlMode, waterAndFanValveMode |
| `A3QD` | COLMO新象中央空调(M)X2 | CAKW22ZN1X2 | 2FA | fan, humidity, mode, switch, temperature | automaticAirswitch, calmSpellSwitch, commonFaultDetection, hvacType, light, sceneMode, sterilization |
| `A3QE` | COLMO新象中央空调(C)X2 | CAKW22ZN1X2 | 2FA | fan, humidity, mode, switch, temperature | automaticAirswitch, calmSpellSwitch, commonFaultDetection, hvacType, light, sceneMode, sterilization |
| `A3QM` | 美的壁挂式空调KS2 | KFR-26G/KS2 | 012 | fan, lightSwitch, mode, switch, temperature | ECOswitch, airConditioner, automaticAirswitch, commonFaultDetection, fastColdheat, switchPTC |
| `A3QT` | 德业除湿机DYD-T22A3 | DYD-T22A3 | 09B | childLockSwitch, humidity, mode, switch, temperature | anionSwitch, dehumidify, gear, waterTank |
| `A3QY` | 美的智能风扇灯 FY3 | M0200062 | 114 | brightness, cct, fan, lightMode, switch | fanMode, switchFan, verticalSwitch |
| `A3R3` | 德业除湿机DYD-E12A3 | DYD-E12A3 | 09B | childLockSwitch, humidity, mode, switch, temperature | gear, waterTank |
| `A3RJ` | 德业除湿机U20 Air | U20 Air | 09B | childLockSwitch, humidity, mode, switch, temperature | anionSwitch, dehumidify, waterTank |
| `A3RO` | 美的立柜式空调T3 | KFR-72L/T3 | 2F9 | fan, humidity, mode, switch, temperature | airClean, airCleangear, airConditioner, automaticAirswitch, commonFaultDetection, freshAirSpeed, freshAirSwitch, keepHumidity, keyToneSwitch, oneTouchFreshAir, sceneMode, switchPTC, switchScreen |
| `A3RX` | 德业除湿机DYD-D50A3 | DYD-D50A3 | 09B | childLockSwitch, humidity, mode, switch, temperature | dehumidify, gear, waterTank |
| `A3SM` | 美的立柜式空调T6 | KFR-72L/T6 | 2F9 | fan, humidity, mode, switch, temperature | TVOC, airClean, airCleangear, airConditioner, airSterilizationSwitch, automaticAirswitch, calmSpellSwitch, commonFaultDetection, freshAirSpeed, freshAirSwitch, healthFunctionSwitch, keepHumidity, keyToneSwitch, light, mildewProofswitch, oneTouchFreshAir, sceneMode, sterilization, switchPTC, switchScreen |
| `A3T4` | 美的智能风扇灯 F5 | M0200057 | 114 | brightness, cct, fan, lightMode, switch | fanMode, switchFan, verticalSwitch |
| `A3TY` | 美的壁挂式空调T6 | KFR-35G/T6 | 012 | fan, humidity, mode, switch, temperature | ECOswitch, airClean, airCleangear, airConditioner, airSterilizationSwitch, automaticAirswitch, calmSpellSwitch, commonFaultDetection, freshAirSpeed, freshAirSwitch, healthFunctionSwitch, keepHumidity, keyToneSwitch, oneTouchFreshAir, sterilization, switchPTC, switchScreen |
| `A3U6` | 美的智能风扇灯 FW3 | FW3 | 114 | brightness, cct, fan, lightMode, switch | switchFan |
| `A3W2` | 美的壁挂式空调T2 | KFR-35G/T2 | 012 | fan, humidity, mode, switch, temperature | ECOswitch, airConditioner, airSterilizationSwitch, automaticAirswitch, calmSpellSwitch, commonFaultDetection, keepHumidity, oneTouchFreshAir, softWindSwitch, switchPTC |
| `A3W3` | 美的壁挂式空调50GT3 | KFR-50G/T3 | 012 | fan, humidity, mode, switch, temperature | ECOswitch, airClean, airCleangear, airConditioner, automaticAirswitch, calmSpellSwitch, commonFaultDetection, fastColdheat, freshAirSpeed, freshAirSwitch, keepHumidity, oneTouchFreshAir, switchPTC |
| `A3W5` | 美的壁挂式空调T5 | KFR-35G/T5 | 012 | fan, humidity, mode, switch, temperature | ECOswitch, airClean, airCleangear, airConditioner, automaticAirswitch, calmSpellSwitch, commonFaultDetection, freshAirSpeed, freshAirSwitch, keepHumidity, oneTouchFreshAir, switchPTC |
| `A3WP` | COLMO睿极风管机A3 | CA38ZN8A3 | 2FA | fan, humidity, mode, switch, temperature | airConditioner, calmSpellSwitch, commonFaultDetection, hvacType, sceneMode, sterilization, switchPTC, switchScreen |
| `A3X6` | 美的立柜式空调空气机T5 | KFR-72L/T5 | 2F9 | fan, humidity, mode, switch, temperature | ECOswitch, airClean, airCleangear, airConditioner, automaticAirswitch, commonFaultDetection, freshAirSpeed, freshAirSwitch, keepHumidity, oneTouchFreshAir, sterilization, switchPTC |
| `A3XN` | 美的壁挂式空调空气机T3II | KFR-35G/T3-II | 012 | fan, humidity, mode, switch, temperature | ECOswitch, airClean, airCleangear, airConditioner, automaticAirswitch, commonFaultDetection, freshAirSpeed, freshAirSwitch, healthFunctionSwitch, keepHumidity, oneTouchFreshAir, sceneMode, switchPTC |
| `A3XY` | 美的立柜式空调空气机T3Z | KFR-51L/T3Z | 2F9 | fan, humidity, mode, switch, temperature | ECOswitch, airConditioner, airSterilizationSwitch, automaticAirswitch, commonFaultDetection, keepHumidity, oneTouchFreshAir, sceneMode, sterilization, switchPTC |
| `A3YH` | COLMO中央空调图灵Pro | CAKW22ZN1T2 | 2FA | fan, humidity, mode, switch, temperature | airConditioner, calmSpellSwitch, commonFaultDetection, hvacType, light, sceneMode, sterilization |
| `A3YI` | COLMO中央空调一风口 | CAKW28ZN1-Y | 2FA | fan, humidity, mode, switch, temperature | airConditioner, commonFaultDetection, sceneMode, sterilization |
| `A3YS` | 美的立柜式空调空气机T2 | KFR-51L/T2 | 2F9 | fan, humidity, mode, switch, temperature | ECOswitch, airConditioner, airSterilizationSwitch, automaticAirswitch, commonFaultDetection, keepHumidity, oneTouchFreshAir, sceneMode, sterilization, switchPTC |
| `A3ZM` | 博世壁挂式迷你洗衣机 | WZW70AU00W | 015 | action, childLockSwitch, mode, status, switch | commonFaultDetection, finishinRelative, leftTime, presetSwitch |
| `A3ZQ` | 嘉格纳200 系列独立式干衣机 | WT260860 | 0D7 | action, childLockSwitch, mode, status, switch | commonFaultDetection, leftTime, preTimeEnd, presetSwitch |
| `A40N` | 美的风管机酷省电Ultra | KFR-75T2/B3-KSU(1) | 2FA | fan, humidity, mode, switch, temperature | airConditioner, commonFaultDetection, hvacType, sceneMode, sterilization, switchPTC |
| `A41P` | 美的壁挂式空调风尊II | KFR-35G/MXC1II | 012 | fan, humidity, mode, switch, temperature | ECOswitch, airConditioner, automaticAirswitch, commonFaultDetection, switchPTC |
| `A41Q` | 美的壁挂式空调风尊3 | KFR-35G/MXC3 | 012 | fan, humidity, mode, switch, temperature | ECOswitch, airConditioner, automaticAirswitch, commonFaultDetection, fastColdheat, favoriteModeSwitch, switchPTC |
| `A424` | 嘉格纳200 系列独立式洗衣机 | WM260860 | 015 | action, childLockSwitch, mode, status, switch | commonFaultDetection, leftTime, preTimeEnd, presetSwitch |
| `A439` | 美的壁挂式空调全面风Q2 | KFR-35G/Q2 | 012 | fan, humidity, mode, switch, temperature | ECOswitch, airConditioner, automaticAirswitch, commonFaultDetection, oneTouchFreshAir, sceneMode, switchPTC |
| `A44A` | 美的除湿机CF14BSDK | CF14BS/DK | 09B | childLockSwitch, fan, humidity, mode, switch | anionSwitch, commonFaultDetection, dehumidity, delayOff, delayOn, indicator, keyToneSwitch |
| `A451` | 欧瑞博空调 | MS-HVAC | 2FA | fan, humidity, mode, switch, temperature | commonFaultDetection |
| `A483` | 美的立柜式空调无风感W2 | KFR-72L/W2 | 2F9 | fan, humidity, mode, switch, temperature | ECOswitch, airConditioner, automaticAirswitch, commonFaultDetection, sceneMode, switchPTC |
| `A485` | 美的立柜式空调无风感FA2 | KFR-72L/FA2 | 2F9 | fan, humidity, mode, switch, temperature | ECOswitch, automaticAirswitch, calmSpellSwitch, commonFaultDetection, oneTouchFreshAir, sceneMode, switchPTC |
| `ZG08` | 华为全屋智能灯带驱动器 | BER-LD01 | A0E | brightness, cct, colour, colourMode, switch | faultDetection, subProduct |
| `ZG0D` | 智能开关 3键 | OSLO-SS3 | A13 | brightness, childLockSwitch, switch1, switch2, switch3 | backlight, button1, button2, button3, faultDetection, memorySwitch, mode1, mode2, mode3, reboot |
| `ZG0O` | 华为全屋智能 1路 RGBCW 恒压 100W | BER-LD01 | A0E | brightness, cct, colour, colourMode, switch | faultDetection, subProduct |
| `ZG11` | 智能开关 3键 | OSLO-SS3 | A13 | brightness, childLockSwitch, switch1, switch2, switch3 | backlight, button1, button2, button3, faultDetection, memorySwitch, mode1, mode2, mode3, reboot |
| `ZG1V` | 智能开关 3键 | PHP-W3-P1 | A13 | brightness, childLockSwitch, switch1, switch2, switch3 | backlight, button1, button2, button3, faultDetection, memorySwitch, mode1, mode2, mode3, reboot |
| `ZG1W` | 智能开关 4键 | PHP-W4-P1 | A13 | brightness, childLockSwitch, switch1, switch2, switch3 | backlight, button1, button2, button3, button4, faultDetection, memorySwitch, mode1, mode2, mode3, mode4, reboot |
| `ZG2K` | 智能开关 6键 | PHP-W6 | A13 | brightness, childLockSwitch, switch1, switch2, switch3 | backlight, button1, button2, button3, button4, button5, button6, faultDetection, memorySwitch, mode1, mode2, mode3, mode4, mode5, mode6, reboot |
| `ZG31` | 智能开关 都灵 4键 | PCP-TP4116 | A13 | brightness, childLockSwitch, switch1, switch2, switch3 | backlight, button1, button2, button3, button4, faultDetection, memorySwitch, mode1, mode2, mode3, mode4, reboot, theme |
| `0107` | 灯带组 |  | 01B | brightness, colour, lightMode, switch | — |
| `101L` |  |  |  | switch, switch1, switch2, switch3 | — |
| `101r` | 得邦智能吸顶灯 | CLL106207213027 | 01B | brightness, cct, lightMode, switch | — |
| `104M` | 欧普智能灯带OPDD | OPDD | 01B | brightness, colour, mode, switch | relativeDelay |
| `1054` | 瑞晶吊灯RAL-1 | RAL-1 | 01B | brightness, cct, colour, switch | — |
| `1056` | 瑞晶灯带RAL-3 | RAL-3 | 01B | brightness, cct, colour, switch | — |
| `105G` |  |  |  | switch, switch1, switch2, switch3 | — |
| `105H` |  |  |  | switch, switch1, switch2, switch3 | — |
| `1062` | 飞比彩灯NZCW125W-H1 | OPDD | 01B | brightness, colour, mode, switch | relativeDelay |
| `1077` | 云水母智能护眼台灯 | D01Kid | 01B | brightness, cct, lightMode, switch | lightGraduallyWakeUp, lightNoisyWakeUp |
| `107E` | LOEIN 乐因智能香薰灯 | YA06 | 04C | brightness, colour, lightMode, switch | aromaMode, aromaSwtich, faultDetection, lightSwtich |
| `111T` | 佛山照明智能吸顶灯ZNQP-9W | ZNQP-9W | 01B | brightness, cct, colourMode, switch | — |
| `114Z` | 奥普浴霸QDP6020AHW | QDP6020AHW | 035 | lightSwitch, mode, switch, temperature | currentTemperature, faultDetection, leftTime |
| `121Q` | 土豆双色智能灯 | T-01 | 01B | brightness, cct, lightMode, switch | backlight |
| `122U` | 智能鞋柜Mini | RS-FT-1S | 065 | action, mode, status, temperature | childLock, faultDetection, purificationWS, selfClean, sortStoving, stovingTemp, stovingWS, warmthTemp, warmthWS, workTime |
| `124R` | 鸿雁WIFIUSB智能排插 | IHC8335A | 01E | switch, switch1, switch2, switch3 | protect, switchLock, usbSwitch1 |
| `128P` | nimova智能护眼台灯Pro | Reading lamp | 046 | brightness, cct, lightMode, switch | — |
| `133H` | 电热水器 | EWH-H | 027 | mode, status, switch, temperature | aes, faultCode, instantHeating, maxCapacity, reserveTimer |
| `133L` | FSL智颖吸顶灯 | FSL-XDD+YD | 01B | brightness, cct, colourMode, switch | NightlightMode |
| `133M` | FSL智能双色灯泡 | FSL-QP-TW | 01B | brightness, cct, colourMode, switch | — |
| `133O` | FSL智能调光调色筒灯 | MQ2.5AD-LED4 | 01B | brightness, cct, colourMode, switch | — |
| `134D` | 华为智选 欧普读写台灯 | Domestic Reading lamp | 046 | brightness, cct, lightMode, switch | backlight, nightSwitch |
| `137W` | A.O.史密斯热泵热水器HPA-EZ系列 | HPA-E1.5Z | 027 | mode, status, switch, temperature | aes, faultCode, instantHeating, pumpCycleTimer, singleCycle |
| `146M` | 华为智选 360智能扫地机2S | 2S-X80V2 | 031 | action, battery, mode, status | availableZones, curZone, edgeElement, faultDetection, gear, mainElement, strainerElement |
| `146N` | 华为智选 360智能扫地机2Pro | 2Pro | 031 | action, battery, mode, status | availableZones, curZone, edgeElement, faultDetection, gear, mainElement, strainerElement |
| `148T` | 木林森睿智系列LED台灯 | WU1215-11-W-40K | 046 | brightness, colourMode, lightMode, switch | tomatoClk |
| `153E` | 领普三键墙壁开关 | Q3D-HW-W3 | 005 | switch, switch1, switch2, switch3 | led |
| `154E` | 漾美无线充智能台灯 | U13 | 046 | brightness, colourMode, lightMode, switch | — |
| `154F` | 三思LED天花灯 | C22FL-DQ3-5W | 01B | brightness, colourMode, lightMode, switch | — |
| `155F` | FSL智薄卧室灯 | FSL-XDD-TW | 01B | brightness, cct, colourMode, switch | — |
| `166O` | 艾美特暖风机HPA21203R-H | HPA21203R-H | 06A | childLockSwitch, mode, switch, temperature | screenSwitch, state, swayLeftRight, timing |
| `172D` | POVOS奔腾加湿器 | PJ8005H | 052 | humidity, mode, switch, temperature | faultDetection, gear |
| `172U` | POVOS奔腾加湿器 | PJ8002H | 052 | humidity, mode, switch, temperature | Time, faultDetection, gear |
| `174Z` | 净诺抗菌除醛空气净化器 | KJ350G-H01 | 013 | childLockSwitch, fan, pm25, switch | Auto, Killscreen, Presskeytone, anionSwitch, cav, cmw1, filterElement, sleep |
| `175J` | 艾美特移动地暖HD30-A9 | HD30-A9 | 06A | childLockSwitch, mode, switch, temperature | heatingArea, screenSwitch, state, timing |
| `175N` | 艾美特移动地暖HD25-A7 | HD25-A7 | 06A | childLockSwitch, mode, switch, temperature | screenSwitch, state, timing |
| `187D` | 欧普暖芯浴霸 HWE6102i | HWE6102i | 035 | lightSwitch, mode, switch, temperature | leftTime, setWorkTime |
| `2008` | 欧普炫彩床头灯 | MoodLamp | 01B | brightness, colour, mode, switch | elantra, sleep, templateSave, templateSet1, templateSet2, templateSet3, templateSet4, templateSet5, templateSet6 |
| `200N` | 易百珑三路开关 | EWS03-H | 064 | switch, switch1, switch2, switch3 | CleanPair, Pair, memorySwitch |
| `2026` | 蓓慈足浴器BZ528V1 | BZ528V1 | 070 | mode, status, switch, temperature | Red, SetTemperature, Settime, faultDetection, leftTime, momo |
| `202Z` | 三思智能LED球泡灯 | C21BB-TE27-7W | 01B | brightness, colourMode, lightMode, switch | — |
| `203U` | 12W恒流调光调色驱动 | SJB01-QL-12W-2 | 01B | brightness, cct, colourMode, switch | — |
| `203X` | 24W恒流调光调色驱动 | SJB01-QL-24W-2 | 01B | brightness, cct, colourMode, switch | — |
| `204B` | 60W恒压调光调色驱动 | SJB01-QY-60W-2 | 01B | brightness, cct, colourMode, switch | — |
| `204E` | 120W恒压调光调色驱动 | SJB01-QY-120W-2 | 01B | brightness, cct, colourMode, switch | — |
| `204I` | 蓓慈足浴器BZ525V1 | BZ525V1 | 070 | mode, status, switch, temperature | faultDetection, leftTime, setTemperature, setTime, surfHeating |
| `207P` | 领普双键零火开关MESH | Q4D-BLE-W2(HW) | 005 | brightness, switch, switch1, switch2 | button1, button2, mode1, mode2 |
| `209D` | 亚摩斯养生壶YSH08-15C | YSH08-15C | 060 | mode, status, switch, temperature | faultDetection, leftTime, preTimeStart, presetSwitch, targetTemp |
| `20B5` | 亚都空气净化器KJ350F-PT2000Hi | KJ350F-PT2000(Hi) | 013 | childLockSwitch, fan, pm25, switch | filterElement1, light, sound |
| `20BE` | 新风门窗 | NH19 | 030 | fan, mode, status, switch | filterElement1, heatSwitch |
| `20CS` | 智汇云三位轻触开关面板 | Z4003 | 005 | switch, switch1, switch2, switch3 | — |
| `20FM` | 海令调色调光器 | SMK-H1-RGBW | 01B | brightness, colour, colourMode, switch | — |
| `20GL` | 万和热水器S5系列 | JSQ32-S5W17 | 027 | mode, status, switch, temperature | AffSetting, CurGas, HotLabor, InWTemp, TotalAff, TotalGas, TotalWater, ZCTempSet, faultDetection, zerocold |
| `20I0` | 华为智选 欧普智能台灯Pro | MT615-D20WTT | 046 | brightness, cct, lightMode, switch | nightMode, studyMode, studyResult |
| `20IU` | 小熊养生壶 | YSH-C15H6 | 060 | action, mode, status, temperature | faultDetection, heatGear, leftTime, preTimeStart, presetSwitch, setWorkTime, warmSwitch, workTime |
| `20K2` | 澳柯玛养生壶ADK-800S6 | ADK-800S6 | 060 | mode, status, switch, temperature | childLock, faultDetection, leftTime, preTimeStart, presetSwitch, targetPower, targetTemp |
| `20KM` | 鸿雁WIFI智能排插 | IHC8345A | 01E | switch, switch1, switch2, switch3 | protect, switch4, switchLock |
| `20KX` | HEIMAN空气质量检测仪 | WS2AQ | 006 | hcho, humidity, pm25, temperature | AlarmState, Disturb, HumidityThr, Identify, Istempc, Language, TemperatureThr, noise, power |
| `20L5` | 亚摩斯养生壶YSH1258 | YSH1258 | 060 | mode, status, switch, temperature | faultDetection, leftTime, preTimeStart, presetSwitch, targetPower, targetTemp |
| `20L7` | 亚摩斯养生壶YSH08-15B | YSH08-15B | 060 | mode, status, switch, temperature | childLock, faultDetection, leftTime, preTimeStart, presetSwitch, targetPower, targetTemp |
| `20MB` | 维尔森智能新风机 | VE-AN60WB | 030 | fan, mode, status, switch | faultDetection, filterElement1, heatSwitch, ledSwitch |
| `20S7` | 亚摩斯净水器AS-RO075 | AS-RO075 | 02D | childLockSwitch, mode, status, temperature | faultDetection, filterElement1, filterElement2, input, manualMode, output, waterLevel |
| `20WI` | 亚摩斯足浴盆AS-FT78B | AS-FT78B | 070 | mode, status, switch, temperature | faultDetection, heating, leftTime, massage, targetTemp, timing, timingOn, workTime |
| `20XC` | 控客-肖邦水地暖面板 | KK-FH-D21D | 012 | childLockSwitch, mode, switch, temperature | — |
| `20XI` | 控客-肖邦电地暖面板 | KK-FH-D31D | 012 | childLockSwitch, mode, switch, temperature | — |
| `2151` | 圆和四路智能开关 | X9ZK4 | 005 | switch, switch1, switch2, switch3 | switch4 |
| `215N` | 触控三开零火开关 | U4030100 | 005 | switch, switch1, switch2, switch3 | — |
| `215O` | 触控四开零火开关 | U4037400 | 005 | switch, switch1, switch2, switch3 | switch4 |
| `215V` | 智能环境盒子 | U40411060 | 006 | humidity, luminance, pm25, temperature | — |
| `2165` | 中央空调智能网关 | U4090509 | 012 | fan, mode, switch, temperature | — |
| `217K` | 开关智能控制器3型 | U4030300 | 005 | switch, switch1, switch2, switch3 | — |
| `2180` |  | KK-CM-D55 | 01C | action, mode, opener, status | — |
| `218A` | 西顿24W防蚊虫快装智能吸顶灯 | CEX24-W01 | 01B | brightness, cct, lightMode, switch | — |
| `218E` | 西顿30W防蚊虫快装智能吸顶灯 | CEX30-W01 | 01B | brightness, cct, lightMode, switch | — |
| `218F` | 西顿40W防蚊虫快装智能吸顶灯 | CEX40-W01 | 01B | brightness, cct, lightMode, switch | — |
| `2196` | 圆和三路智能开关 | X9ZK3 | 005 | switch, switch1, switch2, switch3 | — |
| `21DB` | 云起雅赫地暖温控器 | LS130 | 06A | lightSwitch, mode, switch, temperature | freezeSwitch, heatMode, heatTimer, memorySwitch |
| `21DJ` |  | LS063WH | 04E | battery, humidity, luminance, temperature | — |
| `21EM` | JW智能空调 | 1 | 012 | fan, mode, switch, temperature | — |
| `21EP` | JW空气检测A型 | 1 | 006 | hcho, humidity, pm25, temperature | co2, pm10, tvoc |
| `21FU` | 亚摩斯落地加湿器AS-V618 | AS-V618 | 052 | humidity, mode, switch, temperature | degerming, faultDetection, gear, timing |
| `21GG` | JW空气检测B型 | 1 | 006 | hcho, humidity, pm25, temperature | co2, tvoc |
| `21GI` | JW空气检测D型 | 1 | 006 | hcho, humidity, pm25, temperature | — |
| `21GV` |  | LS175 | 01C | fan, mode, switch, temperature | discovery |
| `21LS` | 欧普读写台灯SE | MT386-D10 | 046 | brightness, colourMode, lightMode, switch | tomatoClk |
| `21Q0` | 欧普智能筒灯 | LTD01306TT03 | 01B | brightness, cct, colourMode, switch | commonMemorySwitch1 |
| `21W4` | 瑞晶四关 | RGBLE-R-S4 | 064 | switch, switch1, switch2, switch3 | switch4 |
| `220K` |  | MR8231H | 012 | fan, mode, switch, temperature | — |
| `221P` |  | A3Z-KTXK-01 | 012 | fan, mode, switch, temperature | — |
| `221V` |  | A3Z-DK-03 | 005 | switch, switch1, switch2, switch3 | — |
| `221W` |  | A3Z-DK-04 | 005 | switch, switch1, switch2, switch3 | switch4 |
| `223Y` | 西顿芳华落地灯 | CEF50R-W01(hilink) | 01B | brightness, cct, lightMode, switch | Kcurve, backlight, select |
| `227T` | 亚摩斯睿雅零火开关双键 | ZJ-KG36H | 005 | brightness, switch, switch1, switch2 | — |
| `22DH` | 爱特嘉智能即热饮水吧 2 | AH-301 | 06F | childLockSwitch, status, switch, temperature | commonMode, dataWater, faultDetection, inputTds, location, machineTemp, outlet, rinseMode, sensorMode, setUpWater, tdsStatus, washingStatus |
| `22HW` | 亚摩斯嵌入式射灯 | AS-L26H | 01B | brightness, cct, colourMode, switch | — |
| `22V8` | 澳柯玛智能茶吧机 | YR5A-Y011（Y） | 09A | childLockSwitch, status, switch, temperature | coldwater, collectiontime, faultDetection, incubator, intake, soakingtime, targettemperature, warm |
| `2302` | 亚摩斯热浪足浴盆 | AS-FT056D | 070 | mode, status, switch, temperature | faultDetection, leftTime, light, massage, surf, timing |
| `231P` | Kyvol及悦空气炸锅 | AF600 | 063 | action, status, switch, temperature | CookMode, QuickRecipe, commonFaultDetection, leftTime, preTimeStart, presetSwitch, workTime |
| `23DZ` | 亚摩斯智能养生杯YSH08-10C | YSH08-10C | 060 | action, mode, status, temperature | faultDetection, heatGear, holdTemp, leftTime |
| `23RO` | 欧普智能吸顶灯 | MX420-D36-WTT-01 | 01B | brightness, cct, colourMode, switch | — |
| `23RP` | 欧普智能吸顶灯 | MX480-D48-WTT-01 | 01B | brightness, cct, colourMode, switch | — |
| `23RQ` | 欧普智能吸顶灯 | MX960-D150-WTT-01 | 01B | brightness, cct, colourMode, switch | — |
| `23W2` | ACEMATIC灯光模块 | SH100310KI | 064 | switch, switch1, switch2, switch3 | — |
| `23WO` | 亚摩斯极境开关四键 | ZJ-KG51H | 005 | switch, switch1, switch2, switch3 | switch4 |
| `2487` | 空气质量检测仪 | SAM/CM-TYC01 | 006 | alarm, hcho, humidity, temperature | displaymode, humHEnable, humLEnable, lightdelaytime, lightpower, tempHEnable, tempLEnable |
| `25WT` | 华为智选 欧普智能床头台灯 | MW001-15CF | 046 | brightness, colour, lightMode, switch | alarmSetting, colourLightMode, dataStatistics, nightWakeup, streamer, whiteLightMode |
| `279E` | 雅乐思电磁炉 | YLS-M03-WF | 079 | mode, status, switch, temperature | determine, powergear, time1 |
| `27B2` | 心智悦新风机B1 | RZBD-Z60A | 030 | fan, mode, status, switch | faultDetection, filterElement1, heatSwitch, ledSwitch |
| `27PM` | 鸿雁智能排插(四位分控) | IHC8345A | 01E | switch, switch1, switch2, switch3 | switch4 |
| `27SC` | 领普双键墙壁开关 | Q3S-HW-W2 | 005 | brightness, switch, switch1, switch2 | — |
| `2847` | 金凯瑞足浴盆 | HW-GY1 | 070 | action, mode, status, temperature | OneClickStart, leftTime, light, massage |
| `291T` | 飞利浦直流变频循环扇ACR3142CF | ACR3142CF | 029 | fan, mode, switch, temperature | OSD, RunTime, angleAutoLROnOff |
| `292D` | 飞利浦直流变频循环扇ACR3144CF | ACR3144CF | 029 | fan, mode, switch, temperature | RunTime, angleAutoAllOnOff, angleAutoLROnOff, childLockOnOff |
| `292H` | 飞利浦直流塔扇ACR3144TF | ACR3144TF | 029 | fan, mode, switch, temperature | RunTime, angleAutoLROnOff, anionOnOff |
| `295G` | TCL智爱台灯 | TCLTD-ZA01 | 046 | cct, colourMode, lightMode, switch | CountdownOff, Switchintelligent, brightnes, countdowntime, progressSwitch |
| `29EP` | 蓓慈X4V智能剃须刀 | X4V | 170 | battery, mode, status, switch | CZDT, CZJL, JCSM, LJZT, LXS, SYSJ, TXSD, TXSJ, TXXZS, commonFaultDetection |
| `29H9` | 华梦智能控制器 | Ai/SRS.0.1 | 064 | switch, switch1, switch2, switch3 | switch10, switch11, switch12, switch4, switch5, switch6, switch7, switch8, switch9 |
| `29X9` | 欧井智能除湿机OJ-223E | OJ-223E | 09B | childLockSwitch, humidity, mode, switch | Countdown, Purify, Temp, commonFilterElement1, faultDetection, gear |
| `2AA3` | 欧派洗碗机 | DW60-D908X | 078 | action, mode, status, switch | RemainingTimer, Temperature, faultDetection |
| `2AA5` | FSL调光调色吸顶灯-72W | FSL-XDD-TW-72 | 01B | brightness, cct, colourMode, switch | — |
| `2AB5` | ACEMATIC智能液晶面板 | SH640615WW | 005 | switch, switch1, switch2, switch3 | — |
| `2AJY` | Paulmann单色温智能灯 | CO200247 | 01B | brightness, colourMode, lightMode, switch | — |
| `2ANJ` |  | U2-86QMP-Z02(HW) | 012 | fan, mode, switch, temperature | — |
| `2ANO` | 鸿雁三路智能开关模块 | IHC1240HW | 064 | switch, switch1, switch2, switch3 | indicator |
| `2AOR` | FSL儿童卧室灯-海星 | FSL-ETD-HX | 01B | brightness, cct, colourMode, switch | — |
| `2AOS` | FSL智薄客厅灯 | XD819*519P-LED108 | 01B | brightness, cct, colourMode, switch | — |
| `2ASU` | 慕派AA级智能护眼台灯 | MPT01S | 046 | brightness, colourMode, lightMode, switch | tomatoClk |
| `2AVV` | 亚都空气净化器KJ450G-B4Hi | KJ450G-B4(Hi) | 013 | childLockSwitch, fan, pm25, switch | filterElement1, light, sound |
| `2AWX` |  | KK-AC-DJ50 | 012 | fan, mode, switch, temperature | — |
| `2BB0` | 华为智选 欧普智能吸顶灯24W | MX420-D24-WTT | 01B | brightness, cct, lightMode, switch | location, sleeping, timeMelody, wakeUp, wallSwitch1, wallSwitch2, wallSwitch3 |
| `2BB2` | 华为智选 欧普智能吸顶灯48W | MX480-D48-WTT | 01B | brightness, cct, lightMode, switch | location, sleeping, timeMelody, wakeUp, wallSwitch1, wallSwitch2, wallSwitch3 |
| `2BB3` | 华为智选 欧普智能吸顶灯128W | MX960-D130-WTT | 01B | brightness, cct, lightMode, switch | location, timeMelody, wallSwitch1, wallSwitch2, wallSwitch3 |
| `2BES` | FSL蓝牙调光调色吸顶灯 | FAX-36G10 | 01B | brightness, cct, colourMode, switch | — |
| `2BET` | FSL蓝牙调光调色筒灯 | MQ2.5J-LED3 | 01B | brightness, cct, colourMode, switch | — |
| `2BEU` | FSL蓝牙调光调色球泡 | FSL-TW-BLE | 01B | brightness, cct, colourMode, switch | — |
| `2BFE` | 东东阅读台灯 | AIT01S | 046 | brightness, colourMode, lightMode, switch | tomatoClk |
| `2BFM` | 享睡智能音乐睡眠灯 | EW202W | 046 | brightness, colour, lightMode, switch | LampDevStatus, alarmPreview, clockSleep, getAlarmList, playMusic, progressTurnOff, progressTurnOn, setAlarm, sleepMode, timeSetSync, timeStyle, tomatoClk |
| `2BG1` | 哈尔斯真空电热水壶 | HEK-1500-5AW | 09A | action, mode, status, temperature | Others, commonFaultDetection, leftTime, preTimeStart, presetSwitch, warmDuration, warmSwitch |
| `2BGN` | 三雄极光Pak智能吸顶灯 | PAK417160 | 01B | brightness, cct, lightMode, switch | — |
| `2BGU` | 沙漠鱼智能台灯 | YSTD-V1 | 046 | brightness, cct, lightMode, switch | — |
| `2BN0` | 领普三键单火开关MESH | Q4S-BLE-W3(HW) | 005 | switch, switch1, switch2, switch3 | button1, button2, button3, mode1, mode2, mode3 |
| `2BNN` | 华为智选 欧普智能台灯 2S | D0.2x108-WTT | 046 | brightness, cct, lightMode, switch | backlight, lightStatistics, nightWakeup, studyMode |
| `2BOS` |  | BL8231H | 012 | fan, mode, switch, temperature | — |
| `2BS9` | FSL智趣UFO吸顶灯 | FSL-ETD-UFO | 01B | brightness, cct, colourMode, switch | — |
| `2BSZ` | FSL智贝吸顶灯 | FSL-ETD-BK | 01B | brightness, cct, colourMode, switch | — |
| `2C88` | 西蒙中央空调温控器Daikin | 70E7031 | 012 | fan, mode, switch, temperature | BackLightLevel, faultDetection |
| `2C89` | 西蒙中央空调温控器Gree | 70E7031 | 012 | fan, mode, switch, temperature | BackLightLevel, faultDetection |
| `2C8A` | 西蒙中央空调温控器Mitsubishi | 70E7031 | 012 | fan, mode, switch, temperature | BackLightLevel, faultDetection |
| `2C8B` | 西蒙中央空调温控器Toshiba | 70E7031 | 012 | fan, mode, switch, temperature | BackLightLevel, faultDetection |
| `2C8D` | 西蒙中央空调温控器Midea | 70E7031 | 012 | fan, mode, switch, temperature | BackLightLevel, faultDetection |
| `2CA6` | ACEMATIC空调模块 | B17XRT | 012 | fan, mode, switch, temperature | — |
| `2CCK` | ACEMATIC色温灯 | SH1216412KG | 01B | brightness, cct, colourMode, switch | — |
| `2CP2` | DBH智能肌肉按摩仪 | HDB20301 | 0C5 | action, battery, status, switch | fgMode, queryinfo, workTime |
| `2CVX` | 山本空气炸锅 | SB-D16TSW | 063 | action, status, switch, temperature | faultDetection, recipe, remainTime, start, temp, workTime |
| `2D80` | 华为智选 360智能扫地机2 | 2 | 031 | action, battery, mode, status | availableZones, curZone, edgeElement, faultDetection, gear, mainElement, strainerElement |
| `2DMD` | 三路智能开关 | JM-6013 | 005 | switch, switch1, switch2, switch3 | backlight |
| `2DME` | 四路智能开关 | JM-6014 | 005 | switch, switch1, switch2, switch3 | backlight, switch4 |
| `2DSD` | 拉孚三路智能开关 | HL303R | 005 | switch, switch1, switch2, switch3 | — |
| `2DXC` | 龙泉智家三路墙壁开关 | LQ-K03H | 005 | switch, switch1, switch2, switch3 | — |
| `2E4V` | 爱莱克特智能擦地机 | ELZ818 | 031 | action, battery, mode, status | cleansum, cleantime, cswitch, dryorwet, faultwaring, find, getclean, setHz, setclean, sethear, setwater, wakeup, water |
| `2ENH` | 亚摩斯星耀开关三键 | ZJ-KG28H | 005 | switch, switch1, switch2, switch3 | — |
| `2ENI` | 亚摩斯星耀开关四键 | ZJ-KG29H | 005 | switch, switch1, switch2, switch3 | switch4 |
| `2EXV` | 达伦自然光吸顶灯S3 Pro | S3 Pro | 01B | brightness, colourMode, lightMode, switch | lampswitch, natural, nightmode |
| `2EZU` | 亚摩斯睿雅单火开关三键 | ZJ-KG33H | 005 | switch, switch1, switch2, switch3 | — |
| `2F2H` | FSL智影炫彩灯带-3米 | ST-10W3ZY | 01B | brightness, colour, colourMode, switch | Create, commonMode1, commonMode2, progressTurnOff, progressTurnOn |
| `2FCZ` | 博顿物联三开 | BD-S6B003 | 005 | switch, switch1, switch2, switch3 | — |
| `2FD0` | 博顿物联四开 | BD-S6B004 | 005 | switch, switch1, switch2, switch3 | switch4 |
| `2FGH` | 宝贝第一灵悦JOY | R153A | 0DF | alarm, battery, switch, temperature | ConstantTemperatureWind, NaturalWind, PowerLimit, powerSupply |
| `2FJ3` | 贝昂落地式循环扇(鸿蒙版) | FZS2-Pro | 029 | fan, mode, switch, temperature | light, lock, timingOff, timingOn |
| `2FJ4` | 贝昂台式循环扇 | FZT2-Table | 029 | fan, mode, switch, temperature | light, lock, timingOff, timingOn |
| `2FNZ` | 长虹空调挂机 | KFR-35GW/ZDAYW2-R1 | 012 | fan, mode, switch, temperature | ECO, electricalHeating, faultDetection, fresh, outdoor, selfclean, temper |
| `2FXH` | 九牧M9智能浴缸 | Y099117-1A02-1 | 297 | mode, status, switch, temperature | commonFaultDetection, countDown, paraSet, waterLevel |
| `2GKG` | 美森智能电动理容器 | WHT8P | 170 | battery, mode, status, switch | AvailableTime, FirmwareUpgrade, TotalTimes |
| `2GKH` | 美森智能吸发理发器 | WHS6 | 0E9 | battery, mode, status, switch | AvailableTime, CutterHeadAlarm, CutterheadRemaining, FirmwareUpgrade, ResetCutterHead, SafeLok, TotalTimes |
| `2GVO` | 狄耐克智能三路开关面板 | SH-WDQ-LGT301 | 005 | switch, switch1, switch2, switch3 | — |
| `2H57` | 鲜芒情景灯 | XM032-F03A | 112 | brightness, cct, lightMode, switch | nightWakeup, progressTurnOff, progressTurnOn, toggleSwitch |
| `2H5I` | 亚都加湿器SZ700-TJK600(Hi) | SZ700-TJK600(Hi) | 052 | childLockSwitch, humidity, switch, temperature | anion, dried, faultDetection, gear, level, light, sleep, timing, uv, water |
| `2HDO` | 嵌洗JBCD15E-X20.i | JBCD15E-X20.i | 078 | mode, status, switch, temperature | faultDetection, leftTime |
| `2HED` | 油烟机X20.i | CXW-358-01-X20.i | 021 | lightSwitch, mode, status, switch | Ambientlight, LockScreen, faultDetection, gear, lockSwitch |
| `2HF2` | 长虹空调柜机 | KFR-72LW/ZDTBW1-R1 | 012 | fan, mode, switch, temperature | ECO, TemperandhumiControl, dedusting, electricalHeating, faultDetection, fresh, humidity1, outdoor, selfclean, temper |
| `2HKE` | 亚都加湿器SZ1200-TK101(Hi) | SZ1200-TK101(Hi) | 052 | childLockSwitch, humidity, switch, temperature | anion, dried, faultDetection, gear, level, light, sleep, timing, uv, water |
| `2HKO` | 空气炸锅D05 | CZG-D05BC | 063 | action, status, switch, temperature | FirmwareUpdate, faultDetection, recipes, workStatus, workTime |
| `2HR8` | 西蒙三位智能开关 | 58E8203 | 005 | switch, switch1, switch2, switch3 | commonFaultDetection, indicator, switchStatus |
| `2HR9` | 西蒙四位智能开关 | 58E8204 | 005 | switch, switch1, switch2, switch3 | commonFaultDetection, indicator, switch4, switchStatus |
| `2HUS` | 万和燃气热水器YL5 | JSQ32-17YL5-HOS | 124 | mode, status, switch, temperature | ECO, appointment, boostMode, curGas, curWater, dingshi, faultDetection, pretemp, totalGas, totalWater, zeroColdMode, zeroColdSwitch |
| `2HYH` | 8859浴用加热器-足浴器 | CDN-ZY8859 | 070 | action, mode, switch, temperature | bubble, faultDetection, leftTime, ozone, setWorkTime, temperatures |
| `2I43` | 万和燃气热水器ML1 | JSQ27-14ML1-HOS | 124 | mode, status, switch, temperature | ECO, appointment, boostMode, curGas, curWater, dingshi, faultDetection, pretemp, totalGas, totalWater, zeroColdMode, zeroColdSwitch |
| `2I67` | 左点砭石按摩器 | ZD-JS0101 | 0CA | battery, mode, status, switch | guide, heat, remainTime, usage, vibrat |
| `2I8T` | 家用智能中央电暖对流取暖器AHR4146ZS | AHR4146ZS | 06A | childLockSwitch, mode, switch, temperature | OSD, gear, runTime |
| `2IEY` | 康宝牌XDZ45-HM1消毒柜 | XDZ45-HM1 | 0D5 | humidity, status, switch, temperature | CleanTips, WarmingPlateTime, cabinetDoor, cabinetMode, cabinetRemainingTime, faultDetection |
| `2IHM` | 万家乐 燃气热水器 Z8L | JSQ30-16Z8L | 124 | mode, status, switch, temperature | Ambient, Doubleboost, SingleParameter, cmdtype, faultDetection, orderTime, totalGas, zeroColdMode, zeroColdSwitch |
| `2INR` | 艾家智能三位开关 | Z1K3 | 005 | switch, switch1, switch2, switch3 | lightness, switchStatus |
| `2ISS` | 根元嵌入式衣物护理机 | RS-AP003 | 1B7 | action, mode, status, switch | faultDetection, leftTime, timing |
| `2IWD` | 西蒙弈系列超薄吸顶灯 | LCR2601-HW | 112 | brightness, colourMode, lightMode, switch | colorTemperature, progressTurnOn, sleepMode |
| `2IWN` | 朗威智能剃须刀 | Rs51 | 170 | battery, mode, status, switch | bladeCleanTime, bladeUseTime, btConnection, clearMode, deviceTime, runTime, shavSpeed, userecord |
| `2J6Y` | 达伦智能台灯3i | DL-01W Pro | 046 | brightness, colourMode, lightMode, switch | backlight, fadeTime, indicator, lightStatus, mainSwitch, nightWakeup, record, toggleSwitch |
| `2J8Z` | 企一照明RGB灯带蓝牙驱动 | QYHW150BRGB | 226 | brightness, colour, colourMode, switch | commonFaultDetection, relBrightness, toggleSwitch |
| `2JCH` | A.O.史密斯彩钢单胆电热水器 | CEWH-80GH | 027 | mode, status, switch, temperature | Timing, faultDetection, increaseCapacitySwitch, instantHeatSwitch |
| `2JCI` | A.O.史密斯彩钢双胆电热水器 | EWH-80HGCH | 027 | mode, status, switch, temperature | faultDetection, increaseCapacitySwitch, instantHeatSwitch, leftTime, presetSwitch, sterilizationSwitch |
| `2JHB` | 黑白生活智能筋膜枪U51 | U51 | 0C5 | battery, mode, status, switch | Remainingtime, Videointroduction, gear, worktime |
| `2K5B` | 大拿电动剃须刀 | DT-R307 | 170 | battery, mode, status, switch | Bassmode, Faultalarm, ResetShaverHead, SpeedAdjustment, others, safetylock, searchequipment, speed, userrecord, worktime |
| `2K88` | 霍尼韦尔空气净化器KJ560F-P22R | KJ560F-P22R | 013 | fan, mode, pm25, switch | UVSwitch, filterElement1, filterElement2, tvoc |
| `2K89` | 霍尼韦尔空气净化器KJ460F-J21SW | KJ460F-J21SW | 013 | fan, mode, pm25, switch | filterElement1, filterElement2 |
| `2K8I` | 黑白生活智能筋膜枪U52 | U52 | 0C5 | battery, mode, status, switch | Remainingtime, Videointroduction, afterservice, gear, worktime |
| `2KCI` | F20蒸烤一体机 | JFQ-50F20 | 19B | action, status, switch, temperature | ClnMode, aTime, cGear1a, cSubMode1a, cTime1a, cUTemp1a, dStat, devMode, faultDetection, id, lackWater, leftTime, preHeatPrg, runStat, typeMode |
| `2KFX` | 德业除湿机DYD-M45A3 | DYD-M45A3 | 09B | humidity, mode, switch, temperature | CO, anionSwitch, fanstate, faultDetection, frost, gear, swingSwitch |
| `2KH6` | CXW-200-J6058吸油烟机 | CXW-200-J6058 | 021 | lightSwitch, mode, status, switch | faultDetection, lBReTl, lBStatl, lBStatr, remainCloseMin, runTim, steamWash |
| `2KHB` | JWV12-A2洗碗机 | JWV12-A2 | 078 | action, mode, status, switch | RemainingTimeD, faultDetection, funcmode, funcstep, leftTime, preTimeEnd, preTimeStart, presetSwitch, runningstatus, washfinishstat |
| `2KJ0` | KAMAI灯 | KM032-F03A | 112 | brightness, cct, lightMode, switch | nightWakeup, progressTurnOff, progressTurnOn, toggleSwitch |
| `2KR9` | 斯诺德凯奇Mini筋膜枪 | 8193 | 0C5 | battery, mode, status, switch | Introduction, Lefttime, afterservice, gear, worktime |
| `2L17` | 亚都除湿机YD-C1600Pro(Hi) | YD-C1600Pro(Hi) | 09B | childLockSwitch, humidity, switch, temperature | anionSwitch, gear, level, light, sound, state, timing |
| `2L8O` | 九牧JD174S多功能取暖器 | JD174S | 035 | humidity, lightSwitch, status, temperature | ArefactionEnable, ArefactionSwitch, airQualityGrade, aircleanSwitch, drySwitch, faultEvent, nightLightSwitch, odorsensingSwitch, sleepSwitch, standbySwitch, swingSwitch, timePara, ventilateSwitch, warmWindMode, windSwitch |
| `2L8U` | 立达信元梦吸顶灯 | CLTD-YM02-D45-HM | 112 | brightness, cct, lightMode, switch | lamplightMode |
| `2L8W` | 立达信云上吊灯 | PLTD-YS05-M120-HS-HM | 21E | brightness, cct, lightMode, switch | lamplightMode |
| `2L9U` | 亚都除湿机YD-C4000Pro(Hi) | YD-C4000Pro(Hi) | 09B | childLockSwitch, humidity, switch, temperature | anionSwitch, gear, level, light, state, timing, uv |
| `2LGR` | 科威德迩空气消毒机CD-VHW | CD-VHW | 013 | fan, mode, status, switch | ATVOC, allstatus, faultDetection, filterElement1, light, quality |
| `2LRN` | 亚都加湿器SZ750-TJK800(Hi) | SZ750-TJK800(Hi) | 052 | childLockSwitch, humidity, switch, temperature | dried, faultDetection, gear, lamp, level, light, timing, uv, water |
| `2LTE` | 摩申电动剃须刀MTR307 | MTR307 | 170 | battery, mode, status, switch | Bassmode, Faultalarm, ResetShaverHead, SpeedAdjustment, safetylock, searchequipment, speed, userrecord, worktime |
| `2LYO` | 松下洗衣机 XQG100-V19R | XQG100-V19R | 015 | childLockSwitch, mode, status, switch | commonFaultDetection, leftTime, newAction, newStatus |
| `2M9H` | 云鲸智能拖扫一体机器人J3 | YJCC012 | 031 | action, battery, mode, status | faultDetection, gear, narwalCmd, revokeDeviceAuth, robotBaseStatus, robotWorkingStatus |
| `2MC1` | SJSW三色灯 | SJSW-DD Smart | 118 | brightness, cct, lightMode, switch | fade |
| `2MCG` | 亚都加湿器SZ400-TJK400(Hi) | SZ400-TJK400(Hi) | 052 | childLockSwitch, humidity, switch, temperature | dried, faultDetection, gear, level, water |
| `2MDD` | 小适智能剃须刀 | Ai501 | 170 | battery, mode, motor, status | charge, knifereset, lock, state, unusual |
| `2MGV` | 吉豪X5智能筒射灯 | JH-X5-75-10W 10W | 111 | brightness, cct, lightMode, switch | fade |
| `2MH0` | 吉豪智能吸顶灯 | 9638 | 112 | brightness, cct, lightMode, switch | auxLight, auxSwitch, fade, mainLight |
| `2MIC` | 松下智能除湿机 | F-AYW50TC | 09B | humidity, mode, pm25, switch | PromptSwitch, anionSwitch, elapsedTimeMode1, faultDetection, filterElement1, filterElement2, gear, tvoc, wind |
| `2MKE` | ELECTA智能取暖器 | ELW399 | 06A | childLockSwitch, mode, switch, temperature | Time, faultDetection, gear |
| `2MMH` | 空气净化器KJ300G-M2 | KJ300G-M2 | 013 | fan, mode, switch, temperature | AirQuality, PM25Value, UVselect, anionSwitch, filtervalue, humility, screenSwitch |
| `2MN7` | 霍尼韦尔智能台灯X5 | HWT-05A01 | 046 | brightness, colourMode, lightMode, switch | lightAdaption, lightFormula, lightforMode, lock, longTimeAlarm, nightAwake, seatSensor, useTime, wakeUpMorning |
| `2MTH` | 达伦智能台灯3i(双控版) |  DL-01W Pro | 046 | brightness, colourMode, lightMode, switch | backlight, currentTime, fadeTime, indicator, lightStatus, mainSwitch, nightWakeup, toggleSwitch |
| `2MWA` | 友邦浴霸X7 | X7 | 035 | action, brightness, lightSwitch, temperature | aircleanSwitch, sceneMode, swingSwitch, ventilateSwitch, warmWindMode, windSwitch |
| `2MXV` | Dual智能料理微波炉DIK02-HW | DIK02-HW | 023 | action, childLockSwitch, status, temperature | addDelay, appointment, cook, doorOpen, fire |
| `2N2U` | 方太油烟机CXW-358-01-X20.i | CXW-358-01-X20.i | 021 | lightSwitch, mode, status, switch | Ambientlight, LockScreen, gear |
| `2N2V` | 慧曼流光系列洗碗机B1max-4 | HTD-B1max-4 | 078 | action, mode, status, switch | appointment, curTemp, doorOpen, errorTip, light, modeFeature, remainTime, rinse, salt |
| `2N4A` | 云鲸智能拖扫一体机器人J4 | YJCC015 | 031 | action, battery, mode, status | commonFilterElement1, commonFilterElement2, commonFilterElement3, commonFilterElement4, faultDetection, getMap, narwalCmd, reqToken, revokeDeviceAuth, robotBaseStatus, robotWorkingStatus |
| `2N8V` | 霍尼韦尔智能护眼吸顶灯U7 60W | HWX-06B | 112 | brightness, cct, lightMode, switch | auxBrightness, auxBrtSwitch, lightFormulaArray, mainBrightness, mainBrtSwitch, nightMode, nightModeSwitch, preLightFormulaArray, preview, previewStatus, relBrightness, relCct, sleepMode, stateHold, wakeupMorning |
| `2NA1` | 小适智能剃须刀Ai501 | Ai501 | 170 | battery, mode, motor, status | charge, deviceVersion, hibernate, knifereset, lock, state, unusual |
| `2NBK` | A.O.史密斯热泵热水器HPA-DAH系列 | HPA-D2.0AH | 125 | mode, status, switch, temperature | AES, PumpCircle, Timer1, Timer2, faultDetection, instantHeatSwitch |
| `2NBL` | A.O.史密斯热泵热水器HPA-EZH系列 | HPA-80E1.5ZH | 125 | mode, status, switch, temperature | AES, TimerCircle, TimerHeat, faultDetection, instantHeatSwitch, zeroColdSwitch |
| `2NDD` | meipont美邦燃气热水器 | JSW32-16M5 | 124 | mode, status, switch, temperature | faultDetection, flameStatus, priority, targetWater |
| `2NF9` | 达伦智能台灯T1 |  DL-28WS | 046 | brightness, colourMode, lightMode, switch | childLock, currentTime, delayOff, directlyConnected, eyeRemind, eyeSuggestion, lightStatus, mainSwitch, runStactics, wakeUp |
| `2NHI` | 佳普乐致瑞智能厨房凉霸 | CP1ZR-01G | 029 | lightSwitch, status, switch, temperature | DevAction, circulationTime, horizSweep, initial, onOffBeep, userMode, water, windDirection, windTime |
| `2NIW` | 霍尼韦尔智能护眼落地灯U7 | HWL-02R01 | 10F | brightness, cct, lightMode, switch | auxBrightness, currentTime, lightAdaption, lightFormula, lightforMode, lock, longTimeAlarm, mainBrightness, nightAwake, preview, prompt, rhythms, seatSensor, useTime, wakeUpMorning |
| `2NOM` | 森森智能鱼缸控制器 | AQ-600 | 1A7 | lightSwitch, switch1, switch2, switch3 | commonFaultDetection, phMonitor, switch4, waterTemp |
| `2NRH` | 早鱼热敷腰带 | JY-008 | 17D | alarm, battery, mode, switch | countDown, heat, hot, shock |
| `2NRV` | 爱华仕智能音浪包 | OEB5103 | 13C | battery, lightMode, lightSwitch, mode | audioplayer, lightGear, lightSceneMode, loseSwitch, sceneMode, speaker |
| `2NU5` | 极米神灯 Sunlight | XN03B | 098 | brightness, cct, lightSwitch, switch | FOCUS, FOCUSLEFT, FOCUSRIGHT, ProjectorSwitch, RESTART, controlMode, focusing, home, keystonemanual, light, menu, relBrightness, rest, return, setting, systemMode, volSwitch, volume |
| `2NX2` | 智能色温吸顶灯 | XD-396 | 112 | brightness, cct, lightMode, switch | ChangeTime, Togglecct, cleverSwitch, commonMemorySwitch |
| `2NXM` | MEIPONT中央空调(WP) | MPT-36F1DCWP | 2FA | fan, mode, switch, temperature | commonFaultDetection, sceneMode, switchPTC, switchScreen |
| `2NZT` | 松下高级智能除菌加湿器 | FE-KFY16C | 052 | childLockSwitch, humidity, mode, switch | UVSwitch, devStatus, elapsedTimeMode, faultDetection, filterElement1, filterElement2, gear, lightSet, nanoeX |
| `2NZZ` | Hitick高速智能剃须刀7系 | Ai701 | 170 | battery, mode, motor, status | charge, clean, cleaningCompartment, deviceVersion, drip, hibernate, knifereset, lock, state, unusual |
| `2O1M` | 霍尼韦尔智能护眼吸顶灯U7 120W | HWX-06BPro | 112 | brightness, cct, lightMode, switch | auxBrightness, auxBrtSwitch, lightFormulaArray, mainBrightness, mainBrtSwitch, nightMode, nightModeSwitch, preLightFormulaArray, preview, previewStatus, relBrightness, relCct, sleepMode, stateHold, wakeupMorning |
| `2O2O` | 水母云智能磁吸轨道灯T1 | T1-FG600 | 221 | brightness, cct, lightMode, switch | fade |
| `2O6R` | 亚都加湿器SZM1100-V12(Hi) | SZM1100-V12(Hi) | 052 | childLockSwitch, humidity, switch, temperature | anion, clean, dried, faultDetection, gear, heat, lamp, level, state, timing, uv |
| `2O8R` | 佳文智能调光调色灯 | DLHC-HW088 | 21D | brightness, cct, lightMode, switch | fadeTime |
| `2O9M` | eachone一起玩 智能立式护眼学习灯 | HF-HM-DLD-001 | 046 | brightness, cct, lightMode, switch | — |
| `2O9P` | 云鲸智能扫拖一体机器人J5 | YJCC020 | 031 | action, battery, mode, status | availableZones, commonFilterElement1, commonFilterElement2, commonFilterElement3, commonFilterElement4, faultDetection, gear, getMap, narwalCmd, narwalReport, reqToken, revokeDeviceAuth, robotBaseStatus, robotWorkingStatus, zoneManagement |
| `2OAM` | eachone一起玩 智能石墨烯取暖器 | HF-HM-QNQ-001 | 06A | childLockSwitch, mode, switch, temperature | countdown, humidifyMode, humidifySwitch, swing, timeremaining |
| `2OE7` | 松下智能筒射灯 | HG9S352SQT | 111 | brightness, cct, lightMode, switch | donotDisturb, nightWakeup, progressSwitch |
| `2OE8` | 松下智能明装筒射灯 | HGXS351DQT | 111 | brightness, cct, lightMode, switch | donotDisturb, nightWakeup, progressSwitch |
| `2OE9` | 松下智能灯带控制装置 | LGC90822520QT | 118 | brightness, cct, lightMode, switch | donotDisturb, nightWakeup, progressSwitch |
| `2OEK` | 松下高级智能除菌加湿器 FE-16C4JD | FE-16C4JD | 052 | childLockSwitch, humidity, mode, switch | UVSwitch, devStatus, elapsedTimeMode, faultDetection, filterElement1, filterElement2, gear, lightSet, nanoeX |
| `2OH0` | 亚都加湿器SZ750-TJK800(Hi)Pro | SZ750-TJK800(Hi)Pro | 052 | childLockSwitch, humidity, switch, temperature | anion, dried, faultDetection, gear, lamp, level, state, timing, uv |
| `2OIB` | 小青芒千分比深度调光线性灯 | HC-DDD-002 | 118 | brightness, cct, lightMode, switch | Ontime, countdown, memoryswitch, offtime |
| `2OQ1` | 慧曼流光洗碗机 | HTD-B2 Plus-4 | 078 | action, mode, status, switch | appointment, curTemp, doorOpen, errorTip, light, modeFeature, remainTime, rinse, salt |
| `2OQ2` | 慧曼溢彩洗碗机 | HTD-I3 Pro | 078 | action, mode, status, switch | appointment, curTemp, doorOpen, errorTip, light, modeFeature, remainTime, rinse, salt |
| `2OR1` | 科技热敷带T3 | WZT3V401 | 17D | alarm, battery, mode, switch | BLEstatus, HotCompress, TemperatureGears, countdown, heat, massage, shutdown |
| `2OR6` | 创维酷开空调 | KFRd-35GW | 012 | fan, mode, switch, temperature | calmSpellSwitch, sceneMode, sterilization, switchPTC, switchScreen |
| `2OS3` | 水母云智能磁吸轨道灯T2 | T1-ZD220-12 | 221 | brightness, cct, lightMode, switch | fade |
| `2OS6` | 水母云智能磁吸轨道灯T3 | T1-SD45 | 221 | brightness, cct, lightMode, switch | fade |
| `2OT9` | 佳普乐致臻智能浴霸 | BH1ZZ-01N | 035 | action, lightSwitch, status, temperature | CirculationTime, UserMode, WarmWindTime, WindTime, commonExecution1, drySwitch, nightLightSwitch, odorsensingSwitch, ventilateSwitch, warmWindMode, windSwitch |
| `2OTA` | PGG腰部按摩仪W7 | W7 | 0CA | battery, mode, status, switch | fault, hot, pulse, remainConnect, remainTime, vibrationIntensity, vibrationIntensityOff, vibrationModeOff |
| `2OW9` | MEIPONT飞凡智能挂机空调S10(Pro) | MAC36V1S10HR(Pro) | 012 | fan, mode, switch, temperature | PtcHeat, commonFaultDetection, light, sceneMode |
| `2OWF` | eachone一起玩 智能吸顶灯 | HF-HM-XDD-004 | 112 | brightness, cct, lightMode, switch | commonMemorySwitch1, nightWakeup, progressTurnOff, progressTurnOn |
| `2OY5` | 慧曼天女洗碗机 | HTD-B2-700P | 078 | action, mode, status, switch | appointment, curTemp, doorOpen, errorTip, light, modeFeature, remainTime, rinse, salt |
| `2OYH` | 吉豪晶漾智能灯具 | 9642/950 144W | 112 | brightness, cct, lightMode, switch | progressSwitch |
| `2OYZ` | MEIPONT赫界智能挂机空调 | MAC36V1P70HR(Pro) | 012 | fan, mode, switch, temperature | calmSpellSwitch, commonFaultDetection, electric, light, sceneMode, switchPTC |
| `2P13` | 达伦智能台灯5i(双控版) |     DL-01W Pro | 046 | brightness, colourMode, lightMode, switch | auxBrightness, auxSwitch, delayTurnoff, directlyConnected, foldAngles, indicator, mainSwitch, nightWakeup, timeSync, toggleSwitch |
| `2P4A` | 佳普乐星辰恒温智控花洒 | SH2XC-01N | 300 | status, switch2, switch3, temperature | coldWaterSwitch, waterOutletSwitch |
| `2P79` | 吉豪智能灯具 | 9567/550 70W | 112 | brightness, cct, lightMode, switch | auxBrightness, auxSwitch, cctReverse, mainSwitch, progressSwitch |
| `2PEL` | JYMC智能双色灯HM1 | HM1 | 112 | brightness, cct, lightMode, switch | auxBrightness, auxSwitch, commonMemorySwitch, commonMode, donotDisturb, mainSwitch, progressSwitch |
| `2PFV` | 小适智能剃须刀T3S | Ai301 | 170 | battery, mode, status, switch | bladeReset, bladeStatus, travelLock |
| `2PI3` | 吉豪智能筒射灯 | JH-M604-10W | 111 | brightness, cct, lightMode, switch | progressSwitch |
| `2PI8` | DL深度调光情景灯Plus | DL032-F03A | 21D | brightness, cct, lightMode, switch | donotDisturb, nightWakeup, progressSwitch, progressTurnOff, progressTurnOn, toggleSwitch |
| `2PIE` | DL深度调光情景灯 | DL040-F03 | 112 | brightness, cct, lightMode, switch | donotDisturb, nightWakeup, progressSwitch, progressTurnOff, progressTurnOn, toggleSwitch |
| `2PIR` | 吉豪一帘幽梦智能灯具 | 9135/400Y 79W | 112 | brightness, cct, lightMode, switch | progressSwitch |
| `2PIS` | 吉豪星辰智能灯具 | 9440/500 95W | 112 | brightness, cct, lightMode, switch | progressSwitch |
| `2PQ3` | THINCO智能台灯 5Pro | DL-56WS | 046 | brightness, childLockSwitch, lightMode, switch | lightAdaptionSwitch, lightFormulaArray, longTimeAlarm, nightModeSet, preLightFormulaArray, preview, progressTurnOn, seatOffLightSet, seatOnLightSet, timeSync, usageRecord |
| `2Q0B` | 正尚4路WiFi开关 | ZS-HWTB-SM-41W | 064 | switch, switch1, switch2, switch3 | CleanPair, Pair, backlight, memorySwitch, mode1, mode2, mode3, mode4, switch4 |
| `2Q1M` | 正尚3路WiFi开关 | ZS-HWTB-SM-31W | 064 | switch, switch1, switch2, switch3 | CleanPair, Pair, backlight, memorySwitch, mode1, mode2, mode3 |
| `2Q23` | THINCO智能落地灯 | DL-65WF | 10F | brightness, childLockSwitch, lightMode, switch | auxBrightness, auxSwitch, intelligentDimming, lightAdaptionSwitch, longTimeAlarm, mainBrightness, mainSwitch, nightModeSet, progressTurnOn, remoteControlSearch, remoteControlStatus, remoteCtrlInfo, remoteCtrlMetering, remoteCtrlType, seatOffLightSet, seatOnLightSet, spectralData, strobeData, timeSync, usageRecord |
| `2Q41` | 吉豪西江月智能灯具 | 9135/500Y 112W | 112 | brightness, cct, lightMode, switch | progressSwitch |
| `2Q4G` | SORONTEK智能面板 | SR-S15 | 201 | switch, switch1, switch2, switch3 | switch4 |
| `2Q61` | 纽恩泰空气能热泵 | NE-C220BZ-BIIR4/U-T | 2FA | humidity, mode, switch, temperature | commonFaultDetection, coolWaterTemp, electric, heatWaterTemp, inletTemperature, outWaterTemp, sceneMode, targetTemp |
| `2Q8G` | 酷开空调KFR-35GWNAAA-N1 | KFR-35GWNAAA-N1 | 012 | fan, mode, switch, temperature | calmSpellSwitch, exAirSwitch, freshAirSwitch, keyToneSwitch, light, sceneMode, softWindSwitch, sterilization, switchPTC |
| `2Q9F` | 埠威充气泵搭电一体机 | N1 | 179 | battery, lightMode, mode, status | airPressure, commonFaultDetection |
| `2QBO` | 豪恩空气质量检测仪 | LH-335WF | 006 | battery, hcho, humidity, temperature | co2, commonFaultDetection, heat, indicator, moisture, screenMode, sleepMode |
| `2QEF` | 三诺智能语音开关 | SSP-YYK2-2C-AG | 349 | brightness, childLockSwitch, switch1, switch2 | autoScene, backlight, batchCmd, bluetooth, bt, button1, button2, capacity, changeDirection, clickedScene, commonFaultDetection, communication, connectDev, devList, deviceLabel, deviceType, discovery, group1, group10, group11, group12, group13, group14, group15, group16, group17, group18, group19, group2, group20, group21, group22, group23, group24, group25, group3, group4, group5, group6, group7, group8, group9, groupControl, groupManage, hiBeaconSync, homeBroadcast, homeGatewayCap, hwaccount, lightLevel, lightRing, localCommand, logEvent, logReport, manualScene, memorySwitch, microphone, mode1, mode2, msgRsp, nearbyWakeup, netReconnection, preWakeUp, quietMode, reboot, sceneManage, sceneOperation, smartspeaker, speaker, speakerAlarm, speakerIfttt, speakerState, switchMap, voiceAssist, voiceAssistDevInfo, wakeUp, wakeupVerifyMode |
| `2QF4` | 颁芙净肤浴电热水器H7 | E60-H7-33 | 027 | mode, status, switch, temperature | aiSwitch, autoPowerOffSwitch, commonFaultDetection, preTimeEnd, presetSwitch |
| `2QJQ` | RANTU ONE智能挂机空调 | KFRD-32GW/R7V1 | 012 | fan, mode, switch, temperature | commonFaultDetection, electric, sceneMode, switchPTC, switchScreen |
| `2QL7` | RANTU ONE智能挂机空调R7 | KFRD-35GW/R7V1 | 012 | fan, mode, switch, temperature | commonFaultDetection, electric, sceneMode, switchPTC, switchScreen |
| `2QL8` | RANTU ONE智能挂机空调M7 | KFRD-36GW/M7V1 | 012 | fan, mode, switch, temperature | commonFaultDetection, electric, sceneMode, switchPTC, switchScreen |
| `2QL9` | MEIPONT智能挂机空调T1 | MAC35V1THR(Max) | 012 | fan, mode, switch, temperature | commonFaultDetection, electric, sceneMode, switchPTC, switchScreen |
| `2QP8` | 朗润阳光灯 | C2500-A4M | 112 | brightness, cct, lightMode, switch | donotDisturb, progressSwitch |
| `2QQQ` | eachone一起玩  人体存在平板灯 | HF-HM-PBD-D1 | 112 | brightness, cct, lightMode, switch | checkTime, commonMemorySwitch, humanSensingStatus, inductionCondition, inductionSwitch, inductionTime, lightFormulaArray, nightWakeup, preLightFormulaArray, preview, progressSwitch, toggleSwitch |
| `2QR4` | eachone一起玩   智能吸顶灯 | HF-HM-XDD-011 | 112 | brightness, cct, lightMode, switch | commonMemorySwitch, nightWakeup, progressTurnOff, progressTurnOn |
| `2QR5` | eachone一起玩  智能吸顶灯 | HF-HM-XDD-013 | 112 | brightness, cct, lightMode, switch | commonMemorySwitch, nightWakeup, progressTurnOff, progressTurnOn |
| `2QR6` | 蜂鸟物联开关PRO-4 | BI-04 | 1FF | switch, switch1, switch2, switch3 | commonMemorySwitch, indicator, switch4 |
| `2QUX` | RANTU ONE智能挂机空调S10 | KFRD-35GW/V1S10 | 012 | fan, mode, switch, temperature | commonFaultDetection, electric, sceneMode, switchPTC, switchScreen |
| `2QUY` | RANTU ONE智能柜机空调 双出风 | KFRD-72LW/M7V1 | 2F9 | fan, mode, switch, temperature | commonFaultDetection, electric, sceneMode, switchPTC, switchScreen |
| `2QUZ` | RANTU ONE 智能柜机空调 圆柜 | KFRD-72LW/R7V1 | 2F9 | fan, mode, switch, temperature | commonFaultDetection, electric, sceneMode, switchPTC, switchScreen |
| `2QXY` | 鸿智烤箱 | HZ-KZ30 | 024 | action, lightSwitch, mode, status | commonFaultDetection, leftDoorStatus, leftRecipes, leftStatus, leftTemperature, leftTime, leftWorkTime, lefthotWindSwitch, rightDoorStatus, rightLeftTime, rightMode, rightRecipes, rightStatus, rightTemperature, rightWorkTime, righthotWindSwitch |
| `2QYA` | 达伦智能台灯3Max |  DL-33WS | 046 | brightness, cct, lightMode, switch | delayOff, eyeRemind, eyeSuggestion, lightFormulas, lightFormulas01, lightFormulas02, lightFormulas03, lightStatus, mainSwitch, nightLightSwitch, nightMode, runStactics |
| `2QYF` | 奥普浴霸F3-Pro-HW | F3-Pro-HW | 035 | action, fan, lightSwitch, status | autoWarmWindSwitch, automaticWarmWindSwitch, commonFaultDetection, deodorization, drySwitch, heat, indicator, leftTime, nightLightSwitch, sceneMode, ventilateGear, ventilateSwitch, windMode, windSwitch |
| `2QYO` | 智能多功能煲 | MF-3.5ERC001H | 062 | action, mode, status, temperature | commonFaultDetection, leftTime, preTimeEnd, preTimeStart, presetSwitch, realBladeStatus, recipes, setWorkTime, workTime |
| `2R3J` | eachone一起玩  智能吸顶灯B3 | HF-HM-XDD-032 | 112 | brightness, cct, lightMode, switch | commonMemorySwitch, inchingSwitch, nightWakeup, progressSwitch, progressTurnOff, progressTurnOn |
| `2R46` | 一起玩eachone  天翼光辅光吸顶灯 | HF-HM-XDD-096B | 112 | brightness, cct, lightMode, switch | auxBrightness, auxSwitch, commonMemorySwitch, inchingSwitch, mainSwitch, nightWakeup, progressSwitch, progressTurnOff, progressTurnOn |
| `2R63` | Hitick高速智能剃须刀7系Pro | Ai701pro | 170 | battery, mode, status, switch | bladeClean, bladeReset, bladeStatus, commonFaultDetection, record, travelLock |
| `2R69` | 格丽思多功能茶饮机T-818 | T-818A | 060 | mode, status, switch, temperature | commonFaultDetection, heatGear, keypressSoundSwitch, leftTime, setWorkTime, warmSwitch |
| `2R8X` | 立达信云上吊灯Pro | PLTD-YS03-L150-XB-HM | 21E | brightness, cct, lightMode, switch | commonFaultDetection, commonMemorySwitch, relBrightness |
| `2RAU` | 立达信智能护眼吸顶灯 光之骄子Pro 65W | LC5S-G1-D50HM | 112 | brightness, cct, lightMode, switch | auxBrightness, auxCct, auxSwitch, commonFaultDetection, commonMemorySwitch, donotDisturb, inductionSwitch, lightFormulaArray, localVoice, mainBrightness, mainCct, mainSwitch, nightModeSet, preview, progressTurnOff, progressTurnOn, relBrightness |
| `2RAV` | 立达信智能护眼吸顶灯 光之骄子Pro 85W | LC5S-G1-D59HM | 112 | brightness, cct, lightMode, switch | auxBrightness, auxCct, auxSwitch, commonFaultDetection, commonMemorySwitch, donotDisturb, inductionSwitch, lightFormulaArray, localVoice, mainBrightness, mainCct, mainSwitch, nightModeSet, preview, progressTurnOff, progressTurnOn, relBrightness |
| `2RD9` | 格丽思便捷烧水杯G-C400 | G-C400S1 | 06B | lightMode, status, switch, temperature | commonFaultDetection, hydrogenProduction, hydrogenProductionSwitch |
| `2RDK` | 一起玩eachone  全面屏雷达吸顶灯 | HF-HM-XDD-506 | 112 | brightness, cct, lightMode, switch | checkTime, commonMemorySwitch, humanSensingStatus, inchingSwitch, inductionCondition, inductionSwitch, inductionTime, lightFormulaArray, nightWakeup, preLightFormulaArray, preview, progressSwitch, progressTurnOff, progressTurnOn |
| `2REH` | 一起玩eachone   天翼光漫反光吸顶灯 | HF-HM-XDD-092B | 112 | brightness, cct, lightMode, switch | auxBrightness, auxSwitch, commonMemorySwitch, inchingSwitch, mainSwitch, nightWakeup, progressSwitch, progressTurnOff, progressTurnOn |
| `2RF1` | 一起玩eachone   全面屏无边框吸顶灯 | HF-HM-XDD-502 | 112 | brightness, cct, lightMode, switch | commonMemorySwitch, inchingSwitch, lightFormulaArray, nightWakeup, preLightFormulaArray, preview, progressSwitch, progressTurnOff, progressTurnOn |
| `2RFB` | 佳普乐沁泽智联龙头 | ST1QZ-01N | 310 | mode, status, switch, temperature | coldWaterSwitch, inductionSwitch, preSchedulingDuration, waterTime |
| `2RFM` | 朗泽吸顶灯 | C2500-CM-TW2 | 112 | brightness, cct, lightMode, switch | donotDisturb, progressSwitch |
| `2RFN` | 朗润吸顶灯 | C2050-AM-TW2 | 112 | brightness, cct, lightMode, switch | donotDisturb, progressSwitch |
| `2RFO` | 朗明吸顶灯 | C3500-AS-TW2 | 112 | brightness, cct, lightMode, switch | donotDisturb, progressSwitch |
| `2RFQ` | HWHL华伟宏亮智能吸顶灯 | HWHL18MT | 112 | brightness, cct, lightMode, switch | auxBrightness, auxSwitch, progressSwitch |
| `2RGT` | 十亿智联智能橱柜灯 | HM1002 | 222 | brightness, colour, colourMode, switch | donotDisturb |
| `2RGV` | 十亿智联橱柜灯 | HM1003 | 222 | brightness, colour, colourMode, switch | donotDisturb |
| `2RH2` | 灵馨橱柜灯Lx-1 | Lx-1 | 222 | brightness, cct, lightMode, switch | donotDisturb |
| `2RH3` | 灵馨橱柜灯Lx-2 | Lx-2 | 222 | brightness, cct, lightMode, switch | donotDisturb |
| `2RH4` | 灵馨吸顶灯Lx-3 | Lx-3 | 112 | brightness, cct, lightMode, switch | donotDisturb |
| `2RHC` | 一起玩eachone 自然光吸顶灯Max版 | HF-HM-XDD-042B | 112 | brightness, cct, lightMode, switch | commonMemorySwitch, inchingSwitch, nightWakeup, progressSwitch, progressTurnOff, progressTurnOn |
| `2RI2` | 百吉兴吸顶灯BJX-1 | BJX-1 | 112 | brightness, cct, lightMode, switch | donotDisturb |
| `2RI4` | 百吉兴吸顶灯BJX-2 | BJX-2 | 112 | brightness, colour, colourMode, switch | donotDisturb |
| `2RIJ` | 百吉兴橱柜灯BJX-3 | BJX-3 | 222 | brightness, cct, lightMode, switch | donotDisturb |
| `2RIT` | 飞利浦空调速铂 | FAC35V1EbSYHR(HM) | 012 | fan, mode, switch, temperature | ECOswitch, commonFaultDetection, favoriteModeSwitch, light, mildewProofswitch, sterilization, switchPTC, switchScreen |
| `2RJY` | 禅念智能双色吸吊灯 | 9619/600Y | 21E | brightness, cct, colourMode, switch | auxSwitch, progressSwitch |
| `2RLX` | HWHL华伟宏亮智控星闪灯 | HWHL19MT | 112 | brightness, cct, lightMode, switch | auxBrightness, auxSwitch, progressSwitch |
| `2RN8` | lipro护眼吸顶灯E2 | T23X1-W0603050-HM | 112 | brightness, cct, lightMode, switch | commonMemorySwitch, progressSwitch |
| `2RNC` | 西顿照明T5无线RGBCW灯带照明驱动 | SWBH-QY-240W-5 | 226 | brightness, cct, colour, switch | commonFaultDetection, commonMemorySwitch, fadeTimeSetting, indicator, lightCurveSetting, relBrightness |
| `2RPF` | 索菲亚智能双色温灯H1 | SJDWH2AA | 222 | brightness, cct, lightMode, switch | commonMemorySwitch, inchingSwitch, progressSwitch, remoteCtrPair |
| `2RQ0` | 艺云 艺术画屏 | 32ALF7003 | 34D | action, brightness, status, switch | autoBrightness, autoPlay, backup, commonFaultDetection, dataManagement, mute, screenMode, undisturbMode, volume |
| `2RQO` | 立达信智能护眼吸顶灯 光之骄子标准款 | LC3S-G1-D45HM | 112 | brightness, cct, lightMode, switch | auxBrightness, auxCct, auxSwitch, commonFaultDetection, commonMemorySwitch, inchingSwitch, lightFormulaArray, localVoice, mainBrightness, mainCct, mainSwitch, nightModeSet, preview, progressTurnOff, progressTurnOn, relBrightness |
| `2RRC` | MEIPONT智能柜机空调 霖界 | KFRD-120LW/K1V1 | 2F9 | fan, mode, switch, temperature | commonFaultDetection, electric, sceneMode, switchPTC, switchScreen |
| `2RVW` | 鸿蒙智选 云鲸JX扫地机器人 | YJCC034 | 031 | action, battery, mode, status | availableZones, commonFilterElement1, commonFilterElement2, commonFilterElement3, commonFilterElement4, commonFilterElement5, commonFilterElement6, commonFilterElement7, faultDetection, gear, getMap, narwalCmd, narwalReport, reqToken, revokeDeviceAuth, robotBaseStatus, robotWorkingStatus, zoneManagement |
| `2RVX` | 鸿蒙智选 云鲸逍遥003扫地机器人 | YJCC036 | 031 | action, battery, mode, status | availableZones, commonFilterElement1, commonFilterElement2, commonFilterElement3, commonFilterElement4, faultDetection, gear, getMap, narwalCmd, narwalReport, reqToken, revokeDeviceAuth, robotBaseStatus, robotWorkingStatus, zoneManagement |
| `2RYD` | 创明左右分控智能窗帘 静音大师 | H3 Pro | 01C | action, leftAction, mode, opener | changeDirection, commonFaultDetection, favorate, followMode, handpullMode, handpullSwitch, indicator, leftOpener, manualspeedControl, remoteControl, reverse, rightAction, rightOpener, routeRuntime, speed, stroke, sync, syncSwitch |
| `2RYO` | 力博得智能冲牙器 博享 | LBE-0077 | 175 | battery, mode, status, switch | applicatorTime, cleaningRecord, commonFaultDetection, filterElement, setWorkTime, voiceGuidance, workGuidance |
| `2SEY` | 三菱电机空调壁挂机AC系列 | MSZ-AC12VFL | 012 | fan, mode, switch, temperature | capabilityset, commonFaultDetection |
| `2SKV` | 捷德韦尔智能灯 | IC110.24BB.001 | 222 | brightness, cct, lightMode, switch | auxSwitch, commonMemorySwitch, progressSwitch |
| `2SMN` | 飞利浦空调E-M9 | FAC35V1Em9YHR | 012 | fan, mode, switch, temperature | ECOswitch, commonFaultDetection, favoriteModeSwitch, light, mildewProofswitch, sterilization, switchPTC, switchScreen |
| `2SQL` | 诺克智能灯 | IC110.24BB.002 | 21E | brightness, cct, lightMode, switch | auxSwitch, commonMemorySwitch, progressSwitch |
| `9MTJ` | 智控夜灯 | haTest1 | 21F | brightness, cct, status, switch | — |
| `9MTR` | 智控水壶 | haTest5 | 09A | mode, status, switch, temperature | commonFaultDetection |
| `9MXO` | 智控空调 | test20 | 012 | fan, mode, switch, temperature | — |
| `9MZK` | 智控洗衣机 | haTest32 | 015 | action, mode, status, switch | leftTime |
| `9MZO` | 智控养生壶 | haTest34 | 060 | mode, status, switch, temperature | warmSwitch |
| `9MZQ` | 智控咖啡机 | haTest35 | 0B9 | action, mode, status, switch | — |
| `9MZV` | 智控烟机 | haTest39 | 021 | lightSwitch, mode, status, switch | gear |
| `A002` | 美的智能空调系列 | Midea Air Conditioner | 012 | fan, mode, switch, temperature | faultDetection |
| `A06W` | 博世洗衣机 | WAWH26600W | 015 | action, mode, status, switch | doorLockSwitch |
| `A06X` | 博世烘干机 | WAWH26600W | 015 | action, mode, status, switch | doorLockSwitch, dryMode |
| `A07D` | 智能空调 | TCL Air Conditioner | 012 | fan, mode, switch, temperature | faultDetection |
| `A0CO` | 美的波轮洗衣机 | COLMO12 | 015 | action, mode, status, switch | leftTime |
| `A0CP` | 格力智能空调 | 111a | 012 | fan, mode, switch, temperature | — |
| `A0CQ` | 美的滚筒洗衣机 | colmo | 015 | action, mode, status, switch | leftTime |
| `A0E0` | 海尔智能空调 | HarmonyOS | 012 | fan, mode, switch, temperature | — |
| `A0MJ` | 智能3D气流风管式温湿平衡型3D气流风管式温湿平衡型 | 1.0 | 012 | fan, mode, switch, temperature | choiceOfColdAndHot, commonFaultDetection, fan1, fan2 |
| `A0MK` | 超薄风管式温湿平衡型 | 1.0 | 012 | fan, mode, switch, temperature | choiceOfColdAndHot, commonFaultDetection |
| `A0ML` | 衣帽间防潮嵌入式标准式 | 1.0 | 012 | fan, mode, switch, temperature | choiceOfColdAndHot, commonFaultDetection, fan1 |
| `A0MM` | 智能3D气流风管式新风净化型3D气流风管式新风净化型 | 1.0 | 012 | fan, mode, switch, temperature | choiceOfColdAndHot, commonFaultDetection, fan1, fan2, fresh3D |
| `A0MN` | 超薄风管式新风净化型 | 1.0 | 012 | fan, mode, switch, temperature | choiceOfColdAndHot, commonFaultDetection, fresh3D |
| `A0MO` | 智能3D气流风管式PM2.5净化型3D气流风管式PM2.5净化型 | 1.0 | 012 | fan, mode, switch, temperature | choiceOfColdAndHot, commonFaultDetection, fan1, fan2 |
| `A0MP` | 超薄风管式PM2.5净化型超薄风管式标准型 | 1.0 | 012 | fan, mode, switch, temperature | choiceOfColdAndHot, commonFaultDetection |
| `A0MQ` | 智能3D气流风管式标准型3D气流风管式标准型 | 1.0 | 012 | fan, mode, switch, temperature | choiceOfColdAndHot, commonFaultDetection, fan1 |
| `A0MR` | 超薄风管式大容量型 | 1.0 | 012 | fan, mode, switch, temperature | choiceOfColdAndHot, commonFaultDetection |
| `A0MS` | 卫浴用嵌入式标准型 | 1.0 | 012 | fan, mode, switch, temperature | choiceOfColdAndHot, commonFaultDetection, fan1, ventilation |
| `A0MT` | 高耐久厨房用嵌入式标准型 | 1.0 | 012 | fan, mode, switch, temperature | choiceOfColdAndHot, commonFaultDetection, fan1 |
| `A0MU` | 客厅向 | 1.0 | 012 | fan, mode, switch, temperature | choiceOfColdAndHot, commonFaultDetection, fan1 |
| `A0MV` | 客厅向高级面板 | 1.0 | 012 | fan, mode, switch, temperature | choiceOfColdAndHot, commonFaultDetection, fan1, fan2 |
| `A0N7` | 智汇云RGB模块 | light001 | 01B | brightness, colour, colourMode, switch | — |
| `A0NQ` | 奥克斯空调 | KFR-26GW | 012 | fan, mode, switch, temperature | eco, healthy, screen, sleep, supportHeat |
| `A0NW` | 智能四通道开关 | Smart wall switch | 005 | switch, switch1, switch2, switch3 | switch4 |
| `A0OK` | 智能三通道插座 | Smart socket | 01E | switch, switch1, switch2, switch3 | — |
| `A0OM` | 智能四通道插座 |  Smart socket | 01E | switch, switch1, switch2, switch3 | switch4 |
| `A0OR` | 智能三通道开关 | Smart wall switch | 005 | switch, switch1, switch2, switch3 | — |
| `A0OX` | 冷暖双色调光灯 |  Smart light | 01B | brightness, cct, colourMode, switch | — |
| `A0PT` | 国美电暖器 | GM-22T11YL | 06A | childLockSwitch, mode, switch, temperature | Auto, Display, gear |
| `A0RD` | 单向气流嵌入式 | 1.0 | 012 | fan, mode, switch, temperature | choiceOfColdAndHot, commonFaultDetection, fan1 |
| `A0RE` | 智能感知环绕气流嵌入式 | 1.0 | 012 | fan, mode, switch, temperature | choiceOfColdAndHot, commonFaultDetection, fan1 |
| `A0RG` | 环绕气流嵌入式 | 1.0 | 012 | fan, mode, switch, temperature | choiceOfColdAndHot, commonFaultDetection, fan1 |
| `A0RH` | 中静压风管式 | 1.0 | 012 | fan, mode, switch, temperature | choiceOfColdAndHot, commonFaultDetection |
| `A0RI` | 自由静压风管式 | 1.0 | 012 | fan, mode, switch, temperature | choiceOfColdAndHot, commonFaultDetection |
| `A0RJ` | 内藏落地式 | 1.0 | 012 | fan, mode, switch, temperature | choiceOfColdAndHot, commonFaultDetection |
| `A0RK` | 明装落地式 | 1.0 | 012 | fan, mode, switch, temperature | choiceOfColdAndHot, commonFaultDetection |
| `A0RL` | 挂壁式 | 1.0 | 012 | fan, mode, switch, temperature | choiceOfColdAndHot, commonFaultDetection, fan1 |
| `A0TG` | 海信日立空调 | IEZ | 012 | fan, mode, switch, temperature | faultDetection, modeAuto, windAuto |
| `A0TN` | 奥克斯空调 | KFR-72LW | 012 | fan, mode, switch, temperature | eco, healthy, screen, sleep, supportHeat |
| `A0UC` | 霍尼韦尔智能控制空调 | HWairCondition01 | 012 | fan, mode, switch, temperature | — |
| `A0VT` | COLMO净水机 | CWRC700-A63 | 02D | mode, status, switch, temperature | commonFaultDetection, commonFilterElement1, filterElement1, filterElement2, filterElement3, rinseMode, water, waterSpeed |
| `A0YZ` | 西门子开关 | 5TA71132NC | 005 | switch, switch1, switch2, switch3 | — |
| `A0Z6` | 西门子空调1 | 5UH73311NC | 012 | fan, mode, switch, temperature | SleepMode, childLock, deviceName, energy, faultDetection |
| `A12Z` | COLMO干衣机 | CLHS10E | 0D7 | action, mode, status, switch | faultDetection, leftTime, preTimeEnd, presetSwitch |
| `A13C` | 方太蒸箱SCD48-M1A.i | SCD48-M1A.i | 022 | mode, status, switch, temperature | AppointmentFlag, WaterShortage, WorkMode, gateState, lackWater, leftTime |
| `A1AE` | 取暖器HFW22ESA | HFW22ESA | 06A | childLockSwitch, mode, switch, temperature | buttonBeepSwitch, faultDetection, gear, humidifySwitch, preTimeOff, preTimeOn, screenOffSwitch, swingSwitch, temperatureControlSwitch |
| `A1AF` | 美的净化器 | KJ700G-H32Y | 013 | childLockSwitch, mode, pm25, switch | closeTime, hosting, openTime |
| `A1B3` | COLMO滚筒洗衣机 | CLGS10E | 015 | action, mode, status, switch | leftTime, preTimeEnd, presetSwitch |
| `A1B4` | COLMO洗干一体机 | CLDS10E | 015 | action, mode, status, switch | leftTime, preTimeEnd, presetSwitch |
| `A1CM` | 美的洗物机 | XH07 | 173 | action, mode, status, switch | faultDetection |
| `A1F9` | 万和燃气热水器LS3 | JSLQ27-WLS3W16 | 027 | mode, status, switch, temperature | faultDetection, zerocold |
| `A1I8` | 万和燃气热水器YL5 | JSQ27-14YL5-HOS | 027 | mode, status, switch, temperature | faultDetection, temRange, zerocold |
| `A1KM` | 万和燃气热水器LS3 | JSLQ21-WLS3W13 | 027 | mode, status, switch, temperature | faultDetection, zerocold |
| `A1OA` | 烤箱KQD62F-M1A.i | KQD62F-M1A.i | 024 | lightSwitch, status, switch, temperature | compoundInstruction, leftTime, presetSwitch, workTime |
| `A1PF` | 小天鹅洗烘一体机 | TD100MS9ILZ | 015 | action, mode, status, switch | leftTime, preTimeEnd, presetSwitch |
| `A1PG` | 小天鹅滚筒洗衣机 | TG100MS9ILZ | 015 | action, mode, status, switch | leftTime, preTimeEnd, presetSwitch |
| `A1PH` | 小天鹅洗烘一体机 | TD100Q81Y | 015 | action, mode, status, switch | leftTime, preTimeEnd, presetSwitch |
| `A1PI` | 小天鹅滚筒洗衣机 | TG100Q81Y | 015 | action, mode, status, switch | faultDetection, leftTime, preTimeEnd, presetSwitch, workTime |
| `A1PK` | 美的滚筒洗衣机 | MG100T10WDQCY | 015 | action, mode, status, switch | leftTime, preTimeEnd, presetSwitch |
| `A1PL` | 美的洗烘一体机 | MD100T10WDQCY | 015 | action, mode, status, switch | leftTime, preTimeEnd, presetSwitch |
| `A1RH` | COLMO抽油烟机CXKCP924W-Z6 | CXKCP924W-Z6 | 021 | lightSwitch, mode, status, switch | faultDetection, gear |
| `A1S7` | 海尔智能洗衣机 | XQG100-BM14266LU1 | 015 | action, mode, status, switch | faultDetection, leftTime, preTimeEnd, returnStandby |
| `A1VR` | 小天鹅 TH100-H81WY 10公斤 热泵干衣机 | TH100-H81WY | 0D7 | action, mode, status, switch | faultDetection, heatTime, leftTime, preTimeEnd, presetSwitch |
| `A2AS` | 美的 MH100-H10WY 10公斤 热泵干衣机 | MH100-H10WY | 0D7 | action, mode, status, switch | faultDetection, leftTime, preTimeEnd, presetSwitch |
| `A2AT` | 小天鹅 TH100-H9WZ 10公斤 热泵干衣机 | TH100-H9WZ | 0D7 | action, mode, status, switch | faultDetection, leftTime, preTimeEnd, presetSwitch |
| `A2B3` | COLMO CLGS10CE-Z 10公斤 滚筒洗衣机 | CLGS10CE-Z | 015 | action, mode, status, switch | faultDetection, leftTime, preTimeEnd, presetSwitch, workTime |
| `A2B4` | COLMO CLHS10CE-Z 10公斤 热泵干衣机 | CLHS10CE-Z | 0D7 | action, mode, status, switch | faultDetection, heatTime, leftTime, preTimeEnd, presetSwitch |
| `A2EN` | COLMO抽油烟机CXSP927W-SS8 | CXSP927W-SS8 | 021 | lightSwitch, mode, status, switch | faultDetection, gear |
| `A2FY` | 小天鹅 10公斤 热泵干衣机 | TH100QH19WZ | 0D7 | action, mode, status, switch | faultDetection, heatTime, leftTime, preTimeEnd, presetSwitch |
| `A2GD` | 万和电热水器Q9D1 | E60-Q9D1-30 | 027 | mode, status, switch, temperature | Book1, Book1Time, Book2, Book2Time, Book3, Book3Time, ModeFlag, SetPower, SetTemp, WaterFresh, WaterRemainTime, WaterTankTemp, autopoweroff, commonFaultDetection, gears |
| `A2GQ` | 西门子干衣机 | WT47U6H80W | 0D7 | action, mode, status, switch | faultDetection, leftTime |
| `A2GV` | 西门子洗干一体机 | XQG100-WD14U5X8HW | 015 | action, childLockSwitch, mode, status | faultDetection, lefttime1 |
| `A2IE` | CXW-200-J6052H吸油烟机 | CXW-200-J6052H | 021 | lightSwitch, mode, status, switch | commonFaultDetection, delayedShutdown, gear, gearStat, lockScreen, lockStat, lockSwtich |
| `A2IX` | 美的电磁炉C22-506 | C22-506 | 079 | mode, status, switch, temperature | heatGear |
| `A2IZ` | 美的空气炸锅MF-KZS3503XM | MF-KZS3503XM | 063 | action, mode, status, temperature | leftTime, pauseTime, targetTemp, workTime |
| `A2J4` | 美的暖风机HFX22AR1 | HFX22AR1 | 06A | childLockSwitch, mode, switch, temperature | faultDetection, preTimeOff, preTimeOn, screenOffSwitch, swingSwitch, tempCtrlSwitch |
| `A2JM` | 智能三通道机械开关 | Smart Switch-3ch | 005 | switch, switch1, switch2, switch3 | — |
| `A2NJ` | 小天鹅 10公斤 洗干一体机 | TD100MS19ILZ | 015 | action, mode, status, switch | leftTime, preTimeEnd, presetSwitch |
| `A2NL` | 小天鹅 10公斤 滚筒洗衣机 | TG100MS19ILZ | 015 | action, mode, status, switch | leftTime, preTimeEnd, presetSwitch |
| `A2NY` | 万和电热水器Q9D1 | E80-Q9D1-30 | 027 | mode, status, switch, temperature | Book1, Book1Time, Book2, Book2Time, Book3, Book3Time, ModeFlag, SetPower, SetTemp, WaterFresh, WaterRemainTime, WaterTankTemp, autopoweroff, commonFaultDetection, gears |
| `A2OA` | CXW-200-E6090H吸油烟机 | CXW-200-E6090H | 021 | lightSwitch, mode, status, switch | commonFaultDetection, delayedShutdown, gear, gearStat, lockScreen, lockStat, lockSwitch, lockSwtich, wacaStat |
| `A2PO` | ZC3i燃气热水器 | JSQ24-13ZC3i | 027 | mode, status, switch, temperature | StronRichWater, faultDetection, funcswit2, highTempUnlock, iwaterTmp, totalGas, totalWater |
| `A2Q2` | 万和电热水器X2 | E60-X2-HOS | 027 | mode, status, switch, temperature | SetPower, SetTemp, appointmenttime, faultDetection, hotwater, poweroff |
| `A2TZ` | 智汇云智能水壶 | ZHY-YSH001 | 09A | mode, status, switch, temperature | boil, color, currentTemp, heatGear, heatMode, leftTime, power, preTimeStart, presetSwitch, warmDuration, warmSwitch, water |
| `A2U1` | TE5i燃气热水器 | JSQ30-16TE5i | 124 | mode, status, switch, temperature | faultDetection, funcswit2, gasTotal, highTempUnlock, iwaterTmp, waterTotal |
| `A2U2` | TW7i燃气热水器 | JSQ30-16TW7i | 124 | mode, status, switch, temperature | Selfclean, cycle, faultDetection, gasTotal, heating, highTempUnlock, iwaterTmp, waterTap, waterTotal, waterfallBath |
| `A2UY` | ZH8i燃气热水器 | JSQ30-16ZH8i | 124 | mode, status, switch, temperature | cycle, faultDetection, gasTotal, heating, highTempUnlock, iwaterTmp, waterTotal, waterfallBath |
| `A2VZ` | JWV13-A6S洗碗机 | JWV13-A6S | 078 | action, mode, status, switch | addMode, brightener, commonFaultDetection, leftTime, washingSalt |
| `A2W0` | JWB19-B8洗碗机 | JWB19-B8 | 078 | action, mode, status, switch | addMode, brightener, faultDetection, leftTime, washingSalt |
| `A2WF` | SJ62燃气热水器 | JSQ30-SJ62-16 | 124 | mode, status, switch, temperature | Selfclean, aiWash, cycle, faultDetection, gasTotal, heating, highTempUnlock, interrupt, iwaterTmp, waterTap, waterTotal, waterfallBath |
| `A2X5` | SJ61燃气热水器 | JSQ30-SJ61-16 | 124 | mode, status, switch, temperature | Selfclean, aiWash, cycle, faultDetection, gasTotal, heating, highTempUnlock, interrupt, iwaterTmp, tempRange, waterTap, waterTotal, waterfallBath |
| `A2X6` | ST61燃气热水器 | JSQ30-ST61-16 | 124 | mode, status, switch, temperature | Selfclean, aiWash, cycle, faultDetection, gasTotal, heating, highTempUnlock, interrupt, iwaterTmp, tempRange, waterTap, waterTotal, waterfallBath |
| `A2X7` | SS62燃气热水器 | JSQ30-SS62-16 | 124 | mode, status, switch, temperature | Selfclean, aiWash, cycle, faultDetection, gasTotal, heating, highTempUnlock, interrupt, iwaterTmp, tempRange, waterTap, waterTotal, waterfallBath |
| `A2Y0` | 松下壁挂ERV | FV-RZ06VD1 | 030 | fan, mode, pm25, switch | commonFaultDetection, filterElement1, filterElement2, filterElement3, filterElement4, holM, leftTime, preStatus |
| `A2YI` | 美的嵌入式厨房空调 |  CKF-35FW/BN1Y-FG100 | 012 | fan, mode, switch, temperature | batchCmd, commonFaultDetection, dry, prepareFood, quickFry, quickFryCenterPoint, visualization |
| `A2ZZ` | 美的吸顶式厨房空调 | CKF-35XW/BN8Y-XD200 | 012 | fan, mode, switch, temperature | batchCmd, commonFaultDetection, dry, prepareFood, quickFry, quickFryCenterPoint, visualization |
| `A30W` | 九牧智能浴霸JD176S | JD176S | 035 | action, lightSwitch, status, temperature | drySwitch, leftTime, leftTimeVen, leftTimeWarm, leftTimeWind, nightLightSwitch, ventilateSwitch, warmWindMode, windSwitch |
| `A328` | GW8i燃气热水器 | JSQ38-20GW8i | 124 | mode, status, switch, temperature | Selfclean, cycle, faultDetection, gasTotal, heating, highTempUnlock, iwaterTmp, tempRange, waterTap, waterTotal, waterfallBath |
| `A38G` | 美的风管机-悦享YX(2)2 | KFR-xxT2/BP2DN1-YX(2)2 | 012 | fan, mode, switch, temperature | automaticAirswitch |
| `A38H` | 美的风管机-悦享YX(1)3 | KFR-xxT2/BDN1(BN8)-YX(1)3 | 012 | fan, mode, switch, temperature | automaticAirswitch |
| `A38I` | 美的风管机-设计家SJ(1) | KFR-xxT2/B3DN1(B3N8)-SJ(1)(3) | 012 | fan, mode, switch, temperature | automaticAirswitch |
| `A38O` | 美的风管机-颐享iX(3) | KFR-xxT2/BxxDN1-iX(3)2/3 | 012 | fan, mode, switch, temperature | automaticAirswitch |
| `A39I` | 美的中央空调-理想家LX2 | MDVH-JxxT2/BP3N1X-LX(B)2 | 012 | fan, mode, switch, temperature | automaticAirswitch |
| `A39X` | COLMO风管机-CA38ZN8A2 | CA38ZN8A2 | 012 | fan, mode, switch, temperature | Dry, automaticAirswitch, customhumidity |
| `A39Y` | 美的风管机-乐享LX(1)3 | KFR-xxT2/B3N8-LX(1)3 | 012 | fan, mode, switch, temperature | automaticAirswitch |
| `A39Z` | 美的风管机-星光旗舰XGQ(1)3 | KFR-xxT2/B3N8-XGQ(1)3 | 012 | fan, mode, switch, temperature | automaticAirswitch |
| `A3A0` | 美的风管机-星光时尚XG(1)3 | KFR-xxT2/BN8-XG(1)3 | 012 | fan, mode, switch, temperature | automaticAirswitch |
| `A3A1` | 美的风管机-雅境YJ(1)3 | KFR-xxT2/BxNx-YJ(1)3 | 012 | fan, mode, switch, temperature | automaticAirswitch |
| `A3A6` | 美的净界星云风扇 | FGD24USQ | 029 | fan, mode, status, switch | darkMode, delayOff, onOffBeep, preOn, waterions |
| `A3A8` | 美的循环扇 | GDG24TZR/FGD24UZR | 029 | fan, mode, status, switch | darkMode, delayOff, onOffBeep, preOn |
| `A3AG` | 美的风管机-梦想家MX(1) | KFR-xxT2/BDN1(/BN8)-MX(1) | 012 | fan, mode, switch, temperature | automaticAirswitch |
| `A3AH` | 美的风管机-梦想家MXP(1) | KFR-xxT2/B3DN1(/B3N8)-MXP(1) | 012 | fan, mode, switch, temperature | automaticAirswitch |
| `A3AK` | COLMO睿极中央空调 | CAKWxxZN1C1-3 | 012 | fan, mode, switch, temperature | automaticAirswitch |
| `A3AY` | 方太Y系列智能油烟机 | CXW-358-01-Y1.i/CXW-358-01-Y2.i | 021 | lightSwitch, mode, status, switch | CtlUpDown, DelayTime, UpDownLock, commonFaultDetection, definedFanGear |
| `A3B2` | 林内燃气热水器 | RUS-R16E42G-CH | 124 | mode, status, switch, temperature | antifreezeStatus, boostMode, commonMode1, ecoSwitch, faultDetection, flameStatus, zeroColdMode, zeroColdSwitch |
| `A3B7` | 美的中央空调-空气梦想家MX | MJV-xxT2(/X)-MX(2) | 012 | fan, mode, switch, temperature | automaticAirswitch |
| `A3B8` | 美的中央空调-星光XGpro | MDS-xxT2(/P)-XGpro | 012 | fan, mode, switch, temperature | automaticAirswitch |
| `A3B9` | 美的中央空调-雅境YJ | MJV-xxT2/DX-YJ | 012 | fan, mode, switch, temperature | automaticAirswitch |
| `A3BB` | 美的中央空调-卧室新风XF | MJV-xxT2/P-XF | 012 | fan, mode, switch, temperature | automaticAirswitch, freshAirSwitch, freshAirgear |
| `A3BC` | 美的中央空调-客厅新风XF | MJV-71/80T2/P-XF | 012 | fan, mode, switch, temperature | Exhaustfan, Exhaustswitch, automaticAirswitch, freshAirSwitch, freshAirgear |
| `A3BD` | 酷风中央空调-卧室新风XF | MJZ-xxT2/DX-XF | 012 | fan, mode, switch, temperature | automaticAirswitch, freshAirSwitch, freshAirgear |
| `A3BE` | 酷风中央空调-客厅新风XF | MJZ-71T2/DX-XF | 012 | fan, mode, switch, temperature | Exhaustfan, Exhaustswitch, automaticAirswitch, freshAirSwitch, freshAirgear |
| `A3BS` | 方太智能洗碗机 | JPCD12E-NT01S | 078 | action, mode, status, switch | commonFaultDetection, leftTime, preSet |
| `A3CG` | 美的智能干衣机 | TH100-H09WZ | 0D7 | action, mode, status, switch | faultDetection, leftTime |
| `A3CJ` | COLMO智能干衣机 | CLHZ10E | 0D7 | action, mode, status, switch | faultDetection, leftTime |
| `A3CM` | COLMO智能洗衣机 | CLGZ10E | 015 | action, mode, status, switch | faultDetection, leftTime |
| `A3DE` | COLMO挂机空调 | KFR-35G/CK1C-9(1)F | 012 | fan, mode, switch, temperature | — |
| `A3DF` | COLMO柜机空调 | KFR-72L/CA1 | 2F9 | fan, mode, switch, temperature | — |
| `A3DK` | COLMO图灵中央空调 | CAKWxZN1C1-9x/CACxZN1C1-8x | 2FA | fan, mode, switch, temperature | automaticAirswitch |
| `A3DQ` | COLMO新象中央空调 | CAKWxxZN1C1-x/CACxxZN1C1-x | 2FA | fan, mode, switch, temperature | automaticAirswitch |
| `A3DR` | COLMO睿极中央空调 | CAKW22ZN1C1-3 | 2FA | fan, mode, switch, temperature | automaticAirswitch |
| `A3DS` | COLMO睿极风管机 | CAxxZNxAx | 2FA | fan, mode, switch, temperature | automaticAirswitch, sceneMode |
| `A3DX` | COLMO睿极风管机 | CAxxxZNxAx | 2FA | fan, mode, switch, temperature | automaticAirswitch, sceneMode |
| `A3DZ` | 美的中央空调 | MJV/MDVH-xx | 2FA | fan, mode, switch, temperature | automaticAirswitch |
| `A3E0` | 美的风管机 | KFR-xx | 2FA | fan, mode, switch, temperature | automaticAirswitch |
| `A3E1` | 美的新风风管机 | KFR-xxx | 2FA | fan, mode, switch, temperature | automaticAirswitch, calmSpellSwitch, freshAirSwitch, freshAirgear, sceneMode, windGear |
| `A3E6` | 海信智能空调 | KFR-35GW/X620U-X1 | 012 | fan, mode, switch, temperature | — |
| `A3E8` | 海信智能中央空调 | HVR-140W/L4FZBp/T | 2FA | fan, mode, switch, temperature | — |
| `A3EK` | 海信智能空调 | KFR-72LW/C300V-X1 | 2F9 | fan, mode, switch, temperature | — |
| `A3EX` | COLMO柜机空调 | KFR-72L/CA2 | 2F9 | fan, mode, switch, temperature | — |
| `A3EY` | COLMO柜机空调 | KFR-72L/CA5 | 2F9 | fan, mode, switch, temperature | — |
| `A3F2` | 海信智能室温控制器 | HSXC-FD01 | 2FA | fan, mode, switch, temperature | — |
| `A3F4` | COLMO新风空调 | KFR-72L/CE1H | 2F9 | fan, mode, switch, temperature | freshAirSwitch, freshAirgear |
| `A3F7` | 方太智能清洗中心 | X1A | 078 | action, mode, status, switch | command, commonFaultDetection, leftTime, lowerAreaswitch, lowerRegionStatus, remainTime, upperRegionStatus, workMode |
| `A3FW` | 美的风管机 | KFR-xxxx | 2FA | fan, mode, switch, temperature | automaticAirswitch |
| `A3FY` | COLMO厨卫中央空调 | CAC/YxxQN1E1 | 2FA | fan, mode, switch, temperature | automaticAirswitch |
| `A3FZ` | COLMO 复式洗衣机 | CLA22-T1 | 015 | action, mode, status, switch | faultDetection, leftTime, washerdoubleType |
| `A3G0` | COLMO厨卫中央空调 | CAC/YxxxQN1E1 | 2FA | fan, mode, switch, temperature | automaticAirswitch |
| `A3G1` | COLMO新象新风中央空调F | CAKW71ZN1C1-F | 2FA | fan, mode, switch, temperature | automaticAirswitch, exAirSwitch, exhaustAirSpeed, freshAirSpeed, freshAirSwitch |
| `A3G2` | COLMO新象新风中央空调 | CAKW71ZN1C1-F | 2FA | fan, mode, switch, temperature | automaticAirswitch, exAirSwitch, exhaustAirSpeed, freshAirSpeed, freshAirSwitch |
| `A3G3` | COLMO新象中央空调 | CAKWxxZN1C1-5(2) | 2FA | fan, mode, switch, temperature | automaticAirswitch |
| `A3GJ` | 格力浴享系列中央空调 | GMV-NHDZ22PLS/B | 2FA | fan, mode, switch, temperature | — |
| `A3GK` | 格力中央地暖空调 | GWV-D27WA/A | 2FA | fan, mode, switch, temperature | — |
| `A3GM` | 美的中央空调 | MJV/MDVH-xxx | 2FA | fan, mode, switch, temperature | automaticAirswitch |
| `A3GN` | 美的风管机 | KFR-x | 2FA | fan, mode, switch, temperature | automaticAirswitch |
| `A3GO` | 格力舒享系列中央空调 | GMV-NHDZ22PLS/A | 2FA | fan, mode, switch, temperature | — |
| `A3GS` | 格力智能中央空调 | FGR20Pd/DNa | 2FA | fan, mode, switch, temperature | — |
| `A3GT` | COLMO新象中央空调 | CAKWxxxZN1C1-5(2) | 2FA | fan, mode, switch, temperature | automaticAirswitch |
| `A3H1` | COLMOEVO柜机空调 | KFR-72L/CX2 | 2F9 | fan, mode, switch, temperature | automaticAirswitch, freshAirSwitch, freshAirgear, sceneMode, sterilization, switchPTC |
| `A3H2` | 华凌中央空调HL | MJZ-22T2/P-HL | 2FA | fan, mode, switch, temperature | automaticAirswitch |
| `A3H3` | 华凌风管机HL1 | KFR-75T2/BN8-HL(1)III | 2FA | fan, mode, switch, temperature | automaticAirswitch |
| `A3H4` | 华凌风管机HL | KFR-75T2/B3N8-HL(1)III | 2FA | fan, mode, switch, temperature | automaticAirswitch |
| `A3H5` | 小天鹅风管机SW1 | KFR-35T2/B3N8-SW(1)III | 2FA | fan, mode, switch, temperature | automaticAirswitch |
| `A3H8` | 小天鹅中央空调LW | MJZ-22T2/DX-LW | 2FA | fan, mode, switch, temperature | automaticAirswitch |
| `A3H9` | 美的风管机SS | KFR-36T2/B3-KS(1) | 2FA | fan, mode, switch, temperature | automaticAirswitch |
| `A3HP` | COLMOEVO竖挂二代挂机空调 | KFR-50G/CX2S | 012 | fan, mode, switch, temperature | calmSpellSwitch, freshAirSpeed, freshAirSwitch, keyToneSwitch, sceneMode, sterilization, switchPTC |
| `A3HU` | 美的风盘式中央空调T1 | MFP51WA-R/ZBPXH-T1 | 2FA | fan, mode, switch, temperature | automaticAirswitch, hvacType, keyToneSwitch, softWindSwitch |
| `A3HW` | COLMO风盘式中央空调(M)T1 | CFP51WA-R/ZBPXH-T1 | 2FA | fan, mode, switch, temperature | automaticAirswitch, hvacType, keyToneSwitch, softWindSwitch |
| `A3HX` | COLMO风盘式中央空调(C)T1 | CFP51WA-R/ZBPXH-T1 | 2FA | fan, mode, switch, temperature | automaticAirswitch, hvacType, keyToneSwitch, softWindSwitch |
| `A3I7` | A.O.史密斯蒸烤一体机 | KZQ45-M5Wi | 19B | action, status, switch, temperature | commonFaultDetection, lackWater, leftTime, mixMode, ovenMode, setWorkTime |
| `A3IW` | 美的中央空调SS | MJV-22T2/P-SS | 2FA | fan, mode, switch, temperature | automaticAirswitch |
| `A3J0` | 小天鹅中央空调客厅新风XF | MJZ-71T2/DX-LWXF | 2FA | fan, mode, switch, temperature | automaticAirswitch, exAirSwitch, exhaustAirSpeed, freshAirSpeed, freshAirSwitch |
| `A3J1` | 小天鹅中央空调卧室新风XF | MJZ-22T2/DX-LWXF | 2FA | fan, mode, switch, temperature | automaticAirswitch, freshAirSpeed, freshAirSwitch |
| `A3J8` | 美诺智能洗碗机 | G 7184 C SCVi | 078 | action, mode, status, switch | commonFaultDetection, filterElement1, filterElement2, filterElement3, leftTime, productModel |
| `A3JI` | 美诺智能烤箱 | H7860BP C | 024 | mode, status, switch, temperature | commonFaultDetection, leftTime, oven |
| `A3K3` | 小天鹅风管机LW | KFR-35T2/B3-LW(1) | 2FA | fan, mode, switch, temperature | automaticAirswitch |
| `A3KH` | 美的柜机空调T6 | KFR-72LW/T6 | 2F9 | fan, mode, switch, temperature | commonFaultDetection |
| `A3KJ` | 美诺智能暖碟机 | ESW7020 C GRGR | 2FE | mode, status, switch, temperature | commonFaultDetection, leftTime |
| `A3KN` | COLMO水系统中央空调C-T1-副本1 | CFPxWA-R/ZBPXH-T1 | 2FA | fan, mode, switch, temperature | automaticAirswitch, commonFaultDetection |
| `A3KO` | A.O.史密斯洗碗机 | DWQ17-R5Wi | 078 | action, mode, status, switch | auxiliarySwitch, commonFaultDetection, leftTime, lowerAreaswitch, lowerRegionStatus, powder, rinse, statusDoor, upperRegionStatus |
| `A3L4` | A.O.史密斯电热水器 | EWH-HGKAi | 027 | mode, status, switch, temperature | aiSwitch, commonFaultDetection, increaseCapacitySwitch, instantHeatSwitch, sterilizationSwitch |
| `A3LW` | 一拖一中央空调 | KFRd-26N/EB81U1 | 2FA | fan, mode, switch, temperature | — |
| `A3MG` | 美的柜机空调N8KS1(1P) | KFR-51L/N8KS1-1P | 2F9 | fan, mode, switch, temperature | ECOswitch, automaticAirswitch, commonFaultDetection, preventStraightWindswitch, sweepHorizon, sweepVertical, switchPTC, switchScreen |
| `A3MJ` | 美的挂机空调YC1 | KFR-26G/YC1 | 012 | fan, mode, switch, temperature | ECOswitch, automaticAirswitch, commonFaultDetection, keyToneSwitch, preventStraightWindswitch, sweepHorizon, sweepVertical, switchPTC, switchScreen |
| `A3MK` | 华凌挂机空调N8HA1III(P) | KFR-35G/N8HA1III-P | 012 | fan, mode, switch, temperature | ECOswitch, automaticAirswitch, commonFaultDetection, preventStraightWindswitch, sweepVertical, switchPTC, switchScreen |
| `A3MN` | 美诺蒸微一体机 | DGM7640 C | 19B | action, status, switch, temperature | commonFaultDetection, leftTime, mixMode |
| `A3MO` | 美诺微烤一体机 | H7840BMX C | 19B | action, status, switch, temperature | commonFaultDetection, leftTime, mixMode |
| `A3MZ` | TCL 挂式空调 好空气版 | KFR-35G/CP71 | 012 | fan, mode, switch, temperature | ECOswitch, calmSpellSwitch, co2Switch, commonFaultDetection, freshAirSpeed, freshAirSwitch, keyToneSwitch, light, softWindSwitch, switchPTC, switchScreen |
| `A3N4` | 老板油烟机CGU2P-i1 | CGU2P-i1 | 021 | fan, lightSwitch, mode, switch | acMode, acSwitch, airQuality, commonFaultDetection, delayOff, gear, leftFanSwitch |
| `A3N6` | 老板洗碗机W76-i1 Pro | W76-i1 Pro | 078 | action, mode, status, switch | addMode, commonFaultDetection, leftTime, preTimeStart, presetSwitch, statusDoor |
| `A3N7` | 老板一体机C80-i1 Pro | C80-i1 Pro | 19B | action, status, switch, temperature | commonFaultDetection, gear, leftTime, mixMode, preTimeStart, presetSwitch, setWorkTime, steamVolume |
| `A3NE` | 美的风管机酷省电KS | KFR-75T2/B3-KS(1) | 2FA | fan, mode, switch, temperature | automaticAirswitch, commonFaultDetection, hvacType, light, sceneMode, switchPTC |
| `A3NG` | 美的风管机乐享IV | KFR-35T2/B3-LX(1)IV | 2FA | fan, mode, switch, temperature | automaticAirswitch, commonFaultDetection, hvacType, sceneMode, switchPTC |
| `A3NQ` | 华帝智能洗碗机 | iD3000Max | 078 | action, mode, status, switch | auxiliarySwitch, commonFaultDetection, orderLeftTime, rinse, rinseAid, washLeftTime |
| `A3NV` | 方太智能集成净洗中心 | JPID6E-03-M-Y1 | 078 | action, mode, status, switch | addMode, commonFaultDetection, leftTime |
| `A3O5` | 老板蒸烤一体机C9077A C5 | C9077A-C5 | 19B | action, status, switch, temperature | commonFaultDetection, mixMode, preTimeStart, presetSwitch, setWorkTime, steamVolume, workTime |
| `A3OC` | 美的空气能热水器睿泉 | RSJF-V33/RN8-X1-200-(E1) | 125 | mode, status, switch, temperature | deviceType, faultDetection, highFlowSwitch, highTemperature, silentSwitch |
| `A3OD` | 美的空气能热水器天悦 | RSJF-33/DN8-200D(E1) | 125 | mode, status, switch, temperature | deviceType, faultDetection |
| `A3OL` | TCL 柜式空调 好空气版 | KFR-72L/CP71 | 2F9 | fan, mode, switch, temperature | automaticAirswitch, calmSpellSwitch, commonFaultDetection, exAirSwitch, freshAirSpeed, freshAirSwitch, keyToneSwitch, light, selfCleanswitch, softWindSwitch, switchPTC |
| `A3OT` | 美的取暖器HPT28BR | HPT28BR | 06A | childLockSwitch, mode, switch, temperature | commonFaultDetection, gear, heatSwitch, indicator, keyToneSwitch |
| `A3P4` | 老板电器油烟机CG26X32 D3 | CG26X32-D3 | 021 | lightSwitch, mode, status, switch | acSwitch, airQuality, delayOff, gear, leftFanSwitch |
| `A3PA` | 华帝智能电热水器 | i14245 | 027 | mode, status, switch, temperature | aiSwitch, autoPowerOffSwitch, capacity, commonFaultDetection, sterilizationSwitch, water |
| `A3PK` | TCL风管机 | KFR-36FW/AF2Gb | 2FA | fan, mode, switch, temperature | calmSpellSwitch, keyToneSwitch, light, softWindSwitch, switchPTC |
| `A3PO` | 美的壁挂式空调M5 | KFR-35GW/M5 | 012 | fan, mode, switch, temperature | ECOswitch, automaticAirswitch, commonFaultDetection, keyToneSwitch, light, sleepCurveSwitch, switchPTC, switchScreen |
| `A3PS` | Leader挂机 | KFR-35GW/LX1-1 | 012 | fan, mode, switch, temperature | commonFaultDetection |
| `A3PT` | Leader柜机 | KFR-72LW/LX1-1 | 2F9 | fan, mode, switch, temperature | commonFaultDetection, exhaustAirSpeed, freshAirSpeed |
| `A3Q1` | 美的立柜式空调BF1 | KFR-72L/JW1 | 2F9 | fan, mode, switch, temperature | automaticAirswitch, commonFaultDetection, preventStraightWindswitch |
| `A3Q2` | TCL中央空调 | TMVd-36F/AF2GbA-P | 2FA | fan, mode, switch, temperature | calmSpellSwitch, keyToneSwitch, light, softWindSwitch, switchPTC |
| `A3Q4` | TCL天花机 | KFR-72QW/AF1Za-D1 | 2FA | fan, mode, switch, temperature | calmSpellSwitch, keyToneSwitch, light |
| `A3Q5` | TCL风管机 新风版 | KFR-72FW/YP1Ca | 2FA | fan, mode, switch, temperature | calmSpellSwitch, freshAirSpeed, freshAirSwitch, keyToneSwitch, light, softWindSwitch, switchPTC |
| `A3QC` | 华凌立柜式空调HE1II | KFR-72L/N8HE1IIUltra | 2F9 | fan, mode, switch, temperature | ECOswitch, automaticAirswitch, commonFaultDetection, sceneMode, switchPTC |
| `A3QF` | 美的壁挂式空调KS1(S1) | KFR-26G/N8KS1-1 | 012 | fan, mode, switch, temperature | ECOswitch, airConditioner, automaticAirswitch, commonFaultDetection, switchPTC |
| `A3QI` | 嘉格纳洗碗机 | DF270800 | 078 | action, mode, status, switch | commonFaultDetection, leftTime, lowerRegionStatus, preTimeStart, presetSwitch, upperRegionStatus |
| `A3QK` | 美的壁挂式空调KS1(S4) | KFR-35G/N8KS1-1X | 012 | fan, mode, switch, temperature | ECOswitch, airConditioner, automaticAirswitch, commonFaultDetection, switchPTC |
| `A3QU` | 美的立柜式空调KS2 | KFR-72L/KS2P | 2F9 | fan, mode, switch, temperature | ECOswitch, automaticAirswitch, commonFaultDetection, sceneMode, switchPTC |
| `A3RA` | 美的壁挂式空调通用 | KFR-35GW/N8HL1XPro | 012 | fan, mode, switch, temperature | commonFaultDetection |
| `A3RC` | 美的立柜式空调通用 | KFR-51LW/N8MFA3 | 2F9 | fan, mode, switch, temperature | commonFaultDetection |
| `A3RK` | 老板电器热水器HT8 i1 Pro | HT8-i1 Pro | 124 | mode, status, switch, temperature | boostMode, commonFaultDetection, zeroColdSwitch |
| `A3RS` | 华凌风管机HLU | KFR-75T2/B3-HLU(1) | 2FA | fan, mode, switch, temperature | automaticAirswitch, commonFaultDetection, hvacType, light, sceneMode, switchPTC |
| `A3S0` | 海信挂机空调 | KFR-35GW/A61-X1 | 012 | fan, mode, switch, temperature | — |
| `A3SD` | 老板洗碗机ZXW80 S2U | ZXW80-S2U | 078 | action, mode, status, switch | commonFaultDetection, filterElement1, filterElement2, leftTime, statusDoor |
| `A3T5` | 老板电器油烟机CG8869 G30 | CG8869-G30 | 021 | lightSwitch, mode, status, switch | acMode, acSwitch, airQuality, delayOff, gear |
| `A3TS` | 博世洗碗机 | SJV6ZMX11C | 078 | action, mode, status, switch | addMode, commonFaultDetection, leftTime, lowerRegionStatus, preTimeStart, presetSwitch, upperRegionStatus |
| `A3TU` | 西门子 洗碗机 | SJ65ZX88MC | 078 | action, mode, status, switch | addMode, commonFaultDetection, leftTime, lowerRegionStatus, preTimeStart, presetSwitch, upperRegionStatus |
| `A3U3` | 美的壁挂式空调KS1(S3) | KFR-35G/N8KS1-1U | 012 | fan, mode, switch, temperature | ECOswitch, airConditioner, automaticAirswitch, commonFaultDetection, switchPTC |
| `A3U4` | 美的壁挂式空调KS1(S2) | KFR-35G/N8KS1-1Q | 012 | fan, mode, switch, temperature | ECOswitch, airConditioner, automaticAirswitch, commonFaultDetection, switchPTC |
| `A3U8` | 嘉格纳Expressive 艺境系列全自动意式咖啡机 | GC451120 | 0B9 | action, mode, status, switch | brewingMode, commonFaultDetection |
| `A3UJ` | 美的风管机星光IV | KFR-35T2/B3-XG(1)IV | 2FA | fan, mode, switch, temperature | airConditioner, commonFaultDetection, hvacType, sceneMode, switchPTC |
| `A3W0` | 老板蒸烤一体机CQ01 i1 | CQ01-i1 | 19B | lightSwitch, status, switch, temperature | commonFaultDetection, leftTime, ovenSteamer |
| `A3WO` | 能率热水器GQ-16K6AAFEX | GQ-16K6AAFEX | 124 | mode, status, switch, temperature | commonFaultDetection, flameStatus, totalGas, totalWater, zeroColdMode |
| `A3WU` | 方太智能烤箱(智能屏) | KQD65F-03-X20.i | 024 | childLockSwitch, lightSwitch, status, temperature | commonFaultDetection, leftTime, oven |
| `A3X4` | 老板电器油烟机78 i7 | 78-i7 | 021 | lightSwitch, mode, status, switch | acMode, acSwitch, airQuality, delayOff, gear, gestureSwitch |
| `A3XK` | 老板蒸烤一体机C98A D3P | C98A-D3P | 19B | lightSwitch, status, switch, temperature | commonFaultDetection, leftTime, ovenSteamer |
| `A3Y3` | 卡萨帝光年洗碗机 | CWC10-B69U1(N11X) | 078 | action, mode, status, switch | remoteControlService, statusDoor |
| `A3Z7` | 美的壁挂式空调风尊IIPro | KFR-35G/N8MXC1IIPro | 012 | fan, mode, switch, temperature | ECOswitch, airConditioner, automaticAirswitch, commonFaultDetection, switchPTC |
| `A40Y` | 美的立柜式空调酷省电KS1(S1) | KFR-51L/N8KS1-1U | 2F9 | fan, mode, switch, temperature | ECOswitch, automaticAirswitch, commonFaultDetection, sceneMode, switchPTC |
| `A40Z` | 美的立柜式空调酷省电KS1(S2) | KFR-51L/N8KS1-2P | 2F9 | fan, mode, switch, temperature | ECOswitch, airConditioner, automaticAirswitch, commonFaultDetection, switchPTC |
| `A41H` | 老板蒸烤一体机C98A G2 | C98A-G2 | 19B | lightSwitch, status, switch, temperature | commonFaultDetection, leftTime, ovenSteamer |
| `A42I` | 奥克斯空调家用挂机 | KFR-35GW | 012 | fan, mode, switch, temperature | commonFaultDetection, eco, healthy, screen, sleep, supportHeat |
| `A42J` | 奥克斯空调家用柜机 | KFR-51LW | 2F9 | fan, mode, switch, temperature | commonFaultDetection, eco, healthy, screen, sleep, supportHeat |
| `A43E` | 美的立柜式空调风尊3 | KFR-72L/MXC3 | 2F9 | fan, mode, switch, temperature | ECOswitch, airConditioner, automaticAirswitch, commonFaultDetection, sceneMode, switchPTC |
| `A43F` | 美的立柜式空调全面风QM1 | KFR-51L/N8QM1 | 2F9 | fan, mode, switch, temperature | ECOswitch, airConditioner, automaticAirswitch, commonFaultDetection, sceneMode, switchPTC |
| `A43H` | 华凌中央空调DXHL | MJZ-22T2/DX-HL | 2FA | fan, mode, switch, temperature | automaticAirswitch, commonFaultDetection, hvacType, sceneMode, sterilization, switchPTC, waterAndFanValveMode |
| `A43Y` | 嘉格纳臻境系列咖啡机 | GC251100 | 0B9 | action, mode, status, switch | brewingMode, commonFaultDetection |
| `A448` | 美的除湿机CF30BDBP3N7DI | CF30BD/BP3N7-DI | 09B | fan, humidity, mode, switch | airClean, anionSwitch, commonFaultDetection, dehumidity, delayOff, delayOn, indicator, keyToneSwitch |
| `A46E` | 美的壁挂式空调酷省电KS2A | KFR-26G/KS2-A | 012 | fan, mode, switch, temperature | ECOswitch, airConditioner, automaticAirswitch, commonFaultDetection, fastColdheat, switchPTC |
| `A46F` | 美的壁挂式空调酷省电72GKS2 | KFR-72G/KS2 | 012 | fan, mode, switch, temperature | ECOswitch, airConditioner, automaticAirswitch, commonFaultDetection, switchPTC |
| `A46G` | 美的壁挂式空调酷省电N8KSU | KFR-26G/N8KSU | 012 | fan, mode, switch, temperature | ECOswitch, airConditioner, automaticAirswitch, commonFaultDetection, switchPTC |
| `A46U` | 美的立柜式空调酷省电KS2 | KFR-72L/KS2 | 2F9 | fan, mode, switch, temperature | ECOswitch, airConditioner, automaticAirswitch, commonFaultDetection, sceneMode, switchPTC |
| `ZG0C` | 智能开关 2键 | OSLO-SS2 | A13 | brightness, childLockSwitch, switch1, switch2 | backlight, button1, button2, faultDetection, memorySwitch, mode1, mode2, reboot |
| `ZG0K` | 智能开关 (无线版) 3键 | OSLO-BS3 | A13 | childLockSwitch, switch1, switch2, switch3 | button1, button2, button3, faultDetection, memorySwitch, mode1, mode2, mode3, reboot |
| `ZG10` | 智能开关 2键 | OSLO-SS2 | A13 | brightness, childLockSwitch, switch1, switch2 | backlight, button1, button2, faultDetection, memorySwitch, mode1, mode2, reboot |
| `ZG1L` | 华为鸿蒙智家 智能开关 蒙德里安 | PCP-MLB300 | A13 | brightness, switch1, switch2, switch3 | DNDmode, backlight, button1, button2, button3, button4, faultDetection, mode1, mode2, mode3, mode4 |
| `ZG1U` | 智能开关 2键 | PHP-W2-P1 | A13 | brightness, childLockSwitch, switch1, switch2 | backlight, button1, button2, faultDetection, memorySwitch, mode1, mode2, reboot |
| `ZG2Q` | 迈腾智能开关 (无线版) 3键 | PCP-OB3106 | A13 | childLockSwitch, switch1, switch2, switch3 | button1, button2, button3, faultDetection, memorySwitch, mode1, mode2, mode3, reboot |
| `ZG2T` | 智能开关 奥斯陆(无线版) 3键 | PCP-OB3106 | A13 | childLockSwitch, switch1, switch2, switch3 | button1, button2, button3, faultDetection, memorySwitch, mode1, mode2, mode3, reboot |
| `ZG2U` | 智能开关 奥斯陆(无线版) 4键 | PCP-OB4116 | A13 | childLockSwitch, switch1, switch2, switch3 | button1, button2, button3, button4, faultDetection, memorySwitch, mode1, mode2, mode3, mode4, modeX, reboot |
| `ZG2V` | 智能开关 奥斯陆(无线版) 6键 | PCP-OB6116 | A13 | childLockSwitch, switch1, switch2, switch3 | button1, button2, button3, button4, button5, button6, faultDetection, memorySwitch, mode1, mode2, mode3, mode4, mode5, mode6, reboot |
| `ZG2Z` | 智能开关 威尼斯(无线版) 3键 | PCP-OB3116-PF | A13 | childLockSwitch, switch1, switch2, switch3 | button1, button2, button3, faultDetection, memorySwitch, mode1, mode2, mode3, reboot |
| `ZG30` | 智能开关 都灵 2键 | PCP-TP2116 | A13 | brightness, childLockSwitch, switch1, switch2 | backlight, button1, button2, faultDetection, memorySwitch, mode1, mode2, reboot, theme |
| `0102` | 灯组 |  | 01B | brightness, cct, switch | — |
| `0106` | 灯组 |  | 01B | brightness, cct, switch | — |
| `101S` | 欧普罗迪智能灯 | floor lamp001 | 04F | brightness, lightMode, switch | — |
| `101s` | 美的清羽智能风扇FTS30 | FTS30-16BR | 029 | fan, switch, temperature | faultDetection |
| `1027` | 美的加湿器 | SZK-3B20 | 052 | humidity, switch, temperature | faultDetection, gear |
| `103O` | 欧普香薰助眠灯 | OPXXD | 01B | brightness, colour, switch | aroma, faultDetection |
| `103P` | 欧普网关OPLYWG | OPLYKG | 020 | brightness, colour, switch | breathiLight, discovery, favorite, groupControl, groupDevList, groupManage, location, voice |
| `1055` | 瑞晶筒灯RAL-2 | RAL-2 | 01B | brightness, cct, switch | — |
| `105T` | YeeLight彩灯 | 未知 | 01B | brightness, mode, switch | faultDetection, relativeDelay |
| `105W` | TPLink彩灯 | 未知 | 01B | brightness, mode, switch | relativeDelay |
| `106I` | 迈迪加Nox音乐床头灯SN902W | SN902W | 01B | brightness, colour, switch | alarmClock , handControl, nightLight, sleepAid, wirelessaudio |
| `112O` | 亚摩斯养生壶 | YSH12-17A | 060 | mode, status, switch | command, cookInfo, currentTemperature, faultDetection, heatpower, keepWarmTP, preTime, remPreTime, remWorkTime, workTime |
| `112Q` | 踢脚线取暖器 | HD83RC-22R | 06A | mode, switch, temperature | childLock, currentTemperature, faultDetection, gear |
| `113N` | Yeelight白光灯泡 | mono | 01B | brightness, lightMode, switch | — |
| `113O` | Yeelight色温灯泡 | ct_bulb | 01B | brightness, cct, switch | — |
| `113Q` | Yeelight护眼台灯 | desklamp | 046 | brightness, lightMode, switch | — |
| `113T` | 柏翠蒸烤箱PE8289WT | PE8289WT | 024 | mode, status, temperature | cookInfo, doorStatus, faultDetection, humidifier, leftTime, light, startCommand |
| `113V` | Yeelight吸顶灯 | ceiling2 | 01B | brightness, lightMode, switch | — |
| `114O` | 奥普智能晾衣机D8 | D8 | 028 | action, lightSwitch, status | — |
| `115Q` | HDL地暖 | HDL-FH06 | 02A | mode, switch, temperature | — |
| `121N` | 亚摩斯足浴盆AS-FT100B | AS-FT100B | 070 | mode, status, temperature | command, cookInfo, currentTemperature, faultCode, leftTime, workTime |
| `121P` | 亚摩斯IH电压力锅AS-YDG502H | AS-YDG502H | 074 | mode, status, switch | command, cookInfo, currentPressure, faultCode, leftTime, preTime, warmDuration, workTime |
| `122O` | 艾美特移动地暖WD22-A1 | WD22-A1 | 06A | childLockSwitch, switch, temperature | faultDetection, screenSwitch, state, timing |
| `123S` | SONOFF TX3C 智能墙壁开关 | T2UK3C | 005 | switch1, switch2, switch3 | hideSwitch, powerLight, pulseLength1, pulseLength2, pulseLength3, pulseSwitch1, pulseSwitch2, pulseSwitch3, startup1, startup2, startup3, switchOff, switchOn |
| `130O` | A.O.史密斯燃气热水器 | JSQ48-SJSX | 027 | mode, switch, temperature | boost, burningStatus, faultCode, gasSafeStatus, loopStatus, machineSafeStatus, noColdWater, noColdWaterMode, reserveTimer |
| `135S` | 流光开关一联 | LS055 | 005 | colour, lightMode, switch | backlight, memoryState |
| `146Z` | 亚摩斯扫地机AS-X5E | AS-X5E | 031 | action, mode, status | area, box, commonFaultDetection, modeswitch, power, powerswitch, suction, worktime |
| `151H` | 欧普延系列蓝牙控制盒 | YAN | 01B | brightness, cct, switch | — |
| `156A` | 欧派油烟机 | CXW-180-E638J | 021 | lightSwitch, mode, switch | autoTurnOff, delayOff, faultDetection, gear, stirFriedOff |
| `157Z` | 威廷智能三开Wi-Fi | VE-AK03LNW | 005 | switch1, switch2, switch3 | — |
| `163K` | 水爱智能盖板 | SA2422 | 066 | mode, switch, temperature | ECO, Water, buzzer, cleaning, deodorization, faultDetection, jetcleaner, light, spraynozzlePosition, stop, warmbraw, waterIntensity, windwarm |
| `164B` | 智能三开开关 | VE-AK03LNB | 005 | switch1, switch2, switch3 | — |
| `164M` | 平头熊三键开关WIFI | PTX-TCswitch03 | 005 | switch1, switch2, switch3 | — |
| `171W` | A.O.史密斯零冷水VJS系列 | JSQ-VJS | 027 | mode, switch, temperature | boost, burningStatus, faultCode, gasSafeStatus, loopStatus, machineSafeStatus, noColdWater, noColdWaterMode, waterControl |
| `171X` | A.O.史密斯ESC系列 | JSQ-CSC | 027 | mode, switch, temperature | burningStatus, faultCode, gasSafeStatus, machineSafeStatus |
| `175M` | 艾美特移动地暖D22-A | D22-A | 06A | childLockSwitch, switch, temperature | screenSwitch, state, timing |
| `175Y` | 艾美特移动地暖D22 | D22 | 06A | childLockSwitch, switch, temperature | faultDetection, screenSwitch, state, timing |
| `181K` | 艾美特移动地暖WD22-A4 | WD22-A4 | 06A | childLockSwitch, switch, temperature | screenSwitch, state, timing |
| `183E` | 噼啪智能三开开关 | PIPA-AK03LNW | 005 | switch1, switch2, switch3 | — |
| `201E` | 麦乐克温湿度传感器 | MIR-TE100 | 04E | battery, humidity, temperature | — |
| `204L` | 亚都加湿器SC300-SK045ProHi | SC300-SK045Pro(Hi) | 052 | childLockSwitch, humidity, switch | capacity, gear, light, sound, timing |
| `204Z` | 四季沐歌M-HY902H-GG智能晾衣机 | M-HY902H-GG | 028 | action, lightSwitch, status | airDry, disinfect, drying |
| `205Q` | 四季沐歌M-HY900Z-GG智能晾衣机 | M-HY900Z-GG | 028 | action, lightSwitch, status | — |
| `208B` | 叶绿体自发电无线门铃WiFi版 | CDB-Q30I | 099 | switch1, switch2, switch3 | bellServ, commonExecution1, commonExecution2, curOpServ, devStateServ, info, muteOpServ, pairInfoServ, pairState, switch4, switch5, switch6, switch7, switch8, volume |
| `20CL` | 12W双色温射灯调光驱动器套装 | BL2210R | 01B | brightness, cct, switch | faultDetection |
| `20CN` | 15W双色温射灯调光驱动器套装 | BL2211R | 01B | brightness, cct, switch | faultDetection |
| `20DG` | 永林双色调光器 | PLH-LB2X40-15-CT1 | 01B | brightness, cct, switch | — |
| `20ED` | 艾优智能电动牙刷-宝可梦 | P8-H | 073 | battery, mode, status | Brushingmode, brushingHistory, custom |
| `20F6` | 智能温感变频静音风扇 | FSD30-19BRBW | 029 | fan, mode, switch | Light, OSC |
| `20FB` | 亚摩斯电炖锅AS-WD40F | AS-WD40F | 026 | action, mode, status | faultDetection, leftTime, preTimeEnd, presetSwitch, setWorkTime, warmTime, workTime |
| `20FI` | 海令冷暖调光器 | SMK-H1-PWM2 | 01B | brightness, cct, switch | — |
| `20GM` | 艾美特空气循环扇FA23-AD17 | FA23-AD17 | 029 | fan, mode, switch | timing |
| `20H9` | 晾品智能晾衣机 | HW60 | 028 | action, lightSwitch, status | airDry, airDryRemTime, airDryTime, disinfect, disinfectRemTime, disinfectTime, dryRemTime, dryTime, drying |
| `20IA` | 亚摩斯电饭煲AS-WF20S | AS-WF20S | 026 | action, mode, status | faultDetection, leftTime, preTimeEnd, presetSwitch, warmTime, workTime |
| `20IB` | 亚摩斯电饭煲AS-WF40SG | AS-WF40SG | 026 | action, mode, status | faultDetection, leftTime, preTimeEnd, presetSwitch, setWorkTime, warmTime, workTime |
| `20JM` | 欧派智能晾衣机 | OP-L1010X | 028 | action, lightSwitch, status | airDry, disinfect, drying, motorBlock |
| `20K0` | 亚摩斯电饭煲AS-IHW40K | AS-IHW40K | 026 | action, mode, status | faultDetection, leftTime, preTimeEnd, presetSwitch, setWorkTime, warmTime, workTime |
| `20NY` | 亚摩斯风扇AS-FS12D | AS-FS12D | 029 | fan, mode, switch | snaking, timing |
| `20PO` | 亚都智能恒湿加湿器045Pro(Hi)2.0 | 1.0 | 052 | childLockSwitch, humidity, switch | capacity, gear, light, sound |
| `20PV` | 锐点智能盒 | S021H | 01B | brightness, cct, switch | — |
| `20PX` | 亚摩斯降糖电饭煲AS-WFT30L | AS-WFT30L | 026 | action, mode, status | faultDetection, leftTime, preTimeEnd, presetSwitch, setWorkTime, warmTime, workTime |
| `20PY` | 亚摩斯挂机空调KFR-35GW | KFR-35GW/BPDC+N3 | 012 | fan, mode, switch | boostingHot, clean, currentTemp, faultDetection, light, sleeping, targetTemp, timing |
| `20QC` | 亚摩斯电饭煲AS-IHW30H | AS-IHW30H | 026 | action, mode, status | faultDetection, leftTime, preTimeEnd, presetSwitch, setWorkTime, warmTime, workTime |
| `20QK` | 摩根调色温灯 | 1.0 | 044 | brightness, cct, switch | — |
| `20SA` | 亚摩斯柜机空调KFR-51LW | KFR-51LW/BPDH+N1 | 012 | fan, mode, switch | boostingHot, clean, currentTemp, faultDetection, light, sleeping, targetTemp, timing |
| `20TJ` | 易百珑双路开关 | EWS02-H | 064 | switch, switch1, switch2 | CleanPair, Pair, memorySwitch |
| `20UC` | 领普双键墙壁开关 | Q3D-HW-W2 | 005 | switch, switch1, switch2 | led |
| `20XW` | 控客-星空三路灯控面板 | KK-LP-L03W | 005 | switch1, switch2, switch3 | — |
| `20Y3` | 永林一拖二色温驱动 | PLH-LB4X40-30-CT11 | 044 | switch, switch1, switch2 | brightness1, brightness2, cct1, cct2 |
| `20YD` | 控客-环境传感器 | KK-ES-J01W | 04E | battery, humidity, temperature | illumination |
| `20YQ` | 亚摩斯电水壶AS-CP071 | AS-CP071 | 09A | status, switch, temperature | faultDetection, workMd |
| `20YY` | 智能充气宝 | A3301M | 179 | mode, status, switch1 | commonFaultDetection, led, power, pressure, pressureBAR, pressurePSI, start, times |
| `20ZJ` | 智能恒温水壶 | AH-H001 | 09A | mode, status, temperature | Chlorine, LongBoiling, PowerSwitch, PoweroffMemory, TemperatureAdjustment, WaterMonitoring, preTimeStart, presetSwitch |
| `213X` | 西顿调色模块 | SWP01-QL-15W-2 | 044 | brightness, cct, switch | — |
| `213Z` | 西顿一拖二调色模块 | SWP01-QL-9W-22 | 044 | switch, switch1, switch2 | brightness1, brightness2, cct1, cct2 |
| `214V` | 智汇云二位轻触开关面板 | Z4002 | 005 | switch, switch1, switch2 | — |
| `2155` | 施铂智能恒温电热水壶 | RS-K01 | 09A | mode, status, temperature | boolwater, faultDetection, warmSwitch, warmswitch1, warmtime, watime |
| `215E` | 西顿恒压调色模块 | SWP01-QY-100W-2 | 044 | brightness, cct, switch | — |
| `215H` | 施铂智能加湿器 | RS-H01 | 052 | childLockSwitch, humidity, switch | AUTO, BEE, FanMode, MOTO, SLEEP, Water, commonFilterElement1, faultDetection, gear |
| `215M` | 触控双开零火开关 | U4030200 | 005 | switch, switch1, switch2 | — |
| `217L` | 开关智能控制器2型 | U4030200 | 005 | switch, switch1, switch2 | — |
| `218D` | 西门子微蒸烤一体机 | CP269AGS0W | 024 | mode, status, switch | childLock, control, devDoor, faultDetection, favorite, leftTime, localFood |
| `218J` | 亚摩斯电压力锅AS-YDG503Z | AS-YDG503Z | 074 | action, mode, status | faultDetection, food, leftTime, preTimeStart, presetSwitch, pression, setWorkTime, workTime |
| `21AN` | 汇优尚品A6智能牙刷 | HY-A6-A | 073 | battery, mode, status | brushLead, brushScore, brushingHistory, filterElement, moreSetting, position |
| `21B6` | 圆和二路智能开关 | X9ZK2 | 005 | switch, switch1, switch2 | — |
| `21BA` | 超声波清洗机 | Q35 | 000 | mode, status, switch1 | commonFaultDetection, power, start, times |
| `21BB` | 亚摩斯饮水机AS-WH22B | AS-WH22B | 06F | childLockSwitch, mode, status | faultDetection, sterilize, sterilizeOff, sterilizeOn, waterLevel |
| `21BV` | 新风水地暖温控器 | B4210800 | 06A | childLockSwitch, fan, temperature | freshAirSwitch, heatSwitch |
| `21CE` | 亚摩斯果蔬净化机AS-FV09D | AS-FV09D | 078 | mode, status, switch | remainTime |
| `21DA` |  | LS087WH | 006 | action, hcho, status | sensitivity |
| `21EJ` | JW智能开关4键型 | JHKJ_PANEL_KEY4 | 005 | switch1, switch2, switch3 | switch4 |
| `21EQ` |  | JHKJ_FA_V1 | 030 | fan, mode, switch | filterElement |
| `21F9` | 艾优智能电动牙刷 | P7-H | 073 | battery, mode, status | Brushingmode, brushingHistory, custom |
| `21FD` | 艾优智能电动牙刷-故宫 | P7-H | 073 | battery, mode, status | Brushingmode, brushingHistory, custom |
| `21G6` | 超广角自然风风扇 | FL-12136DRRa(WF) | 029 | fan, mode, switch | endTime |
| `21GC` | 艾美特空气循环扇CA23-AD37 | CA23-AD37 | 029 | fan, mode, switch | onOffBeep, timing |
| `21GH` | JW空气检测C型 | 1 | 006 | hcho, humidity, temperature | co2, tvoc |
| `21GM` | JW智能开关3键型 | JHKJ_PANEL_KEY3 | 005 | switch1, switch2, switch3 | — |
| `21LA` | 永林恒压色温驱动 | PLH-LA2X24-100-CT1 | 044 | brightness, cct, switch | — |
| `21LH` | 米立3路智能开关面板 | MS-V8613G | 005 | switch1, switch2, switch3 | — |
| `21M7` | 德姆勒智能电风扇 | WAT8-158 | 029 | fan, mode, switch | Angle, BackLight, end |
| `21SE` | 调色温灯带（灯带调光器） | CP2201H | 01B | brightness, cct, switch | — |
| `21SZ` | 蓓慈足浴器BZ307B1 | BZ307B1 | 070 | status, switch, temperature | currentTemperature, faultDetection, leftTime, massage, setWorkTime |
| `21TW` | 鸿蒙智选 达伦智能台灯2 | MT615-D20WTT | 046 | brightness, lightMode, switch | nightSwitch, studyMode, studyResult |
| `21V9` | 瑞晶冷热源一体机 | RGTF-485-04 | 012 | mode, switch, temperature | — |
| `21VA` | 瑞晶壁挂炉 | RGFH-485-01 | 06A | mode, switch, temperature | — |
| `21W3` | 瑞晶色温灯 | RGBLE-R-L3 | 01B | brightness, cct, switch | — |
| `221U` |  | A3Z-DK-02 | 005 | switch, switch1, switch2 | — |
| `224A` |  | CP2003H | 01B | brightness, cct, switch | — |
| `224D` |  | CP2202H | 01B | brightness, cct, switch | — |
| `224J` | 觅石智能加湿器 | HM2508 | 052 | childLockSwitch, humidity, switch | DDJY, DWTJ, QSTS |
| `224M` |  | MR5012H | 006 | humidity, pm25, temperature | pm10 |
| `224Q` |  | CP8231H | 030 | fan, pm25, switch | — |
| `2261` | 欧派智能晾衣机 | OP-JPJD009-B | 028 | action, lightSwitch, status | airDry, disinfect, drying, motorBlock |
| `2262` | 长虹极简挂机 | KFR-35GW/ZDKTW2+R1 | 012 | fan, mode, switch | ECO, electricalHeating, faultDetection, fresh, indoor, outdoor, selfclean, temper |
| `2264` | 欧派智能声控晾衣机 | OP-JPJD010-B | 028 | action, lightSwitch, status | airDry, disinfect, drying, motorBlock |
| `227R` | 亚摩斯睿雅单火开关双键 | ZJ-KG32H | 005 | switch, switch1, switch2 | — |
| `22CL` | 澳柯玛H-power高能瞬热电热水器M101 | FCD-20M101 | 027 | mode, switch, temperature | faultDetection, flow, linertemperature, state |
| `22ER` | 吸顶式温湿度传感器 | BL5009R | 04E | humidity, switch, temperature | humidityReportSetting, tempReportSetting |
| `22EX` | 北欧夫人智能晾衣架 | BO-501 | 028 | action, lightSwitch, status | airDry, airDryRemTime, airDryTime, disinfect, disinfectRemTime, disinfectTime, dryRemTime, dryTime, drying |
| `22F2` | 蓓慈足浴器BZ312V1 | BZ312V1 | 070 | status, switch, temperature | Gushing, Red, faultDetection, temper |
| `22GN` | Soopu智能晾衣架 | SP-501 | 028 | action, lightSwitch, status | airDry, airDryRemTime, airDryTime, disinfect, disinfectRemTime, disinfectTime, dryRemTime, dryTime, drying |
| `22GR` | 澳柯玛智能电热水器C707H | FCD-60C707H | 027 | mode, switch, temperature | breakdown, faultDetection, prSwitch, preStart, setmode, state |
| `22GW` | 汇优尚品电动牙刷A6 | HY-A6-A | 073 | battery, mode, status | brushingHistory, filterElement, position, setWorkTime |
| `22QW` | 澳柯玛智能电热水器B808H | FCD-60B808H | 027 | mode, switch, temperature | faultDetection, frequency, powerdown, prestart, state |
| `22RZ` | 澳柯玛智能燃气热水器13S005H | JSQ25-13S005H | 027 | mode, switch, temperature | WaterInjection, Zerocoldwater, airflow, antifreezing, code, draughtfan, faultDetection, flame, flow, preswitchone, preswitchtwo, pretimeone, pretimetwo, promotion, waterpump, wateryield |
| `22S4` | 町米智能电磁炉 | YCL01H | 079 | mode, status, switch | faultDetection, heatGear |
| `22YK` | 亚摩斯智能踢脚线取暖器 | NS-DL221W | 06A | childLockSwitch, switch, temperature | gear, timingOff, timingOn |
| `22YV` | 澳柯玛智能电热水器A022H | FCD-60A022H | 027 | mode, switch, temperature | Frequencywashing, Latemorningbath, Pointsare, Residualhotwater, faultDetection, prestart, state |
| `23DS` | 倍轻松智能艾灸盒 | TP-201H | 0C3 | battery, switch, temperature | commonFaultDetection, countdown, gear |
| `23QV` | ACEMATIC地暖模块 | SH100312KI | 06A | mode, switch, temperature | — |
| `23RF` | 黑创智能晾衣机 | HWX80 | 028 | action, lightSwitch, status | airDry, disinfect, drying, motorblock |
| `23WL` | 亚摩斯极境开关双键 | ZJ-KG55H | 005 | switch, switch1, switch2 | — |
| `23XJ` | X1Max蒸汽米汤饭煲 | X1Max | 026 | action, mode, status | faultDetection, leftTime, preTimeEnd, presetSwitch, settime, workTime |
| `248K` | 控客-肖邦四路灯控面板 | KK-LP-D84D | 005 | switch1, switch2, switch3 | switch4 |
| `2492` | 太太乐智能晾衣机 | TES-9003SH | 028 | action, lightSwitch, status | airDry, disinfect, drying, motorBlock |
| `24AE` | 波可龙智能加湿器 | HM0801 | 052 | childLockSwitch, humidity, switch | DDJY, DWTJ, QSTS |
| `24HE` | Evoyo三路开关小模块 | MPR0310-ZB.10 | 064 | switch1, switch2, switch3 | — |
| `24RF` | 澳柯玛智能燃气热水器S011H | JSQ25-13S011H | 027 | mode, switch, temperature | WaterInjection, code, draughtfan, faultDetection, flame, flow, promotion, wateryield |
| `24RG` | 澳柯玛智能燃气热水器S012H | JSQ30-16S012H | 027 | mode, switch, temperature | code, draughtfan, faultDetection, flame, flow, promotion |
| `24T6` | 澳柯玛智能燃气热水器16S005H | JSQ30-16S005H | 027 | mode, switch, temperature | WaterInjection, Zerocoldwater, airflow, antifreezing, code, draughtfan, faultDetection, flame, flow, preswitchone, preswitchtwo, pretimeone, pretimetwo, promotion, waterpump, wateryield |
| `24YC` | 奥佳华按摩枕 OG2210 | OG2210 | 0CA | alarm, mode, switch | KnockingSpeed, electricity, heat, stop, surTime, suspend |
| `253M` | ZTK纯净加湿器 | Air Plus X10 | 052 | childLockSwitch, humidity, switch | Anion, Light, Sound, capacity, gear |
| `25BN` | 香百年智能香薰机 | XH-001 | 0DE | battery, mode, switch | Intensity, autoConnect, commonFilterElement1, durationtime, manual, numberofcycles, recommend |
| `25G8` | 美森导入导出焕颜美容仪 | WHD6 | 0EA | battery, status, switch | F002, F003, F004, F005, F006, F007, F008, skinMode |
| `2661` | MAXHUB 会议全向麦音箱 | BM31 | 198 | battery, status, switch | electricity, microphone, noiseReduction, toneMode, userManual, volumeControl |
| `26M7` | 得途BBQ智能空气炸锅 | DT-KZ58L | 063 | action, status, temperature | Devicestatus, customizemode, leftTime, preTimeEnd, preTimeStart, presetSwitch, recipes, workTime |
| `26U1` | 酷轻松石墨烯气囊支撑腰带 | PMA-D30 | 0CA | mode, switch, temperature | heat, remaining, timerlabel, workstatus |
| `26VH` | 创维智能足浴盆 | GY-E606 | 070 | action, switch, temperature | WorkingCondition, leftTime, setWorkTime |
| `26YS` | 好易点智能晾衣机消毒款 | H30C-W-HW | 028 | action, lightSwitch, status | commonFaultDetection, disinfect, disinfectRemTime |
| `2754` | 智能晾衣机 | HP-D204-2BT | 028 | action, lightSwitch, status | airDry, airDryRemTime, airDryTime, commonFaultDetection, disinfect, disinfectRemTime, disinfectTime, dryRemTime, dryTime, drying |
| `279R` | POVOS奔腾上加水加湿器 | PJ8005 | 052 | humidity, switch, temperature | faultDetection, gear |
| `27NV` | 箭牌浴霸 | AYB001-HM | 035 | status, switch, temperature | aromaSwitch, autoWarmWindSwitch, nightLightSwitch, standbySwitch, sterilizationSwitch, ventilateSwitch, warmWindGear, windSwitch |
| `27QC` | 0-10V单色温调光器 | BL2230R | 044 | switch1, switch2, switch3 | brightness1, brightness2, brightness3, brightness4, fadeTime1, fadeTime2, fadeTime3, fadeTime4, faultDetection, switch4 |
| `27QD` | 开关执行器 | BL2228R | 01B | switch1, switch2, switch3 | faultDetection, switch4, switch5, switch6, switch7, switch8 |
| `27W6` | 吸顶式红外人体移动光照传感器 | BL5015R | 03E | luminance, status, switch | — |
| `283O` | UBOT温湿度计Mini | MHO-C121 | 04E | battery, humidity, temperature | highesHumidity, highesTemperature, lowestHumidity, lowestTemperature, temperatureUnit, timeHumidity, timeTemperature |
| `286J` | LeveTop温感美妆蛋 | DZ04B | 0EA | battery, status, switch | currentmoderecord, deepcleaning, gear, rejuvenateeyes, ultramicropenetration |
| `28BF` | 无线续航自然风风扇 | FL-12138DRR(WF)-1W | 029 | fan, mode, switch | endTime |
| `28OH` | 清易智慧无线洗地机 | QYXDJ02B | 19F | battery, status, switch | AllProperties, DailyAverage, DryConfig, EveryDay, FactoryReset, FanLevle, Fault, MachineState, Speaker, cleanwaterboxstate, commonFilterElement1, commonFilterElement2, commonMode1, selfclean, sewageboxstate |
| `28QS` | 博思迪洁面仪 | D-1601 | 0E8 | mode, status, switch | Lowbatterywarning, Reversesetting, firmwareupdate, state |
| `291J` | 澳柯玛智能电热水器B116 | FCD-60B116 | 027 | mode, switch, temperature | PowerSaving, code, cutcapacity, faultDetection, frequency, prestart, preswitch, sterilize, workstate |
| `292G` | 香之君便携咖啡机 | PCM03 | 0B9 | action, mode, switch | currentTemperature, deviceAppoint, devicePower, deviceState, exceptionReporting, history, setting, timedReminders |
| `294I` | 法狮龙灵悦S智能浴霸 | LDXD-2A-S | 035 | lightSwitch, switch, temperature | BYZT, LY, commonFaultDetection, drySwitch, leftTime, setWorkTime, ventilateSwitch, warmWindGear, windSwitch |
| `29BE` | 澳柯玛智能电热水器B115 | FCD-60B115 | 027 | mode, switch, temperature | CapacityIncrease, Cleanup, PowerSaving, code, cutcapacity, faultDetection, prestart, preswitch, sterilize, workstate |
| `29DH` | 澳柯玛智能电热水器W118 | FCD-60W118 | 027 | mode, switch, temperature | Cleanup, code, cutcapacity, faultDetection, frequency, prestart, preswitch, sterilize, workstate |
| `29HQ` | MOLONEY莫洛尼电壁炉 | YN-Q-001 | 06A | mode, switch, temperature | BurningSound, CBedLight, CanelTimer, CountDown, faultDetection, firehigh, gear |
| `29MJ` | 护腰美姿椅 | EW-311H | 05F | mode, switch, temperature | currentTemperature, timeRemaining |
| `29Q3` | 箭牌智能毛巾架AKM011-HM | AKM011-HM | 0BA | fan, status, switch | disinfect, drying, dryingTime, nightlightSwitch, sensingSwitch, swingSwitch, windSwitch |
| `29WV` | 绿克扫拖一体机HS1 | YM-HS1-W08 | 031 | action, mode, status | areaSetting, cleanRecord, commonFaultDetection, deviceStatus, edgeElement, hepaElement, mapService, musicPackage, ossSN, path, remoteControl, rollElement, scheduleService, startClean |
| `29YQ` | 24W双色温恒流控制装置 | BL-LIGHT-CWT | 11A | brightness, cct, switch | — |
| `2A0X` | 博世微蒸烤一体机 | CPA569GS0W | 024 | mode, status, switch | childLock, control, devDoor, faultDetection, favorite, leftTime, localFood |
| `2A26` | eue头部按摩器 | EUET001-TQ | 0CA | battery, mode, switch | strength |
| `2A8P` | sraum4路开关面板 | SP-A1Z8-RaF | 005 | switch1, switch2, switch3 | scene1, scene2, scene3, scene4, switch4 |
| `2A8Q` | sraum3路开关面板 | SP-A1Z7-RaF | 005 | switch1, switch2, switch3 | scene1, scene2, scene3, scene4 |
| `2A96` | 清易智慧扫拖机器人 | QYSDJ01 | 031 | action, mode, status | areaSetting, cleanRecord, commonFaultDetection, deviceStatus, edgeElement, hepaElement, mapService, musicPackage, ossSN, path, remoteControl, rollElement, scheduleService, sensor, startClean |
| `2A9A` | D-Controls面板 | Panel | 005 | switch1, switch2, switch3 | switch4 |
| `2A9O` | 欧派智能声控晾衣机 | OP-L1009X | 028 | action, lightSwitch, status | airDry, disinfect, drying, motorBlock |
| `2AAL` | 艾特三键开关 | ZS132 | 005 | switch1, switch2, switch3 | — |
| `2ABU` | 永林色温驱动 | PLH-LB2X40-15-CT1 | 044 | brightness, cct, switch | — |
| `2AD0` | 西顿24W调色模块 | SWP01-QL-24W-2 | 044 | brightness, cct, switch | — |
| `2AJH` | 瑞美燃气容积式热水器 | RGS/G | 027 | status, switch, temperature | energysavingfunction, faultDetection, hotwatercirculation, instantfunction, settemperature, smartfunctions, timing1, timing2 |
| `2AJR` | 瑞美商用电热水器 | CEA | 027 | status, switch, temperature | energysavingfunction, faultDetection, powerregulation, timing1, timing2 |
| `2AM3` | 乐喝净饮机 | CL-24JR-B | 060 | mode, status, temperature | BoilTea, Caudle, DrinkWaterToday, HeatUpWater, KeepWarm, MaxOfWater, MiddleOfWater, MinOfWater, TR, Wash, commonFilterElement1, commonFilterElement2, faultDetection, leftTime, preTimeStart, presetSwitch |
| `2AN7` | 鸿雁DLT调光开关U2 | U2-86KTGS150-ZXP(HW) | 01B | brightness, cct, switch | — |
| `2AN9` | 鸿雁三键智能开关U2 | U2-86K31ND10-ZD(HW) | 005 | switch1, switch2, switch3 | indicator |
| `2ANP` | 德姆勒取暖器 | WAQ-TDZ04A | 06A | childLockSwitch, switch, temperature | ENDTIME, HeaterGear, backlight |
| `2AOY` | 鸿雁双路智能开关模块 | IHC1239HW | 064 | switch, switch1, switch2 | indicator |
| `2AR1` | 调色温灯（照明调光器） | CP2006H | 01B | brightness, cct, switch | — |
| `2AVX` | 三思青春版台灯 | C22RL-TD10-5W | 046 | brightness, colourMode, switch | tomatoClk |
| `2AW2` | 智能恒温水壶-高配 | AH-H001A | 09A | mode, status, temperature | Chlorine, LongBoiling, PowerSwitch, PoweroffMemory, TemperatureAdjustment, WaterMonitoring, preTimeStart, presetSwitch |
| `2AW4` | usmile星光智能声波电动牙刷 | P1001 | 073 | battery, mode, status | LED, brushHeadLife, brushingHistory , direction, intensity, score, splashProof, startPositon |
| `2AW5` | usmile-U悦智能声波电动牙刷 | X10 | 073 | battery, mode, status | LED, brushHeadLife, brushingHistory , direction, handheldAwaken, intensity, score, splashProof, startPositon |
| `2AWI` | 万家乐燃气热水器16LX7 | JSQ30-16LX7 | 027 | mode, switch, temperature | cruiseSterilization, faultDetection, gesture, heat, orde, pressurize |
| `2B2H` | 晾品智能晾衣机HW70 | HW70 | 028 | action, lightSwitch, status | — |
| `2B5A` | MixSwitch超级智能开关-三开 | T40W3Z | 005 | switch1, switch2, switch3 | — |
| `2BDI` | 吸顶式毫米波人体存在光照传感器 | BL5002R | 03E | luminance, status, switch | — |
| `2BDZ` | 吸顶式PM2.5三合一传感器 | BL5012R | 006 | humidity, switch, temperature | PM10, PM2.5 |
| `2BE8` | 麦乐克无线温湿度传感器 | MIR-TE100 | 04E | battery, humidity, temperature | — |
| `2BFK` | FSL智感小夜灯 | FSL-XYD | 01A | battery, brightness, status | Light, Lm, NightLightMode, motionDetected, online |
| `2BGL` | 三雄极光Pak智能射灯 | PAK565217 | 01B | brightness, lightMode, switch | — |
| `2BMZ` | 领普双键单火开关MESH | Q4S-BLE-W2(HW) | 005 | switch, switch1, switch2 | button1, button2, mode1, mode2 |
| `2BOF` | 堡丽调色温灯（照明调光器） | BL2006H | 01B | brightness, cct, switch | — |
| `2BOI` |  | BL2202H | 01B | brightness, cct, switch | — |
| `2BOK` | 堡丽调色温灯带（灯带调光器） | BL2201H | 01B | brightness, cct, switch | — |
| `2BOT` |  | BL8231H | 030 | fan, pm25, switch | — |
| `2BWB` | 欧派油烟机 | CXW-180-E981X | 021 | lightSwitch, mode, switch | gear |
| `2BXP` | 觅石智能IH电饭煲3L | RC02 | 026 | action, mode, status | YSP, faultDetection, leftTime, preTimeEnd, presetSwitch, setWorkTime, warmDuration, warmSwitch, workTime |
| `2C1E` | 小质即热饮水机 | YR-1201TN | 06F | childLockSwitch, mode, status | currentOutlet, faultDetection, waterLevel |
| `2C1N` | 小狗擦地吸尘器T12 Duke Rinse WIFI | T12 Duke Rinse(WIFI) | 069 | battery, status, switch1 | commonFilterElement1, commonFilterElement2, commonTask1, faultDetection, leftTime, shiftmode1, workTime |
| `2C40` | 2He小夜喵智能照明消毒灯 | LAMP-2LD | 01B | battery, colourMode, lightMode | LEDSwitch, UVSwitch, batteryStatus, lightbright |
| `2C5J` | 凯迪仕晾衣机 | HKL20-1Y | 028 | action, lightSwitch, status | — |
| `2C7W` | 西蒙三位智能开关 | 70E840 | 005 | switch1, switch2, switch3 | BackLightMode |
| `2C7X` | 西蒙四位智能开关 | 70E841 | 005 | switch1, switch2, switch3 | BackLightMode, switch4 |
| `2C87` | 西蒙新风开关 | 70E7028 | 030 | fan, switch, temperature | BackLightLevel, BypassSwitchFunction, BypassSwitchMode, FilterScreenFuction, FilterScreenPeriod, faultDetection |
| `2CCL` | 金鱼音乐智能电动牙刷 | UE02 | 073 | battery, mode, status | brushHeader, brushingHistory, lockMode, music, restDays, setWorkTime, spraySwitch |
| `2CK1` | 叶绿体单火三路墙壁开关 | SWL-XA03-ZB | 005 | switch1, switch2, switch3 | — |
| `2CQF` |  | BL8027R | 064 | switch, switch1, switch2 | backlightMode |
| `2CQU` | 9W双色温射灯驱动器 | BL2207R | 01B | brightness, cct, switch | faultDetection |
| `2CTN` | 艾优智能电动牙刷 | P7-H | 073 | battery, mode, status | Brushingmode, brushingHistory, custom |
| `2CVI` | 三键智能开关面板时尚版 | BL8033R | 064 | switch1, switch2, switch3 | — |
| `2D50` | Mynt智能香薰机 | MC-3175 | 04C | colour, lightSwitch, switch | atomization, autochange |
| `2D59` | 黑创hrlchure智能晾衣机 | hw63pro | 028 | action, lightSwitch, status | airDry, disinfect, drying |
| `2D6F` | 双色温灯带驱动器 | BL2206R | 01B | brightness, cct, switch | faultDetection |
| `2DCA` | HEIMAN智能红外光照度传感器 | HS1MIS-BH | 03E | battery, luminance, status | delayTime, motionDetected, sensitivity, temperAlarm |
| `2DCY` | 华为智选 杜亚智能窗帘 | H1 | 01C | action, mode, opener | calibrate, faultCode, favorite, manualSwitch, memoryControl, reverse |
| `2DDK` | 科西逸尔无叶风扇 | A2H | 029 | fan, mode, switch | anion, lock, onOffBeep, reserveStart, screenLight, shake, timedOff |
| `2DMC` | 二路智能开关 | JM-6012 | 005 | switch, switch1, switch2 | backlight |
| `2DMK` | 力博得智能声波牙刷 悦沁 | LBT-203557A | 073 | battery, mode, status | audioSwitch, brushSettings, brushStart, brushingHistory, brushingHistorys, guide, modes, postHistorys, setTmie, weekHistorys |
| `2DQQ` | 贝昂落地式循环扇 | FZS2-Pro | 029 | mode, switch, temperature | light, lock, lrwind, speed, timingOff, timingOn, udwind |
| `2DRJ` | 澳萌破壁机 | AI-PB07 | 05A | action, status, switch | cupStatus, faultDetection, gear, holdingTemp, holdingTime, leftTime, modeA, modeB, preTimeStart, presetSwitch, temp |
| `2DSE` | 拉孚二路智能开关 | HL202R | 005 | switch, switch1, switch2 | — |
| `2DV1` | 三键智能开关面板尊享版 | BL8373R | 064 | switch1, switch2, switch3 | — |
| `2DXB` | 龙泉智家二路墙壁开关 | LQ-K02H | 005 | switch, switch1, switch2 | — |
| `2DYF` | 亚摩斯多功能电压力锅AS-YDG253Z | AS-YDG253Z | 074 | action, mode, status | faultDetection, food, leftTime, preTimeStart, presetSwitch, settime, workTime |
| `2E4A` | 熊小夕便携式奶茶机 | XL-X515 | 172 | mode, status, temperature | Boilwater, Milktea, commonMemorySwitch1, healthtea, remainingTime, stirMode |
| `2ELR` | 小狗擦地吸尘器 | T12 Earl Rinse(WIFI) | 069 | battery, status, switch1 | commonExecution1, commonFilterElement1, commonFilterElement2, faultDetection, leftTime, shiftmode1, workTime |
| `2ENG` | 亚摩斯星耀开关双键 | ZJ-KG27H | 005 | switch, switch1, switch2 | — |
| `2F5U` | 亚摩斯智能循环扇 | AS-FM528D | 029 | fan, mode, switch | anion, timingOff, timingOn |
| `2F6R` | 达伦智能台灯3 | DL-3HW | 046 | brightness, lightMode, switch | fadeTime, indicator, lightStatus, nightWakeup, progressTurnOff, record, tomatoClk1, tomatoClk2, tomatoClk3, tomatoClk4 |
| `2F7Q` | 绿田创T5锂电洗车机 | TRON-T5 | 13B | battery, mode, status | ProductIntroduction, UsageLog, connectionStatus, faultCode |
| `2F8A` | 绿田勃朗宁B4锂电洗车机 | BROWNING-B4 | 13B | battery, mode, status | ProductIntroduction, UsageLog, connectionStatus, faultCode |
| `2FAO` | 协议地暖 | MC3-Heater | 101 | mode, switch, temperature | capabilityset, controlStrategy, faultDetection, heatingCoolingMode, panelLocation |
| `2FC2` | 造梦者新风机 | DM-XF220-1S | 030 | childLockSwitch, fan, switch | filterElement1, filterElement2, filterElement3, filterElement4, light, sound |
| `2FCX` | 博顿物联二开 | BD-S6B002 | 005 | switch, switch1, switch2 | — |
| `2FEN` | 智能刀筷消毒烘干架 | YSXDJ005SSHI | 100 | alarm, mode, status | childLock, knifeShelfSwitch, presetSwitch, remainingTime |
| `2FIO` | 小适智能电动剃须刀 | FH-305GY | 170 | mode, status, switch | Alarm, Class, Cleaning, CurrentPower, Feedback, Intelligent, NormalMode, Service, ShavingSpeed, ShavingTime, Upgrade, UsingTime |
| `2FJ5` | 贝昂落地式循环扇 | FZS-Lite | 029 | fan, mode, switch | timingOff, timingOn |
| `2FS0` | 箭牌智能浴缸 | AW1762SQ-HM | 297 | status, switch, temperature | WaterInlet, gear |
| `2FSN` | 720智能多效除味器 | RC200s | 1A1 | childLockSwitch, mode, switch | bright, cumulativetime, lightSensor, roomArea |
| `2FY4` | 洒拖派 0 Pro 自动擦窗机 | 0 Pro | 0F7 | action, mode, status | commonFaultDetection, deviceStatus, statusA, voicePack, volume, waterSpray, windowSide |
| `2G3X` | 真空吸尘器 | KXCQ-1207W-T | 069 | battery, mode, status | filterElement |
| `2G5Z` | 西蒙睿极智能吸顶灯 | LCR3601-HW | 112 | colourMode, lightMode, switch | brightne, colorTemperature, progressTurnOn, sleepMode |
| `2GB1` | 温湿度传感器 | MIR-TE100 | 04E | battery, humidity, temperature | commonFaultDetection |
| `2GB4` | 红外人体移动光照传感器 | MIR-IR100 | 049 | battery, luminance, pir | commonFaultDetection |
| `2GCE` | 美邦空调 MAC35V3YHR | MAC35V3YHR | 012 | mode, switch, temperature | Disinfection, Economy, Horizontal, PtcHeat, ScreenDisplay, Sleep, StrongMode, Vertical, Wind, faultDetection |
| `2GIP` | A.O.史密斯燃气热水器零冷水系列 | JSQ31-VJSH | 124 | status, switch, temperature | TimeFunction, TotalTime, boostMode, curWater, faultDetection, gasStatus, inletTemperature, statusOfMachine, totalGas, totalWater, zeroColdMode, zeroColdSwitch |
| `2GKV` | 美森智能专业理发器 | WHS2 | 0E9 | battery, mode, status | AvailableTime, CutterHeadAlarm, Reconnect, RemainingDaysCutterHead, ResetCutterHead, TotalTimes |
| `2GSG` | 康夫KF-3149多功能负离子吹风机 | KF-3149 | 0E4 | mode, status, switch | Gear, Introduction, UserDefineMode, UserDefineName |
| `2GVK` | 狄耐克智能二路开关面板 | SH-WDQ-LGT201 | 005 | switch, switch1, switch2 | — |
| `2GY5` | 欧普暖芯浴霸 | JF-HWBP10i | 035 | fan, lightSwitch, temperature | autoWarmWindSwitch, commonFaultDetection, drySwitch, leftTime, sceneMode, standbySwitch, timeGear, ventilateSwitch, windSwitch |
| `2H4H` | 智小金智能柜内灯电源驱动 | ZXJ-N-LC01-60W | 226 | brightness, colourMode, switch | — |
| `2H5T` | Yours智能负离子电吹风 | 6286 | 0E4 | mode, status, switch | Children, Custom, Haircare, Time, Upgrade |
| `2H5U` | 净颜温感洁面仪 | SKB-1811 | 0E8 | mode, status, switch | Records, Remaining, TimeSet, Upgrade, Vibrating, batteryLevel |
| `2H5Z` | 映趣电动剃须刀MOCHA S | MOCHA S | 170 | mode, status, switch | BatteryLevel, Cleanfunction, NetworkStatus, history, manipulate |
| `2H7W` | RND M1电动滑板车 | M1 | 094 | battery, mode, status | Cruisecontrol, Powerstart, Themileage, bt.connection, currentspeed, lock, shutdown1, unit, update1 |
| `2H9J` | 商贤智能取暖器S8 | S8 | 06A | childLockSwitch, switch, temperature | fire, heat, heatmain, mytimer |
| `2HB1` | 多功能射频胶原蛋白仪 | KD9916H | 0EA | battery, status, switch | Report, Time, btstatus, gear, remainingtime, skinMode |
| `2HB9` | 得力多功能无线吸尘器 | DL881120S | 191 | alarm, battery, status | cumulativeTime, deviceControl, lastTime, suction |
| `2HCI` | 艾芬达电热毛巾架 | GD18-B | 0BA | mode, switch, temperature | consumepower, cumulativeduration, power, reset, timing, weektime |
| `2HGB` | 意诺开关控制器 | SMART-SW08 | 064 | switch1, switch2, switch3 | switch4, switch5, switch6, switch7, switch8 |
| `2HMR` | 磨脚器 | BCM-1138T | 2A6 | battery, mode, switch | duration, history, personalCustom, personalnumber, remainingTime, report, severtime, userecord |
| `2HQI` | 四季沐歌智能晾衣机H100S | MY-LQYH100S | 028 | action, lightSwitch, status | airDry, commonFaultDetection, disinfect, drying |
| `2HR7` | 西蒙二位智能开关 | 58E8202 | 005 | switch, switch1, switch2 | commonFaultDetection, indicator, switchStatus |
| `2HYV` | 金莱特多功能户外灯 | KN-L4361 | 189 | battery, mode, switch | light |
| `2I2E` | 晾霸智能晾衣机 | HW50 | 028 | action, lightSwitch, status | airDry, airDryRemTime, airDryTime, disinfect, disinfectRemTime, disinfectTime, dryRemTime, dryTime, drying |
| `2I4I` | 可拆卸晾衣架踢脚线AHR4146WKS | AHR4146WKS | 06A | childLockSwitch, switch, temperature | OSD, gear, timing |
| `2I7C` | 欧普蓝牙Mesh双色温灯带驱动 | OP-DY220/200-24CV/2-WB | 226 | brightness, cct, switch | commonFaultDetection, toggleSwitch |
| `2I7K` | 欧普蓝牙Mesh双色温筒射灯驱动 | OP-IDSCC0140420B2-01 | 226 | brightness, cct, switch | commonFaultDetection, toggleSwitch |
| `2I8S` | 直流变频石墨烯踢脚线AHR5244KS | AHR5244KS | 06A | childLockSwitch, switch, temperature | OSD, ReserveLeftTime, gear |
| `2IAB` | 罗曼智能电动牙刷HT3pro | HT3pro | 073 | battery, mode, status | Brushhead, OTA, brushingHistory, brushstrength, initPosition, partitionreminder, personalizedservice, spraySwitch, voiceGuidance, workGuidance, workhour |
| `2IEX` | 锐亿剃须刀373A | RS373A | 170 | battery, mode, status | deviceTime, experience, frequency, grade, implemented, seekDevice, userTime, userecord |
| `2IF0` | 锐亿剃须刀373B | RS373B | 170 | battery, mode, status | btConnection, deviceTime, frequency, implemented, seekDevice, userTime, userecord |
| `2IK3` | 企一照明筒射灯驱动设备(蓝牙) | QYHW15B | 226 | brightness, cct, switch | commonFaultDetection, relBrightness, toggleSwitch |
| `2IK7` | 企一照明低压双色温灯带蓝牙驱动 | QYHW80B | 226 | brightness, cct, switch | commonFaultDetection, relBrightness, toggleSwitch |
| `2IN4` | 九阳太空智能空气炸锅 | KL55-V563 | 063 | status, switch, temperature | cookTimes, degerming, faultDetection, independentRecipes, leftTime, preTimeEnd, preTimeStart, presetSwitch, recipes, setWorkTime, start, startCloudMenu, workTime |
| `2INP` | 艾家智能二位开关 | Z1K2 | 005 | switch, switch1, switch2 | lightness, switchStatus |
| `2IU6` | 西蒙四位智能场景开关 | 58E8208 | 005 | switch1, switch2, switch3 | commonFaultDetection, deviceStatus, indicator, mode1, mode2, mode3, mode4, sceneButton1, sceneButton2, sceneButton3, sceneButton4, switch4 |
| `2IU8` | 西蒙三位智能场景开关 | 58E8207 | 005 | switch1, switch2, switch3 | commonFaultDetection, deviceStatus, indicator, mode1, mode2, mode3, sceneButton1, sceneButton2, sceneButton3 |
| `2IWO` | 洒拖派 0 自动擦窗机 | 0 | 0F7 | action, mode, status | commonFaultDetection, deviceStatus, statusA, waterSpray, windowSide |
| `2J1U` | 奥克斯剃须刀 | AS299 | 170 | battery, mode, status | bladeClean, bladeCleanTime, bladeUseTime, btConnection, highTemp, lock, surplusCount, surplusTime |
| `2J24` | 电动剃须刀 | SH08 | 170 | battery, mode, status | bladeCleanTime, btConnection, lock, remaining, rest, surplusCount, usetime |
| `2JC9` | 欧普蓝牙mesh双色温磁吸灯驱动 | OP-IESVC1600024E2-01 | 226 | brightness, cct, switch | commonFaultDetection, toggleSwitch |
| `2JDD` | 欧普WiFi双色温驱动 | OP-DY220/45-58CV-CB-T | 226 | brightness, cct, switch | commonFaultDetection |
| `2JJG` | 趣丸悬浮剃须刀 | LQ-TXD01 | 170 | battery, mode, status | DevStatus, NTP, commonFilterElement1, commonMode1, commonMode2, endurance, record |
| `2JMD` | 无叶电吹风 | X3H | 0E4 | mode, status, temperature | RealTemp, currentSpeed, speed |
| `2JOO` | 锐亿剃须刀RS392 | RS392 | 170 | battery, status, switch | Applications, Currenttime, Finddevices, Gear, History1, History2, History3, History4, Introduction, Power, Report |
| `2JRH` | 消毒柜ZTD100S-02-X20.i | ZTD100S-02-X20.i | 0D5 | action, status, switch | cabinetDoor, cabinetMode, cabinetRemainingTime, faultDetection |
| `2JS6` | 可移式LED灯具 | TD-67 | 046 | brightness, mode, switch | colorTemp, countdown |
| `2K4Z` | FUNSNAP Capture 2云台 | Capture2 | 0EC | battery, mode, status | lowbattery |
| `2K7Y` | 杜亚智能窗帘 DH11 | DH11 | 01C | action, battery, opener | capacity, changeDirection, commonFaultDetection, switchSpeed |
| `2K81` | 易百珑六键智能开关 | EWS56K-HM | 201 | switch1, switch2, switch3 | CleanPair, Pair, led, memorySwitch, mode1, mode2, mode3, sceneButton1, sceneButton2, sceneButton3, sceneButton4, sceneButton5, sceneButton6 |
| `2KFI` | 酷轻松石墨烯热敷按摩支撑护腰带 | JY(Z)10-HMBDH-01 | 17D | battery, mode, status | CurrentTEMP, Shutdown, Thermoregulation, Timedshutdown, Timeremaining, Vibrationgear, service, suspend |
| `2KQI` | 希箭IOT智能镜柜 | 2112H75-02 | 04A | brightness, lightMode, lightSwitch | defoggingSwitch, workStatus |
| `2KWO` | 欧普智能射灯筒灯驱动器 - 6W | OP-IFSCH0060170H2-01 | 226 | brightness, cct, switch | fadeTime, fadeTimeSetting, faultDetection, lightCurveSetting, memorySwitch, subProduct |
| `2KWR` | 欧普智能射灯筒灯驱动器 - 25W | OP-IFSCH0250600H2-01 | 226 | brightness, cct, switch | fadeTime, fadeTimeSetting, faultDetection, lightCurveSetting, memorySwitch, subProduct |
| `2KXR` | 霍尼韦尔红外人体移动光照传感器 | HZBS-H-PIR | 049 | battery, luminance, mode | commonFaultDetection, motionDetected, reminder, sensitivity |
| `2KXS` | 霍尼韦尔红外和超声波双鉴人体移动光照传感器 | HZBS-H-PIRUS1 | 049 | battery, luminance, mode | commonFaultDetection, motionDetected, reminder, sensitivity |
| `2L2P` | 凡家智能暖腹腰带 | WL-i17 | 17D | alarm, mode, status | countdown, cuTemperature, heat, light, power, unit |
| `2L4O` | 西顿巴赫PLC磁吸灯 | CDN-CX01 | 226 | brightness, cct, switch | fadeTime, fadeTimeSetting, faultDetection, lightCurveSetting, memorySwitch |
| `2L8N` | 锐亿智能剃须刀RS393 | RS393 | 170 | battery, mode, status | bladeCleanTime, bladeCongestion, bladeUseTime, dataenv, lock, seekDevice, surplusCount, surplusTime |
| `2LAD` | meipont空调挂机 | MAC35V1Y3HR | 012 | mode, switch, temperature | Disinfection, Economy, Horizontal, PtcHeat, ScreenDisplay, Sleep, StrongMode, Vertical, Wind, faultDetection |
| `2LAI` | 锐亿智能剃须刀RS293 | RS293 | 170 | battery, mode, status | bladeCleanTime, bladeCongestion, bladeUseTime, dataenv, lock, seekDevice, surplusCount, surplusTime |
| `2LBW` | 科西无叶风扇A4-H | A4-H | 029 | fan, mode, switch | LARangle, anion, childLock, onOffBeep, restScreen, startTime, timeOff |
| `2LF3` | FUNSNAP Capture 5云台 | Capture 5 | 0EC | battery, mode, status | lowbattery |
| `2LG4` | 智能塔扇 | M47 | 029 | battery, fan, switch | Standby, Swing, endTime |
| `2LHX` | 厨下净水 | MC3-Cj | 02D | mode, status, temperature | faultDetection, filterElement1, filterElement2, inputTds, outputTds, totalPurifyWater |
| `2LHY` | 燃气热水器 | MC3-Rr | 124 | status, switch, temperature | curGas, faultDetection, inletTemperature, presetSwitch, totalGas, zeroColdMode, zeroColdSwitch |
| `2LLE` | meipont空调挂机 | MAC26V1Y3HR | 012 | mode, switch, temperature | Disinfection, Economy, Horizontal, PtcHeat, ScreenDisplay, Sleep, StrongMode, Vertical, Wind, faultDetection |
| `2LYW` | 松下干衣机 NH-VH102FP | NH-VH102FP | 0D7 | childLockSwitch, mode, status | commonFaultDetection, leftTime, newAction, newStatus, newSwitch |
| `2M5M` | 香百年智能香薰机Pro | XH-002 | 0DE | battery, mode, switch | FirmwareUpdate, autoConnect, durationtime, gear, margin, numberofcycles, scent |
| `2M60` | 除菌模块-6恒 | MC3-CJMK | 013 | fan, mode, switch | UVSwitch, anionSwitch, capability, elapsedTimeMode, faultDetection, filterElement, filterElement1, filterElement2, filterElement3 |
| `2M6R` | 松下语音浴霸照明款 | FV-54BET2C | 035 | action, fan, status | commonFaultDetection, coolDrySwitch, drySwitch, leftTime, lightingMode, nightLightSwitch, sterilizationSwitch, timeGear, ventilateSwitch, warmWindMode, windDirectionSet, windKindSet |
| `2M6Z` | 松下隐蔽式浴霸 | FV-45BH2C | 035 | action, fan, status | commonFaultDetection, coolDrySwitch, drySwitch, gasCheckHas, leftTime, lightingMode, odorsensingSwitch, speakerSet, sterilizationSwitch, timeGear, ventilateSwitch, warmWindMode, windDirectionSet, windKindSet |
| `2M7Q` | 松下语音浴霸无照明款 | FV-54BE2C | 035 | action, fan, status | commonFaultDetection, coolDrySwitch, drySwitch, leftTime, sterilizationSwitch, timeGear, ventilateSwitch, warmWindMode, windDirectionSet, windKindSet |
| `2MDV` | 杜亚PLC版开合帘电机 尊享款H2 | H2 | 01C | action, lightSwitch, opener | changeDirection, faultDetection, placeMemory, selfCheck, speed, switchSpeed |
| `2MGW` | 佳普乐致雅智能浴霸 | BH1ZY-01N | 035 | lightSwitch, status, temperature | CirculationTime, DevAction, UserMode, WarmWindTime, WindTime, commonExecution1, drySwitch, nightLightSwitch, ventilateSwitch, warmWindMode, windSwitch |
| `2MGX` | 佳普乐致尚智能浴霸 | BH1ZS-01N | 035 | lightSwitch, status, temperature | CirculationTime, DevAction, UserMode, WarmWindTime, WindDirection, WindTime, commonExecution1, drySwitch, nightLightSwitch, swingSwitch, ventilateSwitch, warmWindMode, windSwitch |
| `2MHO` | 九牧智能晾衣机A6099 | LA6099-000/2K1-1 | 028 | action, lightSwitch, status | airDry, airDryRemTime, airDryTime, commonExecution1, disinfect, disinfectRemTime, dryRemTime, dryTime, drying, position, systemFault, workStatus |
| `2MNJ` | 四合一空气质量检测仪 | PMT600-SK-PND | 006 | humidity, pm25, temperature | co2, pm10, reportSetting, switchNightLight |
| `2MOU` | 心智悦环境控制器C1 | MJTC-C1 | 10D | humidity, switch, temperature | airKeyGear, airKeyMode, faultDetection |
| `2MPF` | 礼意久久暖腰带柴犬款 | WZT3V206 | 17D | alarm, battery, switch | BLEstatus, CurrentTemperature, countdown, hot, shake, shutdown |
| `2MRT` | meipont空调柜机 | MAC72V1KSR | 012 | mode, switch, temperature | Disinfection, Economy, Horizontal, PtcHeat, ScreenDisplay, Sleep, StrongMode, Vertical, Wind, faultDetection |
| `2MU7` | JoinOne冷暖循环加湿器 | HW-4300(WF) | 052 | humidity, mode, switch | UVSwitch, atomization, fixedTime, gear, humidification, light, remainAppoTime, remainWorkTime, reservation, waterGear |
| `2MUB` | SORONTEK 智能双色射灯 | SR-TH-019-12W | 21D | brightness, lightMode, switch | coolwarm |
| `2MVH` | meipont美邦空调挂机 | MAC35V1THR | 012 | mode, switch, temperature | Disinfection, Economy, Horizontal, PtcHeat, ScreenDisplay, Sleep, StrongMode, Vertical, Wind, faultDetection |
| `2MVJ` | meipont美邦空调挂机 | MAH35VTHR | 012 | mode, switch, temperature | Disinfection, Economy, Horizontal, PtcHeat, ScreenDisplay, Sleep, StrongMode, Vertical, Wind, faultDetection |
| `2MX1` | 北斗浮雕地球仪 | G2516AI | 197 | brightness, mode, switch | Battery, ChargeStatus |
| `2MZW` | 智能控制器-盛和 | MC3-ZK5 | 012 | fan, mode, switch | commonFilterElement1, filterElement, sceneMode |
| `2N1J` | 智掂LED光疗面罩 | GD-PE-6001  | 0EA | action, mode, status | alertService, commonFaultDetection, firmware, plan, remain, workRecord |
| `2N3T` | 欧普PLC磁吸轨道灯 | OP-IDNCD0100300P2 | 226 | brightness, cct, switch | fadeTime, fadeTimeSetting, faultDetection, lightCurveSetting, memorySwitch, relBrightness |
| `2N53` | 嘿码护发高速吹风机 | BC100 | 0E4 | mode, status, temperature | speed |
| `2N59` | 晾霸智能晾衣机Q2烘干王 | Q2-1304D10XFHY1-DC | 028 | action, lightSwitch, status | airDry, airDryRemTime, airDryTime, disinfect, disinfectRemTime, disinfectTime, dryRemTime, dryTime, drying |
| `2N5A` | 晾霸智能晾衣机Q1 | Q1-1104D5FHY1-22DC | 028 | action, lightSwitch, status | airDry, airDryRemTime, airDryTime, dryRemTime, dryTime, drying |
| `2N5X` | 快轮智能电动滑板车1s | 1s | 094 | action, battery, switch | devCmd, devInfo, deviceTime, eventInfo, finddevice, gear, momentInfo, motorLock, paraSet |
| `2N6O` | meipont美邦燃气热水器 | JSQ31-L16X5 | 124 | status, switch, temperature | antifreezeStatus, faultDetection, flameStatus, waterboost, watercontrol, waterloop |
| `2N8I` | 好太太智能晾衣机 1156H | GW-1156H(HM) | 028 | action, lightSwitch, status | commonFaultDetection |
| `2N8J` | 好太太智能晾衣机 1295H | GW-1295H(HM) | 028 | action, lightSwitch, status | airDry, airDryRemTime, airDryTime, commonFaultDetection, disinfect, disinfectRemTime, disinfectTime, dryRemTime, dryTime, drying |
| `2N9B` | 优慧家燃气热水器HA241 | JSQ45-HA241 | 124 | status, switch, temperature | burningTime, curWater, custom, faultDetection, inletTemperature, totalGas, totalWater |
| `2N9C` | 优慧家零冷水燃气热水器HA168GR | JSQ30-HA168GR | 124 | status, switch, temperature | boost, burningTime, curWater, custom, faultDetection, inletTemperature, preheat, pretask, totalGas, totalWater |
| `2N9D` | 优慧家燃气热水器HB162G | JSQ30-HB162G | 124 | status, switch, temperature | burningTime, curWater, custom, faultDetection, inletTemperature, lock, totalGas, totalWater |
| `2NBY` | meipont美邦空调挂机 | MAC26V1THR | 012 | mode, switch, temperature | Disinfection, Economy, Horizontal, PtcHeat, ScreenDisplay, Sleep, StrongMode, Vertical, Wind, faultDetection |
| `2NEB` | meipont美邦燃气热水器 | JSW32-16LM7 | 124 | status, switch, temperature | antifreezeStatus, faultDetection, flameStatus, priority, zeroColdMode |
| `2NEY` | meipont空调柜机 | MAC72V1NNSR | 012 | mode, switch, temperature | ECOswitch, PtcHeat, faultDetection, freshAirgear, light, selfCleanswitch, sleeping, strong, sweepHorizon, sweepVertical |
| `2NF2` | meipont空调柜机 | MAC51V1KSR | 012 | mode, switch, temperature | ECOswitch, PtcHeat, faultDetection, freshAirgear, light, selfCleanswitch, sleeping, strong, sweepHorizon, sweepVertical |
| `2NHB` | eachone一起玩智能循环扇 | HF-HM-XHS-001 | 029 | fan, mode, switch | Countdownshutdown |
| `2NJN` | meipont空调挂机 | MAC35V1Y1HR | 012 | mode, switch, temperature | ECOswitch, PtcHeat, faultDetection, freshAirgear, light, selfCleanswitch, sleeping, strong, sweepHorizon, sweepVertical |
| `2NLQ` | meipont美邦燃气热水器 | JSQ25-13S7 | 124 | status, switch, temperature | conversion, currentgas, currentwater, faultDetection, flameStatus, function, injection, overgas, overwater, seasons, watercapacity |
| `2NLR` | meipont燃气热水器 | JSQ30-16S7 | 124 | status, switch, temperature | conversion, currentgas, currentwater, faultDetection, flameStatus, function, injection, overgas, overwater, seasons, watercapacity |
| `2NMD` | 云康宝筋膜枪CM40F | CM40F | 0C5 | action, battery, mode | btconnection, countDown, speedOn |
| `2NNL` | 地暖 | B39FH | 101 | mode, switch, temperature | capabilityset, controlStrategy, faultDetection, panelLocation, updateData |
| `2NRD` | dynacare涡轮六叶剃须刀 |  DT-R208 | 170 | battery, mode, status | bladeStatus, duration, history, resetTime, screenAnimation, shavingSpeed |
| `2NS7` | 三思智能护眼吸顶灯HC60 | C22PL-HC-60W-W | 112 | brightness, cct, switch | — |
| `2NSM` | 箭牌智能浴缸AQH1782TQ-HM | AQH1782TQ-HM | 297 | status, switch, switch1 | gear1, massage, targettemperature |
| `2NSO` | 箭牌智能浴缸ANH1782TQ-HM | ANH1782TQ-HM | 297 | status, switch, switch1 | gear1, massage, targettemperature |
| `2NTC` | 倍益康压缩靴 | HACM-PLUS-A1 | 32C | mode, status, switch | electricity, errorTip, higherOrder, massageTime, prefer, pressure |
| `2NTH` | meipont空调柜机 | MAC72V1ESR | 012 | mode, switch, temperature | ECOswitch, PtcHeat, faultDetection, freshAirgear, light, selfCleanswitch, sleeping, strong, sweepHorizon, sweepVertical |
| `2NTI` | meipont空调挂机 | MAC50V1THR | 012 | mode, switch, temperature | ECOswitch, PtcHeat, faultDetection, freshAirgear, light, selfCleanswitch, sleeping, strong, sweepHorizon, sweepVertical |
| `2NXL` | GOHOLITE智能护眼灯GS20 | TL100W | 10F | brightness, lightMode, switch | auxBrightness, mainBrightness, nightWakeup, progressTurnOff |
| `2NZ0` | 九牧智能浴霸JD176P | JD176P | 035 | action, lightSwitch, status | drySwitch, leftTime, leftTimeVen, leftTimeWarm, leftTimeWarmStrong, leftTimeWind, nightLightSwitch, temperatureCur, ventilateSwitch, warmWindMode, windSwitch |
| `2O35` | UCAT智能宠物烘干箱D1 PRO | D1 PRO | 1A4 | lightSwitch, switch, temperature | btcSwitch, childLock, dryMode, petRoom, settime, variety |
| `2O3P` | 月影自然光护眼吸顶灯 | MXDD05C-006 | 112 | cct, lightMode, switch | auxBrightness, auxSwitch, faultDetection, mainBrightness, mainSwitch, progressTurnOff, progressTurnOn |
| `2O4K` | IAM智能净水器Pro | I2200G Pro | 02D | childLockSwitch, status, temperature | city, faultDetection, filterElement1, filterElement2, inputTds, machinePara, noMoreOvernightWater, outputTds, rinseMode, tempMode, water, waterOutletType |
| `2O5D` | 优慧家燃气热水器HB132G | JSQ25-HB132G | 124 | status, switch, temperature | burningTime, curWater, custom, faultDetection, inletTemperature, lock, totalGas, totalWater |
| `2O5Q` | WYC 智能热敷腰带 | WYC-lcnyd | 17D | alarm, switch, temperature | BLEstatus, baterry, countdown, hot, shake, shutdown |
| `2O8Z` | 智能富氢蒸茶壶 | C2 | 1A0 | alarm, status, temperature | boilMode, qingMode, qingTimeLeft, steamMode, steamTimeLeft, warmSwitch |
| `2ODK` | 亚都加湿器SZ550-DZ5(Hi) | SZ550-DZ5(Hi) | 052 | childLockSwitch, humidity, switch | anion, display, dried, faultDetection, gear, level, state, timing |
| `2OH1` | 酷轻松EMS腰带 | HA(E)61-HMBD-02 | 17D | battery, mode, switch | commonFaultDetection, countDown, emsGear, hot, redLightSwitch, shock |
| `2ONW` | 亚都加湿器SC280-QL080(Hi) | SC280-QL080(Hi) | 052 | childLockSwitch, humidity, switch | faultDetection, gear, lamp, level, sleep, state, timing, uv |
| `2OPO` | 星闪温湿度传感器 | MIR-TE100-XS | 04E | battery, humidity, temperature | commonFaultDetection |
| `2OT2` | 膳美师轻食破壁机 | BL3455W | 05A | action, mode, status | deviceSwitch, findDevice, leftTime, preTimeStart, selfClean, workRecord |
| `2OVU` | 国恒G6智能按摩椅 | GH-G6 | 05F | action, status, switch | airbagGear, armSwitch, autoMode, bacAction, countDown, gravityMode, heatGear, lbpMode, legSwitch, manuMode, massTime, massageGear, massmode, movementAction, shoulderAction, shoulderSwitch, soleGear, waistSwitch, workingMode |
| `2OWZ` | BENERGIA制冰饮水机 | YC-1H | 06F | mode, status, temperature | coolSwitch, currentTemp, faultDetection, iceMaking, iceSwitch, output, tanklocation, waterTank |
| `2P0W` | 皇家惠人水暖毯HRS53 | HRS53 | 07C | mode, switch, temperature | commonFaultDetection |
| `2P12` | 达伦智能台灯5i |   DL-01W Pro | 046 | brightness, lightMode, switch | auxBrightness, auxSwitch, delayTurnoff, foldAngles, indicator, mainSwitch, nightWakeup, toggleSwitch |
| `2P39` | 口袋咖啡机 | CN-HM201 | 0B9 | action, battery, temperature | brewingMode, commonFaultDetection, cups, stallProtection |
| `2P6N` | IH 智能方煲 | DRC-8IHS004H | 026 | action, mode, status | faultDetection, keptWarmTime, leftTime, preTimeStart, presetSwitch, setWorkTime, warmSwitch |
| `2P7W` | 保温电热水壶 | WEY-SH101DW | 09A | mode, status, temperature | commonFaultDetection, heatMode |
| `2P8U` | 康丽根牌AVE-T3B型纯水机 | AVE-T3B | 02D | mode, switch, temperature | dayPurifyWater, emptySwitch, faultDetection, filterElement1, height, noMoreOvernightWater, outletWater, output, outputTds, scaleTotal, tempMode, waterFlows |
| `2P9M` | 异形不锈钢壶 | XK13Z-B | 09A | mode, status, temperature | warmSwitch |
| `2P9N` | 智能电热水壶-XK981Z | XK981Z | 09A | mode, status, temperature | warmSwitch |
| `2PIJ` | 佳普乐睿享智能晾衣架 | CD1RX-01S | 028 | action, lightSwitch, status | airDry, airDryRemTime, airDryTime, commonExecution, disinfect, disinfectRemTime, disinfectTime, dryRemTime, dryTime, drying, lightBrightness |
| `2PUL` | 贝昂智能电风扇 | FZS-h | 029 | fan, mode, switch | endTime, orderOn |
| `2PWM` | 华帝小恒星燃气热水器 | JSQ30-HS41-16 | 124 | status, switch, temperature | allDayRecircTempSwitch, boostMode, circulatingTemp, cleanCountdown, cleanSwitch, commonFaultDetection, curGasCon, curWaterVol, ecoSwitch, flameStatus, gasElectricDoubleBreakSwitch, inchingSwitch, increaseCapacitySwitch, maintenanceStatus, recircTempTime, scheduledCold, totalGas, totalWater, zeroColdSwitch, zeroColdTemperature, zeroColdTime |
| `2PY3` | 九牧Z300旋转电热毛巾架 | 9340066-HBH-1 | 0BA | childLockSwitch, mode, temperature | commonFaultDetection, dryingLeftTime, dryingTime |
| `2Q1N` | 正尚2路WiFi开关 | ZS-HWTB-SM-21W | 064 | switch, switch1, switch2 | CleanPair, Pair, backlight, memorySwitch, mode1, mode2 |
| `2Q3X` | 双色温吸顶灯24W | C21XD004-W0024A20 | 112 | brightness, cct, switch | — |
| `2Q3Y` | 双色温吸顶灯36W | C21XD004-W0036A20 | 112 | brightness, cct, switch | — |
| `2Q3Z` | 三思智能球泡灯13W | C21BB-TE27-13W-HM | 119 | brightness, cct, switch | — |
| `2Q7M` | 三思智能球泡灯8W | C21BB-TE27-8W-HM | 119 | brightness, cct, switch | — |
| `2Q7V` | 三思智能球泡灯18W | C21BB-TE27-18W-HM | 119 | brightness, cct, switch | — |
| `2QAM` | 格威特循环泵 | GWH-8 | 348 | status, switch, temperature | antifreezeSwitch, backup, commonFaultDetection, flowActivationTime, oneClickCycleTime, timedCycleSwitch, waterFlowSwitch, zeroColdSwitch |
| `2QBF` | 苏泊尔小厨宝E07-UH01 | E07-UH01 | 1A2 | status, switch, temperature | commonFaultDetection, ecoSwitch, sterilizationSwitch |
| `2QCQ` | 杜亚智能窗帘 隐形大师 | Hx | 01C | action, mode, opener | changeDirection, commonFaultDetection, directionalmode, favorate, switchSpeed |
| `2QH9` | IAM智能净水器 鲲泽三合一 | I2200G  Pro | 02D | childLockSwitch, status, temperature | city, cycleSwitch, ecoMode, emptySwitch, faultDetection, filterElement1, filterElement2, inputTds, machinePara, noMoreOvernightWater, outputTds, refluxSwitch, rinseMode, tempMode, water, waterOutletType |
| `2QIE` | 奥佳华按摩椅OG8598X | OG8598X | 05F | action, status, switch | airbagMode, autoMode, backAction, commonFaultDetection, commonMode, countDown, hairSystemMode, heatGear, heatMode, lbpMode, legAction, manuMode, manuskillSwitch, massTime, massmode, setSystemMode, soleSwitch |
| `2QKO` | 易慧家推拉驱动 | CB3CTLVH | 02C | action, lightSwitch, opener | changeDirection, closeSpeed, commonFaultDetection, handStartSwitch, lockMechanism, lockType, silencer, stroke, switchSpeed, torque, travel |
| `2QKP` | 易慧家平开驱动 | CB3CPKVH | 02C | action, lightSwitch, opener | bottomTravel, changeDirection, commonFaultDetection, silencer, stroke, switchSpeed, torque, travel, windowType |
| `2QL5` | MEIPONT智能晾衣机(Pro) | HM70(Pro) | 028 | action, lightSwitch, status | airDry, airDryRemTime, airDryTime, commonExecution, commonFaultDetection, disinfect, disinfectRemTime, disinfectTime, dryRemTime, dryTime, drying, lightBrightness, lightRemTime, lightTime |
| `2QMC` | 箭牌智能花洒 | HM-S01ZCP | 300 | battery, status, switch2 | circulationInsulationSwitch, coldWaterSwitch, commonFaultDetection, drainageDelay, screenSwitch, temperatureSetting |
| `2QN9` | 火焰山多功能智能取暖桌 | HYS22STC22A01-M | 06A | action, childLockSwitch, status | delayOff, gear, multiWarmer |
| `2QO8` | A.O.史密斯燃气热水器零冷水系列JSQ31-DJSH | JSQ31-DJSH | 124 | status, switch, temperature | TimeFunction, TotalTime, boostMode, commonFaultDetection, curWater, gasStatus, inletTemperature, statusOfMachine, totalGas, totalWater, zeroColdMode, zeroColdSwitch |
| `2QSZ` | 九牧智能晾衣机LA7002 | LA7002-000/2M1-2 | 028 | action, lightSwitch, status | commonFaultDetection, fadeSwitch, limit, silencer |
| `2QTJ` | MEIPONT智能剃须刀 磐石 | PS52H | 170 | battery, mode, status | bladeClean, bladeReset, bladeStatus, commonFaultDetection, travelLock |
| `2QTU` | 箭牌智能花洒 Pro | HM-P02ZCP | 300 | battery, status, switch2 | circulationInsulationSwitch, coldWaterSwitch, commonFaultDetection, drainageDelay, screenSwitch, temperatureSetting |
| `2QWL` | 佳普乐致慕智能浴霸 | BH2ZM-01S | 035 | action, fan, lightSwitch | autoWarmWindSwitch, circulationTime, devCustomInfo, drySwitch, heat, inductionCondition, keyToneSwitch, nightLightSwitch, sceneMode, setWorkTime, swingSwitch, timeGear, ventilateSwitch, windSwitch, windTime |
| `2QYG` | 奥普浴霸Q360T5S-Air-HW | Q360T5S-Air-HW | 035 | action, lightSwitch, status | autoDrySwitch, autoLightSwitch, autoWarmWindSwitch, commonFaultDetection, deodorization, drySwitch, heat, leftTime, nightLightSwitch, ventilateGear, ventilateSwitch, windMode, windSwitch |
| `2QYH` | 奥普浴霸MR007-HW | MR007-HW | 035 | action, lightSwitch, status | autoWarmWindSwitch, commonFaultDetection, deodorization, drySwitch, heat, leftTime, lightingMode, nightLightDelay, nightLightSwitch, setWorkTime, swingSwitch, ventilateGear, ventilateSwitch, windMode, windSwitch |
| `2QYJ` | 奥普Smart线性浴霸 L2A-Air-HW | L2A-Air-HW | 035 | action, lightSwitch, status | autoDrySwitch, autoWarmWindSwitch, autoWindSwitch, automaticWarmWindSwitch, commonFaultDetection, deodorization, devCustomInfo, drySwitch, heat, inductionCondition, sensitivity, setWorkTime, ventilateGear, ventilateSwitch, windMode, windSwitch |
| `2QYL` | 奥普浴霸L10B-Pro-HW | L10B-Pro-HW | 035 | action, lightSwitch, status | autoWarmWindSwitch, autoWindSwitch, circulationTime, commonFaultDetection, deodorization, drySwitch, heat, leftTime, swingSwitch, ventilateGear, ventilateSwitch, windMode, windSwitch, windTime |
| `2R61` | 佳普乐星泽智联淋浴花洒 | SH2XZ-01N | 300 | status, switch2, switch3 | coldWaterSwitch, commonFaultDetection, screenSwitch, temperatureSetting |
| `2RBF` | 智能大西施锅 | GAOBO-20E2 | 026 | action, mode, status | leftTime, preTimeStart, presetSwitch, warmDuration, warmSwitch |
| `2RNA` | 西顿照明T5无线磁吸灯照明驱动 | CXL05S01/CW-HBT | 226 | brightness, cct, switch | commonFaultDetection, commonMemorySwitch, fadeTimeSetting, indicator, lightCurveSetting, relBrightness |
| `2RND` | 西顿照明T5无线灯带照明驱动 | SWBH-QY-240W-2 | 226 | brightness, cct, switch | commonFaultDetection, commonMemorySwitch, fadeTimeSetting, indicator, lightCurveSetting, relBrightness |
| `2RNE` | 西顿照明T5无线筒射灯照明驱动 | SWBH-QL-12W-2 | 226 | brightness, cct, switch | commonFaultDetection, commonMemorySwitch, fadeTimeSetting, indicator, lightCurveSetting, relBrightness |
| `2ROF` | 西顿照明T5无线明装筒射灯照明驱动 | SWBH-QL-12W-2/N | 226 | brightness, cct, switch | commonFaultDetection, commonMemorySwitch, fadeTimeSetting, indicator, lightCurveSetting, relBrightness |
| `2RQY` | 欧雅系列洗衣机 | XQG100-LD1039FA | 015 | action, mode, status | commonFaultDetection, leftTime |
| `2RTY` | IAM智能净水器 鲲泽二合一 | I1800G | 02D | childLockSwitch, status, temperature | city, commonFaultDetection, disclaimerStatus, ecoMode, filterElement1, filterElement2, inputTds, noMoreOvernightWater, outputTds, refluxSwitch, rinseMode, tempMode, water |
| `2RU7` | 友望智能高速吹风机Pro | CD2626 | 0E4 | mode, status, temperature | commonFaultDetection, hairDryer, speed |
| `2RUD` | 奥普美容舱浴霸MRGC2-HW | MRGC2-HW | 035 | action, lightSwitch, status | autoWarmWindSwitch, commonFaultDetection, deodorization, drySwitch, heat, leftTime, lightingMode, nightLightDelay, setWorkTime, swingSwitch, ventilateGear, ventilateSwitch, windMode, windSwitch |
| `2RUP` | 达伦智能台灯 大想 | DL-31WS | 046 | brightness, lightMode, switch | delayTurnoff, eyeSuggestion, fadeTime, lightFormulaArray, preLightFormulaArray, preview, usageRecord |
| `2RVR` | 奥普Smart线性浴霸GL21-Pro+-HW | GL21-Pro+-HW | 035 | action, lightSwitch, status | autoDrySwitch, autoWarmWindSwitch, autoWindSwitch, automaticWarmWindSwitch, commonFaultDetection, deodorization, devCustomInfo, drySwitch, heat, inductionCondition, sensitivity, setWorkTime, ventilateGear, ventilateSwitch, windMode, windSwitch |
| `2RWE` | 欧雅系列洗烘一体机 | XQG100-LD1039FAG | 015 | action, mode, status | commonFaultDetection, leftTime |
| `2RWZ` | 奥普奥芯线性浴霸GL22-Pro+-HW | GL22-Pro+-HW | 035 | action, lightSwitch, status | aircleanSwitch, autoDrySwitch, autoLightSwitch, autoWarmWindSwitch, automaticWarmWindSwitch, commonFaultDetection, deodorization, devCustomInfo, drySwitch, heat, setWorkTime, ventilateGear, ventilateSwitch, windMode, windSwitch |
| `2S48` | 华帝小恒星燃气热水器 Pro | JSLQ27-HS71-16 | 124 | status, switch, temperature | allDayRecircTempSwitch, boostMode, circulatingTemp, cleanCountdown, cleanSwitch, commonFaultDetection, curGasCon, curWaterVol, ecoSwitch, energySaving, flameStatus, gasElectricDoubleBreakSwitch, inchingSwitch, increaseCapacitySwitch, maintenanceStatus, recircTempTime, scheduledCold, totalGas, totalWater, zeroColdSwitch, zeroColdTemperature, zeroColdTime |
| `2S4E` | 志高 271 系列 | KFR-35GW/MBP271+A1G+Y2V | 012 | mode, switch, temperature | ECOswitch, calmSpellSwitch, co2Switch, commonFaultDetection, exAirSwitch, exhaustAirSpeed, favoriteModeSwitch, keyToneSwitch, light, preTime, selfCleanswitch, switchPTC |
| `2S4O` | 智能红外光热坐垫 | HXWL-1 | 186 | mode, switch, temperature | commonFaultDetection, massageMode |
| `2S63` | 佳普乐沁澜智联龙头 | ST2QL-01N | 310 | status, switch, temperature | coldWaterSwitch, preSchedulingDuration, waterTime |
| `2S7H` | 佳普乐致雅智能浴霸Pro | BH1ZY-01N+ | 035 | action, lightSwitch, status | autoWarmWindSwitch, circulationTime, devCustomInfo, drySwitch, heat, keyToneSwitch, nightLightSwitch, sceneMode, setWorkTime, ventilateSwitch, warmWindTime, windSwitch, windTime |
| `2SAX` | 奥普Smart线性浴霸L3B-Pro+-HW | L3B-Pro+-HW | 035 | action, lightSwitch, status | autoDrySwitch, autoWarmWindSwitch, autoWindSwitch, automaticWarmWindSwitch, commonFaultDetection, deodorization, devCustomInfo, drySwitch, heat, inductionCondition, sensitivity, setWorkTime, ventilateGear, ventilateSwitch, windMode, windSwitch |
| `2SB0` | 奥普热能环双氧浴霸Q360T5-Pro-HW | Q360T5-Pro-HW | 035 | action, lightSwitch, status | autoDrySwitch, autoLightSwitch, autoWarmWindSwitch, automaticWarmWindSwitch, commonFaultDetection, deodorization, devCustomInfo, drySwitch, heat, inductionCondition, nightLightSwitch, sensitivity, setWorkTime, ventilateGear, ventilateSwitch, windMode, windSwitch |
| `2SCK` | 宠尔顿智能舱 | HongM520LUF | 1A4 | lightSwitch, switch, temperature | Brightness, btcSwitch, childLock, commonFaultDetection, dryMode, filterElement, intakeAirSwitch, petRoom, sleepMode, windSpeed |
| `2SFS` | 豪恩空气质量检测仪LH 368WF | LH-368WF | 006 | battery, humidity, temperature | co2, co2Alarm, co2AlarmSwitch, commonFaultDetection, environment, hchoAlarm, hchoAlarmSwitch, indicator, lowPowerMode, screenMode, sleepMode |
| `2SG4` | 箭牌智雨花洒2 Pro 宽域恒温版 | HM-P03ZHCP | 300 | battery, status, switch2 | circulationInsulationSwitch, coldWaterSwitch, commonFaultDetection, drainageDelay, screenSwitch, temperatureSetting |
| `2SG9` | 宝贝第一智能儿童安全座椅 智悦 | R157B | 0DF | alarm, battery, childLockSwitch | ISOFIXAlarmSwitch, ISOFIXStatus, antiTipingLegsStatus, babyInStatus, beltStatus, beltSwitch, commonFaultDetection, currentTemperature, exceptionInfo, fixedTemperature, gear, noForget, position, powerSupply, seatRotation, seatTiltAction, supportLegsAlarmSwitch, touchSwitch, volumeGear, welcomeDirection, welcomeModeSwitch |
| `2SH5` | 奥普Smart人感双氧浴霸S5-Pro+-HW | S5-Pro+-HW | 035 | action, lightSwitch, status | autoLightSwitch, autoWarmWindSwitch, automaticWarmWindSwitch, commonFaultDetection, deodorization, devCustomInfo, drySwitch, heat, inductionCondition, nightLightSwitch, sensitivity, setWorkTime, swingSwitch, ventilateGear, ventilateSwitch, windMode, windSwitch |
| `2SKJ` | 佳普乐沁沐智联龙头 | ST2QM-01N | 310 | status, switch, temperature | coldWaterSwitch, preSchedulingDuration, waterTime |
| `8003` | 智能台灯 | DL-01W | 046 | brightness, lightMode, switch | backlight, nightSwitch, nightWakeup |
| `9MTL` | 智控床头灯 | haTest2 | 10E | brightness, cct, switch | — |
| `9MTW` | 智控电饭煲 | haTest7 | 026 | action, status, switch | commonFaultDetection, cooker, leftTime |
| `9MU7` | 智控灯泡 | haTest10 | 119 | brightness, cct, switch | — |
| `9MYJ` | 智控炸锅 | haTest30 | 063 | action, status, temperature | leftTime, recipes, workTime |
| `9MZL` | 智控茶具 | haTest33 | 1A0 | mode, status, temperature | outlet, warmSwitch |
| `9MZT` | 智控电磁炉 | haTest37 | 079 | mode, status, switch | — |
| `9MZY` | 智控直饮机 | haTest41 | 06F | mode, status, temperature | outletWater, waterMode, waterPurifier |
| `A08G` | 美的智能电风扇 | FTS30-16BR | 029 | fan, mode, switch | connectStatus |
| `A0CX` | 美的智能电热水器 | midea_heater | 027 | status, switch, temperature | capacity, leftTime |
| `A0NT` | 智能双通道插座 | Smart socket | 01E | switch, switch1, switch2 | — |
| `A0OQ` | 智能双通道开关 | Smart wall switch | 005 | switch, switch1, switch2 | — |
| `A0QP` | 美的蒸烤料理炉 | S1-pro | 024 | action, mode, status | doorState |
| `A0R1` | 大金转角新风 | 1VFFA--AV1 | 013 | fan, mode, switch | commonFaultDetection |
| `A0RV` | 九阳豆浆机 | k2s | 02F | action, status, switch | capacity, commonFaultDetection, drink, iswarm, leftTime1, steam |
| `A0S2` | 大金新风系统 | VAM--GMVE | 030 | fan, mode, switch | commonFaultDetection |
| `A0TY` | 美的电热水器 | CFDV5032 | 027 | status, switch, temperature | commonFilterElement1 |
| `A0VY` | COLMO油烟机 | S83 | 021 | lightSwitch, status, switch | faultDetection, gear, gestureSwitch, hotcleanSwitch, smokeSwitch, steamingSwitch |
| `A0VZ` | 美的电热水器 | CFDV5032 | 027 | status, switch, temperature | commonFilterElement1 |
| `A0Z2` | 西门子开关 | 5TA71122NC | 005 | switch, switch1, switch2 | — |
| `A0Z7` | 西门子新风1 | 5UH73321NC | 030 | status, switch, temperature | SleepMode, bypassStatus, childLock, fanMode, faultDetection, filterAlarmStatus, systemMode |
| `A11H` | 九阳破壁机 | L12-Y536 | 0D2 | action, status, temperature | capacity, clean, commonFaultDetection, cupStatus, leftTime, menuCode |
| `A122` | 苏泊尔小C主厨料理机 | SY-50MT01 | 0D6 | mode, status, switch | addToDevice, cookingFire, cookingPressure, cookingSpeed, cookingStatus, cookingTemperature, cookingTime, cookingType, leftTime, recipes, toCooking |
| `A1AG` | 破壁机MJ-PB10P345 | MJ-PB10P345 | 05A | action, mode, status | cupStatus, leftTime, preTimeEnd |
| `A1AH` | 美的电饭煲 | MB-EFB3030H | 026 | action, mode, status | currentFun, keptWarmTime, leftTime |
| `A1AZ` | 美的家用空调 | KFR-72LW/K1-H1 | 012 | mode, switch, temperature | — |
| `A1B0` | 美的家用空调 | KFR-51LW/K1-H1 | 012 | mode, switch, temperature | — |
| `A1BM` | 美的电热水器 | F6030-TG8S(HEY) | 027 | status, switch, temperature | leftTime |
| `A1BR` | 美的燃气热水器 | JSQ34-RX9 | 027 | status, switch, temperature | faultDetection, inWaterTemp, noCold |
| `A1BT` | 美的JSQ34-18HV燃气热水器 | JSQ34-18HV | 027 | status, switch, temperature | faultDetection, inWaterTemp, noCold |
| `A1C3` | COLMO 图灵嵌入式蒸箱 | CSKO50 | 022 | action, mode, status | doorState, faultDetection, preheatStatus, setWorkTime, waterBox |
| `A1C4` | COLMO 图灵嵌入式烤箱 | COTM70 | 024 | action, mode, status | doorState, faultDetection, preheatStatus, setWorkTime, waterBox |
| `A1EV` | 美的家用空调 | KFR-26GW/K1-H1 | 012 | mode, switch, temperature | — |
| `A1EW` | COLMO除湿机 | CF20/CT1H | 09B | humidity, mode, switch | gear |
| `A1EX` | COLMO空调 | KFR-35GW/CE1H | 012 | mode, switch, temperature | — |
| `A1EY` | COLMO空调 | KFR-72LW/CE1H | 012 | mode, switch, temperature | — |
| `A1IM` | DDF60-i14029储水式电热水器 | DDF60-i14029 | 027 | mode, switch, temperature | cTVolume, commonFaultDetection, orderSwitch, statu, wPswitch |
| `A1JD` | 油烟机CXW-258-X10.i | CXW-258-X10.i | 021 | lightSwitch, mode, switch | Liftingposition, gear |
| `A1JS` | JSQ30-16JH61i家用供热水燃气快速热水器 | JSQ30-16JH61i | 027 | mode, switch, temperature | commonFaultDetection, cycle, heating, highTempUnlock, iwaterTmp, totalGas, totalWater, waterfallBath |
| `A1L2` | 九阳智能空气炸锅VF999 | KL65-VF999(HM) | 063 | action, status, temperature | changeCookParams, devStatus, downloadMenu, start, startCloud, stop, workTime |
| `A1NZ` | DDF60-YH05i储水式电热水器 | DDF60-YH05i | 027 | mode, switch, temperature | cTVolume, commonFaultDetection, orderSwitch, statu, wPswitch |
| `A1Y2` | JSQ30-i12151-16家用燃气热水器 | JSQ30-i12151-16 | 027 | mode, switch, temperature | ECO, Poweroff, commonFaultDetection, highTempUnlock, iwaterTmp, totalGas, totalWater |
| `A1Y7` | JSQ24-13ZH6i家用供热水燃气快速热水器 | JSQ24-13ZH6i | 027 | mode, switch, temperature | Selfclean, commonFaultDetection, cycle, heating, highTempUnlock, iwaterTmp, totalGas, totalWater, waterfallBath |
| `A1Y8` | JSQ30-16ZH6i家用供热水燃气快速热水器 | JSQ30-16ZH6i | 027 | mode, switch, temperature | Selfclean, commonFaultDetection, cycle, heating, highTempUnlock, iwaterTmp, totalGas, totalWater, waterfallBath |
| `A1Y9` | JSQ34-18ZH6i家用供热水燃气快速热水器 | JSQ34-18ZH6i | 027 | mode, switch, temperature | Selfclean, commonFaultDetection, cycle, heating, highTempUnlock, iwaterTmp, totalGas, totalWater, waterfallBath |
| `A1YU` | COLMO燃气热水器JSQ30-CE116 | JSQ30-CE116 | 027 | status, switch, temperature | faultDetection, inWaterTemp, noCold |
| `A2AA` | JSQ30-i12152-16家用燃气热水器 | JSQ30-i12152-16 | 027 | mode, switch, temperature | ECO, Poweroff, commonFaultDetection, highTempUnlock, iwaterTmp, totalGas, totalWater |
| `A2AB` | JSQ30-i12153-16家用燃气热水器 | JSQ30-i12153-16 | 027 | mode, switch, temperature | ECO, Poweroff, commonFaultDetection, highTempUnlock, iwaterTmp, totalGas, totalWater |
| `A2GN` | 西门子洗衣机 | XQG100-WG54C3B8HW | 015 | action, mode, status | faultDetection, lefttime1 |
| `A2H3` | JSQ24-i12151-13家用燃气热水器 | JSQ24-i12151-13 | 027 | mode, switch, temperature | ECO, Poweroff, commonFaultDetection, highTempUnlock, iwaterTmp, totalGas, totalWater |
| `A2H4` | JSQ24-i12152-13家用燃气热水器 | JSQ24-i12152-13 | 027 | mode, switch, temperature | ECO, Poweroff, commonFaultDetection, highTempUnlock, iwaterTmp, totalGas, totalWater |
| `A2H5` | JSQ24-i12153-13家用燃气热水器 | JSQ24-i12153-13 | 027 | mode, switch, temperature | ECO, Poweroff, commonFaultDetection, highTempUnlock, iwaterTmp, totalGas, totalWater |
| `A2IU` | 美的电饭煲MB-HS408 | MB-HS408 | 026 | action, mode, status | currentFun, faultDetection, keptWarmTime, leftTime |
| `A2IV` | 美的电饭煲MB-HS508 | MB-HS508 | 026 | action, mode, status | currentFun, faultDetection, keptWarmTime, leftTime |
| `A2IW` | 美的电压力锅MY-C552N | MY-C552N | 074 | action, mode, status | commonFaultDetection, leftTime |
| `A2J2` | 美的全自动破壁机 | MJ-PB80W3-300 | 05A | action, mode, status | commonFaultDetection, cupType, currentFun, leftTime |
| `A2J6` | 美的电蒸锅 MZ-ZGS352012 |  MZ-ZGS352012 | 022 | action, mode, status | commonFaultDetection, pauseTime, remainTime, waterStatus |
| `A2J7` | 美的电炖锅 MD-DGS4011 | MD-DGS4011 | 026 | action, mode, status | commonFaultDetection, currentFun, leftTime, mouthfeel |
| `A2JL` | 智能双通道机械开关 | Smart Switch-2ch | 005 | switch, switch1, switch2 | — |
| `A2NE` | KEKEN 智能开关3键 | KEN-KK903 | 005 | switch1, switch2, switch3 | backlight2 |
| `A2OZ` | TH7i燃气热水器 | JSQ30-16TH7i | 027 | status, switch, temperature | Selfclean, StronRichWater, cycle, faultDetection, heating, highTempUnlock, iwaterTmp, totalGas, totalWater, waterTap, waterfallBath |
| `A2Q4` | 万家乐燃气热水器零冷水系列 | Macro | 124 | status, switch, temperature | zeroColdSwitch |
| `A2UR` | 万家乐燃气热水器普通恒温系列 | Macro 1 | 124 | status, switch, temperature | — |
| `A2UT` | 万家乐电热水器 | Macro2 | 027 | status, switch, temperature | — |
| `A2UZ` | CXW-200-E6090HS吸油烟机 | CXW-200-E6090HS | 021 | lightSwitch, status, switch | commonFaultDetection, delayedShutdown, gear, gearStat, lockScreen, lockStat, otcStat, otcSwitch, wacaStat |
| `A2VE` | SJ60燃气热水器 | JSQ30-SJ60-16 | 124 | status, switch, temperature | cycle, faultDetection, gasTotal, heating, highTempUnlock, iwaterTmp, waterTotal, waterfallBath |
| `A2VM` | 色温灯 | 0011 | 119 | brightness, cct, switch | — |
| `A2VX` | DDF50-YP07i电热水器 | DDF50-YP07i | 027 | status, switch, temperature | aiBath, bacSwitch, cTVolume, faultDetection, powerMode, wPswitch, waterQuality |
| `A2WW` | DDF60-YP07i电热水器 | DDF60-YP07i | 027 | status, switch, temperature | aiBath, bacSwitch, cTVolume, faultDetection, powerMode, wPswitch, waterQuality |
| `A2WX` | DDF70-YP07i电热水器 | DDF70-YP07i | 027 | status, switch, temperature | aiBath, bacSwitch, cTVolume, faultDetection, powerMode, wPswitch, waterQuality |
| `A2WY` | DDF50-BH04i电热水器 | DDF50-BH04i | 027 | status, switch, temperature | aiBath, bacSwitch, cTVolume, devMode, faultDetection, wPswitch, waterQuality |
| `A2X1` | DDF60-BH04i电热水器 | DDF60-BH04i | 027 | status, switch, temperature | aiBath, bacSwitch, cTVolume, devMode, faultDetection, wPswitch, waterQuality |
| `A2X2` | DDF50-BH03i电热水器 | DDF50-BH03i | 027 | status, switch, temperature | aiBath, bacSwitch, cTVolume, devMode, faultDetection, wPswitch, waterQuality |
| `A2X3` | DDF60-BH03i电热水器 | DDF60-BH03i | 027 | status, switch, temperature | aiBath, bacSwitch, cTVolume, devMode, faultDetection, wPswitch, waterQuality |
| `A2YO` | yeedi全能扫拖机器人CC | YDAX11-3 | 031 | action, battery, status | cleanMode, commonFaultDetection, vacuumGear, waterLevel |
| `A2ZP` | 美的焕新风挂机 | KFR-35GW/N8MKA1A | 012 | fan, mode, switch | ECOswitch, batchCmd, calmSpellSwitch, commonFaultDetection, freshAirSwitch, freshAirgear, heat, preventStraightWindswitch, selfCleanswitch, visualization |
| `A2ZQ` | 美的焕新风挂机 | KFR-26GW/N8MKA1A | 012 | fan, mode, switch | ECOswitch, batchCmd, calmSpellSwitch, commonFaultDetection, freshAirSwitch, freshAirgear, heat, preventStraightWindswitch, selfCleanswitch, visualization |
| `A2ZR` | 美的焕新风柜机 | KFR-72LW/N8MKA1A | 012 | fan, mode, switch | ECOswitch, batchCmd, calmSpellSwitch, commonFaultDetection, freshAirSwitch, freshAirgear, heat, preventStraightWindswitch, selfCleanswitch, visualization |
| `A2ZS` | 美的焕新风柜机 | KFR-51LW/N8MKA1A | 012 | fan, mode, switch | ECOswitch, batchCmd, commonFaultDetection, freshAirSwitch, freshAirgear, heat, preventStraightWindswitch, selfCleanswitch, visualization |
| `A2ZU` | 美的机煌挂机 | KFR-35GW/JH1-1 | 012 | fan, mode, switch | ECOswitch, batchCmd, commonFaultDetection, heat, preventStraightWindswitch, selfCleanswitch, visualization |
| `A2ZV` | 美的机煌挂机 | KFR-46GW/JH1-1 | 012 | fan, mode, switch | ECOswitch, batchCmd, commonFaultDetection, heat, preventStraightWindswitch, selfCleanswitch, visualization |
| `A30B` | 智汇云冷暖调光灯 | ZHY-MP001 | 119 | brightness, cct, switch | turnoffTime, turnonTime |
| `A30V` | COLMO全热交换新风机-GC1 | CAX250/350/500GC1 | 2FB | mode, status, switch | speed |
| `A31J` | COLMO图灵中央空调 | CAKWxxZN1C1-9 | 012 | fan, mode, switch | automaticAirswitch, heat |
| `A31L` | COLMO全热交换新风机-GC1(2) | CAX250/350GC1(2) | 2FB | mode, status, switch | speed |
| `A32D` | COLMO新象中央空调 | CAKWxxZN1C1-5/CAC32ZN1C1-5 | 012 | fan, mode, switch | automaticAirswitch, heat |
| `A32E` | COLMO风管机 | CA75ZN1A1/CA75ZN8A2 | 012 | fan, mode, switch | Dry, automaticAirswitch, customhumidity, heat |
| `A32Q` | COLMO地暖 | CANxxxBN1Cx-6/6A | 2FD | status, switch, temperature | Convenientfeatures |
| `A32R` | 美的智能取暖器 | HYW22KRA | 06A | status, switch, temperature | buttonBeepSwitch, commonFaultDetection, gear, preTimeOff, preTimeOn |
| `A32V` | TCL新风柜式空调 | TCL fresh air cabinet | 2F9 | mode, switch, temperature | PTC, beepSwitch, gear, horizontalWind, newWindECOSwitch, newWindPercentage, newWindSwitch, sleep, softWind, switchEco, switchLight, verticalWind, windSpeedAutoSwitch |
| `A333` | 美的地暖 | SFEN-xxx/N1X-A | 2FD | status, switch, temperature | Convenientfeatures |
| `A33D` | 美的中央空调-理想家LX | MDVH-JxxT2/BP3N1X-LX(B)2 | 012 | fan, mode, switch | automaticAirswitch, heat |
| `A33H` | TCL柜式空调 | TCL_cabinet | 2F9 | mode, switch, temperature | PTC, beepSwitch, gear, horizontalWind, sleep, softWind, switchEco, switchLight, verticalWind, windSpeedAutoSwitch |
| `A33I` | TCL挂式空调 | TCL-on-hook | 012 | mode, switch, temperature | ECOswitch, PTC, beepSwitch, light, sleep, softWind, sweepHorizon, sweepVertical, windGear, windSpeedAutoSwitch |
| `A33S` | 美的中央空调-领航者LH | MDVH-JxxT2/BP3N1X-LH2 | 012 | fan, mode, switch | automaticAirswitch, heat |
| `A33U` | 美的中央空调-超薄轻音TS | MJV-xxT2-TS / MJV-xxT2/P-TS  | 012 | fan, mode, switch | automaticAirswitch, heat |
| `A340` | 欧派智能磁吸轨道灯P24 | OP-LSPS-ZX03TB8W | 221 | brightness, cct, switch | MasterLightMode, MasterLightType, MasterPowerStatus, faultDetection |
| `A341` | 欧派智能CW色温灯P21 | OP-LSPS-TRO1RA7W | 111 | brightness, cct, switch | MasterLightMode, MasterLightType, MasterPowerStatus, faultDetection |
| `A342` | 欧派智能CW柜体灯带P25 | OP-LCLOS-1164 | 222 | brightness, cct, switch | MasterLightMode, MasterLightType, faultDetection |
| `A343` | 欧派智能CW天花灯带P26 | OP-LLIG-BL24SA8W | 118 | brightness, cct, switch | MasterLightMode, MasterLightType, MasterPowerStatus, faultDetection |
| `A364` | 欧派智能三位开关P33 | OP-PLCS-RKRC-3 | 064 | switch1, switch2, switch3 | — |
| `A36E` | 美的中央空调-设计家SJ | MJV-xxT2/(P)X-SJ / MJV-xxT2-SJ | 012 | fan, mode, switch | automaticAirswitch, heat |
| `A36L` | 科沃斯扫地机器人 | X2 | 031 | action, battery, status | — |
| `A36P` | 美的中央空调-玲珑LL | MDVH-JxxT2/BP3DN1X-LL(B)(2) | 012 | fan, mode, switch | automaticAirswitch, heat |
| `A36V` | 万和燃气热水器STL88 | JSW31-16STL88 | 124 | status, switch, temperature | ECO, Manual, Oneshot, bathMode, call, faultDetection, pretemp, waterPressurization, zeroColdMode |
| `A37H` | TCL新风挂式空调 | TCL_fresh air on-hook | 012 | mode, switch, temperature | ECOswitch, PTC, beepSwitch, freshAirSwitch, light, newWindECOSwitch, newWindPercentage, sleep, softWind, sweepHorizon, sweepVertical, windGear |
| `A37I` | 美的加湿器SZK-1Y80 | SZK-1Y80 | 052 | humidity, mode, switch | closeTime, commonFaultDetection, dry, gear, openTime, voice, waterRemain, workStatus |
| `A37M` | 美的风管机-乐享LX | KFR-xxT2/Bx3DN1-LX(1)2/3 | 012 | fan, mode, switch | automaticAirswitch, heat |
| `A37O` | 美的风管机-星光科技XGKJ | KFR-xxT2/B3DN1-XG(1)3 | 012 | fan, mode, switch | automaticAirswitch, heat |
| `A37P` | 美的风管机-星光XG | KFR-xxT2/BDN1-XG(1)3 | 012 | fan, mode, switch | automaticAirswitch, heat |
| `A3A4` | 美的抽油烟机 | CXW-140-JA9 | 021 | lightSwitch, status, switch | commonFaultDetection, gear, linkageStatus, workBurnerStatus |
| `A3A5` | COLMO抽油烟机 | CXKCP927S-D3 Pro | 021 | lightSwitch, status, switch | commonFaultDetection, gear |
| `A3AJ` | COLMO全热交换新风机-CAX500GC1(2) | CAX500GC1(2) | 2FB | mode, status, switch | speed |
| `A3C4` | 小佩智能双子星喂食器 | P591 | 103 | action, battery, status | feederPortion, food1, food2, petStatus, powerSource |
| `A3CR` | COLMO洗碗机 | CDB412 | 078 | action, status, switch | commonFaultDetection, dryLeftTime, filterElement1, filterElement2, keepLeftTime, orderLeftTime, statusDoor, washLeftTime |
| `A3CS` | COLMO电热水器 | CFBQ6032 | 027 | status, switch, temperature | commonFaultDetection |
| `A3CT` | COLMO燃气热水器 | JSQ30-CX116 | 124 | status, switch, temperature | commonFaultDetection |
| `A3D0` | COLMO智能油烟机 | CXKCP925W-S68 | 021 | lightSwitch, status, switch | commonFaultDetection, gear, linkageStatus, workBurnerStatus |
| `A3D3` | 美的洗碗机 | S65Pro | 078 | action, status, switch | commonFaultDetection, dryLeftTime, filterElement1, filterElement2, keepLeftTime, orderLeftTime, statusDoor, washLeftTime |
| `A3D4` | 美的燃气热水器 | JSQ30-MK6 | 124 | status, switch, temperature | commonFaultDetection |
| `A3DG` | 美的抽油烟机 | CXW-270-J25S | 021 | lightSwitch, status, switch | commonFaultDetection, gear, linkageStatus, workBurnerStatus |
| `A3DM` | 美的燃气热水器 | JSLQ27-16LN3 | 124 | status, switch, temperature | commonFaultDetection, zeroColdSwitch |
| `A3DN` | COLMO燃气热水器 | JSQ30-CE216-N | 124 | status, switch, temperature | commonFaultDetection, zeroColdSwitch |
| `A3DT` | COLMO二代新风机 | CAXxxxGC1(2) | 2FB | mode, status, switch | speed |
| `A3DU` | COLMO一代新风机 | CAX250/350/500GC1 | 2FB | mode, status, switch | speed |
| `A3DV` | 小佩智能喂食器SOLO | P571 | 103 | action, battery, status | childLock, foodStatus, perWeight |
| `A3DW` | COLMO水力模块 | CANxxBN1Cx-x | 2FD | status, switch, temperature | ECO, automatic, electricAuxiliaryHeat, goOut |
| `A3E2` | 美的水力模块 | SFEN-xxx/N1X-x | 2FD | status, switch, temperature | automatic, goOut |
| `A3E3` | COLMO水力模块 | CANxxxBN1Cx-x | 2FD | status, switch, temperature | ECO, automatic, electricAuxiliaryHeat, goOut |
| `A3E7` | 方太智能热水器 | JSQ31-X16G1.i-FR-12T | 124 | status, switch, temperature | bathMode, boostMode, changeLitresMode, commonFaultDetection, inchingSwitch |
| `A3EA` | COLMO燃气热水器 | JSQ30-CX916 | 124 | status, switch, temperature | commonFaultDetection |
| `A3EB` | COLMO燃气热水器 | JSQ38-CE820 | 124 | status, switch, temperature | commonFaultDetection, zeroColdSwitch |
| `A3EC` | 美的燃气热水器 | JSQ30-16HTLN | 124 | status, switch, temperature | commonFaultDetection, zeroColdSwitch |
| `A3ED` | 美的燃气热水器 | JSQ30-16HL6 | 124 | status, switch, temperature | commonFaultDetection |
| `A3F3` | 海信智能水温控制器 | FHSXC-VC05 | 2FA | mode, switch, temperature | — |
| `A3FN` | 美的一代全热交换新风机 | MQXF250 | 2FB | mode, status, switch | speed |
| `A3FP` | 美的二代全热交换新风机 | MQXF250II | 2FB | mode, status, switch | speed |
| `A3FQ` | 美的小型化全热交换新风机 | MQXF250M | 2FB | mode, status, switch | exAirSwitch, exhaustAirSpeed, freshAirSpeed, freshAirSwitch |
| `A3FX` | COLMO小型化全热交换新风机M | CAX250GC1M | 2FB | mode, status, switch | exAirSwitch, exhaustAirSpeed, freshAirSpeed, freshAirSwitch |
| `A3G5` | COLMO小型化全热交换新风机 | CAX250GC1M | 2FB | mode, status, switch | exAirSwitch, exhaustAirSpeed, freshAirSpeed, freshAirSwitch |
| `A3GY` | 格力至尊型户式机 | GN-HRZ9MDGV(P)/NaA | 2FA | mode, switch, temperature | — |
| `A3HZ` | 方太智能油烟机 | CXW-358-02-X20 | 021 | lightSwitch, status, switch | delayOff, gear, gestureSwitch, intelligentCruiseControl, lockSwitch, ventilationSwitch |
| `A3J2` | 小天鹅小型化全热交换新风机 | LQXF350M | 2FB | mode, status, switch | exAirSwitch, exhaustAirSpeed, freshAirSpeed, freshAirSwitch |
| `A3J7` | 美诺智能洗衣机 | WSI 862 C | 015 | action, mode, status | commonFaultDetection, filterElement3, filterElement4, leftTime, productModel |
| `A3J9` | 美诺智能干衣机 | TSH782WP C | 0D7 | action, mode, status | commonFaultDetection, leftTime |
| `A3JD` | 美诺蒸烤一体机 | DGC7250 C | 19B | action, status, switch | commonFaultDetection, leftTime, mixMode |
| `A3JE` | 美诺智能油烟机 | DA 3966 C | 021 | lightSwitch, status, switch | commonFaultDetection, gear |
| `A3JF` | 华帝智能燃气热水器 | i12575E | 124 | status, switch, temperature | boostMode, commonFaultDetection, ecoSwitch, inchingSwitch, increaseCapacitySwitch, productModel, zeroColdSwitch |
| `A3KI` | 美的真暖空气源热泵Z1 | MHSR140N8-Z1 | 2FA | mode, switch, temperature | ECOswitch, coolWaterTemp, heatWaterTemp, keyToneSwitch, light, targetTemp, tempControlMode |
| `A3KK` | 美的真享空气源热泵ZX1 | MHSR200SN8ZX1 | 2FA | mode, switch, temperature | ECOswitch, coolWaterTemp, heatWaterTemp, keyToneSwitch, light, tempControlMode |
| `A3L5` | A.O.史密斯燃气热水器FJS | JSQ31-FJSWi | 124 | status, switch, temperature | boostMode, changeLitresMode, commonFaultDetection, curWaterVol, ecoSwitch, zeroColdSwitch, zeroColdTime |
| `A3L9` | 方太智能嵌隐升降油烟机 | CXW-358-01-Y9 | 021 | lightSwitch, status, switch | delayOff, gear, gestureSwitch |
| `A3LE` | COLMO空气源热泵(M)T1 | CHSR200SN8T1 | 2FA | mode, switch, temperature | coolWaterTemp, heatWaterTemp, keyToneSwitch, light, switchScreen, tempControlMode |
| `A3N1` | 华帝智能燃气壁挂炉 | LH1i | 174 | mode, status, switch | aIWarmSwitch, bathTemperature, boostMode, faultDetection, heatStatus, heatTemperature, heatingImmediatelySwitch, productModel, zeroColdSwitch |
| `A3N9` | 能率热水器GQ-16D6AFEX | GQ-16D6AFEX | 124 | status, switch, temperature | commonFaultDetection, flameStatus, increaseCapacitySwitch, totalGas, totalWater, zeroColdMode |
| `A3NN` | 九阳0涂层电饭煲 | 40N9UPro/30N9UPro | 026 | action, mode, status | commonFaultDetection, food, leftTime, preTimeEnd, presetSwitch, workTime |
| `A3NT` | 华帝智能蒸烤箱 | JVQ50-i31110 Pro | 19B | action, status, switch | commonFaultDetection, leftTime |
| `A3NU` | 华帝智能油烟机 | i111Y9 | 021 | lightSwitch, status, switch | commonFaultDetection, gear, workBurnerStatus |
| `A3O9` | 美的除湿机N7DO1 | CF12BD/N7DO1 | 09B | humidity, mode, switch | anionSwitch, commonFaultDetection, delayOff, delayOn, gear |
| `A3OE` | 智能晾衣架D35WMAX | M1100014 | 028 | action, lightSwitch, status | commonFaultDetection, lightBrightness |
| `A3OR` | 美的冷塔扇 | AAF10MR | 029 | fan, mode, switch | commonFaultDetection, indicator, neIon, water |
| `A3OW` | 美的除湿机CF25BSDA | CF25BSDA | 09B | humidity, mode, switch | anionSwitch, commonFaultDetection, delayOff, delayOn, gear, indicator, keyToneSwitch |
| `A3OY` | 美的除湿机CF54BSDA | CF54BS/DA | 09B | humidity, mode, switch | anionSwitch, commonFaultDetection, delayOff, delayOn, drainSwitch, gear, indicator, keyToneSwitch |
| `A3PI` | 好太太智能晾衣机 | GW-1396W Max | 028 | action, lightSwitch, status | airDry, airDryRemTime, airDryTime, commonFaultDetection, disinfect, disinfectRemTime, disinfectTime, dryRemTime, dryTime, drying |
| `A3QR` | 箭牌智能毛巾架AKS22GGSP | AKS22GGSP | 0BA | childLockSwitch, mode, switch | drying, dryingLeftTime, dryingTime, heat |
| `A3RD` | 美的智能晾衣架 | MLY-Z5 | 028 | action, lightSwitch, status | commonFaultDetection, dryRack, lightBrightness |
| `A3RZ` | 好太太智能晾衣架 | GW-1296HT | 028 | action, lightSwitch, status | commonFaultDetection, lightBrightness |
| `A3SS` | 嘉格纳200 系列升降式吸油烟机 | AL200190CN | 021 | lightSwitch, status, switch | commonFaultDetection, delayOff, gear |
| `A3ST` | 博世8系T10双吸油烟机 | DXB98M98BW | 021 | lightSwitch, status, switch | commonFaultDetection, delayOff, gear, gestureSwitch, linkageStatus |
| `A3UA` | 嘉格纳Expressive 艺境系列蒸汽烤箱左侧铰链 | GS451120 | 024 | childLockSwitch, status, switch | commonFaultDetection, lackWater, leftTime, oven |
| `A3US` | 嘉格纳Expressive 艺境系列蒸汽烤箱 | GS450120 | 19B | childLockSwitch, status, switch | commonFaultDetection, lackWater, leftTime, ovenSteamer |
| `A3VP` | 能率热水器GQ-16K3AAFEX | GQ-16K3AAFEX | 124 | status, switch, temperature | commonFaultDetection, flameStatus, totalGas, totalWater |
| `A3VQ` | 美的空气源热泵真暖MAX | MHSR140N8-Z2 | 2FA | mode, switch, temperature | ECOswitch, commonFaultDetection, hvacType, inletTemperature, keyToneSwitch, light, outWaterTemp, targetTemp, tempControlMode |
| `A3WG` | 嘉格纳Expressive 艺境系列微波烤箱右侧铰链 | GM450120 | 024 | childLockSwitch, status, switch | commonFaultDetection, leftTime, oven |
| `A3WX` | 嘉格纳Expressive 艺境系列烤箱左侧铰链 | GO451120 | 024 | childLockSwitch, status, switch | commonFaultDetection, leftTime, oven |
| `A3X0` | 嘉格纳Minimalistic臻境系列蒸汽烤箱碳晶黑 | GS240100 | 024 | childLockSwitch, status, switch | commonFaultDetection, leftTime, oven |
| `A3X1` | 博世御器Z4炫彩大屏蒸烤一体机 | CSP5B93D8W | 19B | childLockSwitch, status, switch | commonFaultDetection, leftTime, ovenSteamer |
| `A3X2` | 嘉格纳Expressive 艺境系列微波烤箱左侧铰链 |  GM451120 | 024 | childLockSwitch, status, switch | commonFaultDetection, leftTime, oven |
| `A3XA` | 嘉格纳Expressive 艺境系列烤箱 | GO450120 | 19B | childLockSwitch, status, switch | commonFaultDetection, leftTime, ovenSteamer |
| `A3XQ` | 卡萨帝揽光蒸烤箱 | C3SO46BGU1 | 19B | childLockSwitch, status, switch | bakeTime, leftTime, ovenSteamer, remoteControlService |
| `A3Y0` | 西门子玄晶Pro蒸烤一体机60厘米 | HS756G3B1W | 024 | childLockSwitch, status, switch | commonFaultDetection, leftTime, oven |
| `A3YP` | 西门子玄晶Pro蒸烤一体机45厘米 | CS736G3B1W | 024 | childLockSwitch, status, switch | commonFaultDetection, leftTime, oven |
| `A3YV` | 西门子studioLine蒸箱 | CD914GXB1W | 024 | childLockSwitch, status, switch | commonFaultDetection, leftTime, oven |
| `A3YW` | 西门子玄晶Pro蒸箱 | CD714GXB1W | 024 | childLockSwitch, status, switch | commonFaultDetection, leftTime, oven |
| `A3YZ` | 西门子studioLine烤箱 | HB978GQB1W | 024 | childLockSwitch, status, switch | commonFaultDetection, leftTime, oven |
| `A3Z3` | 箭牌智能浴缸裙边款Pro | ACH1787SQ | 297 | colourMode, mode, status | constantTemperatureSwitch, devCustomInfo, drainSwitch, gear, heat, massageSwitch, waterGear, waterInletSwitch |
| `A3Z4` | 箭牌智能浴缸独立款Pro | ACH1888TQ | 297 | colourMode, mode, status | constantTemperatureSwitch, devCustomInfo, drainSwitch, gear, heat, massageSwitch, skirtEdgeAmbientLightSwitch, waterGear, waterInletSwitch |
| `A3Z5` | 博世极匠Pro蒸烤一体机60厘米 | HSG7564B1W | 024 | childLockSwitch, status, switch | commonFaultDetection, leftTime, oven |
| `A3Z8` | 博世极匠Pro蒸烤一体机45厘米 | CSG7564B1W | 024 | childLockSwitch, status, switch | commonFaultDetection, leftTime, oven |
| `A3Z9` | 博世accentLine天工蒸箱 | CDG914XB1W | 022 | childLockSwitch, status, switch | commonFaultDetection, leftTime, steamer |
| `A3ZB` | 博世极匠Pro蒸箱 | CDG714XB1W | 022 | childLockSwitch, status, switch | commonFaultDetection, leftTime, steamer |
| `A3ZC` | 博世accentLine天工烤箱 | HBG978QB1W | 024 | childLockSwitch, status, switch | commonFaultDetection, leftTime, oven |
| `A3ZE` | 博世极匠Pro烤箱 | HBG7542B1W | 024 | childLockSwitch, status, switch | commonFaultDetection, leftTime, oven |
| `A3ZI` | 嘉格纳200 系列电磁灶80cm | CI282112 | 079 | childLockSwitch, mode, status | commonFaultDetection, heatGear, heating |
| `A429` | 石头智能扫拖机器人 | A2950RR | 031 | action, battery, status | baseAction, vacuumGear, waterLevel |
| `A42A` | 嘉格纳臻境系列蒸箱 | GS221100 | 024 | childLockSwitch, status, switch | commonFaultDetection, leftTime, oven |
| `A42B` | 嘉格纳艺境系列嵌入式电烤箱 | GO470120 | 024 | childLockSwitch, status, switch | commonFaultDetection, leftTime, oven |
| `A42C` | 嘉格纳艺境系列嵌入式紧凑型蒸烤一体机 | GS471120 | 024 | childLockSwitch, status, switch | commonFaultDetection, leftTime, oven |
| `A43S` | 石头自清洁扫拖机器人 | A3060RR | 031 | action, battery, status | baseAction, commonFaultDetection, vacuumGear, waterLevel |
| `A44B` | 美的除湿机CF24BDN7DY | CF24BD/N7-DY | 09B | humidity, mode, switch | anionSwitch, commonFaultDetection, delayOff, delayOn |
| `A44N` | 方太智能油烟机F5 | CXW-358-F5 | 021 | lightSwitch, status, switch | commonFaultDetection, delayOff, gear, gestureSwitch, remoteAuth |
| `A44O` | 方太智能油烟机JCD18TA | CXW-358-JCD18TA | 021 | lightSwitch, status, switch | commonFaultDetection, delayOff, gear, gestureSwitch, remoteAuth |
| `A44P` | 方太智能油烟机JR01T | CXW-358-JR01T-G | 021 | lightSwitch, status, switch | commonFaultDetection, delayOff, gear, gestureSwitch, remoteAuth |
| `A44Q` | 嘉格纳Minimalistic 曜岩黑系列 | GO240100 | 024 | childLockSwitch, status, switch | commonFaultDetection, leftTime, oven |
| `A44Z` | 欧瑞博新风 | MS-HVAC-FA | 030 | fan, mode, switch | airQuality, co2, commonFaultDetection |
| `A450` | 欧瑞博热水器 | MS-HVAC-DHW | 125 | status, switch, temperature | commonFaultDetection, faultDetection |
| `A454` | 卡萨帝指挥家烤箱 | C7O60DGU1 | 024 | childLockSwitch, status, switch | bakeTime, leftTime, oven, remoteControlService |
| `A456` | 卡萨帝指挥家蒸箱 | C7S46DGU1 | 022 | childLockSwitch, status, switch | bakeTime, leftTime, remoteControlService, steamer |
| `A457` | 卡萨帝致境烤箱 | C6O60AGU1 | 024 | childLockSwitch, status, switch | bakeTime, leftTime, oven, remoteControlService |
| `A45A` | 美的智能浴霸(常规交流无人感) | MY-D6Y27-A3 Pro | 035 | action, brightness, lightSwitch | autoWarmWindSwitch, commonFaultDetection, drySwitch, heat, nightLightSwitch, sceneMode, swingSwitch, ventilateSwitch, windSwitch |
| `A45I` | 方太智能油烟机V1 | CXW-358-V1 | 021 | lightSwitch, status, switch | commonFaultDetection, delayOff, gear, gestureSwitch, remoteAuth |
| `A46J` | 嘉格纳 200 系列壁挂式吸油烟机 | AW240191CN | 021 | lightSwitch, status, switch | commonFaultDetection, delayOff, delayShutdownSetting, gear, gestureSwitch, linkageStatus |
| `A46K` | 嘉格纳艺境系列嵌入式烤箱右开门 | GO480120 | 024 | childLockSwitch, status, switch | commonFaultDetection, leftTime, oven |
| `A46Y` | 嘉格纳艺境系列嵌入式蒸烤一体机左开门 | GS481120 | 024 | childLockSwitch, status, switch | commonFaultDetection, leftTime, oven |
| `A472` | 嘉格纳臻境系列烤箱60cm | GO240130 | 024 | childLockSwitch, status, switch | commonFaultDetection, leftTime, oven |
| `ZG07` | 华为全屋智能射灯筒灯驱动器 | BER-LD00 | A0E | brightness, cct, switch | faultDetection, subProduct |
| `ZG0B` | 智能开关 1键 | OSLO-SS1 | A13 | brightness, childLockSwitch, switch1 | backlight, button1, faultDetection, memorySwitch, mode1, reboot |
| `ZG0F` | 华为全屋智能 AI超感传感器 | BER-SE00 | A14 | action, luminance, switch | backlight, basicFence, basicFenceEvent, devLocation, faultDetection, reboot, userFence1, userFence2, userFence3, userFence4, userFence5, userFence6, userFenceEvent1, userFenceEvent2, userFenceEvent3, userFenceEvent4, userFenceEvent5, userFenceEvent6 |
| `ZG0G` | 华为全屋智能射灯筒灯驱动器 - 12W | BER-LD02 | A0E | brightness, cct, switch | faultDetection, subProduct |
| `ZG0J` | 智能开关 (无线版) 2键 | OSLO-BS2 | A13 | childLockSwitch, switch1, switch2 | button1, button2, faultDetection, memorySwitch, mode1, mode2, modeX, reboot |
| `ZG0M` | 华为全屋智能射灯筒灯驱动器 - 9W | BER-LD00 | A0E | brightness, cct, switch | faultDetection, subProduct |
| `ZG0N` | 华为全屋智能射灯筒灯驱动器 - 12W | BER-LD02 | A0E | brightness, cct, switch | faultDetection, subProduct |
| `ZG0Z` | 智能开关 1键 | OSLO-SS1 | A13 | brightness, childLockSwitch, switch1 | backlight, button1, faultDetection, memorySwitch, mode1, reboot |
| `ZG13` | 调光调色智能灯 | Adjust Color Lamp | A1B | brightness, cct, switch | fadeTime, relBrightness |
| `ZG15` | 调光调色床头灯 | Adjust Color Sleeping Lamp | A1C | brightness, cct, switch | fadeTime, relBrightness |
| `ZG17` | 调光调色灯带 | Adjust Color Light Belt | A1E | brightness, cct, switch | fadeTime, relBrightness |
| `ZG1H` | 华为全屋智能射灯筒灯驱动器 - 9W | BER-LD10 | A0E | brightness, cct, switch | faultDetection, subProduct |
| `ZG1I` | 华为全屋智能射灯筒灯驱动器 - 12W | BER-LD12 | A0E | brightness, cct, switch | faultDetection, subProduct |
| `ZG1M` | AI辅助康养传感器 | BER-SE0X | A14 | action, luminance, switch | backlight, basicFence, basicFenceEvent, devLocation, faultDetection, reboot, userFence1, userFence2, userFence3, userFence4, userFence5, userFence6, userFenceEvent1, userFenceEvent2, userFenceEvent3, userFenceEvent4, userFenceEvent5, userFenceEvent6 |
| `ZG1Q` | 华为全屋智能 调光驱动器 5路 单色温 恒压 100W | BER-LD01 | A0E | switch1, switch2, switch3 | brightness1, brightness2, brightness3, brightness4, brightness5, fadeTime1, fadeTime2, fadeTime3, fadeTime4, fadeTime5, fadeTimeSetting1, fadeTimeSetting2, fadeTimeSetting3, fadeTimeSetting4, fadeTimeSetting5, faultDetection, lightCurveSetting1, lightCurveSetting2, lightCurveSetting3, lightCurveSetting4, lightCurveSetting5, memorySwitch, outputMask, powerCon, relBrightness1, relBrightness2, relBrightness3, relBrightness4, relBrightness5, switch4, switch5 |
| `ZG1T` | 智能开关 1键 | PHP-W1-P1 | A13 | brightness, childLockSwitch, switch1 | backlight, button1, faultDetection, memorySwitch, mode1, reboot |
| `ZG1Y` | AI超感传感器 | BER-SE10 | A14 | action, luminance, switch | backlight, basicFence, basicFenceEvent, devLocation, faultDetection, reboot, userFence1, userFence2, userFence3, userFence4, userFence5, userFence6, userFenceEvent1, userFenceEvent2, userFenceEvent3, userFenceEvent4, userFenceEvent5, userFenceEvent6 |
| `ZG1Z` | AI超感传感器 Lite | BER-SE11 | A14 | action, luminance, switch | backlight, basicFence, basicFenceEvent, devLocation, faultDetection, reboot, userFence1, userFence2, userFence3, userFence4, userFence5, userFence6, userFenceEvent1, userFenceEvent2, userFenceEvent3, userFenceEvent4, userFenceEvent5, userFenceEvent6 |
| `ZG23` | 可视对讲底盒 | LDN-SVI-C25 | A11 | luminance, status, switch | cfgNet, clickedScene, deviceLabel, diagnose, dryContact1, dryContact2, dryContact3, dryContact4, dryContact5, hwaccount, lcdattr, logReport, luminanceReportSetting, pageInfo, plcSubSystem, reboot, reportSceneId, responseSetting, scurity, subScene, txPower |
| `ZG2F` | 调光调色吊灯 | Adjust Color Pendant Lamp | A1B | brightness, cct, switch | fadeTime, relBrightness |
| `ZG2G` | 调光调色射灯 | Adjust Color Spot Lamp | A1B | brightness, cct, switch | fadeTime, relBrightness |
| `ZG2H` | 调光调色筒灯 | Adjust Color Spotlight | A1B | brightness, cct, switch | fadeTime, relBrightness |
| `ZG2I` | 调光调色吸顶灯 | Adjust Color CeilingLamp | A1B | brightness, cct, switch | fadeTime, relBrightness |
| `ZG2J` | 调光调色磁吸灯 | Adjust Color Magnetic Lamp | A1B | brightness, cct, switch | fadeTime, relBrightness |
| `ZG2P` | 迈腾智能开关 (无线版) 2键 | PCP-OB2106 | A13 | childLockSwitch, switch1, switch2 | button1, button2, faultDetection, memorySwitch, mode1, mode2, modeX, reboot |
| `ZG2S` | 智能开关 奥斯陆(无线版) 2键 | PCP-OB2116 | A13 | childLockSwitch, switch1, switch2 | button1, button2, faultDetection, memorySwitch, mode1, mode2, modeX, reboot |
| `ZG2Y` | 智能开关 威尼斯(无线版) 2键 | PCP-OB2116-PF | A13 | childLockSwitch, switch1, switch2 | button1, button2, faultDetection, memorySwitch, mode1, mode2, modeX, reboot |
| `ZG38` | AI睡眠传感器 | BER-SE0X | A14 | action, luminance, switch | backlight, basicFence, basicFenceEvent, devLocation, faultDetection, reboot, userFence1, userFence2, userFence3, userFence4, userFence5, userFence6, userFenceEvent1, userFenceEvent2, userFenceEvent3, userFenceEvent4, userFenceEvent5, userFenceEvent6 |
| `0101` | 灯组 |  | 01B | brightness, switch | — |
| `100J` | 杜亚电动开窗机DJ56TSWH | DJ56TS/WH | 02C | motor, openLevel | — |
| `100K` | 杜亚电动窗帘DT76TV/WH | DT76TV/WH | 01C | motor, openLevel | — |
| `100Y` | 奥克斯柜机 | AHA700 | 012 | switch, temperature | airConditioner, faultDetection, turbo, wind |
| `100Z` | 奥克斯挂机 | TYC2 | 012 | switch, temperature | airConditioner, faultDetection, turbo, wind |
| `100m` | 嵌入式电蒸箱 | SCD26-C2S.H | 022 | switch, temperature | faultDetection, steam |
| `100n` | 方太智能电烤箱 | HBL-13 | 024 | switch, temperature | oven |
| `100s` | 美的音乐热水器 | 30WM6A | 027 | switch, temperature | elecHeater, music |
| `1012` | 艾美特电风扇 | SA35195R-A | 029 | fan, switch | faultDetection |
| `101O` | 720空气净化器KJ420F-EP420 | KJ420F-EP420 | 013 | switch, temperature | airPurifying, faultDetection, filterElement, pm2p5, wind |
| `101P` | 720空气净化器KJ420F-EP350 | KJ420F-EP420 | 013 | switch, temperature | airPurifying, faultDetection, filterElement, pm2p5, wind |
| `101h` | 杜亚电动窗帘DT806TV/WH | DT806TV/WH | 01C | motor, openLevel | — |
| `101j` | 杜亚电动卷帘DM35F/WH | DM35F/WH | 04D | motor, openLevel | — |
| `101x` | 美的智能空调 | 未知 | 012 | switch, temperature | airConditioner, faultDetection, turbo, wind |
| `101z` | 美的风扇 | 未知 | 029 | fan, switch | faultDetection |
| `1026` | 美的空气净化器 | KJ500G-E33 | 013 | switch, temperature | airPurifying, faultDetection, pm2p5, wind |
| `103G` | 生迪Wi-Fi智能球泡灯W11-C21 | W11-C21 | 01B | brightness, switch | — |
| `103H` | 老板蒸汽炉 | ZQB400-S226 | 022 | switch, temperature | faultDetection, steamoven |
| `103I` | 720空气净化器KJ800F-EP800 | KJ800F-EP800 | 013 | switch, temperature | airPurifying, faultDetection, filterElement, pm2p5, wind |
| `103T` | 欧普蓝牙筒灯OPLYTD | OPLYTD | 01B | brightness, switch | relativeDelay |
| `103U` | 欧普蓝牙射灯OPLYSD | OPLYSD | 01B | brightness, switch | faultDetection, relativeDelay |
| `103U` | 欧普蓝牙射灯OPLYSD | OPLYSD | 01B | brightness, switch | faultDetection, relativeDelay |
| `103Z` | 国投一路调光1LT | SMK-01-1LT | 01B | brightness, switch | — |
| `1041` |  | SMK-01-BUS | 012 | switch, temperature | airConditioner, faultDetection, wind |
| `1044` |  | SMK-01-PAC | 01C | motor, openLevel | — |
| `1049` |  | SMS-01-SIR | 03E | switch, temperature | elecHeater, music |
| `104B` | 国投温湿度传感器THC | SMS-01-THC | 04E | airDetector, battery | — |
| `104W` | 汉德森Wi-Fi信号放大吸顶灯 | HDS400-1W×32-WiFi(Huawei) | 01B | brightness, switch | — |
| `1052` | 瑞晶空调RAC-2 | RAC-2 | 012 | switch, temperature | airConditioner, faultDetection, wind |
| `1053` | 瑞晶地暖RAC-3 | RAC-3 | 02A | switch, temperature | floorHeating |
| `1057` | 瑞晶布帘RAL-4 | RAL-4 | 01C | motor, openLevel | — |
| `1058` | 瑞晶纱帘RAL-5 | RAL-5 | 01C | motor, openLevel | — |
| `105A` | 杜亚电动窗帘DH3 | DH3 | 01C | motor, openLevel | — |
| `105B` | 杜亚电动窗帘DH5 | DH5 | 01C | motor, openLevel | — |
| `105C` | 杜亚电动窗帘DH7 | DH7 | 01C | motor, openLevel | — |
| `105Q` | 小米门窗传感器 | 未知 | 018 | battery, cct | doorSensor |
| `105S` | YeeLight白灯 | 未知 | 01B | brightness, switch | faultDetection |
| `105V` | TPLink白灯 | 未知 | 01B | brightness, switch | — |
| `105X` | LIFX 彩灯 | 未知 | 01B | brightness, switch | relativeDelay |
| `1064` | 飞比门磁传感器NDOS107G-M2 | NDOS107G-M2 | 018 | battery, cct | doorSensor |
| `1067` | 飞比智能窗帘TZT2118W-T1 | TZT2118W-T1 | 01C | motor, openLevel | — |
| `1069` | 顺舟门窗磁SZ09-(05) | SZ09-(05) | 018 | battery, cct | doorSensor |
| `106D` | 顺舟窗帘电机SZ09-(18) | SZ09-(18) | 01C | motor, openLevel | — |
| `107C` | 莱柏顿风扇LBT-F02 | LBT-F02 | 029 | battery, mode | angle, binarySwitch, childLock, connectStatus, endTime, handangle, onOffBeep, onOffLight, preTime, speed |
| `1082` | 小熊养生壶YSH-A15U6 | YSH-A15U6 | 060 | mode, status | command, currentTemperature, faultCode, heatpower, keepWarmTP, keepWarmTime, preTime, remPreTime, remWorkTime, warmOnoff, workState, workTime |
| `108Q` | 西睿空气检测蓝盒子 | 5UH70121NC01 | 006 | airDetector, battery | HCHOLevelRange, PM25LevelRange |
| `108R` | 西睿空气检测红盒子 | 5UH70111NC01 | 006 | airDetector, battery | PM25LevelRange |
| `110S` | 亚都加湿器SC175-SK040ProHi | SC175-SK040Pro(Hi) | 052 | humidity, switch | Anion, Sleep, gear, sound, timing |
| `112S` | 东屋静脉锁V8 | V8 | 04B | alarm, battery | controller, counterLockStatus, discovery, event, keyList, volume |
| `113D` | 豪恩温湿度传感器 | H-32ZB | 04E | airDetector, battery | — |
| `114K` | 亚摩斯IH电磁电饭煲AS-IHW40Y | AS-IHW40Y | 026 | mode, status | cookInfo, faultDetection, leftTime, preTimeEnd, start, warm, warmDuration, workTime |
| `114M` | 奥普智能晾衣机D6 | D6 | 028 | action, lightSwitch | airDry, drying |
| `115M` | HDL灯光控制器 | HDL-DN01 | 01B | brightness, switch | — |
| `115O` | HDL空调 | HDL-HVAC | 012 | switch, temperature | airConditioner, wind |
| `117L` | 亚都加湿器SC700-SK071ProHi | SC700-SK071Pro(Hi) | 052 | humidity, switch | gear, light, sound, timing, water |
| `117Q` | A-OK智能开合帘电机 | AM68-1.5/100-EM-P | 01C | mode, opener | reversing |
| `120N` | 海令智能温湿度传感器 | SMK-FC-001 | 04E | airDetector, battery | — |
| `120Y` |  | SMK-DG-001 | 01C | motor, openLevel | — |
| `122C` | 人体红外4合1传感器 | V1.0 | 01A | humidity, luminance | Temperature, motionSensor, workMode |
| `122D` | 调光控制盒 | V1.0 | 01B | brightness, switch | — |
| `123E` | 一位免零线调光开关 | Z9/M2T2 | 044 | brightness, switch | switchLable |
| `123R` | SONOFF TX2C 智能墙壁开关 | T2UK2C | 005 | switch1, switch2 | hideSwitch, powerLight, pulseLength1, pulseLength2, pulseSwitch1, pulseSwitch2, startup1, startup2, switchOff, switchOn |
| `131B` | 莱克智能循环扇 | HF30 | 029 | mode, switch | angleMenu, autoOff, onOffBeep, onOffLight, speed, speedPercent |
| `131R` | 火鸡温感电磁炉 | C21-02H | 079 | mode, status | faultDetection, heatpower, recipe |
| `132S` | 亚都加湿器SZ300-JK361Hi | SZ300-JK361(Hi) | 052 | humidity, switch | Anion, gear, light, sound, timing, water |
| `132Z` | A.O.史密斯甲醛净化器800C+/700C | 800C+/700C | 013 | brightness, switch | PM25, childLock, countdown, detection, faultCode, filter1, filter2, filter3, filterNet, formaldehyde, gasLevel, modeActive, windCount, windSpeed, workMode |
| `133P` | FSL单色智能天花灯 | FSL-THD-DW | 01B | brightness, switch | — |
| `134F` | 祝眠白噪音暖光灯 | DP-011 | 01B | brightness, switch | FanSwitch, WindSpeed |
| `135K` | 红日吸油烟机JE7316i | CXW-260-JE7316i | 021 | mode, switch | Delayshudown, LEDLightSwitch, gear |
| `137E` | 弩牌智能无叶风扇 | CR013F | 029 | mode, switch | autoOff, onOffBeep, speedPercent |
| `138O` | 空调控制器 | hv100 | 012 | mode, switch | currentTemperature, targetTemperature, wind |
| `138Q` | 迷你水暖机 | AH-009H | 06A | mode, switch | faultDetection, gear |
| `140B` | CM智能窗帘电机 | CM_190901_V01 | 01C | mode, opener | Setting |
| `153Y` | 平头熊智能窗帘电机 | PTX-820HN | 01C | mode, opener | Curtainjz, Curtainzfz |
| `155A` | A.O.史密斯甲醛净化器455C-FH | 455C-FH | 013 | brightness, switch | PM25, childLock, countdown, detection, faultCode, filter1, filter2, filter3, formaldehyde, gasLevel, modeActive, windCount, windSpeed, workMode |
| `155C` | A.O.史密斯甲醛净化器400C-FH | 400C-FH | 013 | brightness, switch | PM25, childLock, faultCode, filter1, filter2, filter3, formaldehyde, modeActive, windSpeed, workMode |
| `157Y` | 威廷智能双开Wi-Fi | VE-AK02LNW | 005 | switch1, switch2 | — |
| `162L` | 创明智能窗帘 | S410 | 01C | mode, opener | Changedirection, EnHandtomove |
| `162X` | 卡赫智能净水器WPD60-P | WPD60-P | 02D | childLockSwitch, status | Temp, TotalWater, VolumPerCup, faultDetection, filterElement1, filterElement2, filterElement3, inputTds, outputTds |
| `163O` | 窗帘电动轨道 | Bcm Series | 01C | mode, opener | — |
| `163S` | 维尔森VERSON智能窗帘 | VE-DC65 | 01C | action, opener | — |
| `164A` | 智能双开开关 | VE-AK02LNB | 005 | switch1, switch2 | — |
| `164E` | 达伦护眼台灯T1 | DL-02W | 046 | brightness, switch | WIFIledSwitch, classroom |
| `164V` | 力博得智能声波牙刷 星芒 | LBT-203552B | 073 | mode, status | brushDay, brushScore, brushingHistory , misicState |
| `170E` | 雷士护眼灯 | Q10A | 046 | brightness, switch | autoAdjust, backlight, countdown, rest |
| `172O` | 安士宝智能奶瓶 | ANS-ZY-D-002 | 06B | battery, status | childLock, currentTemp, disinfect, disinfectRec, heat, heatTemp |
| `174F` | 安吉尔净水器 | J2747-ROB60 | 02D | status, switch | Flush, Inputquality, Outputquality, Outputtemperature, Waterquantity, faultDetection, filterElement1, filterElement2, filterElement3 |
| `175S` | 平头熊二键开关WIFI | PTX-TCswitch02 | 005 | switch1, switch2 | — |
| `175U` | 奥普浴霸轻智 | QDP3622AHW | 035 | lightSwitch, mode | NightLight, leftTime |
| `178F` | 居意电动窗帘 | C6 | 01C | mode, opener | State |
| `178K` | 亚都加湿器SZ300-JK262Hi | SZ300-JK262(Hi) | 052 | humidity, switch | Anion, gear, light, sound, timing, water |
| `178Z` | 奥普浴霸QDP2826AHW | QDP2826AHW | 035 | lightSwitch, mode | NightLight, leftTime, swingSwitch |
| `181T` | 碧云泉家用净水机U35 | JST-U35 | 02D | status, temperature | QuantifyWater, attemperation, faultDetection, filterElement1, filterElement2, purifyWater |
| `181U` | 碧云泉家用净水器R302D | JST-R302D | 02D | status, temperature | QuantifyWater, attemperation, faultDetection, filterElement1, filterElement2, filterElement3, inputTds, outputTds, purifyWater |
| `182Z` | 达伦护眼台灯 | DL-27W | 046 | brightness, switch | classroom |
| `183D` | 噼啪智能双开开关 | PIPA-AK02LNW | 005 | switch1, switch2 | — |
| `200D` | A.O.史密斯甲醛净化器455C+ | FPH series | 013 | brightness, switch | PM25, childLock, countdown, detection, faultCode, filter1, filter2, filter3, filterNet, formaldehyde, gasLevel, modeActive, windCount, windSpeed, workMode |
| `200P` | 麦乐克烟雾传感器 | MIR-SM100 | 039 | alarm, battery | Error, TamperAlarm |
| `200T` | 麦乐克人体传感器 | MIR-IR100 | 03E | battery, status | motionDetected |
| `200Y` | 麦乐克水浸传感器 | MIR-WA100 | 03C | alarm, battery | — |
| `2014` | 麦乐克门窗传感器 | MIR-MC100 | 018 | battery, status | TamperAlarm, doorEvent |
| `2019` | 烁为汽车氛围灯 | FW-1001 | 0A6 | brightness, switch | atmospherebrightness, contourbrightness, customcolor, lightcolor, lightswitch, model |
| `202K` | 小熊智能加湿器 | JSQ-E40P3 | 052 | humidity, switch | BactericidalFunction, TargetHumidity, TimingShutdown, faultDetection, gear |
| `2035` | 卡赫智能净水器 600G | V1.0 | 02D | status, switch | contWater, filterElement1, filterElement2, filterElement3, inputTds, outputTds, purifyWater |
| `204J` | 倍觅智能驱蚊器 | CU1 | 0B0 | mode, switch | batteryindicator, circular, moodLight, workStatus |
| `204O` | 蓓慈BA502V1护眼仪 | BA502V1 | 000 | mode, switch | airPressureOnOff, lefttime, musicSwtich, tempSwtich, vibratingOnOff, volume, workstatus |
| `2053` | 百斯腾温润速热暖风机 | HF12TB | 06A | childLockSwitch, switch | gear |
| `206P` | 欧智通-智能吸顶灯 | 6110R-IX | 01B | brightness, switch | — |
| `2074` | 威仕达天玑星 | WSCMJ-2 | 01C | mode, opener | operation |
| `207A` | 博乐宝净饮机B16 | B16-R100 | 02D | childLockSwitch, status | capmodestate, faultDetection, filterElement1, outletWater, rinseMode1, watertypestate |
| `207N` | 领普单键零火开关MESH | Q4D-BLE-W1(HW) | 005 | brightness, switch | button1, mode1 |
| `208Y` | 酷轻松石墨烯发热暖脚宝 | K-NJB-B2V4 | 0D0 | switch, temperature | heat, timerlabel, workstatue |
| `2094` | 松堡王国儿童智能安睡枕 | SP-A-AI002 | 054 | battery, status | Power, RealtimeHR, RealtimeRR, led |
| `20BQ` | 天智星 | WSCMQ-2/12 | 01C | mode, opener | operation |
| `20DF` | 永林单色调光器 | PLH-LB1X40-20-XL1 | 01B | brightness, switch | — |
| `20FL` | 新日电动车F5 | XR1200DT-2L | 0C7 | alarm, switch | NFC, OTA, carLock, diagnosis, openSeat, powStatus, remainEle, remainKm |
| `20FN` | 海令单路调光器 | SMK-H1-PWM1 | 01B | brightness, switch | — |
| `20G4` |  | SMK-DG-002 | 01C | mode, opener | — |
| `20GO` | 摩根调光灯 | 1.0 | 044 | brightness, switch | — |
| `20GQ` | 360扫地机器人X90 | X90 | 031 | action, status | — |
| `20HW` | 达伦自然光护眼台灯 | DL-NTLW | 046 | brightness, switch | classroom |
| `20ID` | 星团智能驱蚊器 | CU2 | 0B0 | mode, switch | once, switchLight, timeRemaining, workStatus |
| `20J6` | 咪呵智能窗帘电机 | ME820H | 01C | mode, opener | Curtainjz, Curtainzfz |
| `20J7` | 米亚智能窗帘电机 | MT800-W | 01C | mode, opener | Curtainjz, Curtainzfz |
| `20JS` | 霍夫曼开合帘 | 1.0 | 01C | mode, opener | — |
| `20L1` |  | SMK-DG-003 | 04D | mode, opener | — |
| `20MH` | 八键场景面板尊享版 | BL8030RC2-B2 | 075 | switch1, switch2 | backlightMode |
| `20P8` | 奥普浴霸炫彩 | QDP2826BHW | 035 | lightSwitch, mode | NightLight, leftTime, swingSwitch |
| `20QV` | 四键场景面板时尚版 | BL8025RP4-E1 | 075 | switch1, switch2 | backlightMode |
| `20QW` | 四键场景面板尊享版 | BL8028RC2-E1 | 075 | switch1, switch2 | backlightMode |
| `20QZ` | 欧派油烟机 | CXW-140-E908X | 021 | lightSwitch, mode | faultDetection, gear, power |
| `20R1` | 四键场景面板尊享版 | BL8028RC2-L1 | 075 | switch1, switch2 | backlightMode |
| `20R3` | 四键场景面板尊享版 | BL8028RC2-K1 | 075 | switch1, switch2 | backlightMode |
| `20R4` | 四键场景面板尊享版 | BL8028RC2-T1 | 075 | switch1, switch2 | backlightMode |
| `20R7` | 六键场景面板尊享版 | BL8029RC2-D1 | 075 | switch1, switch2 | backlightMode |
| `20R9` | 六键场景面板尊享版 | BL8029RC2-R1 | 075 | switch1, switch2 | backlightMode |
| `20RE` | 六键场景面板尊享版 | BL8029RC2-M1 | 075 | switch1, switch2 | backlightMode |
| `20RH` | 八键场景面板时尚版 | BL8027RP4-B1 | 075 | switch1, switch2 | backlightMode |
| `20RJ` | 八键场景面板尊享版 | BL8030RC2-B1 | 075 | switch1, switch2 | backlightMode |
| `20RM` | 八键场景面板时尚版 | BL8027RP4-B2 | 075 | switch1, switch2 | backlightMode |
| `20RT` | 八键场景面板时尚版 | BL8027RP4-L1 | 075 | switch1, switch2 | backlightMode |
| `20RX` | 八键场景面板尊享版 | BL8030RC2-L1 | 075 | switch1, switch2 | backlightMode |
| `20S0` | 八键场景面板时尚版 | BL8027RP4-S1 | 075 | switch1, switch2 | backlightMode |
| `20S1` | 八键场景面板尊享版 | BL8030RC2-S1 | 075 | switch1, switch2 | backlightMode |
| `20S9` | 八键场景面板尊享版 | BL8030RC2-B3 | 075 | switch1, switch2 | backlightMode |
| `20SC` | 八键场景面板尊享版 | BL8030RC2-D1 | 075 | switch1, switch2 | backlightMode |
| `20SD` | 八键场景面板尊享版 | BL8030RC2-L2 | 075 | switch1, switch2 | backlightMode |
| `20SM` | 欧派油烟机 | CXW-150-E908T | 021 | lightSwitch, mode | faultDetection, gear, power |
| `20TB` | 美菱茶吧机 | MY-YT917 | 09A | status, switch | WaterHealthPot, WaterKettle, curtemp, faultDetection, heat, heattemp, warm |
| `20TK` | 易百珑单路开关 | EWS01-H | 064 | switch, switch1 | CleanPair, Pair, memorySwitch |
| `20TN` | 亚摩斯料理破壁机AS-PB60B | AS-PB60B | 05A | action, status | faultDetection, gear, leftTime, modeRecipes, stirAction, stirWorkTime, timing, timingSwitch, workTime |
| `20X9` | 脊安适按摩器G6 | G6 | 0CE | mode, switch | batteryLevel, connectStatus, heatLevel, massageTime, remainTime, strength |
| `20XP` | 控客-星空双路灯控面板 | KK-LP-L02W | 005 | switch1, switch2 | — |
| `20Y9` | 好太太智能晾衣机HP-D204-2BS | HP-D204-2BS | 028 | action, lightSwitch | airDry, airDryRemTime, airDryTime, commonFaultDetection, disinfect, dryRemTime, dryTime, drying |
| `20YS` | 控客-声光报警器 | KK-VA-J01W | 040 | battery, switch | volume |
| `20YT` | 控客-烟雾报警器 | ZX-SA-J01W | 039 | alarm, battery | commonFaultDetection, dismantle |
| `20ZS` | 控客-双路灯控模块 | KK-LM-A12 | 064 | switch1, switch2 | — |
| `213W` | 西顿调光模块 | SWP01-QL-20W-1 | 044 | brightness, switch | — |
| `214Q` | 智能颈椎按摩仪 | HT-304 | 0CA | mode, switch | countdown, heat, intensity, leftTime, power |
| `2157` | 九赞猫咪智能保温杯 | H6 | 06B | battery, temperature | alarmTime1, connectStatus |
| `215D` | 西顿恒压调光模块 | SWP01-QY-100W-1 | 044 | brightness, switch | — |
| `215S` | 智能门窗磁 | U4080500 | 018 | battery, status | doorEvent |
| `215U` | 漏水检测器 | U4040500 | 03C | alarm, battery | — |
| `2162` | 智能窗帘电机 | U4070106 | 01C | mode, opener | — |
| `216L` | HEIMAN智能门窗传感器 | HS1DS-BH | 018 | battery, status | doorEvent, temperAlarm |
| `216S` | HEIMAN智能水浸报警器 | HS2WL-BH | 03C | alarm, battery | iceAlarm, silencer |
| `216U` | HEIMAN智能烟雾报警器 | HS1SA | 039 | alarm, battery | selfCheck |
| `2182` |  | KK-KP-D01W | 018 | battery, status | doorEvent |
| `219G` | FSL智曜读写台灯 | FSL-ZNDXTD2231 | 046 | brightness, switch | tomatoClk |
| `219L` | 脉冲颈椎智能按摩仪 | U3 | 0CA | mode, switch | commonFaultDetection, heat, strength, voiceSwitch |
| `21A8` | HEIMAN智能一氧化碳报警器 | HS1CA-BH | 03A | alarm, battery | selfCheck |
| `21BF` | 圆和一路智能开关 | X9ZK1 | 005 | switch, switch1 | — |
| `21BM` | 云起水浸感应器 | LS064WH | 03C | battery, status | — |
| `21D9` |  | LS086WH | 03A | action, status | gas, sensitivity |
| `21DD` |  | LS133WH | 01C | mode, opener | — |
| `21DH` |  | LS058WH | 018 | battery, status | doorEvent |
| `21DI` |  | LS062WH | 03E | battery, luminance | motionDetected |
| `21ED` | JW智能照明调光灯 | JHKJ_DL_V1 | 01B | brightness, switch | — |
| `21ER` | JW智能地暖 | JHKJ_FH_V1 | 06A | switch, temperature | — |
| `21GJ` | JW空气检测E型 | 1 | 006 | humidity, temperature | — |
| `21GL` | JW智能开关2键型 | JHKJ_PANEL_KEY2 | 005 | switch1, switch2 | — |
| `21JB` | 阳光照明灵睿智能灯泡调光版 | BPZ600-840-7WZ | 01B | brightness, switch | — |
| `21JH` | 新日电动车XC3 | TDT0550Z | 0C7 | alarm, switch | OTA, carLock, diagnosis, powStatus, remainEle, remainKm |
| `21JP` | 西顿杀菌厨卫灯 | CEW12R | 01B | lightMode, switch | — |
| `21LB` | 永林恒压调光驱动 | PLH-LA1X24-100-AL2 | 044 | brightness, switch | — |
| `21LG` | 米立2路智能开关面板 | MS-V8612G | 005 | switch1, switch2 | — |
| `21LY` | 平头熊智能卷帘电机 | PTX-R35T | 04D | action, opener | calibration, rotation |
| `21ME` | ULTTY-空气净化冷暖风扇 | SKJ-CR025H | 029 | humidity, switch | Gear, autoMode, childLock, commonFilterElement1, hotMode, nowTemp, onOffBeep, setTemp, sleepMode, strongMode, swing, uvcEn |
| `21OR` | A.O.史密斯壁挂炉 | L1PB37-V9 | 027 | mode, switch | faultDetection, heatingSwitch, heatingTemperature, heatingTimer, waterControl, waterTemperature, waterTimer |
| `21P0` | 中菱智能卷帘电机 | ZL-R35T | 04D | action, opener | calibration, rotation |
| `21P1` | 致尚智能窗帘电机 | ZS-82TN | 01C | mode, opener | Curtainjz, Curtainzfz |
| `21PC` | 调光灯（照明调光器） | CP2003H | 044 | brightness, switch | — |
| `21PQ` | 水浸传感器 | LH-65 | 03C | battery, status | — |
| `21Q8` | 科创者智能窗帘电机 | KCZ-82TN | 01C | mode, opener | Curtainjz, Curtainzfz |
| `21SD` | RGB调色灯带（灯带调光器） | CP2201H | 01B | colour, switch | — |
| `21SF` | RGBW调色灯带（灯带调光器） | CP2201H | 01B | colour, switch | — |
| `21U1` | 孩视宝智能面加环读写台灯 | OG235B-AI | 046 | brightness, switch | CurrentBrightness, CurrentColorTempurature, NaturalSleep, NightlightMode, SmartLight, TimedReminder, cctmode |
| `21U2` | 孩视宝智能长条形落地灯 | FS706-AI | 01B | brightness, switch | FocusOnPractice, FragmentPractice, NaturalSleep |
| `21UK` | 达伦自然光台灯T3 Pro | DL-35W | 046 | brightness, switch | AutoAMode, ColorTempStep, WIFIledSwitch, WithSleepMode, classroom |
| `21V4` | 瑞晶空气净化器 | RGBLE-R-AM | 013 | fan, switch | — |
| `21V7` | 瑞晶湿度控制器 | RGBLE-R-HM | 09B | humidity, switch | gear |
| `21V8` | 瑞晶四合一传感器 | RGAIRQ | 006 | humidity, temperature | CO2, PM2.5 |
| `21VG` | FSL智影炫彩灯带-2米 | ST-5W2ZY | 01B | brightness, switch | Create, commonMode1, commonMode2, progressTurnOff, progressTurnOn |
| `21VV` | 雷士护眼台灯-银河 | Q999 | 046 | brightness, switch | Auto, Autodimming, RestTime, nlight, rest |
| `21VX` | 瑞晶亮度感应器 | RG-BND | 048 | battery, luminance | — |
| `21W2` | 瑞晶调光灯 | RGBLE-R-L2 | 01B | brightness, switch | — |
| `21WF` | 雷士护眼台灯-米娜 | Q998 | 046 | brightness, switch | Breaks, RestTime |
| `21WG` | 雷士护眼台灯-云光 | TDLP1091NWD1-DG-CN | 046 | brightness, switch | commonMode1 |
| `21X9` | 海盐电热热敷垫 | MZ65x28-1 | 0CA | status, switch | control, realtime |
| `21XI` | 瑞晶红外探测器 | RG-IR | 049 | battery, status | motionDetected |
| `21XM` | 瑞晶水浸探测器 | RG-GAS24A | 03C | alarm, battery | — |
| `21XN` | 瑞晶门窗感应器 | RG-GM | 018 | battery, status | doorEvent |
| `21XP` | 瑞晶报警器 | RG-ALMU | 040 | battery, switch | — |
| `21XQ` | 瑞晶烟雾探测器 | RG-SMO24A | 039 | alarm, battery | — |
| `21Z6` | P50 Pro环闪保护壳 | JADE-RC | 000 | brightness, switch | Callflash, Colortemperature, Devicestatus, Entertainmentlighting, Firmwareupdate, Oneclicklight, conectstatue |
| `21ZU` | 蓓慈BA502E1护眼仪 | BA502E1 | 000 | mode, switch | airPressureOnOff, lefttime, musicSwtich, tempSwtich, vibratingOnOff, volume, workstatus |
| `220W` | 智能毛巾烘干机 | MJ01 | 0BA | switch, temperature | Mode, TimeCountDown, TimeFormat, WorkState, WorkTimer |
| `221F` |  | GF980TV-P | 01C | mode, opener | — |
| `221J` |  | A3Z-SNWK-01 | 06A | switch, temperature | — |
| `221O` |  | T-GAS30 | 03A | alarm, battery | — |
| `221Q` |  | T-WAT30 | 03C | alarm, battery | — |
| `221R` |  | A3Z-XFWK-01 | 030 | fan, switch | — |
| `221Z` |  | S-M30 | 04B | alarm, battery | doorEvent, keyList |
| `2220` |  | S-M50 | 04B | alarm, battery | doorEvent, keyList |
| `223W` | 鸿蒙智选儿童智能牙刷 | LBT-153015A | 073 | mode, status | — |
| `2241` | 杜亚智能窗帘HL1 | HL1 | 01C | mode, opener | commonFaultDetection |
| `224B` |  | CP2002H | 01B | brightness, switch | — |
| `224C` |  | CP2005H | 01B | brightness, switch | — |
| `224R` |  | CP8231H | 06A | switch, temperature | — |
| `227U` | 亚摩斯睿雅零火开关单键 | ZJ-KG35H | 005 | brightness, switch | — |
| `22C1` | 同屏器 | NC-812-16XS | 003 | action, switch | hdmiMode, overscan, player, volume |
| `22C5` | 本博按摩枕 | AM-708HW | 0CA | mode, switch | countdown, hot, speedRegulation, timeLeft |
| `22C7` | 本博按摩枕 | AM-509HW | 0CA | mode, switch | countdown, remainingTime, speedRegulation, vibrationMassage, warmCompress |
| `22CX` | 新日电动车F3 | XR800DQT-5G | 0C7 | alarm, switch | NFC, OTA, carLock, diagnosis, openSeat, powStatus, remainEle, remainKm |
| `22D5` | 捷昌智能窗帘 | JCC50STEW05 | 01C | action, opener | — |
| `22E2` | 八键场景面板时尚版 | BL8053R | 075 | switch1, switch2 | backlightMode |
| `22E3` | 八键场景面板尊享版 | BL8037R | 075 | switch1, switch2 | backlightMode |
| `22G4` | 新日电动车MIKU1 | TDQ0610Z | 0C7 | alarm, switch | OTA, carLock, diagnosis, powStatus, remainEle, remainKm |
| `22G5` | 新日电动车K2 | TDT4780Z | 0C7 | alarm, switch | OTA, carLock, diagnosis, powStatus, remainEle, remainKm |
| `22H8` | 新日电动车XO2 | TDT0560Z | 0C7 | alarm, switch | OTA, carLock, diagnosis, powStatus, remainEle, remainKm |
| `22HQ` | 美森智能声波牙刷 | WHR1 | 073 | battery, mode | F001, F002, F003, brushingHistory, filterElement, gear, setWorkTime |
| `22II` | 格林盈璐无雾加湿器 | FHM-107 | 052 | status, switch | FilterLife, HumidityS, KeepHumi, Level, Time, speed |
| `22RG` | 北冥小鱼智能跳绳S1 | beimingxiaoyu S1 | 095 | battery, mode | ID, calorie, count |
| `22S6` | 御芳华按摩仪 | CQ-PD10S | 0D0 | switch, switch1 | Time, electricity, model, stage, workStatus, worktime |
| `22SL` | 奥佳华颈肩按摩器 | OG2610 | 0CA | alarm, switch | KnockingSpeed, classic, electricity, heat, stop, surTime, suspend |
| `22ZK` | Evoyo水浸传感器 | MSW01/M-ZB.10 | 03C | alarm, battery | — |
| `22ZV` | Evoyo一路调光器小模块 | MPD0101-ZB.10 | 01B | brightness, switch | — |
| `22ZX` | Evoyo窗帘电机 | MWM65B-ZB.20 | 01C | action, opener | — |
| `22ZZ` | Evoyo烟雾传感器 | MSS01/M-ZB.10 | 039 | alarm, battery | — |
| `2300` | Evoyo门窗传感器 | MSDC01/M-ZB.10 | 018 | battery, status | — |
| `23FM` | 亚摩斯智能推窗器 | ZJ-TC01H | 02C | action, opener | level, reverse |
| `23GN` | 新日电动车GF6 | XR1200DT-5K | 0C7 | alarm, switch | NFC, OTA, carLock, diagnosis, openSeat, powStatus, remainEle, remainKm |
| `23SW` | 波可龙高速电吹风 | HD0801 | 0E4 | mode, status | connectStatus, guid, question, recommend, windSpeed |
| `23VR` | 新日电动车FN3 | TDT9291Z | 0C7 | alarm, switch | NFC, OTA, carLock, diagnosis, openSeat, powStatus, remainEle, remainKm |
| `241D` | 达伦自然光台灯T3 RS | 3T | 046 | brightness, switch | classroom |
| `242T` | 格林盈璐无雾加湿器 | FHM-110 | 052 | status, switch | FilterLife, HumidityS, KeepHumi, Level, Time, speed |
| `2434` | 怀里智能浴宝 | HL-YB-X7 | 035 | switch, temperature | DSFUNC, DSTime, HWFUNC, LFFUNC, QNFUNC, WDSet, XDFUNC |
| `2458` | 欧浦立智能门锁 | X10H | 04B | alarm, battery | event, lockState |
| `246B` | 赋安烟感报警器 | JTY-GM-FS3033 | 039 | alarm, battery | commonFaultDetection, pollute, remoteEnable, remoteOperate, smokeState, tamper |
| `2477` | 贝克巴斯食物垃圾处理器 | ELEMENT-60PRO | 0B6 | mode, switch | Reverse, conserve |
| `247P` | 电吹风VC精华智能款 | VC-H100A | 0E4 | mode, status | Airshow, CustomerService, Drynessratedisplay, UsingRecord, VCUsingTime, motorspeed, temperaturedisplay |
| `248F` | 石将军智能门锁 | S3H | 04B | alarm, battery | event, lockState |
| `249F` | 格里维尔高端智能门锁 | i6H | 04B | alarm, battery | event, lockState |
| `24B3` | 卷发器-罗曼智能小芭蕾 | HH80 | 000 | battery, switch | commonFaultDetection, rollDegree, workStatus, workTime |
| `24DE` | 万达康健身律动机 | RNF-71 | 0C2 | mode, switch2 | cal, changeSpeed, changeTime, data, eCalorie, eTime, music, speed, turn, video |
| `24DM` | 亚摩斯读写台灯 | DL-06W1SH | 046 | brightness, switch | progressTurnOff, tomatoClk |
| `24EN` | 华督小型即热饮水机 | D3 | 06F | childLockSwitch, status | ONOFF, Temp, WaterVolume, currentOutlet, faultDetection |
| `24FQ` | 新日电动车UF3 | TDT9290Z | 0C7 | alarm, switch | NFC, OTA, carLock, diagnosis, powStatus, remainEle, remainKm |
| `24G6` | 新日电动车QM2 | TDT4920Z | 0C7 | alarm, switch | NFC, OTA, carLock, diagnosis, powStatus, remainEle, remainKm |
| `24GR` | 吉米康智能眼部按摩仪 | 9S | 0CA | status, switch | Electricity, SleepMode, SoothingMode, SyntaxicMode, VitalityMode, Voice, commonFaultDetection, gear |
| `24HL` | FOOXMET智能温控围巾 | ZL-WK-001 | 07C | switch, temperature | commonFaultDetection, tempDown |
| `24PV` | 亦生堂臂式电子血压计 | JN-163D | 02B | status, switch | commonMemorySwitch1, electricValue, highPressure, historyData, lowPressure, measure, pressure, privacyStatement, pulse, statistics |
| `24R6` | 华督桌面即热饮水机 | H2 | 06F | childLockSwitch, status | ONOFF, WaterVolume, currentOutlet, faultDetection, temp |
| `24T9` | OES按摩枕 | OES-509HW-N | 0CA | mode, switch | cuntdown, remainingTime, speedRegulation, vibrationMassage, warmCompress |
| `24WB` | FOOXMET智能温控马甲 | ZL-WK-002 | 07C | switch, temperature | commonFaultDetection, tempDown |
| `24WC` | FOOXMET 智能温控裤 | ZL-WK-004 | 07C | switch, temperature | commonFaultDetection, tempDown |
| `24WD` | FOOXMET智能温控服 | ZL-WK-003 | 07C | switch, temperature | commonFaultDetection, tempDown |
| `25B7` | 三耐科智能擦窗机器人 | TS-01 | 000 | mode, switch | devState |
| `25BD` | 爱特嘉智能即热饮水机AH-103 | AH-103 | 06F | status, temperature | currentOutlet, faultDetection, outlet, waterMode |
| `25BF` | MPE乳胶枕 | MPE-Z101 | 054 | battery, status | led, power, realtimeHR, realtimeRR |
| `25BG` | 得力保管箱 | 27321C | 08B | battery, switch | alarms, events, lockState, lockStatus |
| `25BR` | 沃荷智能枕 | WO-Z001 | 054 | battery, status | led, power, realtimeHR, realtimeRR |
| `25BS` | 斯尼恩智能枕 | Z21728 | 054 | battery, status | RealtimeHR, RealtimeRR, led, power |
| `25DF` | 华督桌面即热饮水机 | D4 | 06F | childLockSwitch, status | ONOFF, WaterVolume, currentOutlet, faultDetection, temp |
| `25EN` | 达伦自然光台灯T3E | DL-30W | 046 | brightness, switch | WIFIledSwitch, classroom |
| `25GH` | 亚摩斯窗帘电机WiFi版 | AS-CL06H | 01C | action, opener | — |
| `25H8` | 俞福智能枕 | YU-ZT9910 | 054 | battery, status | led, power, realtimeHR, realtimeRR |
| `25I9` | 奥佳华按摩椅 OG-8598Plus | OG-8598Plus | 05F | action, switch | AUTO, Customized, DIY, Heat, autoMode, backAction, heatMode, legAction, soleSwitch |
| `25ND` | 得力保管箱 | 27322C | 08B | battery, switch | alarms, events, lockState, lockStatus |
| `25NE` | 得力保管箱 | 27323C | 08B | battery, switch | alarms, events, lockState, lockStatus |
| `25NG` | 得力保管箱 | 33695C | 08B | battery, switch | alarms, events, lockState, lockStatus |
| `25NI` | 得力保管箱 | 33696C | 08B | battery, switch | alarms, events, lockState, lockStatus |
| `25NJ` | 得力保管箱 | 33697C | 08B | battery, switch | alarms, events, lockState, lockStatus |
| `25OS` | 探梦者智能电动滑板车 L1 MAX | L1 MAX | 094 | lightMode, switch | Electricity, Headlight, Locked, RestoringFactory, StepLight, TheMileage, Unlocked, VehicleSelfCheck, WorkStatus, color, cruise, firmwareUpgrade, lowPower, speed, speedControl, speedUnit, startupSetting, totalMileage |
| `25PZ` | 探梦者智能电动滑板车 L1 PRO | L1 PRO | 094 | lightMode, switch | Electricity, Headlight, Locked, RestoringFactory, StepLight, TheMileage, Unlocked, VehicleSelfCheck, WorkStatus, color, cruise, speed, speedControl, speedUnit, startupSetting, totalMileage |
| `261F` | Freya床头灯 | BL1H | 10E | brightness, switch | Piano, Sleep, WakeUp |
| `2657` | 清易智慧集尘扫拖机器人H40 PLUS | QYSDJ10 | 031 | action, mode | areaSetting, cleanRecord, commonFaultDetection, deviceStatus, edgeElement, hepaElement, mapService, musicPackage, ossSN, path, remoteControl, rollElement, scheduleService, sensor, startClean |
| `269M` | 西马智能马桶 | CB-V86Hm | 066 | mode, switch | autoFlush, deodorizeSwitch, dryGear, eco, faultDetection, flush, heatGear, hipTime, intensity, led, longSeat, longSeatOPT, massage, nozzlePosition, onSeat, sound, waterTemp, womenTime |
| `26FB` | 暖桌宝 | V80 | 197 | switch, temperature | Drinkingtone, Sedentaryremindertime, Sedentarytone, watertime |
| `26G2` | 捷昌智能百叶帘电机 | JCV24SAEDW05 | 0B5 | action, opener | openerAngle |
| `26TX` | 酷轻松石墨烯发热护膝 | PMA-O30 | 0CA | switch, temperature | Message, Mode, Remind, heat, timerlabel, workstatus |
| `27NI` | 阳光博鸿读写台灯 | MTSL2007 | 046 | brightness, switch | — |
| `27NX` | WTT智能晾衣架 | UX02_LYJ_DC_Z12 | 028 | action, lightSwitch | airDry, commonFaultDetection, disinfect, drying |
| `27OA` | 博思迪美容仪 | D-1201 | 0EA | status, switch | Lowbatterywarning, bluetooth, firmwareupdate, gear, model |
| `27OD` | 小智K11 智能门锁 | K11 | 04B | alarm, battery | Volume, keyList, lockMode, lockState, openEvent, publicKey, remoteCode, remoteInfo, remoteResult, userlist |
| `27QE` | MOS调光器 | BL2229R | 044 | switch1, switch2 | brightness1, brightness2, fadeTime1, fadeTime2 |
| `27QM` | 红外幕帘传感器 | BL5019R | 03E | alarm, switch | alarmReportSetting, faultDetection |
| `27W8` | 0-10V双色温调光器 | BL2231R | 044 | switch1, switch2 | brightness1, brightness2, cct1, cct2, faultDetection |
| `27WB` | 超静音窗帘电机 SE | BCHP960TLR-1.2/14 | 01C | action, opener | dryContactSetting, faultDetection |
| `27XN` | MARTUBE暖桌宝 | V80 | 197 | switch, temperature | Drinkingtone, Sedentaryremindertime, Sedentarytone, watertime |
| `284J` | 电吹风VC精华二代(智能款) | VCH-200B | 0E4 | mode, status | VCreset, airVolume, dryingRate, motorSpeed, temperatureShow, vcTime |
| `285N` | 暖宫腰带 | HY-NG2115 | 0CA | switch, temperature | Vibrationgear |
| `2881` | 嘟比恒温暖奶器 | QW-NN-03A | 12D | mode, status | CurrentTemperature, DisinfectionTime, Exceptionprompt, MainSwitch, MakeAnAppointment, Nightight, pattern, targetTemperature |
| `2895` | 雅洁3D人脸自动锁F1 | J2051-03 | 04B | alarm, battery | event, hijackAlarm, lockMode, lockState, openEvent, pryAlarm, systemlockAlarm, tonguebadAlarm, userkeyList |
| `28DY` | 博孚梦幻帘 | BFMH-HW60 | 01C | action, opener | dimmer |
| `28HA` | I7智能门锁 | I7 | 04B | alarm, battery | Records, defenseMode, faultCode, lockState, lockStatus, openEvent, userLists |
| `28IO` | 予智生活智能冲牙器 | Moon C6 | 175 | battery, mode | CVTStrengthDef, applicatorTime, batteryAvailable, cleaningRecord, commonFaultDetection, deviceLock, devicestate, instructions, moreSettings, pulseStrengthDef, softStrengthDef, verycoolStrengthDef, workGuidance |
| `28UW` | 洒拖F7智能拖地吸尘器 | F7 | 069 | battery, status | chargLeftTime, filterElement, landLight, leftTime, module, voice, waterSpray, workTime |
| `28WH` | RND可折叠电动滑板车F16 | F16 | 094 | switch, temperature | Power, cruise, distance, electric, light, lock, running, shutdown, speed, state, unit |
| `28XQ` | 佳普乐G3-300A自动翻盖智能马桶 | G3-300A | 066 | mode, status | ECO, cover, dryGear, drySwitch, flush, hPosition, heatGear, hintenty, nightled, seat, sitdown, smart, wPosition, waterTemp, wintenty |
| `28XT` | 佳普乐G3-300N智能马桶 | G3-300N | 066 | mode, status | ECO, dryGear, drySwitch, flush, hPosition, heatGear, hintenty, nightled, sitdown, smart, wPosition, waterTemp, wintenty |
| `28XU` | 佳普乐G3-400N智能马桶 | G3-400N | 066 | mode, status | ECO, dryGear, drySwitch, flush, hPosition, heatGear, hintenty, nightled, sitdown, smart, wPosition, waterTemp, wintenty |
| `2924` | 萌动温控器 | HLA9030DBL | 10D | status, switch | disTemp, fanMod, tempCool, tempHeat |
| `295D` | 奥佳华按摩椅OG7306Pro | OG7306Pro | 05F | action, switch | Faultcode, Zerogravity, autoMode, backadjustment, customize, footroller, heating, legadjustment, times, type, vibration |
| `296V` | LAICA牌KE9402系列净饮机 | KE9402-W | 06F | childLockSwitch, status | Devicerrow, brewtime, cupadjust, cupcheck, currentTemp, lightswitch, menuchoose, outletWater, soundswitch, temperatureadjust, waterMode |
| `299H` | 九牧i4Pro智能马桶ZD7420 | ZD7420-S2-CJM | 123 | status, switch | WarnEvent, control, faultEvent, gear, setting |
| `299N` | 澳柯玛智能燃气热水器16H101 | JSQ30-16H101 | 027 | switch, temperature | TeasonThermal, Zerocoldwater, airflow, antifreezing, booster, code, draughtfan, faultDetection, flame, flow, promotion, waterpump, wateryield |
| `29AF` | MPE太空椅 | C009 | 128 | lightSwitch, switch | Memoryheight, footControl, headControl, heightControl, legControl, modeSelect |
| `29AS` | 赛诺多效护颈智能枕 | PP-674 | 054 | battery, status | HR, led, power, realtimeRR |
| `29DT` | 小适负离子电吹风(智能款) | AH10-W | 0E4 | mode, status | AirVolume, AnionTotal, Class, Feedback, MotorSpeed, Service, Upgrade |
| `29DV` | 小适恒温电吹风(智能款) | AH11-R | 0E4 | mode, status | AirVolume, AnionTotal, Class, Dryingrate, Feedback, MotorSpeed, Service, Temp, Upgrade |
| `29F4` | 红外幕帘传感器 | BL5023R | 03E | alarm, switch | — |
| `29I9` | 乐歌电动升降桌ET223 | ET223 | 164 | action, childLockSwitch | commonFaultDetection, ctrlhight, day, heightfour, heightone, heightthree, heighttwo, line, month, reporthight |
| `29IB` | 安吉尔 A8 Pro | J3309-ROC120H | 02D | status, switch | faultDetection, filterElement1, filterElement2, filterElement3, inputTds, outputTds, totalPurifyWater |
| `29SC` | 行走助力机器人 | Ant-H1 Pro | 230 | mode, switch | SaveOrRecovery, force, remainBattery, report, volume, walkSteps |
| `29U7` | 智能烘干毛巾架 | 9340005-001-1 | 0BA | switch, temperature | autoMode, commonFaultDetection, disinfect, drying, wind |
| `29UP` | 攀高智能颈椎按摩仪 | P7H | 0CA | battery, switch | Heat, Level, Mode, Time, remindWindow, state |
| `29US` | 安博尔茶吧机 | HB-T909 | 1A0 | childLockSwitch, status | KettleTemperature, Refrigeration, commonMode1, commonMode2, commonMode3, commonMode4, commonMode5, faultDetection |
| `29V2` | 万家乐燃气热水器16TX8 | JSQ30-16TX8 | 124 | switch, temperature | Doubleboost, Heatparameter, cmdtype, faultDetection, orderTime, presetSwitch |
| `29X5` | 欧井智能除湿机OJ-136E | OJ-136E | 09B | childLockSwitch, switch | Countdown, HUM, Purify, SetDUM, SetMode, SetSpeed, Temp, commonFaultDetection |
| `29X8` | 欧井智能除湿机OJ-211E | OJ-211E | 09B | childLockSwitch, switch | Countdown, HUM, Purify, SetDUM, SetSpeed, Temp, commonFaultDetection, setMode |
| `29XC` | 欧井智能除湿机OJ-501E | OJ-501E | 09B | childLockSwitch, switch | Countdown, HUM, Purify, SetDUM, SetMode, SetSpeed, Temp, commonFaultDetection, commonFilterElement1 |
| `2A00` | 背景音乐主机 | MT6012H | 0BD | colour, switch | — |
| `2A0F` | 好太太智能晾衣机HP-D204-6BS | HP-D204-6BS | 028 | action, lightSwitch | airDry, airDryRemTime, airDryTime, commonFaultDetection, disinfect, dryRemTime, dryTime, drying |
| `2A1E` | 掌航智能门锁 | Q8H | 04B | alarm, battery | event, lockState |
| `2A22` | eue魔力贴四驱版 | EUEWB001-TQ | 0CA | status, switch | model, part, strength |
| `2A8L` | sraum1路窗帘面板 | SP-A1Z6-SWC | 064 | switch1, switch2 | close, open, scene1, scene2, scene3, scene4 |
| `2A8R` | sraum2路开关面板 | SP-A1Z6-RaF | 005 | switch1, switch2 | scene1, scene2, scene3, scene4 |
| `2AAK` | 艾特双键开关 | ZS122 | 005 | switch1, switch2 | — |
| `2ABJ` | 艾特四键情景面板 | ZP142 | 075 | switch1, switch2 | scenes |
| `2ABM` | 酷轻松石墨烯腿部按摩器 | K-TBAMQ-B2V1 | 0CA | switch, temperature | heat, pat, reminder, timelabel, timer4DeviceOff, workstate |
| `2ABT` | 永林调光驱动 | PLH-LB1X40-20-XL1 | 044 | brightness, switch | — |
| `2ACA` | 酷轻松石墨烯真丝围脖 | K-WB-B2V3 | 0D0 | switch, temperature | heat, timerlabel, workstate |
| `2ACH` | 晚安智能床垫 | Z400TWP | 05D | action, status | bedStatus, sleep |
| `2ACV` | 开合帘 | CHP300TE-1.2/14 | 01C | mode, opener | — |
| `2ACW` | 推窗器 | WP56TS | 02C | action, opener | — |
| `2ACY` | 卷帘 | BHP25TEQ | 04D | action, opener | — |
| `2ACZ` | 卷帘（高扭矩版） | BHP35EQ | 04D | action, opener | — |
| `2ADG` | 酷轻松智能热敷包 | K-RFB-B2V1 | 0D0 | switch, temperature | heat, timelabel, workstatue |
| `2AE0` |  | KK-DP-D11W | 044 | brightness, switch | fadeTime |
| `2AE9` |  | KK-WA-J01W | 03C | alarm, battery | — |
| `2AK8` | 艾特新风控制器 | ZN112 | 030 | fan, switch | — |
| `2AM5` | LUFTRUM多功能循环扇 | Luftrum-FC600H | 013 | fan, switch | Shake, commonFaultDetection, commonMemorySwitch1, countdown, filterElement1, workmode |
| `2AMM` | 欧派智能坐便器 | OP-W7134RGX-305 | 066 | lightSwitch, mode | autoFlushSwitch, dryGear, energySavingSwitch, faultDetection, flushSwitch, heatGear, massageSwitch, position, reciprocateSwitch, waterPressure, waterTemp |
| `2ANH` | 杜亚智能窗帘DT270 | DT270 | 01C | mode, opener | commonFaultDetection |
| `2ANI` |  | U2-86QMP-Z02(HW) | 030 | fan, switch | — |
| `2ANK` |  | U2-86QMP-Z02(HW) | 012 | switch, temperature | — |
| `2AOQ` | 杜亚智能窗帘DH6 | DH6 | 01C | mode, opener | — |
| `2AP0` | 鸿雁双键智能开关U2 | U2-86K21ND10-ZD(HW) | 005 | switch1, switch2 | indicator |
| `2AQO` | 鸿蒙智选 智能台灯2i | DL-01W | 046 | brightness, switch | — |
| `2AQZ` | 调光灯带（灯带调光器） | CP2201H | 01B | brightness, switch | — |
| `2ASS` | 创明智能窗帘 | 230-WiFi | 01C | mode, opener | workmode, workstatus |
| `2AU0` | 致尚智能卷帘电机 | ZS-R35T | 04D | action, opener | calibration, rotation |
| `2AV0` | 米亚智能卷帘电机 | MT-R35T | 04D | action, opener | calibration, rotation |
| `2AX0` | 创明智能窗帘 | AG40RE-WiFi | 04D | action, opener | LimitSet, rotation |
| `2B2R` | FSL智搏读写台灯 | FSL-TD79 | 046 | brightness, switch | progressTurnOff, tomatoClk |
| `2B31` | 左点智能足蒸器Z8 | ZD-Z8 | 070 | action, switch | volume |
| `2B59` | MixSwitch超级智能开关-二开 | T40W2Z | 005 | switch1, switch2 | — |
| `2B8L` | 优家明创智能毛巾机 | MJ03 | 0BA | switch, temperature | Mode, TimeCountDown, TimeFormat, WorkState, WorkTimer |
| `2BDD` | 单色温灯带调光驱动器 | BL2216R | 01B | brightness, switch | — |
| `2BDP` | 壁挂式水浸传感器套装 | BL5051R | 03C | alarm, switch | — |
| `2BE5` | 麦乐克门窗开关传感器 | MIR-MC100 | 018 | battery, status | doorEvent, temperAlarm |
| `2BE6` | 麦乐克红外人体移动传感器 | MIR-IR100 | 03E | battery, status | motionDetected |
| `2BE7` | 麦乐克水浸传感器 | MIR-WA100 | 03C | alarm, battery | — |
| `2BE9` | 麦乐克声光报警器 | MIR-SR100 | 040 | lightSwitch, switch | alamTime, temperAlarm, volume |
| `2BF3` | 门磁传感器套装 | BL5056R | 018 | status, switch | — |
| `2BGD` | 欧普智能射灯 | LTH010603LT | 01B | brightness, switch | commonMemorySwitch1 |
| `2BN4` | 映趣剃须刀 | BlackStone 3 | 000 | mode, switch | BatteryLevel, CleanRemind, NetworkStatus, history |
| `2BOE` | 堡丽调光灯（照明调光器） | BL2006H | 044 | brightness, switch | — |
| `2BOG` |  | BL2002H | 01B | brightness, switch | — |
| `2BOH` |  | BL2005H | 01B | brightness, switch | — |
| `2BOJ` | 堡丽调光灯带（灯带调光器） | BL2201H | 01B | brightness, switch | — |
| `2BOL` | 堡丽RGB调色灯带（灯带调光器） | BL2201H | 01B | colour, switch | — |
| `2BON` | 堡丽RGBW调色灯带（灯带调光器） | BL2201H | 01B | colour, switch | — |
| `2BOU` |  | BL8231H | 06A | switch, temperature | — |
| `2BT5` | 一维香薰机 | EWH-1207 | 04C | luminance, switch | atomization |
| `2BVL` | 噼啪智能窗帘电机 | PIPA-DZ02 | 01C | mode, opener | Curtainjz, Curtainzfz |
| `2BVY` | 阳光照明插电感应夜灯 | YGS-YD0922-2W | 03E | status, switch | lightmode, motionDetected |
| `2C5N` | 堡丽开合帘 | BCHP620E | 01C | mode, opener | — |
| `2C5P` | 堡丽卷帘 | BTHP25TEQ | 04D | action, opener | — |
| `2C5Q` | 堡丽卷帘（高扭矩版） | BTHP35EQ | 04D | action, opener | — |
| `2C5R` | 堡丽开窗器 | BWP56TS | 02C | action, opener | — |
| `2C7V` | 西蒙二位智能开关 | 70E839 | 005 | switch1, switch2 | BackLightMode |
| `2C85` | 西蒙二位智能调光开关 | 70E849 | 044 | switch1, switch2 | BackLightMode, LedPosition1, LedPosition2 |
| `2C86` | 西蒙地暖温控器 | 70E7025 | 06A | switch, temperature | BackLightLevel, LowTemperatureProtect, SceneMode, ValveState, faultDetection |
| `2CDL` | ACEMATIC新风模块 | SH100311KI | 030 | fan, switch | — |
| `2CDN` | ACEMATIC调光灯 | SH1220101KI | 01B | brightness, switch | — |
| `2CJR` | 杜亚智能窗帘 | DH8 | 01C | mode, opener | commonFaultDetection |
| `2CK0` | 叶绿体单火二路墙壁开关 | SWL-XA02-ZB | 005 | switch1, switch2 | — |
| `2CMK` | 艾多智能窗帘电机 | AIDUO-82TN | 01C | mode, opener | Curtainjz, Curtainzfz |
| `2CP3` | 小智智能锁K8 | K8 | 04B | alarm, battery | event, lastActionTime, lockState |
| `2CPV` | 法洁奥电动牙刷 Marble-01 | Marble-01 | 073 | mode, status | NA, NA1, NA2, NA3, NA4, NA5, NA6 |
| `2CPZ` | 超静音开合帘电机尊享版 | BCHP960TER-1.2/14 | 01C | action, opener | faultDetection |
| `2CQ0` | 标准开合帘电机时尚版 | BCHP190ER-45/20 | 01C | action, opener | faultDetection |
| `2CQ8` | 吸顶式温湿度传感器 | BL5008R | 04E | humidity, temperature | humidityReportSetting, tempReportSetting |
| `2CQG` | 吸顶式红外人体移动传感器 | BL5007R | 03E | status, switch | — |
| `2CQH` | 吸顶式毫米波人体存在传感器 | BL5006R | 03E | status, switch | — |
| `2CQV` | 卡赫智能净水器1000G | WPC160RO-H | 02D | status, switch | contWater, faultDetection, filterElement1, filterElement2, filterElement3, inputTds, outputTds, water |
| `2CTW` | 三思智能厨卫灯 | C22PL-T12-12W-W | 01B | brightness, switch | — |
| `2CUQ` | 麦乐克无线烟感传感器 | MIR-SM100 | 039 | alarm, battery | commonFaultDetection, temperAlarm |
| `2CV3` | 四键场景面板时尚版 | BL8025R | 064 | switch1, switch2 | backlightMode |
| `2CV5` | 六键场景面板时尚版 | BL8026R | 064 | switch1, switch2 | backlightMode |
| `2CV7` | 四键场景面板尊享版 | BL8028R | 064 | switch1, switch2 | backlightMode |
| `2CV9` | 六键场景面板尊享版 | BL8029R | 064 | switch1, switch2 | backlightMode |
| `2CVB` | 八键场景面板尊享版 | BL8010H | 064 | switch1, switch2 | backlightMode |
| `2CVH` | 双键智能开关面板时尚版 | BL8032R | 064 | switch1, switch2 | — |
| `2CVS` | 凯胜头部按摩器 | H2 | 000 | switch, temperature | Airpressure, Comfortmode, Currentbattery, DIYmode, Music, Profitablemodel, Vitalitymode, remainingtime, shock, sleepmode |
| `2CVT` | 领普窗帘电机 | C1 | 01C | action, opener | calibration, reverse |
| `2CY1` | 达伦自然光台灯T3 | DL-31W | 046 | brightness, switch | WIFIledSwitch, classroom |
| `2CY2` | 达伦自然光台灯T3X | DL-33W | 046 | brightness, switch | WIFIledSwitch, classroom |
| `2CYS` | 朗思智能锁 | M1 | 04B | alarm, battery | event, faultCode, lockMode, lockState |
| `2D7A` | 博孚WiFi智能窗帘 | bofu-wifi-01 | 01C | action, opener | — |
| `2D82` | 卡赫智能净水器800G | WPC120RO-H | 02D | status, switch | contWater, faultDetection, filterElement1, filterElement2, filterElement3, inputTds, outputTds, purifyWater |
| `2DAC` | RGBW灯带调光驱动器 | BL2217 | 01B | colour, switch | — |
| `2DB8` | 双键86底盒开关模块 | BL8002R | 064 | switch1, switch2 | — |
| `2DC9` | HEIMAN智能人体移动传感器 | HS1MS-BH | 03E | battery, status | motionDetected, temperAlarm |
| `2DCB` | HEIMAN智能声光报警器 | HS2WD-BH | 040 | battery, switch | alamTime |
| `2DDT` | 李文智能锁 LW-701 | LW-701 | 04B | alarm, battery | event, lastActionTime, lockState |
| `2DEK` | 皇泰肩带按摩仪 | HT-8801 | 0CA | mode, switch | countdown, direction, heat, leftTime, speed |
| `2DEN` | 李文智能锁 LW-703 | LW-703 | 04B | alarm, battery | event, lastActionTime, lockState |
| `2DES` | 9W单色温射灯调光驱动器 | BL2002R | 01B | brightness, switch | faultDetection |
| `2DF2` | BOBOT博宝特洗地机 | DEEP833-H | 069 | battery, status | cleanWater, sewage, workTime |
| `2DF5` | 艾诗摩尔儿童全自动口腔清洁器 | AS-TB08 | 073 | battery, status | morning, night, sterilize, toothbrush |
| `2DFV` | 无线地面清洗机 | EL186 | 069 | battery, status | water, workTime |
| `2DG7` | SMOOKY筋膜枪 | R6 | 0C5 | mode, switch | Battery, RPM, countdown, swtich |
| `2DGG` | 达伦护眼台灯T2 | DL-27WS | 046 | brightness, switch | WIFIledSwitch, classroom |
| `2DGK` | 推窗机 | BWP56TSR | 02C | action, opener | faultDetection |
| `2DMA` | 一路智能开关 | JM-6011 | 005 | switch, switch1 | backlight |
| `2DNR` | 酷轻松颈部固定器 | PMA-L30 | 0D0 | switch, temperature | heat, timerlabel, workstatue |
| `2DNS` | 酷轻松石墨烯热敷眼罩 | K-YZ-B2V2 | 0D0 | switch, temperature | heat, timerlabel, workstatue |
| `2DO9` | 酷轻松石墨烯发热真丝眼罩 | PMA-P30 | 0D0 | switch, temperature | heat, timerlabel, workstatue |
| `2DOB` | 酷轻松石墨烯发热真丝肩颈宝 | PMA-T10 | 0D0 | switch, temperature | countdown, setGear, setTimer, workStatus |
| `2DOC` | 酷轻松石墨烯发热真丝颈带 | PMA-C10 | 0D0 | switch, temperature | countdown, setGear, setTimer, workStatus |
| `2DPA` | 酷轻松石墨烯发热休闲马甲 | K-MJ-B2V4 | 0D0 | switch, temperature | heat, timerlabel, workstatue |
| `2DQU` | 仁豪家居智能枕 | RH-Z01 | 054 | battery, status | RealtimeHR, RealtimeRR, led, power |
| `2DRM` | 计客智能四子棋 | JKSZQ001 | 000 | battery, switch | game, intro |
| `2DSB` | 拉孚一路智能开关 | HL101R | 005 | switch, switch1 | — |
| `2DV0` | 双键智能开关面板尊享版 | BL8372R | 064 | switch1, switch2 | — |
| `2DVN` | 小益智能门锁 | E208 | 04B | alarm, battery | event, faultCode, lockState, setVolume |
| `2E0P` | 攀高智能腰腹部按摩仪 | PG-2645L | 0CA | battery, switch | HEAT, MODE, State, Time, gear |
| `2E3G` | 捷昌智能卷帘 | JCD25STEW05 | 04D | action, opener | — |
| `2E3I` | 爱特嘉3L智能速热饮水机 | AH-019 | 06F | status, temperature | currentOutlet, faultDetection, outlet, waterMode |
| `2E4F` | 飞乐思智能暖宫带 | HL-NGD | 0CA | switch, temperature | Fault, MODE, TEMP, TIME |
| `2E4R` | 多功能按摩椅 | JR-M9 | 05F | mode, switch | Heating, Intensity, Pressurepattern, Strength, UpDown, Zero, foot, massageDuration, remainingTime, speed |
| `2EJY` | 艾优儿童电动牙刷 | A7-H | 073 | battery, mode | BrushingRecord, Brushingmode, custom |
| `2EMN` | 多功能按摩椅 | JR-R5 | 05F | mode, switch | Heating, Intensity, Pressurepattern, Strength, UpDown, Zero, foot, massageDuration, remainingTime, speed |
| `2EOI` | 律动机 | D1019 | 0C8 | mode, switch | Bluetoothstatus, Gear, Music, Musicswitch, RecommendedGameplay, Rhythmtime, Timeremaining, Voiceswitch, Volumecontrol, quantityheat, timecontrl |
| `2EWQ` | MINE 灵动日光镜 | MINE P2 | 000 | brightness, colour | ElectricQuantity, WorkStatus, autoInduction, breath, gradualChange, model, on |
| `2EXA` | MINI关节按摩仪 | QL/HGJ-A1 | 0CA | mode, switch | ElectricQuantity, WorkCountdown, WorkStatus, gear, hot, stop, vibrate |
| `2EYM` | 酷轻松多功能羽绒毯 | K-FRT-B2V1 | 0D0 | switch, temperature | heat, timerlabel, workstatue |
| `2F0K` | ERNTE智能料理盒 | EFC-2001-OGH | 026 | action, status | CurrentTemp, commonMode1, leftTime, preTimeStart, presetSwitch, settemp, workTime |
| `2F2I` | 拜尔智能电动牙刷 | i3plus | 073 | battery, mode | F001, F002, brushingHistory, filterElement, setWorkTime, spraySwitch |
| `2F5F` | 四键场景面板尊享版 | BL8035RC2 | 075 | switch1, switch2 | backlightMode |
| `2F5G` | 四键场景面板时尚版 | BL8051RP4 | 075 | switch1, switch2 | backlightMode |
| `2F85` | 耶鲁智能门锁YMK819 | YMK819 | 04B | alarm, battery | keyList, lockMode, lockState, openEvent, remoteInfo, tempPasswd, userlist |
| `2F87` | 耶鲁智能门锁YMK919 | YMK919 | 04B | alarm, battery | keyList, lockMode, lockState, openEvent, remoteInfo, tempPasswd, userlist |
| `2F8B` | 绿田路飞L2智能充气泵 | LUFFY-L2 | 179 | mode, status | XSZY, connectionStatus, currentAirPressure, faultDetection |
| `2FBR` | 茶吧机 | WL-T98H | 1A0 | childLockSwitch, status | Heatingswitch, Insulationswitch, KettleTemp, Waterintakeswitch, Waterintaketime, faultDetection, soakingtime, thermoregulation |
| `2FEG` | 无线智能洗地吸尘器 | S26 | 19F | battery, status | AutoDuration, AutoTimes, BootTimes, CharginTime, CycleCount, DischargeTime, Function, MainMotor, RollBrush, StandDuration, StandardTimes, StrongDuration, StrongTimes, WaterPump, cleanwaterboxstate, commonFaultDetection, selfclean, sewageboxstate |
| `2FG9` | 万家乐油烟机W8 | CXW-320-W8 | 021 | lightSwitch, switch | AntiBackflow, Cruise, CustomMode, DelayedShutdown, PourOil, Runtime, SmokeLinkState, Ventilate, Working, cleanOnOff, gear |
| `2FHB` | 领普单键墙壁开关 | Q3S-HW-W1 | 005 | brightness, switch | — |
| `2FJX` | 海曼(HEIMAN)智能空气质量检测仪(二氧化碳) | WS3AQ-H | 006 | alarm, battery | CO2Threshold, Metu, SilenceTime, co2, faultDetection, humAlarm, humidityRH, humidityThreshold, tempAlarm, tempUnit, temperatureC, temperatureThreshold |
| `2FM4` | 智能家居驱蚊器 | QWQ22XFJ-01 | 0B0 | brightness, mode | connectstate, otaupgrade, remainliquid, remaintime, reset, timeoff |
| `2FQZ` | MSN智能微电波美眼仪 | WHE2 | 0EA | battery, status | AvailableTime, BatteryLevel, GearAdjustment, Reconnect, TotalTime, TotalTimes, Vibrate, WorkingHours, gear |
| `2G35` | 光谱嫩肤仪 | SKB-1918 | 0EA | status, switch | battery2, lowbattery, state, workMode |
| `2G3K` | 奥普浴霸QDP2826BHW-Pro | QDP2826BHW-Pro | 035 | lightSwitch, switch | NightLight, drySwitch, leftTime, standbySwitch, ventilateSwitch, warmWindGear, windSwitch |
| `2G56` | 杜亚智能卷帘 | DH10 | 04D | action, opener | rotation |
| `2G8J` | 熊二智能洗地机 | X1pro | 19F | battery, status | cleanwaterboxstate, commonFaultDetection, commonFilterElement1, commonMode1, commonMode2, sewageboxstate, workTime |
| `2G9V` | 耶鲁智能门锁YMK829 | YMK829 | 04B | alarm, battery | keyList, lockMode, lockState, openEvent, remoteInfo, tempPasswd, userlist |
| `2G9W` | 耶鲁智能门锁YMK929 | YMK929 | 04B | alarm, battery | keyList, lockMode, lockState, openEvent, remoteInfo, tempPasswd, userlist |
| `2GCF` | VHV驱蚊香薰落地灯 | H1 | 10F | status, switch | errorCode, gas, laser, level, light, list, mosquito, timerOperate, touchLight, wifiLight |
| `2GD7` | 凯迪仕智能锁HK700-F | HK700-F | 04B | alarm, battery | alarmstatus, keyArray, lastActionTime, lockMode, lockState, morefunction, openEvent, publicKey, remoteCode, remoteInfo, remoteResult, userlist |
| `2GE8` | 烟雾传感器 | MIR-SM200 | 039 | alarm, battery | commonFaultDetection, silencer, smokeSensor |
| `2GEB` | 燃气传感器 | JT-GA100-ZB | 03A | alarm, gasSensor | commonFaultDetection, selfCheck, silencer |
| `2GKL` | MSN智能射频美眼仪 | WHE6 | 0EA | battery, status | AvailableTime, BatteryLevel, Reconnect, TotalTime, TotalTimes, Vibrate, WorkingHours, gear |
| `2GS8` | 华为智选 宝贝第一智能儿童安全座椅 智初 | R155D | 0DF | alarm, battery | ISOFIXAlarmSwitch, babyInStatus, beltSwitch, currentTemperature, fanMode, fanSwitch, fixedTemperature, fixedTemperatureWind, powerSupply |
| `2GVP` | 转换器(狄耐克智能插座) | SH-WDB-SKT501 | 01D | childLockSwitch, switch | — |
| `2GX0` | 乐歌电动升降桌ET114 | ET114F-N | 164 | action, childLockSwitch | commonFaultDetection, ctrlhight, day, heightfour, heightone, heightthree, heighttwo, line, month, reporthight |
| `2GXO` | AI生态枕 | 3123000280 | 054 | battery, status | HR, led, power, realtimeRR |
| `2GYR` | Poputar 智能吉他 | Poputar T2 | 159 | mode, status | chord, interactive, learning, practice, tuning |
| `2GYT` | 皓刻电动牙刷 | H9 | 073 | battery, mode | BatteryLevel, DeviceStatus, Reconnect, RemainingDaysOfBrushHead, WorkTimSetting, brushingHistory |
| `2H4Y` | 香百年畅享智能香薰机 | XH-006 | 0DE | mode, switch | autoStart, cycles, density, electricity, fragSetting1, fragSetting2, fragrance, margin1, margin2, near, timing |
| `2H68` | 格林盈璐暖风机GL002 | GL002 | 06A | mode, switch | Remaining, countdown, shake |
| `2H6O` | KEKEN智能锁 P20 | P20 | 04B | alarm, battery | KeyData, KeyManagement, UidKidTable, User, UserManagement, commonMode2, lockMode, lockState, lockStatus, openEvent, tempPasswd |
| `2H8W` | 音乐炫彩氛围灯 | FW-Y01 | 189 | brightness, mode | OnoffLine, SUDU, definecolour, explore, powerswitch, savemode, statemode |
| `2H9E` | 金莱特便携干衣胶囊 | KN-6332 | 1B5 | mode, switch | — |
| `2HAG` | 康佳按摩椅KZ-RH8900 | KZ-RH8900 | 05F | status, switch | AirbagAuto, Hot, Leg, RiseDrop, Roll, TimeSurplus, Timer, Zero, autoMode, heacushion, shoulderarms |
| `2HAK` | 希箭H1 HC半自动WiFi智能锁 | HK-H1 | 04B | alarm, battery | Volume, keyList, lockMode, lockState, openEvent, publicKey, remoteCode, remoteInfo, remoteResult, userlist |
| `2HBZ` | 酷轻松石墨烯热敷颈托 | AG10-02 | 0D0 | mode, temperature | gear, remainder, timing, workstatus |
| `2HC2` | 得力智能闹钟 | NS885 | 197 | humidity, temperature | Alarmsetting, Alarmswitch, Backlightbrightness, Ringtonevolume, Snoozetimes, Timeformat, devicestatus |
| `2HDF` | 绿克手持吸拖一体机HW1 | YM-HW1-W01 | 19F | battery, status | RollerBrushAirDrying, Suction, VolumeAdjusting, WaterSprayVolume, WorkingMode, fault, selfclean |
| `2HGE` | 仁豪家居智能按摩椅 | ZF-9201-D | 05F | action, switch | autoMode, backAction, devStatus, heatMode, intenGear, lbpMode, manuMode, massGear, ppmMode, soleSwitch |
| `2HOB` | 酷轻松石墨烯智能睡袋 | K-SD-B1V1 | 0D0 | mode, temperature | gear, remainder, workstatus |
| `2HOH` | 酷轻松石墨烯智能按摩靠枕 | AH20-01 | 186 | mode, temperature | gear, message, remainder, timing, workstatus |
| `2HOI` | 酷轻松石墨烯智能按摩腰靠 | AI10-01 | 186 | mode, temperature | gear, message, remainder, timing, workstatus |
| `2HOK` | 酷轻松石墨烯热敷按摩颈枕 | AG40-01 | 186 | mode, temperature | HotReminder, LowPower, Switch, currentbattery, heating, remainder, workstatus |
| `2HOL` | 酷轻松石墨烯智能发热坐垫 | MD10-01 | 186 | mode, temperature | gear, remainder, timing, workstatus |
| `2HPC` | iSuke智能枕 | CC07-A | 054 | battery, status | HR, led, power, realtimeRR |
| `2HQ6` | 城市轻骑智能闪盔 | SH50 | 134 | brightness, switch | Autooff, LED, Light, autoon, bat |
| `2HRE` | 西蒙16A三孔智能插座 | 58E8212 | 01D | childLockSwitch, switch | IndicatorMode, electric, faultDetection, power |
| `2HRF` | 西蒙10A五孔智能插座 | 58E8211 | 01D | childLockSwitch, switch | IndicatorMode, electric, faultDetection, power |
| `2HTH` | 启源智能调光 | QY-RS/HMS20-1 | 11A | status, switch | Brigness, LampB, LightName, LightStatu, Name, OpenOClose |
| `2HUA` | 德施曼智能门锁R7H | R7H | 04B | alarm, battery | Hijacking, enableState, errorCode, keyArray, lastActionTime, lockMode, lockState, lockdefense, openEvent, publicKey, remoteCode, remoteInfo, remoteResult, upgradeMode, userlist |
| `2HVI` | 九联智能门锁 | T5L00BCH | 04B | alarm, battery | errorCode, keyList, lockMode, lockState, openEvent, publicKey, remoteCode, remoteInfo, remoteResult, upgradeMode, userlist |
| `2HY5` | 因硕智能锁F1 | F1 | 04B | alarm, battery | erroralarm, keyList, lockState, openEvent, prvdooralarm, publicKey, remoteCode, remoteInfo, remoteResult, userlist |
| `2HY6` | 因硕智能锁T07 | T07 | 04B | alarm, battery | erroralarm, keyList, lockState, openEvent, prvdooralarm, publicKey, remoteCode, remoteInfo, remoteResult, userlist |
| `2HYW` | 时生便携式电源 | Y3000 | 138 | battery, switch | PVPower, RestTime, ShutdownRestTime, commonFaultDetection, inputpower, outputpower, powerswitch, timingshutdown |
| `2HZE` | 海曼(HEIMAN)智能烟雾报警器 | HS2SA | 039 | alarm, battery | alarmtype, selfCheck, silencer, temperAlarm |
| `2I17` | 莱轻松智能护膝按摩器 | QG04 | 0CA | status, switch | batteryView, commonFaultDetection, fomentTemperature, massageStall, timedFuntion |
| `2I22` | 南威G款锂电角磨机 | NW-ZH9100 | 204 | battery, mode | lock, speed, switchR, upkeep, workTimer |
| `2I49` | 蒸汽清洁机 | EL78 | 0E1 | status, switch | faultDetection, steamswitch |
| `2I5C` | MSN智能电吹风 | WHHD1 | 0E4 | mode, status | Anion, Gear, Upgrade, Volume, Warning, speeds, windSpeed |
| `2IFB` | 艾主人智能洗地机 | YLF6327D-B | 19F | battery, status | FirmwareUpgrade, Reconnect, VoiceSwitch, commonFaultDetection, commonFilterElement1, commonFilterElement2, model, selfclean |
| `2IFL` | 正牛智能电吹风 | H5 | 0E4 | mode, status | ConnectStatus, Modelshow, Testsareshown, minute, second |
| `2IHJ` | SmartCurtain | LS82 | 01C | action, opener | stroke |
| `2IK5` | 企一照明可调角阅读灯 | QYHW227N | 113 | brightness, switch | commonFaultDetection, relBrightness, toggleSwitch |
| `2IRF` | 米多全能水洗机A8 Pro | VC-W08B | 19F | battery, status | cleantime, erro, seclean, totalTime, workTime |
| `2ISC` | 奥普浴霸QDP2826BHW | QDP2826B-HW | 035 | lightSwitch, switch | NightLight, drySwitch, leftTime, standbySwitch, ventilateSwitch, warmWindGear, windSwitch |
| `2IU9` | 西蒙二位智能场景开关 | 58E8206 | 005 | switch1, switch2 | commonFaultDetection, deviceStatus, indicator, mode1, mode2, sceneButton1, sceneButton2 |
| `2IUA` | 超人智能门锁Q5-RM | Q5-RM | 04B | alarm, battery | keyArray, lockState, openEvent, publicKey, remoteCode, remoteInfo, remoteResult, userlist |
| `2IVC` | 贝昂智能取暖器H3 | HDN2-H3 | 06A | childLockSwitch, switch | Shake, TimingOff, faultDetection, gear |
| `2IVI` | 贝昂智能取暖器H5 | HDN2-H5 | 06A | childLockSwitch, switch | Screen, Shake, TimingOff, faultDetection, gear |
| `2IVP` | 佳普乐G5-300N智能马桶 | G5-300N | 066 | mode, status | ECO, dryGear, drySwitch, flush, hPosition, heatGear, hintenty, nightled, sitdown, smart, wPosition, waterTemp, wintenty |
| `2IVQ` | 佳普乐G5-400N智能马桶 | G5-400N | 066 | mode, status | ECO, dryGear, drySwitch, flush, hPosition, heatGear, hintenty, nightled, sitdown, smart, wPosition, waterTemp, wintenty |
| `2IVU` | 佳普乐G6-300N智能马桶 | G6-300N | 066 | mode, status | ECO, dryGear, drySwitch, flush, hPosition, heatGear, hintenty, nightled, sitdown, smart, wPosition, waterTemp, wintenty |
| `2IVV` | 佳普乐G6-400N智能马桶 | G6-400N | 066 | mode, status | ECO, dryGear, drySwitch, flush, hPosition, heatGear, hintenty, nightled, sitdown, smart, wPosition, waterTemp, wintenty |
| `2IX9` | 科技暖腰带 | WZT5V101 | 17D | alarm, switch | BLEstatus, CurrentTemperature, HotCompress, TemperatureGears, VibrateMode, baterry, countdown, frenquency, shutdown |
| `2IXD` | 舒适暖腰带 | WZC3V301 | 17D | alarm, switch | BLEstatus, CurrentTemperature, HotCompress, Vibratemode, baterry, countdown, shutdown |
| `2IY0` | 奥特威智能窗帘 | AT5810 | 01C | action, opener | stroke |
| `2J05` | 锐亿电动牙刷 | RT895 | 073 | battery, mode | Record, gear, initPosition, more, remaining, state, workGuidance |
| `2J1Y` | 檬丝眼部按摩仪 | MS-6 | 0CA | mode, switch | BGM, Status, heatSwitch, timeSet |
| `2J2C` | 无尽之窗窗帘机 | MAGE10B | 01C | action, opener | — |
| `2J33` | 火火兔智能早教故事机 H1S | H1-001 | 08D | action, switch | Music, batteryStatus, childLock, custom, earLight, timedTask |
| `2J3X` | A.O.史密斯净热一体机 | DR2000HF2 | 02D | status, temperature | addWaterMode, faultDetection1, filterElement1, filterElement2, heatingSwitch, inputTds, keepWarmMode, outputTds, totalPurifyWater, water, waterLevelStatus |
| `2J46` | 水享智能阀CZC20 | CZC20 | 209 | status, switch | netLight, protection, reEnergizingState, record, valveLight |
| `2J7L` | 水享手动辅助智能阀CZC20S | CZC20S | 20A | status, switch | netLight, reEnergizingState, record, valveLight |
| `2J7P` | 杜亚智能百叶 | DH12 | 2BB | action, opener | changeDirection, rotationAction |
| `2J8E` | Meli1折叠锂电车 | TDW48Z | 296 | mode, switch | Consumption, autosleep, distance, forbidden, level, odometer, safetylock, selfinspection, state, warningmessage |
| `2J8I` | 智能窗 JinLY | SC-88 | 02C | action, opener | devicestatue |
| `2JAR` | 欧普蓝牙Mesh单色温灯带驱动 | OP-DY220/20-24CV/2-WB | 226 | brightness, switch | commonFaultDetection, toggleSwitch |
| `2JBN` | 健诺德腰腹按摩器 | XD-CX-T19 | 0CA | mode, switch | RemainingTime, connect, countdown, electricity, hot, strength, voice |
| `2JFY` | AM35智能百叶帘 | AM35-6/18-MEL-PW-VB | 2BB | action, opener | JointLevel, Limit, SBZT, changeDirection, commonMode1, directionalmode, rotationAction |
| `2JFZ` | AM35智能卷帘 | AM35-6/18-MEL-PW-RB | 04D | action, opener | JointLevel, Limit, SBZT, changeDirection, commonMode1, directionalmode |
| `2JJ9` | 智能梦幻帘 | Q1 | 2BE | action, opener | changeDirection, rotationAction, rotationAngle |
| `2JK2` | 杜亚智能卷帘 | DH20 | 04D | action, opener | changeDirection |
| `2JLE` | gb SMART便携制冷包 | ZLB300 | 2B0 | status, temperature | cool, equipmentStatus, instructions, knowledge, temperatureRecord, workStatus |
| `2JN0` | 三合一拖地机 | FORCE.S1 | 19F | battery, status | DevMode, HandheldNormalSet, WorkPm, aspirationNormalSet, aspirationStrongSet, cleanNormalSet, cleanStrongSet, cleanselfNormalSet, cleanselfStrongSet, commonFaultDetection, consumables, control, handheldStrongSet |
| `2JO1` | 电小酷智能转换插座 | CP1-HW | 01D | childLockSwitch, switch | ChargingProtection, ProtectionSwitch, commonFaultDetection, electric, indicator, memorySwitch, power |
| `2JOZ` | 柏曼智能双色灯 | E0677 | 112 | brightness, switch | colorTem, countdown, nodeInfo, profile, rhythm, timing |
| `2JPT` | 美森智能电动修足器 | WHB1 | 2A6 | battery, status | gear, useTime, workStatus, workingMode, workingTimes |
| `2JXK` | 贝克巴斯垃圾处理器E60PRO | ELEMENT-60 PRO | 0B6 | mode, status | faultDetection, gear, reverse, start |
| `2JXZ` | 飞利浦按摩披肩PPM3212N | PPM3212N | 0CA | mode, switch | CountdownOff, Instructions, Intensity, OTAUpgrade, Remaining, Warning, batteryLevel, deviceSatus, heating |
| `2JZ4` | VOC大屏猫眼人脸锁 | T10Plus | 04B | alarm, battery | errorCode, keyArray, lockMode, lockState, openEvent, publicKey, remoteCode, remoteInfo, remoteResult, upgradeMode, userlist |
| `2K0I` | 卡儿酷户外电源 | S1500Plus | 138 | battery, temperature | ACinput, ACoutput, ACswitch, DC1output, DC2output, DCinput, DCswitch, USB1output, USB2output, USBswitch, battery2, chargingtime, endurance, inputpower, lightmode, outputpower, solarinput, state |
| `2K0T` | 德施曼智能门锁Q30 | Q30 | 04B | alarm, battery | Hijacking, enableState, errorCode, keyArray, lastActionTime, lockMode, lockState, lockdefense, openEvent, publicKey, remoteCode, remoteInfo, remoteResult, upgradeMode, userlist |
| `2K1E` | 科爱元素小面包砭石按摩器智能版 | CI165A | 0D0 | battery, mode | Report, Service, Switchoff, btstatus, compress, exposure, learningchoice, learningvideo, lefttime, pressure, suck, timedown |
| `2K36` | 青越千分比深度调光线性灯 | HC-DDD-001 | 118 | brightness, switch | Ontime, countdown, memoryswitch, offtime, tempvalue |
| `2K72` | VOC大屏猫眼人脸锁K9Plus | K9Plus | 04B | alarm, battery | errorCode, keyArray, lockMode, lockState, openEvent, publicKey, remoteCode, remoteInfo, remoteResult, subBattery, upgradeMode, userlist |
| `2K73` | VOC猫眼智能门锁X11i | X11i | 04B | alarm, battery | errorCode, keyArray, lockMode, lockState, openEvent, publicKey, remoteCode, remoteInfo, remoteResult, upgradeMode, userlist |
| `2KCQ` | 空间卫士健康空气智慧管家01 | KJWS-01 | 030 | pm25, switch | FragranceTime, anion, density, filterElement01, filterElement02, filterElement03, filterElement04, filterElement05, filterElement06, hotline, intelligent, lamp, model, timing, ventilation |
| `2KD9` | 正泰五孔智能插座 | NEW3-W53100D | 1FC | childLockSwitch, switch | electric, faultDetection, indicator, memorySwitch, power |
| `2KE3` | 九联全自动智能门锁 | T5L10BCH | 04B | alarm, battery | errorCode, keyArray, lockMode, lockState, openEvent, publicKey, remoteCode, remoteInfo, remoteResult, upgradeMode, userlist |
| `2KE4` | 九联3D人脸识别智能门锁 | T5L20BCH | 04B | alarm, battery | errorCode, keyArray, lockMode, lockState, openEvent, publicKey, remoteCode, remoteInfo, remoteResult, upgradeMode, userlist |
| `2KF0` | 奥克斯智能门锁HM-620 | HM-620 | 04B | alarm, battery | Volume, keyList, lockMode, lockState, openEvent, publicKey, remoteCode, remoteInfo, remoteResult, userlist |
| `2KGW` | 班弗智能锁7000A | 7000A | 04B | alarm, battery | keyArray, lockState, openEvent, publicKey, remoteCode, remoteInfo, remoteResult, userlist |
| `2KH3` | 班弗智能锁8000A | 8000A | 04B | alarm, battery | keyArray, lockState, openEvent, publicKey, remoteCode, remoteInfo, remoteResult, userlist |
| `2KH4` | 班弗智能锁9000A | 9000A | 04B | alarm, battery | keyArray, lockState, openEvent, publicKey, remoteCode, remoteInfo, remoteResult, userlist |
| `2KKW` | 嘿码智能剃须刀 | BC5000 | 170 | alarm, status | cleanTime, cutterTime, power, version, workMode, workStatus, worktime |
| `2KOY` | 梦幻极光 | WSCMXH-1.2/9 | 2BE | action, opener | directionalmode, rotationAction, rotationAngle, switchSpeed |
| `2KPG` | 天智星 | WSCMQ-A-1.2/9 | 01C | action, opener | directionalmode, switchSpeed |
| `2KVN` | 香百年畅享智能香薰机Pro | XH-008 | 0DE | mode, switch | FirmwareUpdate, Report, autoStart, cycles, density, electricity, fragSetting1, fragSetting2, fragrance, hotline, instruction, margin1, margin2, near, timing |
| `2KXU` | 霍尼韦尔门窗传感器 | HZBS-H-DW | 018 | battery, luminance | alarmSwitch, commonFaultDetection, doorContact, reminder, temperAlarm |
| `2KY3` | 霍尼韦尔独立式感烟火灾探测报警器 | JTYJ-GD-HW01 | 039 | alarm, battery | commonFaultDetection, silencer, smokeSensor |
| `2KY4` | 霍尼韦尔家用可燃气体探测器 | JT-BF-HW01 | 03A | alarm, gasSensor | commonFaultDetection, preheat, selfCheck, silencer |
| `2KZR` | 杜亚智能升降器 DH13 | DM45E-50/12 | 33F | action, opener | — |
| `2L0A` | 荣康摩杰座按摩椅RK2001S | RK2001S | 05F | action, switch | afterSales, autoAdjustment, autoMode, equipmentStatus, manualAdjustment, postureAlignment, shoulDertest, videoDisplay, workingHours |
| `2L0L` | 携住温控 | xiezhu_001 | 10D | mode, temperature | airKey |
| `2L4T` | 创明智能卷帘 | TP35-5/26EHU | 04D | action, opener | directionalmode, rotation |
| `2L52` | 携住取电 | xiezhu_002 | 200 | status, switch | doorContact |
| `2L8V` | 立达信米来单头吊灯 | PLBP-ML01-PR-HM | 21E | brightness, switch | — |
| `2LBT` | 心智悦环境控制器K1 | MJTC-K1 | 10D | humidity, temperature | CO2, HCHO, PM25, airKey, airswitch, fan1, faultDetection, filterElement, freshairswitch, heatingswitch, memorySwitch, mode1 |
| `2LIW` | 贝克巴斯智能水龙头 | F05PRO | 209 | status, switch | clear, downDistance, effluent, leftDistance, leftFunc, onOff, pairingStatus, pullStatus, reconfigure, rightDistance, velocity, waterTemperature, waterUseData |
| `2LJO` | Mate 60系列环闪保护壳 | Be | 228 | brightness, switch | colorTemperature, control, firmwareUpgrade, sceneLightEffect, specialSet, workStatus |
| `2LJP` | Mate 60系列环闪保护壳 | Qa | 228 | brightness, switch | colorTemperature, control, firmwareUpgrade, sceneLightEffect, specialSet, workStatus |
| `2LK5` | 摩申高速吹风机MH08 | MH08 | 0E4 | mode, status | allstatus, fault, rspeed, speed, worktime |
| `2LQA` | 友通多功能空气检测仪 | YT6964 | 1F2 | hcho, pm25 | alarmSwitch, brightness01, clock, co2, commonFaultDetection, humi, pm10, report, temp, tvoc, ytFault |
| `2LX0` | 礼意久久舒适暖腰带双面款 | WZC5V201 | 17D | alarm, switch | BLEstatus, CurrentTemperature, HotCompress, Vibratemode, baterry, countdown, shutdown |
| `2LX8` | 良品主义智能电动剃须刀 | SC026 | 170 | alarm, status | cutterTime, instruction, lock, power, workMode, workStatus, worktime |
| `2M6W` | 创明智能卷帘 | TQA25-1.1/31E | 04D | action, opener | changeDirection, switchSpeed |
| `2M78` | 欧瑞氏2000W暖风机 | DH-QN19A | 06A | switch, temperature | commonFaultDetection, gear, swing, timers, workingStatus |
| `2M8M` | 哈尔斯智能泡茶杯 | HBM-500-001/HGM-450-002 | 06B | battery, status | checkedTea, clock, currentTemperature, customTeaList, drinkRemind |
| `2MAS` | 锐亿剃须刀RS166 | RS166 | 170 | alarm, status | Records, cleanTime, cutterTime, lock, power, remainNumber, remainTime, version, workStatus |
| `2MDA` | BYXAS智能按摩暖腰带 | SMWB-50 | 17D | alarm, switch | BAT, BLEstatus, countdown, hot, shake, shutdown |
| `2ME0` | 奥科PLC版开合帘电机时尚款 | AM130-1.2/100-EM-P | 01C | action, opener | changeDirection, commonFaultDetection, placeMemory, switchSpeed |
| `2MEH` | 施柏阁开合帘电机SMC800H | SMC800H | 01C | action, opener | Motordirection, PasswordSetting, RestoreFactory, commonFaultDetection |
| `2MEJ` | 施柏阁管状电机SMR602H | SMR602H  | 04D | action, opener | JogButton, Motordirection, PasswordSetting, RestoreFactory, Travelsettings, commonFaultDetection |
| `2MEK` | WYC智能暖腰带 | WYC003 | 17D | alarm, switch | BLEstatus, CurrentTemperature, baterry, countdown, hot, shake, shutdown |
| `2MEN` | 力博得智能牙刷3 Pocket | LBT-125002A | 073 | battery, mode | brushDay, brushHistory, deviceColor, deviceLock, hardware, setWorkTime, voiceGuidance, workGuidance |
| `2MFF` | 佛山照明智能插座 | Z1-Z3B-101/ZK | 01D | childLockSwitch, switch | electric, faultDetection, indicator, power |
| `2MFX` | 创明智能百叶帘-TP35 | TP35-5/26EHU | 2BB | action, opener | changeDirection, rotationAction |
| `2MGK` | 杜亚智能窗帘 | H5 | 01C | action, opener | Direction, switchSpeed |
| `2MGL` | 创明智能百叶帘 | TQA25-1.1/31E | 2BB | action, opener | changeDirection, rotationAction, switchSpeed |
| `2MGM` | 易百珑四键智能开关 | EWS54-HM | 201 | switch1, switch2 | CleanPair, Pair, led, memorySwitch, mode1, mode2, sceneButton1, sceneButton2, sceneButton3, sceneButton4 |
| `2MIG` | 光照传感器 | MIR-IL100 | 049 | battery, luminance | commonFaultDetection, delayTime, switchNightLight |
| `2MKA` | 杜亚智能百叶-PLC款 | DH20 | 2BB | action, opener | changeDirection, rotationAction |
| `2MN2` | 爱莱克特高速吹风机EL280 | EL280 | 0E4 | mode, status | information |
| `2MNT` | 膳魔师智能保温杯Pro 弹盖款 | TEEA-470S | 06B | battery, status | Goal, canvasConfig, canvasData, canvasData1, canvasData2, canvasData3, canvasData4, canvasData5, currentTemperature, drinkIntake, drinkRemind, drinkTarget, myHashCode, privacySta, privacyStatus, targetTemperature, waterVolume, waterWeeksIntake |
| `2MO0` | 锐亿剃须刀RS 399B | RS 399B | 170 | alarm, status | Records, cleanTime, cutterTime, find, lock, power, remainNumber, remainTime, version, workStatus |
| `2MQ8` | 莱轻松揉腹仪 | P6 | 0CA | status, switch | batteryView, emsGear, emsMode, fomentTemperature, kneadMode, moxibustion, timedFuntion |
| `2MQB` | 摩申高速吹风机MH03 | MH03 | 0E4 | mode, status | allstatus, fault, rspeed, worktime |
| `2MU2` | 昔马智能电动剃须刀 | HM-X1 | 170 | mode, status | batteryState, shaverState, statusa |
| `2MXG` | 家用可燃气体探测器 | JT-GA01-PLC | 03A | alarm, gasSensor | commonFaultDetection, selfCheck, silencer |
| `2MXH` | 吸顶式红外人体移动光照传感器 | MIR-IR01-PLC | 049 | luminance, pir | commonFaultDetection, configureSwitch1, delayTime, luminanceReportSetting, selfCheck, switchNightLight |
| `2MXI` | 侧装红外人体移动光照传感器 | MIR-IR02-W-PLC | 049 | luminance, pir | commonFaultDetection, configureSwitch1, configureSwitch2, delayTime, lightBrightness, lightCct, nightlightSwitch1, selfCheck, sensitivity, switchNightLight, timeSync |
| `2MYX` | 西马智能马桶盖 | CBG-Q80Hm | 066 | mode, switch | cleanPosition, commonFilterElement1, dryGear, drySwitch, eco, faultDetection, hipTime, intensity, led, massage, nozzleClear, onSeat, seatTemp, sitSwitch, sitTime, sound, waterTemp, womenTime |
| `2N06` | 以内洗地机Z5Pro | INZ015 | 19F | battery, status | cleanwaterboxstate, selfclean, sewageboxstate, workTime |
| `2N09` | 米芙拉浴室取暖器加热毛巾架一体机 | BH-1701E-B | 0BA | mode, temperature | commonFaultDetection, drying, windSwitch |
| `2N28` | 智能语音哑铃 | Y1 | 0C2 | mode, status | ExerciseLog, OTA, courseDetail, devInfo, electric, fault, language, partner, userInfo, voice |
| `2N2A` | 智能俯卧撑平板撑训练器 | F1 | 0C2 | mode, status | ExerciseLog, OTA, courseDetail, devInfo, duvstatus, electric, exerciseNum, exerciseTime, partner, voice |
| `2N2B` | 智能调节哑铃 | Y4 | 0C2 | mode, status | ExerciseLog, OTA, Upgrade, courseDetail, devInfo, electric, partner, userInfo, voice |
| `2N2Q` | A.O.史密斯净热一体机 | DR2000FWi | 02D | status, temperature | addWaterMode, faultDetection, filterElement1, filterElement2, heatingSwitch, inputTds, keepWarmMode, outputTds, totalPurifyWater, water, waterLevelStatus |
| `2N52` | 侧装红外人体移动光照传感器 | MIR-IR02-B-PLC | 049 | luminance, pir | commonFaultDetection, configureSwitch1, configureSwitch2, delayTime, lightBrightness, lightCct, nightlightSwitch1, selfCheck, sensitivity, switchNightLight, timeSync |
| `2N5I` | 创明智能PLC梦幻帘 | Q10172 | 2BE | action, opener | rotationAction, rotationAngle |
| `2N5R` | 新博孚梦幻帘 | BFMH-JDHWG | 2BE | action, opener | directionalmode, rotationAction, rotationAngle |
| `2N5S` | 杜亚智能梦幻帘 | H6 | 2BE | action, opener | changeDirection, rotationAction, rotationAngle, switchSpeed |
| `2N5T` | 杜亚智能齐平卷帘 | H7 | 04D | action, opener | changeDirection, syncAction, syncOpener |
| `2N8Z` | 俏美人热敷护腰带 | QMR8026 | 17D | alarm, switch | BLEstatus, CurrentTemperature, baterry, countdown, hot, shake, shutdown |
| `2ND3` | 传感器-盛和 | MC3-CGQ3 | 1F2 | hcho, pm25 | co2, humi, pm10, temp, tvoc |
| `2NFE` | 香百年智能离子净化香氛机 | XH-009 | 0DE | mode, switch | auto, car, commonFaultDetection, concentration, connectInfo, consumable, cycle, debus, devInfo, electric, ion, lamp, volume |
| `2NGJ` | 新飞532L四门智能冰箱 | BCD-532WGQ8A-PRO | 08A | childLockSwitch, switch | faultDetection, freezeSwitch, freezer, intelligentSwitch, refrigerateSwitch, refrigerationRooClosed, refrigerator, transformingSetting |
| `2NGR` | 智能充气泵 | JC01_BT | 179 | mode, status | charge, error, light, pumpfinish, setPressure, state, syncCurrentData, unit |
| `2NI0` | 佳普乐沁源感应给皂龙头 | ST1QY-01N | 299 | switch, temperature | autoWaterSwitch, coldWaterSwitch, interval, soapTime, waterTime |
| `2NIH` | 暖心睡眠仪 | ZM001 | 08C | battery, switch2 | Devicestatus, gear2, rate, warn |
| `2NK0` | FUNSNAP CM8云台 | CM8 | 0EC | battery, status | followMode, lowbattery |
| `2NM6` | 麦瑞克MR-2365颈肩按摩器 | MR-2365 | 0CE | mode, status | HotCompress, Lefttime, Shutdown, VideoIntroduction, batteryLevel, commonFaultDetection, gear |
| `2NME` | 森森智能鱼缸 | LE-380B | 1A7 | colour, lightSwitch | changewater, commonFaultDetection, feed, filter, waterTemp |
| `2NU1` | 摩申高速吹风机MH02PRO | MH02PRO | 0E4 | mode, status | allstatus, fault, rspeed, worktime |
| `2NV3` | 森瑞智能窗帘 | T150/HW | 01C | action, opener | SBZT, changeDirection |
| `2NVF` | 森瑞智能百叶 | K200/A | 2BB | action, opener | SBZT, changeDirection, rotationAction |
| `2NVI` | 森瑞双生日夜帘 | K610/A | 04D | action, opener | SBZT, nightAction, nightOpener |
| `2NVS` | 三思智能植物生长灯R0260 | C21GL-R02-60W | 177 | brightness, switch | — |
| `2NX3` | 倍益康便携式深层肌肉按摩仪 | HQ7 | 0C5 | action, battery | btconnection, commonFaultDetection, countdown, gear, otaUpgrade, revolution, workStatus |
| `2NX4` | 倍益康超迷你肌肉按摩器 | HC1 | 0C5 | action, battery | btconnection, commonFaultDetection, countdown, gear, otaUpgrade, revolution, workStatus |
| `2NX5` | 倍益康可变振幅深层肌肉按摩仪 | H Ti Max | 0C5 | action, battery | amplitude, btconnection, commonFaultDetection, countdown, otaUpgrade, revolution, strength, workStatus |
| `2O05` | 开合帘电机 | N30136 | 01C | action, opener | changeDirection |
| `2O0E` | usmile智能电动牙刷U7 | usmile U7 | 073 | battery, mode | brushing, brushingState, expert, firmwareUpdate, life, record, resetFactory, setTime, smart, tlock, voiceSwitch, workStatus |
| `2O10` | usmile智能电动牙刷U7 Pro | usmile U7 Pro | 073 | battery, mode | archive, brushing, brushingState, expert, firmwareUpdate, life, record, resetFactory, setTime, tlock, voiceSwitch, workStatus |
| `2O2B` | 贵品开合帘GT50 | GT50 | 01C | action, opener | suitablePoint |
| `2O2C` | 贵品卷帘GJ | GM25 | 04D | action, opener | suitablePoint |
| `2O2D` | 贵品百叶GL | GV24 | 2BB | action, opener | rotationAction, suitablePoint |
| `2O30` | 威仕达卷帘WSERD30 | WSERD30-T-1.5/35 | 04D | action, opener | changeDirection |
| `2O31` | 威仕达百叶帘WSERD24 | WSERD24-DA-1.5/35 | 2BB | action, opener | changeDirection, rotationAction, switchSpeed |
| `2O34` | 威仕达百叶帘WSVM24 | WSVM24-1/35 | 2BB | action, opener | commonFaultDetection, day, limit, night, pair, rotationAction, speed |
| `2O3G` | 信社擦窗机器人 | X60Pro | 0F7 | action, status | ErrorCode, Manual, StartStop, WaterMode, WaySetting, WheelClear, clearMode |
| `2O43` | 威仕达双子星开合帘WSCMXJ | WSCMXJ-3/9 | 01C | action, opener | Motormanual, calibration, controller, left, openspeed, right, swap |
| `2O5A` | 膳魔师智能保温杯Pro 旋盖款 | TEEB-450S | 06B | battery, status | Goal, currentTemperature, myHashCode, privacySta, targetTemperature, waterDayIntake, waterVolume |
| `2O65` | 便携电动剃须刀 | DT-W300 | 170 | battery, status | batteryCycles, bladeStatus, duration, history, power, resetTime |
| `2O6F` | 柏曼智能节律灯 | PCO206212 | 112 | brightness, switch | colorTem, countdown, nodeInfo, profile, rhythm, timing |
| `2O7G` | 光照传感器 | MIR-IL100 | 343 | battery, luminance | commonFaultDetection |
| `2O9H` | eachone一起玩 智能加湿器 | HF-HM-JSQ-001 | 052 | humidity, switch | countdown, gear, lightmode, remainingtime, waterGear |
| `2ODZ` | 造化万物热敷按摩仪 | OP4/5/6 | 17D | battery, switch | countdown, temp, vibrate |
| `2OF2` | 物联网断路器AICB2C-3P | AICB2C-3PC32 | 211 | action, status | commonFaultDetection, count, ctrl, curNeutral, phaseA, phaseB, phaseC, power, proOc, proOuv, proSwitch, proTemp, temp, totalForwardEnergy |
| `2OG1` | 梵吉尼香氛机S5 | S5 | 04C | mode, switch | IntervalDuration, ResidualVolume, SprayDuration, TotalConsumption, faultDetection |
| `2OHL` | 箭牌电子安全水阀 | ALEZ02MB | 209 | battery, status | abnormalAlarm, flowVelocity, inputTds, maxFlow, proSwitch, singleWater, waterDaily, waterLeakage, waterPressure, waterTemperature, waterTime, waterUseData |
| `2OJL` | eachone一起玩 智能加湿器 | HF-HM-JSQ-002 | 052 | humidity, switch | countdown, gear, lightmode, remainingtime, waterGear |
| `2OJQ` | 电小酷智能转换插座 | CP1-HW-A | 01D | childLockSwitch, switch | ChargingProtection, ProtectionSwitch, commonFaultDetection, electric, indicator, memorySwitch, power |
| `2OOR` | 智能热敷腰带 | HY-NG2115 | 17D | alarm, battery | countDown, heat, hot, hotSwitch, massage, massageSwitch |
| `2OPH` | Novia | T600 | 297 | status, switch1 | childLock, light, massage, massageDuration, massageGear, temperature1, waterGear, waterInjectionDuration |
| `2OPI` | 提升窗HY | HC86TSY | 2BC | action, lightSwitch | childLock, light, winScreen |
| `2OQZ` | 哆啦A梦智能热敷腰带 | DL-NG1701 | 17D | alarm, battery | countDown, heat, hot, hotSwitch, massage, massageSwitch |
| `2OT7` | 艾力斯特按摩椅双芯大师M5X | M5X | 05F | status, switch | Auto, BackIntensity, Bluetooth, Health, Manual, Other, Shoulder, SitAdjustment, State, Timing, healthMode, massageGear, ppmMode, pressureSwitch, soleSwitch, voiceSwitch |
| `2OUG` | CZC25系列智能漏水保护阀 | CZC25 | 209 | status, switch | commonFaultDetection, netLight, protection, reEnergizingState, record, valveLight |
| `2OUW` | 艾有舒随身灸 |  K6 | 0C3 | battery, status | commonFaultDetection, devSwitch, windSpeed, workTime |
| `2OYN` | 承弦雨水传感器S1 | RSS1YH | 048 | battery, switch | rainFall, sensitivity |
| `2OYR` | AiRELAXS芝华仕智能床 P1 | AiR_P1 | 14A | childLockSwitch, status | awaken, headControl, legControl, modeSelect, oneKeyReset |
| `2P2M` | 智能便携富氢水杯 | WP-G22-07 | 06B | battery, status | commonFaultDetection, currentTemperature, electrolyticConcentration, hydrogenProductionSwitch, intelligentCleaning |
| `2P43` | 佳普乐宏岚智联毛巾架 | TH1HL-04W | 0BA | status, temperature | drying, dryingLeftTime, dryingTime |
| `2P44` | 佳普乐宏瑞智联毛巾架 | TH1HR-06G | 0BA | status, temperature | drying, dryingLeftTime, dryingTime |
| `2PDM` | SMUI敏升智能床 | Queen009 | 14A | childLockSwitch, status | headControl, headMassage, legControl, legMassage, massageMode, massageTimer, modeSelect, oneKeyReset, positionSelect |
| `2PDQ` | KLST克丽斯汀悬浮云端智能床 | GN-09 | 14A | childLockSwitch, status | headControl, headMassage, legControl, legMassage, massageMode, massageTimer, modeSelect, oneKeyReset, positionSelect |
| `2PDY` | BOXLAMP星空灯 | 6012 | 219 | brightness, switch | meteor, speedOn, starrySky |
| `2PG7` | 焕醒大功率推白剃须刀 | ST101 | 170 | battery, status | bladeReset, bladeStatus, travelLock |
| `2PGE` | BOXLAMP星空灯(ProMax) | 6216 | 219 | brightness, switch | meteor, speedOn, starrySky |
| `2PGT` | 研坤牌消毒液制造机 | JX01-4.5-C | 2FF | status, switch | workTime |
| `2PXQ` | 三思智能厨卫灯Pro | C22PL-T12-12W-HM | 21E | brightness, switch | — |
| `2Q1O` | 正尚1路WiFi开关 | ZS-HWTB-SM-11W | 064 | switch, switch1 | CleanPair, Pair, backlight, memorySwitch, mode1 |
| `2Q3F` | 三思插座小夜灯 | C21HI-TP5-1W-HM | 1F9 | lightSwitch, switch | indicator, lightBrightness |
| `2Q3N` | 美菱606WQ7FG1冰箱 | BCD-606WQ7FG1 | 08A | lightSwitch, status | aiEsSwitch, aiNrSwitch, aiSwitch, commonFaultDetection, featureMode, freezeSwitch, freezerFloat, inhibitPurineCabin, intelligentSwitch, photonSwitch, refrigeratorFloat |
| `2Q3O` | 美菱618WQ7SG1冰箱 | BCD-618WQ7SG1 | 08A | lightSwitch, status | aiEsSwitch, aiNrSwitch, aiSwitch, commonFaultDetection, featureMode, freezeSwitch, freezerFloat, inhibitPurineCabin, intelligentSwitch, photonSwitch, refrigeratorFloat |
| `2Q5C` | 力博得智能电动牙刷5Pro | LBT-183509A | 073 | battery, mode | brushingHistory, customPlan, filterElement, gear, polishElement, setWorkTime, voiceGuidance, workGuidance |
| `2QM8` | 幸福星AI智能养生舱 | XFX-889 | 08C | status, switch | commonFaultDetection, energyWaveSwitch, farInfraredSwitch, grapheneGear, hatchMode, leftCountDown, massageGear, negativeOxygenIonSwitch, ozoneSwitch, padTemperature, suspendedSwitch, volume, workTime |
| `2QN2` | 慕思智能床 | BZZ1-139 | 14A | childLockSwitch, status | backControl, commonFaultDetection, foldAngles, getMemoryMode, legControl, memoryControl1, modeSelect, nightLight, oneKeyReset, patService, sleepHelperSwitch |
| `2QN4` | 慕思智能床Pro | MWI1-059 | 14A | childLockSwitch, status | backControl, commonFaultDetection, foldAngles, getMemoryMode, leftSoftHardness, legControl, memoryControl1, modeSelect, nightLight, oneKeyReset, patService, pause, privacyPolicy, rightSoftHardness, sleepHelperSwitch, snoringIntervention |
| `2QQI` | 智能植物灯 | C23ZW003-W0010A27 | 177 | brightness, switch | — |
| `2QSH` | 佳普乐致煦智能浴霸 | BH2ZX-01S | 035 | action, lightSwitch | autoWarmWindSwitch, circulationTime, devCustomInfo, drySwitch, heat, keyToneSwitch, nightLightSwitch, sceneMode, setWorkTime, ventilateSwitch, windSwitch, windTime |
| `2QVS` | 恩仕AXENT集成浴霸 | A812-01 | 035 | lightSwitch, status | autoWarmWindSwitch, automaticWarmWindSwitch, commonFaultDetection, drySwitch, leftTime, setWorkTime, swingSwitch, ventilateSwitch, windSwitch |
| `2QVT` | 恩仕AXENT.NOVIA暗装智能淋浴器 | F602-F3 | 300 | mode, status | coldWaterSwitch, commonFaultDetection, temperatureSetting, waterGear, waterOutletSwitch |
| `2QVX` | 恩仕AXENT.NOVIA智能浴室镜 | V604-M0 | 301 | colourMode, status | demisterSwitch, dryingTime, sterilizeTime |
| `2QWK` | BOXLAMP星空灯(星闪版) | HZ-558 | 219 | brightness, switch | meteor, speedOn, starrySky |
| `2QWO` | 雷神牌等离子体车载消毒机 | LY20 | 18A | pm25, switch | definiteTime, filterElement, tvoc2, windspeed |
| `2QY5` | 尚美源牌QY-NF型纳滤净水设备 | QY-NF-0.25A | 2B5 | status, switch | commonFaultDetection, outputTds, totalPurifyWater, waterSpeed |
| `2QZG` | BOXLAMP星空灯ProMax(星闪版) | HZ-582 | 219 | brightness, switch | meteor, speedOn, starrySky |
| `2R0O` | 福临门控制器 | FLM-001 | 1B0 | action, switch | backLight, height, travelCompensation |
| `2R0U` | 奥普浴霸N50-HW | N50-HW | 035 | action, status | autoWarmWindSwitch, automaticWarmWindSwitch, commonFaultDetection, deodorization, drySwitch, swingSwitch, ventilateSwitch, windSwitch |
| `2R13` | RO反渗透加热一体净水机 | JL-100 | 02D | mode, status | commonFaultDetection, filterElement1, filterElement2, flushSwitch, noMoreOvernightWater, tempMode, waterMode |
| `2R3W` | Ai智能电动晾衣机 | P9-18 | 028 | action, lightSwitch | airDry, disinfect, drying |
| `2R40` | 路福智能床Link9Max | Link9 Max | 14A | lightSwitch, status | audioPlayer, commonFaultDetection, getMemoryMode, headControl, legControl, massGear, massageMode, massageSwitch, massageTimer, modeSelect, nightLight, oneKeyReset, sleepHelperSwitch, sleepstatus |
| `2R44` | 顾家AI智能床垫S8 | 90.ZX.M0580Z | 068 | childLockSwitch, lightSwitch | headAngle, leftSoftHardness, leftWarmBedTemperature, leftWarmBedTime, legAngle, massageGear, modeSelect, positionSelect, rightSoftHardness, rightWarmBedTemperature, rightWarmBedTime, softHardnessSwitch |
| `2R4G` | 寐MINE智能冥想音乐助眠枕 | 1020300092 | 054 | battery, switch | countDown, musicMode, volume |
| `2R5C` | 易慧家推拉驱动Y | CB04TLVH | 02C | action, opener | changeDirection, closeSpeed, commonFaultDetection, handStartSwitch, lockMechanism, lockType, silencer, stroke, switchSpeed, torque, travel |
| `2R8A` | 物联网断路器AICB2C-2PB | AICB2C-2PC6B30 | 211 | action, status | commonFaultDetection, count, ctrl, curNeutral, phaseA, power, proLeak, proOc, proOuv, proSwitch, proTemp, temp, totalForwardEnergy |
| `2R8Y` | 立达信米来吊灯Pro | PLBP-ML02-PR-HM | 21E | brightness, switch | commonFaultDetection, commonMemorySwitch, relBrightness |
| `2RAY` | 求知2pro-HM儿童安全座椅 | B107 | 0DF | battery, switch | babyInStatus, commonFaultDetection, conttonpadStatus, currentTemperature, fanSwitch, fixedTemperatureWind, heatSwitch, musicPlay, supportLegsAlarmSwitch, temperatureAlarmSwitch |
| `2RC9` | 名豆之约智能插座10A 2代 | ZCZ003 | 01D | childLockSwitch, switch | commonFaultDetection, commonMemorySwitch, electric, indicator, power |
| `2RCL` | 名豆之约智能插座16A 2代 | HPS003 | 01D | childLockSwitch, switch | commonFaultDetection, commonMemorySwitch, electric, indicator, power |
| `2RDU` | 蒙奇奇暖宫腰带 | P11 | 17D | battery, mode | countDown, heat, shock |
| `2RHY` | 贝克洛电动平推窗控制器 | Bucalu_001 | 02C | action, opener | commonFaultDetection, lockMechanism, openStatus |
| `2RKB` | 舒适暖宫带C5V3充电仓款 | WZC5V301 | 17D | battery, switch | countDown, hot, hotSwitch, massage, massageSwitch |
| `2RKX` | 慕思智能床Pro H-DESIGN | MWI1-068 | 14A | childLockSwitch, status | backControl, commonFaultDetection, foldAngles, getMemoryMode, leftAutoAdjust, leftSoftHardness, legControl, memoryControl1, modeSelect, nightLight, oneKeyReset, patService, pause, privacyPolicy, rightSoftHardness, rightautoAdjust, sleepHelperSwitch, sleepstatus, snoringIntervention |
| `2RL5` | 台铃-罗马 | TL1200DT-69T | 0C7 | battery, status | lockSwitch, mileage, powerSwitch, seatSwitch, seekSwitch |
| `2RL7` | 慕思智能床Pro1.5m | MWI1-064 | 14A | childLockSwitch, status | backControl, commonFaultDetection, foldAngles, getMemoryMode, leftSoftHardness, legControl, memoryControl1, modeSelect, nightLight, oneKeyReset, patService, pause, privacyPolicy, rightSoftHardness, sleepHelperSwitch, snoringIntervention |
| `2RLA` | 台铃-黑鲨 | TDT6415Z | 0C7 | battery, status | lockSwitch, mileage, powerSwitch, seatSwitch, seekSwitch |
| `2RLF` | 慕思智能床1.5m | BZZ1-061 | 14A | childLockSwitch, status | backControl, commonFaultDetection, foldAngles, getMemoryMode, legControl, memoryControl1, modeSelect, nightLight, oneKeyReset, patService, sleepHelperSwitch |
| `2RLG` | 台铃-封神 | TL1200DT-83T | 0C7 | battery, status | lockSwitch, mileage, powerSwitch, seatSwitch, seekSwitch |
| `2RLH` | 台铃-赤兔2025 | TL1200DT-84T | 0C7 | battery, status | lockSwitch, mileage, powerSwitch, seatSwitch, seekSwitch |
| `2RMF` | FLYX智能往复式剃须刀 | FX1 | 170 | battery, status | bladeClean, bladeReset, bladeStatus, btConnection, commonFaultDetection, searchDevice, speedDetection |
| `2RMK` | 杜亚智能雨水传感器 | RS1 | 048 | battery, switch | commonFaultDetection, rainFall, sensitivity |
| `2RNB` | 西顿照明T5无线单色温筒射灯照明驱动 | SWBH-QL-9W-1 | 226 | brightness, switch | commonFaultDetection, commonMemorySwitch, fadeTimeSetting, indicator, lightCurveSetting, relBrightness |
| `2ROD` | 路福梦享家Link9Pro | Link9Pro | 068 | childLockSwitch, lightSwitch | angleControl, backControl, backMassage, headControl, legControl, lieControl, massageGear, massageMode, memoryControl4, memoryControl6, modeSelect, oneKeyMassage, rightWarmBedTime |
| `2RP6` | 唯斯特姆食物垃圾处理器 | 1999PRO MAX | 0B6 | mode, status | commonFaultDetection, processingcapacity, start, workTime |
| `2RQE` | AI智能健康舱 | STXZ-49 | 08C | status, switch | commonFaultDetection, energyWaveSwitch, farInfraredSwitch, grapheneGear, hatchMode, leftCountDown, massageGear, negativeOxygenIonSwitch, ozoneSwitch, padTemperature, suspendedSwitch, volume, workTime |
| `2RTX` | 小松鼠壁挂炉 | L1PB20-B30D | 174 | mode, switch | bathStatus, bathTemperature, commonFaultDetection, flameStatus, heatStatus, heatTemperature, zeroColdMode |
| `2RVB` | 宝贝第一智能儿童安全座椅 灵智 | R157H | 0DF | battery, childLockSwitch | ISOFIXAlarmSwitch, ISOFIXStatus, antiTipingLegsStatus, babyInStatus, beltStatus, beltSwitch, commonFaultDetection, currentTemperature, fixedTemperature, gear, noForget, position, powerSupply, seatRotation, seatTiltAction, supportLegsAlarmSwitch, touchSwitch, volumeGear, welcomeDirection, welcomeModeSwitch |
| `2RW7` | 淮海新能源车辆QB15 | HH1500DZK-5W | 0C7 | battery, status | commonFaultDetection, drivingMode, lockSwitch, powerSwitch, seatSwitch, seekSwitch |
| `2RYM` | 力博得智能牙刷 博享 | LBT-203557B | 073 | battery, mode | areaSwitch, brushingHistory, filterElement, gear, setWorkTime, spraySwitch, travelLock, voiceGuidance, workGuidance |
| `2RZS` | VITH专研智能电动牙刷 Pro Max | LBT-183509A | 073 | battery, mode | brushingHistory, customPlan, filterElement, polishElement, voiceGuidance, workGuidance |
| `2S0H` | 杜亚智能窗帘C5 | C5 | 01C | action, opener | Direction, switchSpeed |
| `2S0Z` | 贝克洛电动推拉控制器 | Bucalu_002 | 02C | action, opener | commonFaultDetection, lockMechanism, openStatus |
| `2S1R` | 名豆之约智能插座基础款10A | ZCZ006 | 01D | childLockSwitch, switch | indicator, memorySwitch |
| `2S1V` | 电小酷智能插座CP1-HW-B | CP1-HW-B | 01D | childLockSwitch, switch | commonFaultDetection, indicator, memorySwitch |
| `2S2F` | 友望智能活水自清洁剃须刀 | U801 | 170 | battery, status | bladeClean, bladeReset, btConnection, commonFaultDetection, dryingTime, razor, searchDevice, workingTime |
| `2S3R` | 哈尔斯智能焖泡杯 星闪纯钛版 | HTM-420-003/HGM-420-003 | 06B | battery, temperature | canvasConfig, canvasData1, canvasData2, canvasData3, canvasData4, canvasData5, checkedTea, commonFaultDetection, customTeaList, drinkDisturb, drinkRemindArray, findCup, healthRemindArray, lightColor, userData |
| `2S3X` | 哈尔斯智能焖茶壶 星闪纯钛版 | HTM-1200-003/HGM-1200-003 | 06B | battery, temperature | canvasConfig, canvasData1, canvasData2, canvasData3, canvasData4, canvasData5, checkedTea, commonFaultDetection, customTeaList, drinkDisturb, drinkRemindArray, findCup, healthRemindArray, lightColor, userData, waterRemind |
| `2S5M` | 左点智能扫振电动牙刷 | Care 90系列 | 073 | battery, mode | brushingHistory, checkIn, commonFaultDetection, filterElement, hisRecord, record, resetLifeTime, setWorkTime, smart, travelLock, workStatus |
| `2SD7` | 车载摄像头 | SSL-C119 | 354 | battery, switch | cameraInfo, commonFilterElement, connectDev, silencer, videoSwitch, voip, wifi |
| `2SFZ` | 恒洁电热毛巾架LMP835-03E-SN | LMP835-03E-SN | 0BA | status, switch | commonFaultDetection, dryingGear, dryingLeftTime, dryingTime, heat |
| `2SHO` | 恩仕AXENT.META暗装智能淋浴器 | F702-F3 | 300 | mode, status | coldWaterSwitch, commonFaultDetection, temperatureSetting, waterGear, waterOutletSwitch |
| `2SK3` | 公牛智能五孔轨道适配器 | GN-GS30Z | 1FC | switch, switch1 | commonFaultDetection, electric, indicator, power |
| `9MY5` | 智控窗帘 | haTest23 | 01C | leftAction, opener | leftOpener |
| `9MZU` | 智控壁挂炉 | haTest38 | 174 | status, switch | bathTemperature, heatSwitch, heatTemperature |
| `A054` | 飞利浦加湿器HU4908 | HU4908/00 | 052 | humidity, switch | faultDetection, gear |
| `A0DA` | 布谷智能破壁机 | BG-B1 | 02F | action, status | — |
| `A0DF` | 布谷智能取暖器 | BG-ND1 | 06A | switch, temperature | — |
| `A0GS` | 洗碗机 | NP-F86W2F7 | 078 | action, switch | faultDetection |
| `A0MD` | 智汇云窗帘电机 | curtain001 | 01C | mode, opener | — |
| `A0NG` | 智汇云调光面板 | light002 | 01B | brightness, switch | — |
| `A0OV` | 单色球泡灯 | Smart light | 01B | brightness, switch | — |
| `A0R0` | 大金除湿机 | JKT--AV2CW | 09B | mode, switch | commonFaultDetection |
| `A0RO` | 大金地暖 | NH3R--AA | 06A | switch, temperature | choiceOfColdAndHot, commonFaultDetection, silent |
| `A0S7` | 安吉尔-净水设备 | J2733-ROB8 | 02D | status, switch | faultDetection, filterElement1, filterElement2, filterElement3, filterElement4, inputTds, outputTds, startWash, water |
| `A0SJ` | 加湿器SCK-3A40FW | SCK-3A40FW | 052 | humidity, switch | closeTime, windSpeed |
| `A0UO` | 霍尼韦尔智能控制窗帘 | HWcurtain01 | 01C | action, opener | — |
| `A0UQ` | 霍尼韦尔智能控制新风 | HWventilation01 | 030 | fan, switch | — |
| `A0UR` | 霍尼韦尔智能控制地暖 | HWufh01 | 06A | switch, temperature | — |
| `A0UT` | 霍尼韦尔智能控制调光 | HWdimmer01 | 01B | brightness, switch | — |
| `A0XN` | 帅康智慧健康烹饪空间 | CXW-258-H3 | 021 | lightSwitch, switch | airQuality, cookConnect, faultDetection, fengsuiyandong, gear, qingxi, yanshiguanji, youzao, zuozao |
| `A0Y0` | 方太油烟机EM52.i | CXW-258-EM52.i | 021 | lightSwitch, switch | gear |
| `A0Z4` | 西门子开关 | 5TA71112NC | 005 | switch, switch1 | — |
| `A10Y` | 美的智能取暖器 | HYX22KR | 06A | switch, temperature | cleanTimer, faultDetection, orderTime, preTime |
| `A1BU` | 美的抽油烟机 | CXW-260-T70 | 021 | lightSwitch, switch | faultDetection, gear |
| `A1NX` | JSQ30-16JW6i家用供热水燃气快速热水器 | JSQ30-16JW6i | 027 | switch, temperature | commonFaultDetection, cycle, heating, iwaterTmp, totalGas, totalWater, waterfallBath |
| `A1QJ` | 美的PS3002W蒸烤箱 | PS3002W | 024 | action, childLockSwitch | doorState, faultDetection, leftTime, mode1, preheatStatus, setTemperature, setWorkTime, status1, waterBox |
| `A1RM` | 美的CXW-260-B83S抽油烟机 | CXW-260-B83S | 021 | lightSwitch, switch | faultDetection, gear |
| `A1XG` | TCL-AC | KFRd-72LW/DBp-XCA11+B1 | 012 | switch, temperature | ECO, PTC, beepSwitch, newWindAutoSwitch, newWindECOSwitch, newWindPercentage, newWindSwitch, screen, sleep, softWind, targetTemperature, windDirection, windSpeedAutoSwitch, windSpeedPercentage, workMode |
| `A1XQ` | HD-RO-27/A5净水机 | HD-RO-27/A5 | 02D | status, switch | commonFaultDetection, filterElement1, filterElement2, outputTds, purWater, washing, waterPurMode |
| `A1YA` | 颁芙叠影系列烟机 | CXW-200-BF01L36T | 021 | mode, switch | autoClean, clean, faultDetection, gesture, lightSwitch2, manualClean, sensorLight, setTimer, voice |
| `A1YJ` | 无滚布洗地机QX-V6.i-H | QX-V6.i-H | 19F | battery, status | SelfCleanSwitch, VoiceMode, VoiceVolume, WorkMode, cleanwaterboxstate, commonFaultDetection, sewageboxstate |
| `A1YT` | COLMO燃气热水器JSQ30-CE216-Z | JSQ30-CE216-Z | 027 | status, switch | faultDetection, gasLiftPrecent, inWaterTemp, noCold, temp |
| `A2AC` | 统帅L3运动空调 | KFR-72LW/01VDA81TU1 | 012 | switch, temperature | freshWindSpeed, operationMode, windDirectionHorizontal, windDirectionVertical, windSpeed |
| `A2F7` | 颁芙叠影系列燃气热水器 | JSQ37-20SA8 | 027 | status, switch | SetAff, call, commonFaultDetection, commonFilterElement1, mode1, temRange, temperatureSet, waterPressurization, zerocold, zerocold2 |
| `A2IB` | 华凌空调 | KFR-35GW/N8HK1 | 012 | mode, switch | temperature1, temperature2 |
| `A2ID` | 华凌空调 | KFR-72LW/N8HK1 | 012 | mode, switch | temperature1, temperature2 |
| `A2IL` | 方太油烟机EM52.i | CXW-258-EM52.i | 021 | lightSwitch, switch | gear |
| `A2IR` | 方太油烟机CXW-358-Z8T | CXW-358-Z8T | 021 | lightSwitch, switch | AirHouseMode, DelayTime, GestureState, airQuality, gear |
| `A2IY` | 美的多头灶MC-DZC2201 | MC-DZC2201 | 079 | status, switch | commonFaultDetection, relationGear, relationOperation, relationTemperature |
| `A2J3` | 美的踢脚线HDW22EVA1 | HDW22EVA1 | 06A | switch, temperature | buttonBeepSwitch, faultDetection, gear, preTimeOff, preTimeOn |
| `A2LK` | 万和燃气采暖热水炉EU | LL1PBD24-EU24W | 174 | status, switch | Gas, Heatconductionmode, Heatingmode, appointment1, appointment2, appointment3, appointmenton1, appointmenton2, appointmenton3, bathTemperature, faultDetection, flameStatus, heatTemperature, reset, season |
| `A2LM` | 智汇云温控器 | ZHY-KMM3TC03 | 10D | switch, temperature | airCtrl |
| `A2LW` | 温湿度传感器 | TH Sensor | 04E | humidity, temperature | — |
| `A2LZ` | 智汇云燃气传感器 | ZHY-HK005 | 03A | alarm, gasSensor | alert, fault |
| `A2ND` | KEKEN 智能开关2键 | KEN-KK902 | 005 | switch1, switch2 | backlight2 |
| `A2OP` | 智汇云温湿度传感器 | ZHY-HK007 | 04E | humidity, temperature | heat |
| `A2TW` | 智汇云窗帘电机 | ZHY-WDJ001 | 01C | action, opener | oper |
| `A2TY` | 智汇云梦幻帘电机 | ZHY-MML001 | 2BE | action, opener | oper, rotationAction, rotationAngle |
| `A2VL` | 白灯 | 001 | 119 | brightness, switch | — |
| `A2VV` | 18QC1i燃气壁挂炉 | LL1GBQ30-18QC1i | 174 | status, switch | bathTemp, eneMode, faultDetection, heatSwitch, heatTemp, iwaterTmp, totalGas, totalWater |
| `A2W8` | KEKEN 电动窗帘C10 | KEN-C10 | 01C | action, opener | calibration, reverse |
| `A2WS` | 智汇云温控器 | ZHY-KPQ2TC05 | 10D | switch, temperature | airKey |
| `A30K` | 九牧智能毛巾架9340015 | 9340015-P01-1 | 0BA | status, temperature | commonFaultDetection, drying, dryingLeftTime, dryingTime, order1, order2, order3 |
| `A30L` | 美的扫地机V10 | V10 | 031 | action, battery | cleanMode |
| `A30M` | 美的扫地机V12 | V12 | 031 | action, battery | cleanMode |
| `A33C` | 方太油烟机CXW-358-Z8T | CXW-358-Z8T | 021 | lightSwitch, switch | AirHouseMode, DelayTime, GestureState, airQuality, gear |
| `A33L` | 美的扫地机V12(白) | V12 white | 031 | action, battery | cleanMode |
| `A362` | 欧派智能窗帘电机P41 | OP-CCMS-SA01 | 01C | action, opener | CurrentPositionState1, RangeConfig1 |
| `A368` | 欧派智能C单色柜灯带P23 | OP-PS-60W | 222 | brightness, switch | MasterLightMode, MasterLightType, faultDetection |
| `A36A` | 欧派智能二位开关P32 | OP-PLCS-RKRC-2 | 064 | switch1, switch2 | — |
| `A373` | 美的扫地机W20(彩箱) | W20 colourful | 031 | action, battery | cleanMode |
| `A374` | 美的扫地机V12(彩箱) | V12 colourful | 031 | action, battery | cleanMode |
| `A375` | 美的扫地机W20(黑) | W20 black | 031 | action, battery | cleanMode |
| `A37U` | COLMO 洗衣扫拖空间站-机器人 |  8B | 031 | action, battery | cleanMode |
| `A37V` | 小天鹅双囍站-机器人 |  VRD12 | 031 | action, battery | cleanMode |
| `A389` | 小天鹅双囍站-机器人(第二代) | R23W02C | 031 | action, battery | cleanMode |
| `A3A3` | 美的灵眸扫地机器人 W20 Pro | W20 PRO | 031 | action, battery | cleanMode |
| `A3A7` | 美的灵眸扫地机器人V13 | V13 | 031 | action, battery | cleanMode |
| `A3AT` | 美的灵眸扫地机器人 | RM2301 | 031 | action, battery | cleanMode |
| `A3BM` | 方太智能燃气灶具 | JZT-01-DAY1-12T | 090 | action, status | — |
| `A3C5` | 油烟机 | CG5068S | 021 | status, switch | gear |
| `A3CP` | 老板蒸烤一体机 | CQ928 | 19B | action, status | — |
| `A3CQ` | 燃气灶 | 9B328 | 090 | action, status | — |
| `A3CV` | COLMO净饮机 | CWHO-LA61 | 02D | childLockSwitch, status | commonFaultDetection, outputTds |
| `A3CZ` | COLMO软水机 | CWS-F12 | 2B4 | mode, status | commonFaultDetection, filterElement1, waterSpeed |
| `A3D5` | 美的净饮机 | JD2288T-RO | 02D | childLockSwitch, status | commonFaultDetection |
| `A3D7` | 美的软水机 | MS102-1.0T | 2B4 | mode, status | commonFaultDetection, filterElement1, waterSpeed |
| `A3DJ` | 壁挂炉 | QH1i | 174 | mode, switch | aIWarmSwitch, bathMode, bathTemperature, boostMode, faultDetection, heatTemperature, heatingImmediatelySwitch, sterilizationMode, zeroColdSwitch |
| `A3DP` | 老板洗碗机 | WB758 | 078 | action, status | — |
| `A3F1` | 海信智能新风机 | HYXC-KE01 | 030 | fan, switch | — |
| `A3FA` | 美的微蒸烤一体机 | G3E | 023 | action, status | leftTime |
| `A3FS` | COLMO蒸烤箱 | COLMO CCTO50 | 19B | action, status | leftTime |
| `A3GC` | 美的单向流新风机 | MDXF200 | 2FB | status, switch | freshAirSpeed |
| `A3GP` | 格力热水发生器 | NRZ16G/Al | 2FD | switch, temperature | — |
| `A3GQ` | 格力地暖转接器 | NCHS1M | 2FD | switch, temperature | — |
| `A3HD` | A.O.史密斯智能油烟机 | CXW-350-Q2CWi | 021 | lightSwitch, switch | commonFaultDetection, gear, lockSwitch |
| `A3HS` | 方太智能消毒柜 | ZTD200M-02-X20 | 0D5 | action, switch | cabinetDoor, cabinetMode, cabinetRemainingTime, cleaningSwitch, commonFaultDetection, machineStatus |
| `A3IM` | 倍世中央软水机 | BWS-CN1301PSU1 | 2B4 | mode, status | commonFaultDetection, filterElement1, remainWater |
| `A3IR` | A.O.史密斯智能油烟机S系列 | CXW-200-Q5AWi | 021 | lightSwitch, switch | commonFaultDetection, gear, leftFanSwitch, lockSwitch, rightFanSwitch |
| `A3KL` | 美的真省空气源热泵(D)S1 | MHSR80N8-S1 | 2FA | switch, temperature | ECOswitch, heatWaterTemp, keyToneSwitch, light, targetTemp, tempControlMode |
| `A3KW` | 林内燃气壁挂炉G58系列 | L1GB28-24G58 | 174 | mode, switch | antifreezeStatus, bathTemperature, faultDetection, flameStatus, heatSwitch, heatTemperature, heatingImmediatelySwitch, hotWaterSwitch, instantHeatSwitch |
| `A3KX` | 林内燃气壁挂炉RG68系列 | L1GB28-24RG68 | 174 | mode, switch | antifreezeStatus, bathTemperature, faultDetection, flameStatus, heatSwitch, heatTemperature, heatingImmediatelySwitch, hotWaterSwitch, instantHeatSwitch, usuallyReservationSwitch, zeroColdMode, zeroColdSwitch |
| `A3L3` | A.O.史密斯燃气壁挂炉 | L1PB26-V9/CA | 174 | mode, switch | burningTime, commonFaultDetection, flameStatus, heatTemperature, hotWaterPressure, inTemperature, inchingSwitch, machineSafeStatus, zeroColdMode |
| `A3LD` | 美的真省空气源热泵(S)S1 | MHSR180N8-S1 | 2FA | switch, temperature | ECOswitch, heatWaterTemp, keyToneSwitch, light, targetTemp, tempControlMode |
| `A3MR` | 格力新风净化机(60ab) | FHBQGKWL-D5DB | 2FB | mode, switch | freshAirSpeed |
| `A3R1` | 嘉格纳烤箱 | GO241100 | 024 | status, switch | commonFaultDetection, leftTime, oven |
| `A3R2` | 嘉格纳蒸箱 | GS220100 | 022 | status, switch | commonFaultDetection, lackWater, leftTime, steamer |
| `A3R9` | 方太智能净饮制冰机 | YCZ-JT1500-02-X20Max | 06F | childLockSwitch, status | commonFaultDetection, commonFilterElement, commonFilterElement1, fullStopSwitch, iceSwitch, rinseLeftTime, rinseMode, rinseSwitch, rinseTime, voiceSwitch, waterMode |
| `A3RT` | 美的智慧电饭煲 | MB-30M9C | 026 | action, status | commonFaultDetection, cooker, leftTime |
| `A3U5` | 嘉格纳Vario 400 系列酒柜61cm | RW466364 | 0FE | alarm, temperature | bottomShelftemp, commonFaultDetection, middleShelftemp |
| `A3VL` | 嘉格纳Vario 400 系列灶具38cm | VI422115 | 079 | mode, status | heatGear, heating |
| `A3VS` | 火星人集成灶M80BC03 | M80BC03 | 0D4 | action, temperature | SteamOvenMode, SteamOvenPreTimeEnd, SteamOvenSwitch, SteamOvenWorkStatus, SteamOvenWorkTime, commonFaultDetection, kitchenVentLight, kitchenVentRemainingTime, kitchenVentilatorGear, powerSwitch, workBurnerStatus |
| `A3WS` | 滨特尔牌CF300型中央净水机 | CF300 | 2B5 | mode, status | cleanTime, cycleVolume, filterElement2, flushSwitch, rinseMoment, rinseTime, waterPurifier, waterSpeed |
| `A3XM` | 卡萨帝光年油烟机 | CXW-358-C8Z90WGUD | 021 | lightSwitch, switch | gear |
| `A3XO` | 美的智能电压力锅 | MY-S10 | 074 | action, status | commonFaultDetection, cooker, leftTime |
| `A3Y1` | 卡萨帝指挥家油烟机 | CXW-358-C7Q100DGUD | 021 | lightSwitch, switch | gear |
| `A3Y2` | 卡萨帝致境油烟机 | CXW-358-CKQ71UD | 021 | lightSwitch, switch | gear |
| `A3Y5` | 卡萨帝指挥家双抽洗碗机 | CWC20-B59U1 | 078 | action, mode | command, dishwasher, lowerAreaswitch, lowerRegionStatus, remoteCtrAuthTypeDN, remoteCtrAuthTypeUP, statusDoor, statusDoorDN, upperRegionStatus, workMode |
| `A3YD` | 嘉格纳Expressive艺境系列烹饪暖碟抽屉 | GW451120 | 024 | status, switch | commonFaultDetection, leftTime, oven |
| `A3YM` | 滨特尔牌SF270 型软水机 | SF270 | 2B4 | mode, status | filterElement2, hardness, rewaterTime, softerenMode, totalWorkTime, waterPurifier, waterSpeed |
| `A3YN` | 滨特尔牌SF300 型软水机 | SF300 | 2B4 | mode, status | filterElement2, hardness, rewaterTime, softerenMode, totalWorkTime, waterPurifier, waterSpeed |
| `A3Z2` | 西门子蒸玲珑抽屉蒸箱 | BI710C1B1W | 024 | status, switch | commonFaultDetection, leftTime, oven |
| `A3ZF` | 博世蒸如意抽屉蒸箱 | BIC7101B1W | 024 | status, switch | commonFaultDetection, leftTime, oven |
| `A3ZO` | 嘉格纳Minimalistic臻境系列烹饪暖碟抽屉 | GW251100 | 024 | status, switch | commonFaultDetection, leftTime, oven |
| `A410` | A.O.史密斯燃气壁挂炉V3 | L1PB26-V3/AP | 174 | mode, switch | burningTime, commonFaultDetection, flameStatus, heatTemperature, hotWaterPressure, inTemperature, inchingSwitch, machineSafeStatus |
| `A420` | 卡萨帝酒柜JC-260WGCHND7U1(DZ) | JC-260WGCHND7U1(DZ) | 0FE | humidity, temperature | bottomShelftemp, commonFaultDetection, middleShelftemp |
| `O0BY` | 斯百瑞家用无创呼吸机如意系列 | RM-B90 | 0E7 | mode, status | airLeakage, bloodOxygen, capa, comf, epap, heartRate, historicalData, ipap, realtimeData, starttime, usageTime, wet |
| `O0FY` | 斯百瑞新如意无创呼吸机B80 | RM-B80 | 0E7 | mode, status | capa, comf, epap, heater, ipap, ps, riseTime, starttime, wet |
| `O0FZ` | 斯百瑞新如意无创呼吸机C60 | RM-C60 | 0E7 | mode, status | capa, comf, starttime, wet |
| `O0G0` | 斯百瑞新如意无创呼吸机T30 | RM-T30 | 0E7 | mode, status | RampTime, airLeakage, capa, comf, epap, heater, historicalData, ipap, rampStart, realtimeData, riseTime, starttime, usageTime, wet |
| `O0G1` | 斯百瑞新如意无创呼吸机T80 | RM-T80 | 0E7 | mode, status | RampTime, airLeakage, capa, comf, epap, heater, historicalData, ipap, realtimeData, riseTime, starttime, usageTime, wet |
| `ZF08` | 智能中控屏10.1英寸 | PRS-S10 | A10 | humidity, temperature | addDevice, assistant, blueBroadcast, devList, discovery, homeBroadcast, panelMode, recoverConfigSwitch, ringLightSwitch, roomsleeptime, undisturbMode, volSwitch |
| `ZF0A` | 智能中控屏6.6英寸 | PRS-S10 | A10 | humidity, temperature | addDevice, assistant, blueBroadcast, devList, discovery, homeBroadcast, panelMode, recoverConfigSwitch, ringLightSwitch, roomsleeptime, undisturbMode, volSwitch |
| `ZG0I` | 智能开关 (无线版) 1键 | OSLO-BS1 | A13 | childLockSwitch, switch1 | button1, faultDetection, memorySwitch, mode1, modeX, reboot |
| `ZG14` | 调光智能灯 | Dimmable Lamp | A1B | brightness, switch | fadeTime, relBrightness |
| `ZG16` | 调光床头灯 | Dimmable Sleeping Lamp | A1C | brightness, switch | fadeTime, relBrightness |
| `ZG18` | 调光灯带 | Dimmable Light Belt | A1E | brightness, switch | fadeTime, relBrightness |
| `ZG1P` | 华为全屋智能 调光驱动器 2路 双色温 恒压 100W | BER-LD01 | A0E | switch1, switch2 | brightness1, brightness2, cct1, cct2, fadeTime1, fadeTime2, fadeTimeSetting1, fadeTimeSetting2, faultDetection, lightCurveSetting1, lightCurveSetting2, memorySwitch, outputMask, powerCon, relBrightness1, relBrightness2 |
| `ZG2A` | 调光吊灯 | Dimmable Pendant Lamp | A1B | brightness, switch | fadeTime, relBrightness |
| `ZG2B` | 调光磁吸灯 | Dimmable Magnetic Suction Lamp | A1B | brightness, switch | fadeTime, relBrightness |
| `ZG2C` | 调光射灯 | Dimmable Spot Lamp | A1B | brightness, switch | fadeTime, relBrightness |
| `ZG2D` | 调光筒灯 | Dimmable Spotlight | A1B | brightness, switch | fadeTime, relBrightness |
| `ZG2E` | 调光吸顶灯 | Dimmable CeilingLamp | A1B | brightness, switch | fadeTime, relBrightness |
| `ZG2O` | 迈腾智能开关 (无线版) 1键 | PCP-OB1106 | A13 | childLockSwitch, switch1 | button1, faultDetection, memorySwitch, mode1, modeX, reboot |
| `ZG2R` | 智能开关 奥斯陆(无线版) 1键 | PCP-OB1116 | A13 | childLockSwitch, switch1 | button1, faultDetection, memorySwitch, mode1, modeX, reboot |
| `ZG2X` | 智能开关 威尼斯(无线版) 1键 | PCP-OB1116-PF | A13 | childLockSwitch, switch1 | button1, faultDetection, memorySwitch, mode1, modeX, reboot |
| `100E` | 控客Wi-Fi智能插座 | MINI K | 01D | switch | indicator, timerID |
| `100I` | 电烤箱（调试） | HBL-13 | 024 | temperature | faultDetection, gear, oven, workFlow |
| `100l` | 方太智能油烟机 | CXW-200-JQ01TS.H | 021 | switch | gear, kitchenVentilator |
| `100q` | 老板油烟机 | CXW-200-8700 | 021 | switch | connectStatus, gear, kitchenVentilator, stoveSwitch |
| `100y` | 净美仕空气净化器 | A200 | 013 | switch | pm2p5, wind |
| `1011` | BroadLink智能插座 | SP mini3-HL | 01D | switch | timerID |
| `1014` | 门窗开关传感器 | HO-09AZB | 018 | battery | doorSensor |
| `1015` | 四键摇控器 | B910ZB | 038 | battery | keyEvent |
| `1016` | 烟雾传感器 | LH-99ZB | 039 | battery | smoke |
| `1017` | 燃气泄漏传感器 | LH-89ZB | 03A | battery | smoke |
| `101A` | 中控主机 | VKB201 | 020 | mode | — |
| `101E` | 紧急按钮 | VKU201 | 03F | battery | pushButton |
| `101F` | 人体感应 | VKM201 | 03E | battery | motionSensor |
| `101M` | 超薄三 | DG31 | 031 | cleanerRobot | cleanRecord, edge, faultDetection, hepa, roll |
| `101N` | 720环境宝 | EM1003 | 006 | airDetector | — |
| `101V` | 安朗杰西勒奇指纹锁-SC系列 | SC201V | 04B | battery | account, event, lockAlarm, smartLock |
| `101g` | 红外探测器 | LH-990ZB | 03E | battery | motionSensor |
| `101t` | 超薄三 | D36F | 031 | cleanerRobot | cleanRecord, edge, faultDetection, hepa, roll |
| `101u` | 小天鹅洗衣机 | TG30-DSN1 | 015 | switch | faultDetection, washer |
| `101v` | 公牛WiFi智能插座2代 | GN-Y201H | 01D | switch | powerSupply, timerID |
| `101w` | 净美仕空气净化器 | 9188A | 013 | switch | pm2p5, wind |
| `101y` | 美的空气净化器 | 未知 | 013 | switch | airPurifying, pm2p5, vocDetector, wind |
| `1021` | Libratone ZIPP MINI 无线音响 | LTH200 | 00A | battery | Music, faultDetection |
| `1022` | Libratone ZIPP音响 | LTH200 | 00A | battery | Music, faultDetection |
| `1025` | 美的空气净化器 | KJ210G-C46 | 013 | switch | airPurifying, faultDetection, pm2p5, wind |
| `1028` | 汇泰龙云锁 | H17 | 04B | battery | account, event, lockAlarm, smartLock |
| `103J` | 声光报警器 | HC-109ZB | 040 | battery | alertor |
| `103K` | 美的智能吸尘器VR1716 | VR1716 | 031 | cleanerRobot | cleanRecord, edge, faultDetection, hepa, roll |
| `103L` | 美的智能吸尘器VR1717 | VR1717 | 031 | cleanerRobot | cleanRecord, edge, faultDetection, hepa, roll |
| `103Q` | 欧普蓝牙门磁OPLYMC | OPLYMC | 018 | battery | doorSensor |
| `103R` | 欧普蓝牙红外OPLYHW | OPLYHW | 03E | battery | motionSensor |
| `103S` | 欧普蓝牙开关OPLYKG | OPLYKG | 005 | battery | button, faultDetection |
| `103W` | 国投主控1路开关1LA | SMK-01-1LA | 005 | switch | — |
| `1042` | 国投电动燃气开关MTS | SMK-01-MTS | 05C | battery | gasValve |
| `1043` |  | SMK-01-16A |  | switch | — |
| `1045` |  | SMS-01-WIN | 018 | battery | doorSensor |
| `1047` | 国投紧急按钮SOS | SMS-01-SOS  | 03F | battery | pushButton |
| `104A` | 国投二氧化碳传感器CO2 | SMS-01-CO2 | 05B | airDetector | — |
| `104C` | 国投PM2.5传感器PMX | SMS-01-PMX | 043 | airDetector | — |
| `104D` | 国投光照传感器LUX | SMS-01-LUX | 048 | luminance | — |
| `104N` | 安朗杰西勒奇指纹锁-SE系列 | SE201V | 04B | battery | account, event, lockAlarm, smartLock |
| `104O` | 品多智能指纹门锁M1 | M1 | 04B | battery | account, discovery, event, faultDetection, lockAlarm, smartLock |
| `104R` | Wulian智尚一路开关 | WL-ZCSWLMS-S1311-01 | 005 | switch | — |
| `104U` |  | SR-ZCCENPW-M142011-02 | 01C | openLevel | — |
| `104X` | 柏翠电烤箱PE5389WH | PE5389WH | 024 | temperature | downTemperature, faultDetection, oven, upTemperature |
| `1050` | 瑞晶六合一空气检测器RAD-1 | RAD-1 | 006 | airDetector | — |
| `1051` | 瑞晶新风RAC-1 | RAC-1 | 030 | switch | faultDetection, freshAir, wind |
| `105D` | 易百珑单路多功能接收器ERC309-H | ERC309-H | 064 | switch | — |
| `105I` |  |  |  | switch | — |
| `105M` | 欧瑞博智能插座S30c | S30c | 01D | switch | timerID |
| `105R` | 小米人体传感器 | 未知 | 01A | battery | motionSensor |
| `1063` | 飞比人体传感器NBOT106W-M2 | NBOT106W-M2 | 03E | battery | motionSensor |
| `1065` | 飞比烟雾传感器NSMF106W-M2 | NSMF106W-M2 | 039 | battery | smoke |
| `106A` | 顺舟燃气报警SZ09-(02) | SZ09-(02) | 03A | battery | smoke |
| `106B` | 顺舟人体红外感应SZ09-(04) | SZ09-(04) | 03E | battery | motionSensor |
| `106E` | 顺舟烟雾传感器SZ09-(11) | SZ09-(11) | 039 | battery | smoke |
| `106F` | 顺舟西勒奇门锁SZ09-(19)-320C  | SZ09-(19)-320C | 04B | battery | account, event, lockAlarm, smartLock |
| `106K` |  | WL-ZSPWBPW-PI11-02 | 03E | battery | motionSensor |
| `107M` | 空气堡智慧新风系统NEX-360H | NEX-360H | 030 | airDetector | devOta, faultCode, freshAir, heat, hepa, mediumFilter, ozoneFilter, primaryFilter, screen |
| `107V` | Sonoff basic wifi智能开关 | ITA-GZ1-GL | 005 | switch | startup |
| `107W` | Sonoff POW R2电量监测wifi开关 | ITA-GZ1-GL | 005 | switch | alarmType, energyConsumtion, historyConsumption, onceStatistics, powerProtect, startup |
| `108M` | 西睿空气检测仪底座 | 5UH70811NC01 | 006 | airDetector | airQualityReminder, city, cube, screenSetting |
| `108T` | 720全效空气净化器 | KJ500F-EP500H | 013 | switch | airPurifying, faultDetection, filterElement, pm2p5, wind |
| `108U` |  | KA5 | 013 | switch | airPurifying, faultDetection, filterElement, wind |
| `108X` | 公牛WiFi智能插座（基础V2版） | GN-Y201H | 01D | switch | powerSupply, timerID |
| `110E` | 华为智选 火火兔智能早教故事机 | H1 | 08D | switch | custom, earLight, faceLight, music, timedTask |
| `110Q` | 亚都加湿器SC175-S040Hi | SC175-S040(Hi) | 052 | switch | Sound, gear, light, timing |
| `111W` | 宠物智能喂食器 | V1.0 | 000 | status | copies, faultInfo, feedMode, feedTime, meals, totalCopies |
| `112F` | 博泰智能插座SK505W | SK505W | 01D | switch | backlight, timerID |
| `113C` | 豪恩人体传感器 | LH-992ZB | 03E | battery | motionSensor |
| `113G` | SONOFF TX1C 智能墙壁开关 | T2UK1C | 005 | switch1 | powerLight, pulseLength1, pulseSwitch1, startup1 |
| `113L` | 汇泰龙智能指纹锁 | HiMate-SL0-HN | 04B | battery | doorbell, keyList, keyOperate, lockAlarm, lockEvent, lockStatus, publicKey, settingSwitch, tempCode, userList, wakeup |
| `115P` | HDL新风 | HDL-AC | 030 | switch | freshAir |
| `115S` | HDL空气质量传感器 | HDL-MASLA | 043 | pm25 | — |
| `115U` | 空气堡智慧新风系统ZEN-160H | ZEN-160H | 030 | airDetector | faultCode, freshAir, heat, screen |
| `116X` | HDL窗帘 | V1.0 | 01C | openLevel | — |
| `118H` | 箭牌智能坐便器 | AKB1199 | 066 | switch | device_status, deviceupdate, netinfo, setting, usermodel, warning |
| `120P` | 海令智能门磁传感器 | SMK-WD-001 | 018 | battery | doorSensor |
| `120Q` | 海令智能烟感报警器 | SMK-H1-FIRE | 039 | battery | smoke |
| `120T` |  | SMK-RF-001 | 03E | battery | motionSensor |
| `121A` | 海令智能开关面板 | SMK-H1-1L | 005 | switch | — |
| `121W` | 一位免零线智能开关 | Z9/31/1 | 005 | switch | switchLable |
| `122E` | 继电器模块 | V1.0 | 01B | switch | power |
| `122T` | 智能二三极插座 | Z9/426/10USL | 01D | switch | switchLable01, switchLable02 |
| `122W` | 品多智能指纹门锁H1 | H1 | 04B | battery | account, discovery, event, faultcode, lockAlarm, smartLock |
| `123K` | 一位智能窗帘开关 | Z9/CK | 01C | motor | curtainLable |
| `124U` | 正泰智能插座 | 1.0 | 01D | switch | consumption, faultDetection, memorySwitch, power, timerInfo |
| `124Y` | 即来智能插座C0102 | C0102 | 01D | switch | powerLight, timerID |
| `131Y` | 青稞智能锁_Q7 | Q7 | 04B | battery | event, faultCode, heartBeat, keyList, lastActionTime, lockAlarm, lockMode, lockState, prePowerSwitch, publicKey, remoteCode, remoteResult, userList |
| `134V` | 凯迪仕智能门锁 | S300 | 04B | battery | event, faultCode, keyList, lastActionTime, lockAlarm, lockMode, lockState |
| `137J` | 祈禧智能即热饮水吧YR-25C208 | YR-25C208 | 06F | switch | breakdown, dataWater, deviceStatus, filterElement, setUpWater, waterCond |
| `138F` | 大宇电风扇 | DWF-J12H | 029 | mode | binarySwitch, endTime, onOffLight, speed, swayLeftRight |
| `138S` | 微虎个人冷风扇 | MH01RW | 029 | mode | binarySwitch, consumables, speed |
| `140H` | 控客一路灯光面板 | KK-LP-C01E | 064 | switch | — |
| `140V` | 窗帘控制器 | BZ-HU-W | 01C | motor | — |
| `140W` | 窗帘控制器 | BZ402 | 01C | motor | — |
| `140X` | 开关回路控制器 | BZ416R | 064 | switch | — |
| `140Y` | 开关回路控制器 | BZ-HU-003B | 064 | switch | — |
| `141R` | 杜亚智能百叶DM25 | DM25百叶 | 01C | opener | schedule, sunSwitch, tilt |
| `141W` | 杜亚智能百叶DM35 | DM35百叶 | 01C | opener | schedule, sunSwitch, tilt |
| `141Z` | 杜亚智能窗帘DH3 | DH3 | 01C | opener | schedule |
| `144R` | 杜亚智能卷帘DM25 | DM25卷帘 | 04D | opener | schedule |
| `144S` | 杜亚智能卷帘DM35 | DM35卷帘 | 04D | opener | schedule |
| `146C` | 公牛智能插座-GN-Y201H | GN-Y201H | 01D | switch | backlight, memorySwitch |
| `148M` | 正泰快充智能插排 | 1.0 | 01E | switch | consumption, faultDetection, memorySwitch, power |
| `151J` | 蓝牙情景面板（双键） | OP-PANEL-2KEYS | 075 | battery | button, buttonName |
| `151K` | 蓝牙情景面板（四键） | BLE-PANEL-4KEYS | 075 | battery | button, buttonName |
| `151L` | 蓝牙情景面板（六键） | BLE-PANEL-6KEYS | 075 | battery | button, buttonName |
| `152F` | 平头熊移动插座(WIFI) | PTX-PLUS01 | 01D | switch | backlight |
| `152S` | 艾沃家用净水器 | AWR805-4 | 02D | status | filterElement1, filterElement2, inputTds, outputTds, purifyWater |
| `155V` | 欧派纯水机 | CY-JS810B | 02D | status | faultDetection, filterElement1, filterElement2, filterElement3, filterElement4, outputTds |
| `157I` | 酷轻松石墨烯发热护膝 | PMA-O30 | 000 | switch | — |
| `157X` | 威廷智能单开Wi-Fi | VE-AK01LNW | 005 | switch | — |
| `162W` | 卡赫智能吸尘器 | V1.0 | 069 | battery | ChildLock, Error, VacuumStatus, WorkMethod, filterElement, leftTime, workRecord |
| `163Q` | 智能单开开关 | VE-AK01LNB | 005 | switch1 | — |
| `167U` | Gimbal Pro-L7B-Pro | L7Bpro | 000 | switch | — |
| `168M` | 三思智能面板开关 | C21HI-TP7-1.5W | 01B | switch | yedengstatus, yedengsw |
| `170W` | 720 全效空气净化器 S(C400) | KJ400F-C400 | 013 | switch | airPurifying, faultDetection, filterElement, pm2p5, wind |
| `171Y` | 阿乐乐可模方插座智能家居 | 1073X | 01D | switch | memorySwitch |
| `174O` | 平头熊智能86插座 | PTX-socket01 | 01D | switch | backlight |
| `174W` | 多功能按摩脚机HiLink版 | EW-817H | 0CC | switch | Heat, Intensity, WorkMode |
| `175R` | 平头熊一键开关WIFI | PTX-TCswitch01 | 005 | switch1 | — |
| `176I` | 极米投影仪H3S | XK03K | 098 | switch | BACK, DPADCENTER, DPADDOWN, DPADLEFT, DPADRIGHT, DPADUP, FOCUS, FOCUSAUTO, FOCUSLEFT, FOCUSRIGHT, HOME, KPPOWER, MENU, MOVEHOME, POWER, RESTART, VOLUMEDOWN, VOLUMEPRESS, VOLUMEUP |
| `176Y` | 极米投影仪RS PRO 2 | XK03J | 098 | switch | BACK, DPADCENTER, DPADDOWN, DPADLEFT, DPADRIGHT, DPADUP, FOCUS, FOCUSAUTO, FOCUSLEFT, FOCUSRIGHT, HOME, KPPOWER, MENU, MOVEHOME, POWER, RESTART, VOLUMEDOWN, VOLUMEPRESS, VOLUMEUP |
| `177T` | VANOW智能办公杯 | V2 | 06B | battery | charge, lightTime, reminder, tds, temp |
| `181W` | 噼啪智能单开开关 | PIPA-AK01LNW | 005 | switch | — |
| `183F` | 噼啪智能插座 | PIPA-AC02W | 01D | switch | — |
| `183N` | 天博智-智点点T91 | T91 | 0AF | switch | DeviceContro0012, DeviceContro0013, DeviceControl0010, DeviceControl0011, DeviceState0006, DeviceState0008, DeviceState0009, DeviceWiFiSet0013 |
| `186X` | 欧派煤气灶 | JZT/Y-Q906A | 090 | status | autoTurnOff, faultDetection, heatGear |
| `188B` | 威廷智能插座 | VE-AC02W | 01D | switch | — |
| `2001` | YESOUL野小兽智能健腹轮 | J20 | 0C2 | battery | ClassPart, CumulativeValue, Devicestatus, Disconnecttips, Pause, Sporttype, StartSports, calorie, count, worktime |
| `200G` | 麦乐克紧急按钮 | MIR-SO100 | 03F | battery | button, pushButton |
| `201T` | 小豚当家AI全彩摄像头 双频版 | DPH-IP-350 | 008 | switch | alarmEvent, secSwitch, shootSwitch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 |
| `201V` | 领普三键无线开关MESH | K9BB(HW) | 075 | battery | button1, button2, button3 |
| `201Y` | 领普双键无线开关MESH | K9BB(HW) | 075 | battery | button1, button2 |
| `201Z` | 领普单键无线开关MESH | K9BB(HW) | 075 | battery | button1 |
| `2025` | 酷轻松石墨烯手部按摩仪 | K-SBAMY-B2V2 | 0D0 | switch | Battery, GenderSelection, Heating, Mode, workStatus, workingTime |
| `202O` | 长虹8809浴用加热器_足浴器 | CDN-ZY8809 | 070 | switch | bubble, commonFaultDetection, leftTimeDIY, massage, operateTemperature, ozone, stayTime, temperatureDIY |
| `202U` | 长虹8818浴用加热器_足浴器 | CDN-ZY8818 | 070 | switch | commonFaultDetection, countdown, leftTimeDIY, massage, modelDIY, operateTemperature, surf, temperatureDIY |
| `203F` | YESOUL野小兽筋膜枪 | MG11S | 0C5 | switch | Stall, TimeRemaining |
| `203I` | 鸿雁智能插座 | IHC8301C | 01D | switch | backlight, protect, switchLock |
| `204U` | 便携式深层肌肉按摩仪 | QL/HS6–A | 0C5 | switch | CountDown, LifeTimer, Power, commonFaultDetection, gear |
| `205O` | VOC智能门锁 | X8 | 04B | battery | event, faultCode, keyList, lastActionTime, lockAlarm, lockMode, lockState, publicKey, remoteCode, remoteResult |
| `205U` | JoinOne亲肤暖雾加湿器 | HW-3600WF | 052 | switch | Timer, faultDetection |
| `206A` | 立久佳跑步机 | JD600 | 08F | switch | intensity, tempo |
| `2082` | 白色零火线单路灯控面板超薄 | KK-LP-C01E | 005 | switch | — |
| `208K` | 左点小艾3代智能艾灸盒 | ZD-A11 | 0C3 | switch | Lowbattery, Temperaturesetting, Timesetting, comfortablemode, commonMode1, conventionalmode, dumpenergy, hotmode, keylock, partingmode, screenswitch, timeremaining |
| `208Z` | 酷轻松智能发热手套 | K-ST-B2V2 | 0D0 | switch | Temperature, targetTemperature, workingTime, workstatue |
| `2091` | 酷轻松石墨烯发热围巾 | K-WJ-B2V3 | 0D0 | switch | heat, temprature, timerlabel, workstatue |
| `20BB` | 希影智能投影仪L12 | L12 | 098 | switch | arrow, system, volume |
| `20C0` | 云康宝筋膜枪 | CM10B | 0C5 | switch | Timing, gear, informationdisplay, realtimestatus |
| `20C1` | 未来小七机器人 | F617 | 08D | switch | — |
| `20DJ` | 博联智能插座SP4-HL | SP4-HL | 01D | switch | memorySwitch |
| `20F5` |  |  | 01C | mode | — |
| `20FH` | 海令中控主机 | SMK-H1-GTW04 | 020 | switch | devOta |
| `20FS` | 华为智选 火火兔智能早教故事机 | H1 | 08D | switch | earLight, faceLight, musicPlay, volume |
| `20GX` | 领普单键零火墙壁开关 | Q3D-HW-W1 | 005 | switch | led |
| `20K4` | 控客10A智能插座 | KK-PP-C20W | 01D | switch | — |
| `20K5` | 控客紧急呼叫按钮 | 1.0 | 03F | battery | pushButton |
| `20K7` | 控客16A智能插座 | KK-PP-C26W | 01D | switch | — |
| `20K8` | 控客推窗器面板 | KK-WP-C12W | 02C | mode | — |
| `20KA` |  | KK-CP-C12W | 01C | mode | — |
| `20KC` | 控客快捷面板 | KK-QP-C13W | 075 | battery | buttonName |
| `20PN` | FIVE智能刀筷砧板杀菌架 | YSXDJ001HJHI | 0D5 | alarm | CustTime, LeftTime, Lock, TargetTime, cabinetMode, cabinetStatus, cabinetSwitch |
| `20QN` | 荣泰蜘蛛侠摩舒枕 | K31HiLink | 0CA | switch | Heat, LEVLE, MODE, Time, Workinghours |
| `20S4` | 艾优智能剃须刀 | T8-H | 000 | mode | Cleaningcutting, Cuttinghead, Reset, commonMemorySwitch1, nowbetty, prompt, smartmode, speed |
| `20SV` | eefit元气通二代 | Det-S10 | 0D0 | switch | — |
| `20TG` | 欧派净水器 | CY-JS821 | 02D | status | commonTask1, faultDetection, filterElement1, filterElement2, outputTds |
| `20U3` | GPWELL胶囊咖啡机 | GP100 | 0B9 | switch | Star, commonFaultDetection, cupChoose, cupVolume, currentOutlet, reset, status2, temp |
| `20UF` | 立久佳跑步机 | X7 | 08F | switch | intensity, tempo |
| `20UZ` | 立久佳跑步机 | A6 | 08F | switch | calorie, distance, duration, heartrate, tempo |
| `20XK` | 控客-星空单路灯控面板 | KK-LP-L01W | 005 | switch | — |
| `20XL` | 杰诺无线清洗机 | F1S | 000 | mode | AbnormalPrompt, cumulativeTime, electric |
| `20Y5` | 控客-星空单路窗帘面板 | KK-CP-L01W | 0BE | mode | — |
| `20YI` | 控客-人体红外传感器 | KK-BS-J01W | 03E | battery | motionDetected |
| `20YL` | 小恬空气灭菌加湿器 | KD001 | 052 | switch | COV, Level, SL, SMODE, ST, WAT, WT |
| `20Z0` | 控客-燃气报警器 | JT-LH-801 | 03A | alarm | commonFaultDetection |
| `20Z9` | 控客-红外幕帘探测器 | KK-CS-K02 | 049 | battery | dismantle, motionDetected |
| `20ZB` | MBH跑步机 | HT | 08F | switch | dist, kcal, speed |
| `20ZG` | 青稞智能锁_N5H | A7H | 04B | battery | event, faultCode, heartBeat, keyList, lastActionTime, lockAlarm, lockMode, lockState, prePowerSwitch, publicKey, remoteCode, remoteResult, userList |
| `210D` | 左点颈椎按摩仪 | ZD-AMY-WH6 | 0CE | switch | commonMode1 |
| `211G` | 阿尔法蛋智能词典笔S | TYS01 | 0AF | battery | dict, otareport, rdp, statistic |
| `211L` | 壹指盾Q6H指静脉智能锁 | WF-H861-RTA1 | 04B | battery | event, heartbeatTime, lastActionTime, lockAlarm, lockMode, lockState, publicKey, remoteCode, remoteInfo, remoteResult, userList |
| `2136` | 左点腰椎按摩器 | Y6 | 0CA | switch | Hotcompressgear, Kneadingmode, Lowbattery, Massagemode, Pressthemode, Strengthofgear, Timesetting, commonMode1, dumpenergy, timeremaining |
| `214X` | 智汇云一位轻触开关面板 | Z4001 | 005 | switch | — |
| `215F` | 清易无线吸尘器 | QYXCQ01 | 069 | status | area, batterylevel, calorie, cleanmark, commonFaultDetection, commonFilterElement1, commonFilterElement2, offscreentime, powersetting, worktime |
| `215L` | 触控单开零火开关 | U4030100 | 005 | switch | — |
| `215R` | 紧急按钮 | U4080100 | 03F | battery | pushButton |
| `215T` | 可燃气体探测器 | U4041200 | 03A | alarm | — |
| `2160` | 红外幕帘探测器 | U4081100 | 049 | battery | motionDetected |
| `2161` | 红外人体探测器 | U4080400 | 03E | battery | motionDetected |
| `2163` | 触控单路窗帘电机控制面板 | U4070600 | 01C | mode | — |
| `2164` | 触控双路窗帘电机控制面板 | U4070702 | 01C | mode | outMode |
| `216X` | 亚摩斯加湿器AS-V22Q | AS-V22Q | 052 | switch | faultDetection, gear, light, timing |
| `2173` | 小嘀全自动智能锁Q3H | Q3H | 04B | battery | event, faultCode, keyList, lastActionTime, lockAlarm, lockMode, lockState |
| `2174` | HEIMAN智能燃气报警器 | HS1CG | 03A | alarm | commonFaultDetection, selfCheck |
| `217M` | 开关智能控制器1型 | U4030100 | 005 | switch | — |
| `217P` | 控客-肖邦一路灯光面板 | KK-LP-D81W | 064 | switch | — |
| `217T` |  | KK-CP-D81W | 01C | mode | — |
| `217V` | 控客-肖邦10A智能插座 | KK-PP-C20W | 01D | switch | — |
| `217W` | 控客-肖邦16A智能插座 | KK-PP-D26W | 01D | switch | — |
| `2181` |  | KK-BS-K02 | 03E | battery | motionDetected |
| `2184` | HEIMAN智能紧急按钮 | HS2EB-BH | 03F | battery | pushButton |
| `2191` | HEIMAN智能情景开关 | HS2SS-BH | 075 | battery | sceneState |
| `219N` | ENO智能水杯 | HW-001 | 06B | temperature | alarmTime1, blessing, count, drinkwaterHistory, waterclock |
| `219P` | 酷轻松石墨烯气囊支撑腰带 | PMA-D30 | 000 | switch | — |
| `21A1` |  | KK-GA-H04 | 03A | alarm | faultDetection |
| `21B2` | 单键智能开关面板尊享版 | BL8371RC2-GTK1 | 01B | switch | — |
| `21B7` | 单键智能开关面板时尚版 | BL8031RP4-RGTKD1 | 01B | switch | backlightMode |
| `21B8` | 单键智能开关面板尊享版 | BL8371RC2-RGTKD1 | 01B | switch | backlightMode |
| `21C1` | 帝王智能座便器 | TA014-3-0305Y/CEV | 066 | mode | Bigwater, Light, RInggear, Radar, WaterTemperature, clean, deodorizeSwitch, display, faultDetection, gear, hot, intensity, lamp, move, nozzlePosition, online, ring, seat, smallwater |
| `21DE` | 云起奇点开关模块PRO一联 | LS191 | 064 | switch | memoryState |
| `21DF` | 云起奇点开关模块PRO二联 | LS192 | 064 | switch | memoryState, switch01, switch02 |
| `21DG` | 云起奇点开关模块PRO三联 | LS193 | 064 | switch | memoryState, switch01, switch02, switch03 |
| `21DO` | HEIMAN燃气报警器 | WS2CG | 03A | alarm | Alarmthreshold, Language, Mute, PERIOD, Robot, Sensorselftest, VolumeSetting, equipmentStatus |
| `21EA` | 觅石超声波清洗机 | GH01 | 000 | switch | commonMode1 |
| `21EI` | JW智能照明开关灯 | JHKJ_Light_V1 | 01B | switch | — |
| `21ES` | JW智能窗帘A型 | JHKJ_Curtain_V1 | 01C | mode | — |
| `21G7` | JW光照检测器 | U40411060 | 048 | luminance | — |
| `21G9` | JW门磁 | JHKJ_DS_V1 | 018 | status | doorEvent |
| `21GK` | JW智能开关1键型 | JHKJ_PANEL_KEY1 | 005 | switch | — |
| `21GN` | JW红外人体感应 | JHKJ_PD_V1 | 03E | battery | motionDetected |
| `21GX` | 达阔电蚊香 | ADKZDHL-202001 | 0B0 | switch | Mode, commonFilterElement1 |
| `21I3` | 三思插座小夜灯 | C21HI-TP5-1W | 01B | switch | yedengstatus, yedengsw |
| `21LC` | 米立多合一网关 | MS-G9112M | 020 | switch | devOta |
| `21LD` | 米立1路窗帘控制面板 | MS-V6611G | 01C | mode | — |
| `21LF` | 米立1路智能开关面板 | MS-V8611G | 005 | switch | — |
| `21LK` | 米立紧急报警按钮 | MS-P4741F | 03F | battery | pushButton |
| `21LL` | 米立红外探测器 | MS-P8761F | 049 | battery | motionDetected, tamperAlarm |
| `21LO` | 欧普智能紫外杀菌灯 | OP-UV-L03 | 01B | switch | TimeLeft, commonFaultDetection, commonMode1 |
| `21M4` | 酷轻松石墨烯智能艾灸仪 | PMA-A30 | 0C3 | switch | Battery, Temperature, targetTemperature, workingTime |
| `21M5` | 赤兔Air1智能跑步机 | Air1 | 08F | switch | distance, kcal, po, speedtiao |
| `21MO` | 酷轻松石墨烯发热真丝暖腹宝 | PMA-Q30 | 000 | switch | — |
| `21MT` | 艾谱保险箱 | apsafe01 | 08B | switch | ar, bp, lockstate, oo |
| `21N2` | 欧普智能网关 | OP-WG02 | 020 | switch | — |
| `21NQ` | sraum智能家居网关 | SP-D0Z0-W02 | 020 | switch | discovery |
| `21NZ` | A.O.史密斯中央净水机 | WF25G2 | 02D | status | faultDetection, filterElement, flushTime, purifyWater, useTime, waterSpeed |
| `21OA` | A.O.史密斯反渗透净水机 | R1200BN1 | 02D | status | faultDetection, filterElement, flushTime, purifyWater, useTime, waterSpeed |
| `21OU` | 公牛WiFi智能插座基础V3版 | GN-Y201H | 01D | switch | backlight, memorySwitch |
| `21P9` | 开关灯（底盒开关控制器） | CP2001H | 064 | switch | — |
| `21PG` | 触点开关 | CP7201H | 064 | switch | — |
| `21PH` | 人体移动传感器 | MR5035H | 03E | status | — |
| `21PR` | 烟雾传感器 | LH-94 | 039 | battery | smoke |
| `21PS` | 燃气传感器 | LH-86+ | 03A | alarm | — |
| `21RL` | 华为智选 德施曼智能门锁 | SHEP-SL0-DN | 04B | battery | enableState, event, faultCode, heartbeatTime, keyList, keyOperate, lastActionTime, lockAlarm, lockDefense, lockMode, lockState, publicKey, remoteCode, remoteEnable, remoteInfo, remoteResult, upgradeMode |
| `21RM` | 华为智选 德施曼智能门锁Pro | SHEP-SL0-DNPro | 04B | battery | enableState, event, faultCode, heartbeatTime, keyList, keyOperate, lastActionTime, lockAlarm, lockDefense, lockMode, lockState, publicKey, remoteCode, remoteEnable, remoteInfo, remoteResult, upgradeMode |
| `21SR` | 开关卷帘 | CP7201H | 0B5 | action | — |
| `21TS` | 狄耐克智能插座 |  SH-WAB-SKT503 | 01D | switch | — |
| `21TX` | 西顿开关控制模块 | SWP01-CK-200W | 064 | switch | — |
| `21US` | 鸿雁16A智能插座 | IHC8361H | 01D | switch | backlight, protect, switchLock |
| `21V2` | 瑞晶智能开关 | RGBLE-R-S1 | 064 | switch1 | — |
| `21VY` | 瑞晶开关灯 | RGBLE-R-L1 | 01B | switch | — |
| `21W9` | 友宏智能跳绳 | 2023 | 095 | mode | countRecord, level, record, versionNumber |
| `21WL` | 大拿便携冲牙器 | D0-F11 | 000 | switch | Efimode, Gentlemode, Gumtypes, Massagemode, Usethebible, Usingthelength, electricity, record, standardmodel, tip, waterpressure |
| `21XA` | 瑞晶开合帘 | RGBLE-KH | 01C | mode | — |
| `21XE` | 瑞晶百叶帘 | RGBLE-BY | 01C | mode | — |
| `21XF` | 瑞晶卷帘 | RGBLE-JL | 04D | action | — |
| `21XK` | 瑞晶燃气探测器 | RG-GAS24A | 03A | alarm | — |
| `21XW` | 水立洁净水器 | S3 | 02D | status | faultDetection, filterElement1, filterElement2, filterElement3 |
| `21YH` | 瑞晶智能门锁 | RG-M1 | 04B | alarm | doorEvent, doorState |
| `21YX` | 瑞晶背景音乐 | RGYZ-62 | 000 | switch | CutOver, Play, SoundChannel, Volume |
| `220N` | 人体存在传感器 | MR5009H | 03E | status | — |
| `2212` | REMAC+86型嵌入式网关 | A3Z-WG-01 | 020 | alarm | alertor, devOta, discovery |
| `2219` | 艾谱灵镜保管箱 | BGX-X1-30LG | 08B | switch | ar, bp, lockstate, oo |
| `221G` |  | A3Z-CL-01 | 075 | mode | — |
| `221K` |  | T-INF30 | 03E | battery | motionDetected |
| `221M` |  | SL1018B/DN20 | 000 | switch | — |
| `221T` |  | A3Z-DK-01 | 005 | switch | — |
| `221X` |  | UEN-125CM1P | 000 | switch | electric, reverseTimes |
| `221Y` |  | UEN-125CM3P | 000 | switch | electric, reverseTimes |
| `2221` |  | A3Z-CZ-0510A | 01D | switch | — |
| `2246` |  | CP2007H | 064 | switch | — |
| `2247` |  | CP2003H | 064 | switch | — |
| `224O` |  | CP8010H | 064 | switch | — |
| `225B` | i-Respix-等离子甲醛清除机 | DZ005 | 013 | switch | Led, commonMode1 |
| `2265` | 凯迪仕智能门锁HK600 | HK600 | 04B | battery | event, faultCode, keyList, lastActionTime, lockAlarm, lockMode, lockState, lockStatus |
| `2269` | 瑞晶安防控制器 | RGAF-GATE | 000 | switch | Disarm, devOta |
| `226H` | 门磁 | MR5205H | 018 | status | doorEvent |
| `227Q` | 光传感器 | MR5011H | 048 | luminance | — |
| `227S` | 亚摩斯睿雅单火开关单键 | ZJ-KG31H | 005 | switch | — |
| `22BI` | 乐尔康按摩椅988C9 | LEK-988C9 | 05F | switch | autoMode, backAction, gravitySwitch, heatSwitch, manuMode, manualAction, massGear, mechanicalAction, ppmAction, pressureState, remainingTime, soleAction, stop, widthAction, workTime |
| `22DN` | IPL光子嫩肤脱毛仪 | OES-Y1 | 000 | mode | FlashRecording, Icing, LengthDepilation, Outgoing, directionUse, gears |
| `22DS` | 力博得智能声波牙刷2 冰山款 | LBT-153019A | 073 | status | audioSwitch, batterys, brushDay, brushScore, brushSettings, brushingHistory, brushingHistorys, clear, misicState |
| `22DT` | 捷昌智能橱柜 | JC37B | 000 | status | commonFaultDetection, commonMemoryControl1, ctrl, currentheight |
| `22G1` | E.keyco牌HX-E12-D型反渗透净水器 | HX-E12-D | 02D | switch | Alarm, Cartridgelife, Cartridgelife2, Flushingcontrol, PurewaterTDS, Singlewateryield, Totalnetwater, Totalwastewater, statu, watertemperature |
| `22GO` | 指力大师按摩椅 | A60Hilink+ | 05F | switch | autoMode, backDown, backUp, heatMode, legDown, legUp, manuMode, massGear, soleSwitch, zero |
| `22GT` | 眠虫纯石墨烯暖宫腰带 | ST7060 | 0CA | switch | Fault, Gear, HeatTime, LEVEL, MassageTime, ON, State, TEMP, Video |
| `22I7` | 杰诺无线清洗机 | F1 | 000 | mode | AbnormalPrompt, cumulativeTime, electric |
| `22IA` | 洁云无线清洗机 | SW | 000 | mode | AbnormalPrompt, cumulativeTime, electric |
| `22IK` | 格林盈璐灭蚊器GM965TP | GM965TP | 0B0 | switch | Time |
| `22Q4` | 小豚室外摄像机 云台版 | DPH-OP-200 | 008 | switch | alarmEvent, commonExecution1, cruiseSwith, shootSwitch, videoSwitch, visitPoint1 |
| `22S8` | 佳仁按摩椅 | JR-Q8 | 05F | switch | backAction, hot, intenGear, manuMode1, ppmMode, qiya, remainTime |
| `22VM` | 亚摩斯智能立式暖风机 | NS-TC220W | 06A | switch | gear, snaking, timingOff |
| `22VN` | 格林盈璐灭蚊器GM929A | GM929A | 0B0 | switch | Time |
| `22ZO` | 怡可智能保温杯 | LINK-001 | 06B | temperature | blessing, count, drinkwaterhistory, waterclock |
| `22ZY` | Evoyo燃气传感器 | MSG01/M-ZB.10 | 03A | alarm | — |
| `2301` | Evoyo吸顶式人体传感器 | MSPIR01-ZB.10 | 03E | status | — |
| `2305` | 长虹1588浴用加热器-足浴器 | CDN-ZY1588-A | 070 | switch | changeModel, commonFaultDetection, countdown, leftTimeDIY, massage, modelDIY, operateTemperature, temperatureDIY |
| `230Z` | 萨瓦尼智能门H1 | WZ1DDHW01GGMB | 04B | battery | alarmStatu, alarms, events, lockState, lockStatus |
| `23BZ` | 乐尔康全身按摩垫 | LEK-918-7 | 0CA | switch | BackMassage, HotCompress, Mode, NeckMassage, Speed, Timing |
| `23C0` | 乐尔康按摩枕 | LEK-618-9 | 0CA | switch | HotCompress, Mode, Speed, Timing |
| `23C1` | 乐尔康按摩垫 | LEK-918-5 | 0CE | switch | HotCompress, Mode, Speed, Timing |
| `23EH` | 颈椎按摩枕 | R8 | 0CA | switch | hot, pattern, save, torce |
| `23FC` | 亚摩斯智能家具控制器 | AS-DJ01H | 000 | action | — |
| `23R9` | 智能健身折叠单车T1 | TDN5001Z | 0C6 | switch | always, dataBody, kwh, theCal, theKm |
| `23VV` | VOC智能保管箱 | G300 | 08B | battery | event, faultCode, heartbeatTime, keyList, lastActionTime, lockAlarm, lockState, lockStatus, publicKey, remoteCode, remoteInfo, remoteResult |
| `23XE` | 计客超级魔方i2 | SUPERCUBE i2 | 000 | battery | connect, history, intro, rotate |
| `240B` | 奥科智能开合帘电机 | AM68-1.5/100-EM-PW | 01C | action | UseDefaults, resversal |
| `240W` | 单键86底盒开关模块 | BL8001R | 064 | switch | — |
| `241B` | 长虹8558浴用加热器_足浴器 | CDN-ZY8558 | 070 | switch | changeModel, commonFaultDetection, countdown, leftTimeDIY, massage, modelDIY, operateTemperature, temperatureDIY |
| `246O` | 康佳智能筋膜枪F2 | F2 | 0C5 | switch | LEVEL, ReTime, Speed, TIME, value, workstate |
| `247A` | 唱多多小精灵麦克风MINI | F1mini | 0A7 | battery | Connected, Connecting, Electronic, MusicVolume, Mutevoice, Noise, Reverb, Specialeffects, TrebleBass, TrebleBass1, Unconnected, UsageScenarios, VoiceVolume, electricity, snowflake, volume |
| `247H` | 卷发器-罗曼智能小花卷 | HH60 | 000 | switch | commonFaultDetection, rollDegree, workStatus, workTime |
| `2491` | 当贝投影X3 | DBX3 | 098 | switch | controlKey, volume |
| `2493` | 当贝投影X3Pro | DBX3 Pro | 098 | switch | controlKey, volume |
| `24B1` | 直发梳-罗曼智能小青梳 | HH40 | 000 | switch | commonFaultDetection, tempSet, workStatus, workTime |
| `24BT` | 极米投影仪Play X Home | XJ04D | 098 | switch | BACK, DPADCENTER, DPADDOWN, DPADLEFT, DPADRIGHT, DPADUP, FOCUS, FOCUSAUTO, FOCUSLEFT, FOCUSRIGHT, HOME, KPPOWER, MENU, MOVEHOME, POWER, RESTART, VOLUMEDOWN, VOLUMEPRESS, VOLUMEUP |
| `24BU` | 极米投影仪New Z8X | XJ13Q | 098 | switch | BACK, DPADCENTER, DPADDOWN, DPADLEFT, DPADRIGHT, DPADUP, FOCUS, FOCUSAUTO, FOCUSLEFT, FOCUSRIGHT, HOME, KPPOWER, MENU, MOVEHOME, POWER, RESTART, VOLUMEDOWN, VOLUMEPRESS, VOLUMEUP |
| `24BV` | 极米投影仪New Z6X | XH30L | 098 | switch | BACK, DPADCENTER, DPADDOWN, DPADLEFT, DPADRIGHT, DPADUP, FOCUS, FOCUSAUTO, FOCUSLEFT, FOCUSRIGHT, HOME, KPPOWER, MENU, MOVEHOME, POWER, RESTART, VOLUMEDOWN, VOLUMEPRESS, VOLUMEUP |
| `24BZ` | 极米投影仪New Z6 | XL03A | 098 | switch | BACK, DPADCENTER, DPADDOWN, DPADLEFT, DPADRIGHT, DPADUP, FOCUS, FOCUSAUTO, FOCUSLEFT, FOCUSRIGHT, HOME, KPPOWER, MENU, MOVEHOME, POWER, RESTART, VOLUMEDOWN, VOLUMEPRESS, VOLUMEUP |
| `24DJ` | 亚摩斯智能转换插 | ZJ-CZ507H | 01D | switch | — |
| `24H9` | 欢喜滑板车X8 | X8_HOS01 | 094 | switch | Battery, DrivingMode, Lights, Mileage, RealTimeSpeed, ScooterCruise, StartMode, TotalMileage, commonFaultDetection |
| `24HS` | 坚果投影仪J10S | J73-3D1 | 098 | switch | OK, back, down, focusing1, focusing2, home, input, left, menubutton, right, setting, turndown, turnup, up |
| `24HT` | 坚果投影仪G9S | J74-3D1 | 098 | switch | OK, back, down, focusing1, focusing2, home, input, left, menubutton, right, setting, turndown, turnup, up |
| `24J6` | FOOXMET智能温控外套 | ZL-WK-005 | 07C | switch | DeviceState, ZoneATempture, ZoneBTempture, ZoneCTempture, ZoneTemptureSet, commonFaultDetection |
| `24LC` | FOOXMET智能温控裤子 | ZL-WK-007 | 07C | switch | DeviceState, ZoneATempture, ZoneBTempture, ZoneCTempture, ZoneTemptureSet, commonFaultDetection |
| `24M5` | 捷昌智能中岛电机 | JC37A | 000 | status | commonFaultDetection, commonMemoryControl1, ctrl, currentheight |
| `24MT` | 人教畅读智能笔 | RJ-150A | 153 | battery | registerInfo, studyInfo, verifyCode |
| `24MV` | 月球车运动版 | JRKL102 | 158 | switch | AvoidObstacle, Building, ConnectStatus, DoStunt1, DoStunt2, LeftRightWheel, LightColors, ShowBattery, Universe, UpdownWheel, commonFaultDetection |
| `24NE` | 希影智能投影仪H9 | H9 | 098 | switch | arrow, system, volume |
| `24NF` | 希影智能投影仪P8 | P8 | 098 | switch | arrow, system, volume |
| `24O9` | 乐骑智能电动滑板车 | A5 | 094 | mode | Battery, Bluetooth, CurrentAverageVelocity, CurrentSpeed, Cyclingtime, FirmwareUpdate, Mileage1, Mileage2, TotalDistance, connect, function |
| `24QN` | 鼎宏智能按摩椅 | D1L | 05F | switch | Adjustment, Backlift, Footroller, Heating, Lamp, Manualmode, Mode, Pressure, Status, Time, Zerogravity |
| `24RX` | 物生物H-think云想保温杯 | JV012140-0450 | 06B | battery | TDS, alarmTime1, drinkwaterHistory, drinkwaterTarget, find, intake, more, nodisturbance, signed, smartreminds, sterilize, temperatureArea, watertemp |
| `24S5` | 得小烯 烯时代 石墨烯发热无线按摩眼罩 GSee2 | JHK-09AG | 0D0 | status | Heatingswitch, Massageswitch, Realtimetemperature, Remainingtime, UsageRecord, electric, heat, massage |
| `24S7` | 得小烯 烯时代 石墨烯发热无线按摩眼罩 GSee3 | JHK-04AP | 0D0 | status | Heatingswitch, Massageswitch, Realtimetemperature, Remainingtime, UsageRecord, electric, heat, massage |
| `24S9` | 得小烯 烯时代 石墨烯发热无线按摩护颈 GNeck2 | JHC-06AG | 0CE | status | Heatingswitch, Massageswitch, Realtimetemperature, Remainingtime, UsageRecord, electric, heat, massage |
| `24SB` | 得小烯 烯时代 石墨烯发热无线按摩护颈 GNeck3 | JHC-01AP | 0CE | status | Heatingswitch, Massageswitch, Realtimetemperature, Remainingtime, UsageRecord, electric, heat, massage |
| `24X6` | 赋安燃气报警器 | JT-FS3023H | 03A | alarm | commonFaultDetection, concn, remoteOperate, sensorState, volume |
| `24YL` | 全向麦克风 | eMeet Luna | 198 | switch | abnormalPrompt, batteryLevel, denoise, devicePromptTone, micMute, speakerVolume, standbyTime |
| `250I` | Populele智能尤克里里 | Populele 2 | 000 | status | chord, interactive, learning, practice, tuning |
| `251D` | 康佳智能筋膜枪F5 | F5 | 0C5 | switch | LEVEL, ReTime, Speed, TIME, value, workstate |
| `251E` | 康佳智能筋膜枪F3 | F3 | 0C5 | switch | LEVEL, ReTime, Speed, Time, value, workstate |
| `253F` | 奥克斯智能按摩椅 | LS-X5 | 05F | switch | AutoModeSelect, BackLift, BalloonStrength, BodyGasbag, HipGasbag, LegGasbag, Manualmode, MassageIntensity, MassageTime, ModeSelect, ShoulderGasbag, SoleRoller, WaistMuggy, Workstatus |
| `253V` | 康风车载/便携空气净化器 | F3 | 18A | switch | filterElement, lightswitch, windspeed |
| `2562` | 专业会议宝 | OfficeCore M2 Max | 198 | switch | abnormalPrompt, batteryLevel, denoise, devicePromptTone, micMute, speakerVolume, stanbyTime, voiceLight |
| `2570` | 新日电动摩托车GF6 | XR1200DT-5K | 133 | alarm | NFC, OTA, carLock, diagnosis, openSeat, powStatus, remainEle, remainKm |
| `2571` | 新日电动自行车FN3 | TDT9291Z | 0C7 | alarm | NFC, OTA, carLock, diagnosis, openSeat, powStatus, remainEle, remainKm |
| `257L` | 智能会议宝 | OfficeCore M2 | 198 | switch | abnormalPrompt, batteryLevel, denoise, devicePromptTone, micMute, speakerVolume, stanbyTime, voiceLight |
| `2591` | SHOEKONG智能运动包 | SK-SB001 | 143 | switch | ChargeState, GetAllStatus, RemainingCapacity, RingLampBrightness, SetMode, SetUvSate, TaskLeftTime, WorkTime, zipperStatus |
| `259L` | 巢居全新360度取暖器N4 | N4-C3000H | 06A | switch | CHILDLOCK, Currenttemperature, Lightcolor, Lightinducedsleep, Modeselection, purify, timing, voice |
| `25A4` | 巢居全新360度取暖器N3 | N3-C2200H | 06A | switch | CHILDLOCK, Currenttemperature, Lightcolor, Lightinducedsleep, Modeselection, purify, timing, voice |
| `25C7` | 新日电动自行车XC3 | TDT0550Z | 0C7 | alarm | OTA, carLock, diagnosis, powStatus, remainEle, remainKm |
| `25CX` | 折叠足浴器 | ACK-KH21FG | 070 | switch | Comfortable, Healthy, RedLight, Sleep, TargetTemperature, Timing, WarmingFeet, interrupted |
| `25DD` | 富光智联保温杯 | WFZ1202-450 | 06B | battery | charge, lightTime, reminder, tds, temp |
| `25EK` | 冰点光子嫩肤脱毛仪 | HY-TM2108 | 0EE | switch | FlashRecording, Icing, LengthDepilation, Outgoing, depilationMode, directionUse, gears |
| `25ER` | listeneer倾听者M3 | M3 | 27A | battery | Status, file, filemeta, link, list, plan, summary |
| `25HA` | 德沃福无线清洗机 | DWF-B | 000 | mode | AbnormalPrompt, cumulativeTime, electric |
| `25HQ` | 九阳智能商务保温杯 | B45V-WR955 | 06B | battery | charge, find, lightTime, reminder, tds, temp |
| `25IP` | Helmetphone智能头盔 | BH51M Neo | 0EF | switch | Down, Light, NewSong, Play, TimingOff, Up, VA, bat, led, prev, right, turn |
| `25K2` | 远程辅导机LHW02-C3 | LHW02-C3 | 046 | switch | homework, register, reminder, rssi |
| `25KG` | 思麦耳降噪会议麦克风音箱 | AIMIC-M4 | 198 | switch | battery1, mute, volume |
| `25KW` | 虎牌保险箱 | HP-HW30 | 165 | switch | alarms, batter, events, lockState, lockStatus |
| `25NF` | VSITOO轻巧抑菌智能保温杯 青春版 | C3 | 06B | battery | charge, lightTime, reminder, tds, temp |
| `25NR` | 希诺智能保温杯 | XN-7602 | 06B | status | FirmwareUpdate, remind, watertemperature |
| `25ON` | 天博智-智点点T90 | T90 | 0AF | switch | DeviceContro0012, DeviceContro0013, DeviceControl0010, DeviceControl0011, DeviceState0006, DeviceState0008, DeviceState0009, DeviceWiFiSet0013 |
| `25PN` | 皇家惠人智能水暖毯 | HRS53 | 000 | switch | commonFaultDetection, commonMode1, display, temperatureCTRL, timeCTRL |
| `25R1` | 小豚当家室外摄像头 | DPH-OP-100 | 008 | switch | alarmEvent, cruiseSwith, pushStatus, shootSwitch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6, voip |
| `25UP` | 青稞智能锁N5C | N5C | 04B | battery | event, faultCode, heartBeat, keyList, lastActionTime, lockAlarm, lockMode, lockState, prePowerSwitch, publicKey, remoteCode, remoteInfo, remoteResult, userList |
| `25US` | 音络全向麦克风 | BT-31 | 198 | switch | BatteryStatus, mute, voiceminus, voiceplus |
| `264A` | 飞利浦会议麦克风PSE0500 | PSE0500 | 198 | switch | ConnectionStatus, Instructionsforuse, Volumeadjustment, micMode |
| `264B` | 飞利浦会议麦克风PSE0540Pro | PSE0540Pro | 198 | switch | ConnectionStatus, Electricity, Instruction, Volumeadjustment, micMode |
| `264R` | 爱贝丽智能童车 | I-S037 | 17B | status | Statistics, Trackdetails, Travelrecord, WiFi, electricity, firmwareUP |
| `26H0` | 创维智能足浴盆 | GY-E602 | 070 | switch | CurrentTemperature, DeviceStatus, Massage, RemainingDuration, TargetTemp, Timing |
| `26JA` | 虎牌酷博保险箱 | HP-HC01 | 165 | battery | alarms, events, lockState, lockStatus |
| `26LT` | 卡唛电子指纹智能保管箱 | BGX-X1-30HW | 08B | battery | FP, PW, SetTime, chipid, doorStatus, historyrecord, openMode |
| `26S6` | 金卡智能燃气报警器 | JT-JBY4 | 03A | status | Gasvalue, Valveswitch, commonFault, meterconnect, mute, sensitivity, testresult |
| `26U0` | 酷轻松石墨烯腰带 | PMA-I30 | 0CA | switch | Message, Mode, Remind, backRealTemperature, bakeLevel, frontLevel, frontRealTemperature, timerlabel, workstate |
| `27GC` | 哈鹰H10 | H10 | 094 | switch | Battery, Cruise, Headlight, Mileage, Mileagetotal, Speed, Zerostart, commonFaultDetection, commonMode1 |
| `27UW` | 外研通智能扫读笔 | VT-S30 | 153 | battery | registerInfo, studyInfo, verifyCode |
| `27XR` | 紫外杀菌灯 | HJ-1701 | 110 | switch | childlock, uvtimeleft, uvtimemode, workstatus |
| `27ZQ` | 食具消毒柜 | ZTP35-A | 0D5 | switch | Auto, Lefttime, Worktime, cabinetMode, cabinetStatus |
| `280A` | 小益H7智能门锁 | H7 | 04B | alarm | BatteryA, DeleteOperation, GetKeyInfo, KeyListA, NFCencryption, PwdOperationRes, UserOperation, VerfiyMode, Volume, faultCode, lockState, openEvent |
| `283L` | 品多智能锁H2 | H2 | 04B | battery | erroralarm, event, keyList, lockAlarm, lockMode, lockState, prvdooralarm, publicKey, remoteCode, remoteInfo, remoteResult, upgradeMode |
| `283T` | FSL智能插座 | Z1-Z3B-101/Q | 01D | switch | — |
| `287W` | Sway N Fit摇摆健身机 | SWF-05-TR-02 | 0C9 | switch | Calories, InstallationVideo, PrivacyAgreement, TutorialVideo, data, exerciseDuration, music, profile, workouts |
| `289K` | 皇鼎智能门锁VE06W | VE06W | 04B | alarm | BatteryLevel, UserList, faultCode, lockMode, lockState, lockStatus, openEvent |
| `28A6` | 720冰箱除味器智联版 | RC100s | 1A1 | battery | connectstate, moreset, workmode |
| `28AH` | 智能颈枕按摩器 | uNeck-9825 | 0CA | switch | gear, leftTime, model, power, tempSwitch, voiceSwitch |
| `28E9` | 凯丰电子厨房秤 | KFS-E11 | 227 | switch | tare, unit |
| `28FA` | 凯丰电子厨房秤 | KFS-X10 | 227 | switch | tare, unit |
| `28RD` | 名豆之约通断器 | TDQ007 | 005 | switch | — |
| `28SX` | 小K士智能猫眼门锁 | 767 | 04B | battery | code1, code2, code3, code4, code5, event, imagePack0, imagePack1, imagePack2, imagePack3, imagePack4, imagePack5, keyList, lockAlarm, lockMode, lockState, publicKey, remoteCode, remoteInfo, remoteResult, upgradeMode |
| `28T5` | 小K士智能门锁 | 727 | 04B | battery | code1, code2, code3, code4, event, keyList, lockAlarm, lockMode, lockState, publicKey, remoteCode, remoteInfo, remoteResult, upgradeMode |
| `28TR` | OES按摩椅 | 656 | 05F | switch1 | automaticAirPressure, automaticMassage, backrest, devState, fixedPoint, heat, manualAirPressure, manualMassage, part, position, powerRating, scrollWheel, speed, width, zeroGravity |
| `28UA` | 得途 烯时代 石墨烯发热无线按摩眼罩 GSee2 | JHK-07AG | 0D0 | switch | DeviceStatus, MassageMode, Mode, Power, Record, Remind, RemindWindow, SetTemperature, SetTimer, Temperature, Timer |
| `28UD` | 得途 烯时代 石墨烯发热无线按摩护颈GNeck2 | JHC-04AG | 0CE | switch | DeviceStatus, MassageMode, Mode, Power, Record, Remind, RemindWindow, SetTemperature, SetTimer, Temperature, Timer |
| `28UF` | 得途 烯时代 石墨烯发热无线按摩眼罩 GSee3 | JHK-11AP | 0D0 | switch | DeviceStatus, MassageMode, Mode, Power, Record, Remind, RemindWindow, SetTemperature, SetTimer, Temperature, Timer |
| `28UG` | 得途 烯时代 石墨烯发热无线按摩护颈GNeck3 | JHC-08AP | 0CE | switch | DeviceStatus, MassageMode, Mode, Power, Record, Remind, RemindWindow, SetTemperature, SetTimer, Temperature, Timer |
| `28UT` | 精臣标签打印机D110 | NIIMBOT D110 | 1B1 | switch | PrintableCounts, PrintedCounts, alignment, connection, copies, effect, faultDetection, instructions, mall, offset, preview, print, printParameter, printerStatus, rfid, textfield |
| `28VG` | 电动滑板车G1 | 5LCHG01 | 094 | switch | AlarmInformation, ConnectionStatus, FirmwareUpdate, Gears, OurProducts, PrivacyAgreement, ProductInformation, RestoreFactorySettings, backlitSettings, cruiseControl, currentSpeed, electricquantity, headlight, singleMileage, speedUnit, totalMileage |
| `28VP` | 柯璐斯雾化加湿器 | HF-1000 | 052 | alarm | BS, DS, JS, LD, TS, WH, WL, WS |
| `28XS` | 佳普乐G3-400A自动翻盖智能马桶 | G3-400A | 066 | mode | ECO, cover, dryGear, drySwitch, flush, heatGear, hip2intensity, hipnozzlePosition, nightled, seat, sitdown, smart, waterTemp, woman2intensity, womannozzlePosition |
| `28Z2` | 联邦米尼智能按摩单椅 | IHM | 128 | switch | Airbagmassage, HeatingMode, Home, Seatposition, angleControl, faultDetection, messagetimecountdown, monitorednobody |
| `2900` | 觅泛QM23迷你筋膜枪 | QM23 | 0C5 | battery | battalarm, chargstat, devicestat, gear, usetime |
| `290K` | MT1 Neo 智能骑行头盔 | MT1 Neo | 0EF | switch | Autooff, autoon, bat, led, right, turn |
| `2934` | 大一指纹保管箱 | BGX45 | 165 | battery | event, lockAlarm, lockState, rmRes |
| `2957` | 万象智能数显保温杯 | HVC2227-430 | 06B | temperature | Battery, Moresettings, Regularreminder, Temperatureunit, frequency, homepage, interval, lookup, lowbattterywarning, state, temperaturerange |
| `295A` | UKA智能保温杯 | UKM21 | 06B | temperature | Customtea, Electricity, GreenTea, Lowtemperature, WaterTime, blacktea, doubleclick, lowpower, scentedtea, state |
| `296Z` | 施罗兰智能电动床 | s-99 | 14A | lightSwitch | MassageFrequency, headControl, headMassage, legControl, legMassage, massageTimer, modeSelect |
| `2982` | 名豆之约智能插座10A | ZCZ001 | 01D | switch | electricity, powerElectricity, protect, protectTimer |
| `2983` | 名豆之约智能插座16A | HPS001 | 01D | switch | electricity, powerElectricity |
| `298C` | 艾力斯特按摩椅R2S | R2S | 05F | switch | Auto, Bluetooth, Collector, Intensity3D, Manual, Other, Recommend, Shoulder, SitAdjustment, State, Timing, VoiceControl, nID |
| `298K` | 联邦米尼智能温灸单椅 | IH | 128 | switch | BackDown, BackUp, HeatingMode, Home, Seatabnormal, angleControl, faultDetection, monitorednobody |
| `2999` | 5G通信壳 | Dorado | 228 | switch | — |
| `299C` | VOC猫眼可视门锁 | T11i | 04B | battery | code1, code2, code3, code4, code5, event, imagePack0, imagePack1, imagePack2, imagePack3, imagePack4, imagePack5, keyList, lockAlarm, lockMode, lockState, publicKey, remoteCode, remoteInfo, remoteResult, upgradeMode |
| `29BA` | 舍见智能插座 | SJ-CZ1051H | 01D | switch | — |
| `29BZ` | S1智慧出行头盔 | S1 | 134 | switch | Autooff, LED, Light, TrackAlarm, VoiceControl, autoon, bat |
| `29CV` | BH60SE Neo智能骑行头盔 | BH60SE Neo | 0EF | switch | Autooff, autoon, bat, led, right, turn |
| `29DY` | 飞科智能剃须刀FS892 | FS892 | 170 | status | Class, Lifespan, Records, Remaining, Upgrade, Using, connect |
| `29E9` | 海德 FG309HW 热敷筋膜枪 | FG309 | 0C5 | switch | electricity, gearL, heat, mytimer, running, speed |
| `29LH` | HUAWEI Mate50 Pro 环闪保护壳 | DRACO-RC | 228 | brightness | colorTemperature, control, firmwareUpgrade, sceneLightEffect, specialSet, workStatus |
| `29LI` | HUAWEI Mate50 环闪保护壳 | CETUS-RC | 228 | brightness | colorTemperature, control, firmwareUpgrade, sceneLightEffect, specialSet, workStatus |
| `29M4` | 未来侍酒师智能品酒礼盒套装 | TFS-001 | 22F | status | commonFilterElement1, commonFilterElement2, faultDetection, power, resettime |
| `29MD` | 智能饮水机 | YTL-Vhm | 06F | temperature | ChildLock, TapOn, currentTemp, daypower, daywater, faultDetection, orderwater, output, workstatus |
| `29Q4` | POSO场景面板 | PMK-V3H-3 | 075 | switch | scene1, scene2, scene3, scene4, scene5, scene6 |
| `29SM` | 智能电动水阀 | BL5020R | 209 | switch | faultDetection, rotation |
| `29T9` | 智能电动水阀 | BL5021R | 209 | switch | faultDetection, rotation |
| `29TS` | 万达康智能哑铃 | LYY-015R | 0C2 | battery | devicestatus, eqweight, otaupdate, paraset, sportdata, sportmode, userdata |
| `29UZ` | 九牧智能浴霸 | JD172 | 035 | temperature | Switch, commonFaultDetection, control |
| `29XA` | 欧井智能除湿机OJ-128E | OJ-128E | 09B | switch | Countdown, HUM, SetDUM, SetMode, Temp, commonFaultDetection |
| `29XD` | 欧井智能除湿机OJ-550EP | OJ-550EP | 09B | switch | Countdown, HUM, Purify, SetDUM, SetMode, SetSpeed, Temp, commonFaultDetection |
| `29YN` | VOC猫眼可视门锁T6i | T6i | 04B | battery | errorCode, event, keyList, lockAlarm, lockMode, lockState, publicKey, remoteCode, remoteInfo, remoteResult, upgradeMode, userlist |
| `29Z4` | P40proXM自动翻盖智能坐便器 | ZMT-P040proXM | 066 | switch | CustomFunction, FaultAlarm, FlipFunction, Move, WashMode, dryGear, heatGear, intensity, nozzlePosition, seatstatus, waterTemp |
| `29ZA` | P40proXL自动翻盖智能坐便器 | ZMT-P040proXL | 066 | switch | CustomFunction, FaultAlarm, FlipFunction, Move, WashMode, dryGear, heatGear, intensity, nozzlePosition, seatstatus, waterTemp |
| `2A07` | 艾特智能网关 | ZG100 | 020 | switch | discovery |
| `2A1U` | 凯胜颈椎按摩器 | N1 | 0CE | switch | Acupuncturemodel, Againstthpattern, DIY, Hotcompress, Methodsthelength, Scrappingmode, automaticmode, currentpower, gear, hottemperature, methods, resttime |
| `2A8S` | sraum1路开关面板 | SP-A1Z5-RaF | 005 | switch | scene1, scene2, scene3, scene4 |
| `2A8U` | 三星SHP-P60 | SHP-P60 | 04B | alarm | doorState, event, faultCode, lockMode |
| `2AAJ` | 艾特单键开关 | ZS112 | 005 | switch1 | — |
| `2AAY` | VSITOO不锈钢智能保温杯 | VSITOO T1 Pro | 06B | battery | TDS, charge, lightTime, reminder, temp |
| `2AB2` | 青稞智能锁_A7H | A7H | 04B | battery | event, faultCode, heartBeat, keyList, lastActionTime, lockAlarm, lockMode, lockState, prePowerSwitch, publicKey, remoteCode, remoteResult, userList |
| `2AB7` | 0压智能枕 | MLP-WBP-G2 | 054 | status | bodyMove, electric, heartRate, privacy, respiratoryRate, shake |
| `2ACX` | 百叶帘 | VHP24GF | 0B5 | action | openerAngle |
| `2AD1` | 自清洁无线擦地吸尘器 ONE X | QYXCQ05W | 069 | status | batterylevel, calorie, cleanarea, cleanmark, commonFaultDetection, commonFilterElement1, commonFilterElement2, powersetting, screenbright, screenctrl, worktime |
| `2ADE` | VSITOO智能商务保温杯 | VSITOO V1 | 06B | battery | alarmTime1, charge, lightTime, tds, temp |
| `2ADR` | 酷轻松石墨烯智能睡眠枕 | K-ZMZ-B2V2 | 054 | status | Body, InterferenceSwitch, Internet, Power, Rate, Respiratory, SleepReport, Strength, heat, statue |
| `2AE7` |  | KK-FC-D21W | 03F | battery | pushButton |
| `2AED` |  | KK-TQ-J01W | 075 | battery | button1, button2, button3, button4 |
| `2AK0` | 艾特燃气报警器 | AT200 | 03A | alarm | — |
| `2AK2` | 艾特门磁传感器 | AT300 | 018 | status | doorEvent |
| `2AK4` | 艾特人体红外传感器 | AT400 | 03E | status | — |
| `2AK5` | 艾特插座 | ZST10 | 01D | switch | — |
| `2AK6` | 艾特窗帘控制器 | ZC112 | 01C | mode | — |
| `2AK9` | 全创拉力绳 | SR100 | 000 | switch | calorie, durationTime, exerciseCount, heartRate, personInfo, sportInfo |
| `2AKA` | 全创蝴蝶绳 | SS100 | 000 | switch | calorie, durationTime, exerciseCount, heartRate, personInfo, sportInfo |
| `2AKB` | 全创健腹轮 | SW100 | 000 | switch | calorie, durationTime, exerciseCount, heartRate, personInfo, sportInfo |
| `2AKC` | 全创跳绳 | SJ100 | 000 | switch | calorie, durationTime, exerciseCount, heartRate, personInfo |
| `2AKD` | 全创哑铃 | SY100 | 000 | switch | calorie, durationTime, exerciseCount, heartRate, personInfo, sportInfo |
| `2ALB` | 飞利浦反渗透净水机-AUT2016 | AUT2016 | 02D | status | FilterReset1, FilterReset2, ResetRecord0, ResetRecord1, Rinsefunction, faultDetection, filterElement1, filterElement2, outputTds |
| `2AN8` | 鸿雁门窗传感器B款 | IHG5201HW | 018 | status | doorEvent |
| `2ANZ` | 领普单键单火开关MESH | Q4S-BLE-W1(HW) | 005 | switch | button1, mode1 |
| `2AO8` | 鸿雁智能主机III型 | IHA1221HW | 020 | switch | devOta |
| `2AOC` | 奥佳华7306 | OG7306 | 05F | switch | AirPressure, Intensity, KnockingSpeed, MovementWidth, Vibration, ZeroGravity, backAction, classic, exclusive, heatMode, legAction, manuMode, massGear, on, ppmMode, roller |
| `2AOZ` | 鸿雁单路智能开关模块 | IHC1238HW | 064 | switch | indicator |
| `2AP1` | 鸿雁单键智能开关U2 | U2-86K11ND10-ZD(HW) | 005 | switch1 | indicator |
| `2ARO` | Sleepace享睡RestOn智能睡眠监测器 | Z400TWP | 05D | status | environment, features, historyData, realData, smartscene, tur, workStatus |
| `2AS7` | 锐亿理发器 | RC550 | 000 | switch | — |
| `2AT0` | 倍轻松眼部按摩器 | iSee H | 05F | switch | awakemode, cyclemode, diastolicmode, eyesightmode, firmware, hot, music, sleepmode, timing, workmode |
| `2ATT` |  | MB9871H | 01D | switch | — |
| `2AUJ` | 嘟嘟智能插座 | DD-SC | 01D | switch | TotalPower, backlight, electric, power |
| `2AWD` | 飞利浦反渗透净水机-AUT2116 | AUT2116 | 02D | status | FilterReset1, FilterReset2, ResetRecord0, ResetRecord1, Rinsefunction, faultDetection, filterElement1, filterElement2, outputTds |
| `2AWE` | 飞利浦反渗透净水机-AUT3016 | AUT3016 | 02D | status | FilterReset1, FilterReset2, ResetRecord0, ResetRecord1, Rinsefunction, faultDetection, filterElement1, filterElement2, outputTds |
| `2AWF` | 飞利浦反渗透净水机-AUT3116 | AUT3116 | 02D | status | FilterReset1, FilterReset2, ResetRecord0, ResetRecord1, Rinsefunction, faultDetection, filterElement1, filterElement2, outputTds |
| `2AWL` | 锐亿剃须刀 | RS375 | 000 | switch | currentcapacity, frequency, function, implemented, record, state |
| `2B3F` | 天博智-科学队长3 | T838 | 000 | switch | DeviceContol000107, DeviceControl000106, DeviceControl000108, DeviceControl000109, DeviceControl110, DeviceState0000104, DeviceState000103, DeviceState000105, DeviceState102 |
| `2B49` | 探梦者智能电动滑板车 | L1 MAX | 094 | switch | — |
| `2B4N` | 倍轻松空气按摩颈枕 | iNeck H | 05F | switch | activatingmode, firmware, hotswitch, neckmode, necksmode, nourishingmode, siestamode, timing, travelmode |
| `2B58` | MixSwitch超级智能开关-一开 | T40W1Z | 005 | switch | — |
| `2B5B` | MixSwitch超级智能情景开关 | T40S6Z | 075 | battery | — |
| `2B5N` | 智能药盒 | PB1 | 000 | switch | — |
| `2B6J` | 长虹足浴盆 | CDN-ZY8808 | 070 | switch | — |
| `2B6R` | KUS筋膜枪 | PRO8 | 0C5 | switch | — |
| `2B7W` | 百普瑞智能便携电热水壶 | WM40 | 06B | switch | Targettemperature, state, watertemperature |
| `2B92` | 凯胜眼部按摩器 | A3 | 000 | switch | — |
| `2BB1` | 凯迪仕智能锁HK300 main | HK300 | 04B | battery | event, faultCode, keyList, lastActionTime, lockAlarm, lockMode, lockState, publicKey, remoteCode, remoteResult |
| `2BCC` | 荣泰按摩椅 | A60Hilink | 05F | switch | autoMode, backDown, backUp, heatMode, legDown, legUp, manuMode, massGear, soleSwitch, zero |
| `2BDX` | OOYEE高速无叶吹风机 | X2H | 000 | temperature | commonMemorySwitch1, windspeed |
| `2BGF` | 欧普蓝牙MESH面板-双键 | Z0766E2B2-H3 | 075 | battery | — |
| `2BGG` | 欧普蓝牙MESH面板-四键 | Z0766E4B2-H3 | 075 | battery | — |
| `2BO5` | 堡丽触点开关 | BL7201H | 2BO5 | switch | — |
| `2BO6` | 堡丽开关卷帘 | BL7201H | 0B5 | action | — |
| `2BO7` |  | BL2007H | 064 | switch | — |
| `2BO9` | 堡丽开关灯（底盒开关控制器） | BL2001H | 064 | switch | — |
| `2BOO` | 堡丽人体存在传感器 | BL5002H | 03E | status | — |
| `2BOQ` | 堡丽人体移动传感器 | BL5001H | 03E | status | — |
| `2BOV` |  | BL8010H | 064 | switch | — |
| `2BP9` | 德施曼人脸识别智能锁RH700 | RH700 | 04B | battery | event, faultCode, keyList, lastActionTime, lockAlarm, lockMode, lockState, publicKey, remoteCode, remoteEnable, remoteResult |
| `2BPG` | 318智能运动头盔 | SH30 | 0C2 | switch | breakSwitch, goMode, helmetBattery, keyBattery, ledLevel, testMode, thisTime, totalTime, turnMode |
| `2BRA` | 阳光照明智能杀菌灯 | YGS-UV0211-3W | 01B | switch | bat, state |
| `2BRC` | 瑞莱克斯按摩椅 | RE-H615 | 05F | switch | ARMS, AirBag, FOOTREST, Heat, Intensity, Intervalselection, PositionAdjustment, ROLLERS, SHOULDER, Speed, Width, ZeroG, autoMode, commonFaultDetection, manuMode |
| `2BRM` | 奥佳华颈椎按摩仪 | OG2606 | 000 | switch | classic, heat, strength, surTime, suspend, voice |
| `2BSN` | 水母云炫昼智能插座夜灯 | JLTNLP01 | 01D | switch | NightLightBrightness, NightLightSwitch, backlight, consumption, faultDetection, memorySwitch, power |
| `2BV9` | 乐骑智能儿童滑板车 | M1 | 000 | switch | commonExecution1, statistic |
| `2BVW` | 关阀门机械手套装 | BL5053R | 05C | switch | — |
| `2BWA` | tinyho按摩筋膜枪RELAX | T625 | 0C5 | switch | — |
| `2BX8` | 飞利浦智能锁DDL603E | DDL603E-5HWL | 04B | battery | event, faultCode, keyList, lastActionTime, lockAlarm, lockMode, lockState, publicKey, remoteCode, remoteResult |
| `2C4Z` | MBH ST跑步机 | ST | 08F | switch | dist, incline, kcal, speed |
| `2C5O` | 堡丽百叶帘 | BVHP24GF | 0B5 | action | openerAngle |
| `2C65` | 左点智能膝部按摩器 | ZD-XG9 | 0CA | switch | hot, lowbattery, massage, shake |
| `2C75` | FSL智能插座 | Z1-Z3B-101/HW | 01D | switch | — |
| `2C7U` | 西蒙一位智能开关 | 70E838 | 005 | switch1 | BackLightMode |
| `2C82` | 西蒙10A智能插座 | 70E830 | 01D | switch | BackLightMode, electric, faultDetection, power |
| `2C84` | 西蒙一位智能调光开关 | 70E848 | 044 | switch1 | BackLightMode, LedPosition |
| `2C91` | 觅泛MINi筋膜枪 | QM20 | 0C5 | battery | Gear, Usetime, Workingstatus |
| `2C97` | 锐亿剃须刀 | RS303 | 000 | switch | — |
| `2CDJ` | ACEMATIC窗帘电机 | WSCMT-2/12 | 01C | mode | — |
| `2CJW` | 叶绿体一键情景面板 | SWS-XA01-ZB | 075 | battery | — |
| `2CJX` | 叶绿体二键情景面板 | SWS-XA02-ZB | 075 | battery | — |
| `2CJY` | 叶绿体三键情景面板 | SWS-XA03-ZB | 075 | battery | — |
| `2CJZ` | 叶绿体单火一路墙壁开关 | SWL-XA01-ZB | 005 | switch1 | — |
| `2CM5` | 斯波阿斯儿童篮球机 | K2001（Demi） | 0C2 | switch | pinglv, sudu |
| `2CMV` | 坚果G9 | J74-3D0 | 098 | switch | OK, back, down, focusing1, focusing2, home, input, left, menubutton, right, setting, turndown, turnup, up |
| `2CN1` | 英尔健筋膜枪 | 67J | 0C5 | switch | — |
| `2COA` | 智能蒸汽眼罩 | ECP-02 | 08C | switch | — |
| `2COX` | 坚果投影仪J10 | J73-3D0 | 098 | switch | OK, back, down, focusing1, focusing2, home, input, left, menubutton, right, setting, turndown, turnup, up |
| `2CP9` | 仁豪家居电动巴士门 | BG-8109 | 068 | brightness | autoClosed, doorstatus, massageMode, midJoinOpen, midLeftOpen, midRightOpen, oneKeyReset, openDirection, openTimes, sideJoinOpen, sideLeftOpen, sideRightOpen |
| `2CTK` | VOC智能门锁X20 | X20 | 04B | battery | event, faultCode, keyList, lastActionTime, lockAlarm, lockMode, lockState, publicKey, remoteCode, remoteResult |
| `2CTL` | VOC智能门锁X11 | X6 | 04B | battery | event, faultCode, keyList, lastActionTime, lockAlarm, lockMode, lockState, publicKey, remoteCode, remoteResult |
| `2CUG` | 喜临门智能健康枕 | GNZ-J1 | 054 | status | batteryInfo, commonFaultDetection, devInfo, devVersion, historyData, realData, updateSelf, workStatus |
| `2CUR` | 麦乐克燃气泄漏传感器 | MIR-GA100 | 03A | alarm | commonFaultDetection |
| `2CUS` | 麦乐克紧急按钮传感器 | MIR-SO100 | 03F | battery | pushButton |
| `2CUT` | 智能矫姿精灵 | P1 | 000 | switch | — |
| `2CUZ` | 吸顶式燃气传感器套装 | BL5013R | 03A | alarm | — |
| `2CV0` | 吸顶式烟雾传感器套装 | BL5010R | 039 | alarm | — |
| `2CVF` | 单键智能开关面板时尚版 | BL8031R | 064 | switch | — |
| `2CVY` | 南方家居智能护颈枕 | HP100 | 054 | status | — |
| `2CXO` | 路福梦享家 | PROV | 068 | lightSwitch | amdjs, czjyw, headControl, headLegControl, jbxw, legControl, lieControl, massage, massageMode1, memoryControl1, memoryControl2, memoryControl3, memoryControl4, mszt, nzjs, tbxw |
| `2CXR` | VANOW智能水杯 | VO-HA01 | 06B | temperature | alarmTime1, drinkStatus, lastTime, wish |
| `2CYN` | 华为智选 VOC智能门锁S | SHEP-SL0-VC1S | 04B | battery | event, faultCode, keyList, keyOperate, lastActionTime, lockAlarm, lockMode, lockState, publicKey, remoteCode, remoteInfo, remoteResult |
| `2CYO` | 摩摩哒智能按摩椅M635 | M635 | 05F | switch | airIntensity, autoMode, backDown, backUp, heat, manuMode, massGear, movementDown, movementUP, position, ppmMode, range, rollerMode, rollerSpeed, timing, zeroGravity |
| `2CYR` | SID超人智能门锁 | L5 | 04B | alarm | event, faultCode, lockState, lockStatus |
| `2CZA` | MBH T跑步机 | LTFT | 08F | switch | dist, kcal, speed |
| `2D4Z` | 360儿童安全座椅 | T705 | 000 | switch | deng, feng, gequ, yin |
| `2D53` | 精油温灸仪 | TS-001 | 0C3 | switch | BAT, EMS, HOT, oil, temp |
| `2D56` | 亿健智能筋膜枪 | JM6 | 0C5 | switch | — |
| `2D5Y` | 锐亿剃须刀373 | RS373 | 000 | switch | Currentcapacity, Time, frequency, function, record, state |
| `2D6C` | 画法几何两栖生态懒人鱼缸Pro | C180 | 000 | switch | common, feed, light, pump |
| `2D7W` | 三思杀菌台灯 | C21SJ-TD04 | 046 | switch | ChildLock, SterilizationTime |
| `2D9M` | 一维生活功夫椅 | EW-917H | 05F | switch | KneadAndRoll, ManualMode, MassageArea, Pause, PositionAdjustment, airIntensity, airMode, autoMode, heat, intensity |
| `2DA4` | VOC智能门锁X6 | X6 | 04B | battery | event, faultCode, keyList, lastActionTime, lockAlarm, lockMode, lockState, publicKey, remoteCode, remoteResult |
| `2DAD` | 名豆之约10A智能插座 | ZCZ007 | 01D | switch | ElectricalProtect, chargingProtect, electricity, faultDetection, realPower |
| `2DAE` | 名豆之约16A智能插座 | HPS007 | 01D | switch | electricity, faultDetection, realPower |
| `2DC2` | 婴觅智能杀菌牙刷杯架 | YM01 | 000 | battery | disinfect, disinfectStatus, record, timing, warning |
| `2DD4` | 远程智能陪读机 | AR-Online-01 | 046 | switch | homework, register, reminder, rssi |
| `2DDA` | 荣泰筋膜枪G31 | G31HiLink | 0C5 | mode | Battery, RPM, TIME, operation, swtih |
| `2DDU` | 木有故事-小鸟智能灯 | MUYGS Bird | 046 | switch | bright, color, commonMode1 |
| `2DDV` | 即眠睡眠仪 1s PRO | 1s PRO | 08C | switch | F002, F003, F004, F005, commonExecution1, commonExecution2, commonExecution3 |
| `2DDZ` | 外研通智能笔 | VT-S30 | 0AF | battery | registerInfo, studyInfo, verifyCode |
| `2DE0` | Gimbal Pro-L7C-Pro | L7Cpro | 000 | switch | — |
| `2DE5` | 小恬次氯酸钠发生器 | XT-1.3 | 000 | switch | workInfo |
| `2DEX` | 壁挂式声光报警器套装 | BL5052R | 040 | switch | — |
| `2DF1` | DB913筋膜枪 | DB-913 | 0C5 | switch | CountDown, LifeTimer, Power, UseTutorial, commonFaultDetection, dataStatistics, gear |
| `2DF9` | 艾诗摩尔润眼按摩仪 | AS-RY02 | 000 | mode | commonFaultDetection, commonFilterElement1, commonFilterElement2, electricity, heat, spray |
| `2DFA` | 艾诗摩尔便携式洗手仪 | AS-XS02 | 000 | mode | commonFaultDetection, commonFilterElement1, power, record, workMode |
| `2DFT` | 便携智能剃须刀 | DT-W201 | 000 | switch | Cleantip, Cuttingheadwhen, Morefunctions, Shavingspeed, Shavingtime, Usingtherecord, electricity, recommended, tip |
| `2DGH` | 极米投影仪H3 | XK03E | 098 | switch | BACK, DPADCENTER, DPADDOWN, DPADLEFT, DPADRIGHT, DPADUP, FOCUS, FOCUSAUTO, FOCUSLEFT, FOCUSRIGHT, HOME, KPPOWER, MENU, MOVEHOME, POWER, RESTART, VOLUMEDOWN, VOLUMEPRESS, VOLUMEUP |
| `2DGU` | 梦洁睡眠监测枕 | HP100-8 | 054 | battery | — |
| `2DNV` | 维尔森香薰助眠枕 | VE-A02B | 054 | status | — |
| `2DPY` | 艾诗摩尔健发梳 | AS-SF01 | 000 | mode | EMS, Status, UsageRecord, clear, days, power |
| `2DQM` | MOK PLANET智能音乐伴眠枕 | P401M | 054 | status | aidmusic, alarmCfg, batteryInfo, features, historyData, realData, smartBt, tur, updateSelf, workStatus |
| `2DRC` | 汇优尚品射频美容仪 | AX-M5.0 | 000 | mode | Instructions, gear, remainTime, switchStatus |
| `2DRL` | 计客超级魔方i3 | SUPERCUBE i3 | 000 | battery | history, intro, rotate |
| `2DS0` | MOK PLANET智能健康枕 | P102T | 054 | status | batteryInfo, features, historyData, realData, tur, workStatus |
| `2DU1` | 不锈钢真空保温杯 | BMG6001 | 06B | temperature | Currenttemperature, alarmTime1, count, loss |
| `2DU6` | 呼噜圈智能喉部脉冲止鼾器 | YA4100 | 05D | battery | Connected, Sensitivity, SleepReport, interference |
| `2DUZ` | 单键智能开关面板尊享版 | BL8371R | 064 | switch | — |
| `2DWQ` | 唱多多小雪人麦克风 | CD-1 | 0A7 | battery | Electronic, MusicVolume, Mutevoice, Noise, Reverb, Specialeffects, TrebleBass, TrebleBass1, UsageScenarios, VoiceVolume, electricity, snowflake, volume |
| `2DYZ` | 美森剃须理容套装 | WHM3P | 000 | switch | F005, F006, commonExecution1, commonFilterElement1, commonTask1, f001, f007, f010 |
| `2DZ1` | 美森电动手刮刀 | WHT6 | 000 | switch | F001, F003, commonExecution1, commonMode1, f008 |
| `2E0K` | BMC呼吸机 | M1 Mini | 08C | switch | AHI, AI, AVGPressure, AvgLeak, CAI, HI, Leak95, LeakTime, Pressure95, TreatPressure |
| `2E1I` | VANOW智能玻璃杯 | VO-HA02 | 06B | temperature | alarmTime1, drinkStatus, drinkwaterHistory, lastTime, wish |
| `2E1J` | VANOW智能泡茶玻璃杯 | VO-HB02 | 06B | temperature | alarmTime1, drinkStatus, drinkwaterHistory, lastTime, wish |
| `2E1K` | VANOW智能泡茶杯 | VO-HB01 | 06B | temperature | alarmTime1, drinkStatus, drinkwaterHistory, lastTime, wish |
| `2E3A` | 长虹8519浴用加热器-足浴器 | CDN-ZY8519 | 070 | switch | commonFaultDetection, countdown, leftTimeDIY, massage, operateTemperature, temperatureDIY |
| `2E3B` | 长虹968足浴盆 | CH-968 | 070 | switch | changeModel, commonFaultDetection, countdown, leftTimeDIY, massage, modelDIY, operateTemperature, temperatureDIY |
| `2E3W` | 芝华仕按摩椅 | M1042 | 05F | switch | adjstatus, autoMode, back, ble, cancle, intensity, leg, manuMode, movement, position, ppm, range, roller, shank, shoulder, sitting, speed, timing, voice |
| `2EJ1` | VANOW茶水分离智能杯 | VO-HC01 | 06B | temperature | alarmTime1, drinkStatus, drinkwaterHistory, lastTime, wish |
| `2EJ8` | 罗曼智能电动冲牙器-HS10 | HS10 | 000 | mode | betteryleft, commonFaultDetection, initPosition, moreSet, realTimeGuide, strength, workStatus, workTime |
| `2EJA` | 罗曼智能电动冲牙器-HS8 | HS8 | 000 | mode | batteryLeft, commonFaultDetection, initPosition, moreSet, realTimeGuide, strength, workStatus, workTime |
| `2EJP` | SKG智能颈椎按摩仪 | S0102HA | 0CE | mode | BatteryPower, EmsLevel, ModeLib, Voice, collection, heatLevel |
| `2EKR` | 乐尔康按摩椅988N8 | LEK-988N8 | 05F | switch | autoMode, backAction, gravitySwitch, heatSwitch, manuMode, manualAction, massGear, mechanicalAction, ppmAction, pressureState, remainingTime, soleAction, stop, widthAction, workTime |
| `2ELE` | Kandao Meeting Pro 360视频会议机 | MT0822 | 000 | switch | id, micStatus, videoMode, videoSwitch, volume |
| `2ELY` | 龙泉智家一路墙壁开关 | LQ-K01H | 005 | switch | — |
| `2EN1` | 自动卷发器 | LN-Z2 | 000 | status | commonFaultDetection, curlsA, curlsB, intentTemp, temp, usageCount, usageTimeA, usageTimeB |
| `2EN3` | 俏蜻蜓便携式灭蚊灯 | DYT-16 | 0B0 | mode | Powerstate |
| `2EPG` | 优创生活智能跳绳 | SJ-200 | 095 | switch | avgSpeed, calorie, device, maximalJump, sportCount, sportHistory, sportMode, sportTime, stopCount |
| `2EY7` | 昕科智能电蚊香 | XK-QW001U | 0B0 | mode | Environmentalspace, Powerstate, Surplus, TimerOFF, TimerON |
| `2EZQ` | VOC全自动门锁 | T11 | 04B | battery | enableState, event, faultCode, keyList, keyOperate, lastActionTime, lockAlarm, lockMode, lockState, publicKey, remoteCode, remoteInfo, remoteResult |
| `2EZS` | VOC全自动门锁T10 | T10 | 04B | battery | event, faultCode, heartbeatTime, keyList, lastActionTime, lockAlarm, lockMode, lockState, publicKey, remoteCode, remoteInfo, remoteResult |
| `2EZT` | VOC全自动人脸门锁 | T11 Face | 04B | battery | enableState, event, faultCode, keyList, keyOperate, lastActionTime, lockAlarm, lockMode, lockState, publicKey, remoteCode, remoteInfo, remoteResult |
| `2F01` | 凯胜眼部按摩器 | A3_Pro | 000 | switch | DCDL, MS, QY, RF, RFWD, SYSJ, WDTJ, ZD |
| `2F2A` | VOC全自动门锁T10 Face | T10 Face | 04B | battery | event, faultCode, heartbeatTime, keyList, lastActionTime, lockAlarm, lockMode, lockState, publicKey, remoteCode, remoteInfo, remoteResult |
| `2F4N` | SHOEKONG智能运动包 | SK-SB001 | 000 | switch | ChargeState, GetAllStatus, RemainingCapacity, RingLampBrightness, SetMode, SetUvSate, TaskLeftTime, UVprotection, WorkTime |
| `2F7D` | 凯胜眼部美容仪 | A4 Pro | 0CA | switch | DCDL, EMS, MS, RF, RFWD, SYSJ, WDTJ, ZDJW, ZDLD, ZDSF |
| `2F7F` | 品仕乐立式吹风机B1DHW | B1DHW | 0E4 | switch | FanSpeed, Servicesupport, Windtemperature, hairDrierMode, hairDrierStatus |
| `2F9X` | Gimbal Pro L9pro | L9pro | 0EC | battery | gimbalFollowMode |
| `2FJT` | SKG 按摩腰带 Hi-W7 | S0409AA | 0CA | switch | BattPower, EmsLevel, HeatLevel, MasgTimer, SceneMode, collection, customMode, massageKeyLock |
| `2FJW` | 海曼(HEIMAN)智能可燃气体探测器 | JT-WS2CG | 03A | alarm | AlarmType, Language, VolumeSetting, faultDetection, gasSensorS, handonoff, preheat, selfCheck, silencer, switchNightLight |
| `2FM9` | 友通 PM2.5检测仪 | YT6960 | 043 | pm25 | AQI, PM10, Unit, brightness01, commonFaultDetection, humi, temp, tempF |
| `2FNT` | 电动平衡车 C1 | 5LCDC01 | 067 | status | battery1, curMils, delicacy, encyclopedia, instructions, ledControl, speed, speedControl, totalMil |
| `2FOH` | IWARM 智能温控外套 | ZL-HC-WK-001 | 0D0 | switch | HeatingState, commonFaultDetection, deviceControl, deviceMode, temperatureView |
| `2FPI` | 嘉嘉旺智能取暖茶几A330 | A330HML140W80 | 06A | switch | countDown, energySaving, fall, lowerGear, mute, rise, timing, upperGear, workstatus |
| `2FPO` | 电动自行车D1 Pro | TDR02Z | 296 | mode | AutomaticHeadlight, Automatically, BacklightIntensity, ClearData, CurrentSpeed, ElectronicBrake, FitnessRoute, Headlights, Lock, Maintenance, PowerLevel, PrivacyAgreement, SafeDriving, SingleCalorie, SingleMileage, SpeedGears, SteppedFrequency, UserWeight |
| `2FRG` | 新日小风雅Q3 | TDT9381Z | 0C7 | alarm | NFC, OTA, carLock, diagnosis, openSeat, powStatus, remainEle, remainKm |
| `2FRH` | 新日Q5 22版 | XR1200DT-2N | 133 | alarm | NFC, OTA, carLock, diagnosis, openSeat, powStatus, remainEle |
| `2FRI` | 新日QA1 2.0 | TDT0701Z | 0C7 | alarm | NFC, OTA, carLock, diagnosis, powStatus, remainEle |
| `2FSO` | 沃乐智能口袋筋膜枪蓝牙版 | FGMN-R-35-BT | 0C5 | switch | Devicecharge, Lowbatteryalert, Partselection, Record, Totalrecord, Workstatus, gear |
| `2FVQ` | 万达康智能呼啦圈 | LYQ-7012 | 0C2 | battery | devicestatus, fitnessclass, music, otaupdate, sportdata, sportmode, userdata |
| `2G1W` | 富光梦想家智能办公杯 | WFZ1236-580B | 06B | battery | alarmTime1, alarmTime12, alarmTime7, alarmTime8, btConnection, currentTemperature |
| `2G2P` | 飞乐思黑洞安睡眼罩 | HL-E1 | 0CA | switch | DeviceState, Light, Mode, NowTemp, Remind, Reset, TEMP, TimeSet, Timer, Upgrade |
| `2G3W` | 纽曼便携式储能电源 | H600 | 138 | battery | ACswitch, ConnectionStatus, DCswitch, USBswitch, childlock, inputpower, lightmode, outputpower, timedclosescreen, userDelaytime, userFault, userguidance |
| `2G7S` | 氢稳富氢水杯 | H1 | 06B | battery | Atmospherelightswitch, Customrepetition, Drinkwaterreminder, Equipmentswitch, Glasslookup, Hydrogencompletion, Hydrogenproductionvalue, Hydrogenwatermeter, Hydrogenwatertime, Lowpoweralarm, Settingstotakeeffect, Timetoreport, Todaythecumulative, UsageLog, alarmTime1, currentTemperature, repetitionfrequency, synchronizationtime |
| `2G8V` | HYUNDAI现代电动牙刷 | B002 | 073 | status | cleanMode, commonFaultDetection, gears, leftBattary, massageMode, sensitiveMode, whiteMode |
| `2GB5` | 水浸传感器 | MIR-WA100 | 03C | battery | commonFaultDetection, warterAlarm |
| `2GBJ` | 佳仁筋膜枪 | JR-800 | 0C5 | switch | electricity, model |
| `2GD2` | 奥佳华按摩沙发OG-5008Plus | OG-5008Plus | 05F | status | Airintensity, Airmassage, Faultcode, ManualMode, Strengthadjust, Time, action1, autoMode, backadjust, lbpMode, movementadjust, swing, zerogravity |
| `2GE7` | 门窗传感器 | MIR-MC100 | 018 | battery | commonFaultDetection, doorContact |
| `2GIT` | 万播投影仪T6 Max | T6 Max | 098 | switch | controlKey, jfocusing, jvolume, volSwitch |
| `2GJN` | AUX-7600 | AUX-7600 | 05F | switch | airPressure, autoMode, backAction, disptime, heat, manuMode, massGear, ppmMode, soleRoller, zero |
| `2GKB` | 得力保管箱鸿晖系列 | Honghui | 165 | battery | alarms, events, lockState, lockStatus |
| `2GKE` | 虎牌博瑞保管箱 | HP-BR | 165 | battery | alarms, events, lockState, lockStatus |
| `2GKF` | 虎牌炫彩保管箱 | HP-XC | 165 | battery | alarms, events, lockState, lockStatus |
| `2GKM` | 罗曼智能儿童牙刷HK3 | HK3  | 073 | battery | Brushhead, OTA, brushingHistory, brushstrenght, dutstatus, guidesetting, partitionreminder, spraySwitch, use, voiceGuidance, workGuidance, workhours, workmode |
| `2GOQ` | 艾力斯特按摩椅R6S | R6S | 05F | switch | Auto, Bluetooth, Collector, Health, Manual, Other, Recommend, Shoulder, SitAdjustment, State, Timing, VoiceControl, nID |
| `2GOT` | 富林家用制氧机FL100CW | FL100CW | 0F0 | switch | countdown, currentRecord, currentWorktime, deviceState, flowRate, historyData, realtimeData, setCountdown, setFlowRate, totalWorktime |
| `2GOX` | 希影智能投影仪H9 Pro | XY-091 | 098 | switch | contFocus, controlMode, countdown, focusauto, focusing, home, menu, return, setting, system, volSwitch, volume |
| `2GPQ` | 希影智能投影仪H2 Pro | XY-021 | 098 | switch | contFocus, controlMode, countdown, focusauto, focusing, home, menu, return, setting, system, volSwitch, volume |
| `2GQ2` | AIHOME真丝热敷眼罩 | AI-Y30-1 | 0CA | switch | commonFaultDetection, heatState, temperatureSet, tempertureView |
| `2GR0` | 艾力斯特按摩椅V5 | V5 | 05F | switch | Auto, BackIntensity, Bluetooth, Collector, Health, Manual, Other, Recommend, Shoulder, SitAdjustment, State, Timing, VoiceControl, nID |
| `2GR6` | 仁豪家居智能儿童桌 | ET26-ZL101 | 15B | action | MemoryStation, RunStation, SaveStation, ShowHight |
| `2GR9` | 小黄蜂智能冲牙器 T1 | XHF-T1  | 175 | switch | adjust, gear, memory, mode1, pattern, state |
| `2GRN` | 择柔(ZR)智能声波电动牙刷 | Y1 | 073 | mode | BatteryLevel, LeftTime, WorkState, brushingHistory, filterElement, gear, initPosition, setWorkTime, spraySwitch |
| `2GRX` | 智能防漏宝 | AHW20 | 209 | switch | DateStatistics, DirectorOfMeasurement, ParameterSetting, commonFaultDetection, commonFilterElement1, valveStatus, waterTemperature, waterUseData |
| `2GSJ` | 达伦阿拉丁神灯 | X30 | 098 | switch | controlKey, correct, digitalzoom, focus, light, position, volume1 |
| `2GTD` | 虎牌尊虎保险箱 | HP-ZH | 165 | battery | alarms, events, lockState, lockStatus |
| `2GUE` | 仁豪家居升降办公桌 | ZXT-001 | 164 | action | SaveMemory, Station, commonMemory, currentHeight |
| `2GUY` | 小充嗨跑交流充电桩 | XCHP-CAG-XD | 20F | switch | Status, chaState, chgBK, chgGun, chgLog, chgMode, chgPar, chgStu, chgTim, delete, driveStu, faultStatus, lock |
| `2GV0` | 小充嗨跑交流充电桩 | XCHP-CAT-XY | 20F | switch | Status, chaState, chgBK, chgGun, chgLog, chgMode, chgPar, chgStu, chgTim, delete, faultStatus, lock |
| `2GV1` | 小充嗨跑交流充电桩 | XCHP-CAT-XD | 20F | switch | Status, chaState, chgBK, chgGun, chgLog, chgMode, chgPar, chgStu, chgTim, delete, faultStatus, lock |
| `2GVI` | 狄耐克智能一路开关面板 | SH-WDQ-LGT101 | 005 | switch | — |
| `2GWT` | 迈德斯特单电机升降桌 | MJ-D2D | 164 | action | FaultAndDetection, Heightsetting, childLock, commonHeight, condition, currentHeight, sedentaryrSwitch |
| `2GYL` | 大华可燃气体探测器JT-DH-HY-GA4FA-OL | JT-DH-HY-GA4FA-OL | 03A | gasSensor | GasControl, RelayControl, SensorError, Warm, commonFaultDetection, selfCheck, silencer |
| `2H09` | 卿刻智能门锁T5 | T5 | 04B | battery | lockState, openEvent |
| `2H15` | 卡唛电子指纹智能保管箱45HW | BGX-X1-45HW | 08B | battery | FP, PW, SetTime, chipid, doorStatus, historyrecord, openMode |
| `2H16` | 卡唛电子指纹智能保管箱60HW | BGX-X1-60HW | 08B | battery | FP, PW, SetTime, chipid, doorStatus, historyrecord, openMode |
| `2H17` | 卡唛电子指纹智能保管箱80HW | BGX-X1-80HW | 08B | battery | FP, PW, SetTime, chipid, doorStatus, historyrecord, openMode |
| `2H18` | 卡唛电子指纹智能保管箱100HW | BGX-X1-100HW | 08B | battery | FP, PW, SetTime, chipid, doorStatus, historyrecord, openMode |
| `2H1E` | 值米下巴按摩器 | Z2-2 | 28A | battery | MassageIntensity, MassageNumber, MassageScore, ScoreDegree, SleepScore, SleepTime, SnoreNumber, SnoringDuration, TurnoverTimes, dataMonitoring, delayed, privacy |
| `2H38` | 凯胜眼部按摩器 | A7 Pro | 0CA | switch | DCDL, MS, QY, RF, RFWD, SYSJ, WDTJ, ZD |
| `2H4A` | 酷轻松石墨烯多功能护膝 | AD10-01 | 17C | switch | CurrentTemperature, Lowbattery, RemainingHours, VibrationGear, button, countdown, model, temperatureGear |
| `2H4C` | 酷轻松石墨烯降温冰感防晒空调服 | K-JWF-B2V1 | 0D0 | mode | gear, kaiguan, pauseState, timing, workHours |
| `2H4L` | SKG Hi-K3 倍护3 | K3 | 0CA | switch | BattPower, Countdown, EmsLevel, HeatLevel, SceneMode, VoiceAnnouncements, VoicePacket, collection, customMode |
| `2H6G` | 便携式气压按摩系统 | HACM-A1 | 0CA | switch | Alarm, BetteryLevel, Countdown, MassageMode, Personal, Preferences, Recommended, Specification, Strength, connect |
| `2HAH` | 康佳按摩椅KZ-RH6687 | KZ-RH6687 | 05F | switch | AirbagAuto, Hot, Leg, RiseDrop, Roll, TimeSurplus, Timer, VibSwitch, Zero, connect, heacushion, ppmMode, shoulderarms |
| `2HIK` | 慕思FZZ1-002电动床 | FZZ1-002 | 068 | lightSwitch | Stop, headControl, headLegControl, headMassage, legControl, legMassage, modeSelect, oneKeyReset |
| `2HJ2` | 康佳按摩椅KZ-RH6699 | KZ-RH6699 | 05F | switch | AirbagAuto, Hot, Leg, RiseDrop, Roll, TimeSurplus, Timer, VibSwitch, Zero, autoMode, connect, heacushion, shoulderarms |
| `2HJP` | 酷轻松智能热敷包 | K-ZNRFB-B2V1 | 0CA | switch | CurrentTemperature, RemainingHours, TimeOff, button, model, temperatureGear |
| `2HJS` | 开能牌CF-12EYT1型中央净水机 | CF-12EYT1 | 02D | status | dailyWaterVolume, deviceControl, faultDetection, wateSpeed, waterVolume |
| `2HKW` | 智能按摩椅AM | AM-U1 | 05F | switch | AutomaticAirBag, BackRest, Backautomatically, CalfBladder, ConnectionStatus, Constanttemperatureapply, Countdown, Headhipsac, Hipmassage, PressureRegulation, Theremainingtime, autoMode, backmalaxation, footkneading, modeselection, shoulderarms, velocity, waistmassage, zerog |
| `2HLQ` | 奥普浴霸QDP3622AHW | QDP3622A-HW | 035 | lightSwitch | NightLight, drySwitch, leftTime, standbySwitch, ventilateSwitch, warmWindGear, windSwitch |
| `2HLV` | 小充嗨跑交流充电桩 | XCHP-CAG-XY | 20F | switch | ChargingStatistics, chaState, chargingBook, chargingDuration, chargingGun, chargingLock, chargingLog, chargingStatus, chgMode, delete, deviceTime, faultStatus |
| `2HM0` | 黑白生活智能筋膜枪 | U5 | 0C5 | status | Lowbatteryprompt, Remainingtime, Videointroduction, gears, speed, worktime |
| `2HO0` | 上谷智能往复式剃须刀 | S5 | 170 | status | AfterGuide, BatteryLevel, SmartLock, UseTime, btConnection |
| `2HR5` | 西蒙一位智能开关 | 58E8201 | 005 | switch | commonFaultDetection, indicator, switchStatus |
| `2HSK` | FOOXMET智能温控裤 | IWARM-HM-007 | 0D0 | switch | commonFaultDetection, deviceControl, deviceMode, heatingState, tempertureView |
| `2HSL` | FOOXMET智能温控腰包 | IWARM-HM-003 | 0CA | switch | commonFaultDetection, deviceControl, deviceMode, heatingState, tempertureView |
| `2HTE` | FOOXMET智能温控马甲 | IWARM-HM-001 | 0D0 | switch | commonFaultDetection, deviceControl, deviceMode, heatingState, tempertureView |
| `2HTN` | 智能剃须刀2130 | DWF-TX2130 | 170 | status | AbnormalLowBattery, BluetoothStatus, DevCharge, DevVbatt, WorkStatus |
| `2HUZ` | 唯妙智能影音控制主机 | TW500 | 0BD | switch | back, direction, home, hybrid, microphone, music, mute, ok, playControl, soundMode |
| `2HW4` | 虎牌尚悦保险箱 | HP-SY | 165 | battery | alarms, events, lockState, lockStatus |
| `2HZC` | 海曼(HEIMAN)智能可燃气体报警器 | JT-WS725 | 03A | alarm | AlarmType, faultDetection, handonoff, preheat, selfCheck, silencer, switchNightLight |
| `2HZW` | 电热毯(酷轻松智能电热毯) | MA20-01 | 0D0 | status | attribute, err, lock, sleepSet, synchronization, userSet |
| `2I0F` | 东鹏智能马桶W8481 | W8481T | 123 | switch | Move, PowerSaving, autoFlushing, cleaningSwitch, dryGear, faultDetection, filpSwitch, footFeel, gear, lightSense, nozzlePos, seatGear, seatRing, seatStatus, toiletMode, waterGear |
| `2I10` | 莱轻松智能暖宫腰带 | LG04 | 0CA | switch | batteryView, commonFaultDetection, fomentTemperature, messageStall, timedFuntion |
| `2I1N` | 梦百合0压智能床L7 | L7 | 14A | lightSwitch | BedData, GetMemoryMode, SleepReport, headControl, headMassage, instructions, legControl, legMassage, massageMode, massageTimer, memoryControl1, modeSelect, oneKeyReset, pause, runningstate, sleepstatus |
| `2I3G` | 梦百合0压智能枕 | MLP-WBP-G2 | 054 | battery | MianOTA, PillowData, SleepReport, Snoring, deviceState, notice, sleepstatus, wifi |
| `2I3Y` | 探梦者智能电动漂移鞋 | S1 | 067 | status | LEDLight1, LEDLight2, LEDLightcolour1, LEDLightcolour2, Lowpoweralarm, battery1, battery2, deviceSelftest, gear, instructions, lockMechanism, mileage, reset, speed, standbyTime, status1, status2 |
| `2I4E` | 5G通信壳 618 |  | 228 | switch | — |
| `2I5A` | 舒元AS-8883足疗机 | AS-8883 | 0CA | switch | air, cdRemain, cdTotal, customMode, firmware, heating, massage, sync, workTime |
| `2I5Q` | 飞利浦智能台式净饮机 | ADD6861 | 02D | status | BoilingPoint, InputTemp, SmartOutletSet, SmartTempSet, Warning, WinterMode, faultDetection, filterElement1, filterReset, inputTds, outWaterTemp, output, outputTds, rinseMode, water |
| `2I8R` | 木林森智联车载氧吧 | MLS-CZ01A | 18A | switch | CronJob, Equipmentstatus, Lowpoweralarm, O3switch, PM2D5, anion, fanSpeed, powerState, timeSync |
| `2I91` | FOOXMET智能温控围巾 | IWARM-HM-002 | 0D0 | switch | commonFaultDetection, deviceControl, deviceMode, heatingState, tempertureView |
| `2I92` | 博凡保险箱 | BGX-X2-45W | 165 | battery | alarms, lockState, lockStatus, openMode |
| `2I93` | 智能喉部脉冲按摩器 | YA4200 | 0CA | switch | Batterydisplay, Connected, FaultAlarm, InterventionIntensity, Interventiondelay, Sensitivity, SleepReport |
| `2IBH` | 驰球珍柜保险箱 | FDX-A/D-45ZG | 08B | battery | alarmEvent, connectionStatus, lockStatus, openMode |
| `2ICD` | 海雀智能摄像头2S 3K版 | IG5S5H0B1 | 008 | switch | alarmEvent, cruiseSwith, shootSwitch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 |
| `2IGA` | 万播投影仪WB-T3 | WB-T3 | 098 | switch | controlKey, jfocusing, jvolume, volSwitch |
| `2IGO` | 欧普蓝牙Mesh小夜灯 | LDJ86860110HG02 | 21F | switch | commonFaultDetection, toggleSwitch |
| `2IHC` | 爱华仕智能花朵箱 | OCX6695 | 13D | status | Led |
| `2IJ4` | 摩托车头盔对讲耳机 | EJEAS Q7 | 2AD | status | FM, FMSwitch, FmList, Music, Power, Selfbattery, Team, VoiceSet |
| `2IKH` | 皇鼎智能门锁VE08W | VE08W | 04B | alarm | BatteryLevel, UserList, faultCode, lockMode, lockState, lockStatus, openEvent |
| `2INC` | 智能空调控制器 | HL-AC001 | 10D | temperature | airKey, airSwitch |
| `2INL` | 艾家智能一位开关 | Z1K1 | 005 | switch | lightness |
| `2INT` | 艾家智能四位场景面板 | Z1CK4 | 005 | luminance | deviceStatus, sceneButton1, sceneButton2, sceneButton3, sceneButton4 |
| `2INU` | 艾家智能六位场景面板 | Z1CK6 | 005 | luminance | deviceStatus, sceneButton1, sceneButton2, sceneButton3, sceneButton4, sceneButton5, sceneButton6 |
| `2IRH` | CRMCR卡唛卡诺II智能保管箱 | BGX-X1-55KN | 08B | battery | CID, FP, PW, SetTime, alarmEvent, connectionStatus, historyrecord, lockStatus, openMode |
| `2IRM` | 燃动智能单杠 | LYDG-011 | 0C2 | battery | devicestatus, fitness, historicaldata, otaupdate, paraset, sportdata, sportmode, userdata |
| `2ISY` | 澳莱克林商务直饮机 | AL-2GA | 06F | status | afterservice, dts, faultprompt, filterstatus, timerset, watertemperature |
| `2IUB` | 西蒙一位智能场景开关 | 58E8205 | 005 | switch1 | commonFaultDetection, deviceStatus, indicator, mode1, sceneButton1 |
| `2IUI` | 雅兰云电动床N030 | N030 | 14A | lightSwitch | angleControl, backcalfControl, headLegControl, headMassage, legControl, legMassage, massageMode, modeSelect, oneKeyReset |
| `2IVN` | 佳普乐G5-300A自动翻盖智能马桶 | G5-300A | 066 | mode | ECO, cover, dryGear, drySwitch, flush, hPosition, heatGear, hintenty, nightled, seat, sitdown, smart, wPosition, waterTemp, wintenty |
| `2IVO` | 佳普乐G5-400A自动翻盖智能马桶 | G5-400A | 066 | mode | ECO, cover, dryGear, drySwitch, flush, hPosition, heatGear, hintenty, nightled, seat, sitdown, smart, wPosition, waterTemp, wintenty |
| `2IVS` | 佳普乐G6-300A自动翻盖智能马桶 | G6-300A | 066 | mode | ECO, cover, dryGear, drySwitch, flush, hPosition, heatGear, hintenty, nightled, seat, sitdown, smart, wPosition, waterTemp, wintenty |
| `2IVT` | 佳普乐G6-400A自动翻盖智能马桶 | G6-400A | 066 | mode | ECO, cover, dryGear, drySwitch, flush, hPosition, heatGear, hintenty, nightled, seat, sitdown, smart, wPosition, waterTemp, wintenty |
| `2IVW` | 左点智能蒲团 | ZD-AH0201 | 0C3 | mode | close, connectStatus, mugwort, open, play, remainTime, reset, temp |
| `2IWW` | 智能门 JinLY | JL-Y001 | 04B | battery | encryptedText, faultCode, lockState, lockStatus, openEvent, publicKey, tempPasswd, tempPasswd2 |
| `2IXY` | 惠尔顿智转PRO MAX | WD016 | 0DF | battery | Buckle, LeftISOFIXstatus, RightISOFIXstatus, RotationStatus, SeatStatus, SupportLegStatus |
| `2IZ3` | 5G通信壳 658 |  | 228 | switch | — |
| `2IZ4` | 5G通信壳 688 |  | 228 | switch | — |
| `2J1T` | 智能洗地机2202 | ePro-2202 | 19F | status | Cleanreminder, batterystatus, cleandata2, cleandata3, cleanwaterboxstatus, commonExecution4, devicealarm, filterlife, filterlifealarm, rollerbrushlife, rollerbrushlifealarm, sewageboxstatus, timingselfclean, voiceset, workmode, workstatus |
| `2J34` | VTT智能筋膜枪 | V6 | 0C5 | switch | ReTime, Speed, TIME, value, workstate |
| `2J40` | A.O.史密斯中央净水机WF25G2 | WF25G2 | 2B5 | status | dayPurifyWater, faultDetection, filterElement1, flushTime, totalPurifyWater, useTime, waterSpeed |
| `2J41` | A.O.史密斯中央软水机S20G2 | S20G2 | 2B4 | status | dayWater, faultDetection, filterElement1, remakeTime, totalWater, useTime, waterSpeed |
| `2J42` | A.O.史密斯反渗透净水机R1200BN1 | R1200BN1 | 02D | status | faultDetection, filterElement1, filterElement2, purifyWater, suggestCount, totalPurifyWater, useTime |
| `2J6E` | 路福梦享家link | S202 | 068 | lightSwitch | headControl, legControl, lieTime, massage, massageMode1, massageTime, memoryControl1, memoryControl2, memoryControl3, memoryControl4, memoryControl5, modeSelect, oneKeyReset, resetMemory, yogaNumber |
| `2J7W` | 飞利浦膝盖按摩器PPM3102L | PPM3102L | 0CA | switch | Intensity, OTAUpgrade, Remaining, Warning, batteryLevel, deviceSatus, message, myCollection, temper, waterTemp, workMode |
| `2J90` | 艾力斯特按摩椅S730H | S730H | 05F | switch | Auto, Bluetooth, Collector, Manual, Other, Recommend, Shoulder, SitAdjustment, State, Timing, VoiceControl, nID |
| `2J9V` | 十字勋章智能运动健身包 | CR-9956BK-HW | 13C | status | Battery, Finder, PowerSwitch, Tone, commonFaultDetection, sterilize |
| `2JDF` | 拉维莱特智慧酒柜LT-1270AW1 | LT-1270AW1 | 0FE | temperature | Connection, Door, Mode, commonFaultDetection |
| `2JDK` | 智能椅SC-0004 | SC-0004 | 2BA | battery | EquipmentStatus, ManualMode, SmartWaistMode, chargeStatus, eventTime, faultDetection, lengthofwaistsupport, seated, seatingtime, sedentaryReminder, sedentaryReminderMode, sedentaryTime, sitPosture, sitTime, switchingfrequency |
| `2JFK` | FOOXMET智能温控外套 | IWARM-HM-004 | 0D0 | switch | commonFaultDetection, deviceControl, deviceMode, heatingState, tempertureView |
| `2JG4` | FOOXMET智能温控披肩 | IWARM-HM-008 | 0D0 | switch | commonFaultDetection, deviceControl, deviceMode, heatingState, tempertureView |
| `2JGU` | FOOXMET智能温控背包 | IWARM-HM-006 | 0D0 | switch | commonFaultDetection, deviceControl, deviceMode, heatingState, tempertureView |
| `2JH9` | 波司登智能温控科技羽绒服 | IWARM-HM-009 | 0D0 | switch | commonFaultDetection, deviceControl, deviceMode, heatingState, tempertureView |
| `2JHA` | 波司登智能温控科技羽绒马甲 | IWARM-HM-010 | 0D0 | switch | commonFaultDetection, deviceControl, deviceMode, heatingState, tempertureView |
| `2JHL` | 智能升降桌AD2-HW | AD2-HW | 164 | action | HealthyNeckHeight, HealthyNeckMode, HealthyNeckTime, childLock, currentHeight, faultDetection, memoryControl1, memoryControl2, postureSittingHeight, postureStandHeight, sedentaryHeight, sedentaryTimeSet, sedentaryrSwitch |
| `2JK9` | 虎牌北辰床头保管箱 | HP-BC | 165 | battery | alarms, lockState, lockStatus, openMode |
| `2JLB` | gb SMART儿童座椅通风垫 | TFD001 | 287 | mode | close, connectstatus, devDesc, devStatus, timeOff, wind |
| `2JLF` | gb SMART智能安抚摇床 | YC600 | 285 | status | cryingSwitch, gear, knowledge, music, nightSwitch, speed, usage, volume |
| `2JNB` | 莱轻松智能暖宫宝 | LG-02 | 0D0 | status | batt, hot, wave |
| `2JOG` | 按摩椅RSM6 | RSM6 | 05F | switch | AutomaticAirBag, BackRest, Backautomatically, CalfBladder, ConnectionStatus, Constanttemperatureapply, Countdown, Headhipsac, Hipmassage, PressureRegulation, Theremainingtime, autoMode, backmalaxation, footkneading, modeselection, shoulderarms, velocity, waistmassage, zerog |
| `2JOJ` | VSITOO智能手冲咖啡壶 | K01 | 2C2 | switch | commonFaultDetection, heating, temp, workState |
| `2JOK` | VSITOO智能咖啡电子秤 | K02 | 2C2 | battery | charge, min, preWater0, preWater1, preWeight, sec, stage, weight |
| `2JP5` | 贝琪B321数码电子钢琴 | B321 | 159 | mode | Beatvolume, Deviceswitch, Service, metronome, practice, practiceHistory, speed, volume |
| `2JQE` | HCK哈士奇赛博朋克冰吧SC-98ZZAS | SC-98ZZAS | 08A | childLockSwitch | Quickcoolingmode, Warning, door, door2, light, power, service, temp |
| `2JR2` | sayrelances智能剃须刀 | TX-100 | 170 | status | devicestatus, gear, lowPowerAlarm, quantity, score, workingHours |
| `2JTK` | CRMCR卡唛卡诺II智能保管箱-抽柜版 | BGX-X1-55KNII | 08B | battery | CID, FP, PW, SetTime, alarmEvent, connectionStatus, historyrecord, lockStatus, openMode |
| `2JTL` | CRMCR卡唛卡诺II智能保管箱-抽柜无线充版 | BGX-X1-55KNIII | 08B | battery | CID, FP, PW, SetTime, alarmEvent, connectionStatus, historyrecord, lockStatus, openMode |
| `2JTR` | 公牛智能转换插座GN-Y201HJ | GN-Y201HJ | 01D | switch | commonFaultDetection, electric, indicator, memorySwitch, power |
| `2JUA` | 邮差 | TL1000DT-3E | 0C7 | switch | Locked, autoLock, batteryTemp, derviceStatus, remainBattery, remainingMileage, saddleOpen, vehicleDiag, voiceBroadcast |
| `2JVR` | SMK石墨烯智能护具 | GH01 | 0CA | switch | CurrentTemperature, EquipmentStatus, Gear, MODE, RemainingHours, TEMP, TIME, button, level |
| `2JVZ` | 巢居全新360度取暖器N3-C2200HA | N3-C2200HA | 06A | switch | CHILDLOCK, Currenttemperature, Lightcolor, Lightinducedsleep, Modeselection, purify, timing, voice |
| `2JYH` | 健诺德云朵暖宫宝 | XD-CX-T18 | 17D | battery | alert, countdown, light, massage, state, warm |
| `2JYT` | 一米大流量智能净水器600X | OM-RO-600X | 02D | status | Cleaning, commonFaultDetection, filterElement1, filterElement2, filterElement3, pureWater, rawWaterTDS, totalPurifyWater |
| `2JZI` | 乐维熺红外理疗仪S01 | LV-S01 | 0D0 | switch | Countdown, Gear, aftersaleservice, devicestatus |
| `2K0M` | 希影智能投影仪L12 Pro | XY-016 | 098 | switch | contFocus, controlMode, countdown, focusauto, focusing, home, menu, return, setting, system, volSwitch, volume |
| `2K0Q` | 希影智能投影仪L12 Mini | XY-018 | 098 | switch | contFocus, controlMode, countdown, focusauto, focusing, home, menu, return, setting, system, volSwitch, volume |
| `2K1K` | 顾家智能电动床 | I06-900 | 14A | lightSwitch | angleControl, headControl, headLegControl, legControl, legMassage, massageMode, modeSelect, oneKeyReset, service |
| `2K2I` | 宝宝巴士点读笔G3 | CDDJJ00301 | 155 | battery | AccountInformation, Aftersalesservice, Logonstatus, MP3mode, PrivacyStatement, Scheduleadjustment, WIFIconnect, WIFIinfo, batterylevel, connectedWIFI, currentplay, deviceStatus, deviceinformation, isBindAccount, playadjust, resultCode, selectsong, songlist, volume |
| `2K3K` | 贝氪智能托腰椅C1 | C1 | 2BA | battery | Bat, BeepTips, ChairStatus, Pressure, RunMode, Version, sedentaryTime |
| `2K5N` | 智能清洗一体机 | YLQ4101D-Z | 13B | battery | BatteryLife, ChildLock, Gear, Instructions, WaterPressure, WaterYield |
| `2KDA` | 正泰三孔智能插座 | NEW3-W53010D | 1FC | switch | electric, faultDetection, indicator, memorySwitch, power |
| `2KEK` | simon玻璃材质10A五孔智能插座面板 | 58E8241QW | 1FC | switch | IndicatorMode, electric, faultDetection, indicator, memorySwitch, power |
| `2KEL` | simon玻璃材质16A三孔智能插座面板 | 58E8242QW | 1FC | switch | IndicatorMode, electric, faultDetection, indicator, memorySwitch, power |
| `2KFV` | 小豚室外摄像头 | XT-X31 | 008 | switch | alarmEvent, cruiseSwitch, pushStatus, shootSwitch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 |
| `2KL7` | 哈尔斯智能水杯 弹盖款(升级版) | HDM-450-16/HDM-420-66 | 06B | battery | canvasConfig, canvasData1, canvasData2, canvasData3, canvasData4, canvasData5, config, currentTemperature, darkWeekTarget, drinkDisturb, drinkRemind, drinkTarget, drinkTemperature, drinkWarn, drinkWeekTarget, tempRemind, waterDayIntake, waterHoursIntake, waterWeeksIntake |
| `2KL8` | 哈尔斯智能水杯 旋盖款(升级版) | HDM-450-36/HDM-450-36A | 06B | battery | canvasConfig, canvasData1, canvasData2, canvasData3, canvasData4, canvasData5, config, currentTemperature, drinkDisturb, drinkRemind, drinkTarget, drinkTemperature, drinkWarn, drinkWeekTarget, tempRemind, waterHoursIntake, waterWeeksIntake |
| `2KLC` | 哈尔斯智能咖啡杯 | HGM-350-001 | 06B | battery | clockIn, coffe, currentTemperature, totalCount |
| `2KLE` | 哈尔斯智能水杯  恒温暖暖杯 | HEK-0350-23 | 06B | battery | buzzerSwitch, connectStatus, constTempTime, constTempTimeAlready, constTempTimeSwitch, currentTemperature, customTemperature, drinkTemperature, findCupState, hasSetHeatTemp, hotMode, hotState, usbState |
| `2KPV` | 5G通信壳 698 |  | 228 | switch | — |
| `2KXT` | 霍尼韦尔水浸传感器 | HZBS-H-WL | 03C | battery | commonFaultDetection, waterAlarm |
| `2L40` | 美颜枕(4D智能版) | HP100-5 | 054 | battery | HR, led, power, realtimeRR, sleepstatus |
| `2L53` | 携住红外遥控器XZB-HWZFQ-3.0 | XZB-HWZFQ-3.0 | 007 | mode | GATT, STBKey, TVKey, airKey, hchoElement, matchedCap, projectorKey, rcList |
| `2L5L` | 嘿码智能剃须刀BC9000 | BC9000 | 170 | status | AlarmMessage, CleanTime, CutterTime, Lock, Ota, OuterCluter, Power, Speed, Version, WorkMode, WorkStatus, Worktime |
| `2L5P` | 智能加热护膝 | A3 | 17C | switch | BatteryLevel, CountDownOff, CurrentTemp, DeviceSatus, Heating, Massage, OTAUpgrade, Warning |
| `2L5Z` | 爱里森电子琴 | ALS-D61 | 159 | status | jiaoxue, jiepai, jiezou, led, song, yinse |
| `2L9O` | 奥莱敏控人体传感器 | AL256-W | 049 | luminance | alarmTime, lightBrightness, motionDetected, pirs, sensitivity, switchNightLight |
| `2LAN` | 哈尔斯智能水杯 茶水分离款 | HDM-350-71 | 06B | battery | brewCount, brewTime, canvasConfig, canvasData1, canvasData2, canvasData3, canvasData4, canvasData5, config, connectStatus, currentTea, currentTemperature, drinkRemind, drinkTemperature, teaMode, teaOrder |
| `2LB6` | 希影智能投影仪L12 Max | XY-020 | 098 | switch | contFocus, controlMode, countdown, focusauto, focusing, home, menu, return, setting, system, volSwitch, volume |
| `2LBD` | 百朗亚利桑那200浴霸系列 | HB-NL200-H/H | 035 | lightSwitch | drytype, nightLightSwitch, odorsensingSwitch, radar, sterilizationSwitch, swingSwitch, ventilateSwitch, warmWindGear, windSwitch |
| `2LBL` | 百朗亚利桑那280浴霸系列 | HB-NL280-H/H | 035 | lightSwitch | drytype, nightLightSwitch, odorsensingSwitch, radar, sterilizationSwitch, swingSwitch, timeset, ventilateSwitch, warmWindGear, windSwitch |
| `2LC9` | 鸿蒙智选 小豚当家室外摄像头 4G版 | XT-H32 | 008 | switch | alarmEvent, lteService, pushStatus, shootSwitch, videoSwitch |
| `2LD6` | 惠尔顿AI前置过滤器 | WHT-P0068 | 02D | mode | CareReminder, DailyWaterLog, batteryLevel, charge, commonFaultDetection, console, dayUseRecord, drain, flow, fortify, temp, waterConsumption, waterValve |
| `2LFZ` | 乐德飞翼AI智能床垫A3 | ADL 200-A3-AI | 068 | childLockSwitch | antiSnoring, bedCondition, headControl, legControl, mac, memoryControl1, memoryControl3, modeSelect, oneKeyReset, pause, privacyStatement, rouseHeight, siteSelection, sleepStatistics, sleepstatus, wakeUp |
| `2LHK` | 捷昌智能升降桌 | JC35TS-NE2 | 164 | action | currentHeight, equipmentStatus, faultDetection, memoryControl1, memoryControl2, memoryControl3, memoryControl4, patternJudgment, sedentaryReminder |
| `2LHV` | 中央净水 | MC3-Js | 2B5 | status | dayPurifyWater, faultDetection, filterElement1, flushTime, totalPurifyWater, waterSpeed |
| `2LHW` | 中央软水 | MC3-Rs | 2B4 | status | dayWater, faultDetection, filterElement1, remakeTime, totalWater, waterSpeed |
| `2LIK` | 小豚当家室外摄像头3K版 | XT-H33 | 008 | switch | alarmEvent, cruiseSwith, pushStatus, shootSwitch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6, voip |
| `2LIZ` | 达伦阿拉丁神灯X30 Pro | X30 Pro | 098 | switch | controlKey, correct, digitalzoom, focus, light, position, volume1 |
| `2LKK` | 德国朗乐福智能床 Max II | MaxII | 14A | lightSwitch | BedData, GetMemoryMode, Massagearea, Massagegear, Modeloop, SleepReport, backControl, legControl, lumbarsupport, massageMode, massageTimer, memoryControl1, memoryControl2, modeSelect, oneKeyReset, runningstate, sleepstatus |
| `2LMH` | 根元智能运动包 | SK-SB002 | 143 | switch | LightingDelay, Mode, RemainingCapacity, RingLampBrightness, WorkTime, batteryState, leftTime, lightingState |
| `2LOJ` | 燃气壁挂炉 | MC3-GL | 174 | switch | Gas, bathTemperature, burningTime, coStatus, faultDetection, heatTemperature, maintenanceStatus |
| `2LOY` | 海雀智能摄像头3i 2.5K版 | AG432IG2S400S1 | 008 | switch | alarmEvent, cruiseSwitch, shootSwitch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6, voip |
| `2LP1` | 海雀智能摄像头3Pro 4K版 128GB | IH6SC800S2 | 008 | switch | alarmEvent, shootSwitch, videoSwitch, voip |
| `2LP7` | 友通甲醛检测仪 | YT6965 | 1F2 | hcho | alarmSwitch, brightness01, clock, commonFaultDetection, humi, report, temp |
| `2LPA` | 海雀智能摄像头3 4K版 | HS864IH6S800B1 | 008 | switch | alarmEvent, cruiseSwitch, shootSwitch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 |
| `2LPJ` | 海雀智能摄像头3S 3K版 | AS532IG5S5H0B1 | 008 | switch | alarmEvent, cruiseSwitch, shootSwitch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 |
| `2LQ1` | 友通空气质量检测仪 | YT6960S | 1F2 | pm25 | aqi, brightness01, clock, commonFaultDetection, humi, pm10, report, temp |
| `2LR3` | iSteady XE Kit | iSXE | 0EC | battery | ModeSwitch, RockerControl |
| `2LRK` | 博芬智能酒柜BF-1900AU1 | BF-1900AU1 | 0FE | temperature | commonFaultDetection, number |
| `2LRO` | 希影智能投影仪H9 Max | XY-092 | 098 | switch | contFocus, controlMode, countdown, focusauto, focusing, home, menu, return, setting, system, volSwitch, volume |
| `2LX2` | 在鸿学生终端 | KHZD-EDD-001 | 281 | battery | turningOffScreen |
| `2M4E` | 九牧轻智能丝雨置物恒温淋浴器 | 26185-624/HBS-1 | 300 | status | coldWaterSwitch, commonFaultDetection, devStatus, waterTemp |
| `2M4P` | 台铃YO兔 | TDT6028Z | 0C7 | switch | Locked, Status, derviceStatus, remainBattery, remainingMileage, saddleOpen, voiceBroadcast |
| `2M4T` | 台铃XTM2.0 | TDR6042Z | 0C7 | switch | Locked, Status, derviceStatus, remainBattery, remainingMileage, saddleOpen, voiceBroadcast |
| `2M4U` | 台铃狂飙60超能版KS | TL1200DT-25E | 0C7 | switch | Locked, Status, derviceStatus, remainBattery, remainingMileage, saddleOpen, voiceBroadcast |
| `2M68` | 值米智能下巴按摩器 | Z3-1 | 28A | battery | MassageIntensity, MassageNumber, MassageScore, ScoreDegree, SleepDataStatistics, SleepQuality, SleepScore, SleepTime, SleepingPosition, SleepingPositionData, SnoreNumber, SnoringDuration, TurnoverTimes, dataMonitoring, delayed, privacy |
| `2M6T` | 小豚当家智能摄像头 2 | XT-X10 | 008 | switch | alarmEvent, cruiseSwitch, pushStatus, shootSwitch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6, voip |
| `2M7Y` | 良品主义智能热敷腰带 | N515 | 17D | switch | AlarmMessage, Countdown, Heating, LastTime, Ota, Power, Vibrate, WorkStatus |
| `2M8O` | 舒怡温润床垫 | ZW-SY-002 | 07C | switch | aboutchange, currenttemp, longvave, modechange, oldmode, settemp |
| `2MDC` | 多合一空调新风地暖温控器(开关型) | F14C | 10D | temperature | acTemperature, acmaxtempSet, acmintempSet, airFan, airKey, antifreezingMode, capabilitySet, deviceFormSetting, faultDetection, freshAirFan, freshAirMode, freshAirSwitch, heaterSwitch, heaterTemperature, heatermaxtempSet, heatermintempSet |
| `2MDH` | 台铃-标兵2.0 | TL1200DT-29E | 0C7 | switch | Locked, Status, derviceStatus, remainBattery, remainingMileage, saddleOpen, voiceBroadcast |
| `2MDI` | 台铃-劲风EB | TDT740Z | 0C7 | switch | Locked, Status, derviceStatus, remainBattery, remainingMileage, saddleOpen, voiceBroadcast |
| `2MDJ` | 台铃-周末 | TL1000DT-31E | 0C7 | switch | Locked, Status, derviceStatus, remainBattery, remainingMileage, saddleOpen, voiceBroadcast |
| `2MDK` | 台铃-塞北 | TL1200DT-15F | 0C7 | switch | Locked, Status, derviceStatus, remainBattery, remainingMileage, saddleOpen, voiceBroadcast |
| `2MDN` | 台铃-夺冠EB | TDT738Z | 0C7 | switch | Locked, Status, derviceStatus, remainBattery, remainingMileage, saddleOpen, voiceBroadcast |
| `2MDO` | 台铃-潮达 | TDT6107Z | 0C7 | switch | Locked, Status, derviceStatus, remainBattery, remainingMileage, saddleOpen, voiceBroadcast |
| `2MDP` | 台铃-天鹅 | TL1200DT-17F | 0C7 | switch | Locked, Status, derviceStatus, remainBattery, remainingMileage, saddleOpen, voiceBroadcast |
| `2MDQ` | 台铃-未莱 | TL1200DT-18F | 0C7 | switch | Locked, Status, derviceStatus, remainBattery, remainingMileage, saddleOpen, voiceBroadcast |
| `2MDR` | 台铃-T300 | TL2000DT-33T | 0C7 | switch | Locked, Status, derviceStatus, remainBattery, remainingMileage, saddleOpen, voiceBroadcast |
| `2MDS` | 台铃-摩术 | TL2000DT-35T | 0C7 | switch | Locked, Status, derviceStatus, remainBattery, remainingMileage, saddleOpen, voiceBroadcast |
| `2MDT` | 台铃-追风EB | TDT733Z | 0C7 | switch | Locked, Status, derviceStatus, remainBattery, remainingMileage, saddleOpen, voiceBroadcast |
| `2MFE` | 多合一空调新风地暖温控器(协议型) | P14C | 10D | temperature | acTemperature, acmaxtempSet, acmintempSet, airKey, antifreezingMode, capabilitySet, deviceFormSetting, faultDetection, freshAirFan, freshAirMode, freshAirSwitch, heaterSwitch, heaterTemperature, heatermaxtempSet, heatermintempSet, reboot |
| `2MH8` | 易百珑一键智能开关 | EWS51-HM | 201 | switch1 | CleanPair, Pair, led, memorySwitch, mode1, sceneButton1 |
| `2MIQ` | 艾优智能剃须刀 | H1 | 170 | status | alrmPrompt, bladeCleaning, bladeStatus, currentElectricity, findDevices, hota, syncTime, workMode, workStatus |
| `2MJD` | 红外万能遥控中心 | YKK-H1025 | 007 | status | STBKey, TVKey, airKey, backup, batchCmd, customKey, delay1, fanMode, fanSwitch, indicatorSwitch, matchedCap, mediaKey, mediaKey1, mediaKey2, mediaKey3, projectorKey, purifierKey, rcList, speakerKey |
| `2MLD` | 红外转发器 | YKK-H1027 | 007 | status | STBKey, TVKey, airKey, backup, batchCmd, customKey, delay1, fanMode, fanSwitch, indicatorSwitch, matchedCap, mediaKey, mediaKey1, mediaKey2, mediaKey3, projectorKey, purifierKey, rcList, speakerKey |
| `2MLY` | 奇立智能投影仪H6 Pro | CL-C58 | 098 | switch | contFocus, controlMode, countdown, focusauto, focusing, home, menu, return, setting, system, volSwitch, volume |
| `2MMM` | 嵌饮机 | WS5054BC1C | 02D | childLockSwitch | customProgram, faultDetection, filterElement1, filterElement2, inputTds, outputTds, totalPurifyWater |
| `2MNC` | 佳普乐宏臻智能毛巾架 | TH1HZ-06S | 0BA | mode | BathMode, KeySoundReminder, TimingMode, drying, dryingGear |
| `2MNU` | 佳普乐宏尚智能毛巾架 | TH1HS-05G | 0BA | temperature | disinfect, drying, dryingLeftTime, dryingTime, nightlightSwitch |
| `2MPD` | 家用制氧机H-601L | H-601L | 0F0 | switch | Control, onetime, oxygen, oxygenflow, workRecord |
| `2MPT` | 佳普乐舒樾智能方镜柜 | MC2SY-10C | 301 | switch | Beep, Humidity, Temperature, aromatherapyGear, atmosphereLightSwitch, demisterSwitch, demisterTime, makeupLightGear, makeupLightPercentage, sterilizeSwitch, sterilizeTime |
| `2MQI` | 希影H9 Max家庭K歌影院 | XY-093 | 098 | switch | contFocus, controlMode, countdown, focusauto, focusing, home, menu, return, setting, system, volSwitch, volume |
| `2MQT` | 希影智能投影仪H9 Pro第二代 | XY-097 | 098 | switch | contFocus, controlMode, countdown, focusauto, focusing, home, menu, return, setting, system, volSwitch, volume |
| `2MTN` | 华为智选 海雀智能摄像头3 4K版 64GB | IS8SC800B2 | 008 | switch | alarmEvent, cruiseSwitch, shootSwitch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6, voip |
| `2MUI` | 鸿蒙智选 海雀智能摄像头3 4K版 128GB | IS8SC800B3 | 008 | switch | alarmEvent, cruiseSwitch, shootSwitch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6, voip |
| `2MWB` | 云康宝肩颈按摩仪CMN10C | CMN10C | 0CE | switch | Information, SetData |
| `2MXF` | 独立式光电感烟火灾探测报警器 | MIR-SM01-PLC | 039 | alarm | commonFaultDetection, selfCheck, silencer, smokeSensor |
| `2MXT` | 嘿码智能剃须刀BC8010 | BC8010 | 170 | status | AlarmMessage, CleanTime, CutterTime, Lock, Ota, Power, Speed, Version, WorkMode, WorkStatus, Worktime |
| `2MZN` | 小豚当家室外摄像头T5 3K双摄版 | XT-H40 | 008 | switch | alarmEvent, familiarFaceAlarm, logReport, pushStatus, shootSwitch, strangerFaceAlarm, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 |
| `2N0S` | 永艺智能撑腰椅Flow 660 | Flow 660 | 2BA | battery | ChargeState, LongSitState, LongSitStop, RemindCout, RemindInterval, RemindTime, SetTimeIncrease, SitState, sedentaryReminder, sedentaryTime |
| `2N1C` | 永艺智能升降桌Thea 680 | Thea 680 | 164 | action | HealthyNeckHeight, HealthyNeckMode, HealthyNeckTime, childLock, currentHeight, faultDetection, memoryControl1, memoryControl2, postureSittingHeight, postureStandHeight, sedentaryHeight, sedentaryTimeSet, sedentaryrSwitch |
| `2N1I` | 艾力斯特M6按摩椅 | M6 | 05F | switch | Auto, BackIntensity, Bluetooth, Collector, Manual, Other, Shoulder, SitAdjustment, State, Timing, VoiceControl |
| `2N2R` | A.O.史密斯反渗透净水机R1200H | R1200H | 02D | status | faultDetection, filterElement1, filterElement2, purifyWater, suggestCount, totalPurifyWater, useTime |
| `2N44` | 嘿码智能剃须刀BC3000 Pro | BC3000 Pro | 170 | status | AlarmMessage, CleanTime, CutterTime, Lock, Ota, OuterCluter, Power, Speed, Version, WorkMode, WorkStatus, Worktime |
| `2N63` | 电动智能窗HC86PY | HC86PY | 2BC | action | childLock, lock, windowOpener |
| `2N7I` | 月光星球暖腹腰带 | WW-001 | 17D | battery | heat, light, massage, usetime |
| `2N7Z` | subnado水下推进器PP11011 | PP11011 | 293 | mode | deviceNum, deviceVersion, fault, leftDevice, otaUpdate, protection, rapidRemian, record, rightDevice, speed, workStatus |
| `2N8D` | 空间卫士健康空气智慧管家01 | KJWS-01 | 030 | switch | FragranceTime, PM, anion, density, filterElement01, filterElement02, filterElement03, filterElement04, filterElement05, filterElement06, hotline, intelligent, lamp, model, timing, ventilation |
| `2N8T` | 嘿码智能剃须刀BC8200 | BC8200 | 170 | status | AlarmMessage, CleanTime, CutterTime, Lock, Ota, Power, Speed, Version, WorkMode, WorkStatus, Worktime |
| `2NAA` | 永艺智能撑腰椅Flow 600 | Flow 600 | 2BA | battery | ChargeState, LongSitState, LongSitStop, RemindCout, RemindInterval, RemindTime, SetTimeIncrease, SitState, sedentaryReminder, sedentaryTime |
| `2NAB` | 永艺智能撑腰椅Act 280 | Act 280 | 2BA | battery | ChargeState, LongSitState, LongSitStop, RemindCout, RemindInterval, RemindTime, SetTimeIncrease, SitState, sedentaryReminder, sedentaryTime |
| `2NAC` | 永艺智能撑腰椅Act 260 | Act 260 | 2BA | battery | ChargeState, LongSitState, LongSitStop, RemindCout, RemindInterval, RemindTime, SetTimeIncrease, SitState, sedentaryReminder, sedentaryTime |
| `2NBO` | 根元托特包 | RS-TB001 | 143 | switch | LightingDelay, Mode, RemainingCapacity, RingLampBrightness, WorkTime, batteryState, leftTime, lightingState |
| `2NC3` | 梦百合0压智能床M3pro | M3pro | 14A | alarm | GetMemoryMode, Massageintensity, Relievestress, headControl, instructions, legControl, legMassage, massageMode, massageTimer, memoryControl1, memoryControl2, modeSelect, oneKeyReset, pause, runningstate |
| `2ND6` | 好孩子智能汽车安全座椅CS8100 | CS8100 | 0DF | battery | ISOFIXStatus, antiTipingLegsStatus, babyInStatus, beltStatus, calibrationSwitch, conttonpadStatus, currentTemperature, fanMode, fixedTemperature, fixedTemperatureWind, horizontalTurnStatus, noForget, seatRotation, seatTiltAction, welcomeDirection |
| `2ND9` | 小豚当家智能摄像头2 双频版 | XT-X10D | 008 | switch | alarmEvent, cruiseSwitch, logReport, pushStatus, shootSwitch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6, voip |
| `2NF5` | 吸顶式温湿度传感器 | MIR-TE01-PLC | 006 | humidity | heat, reportSetting, switchNightLight |
| `2NGD` | 新飞445L四门智能冰箱 | BCD-445WKQ8AT | 08A | childLockSwitch | faultDetection, freezeSwitch, freezer, intelligentSwitch, refrigerateSwitch, refrigerationRooClosed, refrigerator, transformingSetting |
| `2NGE` | 新飞450L对开门智能冰箱 | BCD-450WKQ9AT | 08A | childLockSwitch | faultDetection, freezeSwitch, freezer, intelligentSwitch, refrigerateSwitch, refrigerationRooClosed, refrigerator |
| `2NGF` | 新飞467L四门智能冰箱 | BCD-467WKQ8AT | 08A | childLockSwitch | faultDetection, freezeSwitch, freezer, intelligentSwitch, refrigerateSwitch, refrigerationRooClosed, refrigerator, transformingSetting |
| `2NGG` | 新飞467L四门变频冰箱 | BCD-467WKQ8CT | 08A | childLockSwitch | faultDetection, freezeSwitch, freezer, intelligentSwitch, refrigerateSwitch, refrigerationRooClosed, refrigerator, transformingSetting |
| `2NGH` | 新飞470L四门智能冰箱Pro | BCD-470WGQ8A-PRO | 08A | childLockSwitch | faultDetection, freezeSwitch, freezer, intelligentSwitch, refrigerateSwitch, refrigerationRooClosed, refrigerator, transformingSetting |
| `2NGI` | 新飞470L四门智能冰箱 | BCD-470WG8A | 08A | childLockSwitch | faultDetection, freezeSwitch, freezer, intelligentSwitch, refrigerateSwitch, refrigerationRooClosed, refrigerator, transformingSetting |
| `2NGK` | 新飞535L对开门智能冰箱 | BCD-535WKQ9AT | 08A | childLockSwitch | faultDetection, freezeSwitch, freezer, intelligentSwitch, refrigerateSwitch, refrigerationRooClosed, refrigerator |
| `2NGL` | 新飞615L对开门智能冰箱 | BCD-615WKQ9AT | 08A | childLockSwitch | faultDetection, freezeSwitch, freezer, intelligentSwitch, refrigerateSwitch, refrigerationRooClosed, refrigerator |
| `2NNO` | 正泰智能五孔插座 | NEW3-W53100D. | 1FC | switch | electric, faultDetection, indicator, memorySwitch, power |
| `2NPA` | 海雀智能摄像头3Pro 4K双频版 | AD08C M4 | 008 | switch | alarmEvent, areaFencing, cruiseSwitch, numberIdentification, shootSwitch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6, voip |
| `2NPB` | 海雀智能摄像头3Pro 4K 双频版 | AD08C M8 | 008 | switch | alarmEvent, shootSwitch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 |
| `2NPI` | 研森便携式咖啡机YK-0105C | YK-0105C | 0B9 | action | clean, commonFaultDetection, info, state, watertemp |
| `2NRQ` | 酷轻松石墨烯腰部支撑按摩器 | HA(Z)60-HMBDHW-01 | 0CA | mode | bleStatus, countdown, electricity, firmware, heating, inflation, inflationTime, lowpower, massage, remainTime, syncTime, workStatus |
| `2NVP` | 推拉窗HY | HC86TLY | 2BC | action | childLock, lock, windowOpener |
| `2NVQ` | 天窗HY | HC86TCY | 2BC | action | windowOpener |
| `2NXA` | Jeep智能剃须刀J1H | J1H | 170 | status | bleStatus, clean, cutterTime, electricity, faultDetection, speed, worktime |
| `2NXG` | SleeponeAi智能电动床 | 2123 | 14A | lightSwitch | backMassage, devStatus, headControl, legControl, legMassage, massageFrequency, modeSelect, oneKeyReset |
| `2NXN` | 美菱茶吧机MC-13BH | MC-13BH | 1A0 | status | ID256, ID257, ID258, ID259, ID260, ID261, ID262, ID263, ID264, ID266, ID272, ST110, ST20, faultDetection, status1, status2 |
| `2O2L` | 美菱茶吧机MC-13H | MC-13H | 1A0 | status | ID256, ID257, ID258, ID259, ID260, ID262, ID263, ID264, ID266, ID272, ST110, ST20, faultDetection, status1, status2 |
| `2O45` | 菠萝斑马智能床 | ELE1.0 | 14A | childLockSwitch | BackAngel, LegAngel, SnoringMonitor, memoryControl1, memoryControl2, memoryControl3, modeSelect, oneKeyReset |
| `2O62` | 哈尔斯智能水杯 G5 | HGM-450-008 | 06B | battery | config, currentTemperature, drinkDisturb, drinkRemind, healthRemind, waterDayIntake |
| `2O6X` | 霹雳仔智能运动包 | PZ-ZB001 | 143 | switch1 | LightingDelay, Mode, RemainingCapacity, RingLampBrightness, WorkTime, batteryState, leftTime, lightingState |
| `2O6Y` | 霹雳仔托特包 | PZ-ZB003 | 143 | switch1 | LightingDelay, Mode, RemainingCapacity, RingLampBrightness, WorkTime, batteryState, leftTime, lightingState |
| `2O8J` | 倍益康水杯式保健制氧机 | HAC6 | 0F0 | mode | batteryLevel, buttonSound, deviceVersion, fault, filterCotton, gear, molecular, oxygen, plain, pulse, shutDown, upgrade, workStatus, workTime |
| `2O91` | 小豚当家室外摄像头 3K升级版 | XT-H33C | 008 | switch | alarmEvent, cruiseSwitch, logReport, pushStatus, shootSwitch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 |
| `2O9K` | 海雀智能摄像头3i 3K版 64GB | AZ05G M4 | 008 | switch | logReport, shootSwitch, videoSwitch |
| `2O9R` | 华为悦彰家庭影院 | KPNG-00 | 2CA | brightness | acousticsAbility2, commonExecution, commonMode, commonMode1, commonMode2, playSource, stereo, stereoDeviceTest, volume |
| `2OAJ` | 海雀智能摄像头3i 3K版 128GB | AZ05G | 008 | switch | alarmEvent, cruiseSwitch, logReport, shootSwitch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 |
| `2OBE` | 海雀智能摄像头3i 3K版 32GB | AZ05G | 008 | switch | alarmEvent, cruiseSwitch, logReport, shootSwitch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 |
| `2OCP` | 若瀑负氧离子机H2 | HC.NAI.H2 | 013 | switch | airQuality, changefilter, commonFaultDetection, countdown, screen, totaltime |
| `2OD1` | 厨余垃圾处理器 | ELEMENT60 PRO | 0B6 | mode | EqGear, EqReversal, EqStart |
| `2ODW` | 涂趣智慧盒 | TH-LINK | 195 | switch | HifiKey, HifiScene, MUTE, MicVolume, Modeselect, MusicVolume, volume |
| `2OFW` | 安吉尔全屋大水量净水器J3539-ROC120 | J3539-ROC120 | 02D | switch | commonFaultDetection, dayPurifyWater, emptySwitch, filterElement1, filterElement2, filterElement3, inputTds |
| `2OFX` | 安吉尔净水器J3303-ROB60 | J3303-ROB60 | 02D | switch | commonFaultDetection, dayPurifyWater, emptySwitch, filterElement1, filterElement2, inputTds |
| `2OFY` | 安吉尔全屋Mini软水机S3561-F08 | S3561-F08 | 2B4 | mode | commonFaultDetection, dayWater, filterElement1, inputTds, outputTds, remainWater, rewaterTime, totalWater, waterPressure, waterSpeed |
| `2OI8` | 哈尔斯智能泡茶杯星闪版 | HTM-420-002/HGM-450-002 | 06B | battery | checkedTea, currentTemperature, customTeaList, drinkRemind, takeMedicineRemind |
| `2OK6` | 海雀智能摄像头3s 4K版 32GB | AZ08G | 008 | switch | alarmEvent, cruiseSwitch, logReport, shootSwitch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 |
| `2OKA` | 海雀智能摄像头3s 4K版 64GB | AZ08G | 008 | switch | alarmEvent, cruiseSwitch, logReport, shootSwitch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 |
| `2OKB` | 海雀智能摄像头3s 4K版 128GB | AZ08G | 008 | switch | alarmEvent, logReport, shootSwitch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 |
| `2ONM` | BOW折叠智能触控蓝牙键盘 | HB168 | 2C0 | battery | capsLock |
| `2OO5` | 璟睿UnitLink影音中控主机 | AVSC-AC5300 | 0BD | switch | interfaceControl, ktvCtrl, micMute, micVolume, mute, playControl, sceneEnable, sceneMode, soundMode, volume |
| `2OP8` | 唯妙智能影音控制主机全屋款 | TW500 | 0BD | switch | interfaceControl, micVolume, musicVolume, mute, playControl, soundMode, volume |
| `2OSI` | 神通猫筋膜枪 | JMQ001 | 0C5 | battery | countdown, overCurrentAlarm, timedShutdown, vibrationGear, workSwitch |
| `2OST` | 艾诺华智能猫砂盆 | WLZC-01 | 1A5 | alarm | clean, deviceStatus, empty, resetRoller |
| `2OU9` | 哈尔斯智能水杯 弹盖款2 | HGM-450-006 | 06B | battery | canvasConfig, canvasData1, canvasData2, canvasData3, canvasData4, canvasData5, config, darkWeekTarget, drinkDisturb, drinkRemind, drinkTarget, drinkWarn, drinkWeekTarget, healthRemind, waterDayIntake, waterHoursIntake |
| `2OV9` | 雅兰智能床AC-408 | AC-408 | 14A | lightSwitch | backControl, backLegControl, backMassage, devStatus, legControl, legMassage, lumbarControl, massageFrequency, modeSelect, oneKeyReset |
| `2OWH` | 小豚当家室外摄像头5 4K版 | XT-H34 | 008 | switch | alarmEvent, commonFaultDetection, logReport, pushStatus, shootSwitch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 |
| `2OXZ` | 海雀智能摄像头5i 3K版 32GB | AQ05 | 008 | switch | alarmEvent, cruiseSwitch, logReport, shootSwitch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6, voip |
| `2OY0` | 海雀智能摄像头5i 3K版 64GB | AQ05 | 008 | switch | alarmEvent, cruiseSwitch, logReport, shootSwitch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6, voip |
| `2OY2` | 海雀智能摄像头5i 3K版 128GB | AQ05 | 008 | switch | alarmEvent, cruiseSwitch, logReport, shootSwitch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6, voip |
| `2OZT` | 怡口牌S82ECM型软水机 | S82ECM | 2B4 | status | cleanTime, commonFaultDetection, dayWater, remainWater, totalWater, totalWorkTime, waterSpeed |
| `2OZV` | 怡口牌ERO162C型反渗透直饮水机 | ERO162C | 02D | status | commonFaultDetection, dayPurifyWater, filterElement1, filterElement2, totalPurifyWater, totalWorkTime |
| `2OZW` | 怡口牌EUF205-2型直饮净水机 | EUF205-2 | 02D | status | commonFaultDetection, dayPurifyWater, filterElement1, filterElement2, totalPurifyWater, totalWorkTime |
| `2P5P` | 怡口牌S82WHF型净水机 | S82WHF | 2B5 | status | cleanTime, commonFaultDetection, dayPurifyWater, totalPurifyWater, totalWorkTime, waterSpeed |
| `2P8F` | 良信智能断路器NDB5E-80 | NDB5E-80 | 211 | status | ctrl, curNeutral, electric, electricA, electricB, electricC, faultDetection, poles, rcFunction |
| `2PFB` | 元响智能音乐主机 | 520 | 0BD | switch | deviceStatus, interfaceControl, mute, playStatus, systemMode, volume |
| `2PH0` | VIDON威动影K一体机 | C3000 | 0BD | switch | deviceStatus, interfaceControl, micVolume, musicPlay, mute, playStatus, soundMode, systemMode, volume |
| `2PHY` | 海雀智能摄像头 雀蛋Max 64GB | AZ08H | 008 | switch | alarmEvent, cruiseSwitch, familiarFaceAlarm, funRecord, localMode, logReport, shootSwitch, strangerFaceAlarm, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6, voip |
| `2PI5` | 海雀智能摄像头 雀蛋Max 128GB | AZ08H | 008 | switch | alarmEvent, cruiseSwitch, logReport, shootSwitch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6, voip |
| `2PIC` | Core Max全景相机 | Core Max | 2C2 | mode | photo, video |
| `2PJM` | 哈尔斯智能咖啡杯 星闪版 | HGM-500-001/HTM-470-001 | 06B | battery | currentTemperature, waterDayIntake, waysOfDrinking |
| `2PON` | 海雀智能摄像头 双雀Max 128GB | AD310 | 008 | switch | alarmEvent, alarmEvent2, cruiseSwitch, cruiseSwitch2, logReport, shootSwitch, videoSwitch, visitPoint1, visitPoint10, visitPoint11, visitPoint12, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6, visitPoint7, visitPoint8, visitPoint9, voip |
| `2POO` | 海雀智能摄像头 双雀Max 64GB | AD310 | 008 | switch | alarmEvent, alarmEvent2, cruiseSwitch, cruiseSwitch2, logReport, shootSwitch, videoSwitch, visitPoint1, visitPoint10, visitPoint11, visitPoint12, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6, visitPoint7, visitPoint8, visitPoint9, voip |
| `2PRW` | 华歌智能影K功放CIC-MINI-7.2-MIC | CIC-MINI-7.2-MIC | 2C9 | switch | audioSelection, audioplayer, channelFine-tuning, channelTest, inputSource, mediaKey, micGain, reset, saveConfig, surroundMode, userConfig, volSwitch, volume |
| `2PRX` | 华歌智能影K功放CIC-MINI-5.1-MIC | CIC-MINI-5.1-MIC | 2C9 | switch | audioSelection, audioplayer, channelFine-tuning, channelTest, inputSource, mediaKey, micGain, reset, saveConfig, surroundMode, userConfig, volSwitch, volume |
| `2PUP` | 爱路德智能床GC888 | GC888 | 14A | lightSwitch | devStatus, headControl, headLegControl, headMassage, legControl, legMassage, massageMode, massageTimer, memoryControl1, memoryControl2, memoryControl3, oneKeyReset, positionFunction, runingMode, stopWorking, timingSetting |
| `2PV1` | 哈尔斯智能泡茶杯 星闪纯钛版 | HTM-420-002 | 06B | battery | checkedTea, currentTemperature, customTeaList |
| `2Q45` | 电亿秒智能插座 CH1 | CH1 | 01D | switch | electric, indicator, memorySwitch, power |
| `2QAP` | 智能儿童眼部按摩器 | ESaver X1 | 32A | mode | childlockSwitch, gear, globalVolume, hotcompressTemperature |
| `2QCU` | 小豚当家室外4G摄像头 3K版 | XT-H33D | 008 | switch | alarmEvent, commonFaultDetection, logReport, shootSwitch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 |
| `2QGA` | 小豚当家智能摄像头 鲸瞳Max | XT-H42 | 008 | switch | alarmEvent, commonFaultDetection, logReport, shootSwitch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 |
| `2QHO` | 海雀智能摄像头 雀蛋Pro 128GB | AZ08K | 008 | switch | alarmEvent, commonFaultDetection, cruiseSwitch, localMode, logReport, shootSwitch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6, voip |
| `2QHP` | 海雀智能摄像头 雀蛋Pro 64GB | AZ08K | 008 | switch | alarmEvent, commonFaultDetection, cruiseSwitch, localMode, logReport, shootSwitch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6, voip |
| `2QJV` | 奥马全嵌母婴冰箱520PLUS | BCD-520PLUS | 08A | status | commonFaultDetection, featureMode, flexiTempZone, freezeSwitch, freezerFloat, intelligentSwitch, refrigerateSwitch, refrigerationSwitch, refrigeratorFloat |
| `2QL4` | MEIPONT智能冰箱437(Pro) | BM437LWX(Pro) | 08A | status | commonFaultDetection, featureMode, flexiTempZone, freezeSwitch, freezerFloat, intelligentSwitch, refrigerateSwitch, refrigeratorFloat |
| `2QM9` | 华愈康AI智能睡眠舱 | KY-Starlink23 | 08C | status | bioenergySwitch, bloodOxygen, cellularSwitch, commonFaultDetection, controlAction, downLiveTemperature, downTemperature, hatchMode, heartRate, leftCountDown, lightGear, musicGear, suspendedSwitch, upLiveTemperature, upTemperature |
| `2QME` | 星飞菱投影幕吊架控制器 | SPC-03HW | 1B0 | action | backLight, travelCompensation, travelTime, workStatus |
| `2QQB` | BOW星闪触控折叠键盘 | HB416 | 2C0 | battery | capsLock, keyboardLock |
| `2QUA` | 恩仕AXENT线性浴霸 | A822-01 | 035 | status | autoWarmWindSwitch, automaticWarmWindSwitch, commonFaultDetection, drySwitch, leftTime, setWorkTime, swingSwitch, ventilateSwitch, windSwitch |
| `2QUH` | 奥马法式平嵌冰箱 | BCD-455PLUS | 08A | status | commonFaultDetection, featureMode, freezeSwitch, freezerFloat, intelligentSwitch, refrigerateSwitch, refrigeratorFloat |
| `2QUI` | 奥马全嵌母婴冰箱520阿尔卑斯白 | BCD-520WDPG/B | 08A | status | commonFaultDetection, featureMode, flexiTempZone, freezeSwitch, freezerFloat, intelligentSwitch, refrigerateSwitch, refrigerationSwitch, refrigeratorFloat |
| `2QUJ` | 奥马全嵌母婴冰箱508Pro | BCD-508Pro | 08A | status | commonFaultDetection, featureMode, flexiTempZone, freezeSwitch, freezerFloat, intelligentSwitch, refrigerateSwitch, refrigerationSwitch, refrigeratorFloat |
| `2QWE` | 智能门铃HY | H8 | 0F2 | switch | commonFaultDetection, irMode, overstayTime, toneMode, volume |
| `2QX3` | 冰虎车载冰箱 | MP8 | 187 | battery | childLock, commonFaultDetection, currentTemperature, gear, modeSelection, powerCon, powerMode, powerSwitch, targetTemperature |
| `2QXU` | 欧派克全景幕控制器 | A80-A90 | 1B0 | action | backLight, reminderSwitch, workStatus |
| `2QY4` | 尚美源牌QY-UF型超滤净水机 | QY-UF-2 | 02D | temperature | filterElement2, outputTds, totalPurifyWater |
| `2QZR` | 欧普单路开关执行器PLC | OP-CBX-IC-PLC-00 | 064 | switch | backup, buzzer, commonFaultDetection, indicator, memorySwitch |
| `2R0N` | 恩仕AXENT暗装电热毛巾架 | A820-0 | 0BA | status | commonFaultDetection, drying, dryingLeftTime, dryingTime, heat |
| `2R4K` | 海雀智能摄像头5s | AZ08L | 008 | switch | alarmEvent, commonFaultDetection, cruiseSwitch, logReport, shootSwitch, strangerFaceAlarm, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 |
| `2R9O` | 海雀智能摄像头5i 4K版 | AZ08M | 008 | switch | alarmEvent, commonFaultDetection, cruiseSwitch, logReport, shootSwitch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6, voip |
| `2RBD` | 小豚当家智能摄像头 鲸瞳4G版 | XT-H41 | 008 | switch | alarmEvent, commonFaultDetection, logReport, shootSwitch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 |
| `2RCO` | 名豆之约智能通断器 2代 | TDQ001 | 211 | switch | commonMemorySwitch, indicator, jogMode, timeSet |
| `2RCP` | 恩仕AXENT.NOVIA明装轻智能淋浴器 | F601-12 | 300 | status | coldWaterSwitch |
| `2RE4` | simon玻璃材质16A智能三孔插 | 58E8242G | 1FC | switch | commonFaultDetection, electric, indicator, memorySwitch, power |
| `2RE5` | simon玻璃材质10A智能五孔插 | 58E8241G | 1FC | switch | commonFaultDetection, electric, indicator, memorySwitch, power |
| `2RE6` | simon塑料材质16A智能三孔插 | 580E8242 | 1FC | switch | commonFaultDetection, electric, indicator, memorySwitch, power |
| `2RE7` | simon塑料材质10A智能五孔插 | 580E8241 | 1FC | switch | commonFaultDetection, electric, indicator, memorySwitch, power |
| `2RE8` | simon金属材质16A智能三孔插 | 58E8242M | 1FC | switch | commonFaultDetection, electric, indicator, memorySwitch, power |
| `2RE9` | simon金属材质10A智能五孔插 | 58E8241M | 1FC | switch | commonFaultDetection, electric, indicator, memorySwitch, power |
| `2RFH` | 海雀智能摄像头5 4K版 | AD08E | 008 | switch | alarmEvent, commonFaultDetection, cruiseSwitch, localMode, logReport, shootSwitch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6, voip |
| `2RHS` | 净水控制盒 Sinkfusion A01 | Sinkfusion A01 | 02D | status | commonFaultDetection, flushSwitch, outputTds, totalPurifyWater, waterSpeed |
| `2RHX` | 旭格平开窗驱动 | 263822 | 02C | action | bottomTravel, openStatus, switchSpeed, travel |
| `2RI3` | 欧普单路开关执行器WIFI | OP-CBX-IC-W-00 | 064 | switch | backup, buzzer, commonFaultDetection, indicator, memorySwitch |
| `2RJ1` | 海雀智能摄像头雀蛋 | AZ08N | 008 | switch | alarmEvent, commonFaultDetection, cruiseSwitch, localMode, logReport, shootSwitch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6, voip |
| `2RJ2` | 宝褓620精控床垫 | CDS21-C | 068 | childLockSwitch | commonFaultDetection, leftSoftHardness, memoryControl1, memoryControl2, memoryControl4, memoryControl5, memoryControl6, modeSelect, pause, rightSoftHardness, sleepstatus |
| `2RJ9` | 贝克巴斯超级感应净水龙头 | F02 | 310 | switch | commonFaultDetection, faucetElement, inductionSwitch, outletWater, outletWater1, outputTds, waterSwitch |
| `2RKZ` | 恩仕AXENT暗装电热浴巾架 | A821-0 | 0BA | status | commonFaultDetection, drying, dryingLeftTime, dryingTime, heat |
| `2RL8` | 海雀智能门铃5 | APZ36 | 0F2 | battery | alarmEvent, commonFaultDetection, voip |
| `2RLB` | 海雀智能门铃5Max | APX39 | 0F2 | battery | alarmEvent, commonFaultDetection, voip |
| `2RM8` | 便携移动冰箱(车家两用) | HMZY-CRE-001 | 187 | battery | childLock, commonFaultDetection, currentTemperature, deviceStatus, gear, modeSelection, powerCon, powerSwitch, targetTemperature |
| `2RMS` | 西顿照明T5无线地脚灯 | SWBH-DJD | 21F | switch | nightLightMode |
| `2RNH` | 海雀双雀Pro摄像头 | AE310 | 008 | switch | alarmEvent, alarmEvent2, commonFaultDetection, cruiseSwitch, cruiseSwitch2, localMode, logReport, shootSwitch, videoSwitch, visitPoint1, visitPoint10, visitPoint11, visitPoint12, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6, visitPoint7, visitPoint8, visitPoint9, voip |
| `2RPW` | 大疆云台Osmo Mobile 9 | OM9 | 0EC | battery | commonFaultDetection |
| `2RRO` | 小豚当家智能摄像头 鲸瞳 | XT-H43 | 008 | switch | alarmEvent, commonFaultDetection, logReport, shootSwitch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 |
| `2RUX` | 车载香氛机 | XH-010 | 0DE | switch | autoConnect, commonFaultDetection, filterElement, filterElement02, filterElement03, gear, scent |
| `2RXX` | 海雀智能摄像头5Pro 4K全场景版 | AZ08E | 008 | switch | alarmEvent, commonFaultDetection, cruiseSwitch, logReport, shootSwitch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6, voip |
| `2RY8` | 良信智能断路器NDB5EL-80 | NDB5EL-80 | 211 | status | ctrl, curNeutral, electric, electricA, electricB, electricC, faultDetection, poles, rcFunction |
| `2RZA` | 海雀智能摄像头 雀蛋S | AZ08Q | 008 | switch | alarmEvent, commonFaultDetection, cruiseSwitch, logReport, shootSwitch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6, voip |
| `2S0N` | 鸿蒙智选 桌面精灵 | T1 | 158 | switch | commonFaultDetection |
| `2S2G` | 佳普乐宏尚智联毛巾架 | TH1HS-02G | 0BA | status | disinfect, drying, dryingLeftTime, dryingTime, heat, indicator, nightlightSwitch |
| `2S5N` | 奥马智能冰箱五门零嵌 | BCD-466WFRMZ/B | 08A | status | commonFaultDetection, ecoMode, flexiTempZone, freezeSwitch, freezerGear, fridgeGear, iceMode |
| `2S77` | 丝涟智眠智能床 | Auto Dream | 14A | lightSwitch | headControl, legControl, massGear, massageMode, massageTimer, modeSelect, oneKeyReset, pause |
| `2S8M` | 良信智能断路器NDB5E-40 | NDB5E-40 | 211 | status | ctrl, curNeutral, electric, electricA, electricB, electricC, faultDetection, poles, rcFunction |
| `2S8N` | 良信智能断路器NDB5EL-40 | NDB5EL-40 | 211 | status | ctrl, curNeutral, electric, electricA, electricB, electricC, faultDetection, poles, rcFunction |
| `2SB5` | 小豚当家智能摄像头6 4K | XT-H35 | 008 | switch | alarmEvent, commonFaultDetection, logReport, shootSwitch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 |
| `2SB7` | 小豚当家智能摄像头6 Pro 双摄 | XT-H45 | 008 | switch | alarmEvent, commonFaultDetection, logReport, shootSwitch, videoSwitch, visitPoint1, visitPoint2, visitPoint3, visitPoint4, visitPoint5, visitPoint6 |
| `9MTM` | 智控压力传感器 | haTest4 | 1F1 | alarmBell | — |
| `9MTV` | 智控灭蚊器 | haTest6 | 0B0 | switch | — |
| `9MTX` | 智控断路器 | haTest8 | 211 | switch | electric |
| `9MZR` | 智控微波炉 | haTest | 023 | status | microWave |
| `A001` | 古北WiFi智能插座 | SP mini 3-JD | 01D | switch | timerID |
| `A065` | 长虹电视 | KA5 | 013 | switch | volSwitch |
| `A073` | 美的智能电饭煲 | BG-R1 | 026 | status | — |
| `A07B` | TCL智能电视 | Z6 | 02E | switch | volSwitch |
| `A08L` | 美的智能冰箱 | BCD-609WKGPZM(E) | 08A | switch | freezeSwitch, freezer, intelligentSwitch, refrigerateSwitch, refrigerator |
| `A091` | 博世冰箱 | KFN86A246C | 012 | switch | faultDetection, freezeSwitch, freezer, refrigerateSwitch, refrigerator |
| `A094` | 创维电视 | Q80 | 02E | switch | volSwitch |
| `A0D8` | 康佳智能电视 | led55m1 | 02E | switch | channel, sigInterface, volSwitch, volume |
| `A0DO` | 插座 | SMARTPLUG | 01D | switch | — |
| `A0EQ` | 布谷智能扫拖机器人 | BG-C3 | 031 | status | — |
| `A0GO` | 智能便座 | 3435 | 066 | switch | — |
| `A0GP` | 智能便座PL40 | PL40 | 066 | switch | — |
| `A0GR` | 蒸烤箱 | SC88J | 022 | status | gateSwitch, hotStatus, preStatus, remoteSwitch |
| `A0MC` | 智汇云智能开关 | switch001 | 005 | switch | — |
| `A0N8` | 智汇云智能插座 | socket001 | 01D | switch | — |
| `A0NN` | 智能单通道插座 | Smart socket | 01D | switch | — |
| `A0NV` | 智能窗帘 | Smart curtain | 01C | opener | — |
| `A0OP` | 智能单通道开关 | Smart wall switch | 005 | switch | — |
| `A0SQ` | 美的净水机 | MRO1787D-1000G | 02D | status | faultDetection, filterElement1, filterElement2, inputTds, outputTds, purifyWater, rinseSwitch |
| `A0UB` | 霍尼韦尔智能控制灯光 | HWlight01 | 01B | switch | — |
| `A104` | 阿尔法蛋故事机Z1 | TYZ1 | 08D | switch | L1201, L3901, L701, L803, L901, LS202, musicPlay, volume |
| `A108` | 西门子三孔插座1 | 5UB71117NC | 01D | switch | — |
| `A10E` | 九阳破壁机 | L12-Y521 | 0D2 | status | cleanMode, commonFaultDetection, cupWarn, leftTimes, start, stop |
| `A10T` | 西门子五孔插座1 | 5UB71112NC | 01D | switch | — |
| `A10U` | 西门子五孔插座1 | 5UB71115NC | 01D | switch | — |
| `A11T` | 九阳蒸汽饭煲 | F-S5 | 026 | status | clean, commonFaultDetection, continue, leftTimes, pause, start, startCloud, stop |
| `A14C` | 九阳高速破壁调理机 | L18-P156 | 0D2 | status | clean, commonFaultDetection, leftTimes, like, start, startCloud, stop, warmTime |
| `A15V` | 美的管线机 | CWG-DA01 | 02D | status | germicidalDuration, germicidalSwitch, outlet, water |
| `A1BJ` | 美的MRO899-1500橱下式净水机 | MRO899-1500 | 02D | status | faultDetection, filterElement1, heatSwitch, purifiedWaterTDS, rawWaterTDS, rinseSwitch, water |
| `A1FS` | 九阳无涂层蒸汽电饭煲 | F40S-S710(HM) | 026 | status | clean, devStatus, pauseContinue, start, stop |
| `A1H6` | 九阳智能养生壶 | K15D-WY520(HM) | 060 | status | devStatus, faultDetection, resetHoldingTemperature, start, stop, warmDuration |
| `A1KV` | 九阳铁釜IH电饭煲 | F-40TD01(HM) | 026 | status | commonFaultDetection, progress, remainingTime, start, startCloud, stop |
| `A1L9` | 九阳IH炭钢釜液晶智能电饭煲 | F40C-F981 | 026 | status | commonFaultDetection, lastFuncCode, leftTime, progress, start, stop |
| `A1RQ` | 美的CXW-260-B87抽油烟机 | CXW-260-B87 | 021 | switch | faultDetection, gear |
| `A1SI` | COLMO橱下式净水机CWRC800-B139 | CWRC800-B139 | 02D | status | faultDetection, filterElement1, filterElement2, purifiedWaterTDS, rawWaterTDS, rinseSwitch |
| `A1SV` | 不用手洗多功能破壁机 | L12-Y521 | 0D2 | status | clean, commonFaultDetection, commonMenu, currentCapacity, currentFuncCode, startHealth, stop |
| `A1W2` | 九阳无涂层蒸汽电饭煲 | F-S3(HM) | 026 | status | clean, commonFaultDetection, pauseContinue, progress, remainingTime, riceCup, start, stop |
| `A1WN` | 九阳免手洗破壁机L12-Y951 | L12-Y951 | 0D2 | status | devStatus, finshReport, start, stop |
| `A2D8` | COLMO橱下式净水机CWRC800-B106 | CWRC800-B106 | 02D | status | faultDetection, filterElement1, filterElement2, rinseSwitch |
| `A2EE` | 净水器 JYW-R782 | JYW-R782 | 02D | status | commonFaultDetection, filterElementDataPcp, filterElementDataRoc, resetData |
| `A2FS` | FC9 OS洗地机 | FC9 OS | 19F | status | batteryRatio, controlVoice, plugStatus, runMode, selfcleanswicth |
| `A2JK` | 智能单通道机械开关 | Smart Switch | 005 | switch | — |
| `A2JN` | ZB单通道开关 | ZB Smart Switch | 005 | switch | — |
| `A2JO` | 恒温恒湿智能开关 | TempHumid Smart Switch | 005 | switch | — |
| `A2K1` | CT-UNITE 智能物联网水表 | ZKTX-15W | 0DA | battery | waterMeterReading |
| `A2K7` | 净热一体式反渗透净水机 JYW-RF689s | JYW-RF689s | 02D | status | commonFaultDetection, filterElement, offOn, resetData, waterPattern |
| `A2L4` | 智汇云智能开关 | ZHY-Q1001 | 005 | switch | — |
| `A2L6` | 智汇云智能空开 | ZHY-KC001 | 211 | switch | devStatus, kwh, limit |
| `A2M0` | 智汇云烟雾传感器 | ZHY-HK004 | 039 | alarm | alert, remove, temperAlarm |
| `A2M5` | 智汇云窗帘模块 | ZHY-WK001 | 1FE | action | — |
| `A2ML` | 厦讯科技智能水表 | KEN-SU30 | 0DA | status | waterConsumptionForYesterday, waterMeterReading |
| `A2N2` | KEKEN 智能开关1键 | KEN-KK901 | 005 | switch1 | backlight2 |
| `A2P7` | KEKEN 商业锁F20 | KEN-F20 | 04B | battery | ROOM, lockMode, lockState, lockStatus |
| `A2PS` | 脉冲式蓝牙热水表DN25 | AMC-MCBL-H-DN25 | 0DA | status | waterConsumptionForYesterday, waterMeterReading |
| `A2PT` | 脉冲式蓝牙热水表DN20 | AMC-MCBL-H-DN20 | 0DA | status | waterConsumptionForYesterday, waterMeterReading |
| `A2PV` | KEKEN 商业锁P10 | KEN-P10 | 04B | battery | ROOM, lockMode, lockState, lockStatus |
| `A2PW` | KEKEN 商业锁P20 | KEN-P20 | 04B | battery | ROOM, lockMode, lockState, lockStatus |
| `A2QK` | 脉冲式蓝牙水表DN20 | AMC-MCBL-DN20 | 0DA | status | waterConsumptionForYesterday, waterMeterReading |
| `A2QL` | 脉冲式NB水表DN15 | AMC-MCNB-DN15 | 0DA | status | waterConsumptionForYesterday, waterMeterReading |
| `A2QM` | 脉冲式NB水表DN25 | AMC-MCNB-DN25 | 0DA | status | waterConsumptionForYesterday, waterMeterReading |
| `A2QN` | 脉冲式NB水表DN20 | AMC-MCNB-DN20 | 0DA | status | waterConsumptionForYesterday, waterMeterReading |
| `A2QO` | 光电直读水表DN15 | AMC-GDZD-DN15 | 0DA | status | waterConsumptionForYesterday, waterMeterReading |
| `A2QP` | 光电直读水表DN20 | AMC-GDZD-DN20 | 0DA | status | waterConsumptionForYesterday, waterMeterReading |
| `A2QQ` | 光电直读水表DN25 | AMC-GDZD-DN25 | 0DA | status | waterConsumptionForYesterday, waterMeterReading |
| `A2QT` | 脉冲式蓝牙水表DN25 | AMC-MCBL-DN25 | 0DA | status | waterConsumptionForYesterday, waterMeterReading |
| `A2QW` | NB大口径水表 | AMC-NBCS-DB | 0DA | status | waterConsumptionForYesterday, waterMeterReading |
| `A2QX` | 光电直读大口径水表 | AMC-GDZD-DB | 0DA | status | waterConsumptionForYesterday, waterMeterReading |
| `A2QY` | 脉冲式蓝牙热水表DN15 | AMC-MCBL-H-DN15 | 0DA | status | waterConsumptionForYesterday, waterMeterReading |
| `A2QZ` | 脉冲式NB热水表DN15 | AMC-MCNB-H-DN15 | 0DA | status | waterConsumptionForYesterday, waterMeterReading |
| `A2R0` | 光电直读热水表DN15 | AMC-GDZD-H-DN15 | 0DA | status | waterConsumptionForYesterday, waterMeterReading |
| `A2R1` | 脉冲式NB热水表DN20 | AMC-MCNB-H-DN20 | 0DA | status | waterConsumptionForYesterday, waterMeterReading |
| `A2R2` | 脉冲式NB热水表DN25 | AMC-MCNB-H-DN25 | 0DA | status | waterConsumptionForYesterday, waterMeterReading |
| `A2R3` | 光电直读热水表DN20 | AMC-GDZD-H-DN20 | 0DA | status | waterConsumptionForYesterday, waterMeterReading |
| `A2R4` | 光电直读热水表DN25 | AMC-GDZD-H-DN25 | 0DA | status | waterConsumptionForYesterday, waterMeterReading |
| `A2R8` | NB大口径热水表 | AMC-NBCS-H-DB | 0DA | status | waterConsumptionForYesterday, waterMeterReading |
| `A2R9` | 光电直读大口径热水表 | AMC-GDZD-H-DB | 0DA | status | waterConsumptionForYesterday, waterMeterReading |
| `A2RT` | 博芬智能酒柜BF1900 | BF1900 | 0FE | temperature | number |
| `A2TN` | 脉冲式蓝牙水表DN15 | AMC-MCBL-DN15 | 0DA | status | waterConsumptionForYesterday, waterMeterReading |
| `A2TV` | 智汇云摄像头 | ZHY-CS49 | 008 | switch | alarmEvent, push, shootSwitch, videoSwitch |
| `A2U3` | 14QC1i燃气壁挂炉 | LL1GBQ24-14QC1i | 174 | switch | bathTemp, eneMode, faultDetection, heatSwitch, heatTemp, iwaterTmp, totalGas, totalWater |
| `A2UA` | COLMO净水CWHO-RB117 | CWHO-RB117 | 02D | status | faultDetection, filterElement1, heatSwitch, outputTds, rinseSwitch |
| `A2WB` | 智汇云智能开关 | ZHY-MGK1003 | 211 | switch | — |
| `A2WK` | 智汇云智能开关 | ZHY-GWK1C003 | 211 | switch | — |
| `A2WL` | 智汇云智能开关 | ZHY-MGA1003 | 211 | switch | — |
| `A2WM` | 智汇云轨道式开关 | ZHY-RS001 | 211 | switch | — |
| `A36B` | 欧派智能一位开关P31 | OP-PLCS-RKRC-1 | 064 | switch1 | — |
| `A3CU` | COLMO净水器 | CWRC600-A106 | 02D | status | commonFaultDetection, outputTds, rinseMode |
| `A3CW` | COLMO管线机 | CWG-DA01 | 2B3 | childLockSwitch | commonFaultDetection |
| `A3CX` | COLMO中央净水器 | CWJ-C133 | 2B5 | status | commonFaultDetection, rinseMode, waterSpeed |
| `A3CY` | COLMO前置过滤器 | CWQZ-A36S | 312 | status | commonFaultDetection, rinseMode, waterSpeed |
| `A3D6` | 美的管线机 | MG908-R | 2B3 | childLockSwitch | commonFaultDetection |
| `A3D9` | 美的中央净水器 | MC802-1.5T | 2B5 | status | commonFaultDetection, rinseMode, waterSpeed |
| `A3DB` | 美的净水器 | MRC1975-1000G | 02D | status | commonFaultDetection, outputTds |
| `A3DC` | 美的茶吧机 | YR1629S-X | 06F | status | commonFaultDetection |
| `A3DD` | 美的净水器 | MRO1790B-400G | 02D | status | commonFaultDetection, rinseMode |
| `A3DH` | 美的净饮机 | JR2183T-RO | 02D | status | commonFaultDetection |
| `A3DL` | 美的饮水机 | MKR001 | 06F | childLockSwitch | commonFaultDetection |
| `A3E5` | 方太智能净水机 | YCZ-JT2000-02-HR7 | 02D | status | cleanTime, commonFaultDetection, filterElement2, filterElement3, rinseMode |
| `A3EU` | 方太智能灶蒸烤烹饪机 | JZT/Y-ZK60-X20.i | 0D4 | temperature | SteamOvenLight, SteamOvenMode, SteamOvenWorkStatus, SteamOvenWorkTime, commonFaultDetection, gestureSwitch, kitchenVentRemainingTime, kitchenVentSteaming, kitchenVentilatorGear, powerSwitch, totalWaterShortageStatus, workBurnerStatus |
| `A3FB` | 美的净水器 | MRO966-R | 02D | status | commonFaultDetection, heatSwitch |
| `A3FG` | 美的蒸烤一体机 | GR6 | 19B | status | commonFaultDetection, leftTime, ovenSteamer |
| `A3HB` | 格力新风净化机 | FHG-D1.5DA | 2FB | switch | freshAirSpeed |
| `A3HC` | 格力新风净化机(60a3) | FHBQGKWL-D1.5DB | 2FB | switch | freshAirSpeed |
| `A3IK` | 倍世中央净水机 | BWF-CN1301CU1 | 2B5 | status | cleanTime, flushSwitch, rinseMode |
| `A3IO` | 倍世厨下净水机 | BWRO-400GC1U1 | 02D | status | filterElement1, filterElement2, flushSwitch |
| `A3JA` | 美诺智能冰箱 | KF 2901 Vi | 08A | status | commonFaultDetection, freezeSwitch, freezerFloat, refrigerateSwitch, refrigeratorFloat |
| `A3JQ` | COLMO冰箱CRBUS601X1 | CRBUS601-X1 | 08A | status | aiSwitch, commonFaultDetection, disinfectSwitch, featureMode, freezerFloat, freshTemperature, iceMode, refrigerateSwitch, refrigeratorFloat |
| `A3K1` | COLMO冰箱CRBUS531FDA6 | CRBUS531FD-A6 | 08A | status | aiVersatileCabin, commonFaultDetection, disinfectSwitch, freezeSwitch, freezerFloat, iceMode, refrigerateSwitch, refrigeratorFloat |
| `A3KP` | 美诺智能冷藏箱 | KS 7743 E C | 08A | status | commonFaultDetection, refrigerateSwitch, refrigeratorFloat |
| `A3KQ` | 美诺智能冷冻箱 | FNS 7740 F C | 08A | status | commonFaultDetection, freezeSwitch, freezerFloat |
| `A3LI` | A.O.史密斯软水机 | S15D1 | 2B4 | status | cleanTime, commonFaultDetection, filterElement1, regenerateSwitch, totalWater, waterSpeed |
| `A3LP` | A.O.史密斯中央净水器 | WF10D1 | 2B5 | status | cleanTime, commonFaultDetection, filterElement1, flushSwitch, totalPurifyWater, waterSpeed |
| `A3NP` | 九阳智能全自动破壁机器人 | Y8 | 0D2 | status | blender, commonFaultDetection, cupStatus, leftTime |
| `A3OP` | 美的智能饭煲 | MB-HS412 | 026 | status | commonFaultDetection, cooker, leftTime |
| `A3PQ` | 箭牌智能浴室柜QN-PRO | QN-PRO | 301 | childLockSwitch | ambientLight, demisterSwitch, indicator, lightSwitcht, makeupLightGear, sensorDistanceGear, sensorLightGear |
| `A3RM` | 九阳变频轻音破壁机B7 | B7 | 0D2 | status | blender, commonFaultDetection, cupStatus, leftTime |
| `A3RN` | 九阳变频轻音破壁机B5 | B5 | 0D2 | status | blender, commonFaultDetection, cupStatus, leftTime |
| `A3RR` | 九阳变频破壁机PB-UL5B8P | PB-UL5B8P | 0D2 | status | blender, commonFaultDetection, cupStatus, leftTime |
| `A3RY` | 安吉尔J3402-ROB120H | J3402-ROB120H | 02D | switch | commonFaultDetection, filterElement1, filterElement2, flushSwitch, water |
| `A3SA` | 嘉格纳 冰箱 | RB492303 | 08A | status | commonFaultDetection, freezeSwitch, freezerFloat, refrigerateSwitch, refrigeratorFloat |
| `A3SK` | 九阳变频破壁机PB-UL5B80 | PB-UL5B80 | 0D2 | status | blender, commonFaultDetection, cupStatus, leftTime |
| `A3SY` | 美的燃气壁挂炉尊享ML1II | LL1PBD24-ML1 II | 174 | switch | aIWarmSwitch, bathStatus, bathTemperature, commonFaultDetection, ecoSwitch, heatStatus, heatSwitch, heatTemperature, hotWaterPressure, hotWaterSwitch, instantHeatSwitch |
| `A3T1` | 美的燃气壁挂炉畅享MC2GII | L1PB20-MC2GII | 174 | switch | antifreezeStatus, bathStatus, bathTemperature, commonFaultDetection, ecoSwitch, heatStatus, heatSwitch, heatTemperature, hotWaterPressure |
| `A3T2` | 美的燃气壁挂炉畅享MC2II | L1PB20-MC2II | 174 | switch | aIWarmSwitch, bathStatus, bathTemperature, commonFaultDetection, ecoSwitch, heatStatus, heatSwitch, heatTemperature, hotWaterPressure, hotWaterSwitch |
| `A3TA` | 西门子 冰箱 | KI86NHFD0C | 08A | status | commonFaultDetection, freezeSwitch, freezerFloat, refrigerateSwitch, refrigeratorFloat |
| `A3TH` | 博世 冰箱 | KIN86HFD0C | 08A | status | commonFaultDetection, freezeSwitch, freezerFloat, refrigerateSwitch, refrigeratorFloat |
| `A3V9` | 箭牌智联浴霸AQW11838 | AQW11838-R-AM | 035 | lightSwitch | autoWarmWindSwitch, circulationTime, drySwitch, heat, nightLightSwitch, sterilizationSwitch, swingSwitch, ventilateGear, ventilateSwitch, windMode, windSwitch |
| `A3VV` | 箭牌智联浴室柜XL | XL | 301 | childLockSwitch | ambientLight, demisterSwitch, indicator, lightSwitcht, makeupLightGear, sensorDistanceGear, sensorLightGear |
| `A3W1` | 嘉格纳Vario 400 系列酒柜45.7cm | RW414364 | 0FE | temperature | bottomShelftemp, commonFaultDetection |
| `A3X9` | 安吉尔S7 800 | J3669-ROC120 | 02D | switch | commonFaultDetection, filterElement1, filterElement2, flushSwitch, water |
| `A3XT` | 安吉尔 E-Tech鲜热一体机 | J3406-ROC90H | 02D | switch | commonFaultDetection, filterElement1, filterElement2, flushSwitch, water |
| `A3XU` | 安吉尔 M5 600 | J3402-ROB90 | 02D | switch | commonFaultDetection, filterElement1, flushSwitch, water |
| `A3XV` | 安吉尔 M7 Home Pro 800(末端) | J3540-ROC120H | 02D | switch | commonFaultDetection, filterElement1, filterElement2, flushSwitch, water |
| `A3XW` | 安吉尔 Q7 1000 | J3749-ROC150 | 02D | switch | commonFaultDetection, filterElement1, filterElement2, flushSwitch, water |
| `A3XX` | 安吉尔 Q3 600 | J3745-ROC90 | 02D | switch | commonFaultDetection, filterElement1, filterElement2, flushSwitch, water |
| `A3YA` | 安吉尔M7 Home Pro 800(预处理) | J3540-ACF4000 | 2B5 | switch | commonFaultDetection, filterElement1, filterElement2, totalPurifyWater |
| `A3YC` | 安吉尔M7 Home 800(预处理) | J3539-ACF4000 | 2B5 | switch | commonFaultDetection, filterElement1, filterElement2, totalPurifyWater |
| `A408` | 卡萨帝冰箱BCD-520WGCFDM4WKU1 | BCD-520WGCFDM4WKU1 | 08A | switch | aiFfSwitch, commonFaultDetection, freezeSwitch, freezerFloat, refrigeratorFloat |
| `A409` | 卡萨帝冰箱BCD-562WGCFDM4DUU1 | BCD-562WGCFDM4DUU1 | 08A | switch | aiFfSwitch, commonFaultDetection, freezerFloat, refrigeratorFloat |
| `A40O` | 九阳不用手洗破壁机Y9 | Y9 | 0D2 | status | blender, commonFaultDetection, cupStatus, leftTime |
| `A40R` | TCL冰箱标准款 | R510T9-UQS | 08A | childLockSwitch | freezeSwitch, freezerFloat, refrigerateSwitch, refrigerationSwitch, refrigeratorFloat |
| `A41C` | 九阳变频轻音破壁机B5-B | B5-B | 0D2 | status | blender, commonFaultDetection, cupStatus, leftTime |
| `A41X` | 安吉尔集成设备(末端)H3770-R2 a | H3770-R2 a | 02D | switch | commonFaultDetection, filterElement1, filterElement2, flushSwitch, water |
| `A41Y` | 安吉尔集成设备(末端)H3770-R2 b | H3770-R2 b | 02D | switch | commonFaultDetection, filterElement1, filterElement2, flushSwitch, water |
| `A44Y` | 欧瑞博地暖 | MS-HVAC-FH | 2FD | switch | commonFaultDetection, heat |
| `K1C7` | 华为路由TC7206 | TC7206-10 | 001 | switch | — |
| `K1C8` | 华为移动路由Pro | B535-836 | 061 | switch | — |
| `K1D5` | 华为随行WiFi 3 Pro | E5783-836 | 061 | switch | — |
| `K1D6` | 华为随行WiFi 3 | E5576-820 | 061 | switch | — |
| `K1D7` | 华为全屋智能 智能主机 EZ（网线版） | Medusa-BR80E-10 | 001 | switch | — |
| `K1DL` | 5G CPE 5 | H155-381 | 061 | switch | — |
| `K1EU` | 随行WiFi | E5576-325 | 061 | switch | — |
| `K1F5` | HUAWEI 4G CPE 5 | B636-336 | 061 | switch | — |
| `K1F6` | HUAWEI 4G CPE 5 | B636-536 | 061 | switch | — |
| `K1F7` | HUAWEI CPE 5R | H151-370 | 061 | switch | — |
| `K1FF` | 华为随行WiFi 5 | E5586-822 | 061 | switch | — |
| `K1FN` | 华为随行WiFi 5 | E5586-822 | 061 | switch | — |
| `K1FO` | HUAWEI 4G Mobile WiFi 5 | E5586-822 | 061 | switch | — |
| `K1FV` | 5G Mobile WiFi Pro 5 | E6888-982 | 061 | switch | — |
| `K1FX` | 华为全屋智能 分布式路由 M1 子路由 | WS8502-12 | 001 | switch | — |
| `K1GA` | 华为随行WiFi 5 eSIM | E5586-822-E | 061 | switch | — |
| `M0B5` | HUAWEI WATCH Buds | SGA-B19 | 06D | switch | — |
| `M0BW` | HUAWEI WATCH GT Cyber | AND-B19 | 06D | switch | — |
| `M0C5` | HUAWEI WATCH GT Cyber | AND-B19 | 06D | switch | — |
| `M0C6` | HUAWEI WATCH GT Cyber | AND-B19 | 06D | switch | — |
| `RX01` | HUAWEI 蓝牙鼠标 | CD23 | A06 | switch | — |
| `RX08` | HUAWEI 无线鼠标 | CD26 | A06 | switch | — |
| `RX09` | HUAWEI 蓝牙鼠标 第二代 | CD23 SE | A06 | switch | — |
| `RX0A` | HUAWEI 蓝牙鼠标 第二代 | CD26 SE | A06 | switch | — |
| `RX0G` | HUAWEI 高键程智能键盘 | CD34 | A05 | switch | — |
| `RX1B` | HUAWEI 蓝牙鼠标 第二代 | CD23-RA | A06 | switch | — |
| `RX1C` | HUAWEI 无线鼠标 第二代 | CD26-R | A06 | switch | — |
| `RX1E` | 华为星芒鼠标 | CD28-S | A06 | switch | — |
| `RX1G` | 华为星跃鼠标 GT | CD28 | A06 | switch | — |
| `RX1L` | 华为星跃鼠标 SE版本 | CD23SE-R | A06 | switch | — |
| `RX1M` | 华为星跃鼠标 SE悦享版 | CD20-R | A06 | switch | — |
| `RX1N` | TBD | Zhujiang-CD23M | A06 | switch | — |
| `RX1O` | TBD | Huaihe-CD26M | A06 | switch | — |
| `RX1P` | TBD | Huaihe-CD26K | A06 | switch | — |
| `RX1X` | TBD | Nujiang-CD23SEG | A06 | switch | — |
| `RX1Y` | TBD | CD20-RZ | A06 | switch | — |
| `RX21` | TBD | Nujiang-CD23SEPU | A06 | switch | — |
| `RX24` | TBD | Huaihe-CD26MA | A06 | switch | — |
| `T100` | HUAWEI MateView | HSN-CBA | A02 | brightness | deviceMgr, mic, protectEye, volume, whiteList |
| `V0EJ` | 虚拟电子白板 | VWB-1 | A01 | switch | inputSource |
| `V0EK` | 虚拟智慧屏 | VTV-1 | A01 | switch | volume |
| `ZCA2` | AI眼镜 | AIL-G01 | A31 | battery | — |
| `ZF01` | 华为全屋智能 智能主机 | ROM-HC00 | A0A | switch | clickedScene, devOta |
| `ZF02` | 华为全屋智能 智能主机 | ROM-HC01 | A0A | switch | clickedScene, devOta |
| `ZF0B` | 华为全屋智能 智能主机SE | LDN-C00 | A0A | switch | clickedScene, devOta |
| `ZF0C` | 华为全屋智能 智能主机SE | LDN-C01 | A0A | switch | clickedScene, devOta |
| `ZF0H` | 华为全屋智能 智能中控屏S2 | HCP23-S10 | A10 | battery | addDevice, assistant, blueBroadcast, cameraSwitch, communication, devList, discovery, faceEntryAuthorization, homeBroadcast, logReport, micSwitch, panelMode, panelStatus, recoverConfigSwitch, speakerIfttt, undisturbMode, volSwitch |
| `ZF0J` | 华为全屋智能 智能主机 Lite | LDN-C02 | A0A | switch | — |
| `ZF0M` | 华为鸿蒙智家 智能主机 X2 Pro | SSH-HC25 | A0A | switch | clickedScene, devOta |
| `ZF0N` | 华为鸿蒙智家 智能主机 X2 Pro | SSH-HCB25 | A0A | switch | clickedScene, devOta |
| `ZF0Q` | 华为鸿蒙智家 智能主机 EZ 2 | SSH-WHC25-AIR | A0A | switch | devOta |
| `ZF0R` | 华为鸿蒙智家 智能主机 X2 | SSH-HC25LT | A0A | switch | clickedScene, devOta |
| `ZG0R` | 吊灯 | Pendant Lamp | A1A | switch | — |
| `ZG0S` | 智能照明 | Lamp | A1B | switch | — |
| `ZG0T` | 床头灯 | Sleeping Lamp | A1C | switch | — |
| `ZG0U` | 磁吸灯 | Magnetic Suction Lamp | A1D | switch | — |
| `ZG0V` | 灯带 | Light Belt | A1E | switch | — |
| `ZG0W` | 射灯 | Spot Lamp | A1F | switch | — |
| `ZG0X` | 筒灯 | Spotlight | A20 | switch | — |
| `ZG0Y` | 吸顶灯 | CeilingLamp | A21 | switch | — |
| `ZG1A` | 红外幕帘传感器 | HDC-PIRS01 | A28 | status | — |
| `ZG1C` | 烟雾传感器 | HDC-SS01 | A26 | alarm | — |
| `ZG1D` | 燃气传感器 | HDC-GS01 | A27 | alarm | — |
| `ZG1F` | 华为鸿蒙智家 智能MINI | HCP23-BT | A2D | battery | faultDetection |
| `ZG1G` | 干接点开关 | HDC-SW001 | A13 | switch | — |
| `ZG1K` | 华为鸿蒙智家 智能MINI Pro | MINI-MLG320 | A2D | battery | faultDetection, rotationMode, wakeup |
| `ZG1N` | 清理开关 | HDC-CUS01 | A13 | switch | — |
| `ZG1O` | 勿扰开关 | HDC-CUS01 | A13 | switch | — |
| `ZG1R` | 家居设备 | Switch | A13 | switch | — |
| `ZG1X` | 虚拟投影仪开关 | VPS-1 | A13 | switch | — |
| `ZG2L` | AI超感传感器 Air（WiFi版） | SEN-MW11 | A14 | luminance | — |
| `ZG2M` | AI超感传感器 Air | SEN-MW10 | A14 | luminance | backlight |
| `ZG2W` | 智控旋钮 | SSL-H028 | A2D | battery | faultDetection, rotation |
| `ZGA0` | 华为摄像机D2150-10-LI-SV | D2150-10-LI-SV | A2A | switch | alarmEvent, capability, shootSwitch, videoSwitch |
| `ZGA1` | 华为摄像机D3250-10-SIU | D3250-10-SIU | A2A | switch | alarmEvent, capability, shootSwitch, videoSwitch |
| `ZGA3` | 华为摄像机HS-CAM-201 | HS-CAM-201 | A2A | switch | alarmEvent, capability, shootSwitch, videoSwitch |
| `ZGA4` | 华为摄像机HS-CAM-301 | HS-CAM-301 | A2A | switch | alarmEvent, capability, shootSwitch, videoSwitch |
| `ZGA5` | 华为摄像机HS-CAM-302 | HS-CAM-302 | A2A | switch | alarmEvent, capability, shootSwitch, videoSwitch |
| `ZGA7` | 华为摄像机HS-CAM-601 | HS-CAM-601 | A2A | switch | alarmEvent, capability, shootSwitch, videoSwitch |
| `ZGB1` | 华为摄像机HS-CAM-202 | HS-CAM-202 | A2A | switch | alarmEvent, capability, shootSwitch, videoSwitch |
| `ZGB2` | 华为摄像机HS-CAM-203 | HS-CAM-203 | A2A | switch | alarmEvent, capability, shootSwitch, videoSwitch |
| `ZGB3` | 华为摄像机HS-CAM-205 | HS-CAM-205 | A2A | switch | alarmEvent, capability, shootSwitch, videoSwitch |
| `ZGB4` | 华为摄像机HS-CAM-303 | HS-CAM-303 | A2A | switch | alarmEvent, capability, shootSwitch, videoSwitch |
| `ZGB5` | 华为摄像机HS-CAM-305 | HS-CAM-305 | A2A | switch | alarmEvent, capability, shootSwitch, videoSwitch |
| `ZGE0` | 华为网络录像机NVR800-A02-16P | NVR800-A02-16P | A29 | switch | alarmEvent, cruiseSwith, pushStatus, shootSwitch, videoSwitch |
| `ZGE1` | 华为网络录像机HS-NVR-801 | HS-NVR-801 | A29 | switch | alarmEvent, capability, shootSwitch, videoSwitch |

## 完全覆盖的设备

### switch（155 台）
- `103W` 国投主控1路开关1LA ・ `1043`  ・ `104R` Wulian智尚一路开关 ・ `105D` 易百珑单路多功能接收器ERC309-H
- `105I`  ・ `121A` 海令智能开关面板 ・ `140H` 控客一路灯光面板 ・ `140X` 开关回路控制器
- `140Y` 开关回路控制器 ・ `157I` 酷轻松石墨烯发热护膝 ・ `157X` 威廷智能单开Wi-Fi ・ `167U` Gimbal Pro-L7B-Pro
- `181W` 噼啪智能单开开关 ・ `183F` 噼啪智能插座 ・ `188B` 威廷智能插座 ・ `2082` 白色零火线单路灯控面板超薄
- `20C1` 未来小七机器人 ・ `20K4` 控客10A智能插座 ・ `20K7` 控客16A智能插座 ・ `20SV` eefit元气通二代
- `20XK` 控客-星空单路灯控面板 ・ `214X` 智汇云一位轻触开关面板 ・ `215L` 触控单开零火开关 ・ `217M` 开关智能控制器1型
- `217P` 控客-肖邦一路灯光面板 ・ `217V` 控客-肖邦10A智能插座 ・ `217W` 控客-肖邦16A智能插座 ・ `219P` 酷轻松石墨烯气囊支撑腰带
- `21B2` 单键智能开关面板尊享版 ・ `21EI` JW智能照明开关灯 ・ `21GK` JW智能开关1键型 ・ `21LF` 米立1路智能开关面板
- `21MO` 酷轻松石墨烯发热真丝暖腹宝 ・ `21N2` 欧普智能网关 ・ `21P9` 开关灯（底盒开关控制器） ・ `21PG` 触点开关
- `21TS` 狄耐克智能插座 ・ `21TX` 西顿开关控制模块 ・ `21VY` 瑞晶开关灯 ・ `221M` 
- `221T`  ・ `2221`  ・ `2246`  ・ `2247` 
- `224O`  ・ `227S` 亚摩斯睿雅单火开关单键 ・ `240W` 单键86底盒开关模块 ・ `24DJ` 亚摩斯智能转换插
- `283T` FSL智能插座 ・ `28RD` 名豆之约通断器 ・ `2999` 5G通信壳 ・ `29BA` 舍见智能插座
- `2AK5` 艾特插座 ・ `2AS7` 锐亿理发器 ・ `2ATT`  ・ `2B49` 探梦者智能电动滑板车
- `2B58` MixSwitch超级智能开关-一开 ・ `2B5N` 智能药盒 ・ `2B6J` 长虹足浴盆 ・ `2B6R` KUS筋膜枪
- `2B92` 凯胜眼部按摩器 ・ `2BO5` 堡丽触点开关 ・ `2BO7`  ・ `2BO9` 堡丽开关灯（底盒开关控制器）
- `2BOV`  ・ `2BVW` 关阀门机械手套装 ・ `2BWA` tinyho按摩筋膜枪RELAX ・ `2C75` FSL智能插座
- `2C97` 锐亿剃须刀 ・ `2CN1` 英尔健筋膜枪 ・ `2COA` 智能蒸汽眼罩 ・ `2CUT` 智能矫姿精灵
- `2CVF` 单键智能开关面板时尚版 ・ `2D56` 亿健智能筋膜枪 ・ `2DE0` Gimbal Pro-L7C-Pro ・ `2DEX` 壁挂式声光报警器套装
- `2DUZ` 单键智能开关面板尊享版 ・ `2ELY` 龙泉智家一路墙壁开关 ・ `2GVI` 狄耐克智能一路开关面板 ・ `2I4E` 5G通信壳 618
- `2IZ3` 5G通信壳 658 ・ `2IZ4` 5G通信壳 688 ・ `2KPV` 5G通信壳 698 ・ `9MTV` 智控灭蚊器
- `A0DO` 插座 ・ `A0GO` 智能便座 ・ `A0GP` 智能便座PL40 ・ `A0MC` 智汇云智能开关
- `A0N8` 智汇云智能插座 ・ `A0NN` 智能单通道插座 ・ `A0OP` 智能单通道开关 ・ `A0UB` 霍尼韦尔智能控制灯光
- `A108` 西门子三孔插座1 ・ `A10T` 西门子五孔插座1 ・ `A10U` 西门子五孔插座1 ・ `A2JK` 智能单通道机械开关
- `A2JN` ZB单通道开关 ・ `A2JO` 恒温恒湿智能开关 ・ `A2L4` 智汇云智能开关 ・ `A2WB` 智汇云智能开关
- `A2WK` 智汇云智能开关 ・ `A2WL` 智汇云智能开关 ・ `A2WM` 智汇云轨道式开关 ・ `K1C7` 华为路由TC7206
- `K1C8` 华为移动路由Pro ・ `K1D5` 华为随行WiFi 3 Pro ・ `K1D6` 华为随行WiFi 3 ・ `K1D7` 华为全屋智能 智能主机 EZ（网线版）
- `K1DL` 5G CPE 5 ・ `K1EU` 随行WiFi ・ `K1F5` HUAWEI 4G CPE 5 ・ `K1F6` HUAWEI 4G CPE 5
- `K1F7` HUAWEI CPE 5R ・ `K1FF` 华为随行WiFi 5 ・ `K1FN` 华为随行WiFi 5 ・ `K1FO` HUAWEI 4G Mobile WiF
- `K1FV` 5G Mobile WiFi Pro 5 ・ `K1FX` 华为全屋智能 分布式路由 M1 子路由 ・ `K1GA` 华为随行WiFi 5 eSIM ・ `M0B5` HUAWEI WATCH Buds
- `M0BW` HUAWEI WATCH GT Cybe ・ `M0C5` HUAWEI WATCH GT Cybe ・ `M0C6` HUAWEI WATCH GT Cybe ・ `RX01` HUAWEI 蓝牙鼠标
- `RX08` HUAWEI 无线鼠标 ・ `RX09` HUAWEI 蓝牙鼠标 第二代 ・ `RX0A` HUAWEI 蓝牙鼠标 第二代 ・ `RX0G` HUAWEI 高键程智能键盘
- `RX1B` HUAWEI 蓝牙鼠标 第二代 ・ `RX1C` HUAWEI 无线鼠标 第二代 ・ `RX1E` 华为星芒鼠标 ・ `RX1G` 华为星跃鼠标 GT
- `RX1L` 华为星跃鼠标 SE版本 ・ `RX1M` 华为星跃鼠标 SE悦享版 ・ `RX1N` TBD ・ `RX1O` TBD
- `RX1P` TBD ・ `RX1X` TBD ・ `RX1Y` TBD ・ `RX21` TBD
- `RX24` TBD ・ `ZF0J` 华为全屋智能 智能主机 Lite ・ `ZG0R` 吊灯 ・ `ZG0S` 智能照明
- `ZG0T` 床头灯 ・ `ZG0U` 磁吸灯 ・ `ZG0V` 灯带 ・ `ZG0W` 射灯
- `ZG0X` 筒灯 ・ `ZG0Y` 吸顶灯 ・ `ZG1G` 干接点开关 ・ `ZG1N` 清理开关
- `ZG1O` 勿扰开关 ・ `ZG1R` 家居设备 ・ `ZG1X` 虚拟投影仪开关

### brightness, cct, colourMode, lightMode, switch（55 台）
- `1070` 奥普吸顶灯AX560 ・ `1080` 欧普智能灯具 ・ `111F` 三思双色温灯泡 ・ `111Z` 三思双色温灯泡
- `116F` 博乐落地灯_FOL01 ・ `134R` U2C-智能护眼台灯-GD-TDW12B ・ `178O` 西顿锋芒智能灯带 ・ `184O` 博乐智能吸顶灯
- `206N` 高盛达智能吸顶灯 ・ `20RG` 威诺华智能灯泡 ・ `20VY` 亚摩斯智能筒灯 ・ `21JC` 阳光照明灵睿智能灯泡调光调色版
- `21UN` 三思LED吸顶灯 ・ `21Y4` 雷士简韵圆形卧室灯 ・ `21YB` 雷士叠影方形客厅灯 ・ `220J` 雷士智能灯带
- `2223` 雷士简韵方形卧室灯 ・ `2225` 雷士简韵方形客厅灯 ・ `2229` 雷士柠梦圆形小卧室灯 ・ `222B` 雷士满天星圆形卧室灯
- `222C` 雷士柠梦圆形卧室灯 ・ `222D` 雷士柠梦方形卧室灯 ・ `222E` 雷士柠梦方形客厅灯 ・ `226X` 阳光照明皓翼大三防灯
- `2274` 阳光照明至简方形客厅灯 ・ `2275` 阳光照明至简方形卧室灯 ・ `2276` 阳光照明至简圆形卧室灯 ・ `25FO` 三加三维智能筒射灯
- `25UT` 得途智能护眼吸顶灯 ・ `264S` 雷士智能吸顶灯 ・ `29QR` 三加三维智能三色 ・ `2AJO` Paulmann-Finn-Smart吸
- `2AJX` Paulmann-Diskette-Pr ・ `2AKM` 华艺凝玛吸顶灯 ・ `2APC` 雷士满天星方形客厅灯 ・ `2APF` 雷士叠影方形卧室灯
- `2APH` 雷士满天星方形卧室灯 ・ `2APM` 雷士叠影圆形卧室灯 ・ `2APN` 雷士叠影圆形小卧室灯 ・ `2B63` 捷德韦尔两线式可调光调色灯控盒
- `2B7O` Paulmann-Konig-Smart ・ `2BEG` 得邦A60蓝牙智能灯泡调光调色版 ・ `2BEH` 得邦A70蓝牙智能灯泡调光调色版 ・ `2BEK` 智能筒灯
- `2BEL` 智能光源模组 ・ `2BEN` 星空版悸动客厅吸顶灯 ・ `2BEO` 星空版悸动卧室吸顶灯 ・ `2BFP` 智能护眼台灯
- `2BGM` 三雄极光Pak智能筒灯 ・ `2DGO` 水母云智能双色筒灯 ・ `2DWC` 水母云智能双色灯带 ・ `2ENX` 得途智能护眼吸顶灯
- `2EO8` 熠世华彩情景灯 ・ `2EXO` 三思LED吸顶灯 24W ・ `2FW5` 吉豪智能吊灯

### brightness, switch（43 台）
- `0101` 灯组 ・ `103G` 生迪Wi-Fi智能球泡灯W11-C21 ・ `103Z` 国投一路调光1LT ・ `104W` 汉德森Wi-Fi信号放大吸顶灯
- `105V` TPLink白灯 ・ `115M` HDL灯光控制器 ・ `122D` 调光控制盒 ・ `133P` FSL单色智能天花灯
- `206P` 欧智通-智能吸顶灯 ・ `20DF` 永林单色调光器 ・ `20FN` 海令单路调光器 ・ `20GO` 摩根调光灯
- `213W` 西顿调光模块 ・ `215D` 西顿恒压调光模块 ・ `21ED` JW智能照明调光灯 ・ `21JB` 阳光照明灵睿智能灯泡调光版
- `21LB` 永林恒压调光驱动 ・ `21PC` 调光灯（照明调光器） ・ `21W2` 瑞晶调光灯 ・ `224B` 
- `224C`  ・ `227U` 亚摩斯睿雅零火开关单键 ・ `22ZV` Evoyo一路调光器小模块 ・ `27NI` 阳光博鸿读写台灯
- `2ABT` 永林调光驱动 ・ `2AQO` 鸿蒙智选 智能台灯2i ・ `2AQZ` 调光灯带（灯带调光器） ・ `2BDD` 单色温灯带调光驱动器
- `2BOE` 堡丽调光灯（照明调光器） ・ `2BOG`  ・ `2BOH`  ・ `2BOJ` 堡丽调光灯带（灯带调光器）
- `2CDN` ACEMATIC调光灯 ・ `2CTW` 三思智能厨卫灯 ・ `2FHB` 领普单键墙壁开关 ・ `2L8V` 立达信米来单头吊灯
- `2NVS` 三思智能植物生长灯R0260 ・ `2PXQ` 三思智能厨卫灯Pro ・ `2QQI` 智能植物灯 ・ `A0NG` 智汇云调光面板
- `A0OV` 单色球泡灯 ・ `A0UT` 霍尼韦尔智能控制调光 ・ `A2VL` 白灯

### brightness, cct, switch（33 台）
- `0102` 灯组 ・ `0106` 灯组 ・ `1055` 瑞晶筒灯RAL-2 ・ `113O` Yeelight色温灯泡
- `151H` 欧普延系列蓝牙控制盒 ・ `20DG` 永林双色调光器 ・ `20FI` 海令冷暖调光器 ・ `20PV` 锐点智能盒
- `20QK` 摩根调色温灯 ・ `213X` 西顿调色模块 ・ `215E` 西顿恒压调色模块 ・ `21LA` 永林恒压色温驱动
- `21SE` 调色温灯带（灯带调光器） ・ `21W3` 瑞晶色温灯 ・ `224A`  ・ `224D` 
- `29YQ` 24W双色温恒流控制装置 ・ `2ABU` 永林色温驱动 ・ `2AD0` 西顿24W调色模块 ・ `2AN7` 鸿雁DLT调光开关U2
- `2AR1` 调色温灯（照明调光器） ・ `2BOF` 堡丽调色温灯（照明调光器） ・ `2BOI`  ・ `2BOK` 堡丽调色温灯带（灯带调光器）
- `2NS7` 三思智能护眼吸顶灯HC60 ・ `2Q3X` 双色温吸顶灯24W ・ `2Q3Y` 双色温吸顶灯36W ・ `2Q3Z` 三思智能球泡灯13W
- `2Q7M` 三思智能球泡灯8W ・ `2Q7V` 三思智能球泡灯18W ・ `9MTL` 智控床头灯 ・ `9MU7` 智控灯泡
- `A2VM` 色温灯

### fan, mode, switch, temperature（26 台）
- `2165` 中央空调智能网关 ・ `21EM` JW智能空调 ・ `220K`  ・ `221P` 
- `2ANJ`  ・ `2AWX`  ・ `2BOS`  ・ `2CA6` ACEMATIC空调模块
- `9MXO` 智控空调 ・ `A0CP` 格力智能空调 ・ `A0E0` 海尔智能空调 ・ `A0UC` 霍尼韦尔智能控制空调
- `A3DE` COLMO挂机空调 ・ `A3DF` COLMO柜机空调 ・ `A3E6` 海信智能空调 ・ `A3E8` 海信智能中央空调
- `A3EK` 海信智能空调 ・ `A3EX` COLMO柜机空调 ・ `A3EY` COLMO柜机空调 ・ `A3F2` 海信智能室温控制器
- `A3GJ` 格力浴享系列中央空调 ・ `A3GK` 格力中央地暖空调 ・ `A3GO` 格力舒享系列中央空调 ・ `A3GS` 格力智能中央空调
- `A3LW` 一拖一中央空调 ・ `A3S0` 海信挂机空调

### brightness, cct, colourMode, switch（22 台）
- `111T` 佛山照明智能吸顶灯ZNQP-9W ・ `133M` FSL智能双色灯泡 ・ `133O` FSL智能调光调色筒灯 ・ `155F` FSL智薄卧室灯
- `203U` 12W恒流调光调色驱动 ・ `203X` 24W恒流调光调色驱动 ・ `204B` 60W恒压调光调色驱动 ・ `204E` 120W恒压调光调色驱动
- `22HW` 亚摩斯嵌入式射灯 ・ `23RO` 欧普智能吸顶灯 ・ `23RP` 欧普智能吸顶灯 ・ `23RQ` 欧普智能吸顶灯
- `2AA5` FSL调光调色吸顶灯-72W ・ `2AOR` FSL儿童卧室灯-海星 ・ `2AOS` FSL智薄客厅灯 ・ `2BES` FSL蓝牙调光调色吸顶灯
- `2BET` FSL蓝牙调光调色筒灯 ・ `2BEU` FSL蓝牙调光调色球泡 ・ `2BS9` FSL智趣UFO吸顶灯 ・ `2BSZ` FSL智贝吸顶灯
- `2CCK` ACEMATIC色温灯 ・ `A0OX` 冷暖双色调光灯

### switch, switch1, switch2, switch3（20 台）
- `101L`  ・ `105G`  ・ `105H`  ・ `20CS` 智汇云三位轻触开关面板
- `215N` 触控三开零火开关 ・ `217K` 开关智能控制器3型 ・ `2196` 圆和三路智能开关 ・ `221V` 
- `23W2` ACEMATIC灯光模块 ・ `2AB5` ACEMATIC智能液晶面板 ・ `2DSD` 拉孚三路智能开关 ・ `2DXC` 龙泉智家三路墙壁开关
- `2ENH` 亚摩斯星耀开关三键 ・ `2EZU` 亚摩斯睿雅单火开关三键 ・ `2FCZ` 博顿物联三开 ・ `2GVO` 狄耐克智能三路开关面板
- `A0OK` 智能三通道插座 ・ `A0OR` 智能三通道开关 ・ `A0YZ` 西门子开关 ・ `A2JM` 智能三通道机械开关

### switch, switch1, switch2（16 台）
- `214V` 智汇云二位轻触开关面板 ・ `215M` 触控双开零火开关 ・ `217L` 开关智能控制器2型 ・ `21B6` 圆和二路智能开关
- `221U`  ・ `227R` 亚摩斯睿雅单火开关双键 ・ `23WL` 亚摩斯极境开关双键 ・ `2DSE` 拉孚二路智能开关
- `2DXB` 龙泉智家二路墙壁开关 ・ `2ENG` 亚摩斯星耀开关双键 ・ `2FCX` 博顿物联二开 ・ `2GVK` 狄耐克智能二路开关面板
- `A0NT` 智能双通道插座 ・ `A0OQ` 智能双通道开关 ・ `A0Z2` 西门子开关 ・ `A2JL` 智能双通道机械开关

### switch1, switch2（15 台）
- `157Y` 威廷智能双开Wi-Fi ・ `164A` 智能双开开关 ・ `175S` 平头熊二键开关WIFI ・ `183D` 噼啪智能双开开关
- `20XP` 控客-星空双路灯控面板 ・ `20ZS` 控客-双路灯控模块 ・ `21GL` JW智能开关2键型 ・ `21LG` 米立2路智能开关面板
- `2AAK` 艾特双键开关 ・ `2B59` MixSwitch超级智能开关-二开 ・ `2CK0` 叶绿体单火二路墙壁开关 ・ `2CVH` 双键智能开关面板时尚版
- `2DB8` 双键86底盒开关模块 ・ `2DV0` 双键智能开关面板尊享版 ・ `A36A` 欧派智能二位开关P32

### action, opener（15 台）
- `163S` 维尔森VERSON智能窗帘 ・ `22D5` 捷昌智能窗帘 ・ `22ZX` Evoyo窗帘电机 ・ `25GH` 亚摩斯窗帘电机WiFi版
- `2ACW` 推窗器 ・ `2ACY` 卷帘 ・ `2ACZ` 卷帘（高扭矩版） ・ `2C5P` 堡丽卷帘
- `2C5Q` 堡丽卷帘（高扭矩版） ・ `2C5R` 堡丽开窗器 ・ `2D7A` 博孚WiFi智能窗帘 ・ `2E3G` 捷昌智能卷帘
- `2J2C` 无尽之窗窗帘机 ・ `2KZR` 杜亚智能升降器 DH13 ・ `A0UO` 霍尼韦尔智能控制窗帘

### switch1, switch2, switch3（14 台）
- `157Z` 威廷智能三开Wi-Fi ・ `164B` 智能三开开关 ・ `164M` 平头熊三键开关WIFI ・ `183E` 噼啪智能三开开关
- `20XW` 控客-星空三路灯控面板 ・ `21GM` JW智能开关3键型 ・ `21LH` 米立3路智能开关面板 ・ `24HE` Evoyo三路开关小模块
- `2AAL` 艾特三键开关 ・ `2B5A` MixSwitch超级智能开关-三开 ・ `2CK1` 叶绿体单火三路墙壁开关 ・ `2CVI` 三键智能开关面板时尚版
- `2DV1` 三键智能开关面板尊享版 ・ `A364` 欧派智能三位开关P33

### mode（14 台）
- `101A` 中控主机 ・ `20F5`  ・ `20K8` 控客推窗器面板 ・ `20KA` 
- `20Y5` 控客-星空单路窗帘面板 ・ `2163` 触控单路窗帘电机控制面板 ・ `217T`  ・ `21ES` JW智能窗帘A型
- `21LD` 米立1路窗帘控制面板 ・ `21XA` 瑞晶开合帘 ・ `21XE` 瑞晶百叶帘 ・ `221G` 
- `2AK6` 艾特窗帘控制器 ・ `2CDJ` ACEMATIC窗帘电机

### motor, openLevel（13 台）
- `100J` 杜亚电动开窗机DJ56TSWH ・ `100K` 杜亚电动窗帘DT76TV/WH ・ `101h` 杜亚电动窗帘DT806TV/WH ・ `101j` 杜亚电动卷帘DM35F/WH
- `1044`  ・ `1057` 瑞晶布帘RAL-4 ・ `1058` 瑞晶纱帘RAL-5 ・ `105A` 杜亚电动窗帘DH3
- `105B` 杜亚电动窗帘DH5 ・ `105C` 杜亚电动窗帘DH7 ・ `1067` 飞比智能窗帘TZT2118W-T1 ・ `106D` 顺舟窗帘电机SZ09-(18)
- `120Y` 

### mode, switch, temperature（11 台）
- `115Q` HDL地暖 ・ `21V9` 瑞晶冷热源一体机 ・ `21VA` 瑞晶壁挂炉 ・ `23QV` ACEMATIC地暖模块
- `A1AZ` 美的家用空调 ・ `A1B0` 美的家用空调 ・ `A1EV` 美的家用空调 ・ `A1EX` COLMO空调
- `A1EY` COLMO空调 ・ `A3F3` 海信智能水温控制器 ・ `A3GY` 格力至尊型户式机

### mode, opener（11 台）
- `163O` 窗帘电动轨道 ・ `20G4`  ・ `20JS` 霍夫曼开合帘 ・ `20L1` 
- `2162` 智能窗帘电机 ・ `21DD`  ・ `221F`  ・ `2ACV` 开合帘
- `2AOQ` 杜亚智能窗帘DH6 ・ `2C5N` 堡丽开合帘 ・ `A0MD` 智汇云窗帘电机

### status（11 台）
- `21PH` 人体移动传感器 ・ `220N` 人体存在传感器 ・ `2301` Evoyo吸顶式人体传感器 ・ `2AK4` 艾特人体红外传感器
- `2BOO` 堡丽人体存在传感器 ・ `2BOQ` 堡丽人体移动传感器 ・ `2CVY` 南方家居智能护颈枕 ・ `2DNV` 维尔森香薰助眠枕
- `A073` 美的智能电饭煲 ・ `A0EQ` 布谷智能扫拖机器人 ・ `ZG1A` 红外幕帘传感器

### alarm, battery（10 台）
- `200Y` 麦乐克水浸传感器 ・ `215U` 漏水检测器 ・ `21XM` 瑞晶水浸探测器 ・ `21XQ` 瑞晶烟雾探测器
- `221O`  ・ `221Q`  ・ `22ZK` Evoyo水浸传感器 ・ `22ZZ` Evoyo烟雾传感器
- `2AE9`  ・ `2BE7` 麦乐克水浸传感器

### switch, temperature（9 台）
- `21ER` JW智能地暖 ・ `221J`  ・ `224R`  ・ `2ANK` 
- `2BOU`  ・ `A0DF` 布谷智能取暖器 ・ `A0UR` 霍尼韦尔智能控制地暖 ・ `A3GP` 格力热水发生器
- `A3GQ` 格力地暖转接器

### alarm（9 台）
- `215T` 可燃气体探测器 ・ `21PS` 燃气传感器 ・ `21XK` 瑞晶燃气探测器 ・ `22ZY` Evoyo燃气传感器
- `2AK0` 艾特燃气报警器 ・ `2CUZ` 吸顶式燃气传感器套装 ・ `2CV0` 吸顶式烟雾传感器套装 ・ `ZG1C` 烟雾传感器
- `ZG1D` 燃气传感器

### brightness, cct, lightMode, switch（8 台）
- `101r` 得邦智能吸顶灯 ・ `128P` nimova智能护眼台灯Pro ・ `218A` 西顿24W防蚊虫快装智能吸顶灯 ・ `218E` 西顿30W防蚊虫快装智能吸顶灯
- `218F` 西顿40W防蚊虫快装智能吸顶灯 ・ `2BGN` 三雄极光Pak智能吸顶灯 ・ `2BGU` 沙漠鱼智能台灯 ・ `2O9M` eachone一起玩 智能立式护眼学习灯

### battery（8 台）
- `2B5B` MixSwitch超级智能情景开关 ・ `2BGF` 欧普蓝牙MESH面板-双键 ・ `2BGG` 欧普蓝牙MESH面板-四键 ・ `2CJW` 叶绿体一键情景面板
- `2CJX` 叶绿体二键情景面板 ・ `2CJY` 叶绿体三键情景面板 ・ `2DGU` 梦洁睡眠监测枕 ・ `ZCA2` AI眼镜

### brightness, cct, colour, colourMode, switch（7 台）
- `0103` 灯组 ・ `0104` 灯组 ・ `0105` 灯组 ・ `2BEV` FSL蓝牙彩光灯带
- `A0OW` 律动灯带 ・ `A0OY` 五色灯 ・ `A2V7` 彩灯

### fan, switch（7 台）
- `21V4` 瑞晶空气净化器 ・ `221R`  ・ `2AK8` 艾特新风控制器 ・ `2ANI` 
- `2CDL` ACEMATIC新风模块 ・ `A0UQ` 霍尼韦尔智能控制新风 ・ `A3F1` 海信智能新风机

### brightness, cct, colour, colourMode, lightMode, switch（6 台）
- `0100` 三思全彩灯泡灯组 ・ `131N` 生迪智能LED彩光灯泡 ・ `208J` 水母云唤醒灯 ・ `242X` 亚摩斯RGBCW灯带控制器
- `2BEI` 得邦A60蓝牙智能灯泡全彩版 ・ `2BEJ` 得邦A70蓝牙智能灯泡全彩版

### action, status（6 台）
- `20GQ` 360扫地机器人X90 ・ `A0DA` 布谷智能破壁机 ・ `A3BM` 方太智能燃气灶具 ・ `A3CP` 老板蒸烤一体机
- `A3CQ` 燃气灶 ・ `A3DP` 老板洗碗机

### colour, switch（6 台）
- `21SD` RGB调色灯带（灯带调光器） ・ `21SF` RGBW调色灯带（灯带调光器） ・ `2A00` 背景音乐主机 ・ `2BOL` 堡丽RGB调色灯带（灯带调光器）
- `2BON` 堡丽RGBW调色灯带（灯带调光器） ・ `2DAC` RGBW灯带调光驱动器

### switch1（6 台）
- `163Q` 智能单开开关 ・ `175R` 平头熊一键开关WIFI ・ `21V2` 瑞晶智能开关 ・ `2AAJ` 艾特单键开关
- `2CJZ` 叶绿体单火一路墙壁开关 ・ `A36B` 欧派智能一位开关P31

### brightness, cct, colour, lightMode, switch（5 台）
- `100z` 三思全彩灯泡 ・ `101q` 得邦智能台灯 ・ `105L` Hue智能调光灯泡(彩灯) ・ `113P` Yeelight彩光灯泡
- `113S` Yeelight彩光灯带

### brightness, lightMode, switch（5 台）
- `101S` 欧普罗迪智能灯 ・ `113N` Yeelight白光灯泡 ・ `113Q` Yeelight护眼台灯 ・ `113V` Yeelight吸顶灯
- `2BGL` 三雄极光Pak智能射灯

### action（5 台）
- `21SR` 开关卷帘 ・ `21XF` 瑞晶卷帘 ・ `23FC` 亚摩斯智能家具控制器 ・ `2BO6` 堡丽开关卷帘
- `A2M5` 智汇云窗帘模块

### brightness, colourMode, lightMode, switch（4 台）
- `154E` 漾美无线充智能台灯 ・ `154F` 三思LED天花灯 ・ `202Z` 三思智能LED球泡灯 ・ `2AJY` Paulmann单色温智能灯

### action, lightSwitch, status（4 台）
- `114O` 奥普智能晾衣机D8 ・ `205Q` 四季沐歌M-HY900Z-GG智能晾衣机 ・ `2B2H` 晾品智能晾衣机HW70 ・ `2C5J` 凯迪仕晾衣机

### airDetector（4 台）
- `101N` 720环境宝 ・ `104A` 国投二氧化碳传感器CO2 ・ `104C` 国投PM2.5传感器PMX ・ `1050` 瑞晶六合一空气检测器RAD-1

### luminance（4 台）
- `104D` 国投光照传感器LUX ・ `21G7` JW光照检测器 ・ `227Q` 光传感器 ・ `ZG2L` AI超感传感器 Air（WiFi版）

### airDetector, battery（3 台）
- `104B` 国投温湿度传感器THC ・ `113D` 豪恩温湿度传感器 ・ `120N` 海令智能温湿度传感器

### switch, switch1（3 台）
- `21BF` 圆和一路智能开关 ・ `2DSB` 拉孚一路智能开关 ・ `A0Z4` 西门子开关

### battery, status（3 台）
- `21BM` 云起水浸感应器 ・ `21PQ` 水浸传感器 ・ `2300` Evoyo门窗传感器

### status, switch（3 台）
- `2BF3` 门磁传感器套装 ・ `2CQG` 吸顶式红外人体移动传感器 ・ `2CQH` 吸顶式毫米波人体存在传感器

### brightness, cct, lightSwitch, status, switch, switch1（2 台）
- `27W5` 侧装红外人体移动光照传感器 ・ `29F2` 侧装红外人体移动光照传感器

### brightness, colour, colourMode, lightMode, switch（2 台）
- `178N` 西顿风影彩光灯带 ・ `2588` 三加三维智能幻彩灯带

### brightness, switch, switch1, switch2, switch3（2 台）
- `274F` 领普三键墙壁开关 ・ `2EZR` 亚摩斯睿雅零火开关三键

### brightness, cct, colour, switch（2 台）
- `1054` 瑞晶吊灯RAL-1 ・ `1056` 瑞晶灯带RAL-3

### brightness, colour, colourMode, switch（2 台）
- `20FM` 海令调色调光器 ・ `A0N7` 智汇云RGB模块

### childLockSwitch, mode, switch, temperature（2 台）
- `20XC` 控客-肖邦水地暖面板 ・ `20XI` 控客-肖邦电地暖面板

### brightness, switch, switch1, switch2（2 台）
- `227T` 亚摩斯睿雅零火开关双键 ・ `27SC` 领普双键墙壁开关

### battery, humidity, temperature（2 台）
- `201E` 麦乐克温湿度传感器 ・ `2BE8` 麦乐克无线温湿度传感器

### fan, pm25, switch（2 台）
- `224Q`  ・ `2BOT` 

### luminance, status, switch（2 台）
- `27W6` 吸顶式红外人体移动光照传感器 ・ `2BDI` 吸顶式毫米波人体存在光照传感器

### status, switch, temperature（2 台）
- `A2UR` 万家乐燃气热水器普通恒温系列 ・ `A2UT` 万家乐电热水器

### humidity, temperature（2 台）
- `21GJ` JW空气检测E型 ・ `A2LW` 温湿度传感器

### alarm, switch（2 台）
- `29F4` 红外幕帘传感器 ・ `2BDP` 壁挂式水浸传感器套装

### openLevel（2 台）
- `104U`  ・ `116X` HDL窗帘

### motor（2 台）
- `140V` 窗帘控制器 ・ `140W` 窗帘控制器

### battery, brightness, mode, status, switch（1 台）
- `28SL` 智能贝壳镜

### brightness, colour, lightMode, switch（1 台）
- `0107` 灯带组

### humidity, luminance, pm25, temperature（1 台）
- `215V` 智能环境盒子

### action, mode, opener, status（1 台）
- `2180` 

### battery, humidity, luminance, temperature（1 台）
- `21DJ` 

### hcho, humidity, pm25, temperature（1 台）
- `21GI` JW空气检测D型

### brightness, cct, status, switch（1 台）
- `9MTJ` 智控夜灯

### action, mode, status, switch（1 台）
- `9MZQ` 智控咖啡机

### brightness, colourMode, switch（1 台）
- `2H4H` 智小金智能柜内灯电源驱动

### mode, status, switch（1 台）
- `9MZT` 智控电磁炉

### action, battery, status（1 台）
- `A36L` 科沃斯扫地机器人

### lightMode, switch（1 台）
- `21JP` 西顿杀菌厨卫灯

### battery, luminance（1 台）
- `21VX` 瑞晶亮度感应器

### battery, switch（1 台）
- `21XP` 瑞晶报警器

### mode, status（1 台）
- `223W` 鸿蒙智选儿童智能牙刷

### childLockSwitch, switch（1 台）
- `2GVP` 转换器(狄耐克智能插座)

### mode, switch（1 台）
- `2H9E` 金莱特便携干衣胶囊

### pm25（1 台）
- `115S` HDL空气质量传感器

### alarmBell（1 台）
- `9MTM` 智控压力传感器

### opener（1 台）
- `A0NV` 智能窗帘
