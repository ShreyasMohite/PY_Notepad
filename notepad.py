from tkinter import *
from tkinter import colorchooser
from tkinter import commondialog



class notepad:
    def __init__(self,root):
        self.root=root
        self.root.title("notepad")
        self.root.minsize(800,400)
        

        
        def do_pop(event):
            m.tk_popup(event.x_root,event.y_root)
            m.grab_release()

        
        def function():
            pass
            
        def Background_color():
            bgcolor=colorchooser.askcolor(title="Background Color")
            TXT.config(bg=bgcolor[1])
            
        def Foreground_color():
            fgcolor=colorchooser.askcolor(title="Foreground Color")
            TXT.config(fg=fgcolor[1])



        #right click menu
        m=Menu(self.root,tearoff=0)
        m.add_command(label="Select All",command=function)
        m.add_command(label="Copy",command=function)
        m.add_command(label="Cut",command=function)
        m.add_command(label="Paste",command=function)
        m.add_command(label="Refresh",command=function)

        self.root.bind("<Button-3>",do_pop)
        #=================================================================================
        #menubar  
        menubar = Menu(self.root)

        #filemenu bar 
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New   Clt+N",)
        filemenu.add_command(label="Open   Clt+O",)
        filemenu.add_command(label="Save    Clt+S",)
        filemenu.add_command(label="Save as...   Clt+Shift+S",)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.destroy)
        menubar.add_cascade(label="File", menu=filemenu)
        #======================================================================================
        #editmenu bar
        editmenu = Menu(menubar, tearoff=0)
        #submenu 
        sub_color=Menu(editmenu)
        sub_color.add_command(label="Background Color",command=Background_color)
        sub_color.add_command(label="Foreground Color",command=Foreground_color)
        #========================================
        editmenu.add_command(label="Undo  Clt+Z",)
        editmenu.add_separator()
        editmenu.add_command(label="Cut  Clt+X", )
        editmenu.add_command(label="Copy  Clt+C",)
        editmenu.add_command(label="Paste   Clt+V", )
        editmenu.add_command(label="Delete", )
        editmenu.add_command(label="Select All  Clt+A",)
        editmenu.add_cascade(label="Color",menu=sub_color)
        menubar.add_cascade(label="Edit", menu=editmenu)
        #=====================================================================================
        #menubar help

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index",)
        helpmenu.add_command(label="About...",)
        menubar.add_cascade(label="Help", menu=helpmenu)
        self.root.config(menu=menubar)



        #=======================scrollbar ===============================and text------------------------------
        scroll=Scrollbar(self.root)
        scroll.pack(side=RIGHT,fill=Y)
        
        TXT=Text(self.root, width=168,height=43,font=('arial',11),bg="white",yscrollcommand=scroll.set)
        TXT.place(x=0,y=0)
        scroll.config(command=TXT.yview)




if __name__ == "__main__":
    root=Tk()
    app=notepad(root)
    
    root.mainloop()
