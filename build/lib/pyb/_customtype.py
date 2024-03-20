from typing import Any, Literal, Annotated
from dataclasses import dataclass

@dataclass
class ValueRange:
  min: int
  max: int

uint8 = Annotated[int, ValueRange(0, 255)]
uint16 = Annotated[int, ValueRange(0, 65535)]
short = Annotated[int, ValueRange(-32768, 32767)]
char = Annotated[int, ValueRange(-128, 127)]

# 分别对应P1-P8
IoPort = Literal["A0", "A2", "A4", "A6", "B0", "C0", "C2", "C4"]

# 分别对应P1-P6
IICPort = Literal["A0", "A2", "A4", "A6", "B0", "C0"]

# 分别对应P7-P8
UARTPort = Literal[1, 2]

KeyType = Literal["left", "right", "up", "down", "center"]

# 颜色id
ColorId = Literal[1, 2, 3, 4, 5, 6, 7, 8]