from pyb._customtype import uint8

class RGBLED:
  """ 板载七彩灯 """

  def __init__(self) -> None:
    pass

  def boardShow(self, r: uint8, g: uint8, b: uint8) -> None:
    """
    板载七彩灯显示
    
    r/g/b-红绿蓝, 取值范围0-100 
    """
    pass

