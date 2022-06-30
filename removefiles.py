import os ,shutil,time
def main():
    deletedfolderscount=0
    deletedfilescount=0
    path="new"
    days=0
    seconds=time.time()-(days*24*60*60)
    if os.path.exists(path):
        for root_folder,folders,files in os.walk(path):
            if seconds>=get_file_or_folder_age(root_folder):
                remove_folder(root_folder)
                deletedfolderscount+=1
                break
            else:
                for folder in folders:
                    folderpath=os.path.join(root_folder,folder)
                    if seconds >=get_file_or_folder_age(folderpath):
                        remove_folder(folderpath)
                        deletedfolderscount+=1
                for file in files:
                    filepath=os.path.join(root_folder,file)
                    if seconds>=get_file_or_folder_age (filepath):
                        remove_file(filepath)
                        deletedfilescount+=1
        else:
            if seconds>=get_file_or_folder_age(path):
                remove_file(path)
                deletedfilescount+=1
    else:
        print(f'"{path}"is not found')
        deletedfilescount+=1
    print(f"total folder deleted: {deletedfolderscount}")
    print(f"total files deleted: {deletedfilescount}")

def remove_folder(path):
    if not shutil.rmtree(path):
        print("{path} is removed successfully")
    else:
        print(f"unable to delete the "+path)
def remove_file(path):
    
    if not os.remove(path):
        print("{path} is removed successfully")
    else:       
        print(f"unable to delete the "+path)

def get_file_or_folder_age(path):
    ctime=os.stat(path).st_ctime
    return ctime

if __name__=="__main__":
    main()