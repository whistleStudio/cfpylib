from _customtype import uint8, short, IoPort
from typing import Literal

CrossType = Literal["cross", "left", "right"]

class CarTrack:
  """ 智能车循迹库 """

  def __init__(self) -> None:
    pass

  def trackPow(self, power: uint8) -> None:
    """  
    以指定动力循迹(仅单次循迹逻辑)

    power - 动力值: 0-100

    e.g.

    while True:
      CarTrack().trackPow(50)
    """
    pass

  def trackPowRoad(self, power: uint8, cross: CrossType | str) -> None:
    """  
    以指定动力循迹(异步循环循迹逻辑)到指定种类路口停止

    power - 动力值: 0-100;
    cross - 路口种类: cross(十字路口)/left(左路口)/right(右路口)

    任务完成时, .taskok()自动置为True

    e.g.

    CarTrack().trackPowRoad(50, "cross")
    """
    pass

  def taskok(self) -> bool:
   """  
   校验当前循迹任务是否完成
   """
   return False
  
  def stopTask(self) -> None:
    """ 
    停止本次循迹任务

    .taskok()置为True; M1和M2接口电机停止
    """
    pass

  def setGrayPin(self, grayscale: short, g1: IoPort, g2: IoPort, g3: IoPort, g4: IoPort) -> None:
    """ 
    设置循迹时灰度阈值及灰度传感器

    grayscale - 灰度阈值
    g1/2/3/4 - 灰度传感器接口(P1-8): A0、A2、A4、A6、B0、C0、C2、C4;   

    e.g.

    CarTrack().setGrayPin(600, "A0", "A2", "A4", "A6")
    """
    pass

  def setDifSpeed(self, smallDif: uint8, bigDif: uint8) -> None:
    """ 
    设置循迹时纠正速度

    smallDif - 小幅度纠正差速
    bigDif - 大幅度纠正差速
    """
    pass