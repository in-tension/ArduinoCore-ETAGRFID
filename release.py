import tarfile
import os

fileNames = os.listdir("ArduinoCore-ETAGRFID")
print(fileNames)


tar = tarfile.open("ArduinoCoreETAGRFID.tar.bz2", "w:bz2")
for name in fileNames:
    tar.add("ArduinoCore-ETAGRFID/" + name)
tar.close()


import hashlib
BLOCKSIZE = 65536
hasher = hashlib.sha256()
with open('ArduinoCoreETAGRFID.tar.bz2', 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
checksum = hasher.hexdigest()
print(checksum)

fileSize = os.path.getsize('ArduinoCoreETAGRFID.tar.bz2')
print(fileSize)



JSONstring = '{"packages":[{"name":"ArduinoCore-ETAGRFID","maintainer":"ArduinoBetatesting","websiteURL":"http://www.arduino.cc/","email":"packages@arduino.cc","help":{"online":"http://www.arduino.cc/en/Reference/HomePage"},"platforms":[{"archiveFileName":"package_ETAGRFID_index.tar.bz2","name":"ArduinoETAGRFIDcore","architecture":"samd","category":"Arduino",'
versionCode = '1.0.0'
JSONstring += '"version": "' + versionCode + '",'
JSONstring += '"url": "https://github.com/jaywilhelm/ArduinoCore-ETAGRFID/raw/master/ArduinoCoreETAGRFID.tar.bz2",'
JSONstring += '"checksum": "SHA-256:' + checksum + '",'
JSONstring += '"size": "' + str(fileSize) + '",'
JSONstring += '"boards":[{"name":"ArduinoZero"}],"toolsDependencies":[{"packager":"arduino","name":"arm-none-eabi-gcc","version":"4.8.3-2014q1"},{"packager":"arduino","name":"bossac","version":"1.7.0"},{"packager":"arduino","name":"openocd","version":"0.9.0-arduino6-static"},{"packager":"arduino","name":"CMSIS","version":"4.5.0"},{"packager":"arduino","name":"CMSIS-Atmel","version":"1.1.0"},{"packager":"arduino","name":"arduinoOTA","version":"1.2.0"}]}],"tools":[]}]}'
print(JSONstring)

f= open("package_ETAGRFID_index.json","w+")
f.write(JSONstring)
f.close()