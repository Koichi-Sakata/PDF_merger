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
    global merger

    if os.path.exists(textbox1.get()):
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

    savePath = os.path.join(textbox1.get(), textbox2.get() + '.pdf')

    for k in range(len(filelist)):
        merger.append(filelist[k])
    if os.path.exists(savePath):
        textbox3.insert(tkinter.END, '\nA file with the same name (' + textbox2.get() + '.pdf)' + ' exists.\n')
        textbox3.insert(tkinter.END, 'Change to another name.')
        return
    merger.write(savePath)
    merger.close()
    merger = PyPDF2.PdfFileMerger()

    textbox3.insert(tkinter.END, '************************************************\n')
    textbox3.insert(tkinter.END, 'The merged file is saved as ' + textbox2.get() + '.pdf.')


def reset():
    global filelist
    textbox3.delete(1.0, tkinter.END)
    textbox3.insert('1.0', 'Drag and drop PDF files you want to merge.')
    filelist = []
    print(filelist)


def drop(event):
    global filelist
    if event.data:
        filename = event.data
        filename = filename.replace('\\', '/')
        filename = filename.replace('{', '')
        filename = filename.replace('}', '')
        filelist.append(filename)
        print(filelist)
        textbox3.delete(1.0, tkinter.END)
        textbox3.insert(tkinter.END, 'Merge the below PDF files.\n\n')
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
button.place(x=275, y=120)

# Reset button
button = tkinter.Button(root, text="Reset", command=reset, width=8, height=2, font=(u'Meiryo', 12), bg='#FF4500', fg='#ffffff')
button.place(x=400, y=120)

# Label1 Path
lbl = tkinter.Label(text='Folder path', font=(u'Meiryo', 12))
lbl.place(x=25, y=30)

# Textbox1 Path
textbox1 = tkinter.Entry(width=60, font=(u'Meiryo', 12))
textbox1.insert(tkinter.END, "Push Ref button to select a folder path of a new PDF file.")
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

folderPath = ''
filelist = []
merger = PyPDF2.PdfFileMerger()

root.mainloop()
