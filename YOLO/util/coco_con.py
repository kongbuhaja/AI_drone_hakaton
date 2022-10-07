import cv2
import glob

#0, 4, 14
load_text_dir='./lval2014txt/'
save_text_dir='./sval2014/'
load_image_dir='./lval2014img/val2014/'
save_image_dir='./sval2014/'
texts=glob.glob(load_text_dir + '*.txt')
file_list=[]
i=0
for text in texts:
    folder, file=text.split('\\')
    lbl, cx, cy, w, h=[],[],[],[],[]
    result=[]
    f=open(text,'r')
    lines=f.readlines()
    for line in lines:
##        print(line)
        l,c1,c2,w1,h1,_=line.split(' ')
        lbl.append(l)
        cx.append(c1)
        cy.append(c2)
        w.append(w1)
        h.append(h1)
    for j in range(len(lbl)):
        if lbl[j]=='14':
            result.append('4'+' '+cx[j]+' '+cy[j]+' '+w[j]+' '+h[j]+'\n')
        else:
            continue
    if len(result)!=0:
##        print(file)
##        print(i)
        i+=1
        fl=open(save_text_dir + 'bird_v3_'+str(i)+'.txt', 'w')
        for info in result:
            fl.write(info)
        fl.close()
        file_list.append(file[:len(file)-4])
        if(len(file_list)==100):
            break;
    f.close()
i=0
for file in file_list:
    i+=1
    img=cv2.imread(load_image_dir+file+'.jpg')
    cv2.imwrite(save_image_dir+'bird_v3_'+str(i)+'.jpg',img)
        
