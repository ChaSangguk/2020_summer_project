from os import mkdir,path,remove
#메인화면
def MakeFolder(Path):
    if path.exists(Path):
        pass
    else :
        mkdir('./'+ Path)
def DeleteFolder(Path):
    if path.exists(Path):
        remove("./"+Path)
    else:
        pass