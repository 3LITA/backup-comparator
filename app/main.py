from app import script

if __name__ == '__main__':
    decompressed = script.unzip('../data/src/directoryObjects_001.gz')
    with open('decompressed.json', 'wb') as file:
        file.write(decompressed)
