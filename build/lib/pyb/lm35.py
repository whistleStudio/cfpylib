from pyb._customtype import IoPort


class LM35:
  """ LM35温度传感器 """
   
  def __init__(self, port: IoPort) -> None:
    """ 
    port - 接口编号P1-8: A0、A2、A4、A6、B0、C0、C2、C4   
    """
    pass

  def readTem(self) -> float:
    """  
    读取温度值

    e.g.
    LM35("A0").readTem()
    """
    return 0.0