import cv2 as cv

image_path = "images/jf1.jpg"
image = cv.imread(image_path)

# 查看图像的尺寸信息
'''
    image1是一个多维(三维)数组，三个维度分别代表图片的高(H)、宽(W)和颜色通道数(C)
    对于彩色图片，颜色通道数为3，分别代表蓝色(B)、绿色(G)和红色(R)分量
    shape属性由3个值组成：
        第1个值表示图片的高，同时也代表数组的行数(将图片看成若干行若干列的二维像素集合)
        第2个值表示图片的宽，同时也代表数组的列数
        第3个值表示图片的颜色通道数，可认为代表数组中指定的行列单元格中的颜色元素数
'''
print("图像尺寸(高x宽x颜色通道数): ", image.shape)

# 查看图像每个颜色通道的颜色值数据类型
print("颜色色彩值数据类型：", image.dtype)       # uint8代表用1个字节表示一个颜色值