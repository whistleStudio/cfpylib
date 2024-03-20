from pyb._customtype import uint8

# 需连接在主控P1-6接口
class HeartRate:
  """ 心率检测传感器(IIC) """

  def __init__(self) -> None:
    pass

  def getHeartRate(self) -> uint8:
    """ 
    读取心率检测值

    e.g.
    
    HeartRate().getHeartRate()
    """
    return 0


