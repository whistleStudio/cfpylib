from pyb._customtype import IoPort

class Ultrasonic:
  """ 超声波测距传感器 """

  def __init__(self, port: IoPort) -> None:
    """  
    port - 接口编号P1-8: A0、A2、A4、A6、B0、C0、C2、C4
    """
    pass

  def readDistance(self) -> float:
    """  
    获取探头至前方障碍物距离, 单位cm

    e.g.
    
    Ultrasonic("A0").readDistance()
    """
    return 0.0