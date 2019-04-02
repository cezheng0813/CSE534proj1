import numpy
import cv2
img=cv2.imread("t2.jpg")
r,g,b=cv2.split(img)
row,col=r.shape
b_dif=b.max()-b.min()
r_dif=r.max()-r.min()
g_dif=g.max()-g.min()
print(r_dif,g_dif,b_dif)
print(numpy.median(r),numpy.median(g),numpy.median(b))
r_big=r>numpy.median(r)
pix_big = numpy.sum(r_big==True)
pix_small= numpy.sum(r_big==False)
x0=0
y0=0
z0=0
x1=0
y1=0
z1=0
x10=0
y10=0
z10=0
x11=0
y11=0
z11=0
list_r=[]
list_r1=[]
list_b=[]
list_b1=[]
list_g=[]
list_g1=[]
for i in range(0,row,1):
    for j in range(0,col,1):
        if img[i][j][0]<=numpy.median(r):
            list_r.append(img[i][j][0])
            list_g.append(img[i][j][1])
            list_b.append(img[i][j][2])
        else:
            list_r1.append(img[i][j][0])
            list_g1.append(img[i][j][1])
            list_b1.append(img[i][j][2])
dif_r=max(list_r)-min(list_r)
dif_g=max(list_g)-min(list_g)
dif_b=max(list_b)-min(list_b)
dif_r1=max(list_r1)-min(list_r1)
dif_g1=max(list_g1)-min(list_g1)
dif_b1=max(list_b1)-min(list_b1)
# print(dif_b,dif_b1)
b_array=numpy.array(list_b)
b1_array=numpy.array(list_b1)
median_b0=numpy.median(b_array)
median_b1=numpy.median(b1_array)
# print(median_b0,median_b1)
count=0
count1=0
count2=0
count3=0
for i in range(0,row,1):
    for j in range(0,col,1):
        if img[i][j][0]<=numpy.median(r):
            if  img[i][j][2]<=median_b0:
                x0 = img[i][j][0] + x0
                y0 = img[i][j][1] + y0
                z0 = img[i][j][2] + z0
                count=count+1
            else:
                x1 = img[i][j][0] + x1
                y1 = img[i][j][1] + y1
                z1 = img[i][j][2] + z1
                count1 = count1 + 1
        else:
            if img[i][j][2]<=median_b1:
                x10 = img[i][j][0] + x10
                y10 = img[i][j][1] + y10
                z10 = img[i][j][2] + z10
                count2 = count2 + 1
            else:
                x11 = img[i][j][0] + x11
                y11 = img[i][j][1] + y11
                z11 = img[i][j][2] + z11
                count3 = count3 + 1
x0=int(x0/count)
y0=int(y0/count)
z0=int(z0/count)
x1=int(x1/count1)
y1=int(y1/count1)
z1=int(z1/count1)
x10=int(x10/count2)
y10=int(y10/count2)
z10=int(z10/count2)
x11=int(x11/count3)
y11=int(y11/count3)
z11=int(z11/count3)
distance=[]
d=0
for k in range(0,row,1):
    for p in range(0,col,1):
        dis=(img[k][p][0]-x0)*(img[k][p][0]-x0)+(img[k][p][1]-y0)*(img[k][p][1]-y0)+(img[k][p][2]-z0)*(img[k][p][2]-z0)
        dis2=(img[k][p][0]-x1)*(img[k][p][0]-x1)+(img[k][p][1]-y1)*(img[k][p][1]-y1)+(img[k][p][2]-z1)*(img[k][p][2]-z1)
        dis3=(img[k][p][0] - x10) * (img[k][p][0] - x10) + (img[k][p][1] - y10) * (img[k][p][1] - y10) + (img[k][p][2] - z10) * (img[k][p][2] - z10)
        dis4=(img[k][p][0] - x11) * (img[k][p][0] - x11) + (img[k][p][1] - y11) * (img[k][p][1] - y11) + (img[k][p][2] - z11) * (img[k][p][2] - z11)
        distance.append(dis)
        distance.append(dis2)
        distance.append(dis3)
        distance.append(dis4)
        index_dis=distance.index(min(distance))
        if index_dis==0:
            img[k][p][0] = x0
            img[k][p][1] = y0
            img[k][p][2] = z0
        elif index_dis==1:
            img[k][p][0] = x1
            img[k][p][1] = y1
            img[k][p][2] = z1
        elif index_dis==2:
            img[k][p][0] = x10
            img[k][p][1] = y10
            img[k][p][2] = z10
        elif index_dis==3:
            img[k][p][0] = x11
            img[k][p][1] = y11
            img[k][p][2] = z11
        distance.clear()

print(img)
cv2.imwrite("median-2bit-2.jpg", img)
