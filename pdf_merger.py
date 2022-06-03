import tkinter
import tkinterdnd2
import tkinter.filedialog
import PyPDF2
import os


def readfolder():
    iDir = os.path.abspath(os.path.dirname(__file__))
    iDirPath = tkinter.filedialog.askdirectory(initialdir=iDir)
    txt1.delete(0, tkinter.END)
    txt1.insert(tkinter.END, iDirPath)

# Open
def readfiles():
    txt3.delete(1.0, tkinter.END)
    filePath = txt1.get()

    if os.path.exists(filePath):
        pass
    else:
        txt3.insert('1.0', 'Path is not found.')

    drawings = []
    allFiles = os.listdir(filePath)

    for f in os.listdir(filePath):
        if os.path.join(filePath, f)[-4:] == '.pdf':
            drawings.append(f)

    count = int(len(drawings))
    txt3.insert('1.0', 'Merge the below PDF files.\n\n')
    for i in range(count):
        txt3.insert(1.0 * i + 3.0, drawings[i] + '\n')

# Merge
def merge():
    filePath = txt1.get()

    if os.path.exists(filePath):
        txt3.delete(1.0, tkinter.END)
        txt3.insert('1.0', 'Merge the below PDF files.\n\n')
        for k in range(len(filelist)):
            txt3.insert(tkinter.END, filelist[k] + '\n')
        pass
    else:
        txt3.delete(1.0, tkinter.END)
        txt3.insert('1.0', 'Path is not found.')
        return

    if len(filelist) < 2:
        txt3.insert(tkinter.END, 'Drag and drop at least two PDF files you want to merge.\n\n')
        return


    #filePath = str(txt1.get())
    savePath = filePath #'C:\\Users\\' + username + '\\Desktop'
    savedName = txt2.get()

    # for f in os.listdir(filePath):
    #     if os.path.join(filePath, f)[-4:] == '.pdf':
    #         merger.append(os.path.join(filePath, f))
    #         print(os.path.join(filePath, f))
    for k in range(len(filelist)):
        merger.append(filelist[k])
    merger.write(os.path.join(savePath, savedName + '.pdf'))
    merger.close()

    txt3.insert(tkinter.END, '\n\n**************************\n\n')
    txt3.insert(tkinter.END, 'The merged file is saved as ' + savedName + '.pdf.')


def drop(event):
    if event.data:
        filename = event.data
        filename = filename.replace('\\', '/')
        filename = filename.replace('{', '')
        filename = filename.replace('}', '')
        filelist.append(filename)
        print(filelist)
        txt3.delete(1.0, tkinter.END)
        txt3.insert('1.0', 'Merge the below PDF files.\n\n')
        for k in range(len(filelist)):
            txt3.insert(tkinter.END, filelist[k] + '\n')
    return event.action


root = tkinterdnd2.TkinterDnD.Tk()
root.title('PDF Merger')
root.geometry("800x480")
ver = '1.0.0'

# Ref button
button = tkinter.Button(root, text="Ref", command=readfolder, width=8, height=2, font=(u'Meiryo', 12), bg='#add8e6', fg='#000000')
button.place(x=150, y=120)

# Open button
# button = tkinter.Button(root, text="Open", command=readfiles, width=8, height=2, font=(u'Meiryo', 12), bg='#add8e6', fg='#000000')
# button.place(x=220, y=120)

# Merge button
button = tkinter.Button(root, text="Merge", command=merge, width=8, height=2, font=(u'Meiryo', 12), bg='#4169e1', fg='#ffffff')
button.place(x=260, y=120)

# Label1 Path
lbl = tkinter.Label(text='Path name', font=(u'Meiryo', 12))
lbl.place(x=25, y=30)

# Textbox1 Path
txt1 = tkinter.Entry(width=60, font=(u'Meiryo', 12))
txt1.insert(tkinter.END, "Enter a path name or select a path by Ref button.")
txt1.place(x=150, y=30)

# Label2 merged file name
lbl = tkinter.Label(text='Merged file name', font=(u'Meiryo', 12))
lbl.place(x=5, y=75)

# Textbox2 merged file name
txt2 = tkinter.Entry(width=60, font=(u'Meiryo', 12))
txt2.insert(tkinter.END,"merged_file")
txt2.place(x=150, y=75)

# Textbox3
scroll_Y = tkinter.Scrollbar(orient='vertical')
txt3 = tkinter.Text(width=60, height=10, font=(u'Meiryo', 12),  yscrollcommand=scroll_Y.set)
txt3.place(x=150, y=200)
txt3.insert('1.0', 'Drag and drop PDF files you want to merge.')

root.drop_target_register(tkinterdnd2.DND_FILES)
root.dnd_bind('<<Drop>>', drop)

scroll_Y['command'] = txt3.yview
scroll_Y.place(x=755, y=200, height=250)

filelist = []

merger = PyPDF2.PdfFileMerger()
user = os.getlogin()
username = str(user)

root.mainloop()
