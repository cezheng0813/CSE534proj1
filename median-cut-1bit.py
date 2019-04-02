import numpy
import cv2
img=cv2.imread("t2.jpg")
r,g,b=cv2.split(img)
row,col=r.shape
b_dif=b.max()-b.min()
r_dif=r.max()-r.min()
g_dif=g.max()-g.min()
print(b_dif,r_dif,g_dif)
print(numpy.median(b),numpy.median(g),numpy.median(r))
r_big=r>numpy.median(r)
pix_big = numpy.sum(r_big==True)
pix_small= numpy.sum(r_big==False)
x=0
y=0
z=0
xb=0
yb=0
zb=0
for i in range(0,row,1):
    for j in range(0,col,1):
        if img[i][j][0]<=numpy.median(r):
            x = img[i][j][0] + x
            y = img[i][j][1] + y
            z = img[i][j][2] + z
        else:
            xb = img[i][j][0] + xb
            yb = img[i][j][1] + yb
            zb = img[i][j][2] + zb
x1=int(x/pix_small)
y1=int(y/pix_small)
z1=int(z/pix_small)
xb1=int(xb/pix_big)
yb1=int(yb/pix_big)
zb1=int(zb/pix_big)
for k in range(0,row,1):
    for p in range(0,col,1):
        dis=(img[k][p][0]-x1)*(img[k][p][0]-x1)+(img[k][p][1]-y1)*(img[k][p][1]-y1)+(img[k][p][2]-z1)*(img[k][p][2]-z1)
        dis2=(img[k][p][0]-xb1)*(img[k][p][0]-xb1)+(img[k][p][1]-yb1)*(img[k][p][1]-yb1)+(img[k][p][2]-zb1)*(img[k][p][2]-zb1)
        if dis<dis2:
            img[k][p][0]=x1
            img[k][p][1] = y1
            img[k][p][2] = z1
        else:
            img[k][p][0] = xb1
            img[k][p][1] = yb1
            img[k][p][2] = zb1
# print(img)
# cv2.imshow("plot", img)
# cv2.waitKey(0)
cv2.imwrite("median-1bit-2.jpg", img)