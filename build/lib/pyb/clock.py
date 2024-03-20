from _customtype import uint8, ValueRange
from typing import Annotated

Month = Annotated[uint8, ValueRange(1, 12)]
Date = Annotated[uint8, ValueRange(1, 31)]
Day = Annotated[uint8, ValueRange(1, 7)]
Hour = Annotated[uint8, ValueRange(0, 24)]
Minute = Annotated[uint8, ValueRange(0, 60)]
Second = Annotated[uint8, ValueRange(0, 60)]

# 需连接在主控P1-6接口
class Clock:
  """ 时钟模块(IIC) """

  def __init__(self) -> None:
    pass

  def setYMDW(self, y: uint8, m: Month, d: Date, w: Day) -> None:
    """ 
    设置年 月 日 周\n
    y - 年;
    m - 月;
    d - 日;
    w - 周(星期几) 

    e.g.\n
    Clock().setYMDW(2024, 2, 21, 3)
    """
    pass

  def setHMS(self, h: Hour, m: Month, s: Second) -> None:
    """
    设置时 分 秒\n
    h - 时;
    m - 分;
    s - 秒
    
    e.g.\n
    Clock().setHMS(15, 55, 19)
    """
    pass

  def readYear(self) -> uint8:
    """ 获取年份 """
    return 0

  def readMonth(self) -> Month:
    """ 获取月份 """
    return 1

  def readDate(self) -> Date:
    """ 获取日期 """
    return 1

  def readWeek(self) -> Day:
    """ 获取星期几 """
    return 1

  def readHour(self) -> Hour:
    """ 获取时 """
    return 0

  def readMinute(self) -> Minute:
    """ 获取分 """
    return 0

  def readSecond(self) -> Second:
    """ 获取秒 """
    return 0
