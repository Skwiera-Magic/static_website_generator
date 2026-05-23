import os
import shutil


def clean_and_copy(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    copier(source, destination)


def copier(source, destination):
    files = os.listdir(source)
    for file in files:
        path = os.path.join(source, file)
        if os.path.isfile(path):
            print(f" * {path} -> {destination}")
            shutil.copy(path, destination)
        else:
            new_destination = os.path.join(destination, file)
            os.mkdir(new_destination)
            copier(path, new_destination)
