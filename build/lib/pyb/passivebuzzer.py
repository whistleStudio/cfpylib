from typing import Literal
from _customtype import IoPort

Pitch = Literal[
  "C4", "D4", "E4", "F4", "G4", "A4", "B4",
  "C5", "D5", "E5", "F5", "G5", "A5", "B5",
  "C6", "D6", "E6", "F6", "G6", "A6", "B6",
  "C7", "D7", "E7", "F7", "G7", "A7", "B7",
  "C8", "D8"
  ]

Duration = Literal[
  "1/2", "1/4", "3/4", "1/8", "3/8", "5/8",
  "7/8", "1/16", "1/32", "1", "2", "0"
  ]

class PassiveBuzzer:
  """ 无源蜂鸣器 """

  def __init__(self, port: IoPort) -> None:
    """ 
    port - 接口编号P1-8: A0、A2、A4、A6、B0、C0、C2、C4
    """
    pass

  def tone(self, p: Pitch, dur: Duration) -> None:
    """ 
    发出指定节拍长度音调

    p - 音调: C4-D8;
    dur - 节拍

    e.g.
    
    PassiveBuzzer("A0").tone("C4", "1")
    """