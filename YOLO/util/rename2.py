import cv2
import glob

l_dir='./img/'
s_dir='./img2/'
images=glob.glob(l_dir+'*.jpg')
texts=glob.glob(l_dir+'*.txt')

i=0
for image in images:
    i+=1
    img=cv2.imread(image)
    cv2.imwrite(s_dir + 'Cervidae_v2_' + str(i) + '.jpg',img)


i=0
for text in texts:
    i+=1
    f=open(text,'r')
    fl=open(s_dir + 'Cervidae_v2_'+ str(i) + '.txt', 'w')
    lines=f.readlines()
    for line in lines:
        fl.write(line)
    f.close()
    fl.close()
    
