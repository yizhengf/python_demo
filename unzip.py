


#scan --- unzip --- delete


import os
import shutil

def scan_file():

    files = os.listdir()
    for f in files:
        if f.endswith('.zip'):
            return f


def unzip_it(f):
    folder_name = f.split('.')[0]
    target_path = './'+folder_name
    os.mkdir(target_path)
    shutil.unpack_archive(f,target_path)


def delete(f):
    os.remove(f)



while True:
    zip_files =scan_file()
    if zip_files:
        unzip_it(zip_files)
        delete(zip_files)