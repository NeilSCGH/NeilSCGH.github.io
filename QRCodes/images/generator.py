import qrcode
import os

currentPath= os.getcwd()

for i in range(0,5):
    name="https://neilscgh.github.io/QRCodes/{}.html".format(i)
    img = qrcode.make(name)
    img.save("{}\\{}.png".format(currentPath,i))

print("Done")