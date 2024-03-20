from _customtype import uint8, short
from typing import Literal

MotorPort = Literal[1, 2, 3, 4]
MotorDir = Literal["forward", "reverse"]

class DCMotor:
  """
  电机
  """

  def __init__(self, port: MotorPort|uint8) -> None:
    """
    port - 电机接口M1-4: 1-4
    """
    pass

  def setDirPower(self, dir: MotorDir|str, p: uint8) -> None:
    """
    设置电机转动(动力值形式)

    dir - 转动方向: forward(正)/reverse(反)
    p - 动力值: 0-100

    e.g.
    DCMotor(1).setDirPower("forward", 60)
    """
    pass

  def setRatio(self, ratio: float = 51) -> None:
    """
    设置减速比
    """
    pass

  def setDirSpeed(self, dir: MotorDir|str, speed: short) -> None:
    """
    设置编码电机转动(圈/分钟形式)

    dir - 转动方向: forward(正)/reverse(反);
    speed - 速度值: 单位 圈/分钟
    """
    pass

  def setDirSpeedC(self, dir: MotorDir|str, speed: short, cycle: float) -> None:
    """
    设置编码电机转动固定圈数后停止

    dir - 转动方向: forward(正)/reverse(反);
    speed - 速度值: 单位 圈/分钟;
    cycle - 目标圈数

    [注]该方法在电机未达到指定圈数前, 不会阻塞线程, 在连续调用电机转动相关方法时, 需确保二者间隔时长充分
    """
    pass

  def setDirSpeedA(self, dir: MotorDir|str, speed: short, angle: short) -> None:
    """
    设置编码电机转动固定角度后停止

    dir - 转动方向: forward(正)/reverse(反);
    speed - 速度值: 单位 圈/分钟;
    angle - 目标角度

    [注]该方法在电机未达到指定角度前, 不会阻塞线程, 在连续调用电机转动相关方法时, 需确保二者间隔时长充分
    """
    pass

  def setDirSpeedT(self, dir: MotorDir|str, speed: short, t: float) -> None:
    """
    设置编码电机转动固定时长后停止
    
    dir - 转动方向: forward(正)/reverse(反);
    speed - 速度值: 单位 圈/分钟;
    t - 目标时长: 单位 秒
    """

  def readCycle(self) -> float:
    """
    读取编码电机转动的圈数
    """
    return 0.0

  def readAngle(self) -> float:
    """
    读取编码电机转动的角度
    """
    return 0.0
  
  def clearCycle(self) -> None:
    """
    重置记录的转动角度/圈数; 归零
    """
    pass
