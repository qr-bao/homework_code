import cv2 as cv

# 指定待装载的图片路径
image1_path = "images/jf1.jpg"
image2_path = "images/jf2.jpg"

# 创建名为"tutorials"的窗口以显示图片
window_name = "tutorials"
cv.namedWindow(window_name)

# 装载并显示图片1
image1 = cv.imread(image1_path)
cv.imshow(window_name, image1)

# 等待用户按任意键后继续运行后续代码
cv.waitKey()

# 装载并显示图片2
image2 = cv.imread(image2_path)
cv.imshow(window_name, image2)

# 等待用户按任意键后继续运行后续代码
cv.waitKey()

# 销毁所有窗口
cv.destroyAllWindows()
