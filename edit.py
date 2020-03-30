def chexiao():
    t11.edit_undo()
def huifu():
    t11.edit_redo()

def yanse():
    rys=Toplevel()
    t11.tag_add('tag1',SEL_FIRST,SEL_LAST)
    rys.title('编辑——颜色')
    l31=Label(rys,text='请选择颜色')
    l31.grid(row=0,column=0,padx=10)
    v=IntVar()
    butt=[('黄色',0),('蓝色',1),('红色',2),('黑色',3),('白色',4),('紫色',5),('绿色',6)]
    def color():
        col=['yellow','blue','red','black','white','purple','green']
        re=col[v.get()]
        t11.tag_config('tag1',background=re)
    for c,num in butt:
        Radiobutton(rys,text=c,value=num,command=color,variable=v).grid(row=1,column=num)   
    def quxiao2():
        rys.destroy()
    b37=Button(rys,text='确认',command=quxiao2)
    b37.grid(row=2,column=2)    
    b38=Button(rys,text='取消',command=quxiao2)
    b38.grid(row=2,column=3)
    
def fangda():
    t11.tag_add('tag2',SEL_FIRST,SEL_LAST)
    t11.tag_config('tag2',font=('Times New Roman',18))

def xiahuaxian():
    global flag1
    t11.tag_add('tag2',SEL_FIRST,SEL_LAST)
    if flag1:
        t11.tag_config('tag2',underline=True)
        flag1=False
    else:
        t11.tag_config('tag2',underline=False)
        flag1=True