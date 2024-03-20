from _customtype import char, UARTPort

class BlueToothAPP:
  """ 
  蓝牙通讯模块\n
  结合微信小程序【创趣蓝牙】使用
  """

  # 蓝牙应用水平/垂直分量 ±100
  rockerX: char
  rockerY: char

  # 蓝牙应用按钮A/B/C/D, True(按下)/False(松开)
  buttonA: bool
  buttonB: bool
  buttonC: bool
  buttonD: bool

  def __init__(self, port: UARTPort) -> None:
    """ 
    port - 接口编号: 1(P7), 2(P8)
    """
    pass

  def receive(self) -> bool:
    """ 
    串口是否有数据可读 

    e.g.\n
    BluAPP1 = BlueToothAPP(1)
    if BluAPP1.receive():
      x = BluAPP1.rockerX
      a = BluAPP2.buttonA 
    """
    return False
  