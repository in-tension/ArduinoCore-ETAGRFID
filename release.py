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



# JSONstring = '{"packages":[{"name":"ArduinoCore-ETAGRFID","maintainer":"ArduinoBetatesting","websiteURL":"http://www.arduino.cc/","email":"packages@arduino.cc","help":{"online":"http://www.arduino.cc/en/Reference/HomePage"},"platforms":[{"archiveFileName":"package_ETAGRFID_index.tar.bz2","name":"ArduinoETAGRFIDcore","architecture":"samd","category":"Arduino",'
JSONstring = '{\n'
JSONstring += '   "packages":[\n'
JSONstring += '      {\n'
JSONstring += '         "name":"ArduinoCore-ETAGRFID",\n'
JSONstring += '         "maintainer":"JayWilhelm",\n'
JSONstring += '         "websiteURL":"http://github.com/jaywilhelm",\n'
JSONstring += '         "email":"jwilhelm@ohio.edu",\n'
JSONstring += '         "help":{\n'
JSONstring += '            "online":"http://www.arduino.cc/en/Reference/HomePage"\n'
JSONstring += '         },\n'
JSONstring += '         "platforms":[\n'
JSONstring += '            {\n'
JSONstring += '               "archiveFileName":"package_ETAGRFID_index.tar.bz2",\n'
JSONstring += '               "name":"ArduinoETAGRFIDcore",\n'
JSONstring += '               "architecture":"samd",\n'
JSONstring += '               "category":"Arduino",\n'
JSONstring += '               "version":"1.0.0",\n'
JSONstring += '               "url":"https://github.com/jaywilhelm/ArduinoCore-ETAGRFID/raw/master/ArduinoCoreETAGRFID.tar.bz2",\n'

JSONstring += '               "checksum":"SHA-256:' + checksum + '",\n'
JSONstring += '               "size":"' + str(fileSize) + '",\n'

JSONstring += '               "boards":[\n'
JSONstring += '                  {\n'
JSONstring += '                     "name":"ArduinoZero"\n'
JSONstring += '                  }\n'
JSONstring += '               ],\n'
JSONstring += '               "toolsDependencies":[\n'
JSONstring += '                  {\n'
JSONstring += '                     "packager":"arduino",\n'
JSONstring += '                     "name":"arm-none-eabi-gcc",\n'
JSONstring += '                     "version":"4.8.3-2014q1"\n'
JSONstring += '                  },\n'
JSONstring += '                  {\n'
JSONstring += '                     "packager":"arduino",\n'
JSONstring += '                     "name":"bossac",\n'
JSONstring += '                     "version":"1.7.0"\n'
JSONstring += '                  },\n'
JSONstring += '                  {\n'
JSONstring += '                     "packager":"arduino",\n'
JSONstring += '                     "name":"openocd",\n'
JSONstring += '                     "version":"0.9.0-arduino6-static"\n'
JSONstring += '                  },\n'
JSONstring += '                  {\n'
JSONstring += '                     "packager":"arduino",\n'
JSONstring += '                     "name":"CMSIS",\n'
JSONstring += '                     "version":"4.5.0"\n'
JSONstring += '                  },\n'
JSONstring += '                  {\n'
JSONstring += '                     "packager":"arduino",\n'
JSONstring += '                     "name":"CMSIS-Atmel",\n'
JSONstring += '                     "version":"1.1.0"\n'
JSONstring += '                  },\n'
JSONstring += '                  {\n'
JSONstring += '                     "packager":"arduino",\n'
JSONstring += '                     "name":"arduinoOTA",\n'
JSONstring += '                     "version":"1.2.0"\n'
JSONstring += '                  }\n'
JSONstring += '               ]\n'
JSONstring += '            }\n'
JSONstring += '         ],\n'
JSONstring += '         "tools":[\n'
JSONstring += '\n'
JSONstring += '         ]\n'
JSONstring += '      }\n'
JSONstring += '   ]\n'
JSONstring += '}\n'

print(JSONstring)

f= open("package_ETAGRFID_index.json","w+")
f.write(JSONstring)
f.close()