from pyb._customtype import uint8

# 需连接在主控P1-6接口
class Gyro:
  """ 陀螺仪(IIC) """

  # 绕X/Y/Z轴的倾斜角度, 需先调用.read()方法
  angleX: uint8
  angleY: uint8
  angleZ: uint8

  # 绕X/Y/Z轴的转动角速度, 需先调用.read()方法
  angularvX: uint8
  angularvY: uint8
  angularvZ: uint8


  def __init__(self) -> None:

    pass

  def read(self) -> None:
    """ 
    刷新一次实时读取数据

    e.g.
    
    Gyro().read()
    Gyro.angleX
    """
    pass


