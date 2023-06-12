import PySimpleGUI as gui
from zip_creator import make_archive

gui.theme("DarkAmber")
# Tạo các elements nhập file cần zip
label1 =gui.Text("Select files to compress: ")
input1 =gui.Input()
choose_button1 = gui.FilesBrowse("Choose",key= "files")

# Tạo dest lưu file cần zip
label2 =gui.Text("Select destination folder: ")
input2 =gui.Input()
choose_button2 = gui.FolderBrowse("Choose",key="folder")

# Tạo nút compress và thông báo khi zip thành công
compress_button = gui.Button("Compress")
output_label = gui.Text(key="output", text_color= "silver")

window =gui.Window("File Compressor", 
                   layout= [[label1,input1, choose_button1],
                            [label2,input2, choose_button2],
                            [compress_button, output_label]])

while True:
    event, values = window.read()
    print(event,values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths,folder)
    window["output"].update(value= "Compression completed !")

window.close()