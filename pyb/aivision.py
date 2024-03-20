from _customtype import uint8
from typing import Literal

AIVisionAddr = Literal[0x32]
ZoomMode = Literal["zoom1", "zoom2", "zoom3", "zoom4"]
BasicMode = Literal["colorDetection", "cardDetection"]
AdvancedMode = Literal["faceRecognition", "KNNRecognition", "objectADetection", "objectBDetection", "objectCDetection", "objectDDetection", "objectEDetection", "objectFDetection"]
DetectAttr = Literal["X", "Y", "width", "height", "ID", "confidence", "R", "G", "B", "colorLabel"]
ColorName = Literal["black", "white", "red", "yellow", "green", "cyan", "blue", "purple"]

class AIVision:
  """ 
  视觉识别传感器 
  
  e.g.

  from pyb import AIVision
  from time import sleep

  sleep(3) #视觉识别模块上电有短暂启动时间, 此时无法操作模块
  aiv = AIVision(0x32)
  aiv.openBasicDetection("cardDetection")
  while True:
    if aiv.getCardDetection() > 0:
      print(aiv.pickCardDetection(1, "ID"))
    sleep(0.5)
  """



  def __init__(self, addr: AIVisionAddr) -> None:
    """ 
    addr - 硬件地址: 0x32
    """
    pass

  def getVersion(self) -> uint8:
    """ 获取视觉识别传感器固件版本号 """
    return 0
  
  def setAwb(self) -> None:
    """ 
    启动自动白平衡

    需要约2秒时长校正 
    """
    pass

  def setZoom(self, zoom: ZoomMode) -> None:
    """ 
    设置变焦模式

    zoom - 模式: zoom1/2/3/4
    """
    pass

  def setLEDIntensity(self, intensity: uint8) -> None:
    """ 
    设置补光灯强度

    intensity - 强度:0-100
    """
    pass

  def setThresholdBW(self, black: uint8, white: uint8, brightness: uint8, saturation: uint8) -> None:
    """ 
    设置黑色、白色、亮度、饱和度的阈值

    black - 黑色:0-255;
    white - 白色:0-255;
    brightness - 亮度:0-255;
    saturation - 饱和度:0-255
    """

  def openBasicDetection(self, mode: BasicMode) -> None:
    """ 
    开启指定基础功能(允许多个)

    mode - 基础功能: colorDetection(色块检测)/cardDetection(卡片检测)
    """
    pass

  def closeBasicDetection(self, mode: BasicMode) -> None:
    """
    关闭指定基础功能

    mode - 基础功能: colorDetection(色块检测)/cardDetection(卡片检测)
    """
    pass

  def openAdvancedDetection(self, mode: AdvancedMode) -> None:
    """
    开启指定高级功能(仅允许一个)

    mode - 高级功能: faceRecognition(人脸检测)/KNNRecognition(KNN分类识别)/ objectA/B/C/D/E/FDetection(物体A/B/C/D/E/F检测)
    """
    pass

  def closeAavancedDetection(self, mode: AdvancedMode) -> None:
    """
    关闭指定高级功能

    mode - 高级功能: faceRecognition(人脸检测)/KNNRecognition(KNN分类识别)/ objectA/B/C/D/E/FDetection(物体A/B/C/D/E/F检测)
    """
    pass

  def setFaceRecognition(self, detectCL: uint8, identifyCL: uint8, faceArea: int) -> None:
    """
    设置人脸识别功能参数

    detectCL - 检测置信度: 0-99;
    identifyCL - 识别置信度: 0-99;
    faceArea - 最小人脸面积: 0-10000(坐标区间100*100)
    """
    pass

  def setObjectDetection(self, detectCL: uint8, objectArea: int) -> None:
    """
    设置物体检测功能参数

    detectCL - 检测置信度: 0-99;
    objectArea - 最小物体面积: 0-10000(坐标区间100*100)
    """
    pass

  def setKNNRecognition(self, K: uint8) -> None:
    """
    设置KNN分类识别功能参数

    K - K参数: 1-8
    """
    pass

  def inputFaceID(self, faceId: uint8) -> None:
    """ 
    当前拍摄人脸录入至指定编号

    faceId - 编号: 1-64
    """
    pass

  def faceIDAvailable(self, faceId: uint8) -> bool:
    """
    校验指定编号人脸是否录入成功
    
    faceId - 编号: 1-64
    """
    return False

  def deleteFaceID(self, faceId: uint8) -> None:
    """
    删除指定编号人脸

    faceId - 编号: 1-64 / 255(全部删除)
    """
    pass

  def inputKNNID(self, knnId: uint8) -> None:
    """
    当前拍摄样本录入至指定编号

    knnId - 编号: 1-8
    """
    pass

  def deleteKNNID(self, knnId: uint8) -> None:
    """
    删除指定编号样本

    knnId - 编号: 1-8 / 255(全部删除)
    """
    pass

  def getColorRecognition(self, x: uint8, y: uint8, w: uint8, h: uint8) -> None:
    """
    检测指定区域颜色

    x - 检测中心x坐标: 0-100;
    y - 检测中心y坐标: 0-100;
    w - 检测区域宽度: 0-100;
    h - 检测区域高度: 0-100
    """
    pass

  def getColorDetection(self, w: uint8, h: uint8, color: ColorName) -> uint8:
    """
    返回识别到的指定色块数量

    w - 识别区域宽度: 0-100;
    h - 识别区域高度: 0-100;
    color - 颜色名称: black(黑), blue(蓝), green(绿), yellow(黄), red(红), white(白), cyan(青), purple(紫)
    """
    return 0
  
  def getCardDetection(self) -> uint8:
    """ 
    返回识别到的卡片数量
    
    同时会对识别到的卡片的属性重新赋值
    """
    return 0
  
  def getFaceRecognition(self) -> uint8:
    """ 
    返回识别到的人脸数量 
    
    同时会对识别到的人脸的属性重新赋值
    """
    return 0
  
  def getObjectDetection(self) -> uint8:
    """ 
    返回识别到的物体数量
    
    同时会对识别到的物体属性重新赋值
    """
    return 0
  
  def pickColorDetection(self, areaSort: uint8, attr: DetectAttr) -> uint8:
    """
    areaSort - 面积大小顺序: 1(最大)-5(最小)
    attr - 识别到的对象属性: X(中心点x坐标)/Y(中心点y坐标)/width(宽度)/height(高度)/ID/confidence(置信度)/R(红色通道)/G(绿色通道)/B(蓝色通道)/colorLabel(颜色编号)
    """
    return 1
  
  def pickCardDetection(self, areaSort: uint8, attr: DetectAttr) -> uint8:
    """
    areaSort - 面积大小顺序: 1(最大)-5(最小)
    attr - 识别到的对象属性: X(中心点x坐标)/Y(中心点y坐标)/width(宽度)/height(高度)/ID/confidence(置信度)/R(红色通道)/G(绿色通道)/B(蓝色通道)/colorLabel(颜色编号)
    """
    return 1
  
  def pickFaceDetection(self, areaSort: uint8, attr: DetectAttr) -> uint8:
    """
    areaSort - 面积大小顺序: 1(最大)-5(最小)
    attr - 识别到的对象属性: X(中心点x坐标)/Y(中心点y坐标)/width(宽度)/height(高度)/ID/confidence(置信度)/R(红色通道)/G(绿色通道)/B(蓝色通道)/colorLabel(颜色编号)
    """
    return 1
  
  def pickObjectDetection(self, areaSort: uint8, attr: DetectAttr) -> uint8:
    """
    areaSort - 面积大小顺序: 1(最大)-5(最小)
    attr - 识别到的对象属性: X(中心点x坐标)/Y(中心点y坐标)/width(宽度)/height(高度)/ID/confidence(置信度)/R(红色通道)/G(绿色通道)/B(蓝色通道)/colorLabel(颜色编号)
    """
    return 1 
  
  def getKNNRecognition(self) -> uint8:
    """
    识别到的图像类别
    """
    return 1
