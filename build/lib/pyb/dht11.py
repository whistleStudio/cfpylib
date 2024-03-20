from pyb._customtype import IoPort, uint8

class DHT11:
  """ DHT11温湿度传感器 """

  def __init__(self, port: IoPort) -> None:
    """ 
    port - 接口编号P1-8: A0、A2、A4、A6、B0、C0、C2、C4
    """
    pass

  def readTem(self) -> uint8:
    """ 
    读取温度值

    e.g.\n
    DHT11("A0").readTem()  
    """
    return 0
  
  def readHum(self) -> uint8:
    """ 
    读取湿度值

    e.g.\n
    DHT11("A0").readHum()  
    """
    return 0