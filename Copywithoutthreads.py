import os
import shutil


def copy(fr, to):
    src_files = os.listdir(fr)
    for file_name in src_files:
        full_file_name = os.path.join(fr, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, to)
            print("Copied")


copy("./folder1", "./folder2")
