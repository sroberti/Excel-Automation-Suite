

import excelReader as reader
import codegen
import query

import tkinter as tk
import tkinter.filedialog as fdialog


class GUI:
    def __init__(self, title):
        self.master=tk.Tk() #root
        self.master.title(title)
        self.button={}
        self.fileName=None
        self.pipeline=codegen.PipelineGenerator(("query","plotting",))

        self.generateGUI()
        # run the gui
        self.master.mainloop()

    def generateGUI(self):
        # Main page
        self.label = tk.Label(self.master,text="Excel Big Data")
        self.label.pack()
        self.button.update({"Query" : tk.Button(
            self.master,text="Query",command=self.do_query
            )})
        self.button['Query'].pack()
        

        # Menu bar
        self.menubar = tk.Menu(self.master)
        self.filemenu = tk.Menu(self.master, tearoff=0)
        self.filemenu.add_command(label="Open", command=self.loadFile)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.master.config(menu=self.menubar)
        
    def loadFile(self):
        filename = fdialog.askopenfilename(parent=self.master)
        self.fileName=filename

    def quit(self):
        self.master.quit()
        quit()

    def do_query(self):
        if self.fileName:
            
            #colName=input()
            with open("output.py", "a+") as file:
                file.write('''import query
import excelReader as reader
df=reader.excel(self.fileName)
q=query.Query(df)
return q.rows({}, {}, {})'''.format(colName,op,value)
        

gui = GUI("Excel Big Data GUI")
