from _customtype import uint8, short

# 需连接在主控P1-6接口
class NRF24L01:
  """ 
  NRF24L01无线通讯模块(IIC) 
  
  e.g.

  # 发送方示例
  from pyb import NRF24L01
  from time import sleep_ms
  nrf = NRF24L01()
  nrf.setMode_TX() 
  while True:
    sleep_ms(500)
    nrf.transition(1,1.1,2.2,3.3,2703)

  # 接收方示例
  from pyb import NRF24L01
  from time import sleep_ms
  nrf = NRF24L01()
  nrf.setMode_RX()
  while True:
    sleep_ms(500)
    nrf.receive()
    print(nrf.oppositeID)
  """

  oppositeID: short
  """ 对方无线模块编号 """
   
  typeCode: uint8
  """ 类别码0-255 """

  dataA: float
  dataB: float
  dataC: float
  sentence: str

  dataX: float
  """ 无线遥控器的摇杆水平分量 """

  dataY: float
  """ 无线遥控器的摇杆垂直分量 """

  upButton: bool
  """ 无线遥控器的上键: True(按下)/False(松开) """

  downButton: bool
  """ 无线遥控器的下键: True(按下)/False(松开) """

  leftButton: bool
  """ 无线遥控器的左键: True(按下)/False(松开) """

  rightButton: bool
  """ 无线遥控器的右键: True(按下)/False(松开) """

  def __init__(self) -> None:
    pass

  def setMode_TX(self) -> None:
    """ 设置为发送模式 """
    pass

  def setMode_RX(self) -> None:
    """ 设置为接收模式 """
    pass

  def transition(self, dataClass: uint8, dataA: float, dataB: float, dataC: float, receiver: short) -> None:
    """ 
    发送数值信息至指定模块

    dataClass - 类别码: 0-255;
    dataA - 数值A;
    dataB - 数值B;
    dataC - 数值C;
    receiver - 接收方编号(见PCB丝印)
    """
    pass

  def transitionStr(self, data: str, receiver: short) -> None:
    """ 
    发送字符串信息至指定模块

    data - 文本信息;
    recevier - 接收方编号(见PCB丝印)
    """
    pass

  def receive(self) -> None:
    """
    接收一次无线通讯数据
    
    实现了接收数据的重新赋值
    """
    pass

