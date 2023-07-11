import zipfile

def extract(zip_file, dest):
    with zipfile.ZipFile(zip_file, "r") as zip:
        zip.extractall(dest)


# testing
if __name__ == "__main__":
    extract("compressed.zip", "output")