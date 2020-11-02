import qrcode
import os

currentPath= os.getcwd()

for i in range(1,100):
    name="https://neilscgh.github.io/QRCodes/{}.html".format(i)
    img = qrcode.make(name)
    img.save("{}\\{}.png".format(currentPath,i))
    print("{}\\{}.png created".format(currentPath,i))

print("Done")