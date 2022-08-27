import os
import shutil
def main():
    path1=input('请输入需要整理的路径:')
    path2=path1.replace('\\','/')
    print(path2)
    files=os.listdir(path2)
    for item in files:
        folder_name=path2+'/'+item.split('.')[-1]
        source=path2+'/'+item
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            shutil.move(source,folder_name)
        else:
            shutil.move(source,folder_name)
    #C:\Users\DELL\Documents\KYC\__MACOSX\寻梦远航实践队
if __name__=='__main__':
    main()