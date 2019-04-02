import numpy
import cv2

def ostu(count,gray_img):
    max1=0
    for T in range(0, 256, 1):
        back=0
        front_point=gray_img>T
        back_point=gray_img<=T
        for j in range(0, T + 1, 1):
            back = count[j] + back
        front=total_point-back
        w0=front/total_point
        w1=back/total_point
        if front==0:
            break
        u0=float(numpy.sum(gray_img*front_point)/front)
        u1=float(numpy.sum(gray_img*back_point)/back)
        g=float(w0*w1*(u0 - u1)*(u0 - u1))
        if g>max1:
            max1=g
            max_T=T
    return max_T

def plot(T,gray_img):
    row, col = gray_img.shape
    for a in range(row):
        for b in range(col):
            if gray_img[a,b]>T:
                gray_img[a, b]=255
            else:
                gray_img[a, b]=0
    cv2.imshow("plot",gray_img)
    cv2.waitKey(0)


img=cv2.imread("t3.jpg")
gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
row,col=gray_img.shape
total_point=row*col
count=[]
gray_level=[0,255]
for i in range(0,256,1):
    a=numpy.sum(gray_img==i)
    count.append(a)
T=ostu(count,gray_img)
plot(T,gray_img)
cv2.imwrite("Otsu-gray3.jpg", gray_img)