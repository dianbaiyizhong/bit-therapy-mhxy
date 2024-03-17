import os
import shutil

# folder = 'ts'
# folder = 'vampire'
folder = 'ghost_general'


def compress_folder_to_zip(folder_path, zip_path):
    shutil.make_archive(zip_path, "zip", folder_path)


compress_folder_to_zip(os.getcwd() + '/' + folder, folder)
