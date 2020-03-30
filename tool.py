def zhuanhuan():
    t21=Text(r1,height=20,width=103,undo=True)
    s2=Scrollbar(r1)
    s2.config(command=t21.yview)
    s2.grid(row=2,column=1,sticky=NS)
    t21.config(yscrollcommand=s2.set)  
    t21.grid(row=2,column=0)
    txt=t11.get(1.0,END)
    a=''
    for i in txt:
        if 65<=ord(i)<=90 or 97<=ord(i)<=122:
            if 65<=ord(i)<=90:a=a+chr(ord(i)+32)
            else:a=a+i
    t21.insert(INSERT,a)
    def qingchu():
        t21.delete(1.0,END)
        t21.grid_forget()
        s2.grid_forget()
        b22.grid_forget()
    b22=Button(r1,text='清除',command=qingchu)
    b22.grid(row=3)

def chazhao():
    rcz=Tk()
    rcz.title('查找')
    l23=Label(rcz,text='请输入查找的内容：')
    l23.grid(row=0,column=0,pady=5,padx=10,sticky=E)
    e24=Entry(rcz,width=20,show=None)
    e24.grid(row=0,column=1,pady=5,padx=20,sticky=W)    
    def queren1():
        txt=t11.get(1.0,END)
        index1=1.0
        word=e24.get()
        pos=[i.start() for i in re.finditer(word,txt)]
        pos=str(pos)
        rcz.destroy()
        l27=Label(r1,text='位置索引：'+pos)
        l27.grid(row=2,column=0,pady=5,sticky=SW)
        def qingchu2():
            l27.grid_forget()
            b28.grid_forget()
        b28=Button(r1,text='清除',command=qingchu2)
        b28.grid(row=3,column=0,padx=30)
    def quxiao1():
        rcz.destroy()
    b25=Button(rcz,text='确认',command=queren1)
    b26=Button(rcz,text='取消',command=quxiao1)
    b25.grid(row=1,column=0,pady=5,padx=10)
    b26.grid(row=1,column=1,pady=5,padx=15)

def tihuan():
    rth=Tk()
    rth.title('替换')
    l41=Label(rth,text='被替换内容：')
    l42=Label(rth,text='替换内容：')
    l41.grid(row=0,column=2,pady=5,padx=50,sticky=E)
    l42.grid(row=1,column=2,pady=5,padx=50,sticky=E)
    e41=Entry(rth,width =15,show=None)
    e42=Entry(rth,width=15,show=None) 
    e41.grid(row=0,column=3,pady=5,padx=20,sticky=W)
    e42.grid(row=1,column=3,pady=5,padx=20,sticky=W)  
    def queren3():
        a=e41.get()
        b=e42.get()
        txt=t11.get(1.0,END)  
        replace_reg=re.compile(a)
        t11.delete(1.0,END)
        t11.insert(INSERT,replace_reg.sub(b, txt))
        rth.destroy()
    def quxiao3():
        rth.destroy()
    b41=Button(rth,text='确认',command=queren3)
    b42=Button(rth,text='取消',command=quxiao3)
    b41.grid(row=2,column=2,pady=5,padx=10)
    b42.grid(row=2,column=3,pady=5,padx=15)