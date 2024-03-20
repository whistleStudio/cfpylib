from pyb._customtype import IoPort

class PM25:
  """ PM2.5浓度检测传感器 """

  def __init__(self, port: IoPort) -> None:
    """ 
    port - 接口编号P1-8: A0、A2、A4、A6、B0、C0、C2、C4  
    """
    pass

  def read(self) -> float:
    """ 
    读取浓度值  
    """
    return 0.0