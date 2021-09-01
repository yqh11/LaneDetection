# coding: utf-8
carWidth = 160
carHeight = 240
chessboardSize = 80
shiftWidth = 120
shiftHeight = 120
innerShiftWidth = 0
innerShiftHeight = 0
totalWidth = carWidth + 2 * chessboardSize + 2 * shiftWidth
totalHeight = carHeight + 2 * chessboardSize + 2 * shiftHeight

x1 = shiftWidth + chessboardSize + innerShiftWidth
x2 = totalWidth - x1
y1 = shiftHeight + chessboardSize + innerShiftHeight
y2 = totalHeight - y1

frontShape = (totalWidth, y1)
leftShape = (totalHeight, x1)
# 四个角点的坐标分别为 $(x1,y1), (x2,y1), (x1,y2),(x2,y2)
