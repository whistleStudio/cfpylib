from typing import Literal


ServoPort = Literal["A0", "A1", "A2", "A3", "A6", "A7", "B0", "B1"]

class CFunServo:
  """ 舵机 """

  def __init__(self, port: ServoPort) -> None:
    """
    port - 舵机接口: P1(A0/A1), P2(A2/A3), P4(A6/A7), P5(B0/B1) 
    """
    pass

  def angle(self, v: float) -> None:
    """
    转动一定角度\n
    v - PWM占空比: 0(最小角度)-100(最大角度); 转动角度由电机自身参数决定

    e.g.\n
    CFunServo("A0").angle(50)
    """
    pass