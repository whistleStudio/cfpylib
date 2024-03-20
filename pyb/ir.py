from pyb._customtype import IoPort, uint8

class IR:
  """ 红外遥控接收模块 """

  def __init__(self, port: IoPort) -> None:
    """ 
    port - 接口编号P1-8: A0、A2、A4、A6、B0、C0、C2、C4
    """
    pass

  def readCode(self) -> uint8:
    """ 
    读取红外模块接收的值 
    """
    return 0