import numpy as np
import cv2
from collections import Counter


img=cv2.imread("t3.jpg")
row,col,w=img.shape

def pop(img,bit):
    img1 = []
    r, g, b = cv2.split(img)
    for i in range(0, row, 1):
        for j in range(0, col, 1):
            img1.append(img[i][j])
    # print(len(img1))
    for i in range(0, len(img1), 1):
        img1[i] = img1[i].tolist()
    # print(type(img1[0]), img1[0])

    for i in range(0, len(img1), 1):
        img1[i] = img1[i][0] * 1000000 + img1[i][1] * 1000 + img1[i][2]
        img1[i] = "%09d" % img1[i]
    # print(img1)
    result = Counter(img1)
    result = sorted(result.items(), key=lambda item: item[1], reverse=True)
    # print(result)
    point = [[0] * 3] * bit
    for i in range(0, bit, 1):
        point[i] = int(result[i][0][0:3]), int(result[i][0][3:6]), int(result[i][0][6:9])
    print(point)
    distance = np.zeros([row, col, bit], dtype=int)
    for i in range(0, row, 1):
        for j in range(0, col, 1):
            for k in range(0, bit, 1):
                distance[i][j][k] = pow((int(img[i][j][0]) - point[k][0]), 2) + pow(
                    (int(img[i][j][1]) - point[k][1]), 2) + pow((int(img[i][j][2]) - point[k][2]), 2)

    for i in range(0, row, 1):
        for j in range(0, col, 1):
            list = distance[i][j].tolist()
            index = list.index(min(list))
            img[i][j][0] = point[index][0]
            img[i][j][1] = point[index][1]
            img[i][j][2] = point[index][2]
            list.clear()
    return img
# for i in [4,16,64,256]:
#     cv2.imwrite("popularity-"+str(i)+"-t2.jpg", pop(img,i))
img=pop(img,4)
# cv2.imshow("plot",img)
# cv2.waitKey(0)
cv2.imwrite("popularity-4  -t3.jpg", img)


