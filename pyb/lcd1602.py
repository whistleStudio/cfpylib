from pyb._customtype import uint8
from typing import Annotated, Literal
from dataclasses import dataclass

@dataclass
class ValueRange:
  min: int
  max: int

Row = Annotated[int, ValueRange(1, 2)]
Col = Annotated[int, ValueRange(1, 16)]

ModuleId = Literal[1, 2, 3, 4, 5, 6, 7, 8] 
# 需连接在主控P1-6接口
class lcd1602:
  """ lcd显示屏16*2(IIC) """

  def __init__(self, id: ModuleId) -> None:
    """
    id - 模块编号: 1-8
    """
    pass

  def display(self, x: Row, y: Col, val: str) -> None:
    """ 
    显示英文字符或数字

    x - 行号: 1/2;
    y - 列号: 1-16;
    val - 文本内容

    e.g.
    
    lcd = lcd1602(1)
    lcd.display(1,1,'helloWorld!')
    lcd.display(1,1,1234567)
    lcd.display(1,1,3.14)
    """
    pass

  def clear(self) -> None:
    """
    清屏
    """
    pass
