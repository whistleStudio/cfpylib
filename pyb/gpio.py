from pyb._customtype import short, uint8, IoPort


class Pin:
  IN: None
  OUT_PP: None

  def __init__(self, port: IoPort, mode) -> None:
    """ 
    port - 接口编号P1-8: A0、A2、A4、A6、B0、C0、C2、C4;
    mode - 模式: Pin.IN(输入)、Pin.OUT_PP(推挽输出)
    """
    pass

  def __call__(self, val: bool) -> None:
    """
    val - True(高)/False(低)电平;
    自动类型转化, 比如1->True, 0->False
    """
    pass
  
  def value(self) -> bool:
    """
    读取接口数字量

    返回值: True(高)/False(低)电平
    
    e.g.
    Pin("A0",Pin.IN).value()
    """
    return False


class PWM:
  def __init__(self, port: IoPort, freq: short = 1000) -> None:
    """ 
    port - 接口编号: A0(P1)、A2(P2)、A6(P4)、B0(P5);
    freq - PWM波频率, 默认1000
    """
    pass

  def out(self, val: uint8) -> None:
    """ 
    out - 占空比: 取值0-100
    """
    pass


class ADC:
  def __init__(self, port: IoPort) -> None:
    """
    port - 接口编号P1-8: A0、A2、A4、A6、B0、C0、C2、C4;
    """
    pass

  def read(self) -> short:
    """
    读取接口模拟量
    
    返回值: 0-1023 
    """
    return 0