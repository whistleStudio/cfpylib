from _customtype import IoPort

class Weigh:
  """ 称重传感器 """

  def __init__(self, port: IoPort) -> None:
    """  
    port - 接口编号P1-8: A0、A2、A4、A6、B0、C0、C2、C4
    """
    pass

  def read (self) -> int:
    """ 
    读取重量: 返回数值与负载呈线性变化
    """
    return 0
  
