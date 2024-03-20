from pyb._customtype import uint8

# 需连接在主控P1-6接口
class ASR:
  """ 语音识别传感器(IIC) """

  def __init__(self) -> None:

    pass

  def readCode(self) -> uint8:
    """ 
    读取识别语句的录入ID

    e.g.\n
    ASR().readCode()
    """
    return 0


