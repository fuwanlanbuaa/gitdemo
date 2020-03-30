def dakai():
    global flag2
    if flag2:
        mb.showinfo('文件','打开文件：article.txt')
        flag2=False
    txt11=open('article.txt','r')
    txt1=txt11.read()
    global s1
    global l0
    s1=Scrollbar(r1)
    s1.config(command=t11.yview)
    s1.grid(row=0,column=1,sticky=NS)
    t11.config(yscrollcommand=s1.set)  
    t11.insert(INSERT,txt1)
    l0=Label(r1)
    l0.grid(row=1,column=0,pady=5,sticky=SW)
    #---------状态------
    def zhuangtai(event):
        txt0=t11.get(1.0,END)
        s1=0
        for i in txt0:
           if i==' ':s1=s1+1
           if i=='—':s1=s1+1
        rl=t11.index(CURRENT)   
        ro,li=rl.split('.')
        l0['text']='总词数：'+str(s1+1)+'       INDEX：'+li
    r1.bind('<Button-1>',zhuangtai)
    r1.bind('<Key>',zhuangtai)

def baocun():
    mb.showinfo("提示","已保存")
    strings=t11.get(1.0,END)
    f=open('article.txt','w')
    f.write(strings)
    f.close()

def lingcunwei():
    rbc=Tk()
    rbc.title('提示：另存为')
    strings=t11.get(1.0,END)
    l13=Label(rbc,text='请输入保存的文件名：')
    l13.grid(row=0,column=0,pady=5,padx=10,sticky=E)
    e14=Entry(rbc,width=20,show=None)
    e14.grid(row=0,column=1,pady=5,padx=20,sticky=W)
    def queren():
        name=e14.get()+'.txt'
        f=open(name,'w')
        f.write(strings)
        f.close()
        rbc.destroy()
    def quxiao():
        rbc.destroy()
    b15=Button(rbc,text='确认',command=queren)
    b16=Button(rbc,text='取消',command=quxiao)
    b15.grid(row=1,column=0,pady=5,padx=10)
    b16.grid(row=1,column=1,pady=5,padx=15)

def guanbi():
    t11.grid_forget()
    s1.grid_forget()
    l0.grid_forget()
    
def tuichu():
    r1.destroy()