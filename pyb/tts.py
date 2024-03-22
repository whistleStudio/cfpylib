from pyb._customtype import uint8

# 需连接在主控P1-6接口
class TTS:
  """ 语音合成模块(IIC) """

  def __init__(self) -> None:
    pass

  def setMode(self, fgVol: uint8, bgVol: uint8, speed: uint8) -> None:
    """ 
    设置语音属性

    fgVol - 前景音音量: 0-16;
    bgVol - 背景音音量: 0-16;
    speed - 语速: 0-5
    """
    pass

  def playBeep(self, hintId: uint8) -> None:
    """
    播放提示音

    hintId - 内置提示音编号: 1-48
    """
    pass

  def playTextH(self, text: str, bgmId: uint8) -> None:
    """  
    播放文本

    text - 自定义文本 (需转GBK编码字节)
    bgmId - 背景音编号: 
    """
    pass