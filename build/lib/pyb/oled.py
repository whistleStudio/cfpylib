from typing import Literal, Annotated
from dataclasses import dataclass

@dataclass
class ValueRange:
  min: int
  max: int

Row = Annotated[int, ValueRange(1, 64)]
Col = Annotated[int, ValueRange(1, 128)]

Size = Literal["big", "small"]
DisplayMode = Literal["forward", "reverse"]

class OLED: 
  """ 板载128*64显示屏 """
  
  def __init__(self) -> None:
    pass

  def displayStr(self, x: Row, y: Col, size: Size, mode: DisplayMode, val: str) -> None: 
    """
    显示英文字符或数字

    x - 行号(单位:像素点): 1/9/17/25/33/41/49/57;
    y - 列号(单位:像素点): 1-128;
    size - 字号: big(大16*16)/small(小8*8);
    mode - 显示模式: forward(黑字白底)/reverse(白字黑底) 
    str - 文本内容

    e.g.

    OLED().displayStr(1, 1, "big", "forward", "hello") 
    """
    pass

  def displayNum(self, x: Row, y: Col, size: Size, mode: DisplayMode, num: float) -> None:
    """
    显示数字

    x - 行号(单位:像素点): 1/9/17/25/33/41/49/57;
    y - 列号(单位:像素点): 1-128;
    size - 字号: big(大16*16)/small(小8*8);
    mode - 显示模式: forward(黑字白底)/reverse(白字黑底); 
    num - 数字 

    e.g.

    OLED().displayNum(1, 1, "big", "forward", 123.4) 
    """
    pass

  def displayChineseH(self, x: Row, y: Col, mode: DisplayMode, text: str) -> None:
    """
    显示中文

    x - 行号(单位:像素点): 1/9/17/25/33/41/49/57;
    y - 列号(单位:像素点): 1-128;
    mode - 显示模式: forward(黑字白底)/reverse(白字黑底); 
    text - 中文文本GBK

    [注] 中文字号为big(16*16)

    e.g.

    OLED().displayChinese(1, 1, "forward", "你好") 
    """
    pass

  def displayPic(self, x: Row, y: Col, picName: str) -> None:
    """
    显示图片

    x - 行号(单位:像素点): 1-64;
    y - 列号(单位:像素点): 1-128;
    picName - 图片文件名称(不含后缀名; 必须为二值化BMP图片文件, 并提前存储在磁盘指定文件夹picture下)
    """
    pass

  def clear(self) -> None:
    """
    清屏(白底)
    """
    pass

  