import tarfile
import os

fileNames = os.listdir(".")
print(fileNames)


tar = tarfile.open("ArduinoCoreETAGRFID.tar.bz2", "w:bz2")
for name in fileNames:
    if not name == "ArduinoCoreETAGRFID.tar.bz2":
        tar.add(name)
tar.close()