import cv2
path=('C:/Users/m/OneDrive/Desktop/imageprocessing/grid_2.png')
image=cv2.imread(path)
image=cv2.resize(image,(540,540))

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edged=cv2.Canny(gray,0,255)
ret,binary = cv2.threshold(edged,0,255,cv2.THRESH_BINARY)



contor,hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cont_count=0
copyimage=image.copy()
list=[]
for i in  contor:
    if cv2.contourArea(i)>16000 and cv2.contourArea(i)<18000:
        cont_count+=1
        list.append(i)

newlist=[]
for i in range(len(list)):
    if i%2==0:
        newlist.append(list[i])
l=[]
h=[]
boximages=[]
for i in range(len(newlist)):
    single=newlist[i]
    for j in single:
        pingle=j
        [L,H]=pingle[0]
        l.append(L)
        h.append(H)
    xl=min(l)
    xh=max(l)
    yl=min(h)
    yh=max(h)
    cc=image[yl:yh,xl:xh]
    boximages.append(cc)
    xl=0
    xh=0
    yl=0
    yh=0
    l=[]
    h=[]

for i in boximages:
    cv2.imshow('m',i)
    cv2.waitKey(0)






   


