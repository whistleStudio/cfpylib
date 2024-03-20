from typing import Annotated
from _customtype import ValueRange, UARTPort

CodeId = Annotated[int, ValueRange(0, 99)]

class IRStudy:
  """ 红外遥控学习模块 """

  def __init__(self, port: UARTPort) -> None:
    """ 
    port - 接口编号: 1(P7), 2(P8)
    """
    pass

  def learn(self, id: CodeId) -> None:
    """ 
    记录信号

    id - 记录编号: 0-99 
    """
    pass

  def send(self, id: CodeId) -> None:
    """ 
    发送信号
    
    id - 发送编号: 0-99
    """