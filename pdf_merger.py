# Copyright (c) 2022 Koichi Sakata

import tkinter
import tkinterdnd2
import tkinter.filedialog
import PyPDF2
import os


def readfolder():
    iDir = os.path.abspath(os.path.dirname(__file__))
    iDirPath = tkinter.filedialog.askdirectory(initialdir=iDir)
    textbox1.delete(0, tkinter.END)
    textbox1.insert(tkinter.END, iDirPath)


def merge():
    savePath = textbox1.get()

    if os.path.exists(savePath):
        textbox3.delete(1.0, tkinter.END)
        textbox3.insert('1.0', 'Merge the below PDF files.\n\n')
        for k in range(len(filelist)):
            textbox3.insert(tkinter.END, filelist[k] + '\n')
        pass
    else:
        textbox3.delete(1.0, tkinter.END)
        textbox3.insert('1.0', 'Path is not found.')
        return

    if len(filelist) < 2:
        textbox3.insert(tkinter.END, 'Drag and drop at least two PDF files you want to merge.\n\n')
        return

    savedName = textbox2.get()

    for k in range(len(filelist)):
        merger.append(filelist[k])
    merger.write(os.path.join(savePath, savedName + '.pdf'))
    merger.close()

    textbox3.insert(tkinter.END, '\n\n**************************\n\n')
    textbox3.insert(tkinter.END, 'The merged file is saved as ' + savedName + '.pdf.')


def drop(event):
    if event.data:
        filename = event.data
        filename = filename.replace('\\', '/')
        filename = filename.replace('{', '')
        filename = filename.replace('}', '')
        filelist.append(filename)
        print(filelist)
        textbox3.delete(1.0, tkinter.END)
        textbox3.insert('1.0', 'Merge the below PDF files.\n\n')
        for k in range(len(filelist)):
            textbox3.insert(tkinter.END, filelist[k] + '\n')
    return event.action


root = tkinterdnd2.TkinterDnD.Tk()
root.title('PDF Merger')
root.geometry("800x480")
ver = '1.0.0'

# Ref button
button = tkinter.Button(root, text="Ref", command=readfolder, width=8, height=2, font=(u'Meiryo', 12), bg='#add8e6', fg='#000000')
button.place(x=150, y=120)

# Merge button
button = tkinter.Button(root, text="Merge", command=merge, width=8, height=2, font=(u'Meiryo', 12), bg='#4169e1', fg='#ffffff')
button.place(x=260, y=120)

# Label1 Path
lbl = tkinter.Label(text='Path name', font=(u'Meiryo', 12))
lbl.place(x=25, y=30)

# Textbox1 Path
textbox1 = tkinter.Entry(width=60, font=(u'Meiryo', 12))
textbox1.insert(tkinter.END, "Enter a path name or select a path by Ref button.")
textbox1.place(x=150, y=30)

# Label2 merged file name
lbl = tkinter.Label(text='Merged file name', font=(u'Meiryo', 12))
lbl.place(x=5, y=75)

# Textbox2 merged file name
textbox2 = tkinter.Entry(width=60, font=(u'Meiryo', 12))
textbox2.insert(tkinter.END,"merged_file")
textbox2.place(x=150, y=75)

# Textbox3
scroll_Y = tkinter.Scrollbar(orient='vertical')
textbox3 = tkinter.Text(width=60, height=10, font=(u'Meiryo', 12),  yscrollcommand=scroll_Y.set)
textbox3.place(x=150, y=200)
textbox3.insert('1.0', 'Drag and drop PDF files you want to merge.')

root.drop_target_register(tkinterdnd2.DND_FILES)
root.dnd_bind('<<Drop>>', drop)

scroll_Y['command'] = textbox3.yview
scroll_Y.place(x=755, y=200, height=250)

filelist = []

merger = PyPDF2.PdfFileMerger()
user = os.getlogin()
username = str(user)

root.mainloop()
