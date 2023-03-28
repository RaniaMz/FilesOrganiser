import sys
import os
import shutil
import time


class FolderReader:

    def __init__(self, folder=0):
        self.folder = folder


def validate_directory(directory):
    if not os.path.exists(directory) or not os.path.isdir(directory):
        raise Exception('--- Please pass a valid folder name ---')
    else:
        print("--- Start processing on folder name : " + os.path.basename(directory) + " ---")


if __name__ == '__main__':
    start_time = time.time()

    directory = sys.argv[1]

    validate_directory(directory)

    list_files = os.listdir(directory)

    files = [file for file in list_files if os.path.isfile(directory + '/' + file)]

    folders_names = {}

    for file in files:
        name = os.path.basename(file).split('-')

        if name[0] not in folders_names:
            folders_names[name[0]] = True
            os.mkdir(directory + '/' + name[0])

        shutil.move(os.path.basename(directory) + '/' + file, directory + '/' + name[0] + '/')

    print("--- End program time in seconds : %s ---" % (time.time() - start_time))
