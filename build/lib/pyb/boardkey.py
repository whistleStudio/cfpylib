from pyb._customtype import KeyType

class BoardKey:
  """ 板载按键 """

  def __init__(self, key: KeyType) -> None:
    """  
    key - 按键类别: left(左)、right(右)、up(上)、down(下)、center(中)
    """
    pass
  
  def value(self) -> bool:
    """ 
    读取板载按键状态\n
    返回值: True(按下)/False(松开)
    """
    return False
