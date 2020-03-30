def shuliang():
    txt=t11.get(SEL_FIRST,SEL_LAST)
    s1=0
    for i in txt:
        if i==' ':s1=s1+1
        if i=='—':s1=s1+1
    mb.showinfo('统计','单词数量：'+str(s1+1))
    
def cishu():
    rcs=Tk()
    rcs.title('统计——词频')
    rcs.geometry('340x600')
    txt=t11.get(SEL_FIRST,SEL_LAST)
    txt=str(txt)
    a1=txt.split(' ')
    for i in range(0,len(a1)):
        a1[i]=str(a1[i])
        if a1[i]=='':continue
        b=''
        for j in a1[i]:
            if 65<=ord(j)<=90 or 97<=ord(j)<=122:
                if 65<=ord(j)<=90:b=b+chr(ord(j)+32)
                else:b=b+j
        a1[i]=b
    a11=set()
    a12=[]
    a13=[]
    for i in a1:
        if i in a11:a13[a12.index(i)]=a13[a12.index(i)]+1
        else:
            a11.add(i)
            a12.append(i)
            a13.append(1) 
    lb1=Listbox(rcs,width=40)  
    ly2=Scrollbar(rcs)  
    ly2.pack(side=RIGHT,fill=Y)  
    lb1['yscrollcommand']=ly2.set 
    for i in range(0,len(a12)):  
        lb1.insert(END,a12[i]+':'+str(a13[i]))  
    lb1.pack(side=LEFT,fill=BOTH)  
    ly2['command']=lb1.yview  

def guanjianci():
    rgj=Toplevel()
    rgj.title('统计——关键词')
    rgj.geometry('400x400')
    txt=t11.get(1.0,END)
    txt=str(txt)
    a1=txt.split(' ')
    for i in range(0,len(a1)):
        a1[i]=str(a1[i])
        b=''
        for j in a1[i]:
            if 65<=ord(j)<=90 or 97<=ord(j)<=122:
                if 65<=ord(j)<=90:b=b+chr(ord(j)+32)
                else:b=b+j
        a1[i]=b
    a11=set()
    a12=[]
    a13=[]
    a14=[]
    a15=[]
    for i in a1:
        if i in stoplist:continue
        if i in a11:a13[a12.index(i)]=a13[a12.index(i)]+1
        else:
            a11.add(i)
            a12.append(i)
            a13.append(1)
    for j in range(0,6):
        for i in range(0,len(a13)):
            if a13[i]==max(a13):
                a14.append(a12[i])
                a15.append(a13[i])
                del a13[i]
                del a12[i]
                break
    lb2=Listbox(rgj,height=5)
    for i in range(0,6):
        lb2.insert(END,a14[i]+':'+str(a15[i]))  
        lb2.pack()  
    plt.bar(range(6),a15,fc='b',tick_label=a14,label='次数')
    plt.xlabel('单词')
    plt.ylabel('数值')
    plt.title('关键词')
    plt.savefig('result.png')
    #plt.show()
    photo=PhotoImage(file='result.png')
    i3=Label(rgj,image=photo)
    i3.image=photo
    i3.pack()