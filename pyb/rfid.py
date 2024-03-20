from pyb._customtype import uint8

# 需连接在主控P1-6接口
class RFID:
  """ 射频IC传感器(IIC) """

  def __init__(self) -> None:

    pass

  def readCode(self) -> uint8:
    """ 
    读取IC卡编号

    e.g.
    
    RFID().readCode()
    """
    return 1


