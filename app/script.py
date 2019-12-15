import gzip


def unzip(path: str):
    with open(path, 'rb') as file:
        data = file.read()
        return gzip.decompress(data)
