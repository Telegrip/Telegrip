import os
import sys
import zipfile

import pyzipper
from io import BytesIO

from zipfile import ZipFile

def zip_folderPyzipper(folder_path,output_path): # add the cache4.db
    """Zip the contents of an entire folder (with that folder included
    in the archive). Empty subfolders will be included in the archive
    as well.
    """
    parent_folder = os.path.dirname(folder_path)
    # Retrieve the paths of the folder contents.
    contents = os.walk(folder_path)
    try:
        print("here1")
        zip_file = pyzipper.AESZipFile('SARA2.zip','w',compression=pyzipper.ZIP_DEFLATED,encryption=pyzipper.WZ_AES)
        zip_file.pwd=b'PASSWORD'
        for root, folders, files in contents:
            # Include all subfolders, including empty ones.
            for folder_name in folders:
                absolute_path = os.path.join(root, folder_name)
                relative_path = absolute_path.replace(parent_folder + '\\',
                                                      '')
                print ("Adding '%s' to archive." % absolute_path)
                zip_file.write(absolute_path, relative_path)
            for file_name in files:
                absolute_path = os.path.join(root, file_name)
                relative_path = absolute_path.replace(parent_folder + '\\',
                                                      '')
                print ("Adding '%s' to archive." % absolute_path)
                zip_file.write(absolute_path, relative_path)

        print ("'%s' created successfully." % output_path)

    except IOError as message:
        print (message)
        sys.exit(1)
    except OSError as message:
        print(message)
        sys.exit(1)
    except zipfile.BadZipfile as message:
        print (message)
        sys.exit(1)
    finally:
        zip_file.close()

folder_path = os.getcwd() +"/dump" #dump
output_path = os.getcwd()
folder2 = os.getcwd() +"dump/cache4.db"
zip_folderPyzipper(folder_path,output_path)



str_zipFile = 'C:/Users/Norah/Desktop/fri_9.37/Fri-7-9.37/telegrip/SARA2.zip'
str_pwd= 'PASSWORD'

with ZipFile(str_zipFile) as zipObj:
  zipObj.extractall(pwd = bytes(str_pwd,'utf-8'))