import zipfile
import pathlib

#Tạo function zip file
def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir,"compressed.zip")
    with zipfile.ZipFile(dest_path,"w" ) as archive:
        for filepath in filepaths:
            filepath =pathlib.Path(filepath)
            archive.write(filepath, arcname = filepath.name)

if __name__== "__main__":
    make_archive(filepaths=["t1.txt","t2.txt"], dest_dir="dest")