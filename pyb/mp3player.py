from _customtype import uint8
from typing import Literal, Annotated
from dataclasses import dataclass

@dataclass
class ValRange:
  low: int
  high: int

PlayMode = Literal[1, 2, 3, 4]
Volume = Annotated[int, ValRange(0, 31)]
LoopMode = Literal[0, 1, 2, 3]

# 需连接在主控P1-6接口
class MP3Player:
  """ MP3音乐播放器(IIC) """

  def __init__(self) -> None:
    pass

  def setPlayMode(self, mode: PlayMode) -> None:
    """
    设置播放模式

    mode - 模式: 1(播放/暂停), 2(停止), 3(下一首), 4(上一首) 
    """
  
  def setVolume(self, vol: Volume) -> None:
    """  
    设置播放音量

    vol - 音量: 0-31
    """
    pass

  def rootPlay(self, songNum: uint8) -> None:
    """ 
    播放根目录下指定编号曲目

    songNum - 曲目编号: 0-255
    
    [注]MP3存储卡内文件命名应以四位数打头形式, 如0001双截棍.mp3, 0002littlestar.mp3

    e.g.

    MP3Player().rootPlay(1)
    """
    pass

  def folderPlay(self, folderNum: uint8, songNum: uint8) -> None:
    """ 
    播放指定目录下指定曲目

    folderNum - 目录编号: 0-255;
    songNum - 曲目编号: 0-255
    
    [注]MP3存储卡内文件夹、文件命名应以四位数打头形式, 如0001周杰伦, 0001分裂.mp3

    e.g.

    MP3Player().folderPlay(1, 1)
    """
    pass

  def setLoopMode(self, mode: LoopMode) -> None:
    """ 
    设置循环模式
    
    mode - 模式: 0(不循环), 1(单曲循环), 2(所有曲目循环), 3(随机播放) 
    """