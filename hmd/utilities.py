from os import path, listdir, unlink, remove
import shutil
from zipfile import ZipFile
import pathlib


def clean_folder(folder: str) -> None:
    for filename in listdir(folder):
        file_path = path.join(folder, filename)
        try:
            if path.isfile(file_path) or path.islink(file_path):
                unlink(file_path)
            elif path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def zip_test_case(folder: str, name: str) -> None:
    directory = pathlib.Path(folder)
    with ZipFile(path.join(folder, f"{name}.zip"), mode="w") as archive:
        for file_path in directory.iterdir():
            if file_path.suffix in ['.in', '.out']:
                archive.write(file_path, arcname=file_path.name)
                remove(file_path)
