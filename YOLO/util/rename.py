import cv2
import glob

classes='plain_bird'
l_dir='./'+classes+'_/'
s_dir='./'+classes+'/'
images=glob.glob(l_dir+'*.jpg')
i=0
for image in images:
    i+=1
##    img=cv2.imread(image)
##    cv2.imwrite(s_dir + classes + '_' + str(i) + '.jpg',img)

texts=glob.glob(l_dir+'*.xml')

##i=0
##for text in texts:
##    a=0
##    i+=1
##    rf=open(text, 'rt', encoding='utf-8')
##    wf=open(s_dir + classes + '_' + str(i) +'.xml', 'wt', encoding='utf-8')
##    while True:
##        line=rf.readline()
##        a+=1
##        if not line:break
##        if a==3:
##            wf.write('\t<filename>'+classes+'_'+str(i)+'.jpg</filename>\n')
##        else:
##            wf.write(line)
##    wf.close()
##    rf.close()
        
        
##text=texts[0]
##f=open(text, 'rt', encoding='utf-8')
##a=0
##
##while True:
##    line=f.readline()
##    if not line:break
##    a+=1
##    if a==3:
##        t=line
##    print(a,' :::: ', line)
