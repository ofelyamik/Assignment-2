from concurrent.futures import ProcessPoolExecutor
from time import sleep
import os
import shutil


def copy(full_file_name, to):
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name, to)
        print("Copied")


def main(fr, to):
    src_files = os.listdir(fr)
    executor = ProcessPoolExecutor(len(src_files))
    for file_name in src_files:
        full_file_name = os.path.join(fr, file_name)
        future = executor.submit(copy, full_file_name, to)


if __name__ == '__main__':
    main("./folder1", "./folder2")
