from _customtype import uint8, UARTPort

class CFunUART:
  """ 串口通讯模块 """

  def __init__(self, port: UARTPort) -> None:
    """ 
    port - 接口编号: 1(P7), 2(P8) 
    """
    pass

  def setBaudrate(self, baudrate: int) -> None:
    """ 
    设置波特率\n
    baudrate - 波特率数值
    """
    pass

  def writeChar(self, b: uint8) -> None:
    """ 
    发送一字节数值

    b - 字节数值
    """
    pass

  def writeVal(self, varStr: str, var: float) -> None:
    """ 
    发送变量

    varStr - 变量名称;
    var - 变量
  
    e.g.

    a = 12.3
    CFunUART(1).writeVal("a", a) 
    """

  def readAvailable(self) -> bool:
    """ 
    校验串口是否有可读数据
    """
    return False
  
  def readChar(self) -> uint8:
    """
    读取一字节数据

    e.g.

    cfuart = CFunUART(2)
    if cfuart.readAvailable():
      cfunart.readChar()
    """
    return 0
  
  def readVal(self, varStr: str) -> float:
    """
    读取接收到的变量的值

    valStr - 变量名称

    e.g.

    CFunUART(2).readVal("a")
    """
    return 0.0