from _customtype import uint16
from typing import Literal

EspPort = Literal[2]
EspBaudRate = Literal[9600]

class MqttESP8266:
  """ 
  物联网模块(接口P8) 

  需结合物联网平台iot.cfunworld.com使用
 
  e.g.\n
  from pyb import MqttESP8266
  from time import sleep
  mqtt8266 = MqttESP8266(2,9600)
  mqtt8266.connectWiFi("wifiname","password1")
  sleep(10)
  while not mqtt8266.checkWiFi() :
    pass
  mqtt8266.setMqtt("username", 1, "password2")
  mqtt8266.connectTCP("iot.cfunworld.com",1883)
  sleep(1)
  while not mqtt8266.checkMqtt() :
    pass
  mqtt8266.subscribe(1,"CmsgW")
  sleep(1)
  while True:
    if mqtt8266.readData(1,"CmsgW"):
      print(mqtt8266.mqtt_string)
    mqtt8266.publishStr("Cmsg","hello cfunworld")
    sleep(1)
  """

  mqtt_string: str
  mqtt_dataA: float
  mqtt_dataB: float
  mqtt_dataC: float
  mqtt_dataD: float

  def __init__(self, port: EspPort, baudRate: EspBaudRate) -> None:
    """
    port - 接口P8: 2
    baudRate - 波特率: 9600
    """
    pass

  def connectWiFi(self, wifi: str, password: str) -> None:
    """ 
    初始化步骤1: 连接无线网

    wifi - 无线网名称(英文字符和数字构成, 且不包含空格), 不支持5G频段;
    password - 无线网密码

    [注] 连接过程需消耗一定时间, 建议调用后等待>9秒
    """
    pass
  
  def checkWiFi(self) -> bool:
    """ 
    初始化步骤2: 校验无线网是否连接成功

    返回值为True时, 可进行下一步
    """
    return False
  
  def setMqtt(self, username: str, deviceId: str, password: str) -> None:
    """  
    初始化步骤3: 设置物联网登录信息, 由物联网平台iot.cfunworld.com生成
    
    username - 用户名;
    deviceId - 设备ID;
    password - 连接密钥
    """
    pass

  def connectTcp(self, ip: str, port: uint16) -> None:
    """ 
    初始化步骤4: 连接物联网

    ip - 服务ip(iot.cfunworld.com);
    port - 端口号(1883)

    [注] 连接过程需消耗一定时间, 建议调用后等待>1秒
    """
    pass

  def checkMqtt(self) -> bool:
    """ 
    初始化步骤5: 校验物联网是否连接成功

    返回值为True时, 可进行后续操作
    """
    return False
  
  def cleanMqtt(self) -> None:
    """ 
    主动断开物联网连接
    """
    pass

  def publishNum(self, topic: str, dataA: float, dataB: float, dataC: float, dataD: float) -> None:
    """ 
    向创建连接设备的指定主题发布数值信息

    topic - 发布主题的名称: 主题"Cnum1"对应平台数据监控的数据A-D, 主题"Cnum2"对应平台数据监控的数据E-H;
    dataA - 数据A;
    dataB - 数据B;
    dataC - 数据C;
    dataD - 数据D

    [注] 发布行为间隔>=1秒
    """
    pass

  def publishStr(self, topic: str, data: str) -> None:
    """ 
    向创建连接设备的指定主题发布字符串信息

    topic - 发布主题的名称: 主题"Cmsg"对应平台会话监听;
    data - 文本信息
    """
    pass

  def subscribe(self, deviceId: str, topic: str) -> None:
    """ 
    订阅指定设备的指定主题

    deviceId - 设备ID;
    topic - 订阅主题的名称: 主题"CmsgW"监控平台控制界面的发布会话; 主题"Cbtn"监控平台控制界面的按钮A-D, 主题"Cran"监控平台控制界面的滑杆A-D

    [注] 订阅行为间隔>=1秒
    """
    pass

  def unsubscribe(self, deviceId: str, topic: str) -> None:
    """
    取消订阅指定设备的指定主题

    deviceId - 设备ID;
    topic - 取消订阅主题的名称: 主题"CmsgW"监控平台控制界面的发布会话, 主题"Cbtn"监控平台控制界面的按钮A-D, 主题"Cran"监控平台控制界面的滑杆A-D
    """
    pass

  def readData(self, deviceId: str, topic: str) -> bool:
    """
    校验是否接收到一次订阅主题的信息
    
    mqtt_string, mqtt_dataA/B/C/D重新赋值
    """
    return False