PDF Merger
===

# 1. Introduction

This is a python program to create PDF merger software.
The program requires [tkinterdnd2](https://pypi.org/project/tkinterdnd2/) and [PyPDF2](https://pypi.org/project/PyPDF2/).


# 2. How to make an exe-file

You can make exe file which is not necesasary python environment by the following commands on the command prompt or on the shell with [pyinstaller](https://pypi.org/project/pyinstaller/).
```shell
pyinstaller pdf_merger.py --onefile --noconsole --collect-all tkinterdnd2
```

# 3. How to use the software

<img src="figure\PDF_Merger.png" alt="spyder_disp" style="zoom: 66%;" />

1. Push "Ref" button to select a folder path of a new PDF file.
1. Drag and drop at least two PDF files you want to merge.
1. Push "Merge" button.
1. A new merged file will be created in the folder path you selected.
1. If "Reset" button is pushed, the dropped PDF files to merge will be cleared.
