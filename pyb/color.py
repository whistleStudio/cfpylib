from typing import Literal
from pyb._customtype import uint8, ColorId

# 颜色识别模块编号1-6, 见模块丝印
ModuleId = Literal[1, 2, 3, 4, 5, 6]

# 需连接在主控P1-6接口
class Color:
  """ 颜色识别传感器(IIC) """

  def __init__(self, id: ModuleId) -> None:
    """  
    id - 模块编号1-6, 详见PCB板丝印
    """
    pass

  def readColor(self) -> ColorId:
    """ 
    识别颜色, 返回对应颜色ID值\n
    1(黑), 2(蓝), 3(绿), 4(黄), 5(红), 6(白), 7(棕), 8(紫)

    e.g.\n
    Color(1).readColor()
    """
    return 1


