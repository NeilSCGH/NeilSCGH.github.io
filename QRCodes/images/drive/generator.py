import qrcode
import os

currentPath= os.getcwd()

for i in range(1,10):
    name="https://pzfczh27edy8hocjobyt5a-on.drv.tw/webserver/qr codes/{}.html".format(i)
    img = qrcode.make(name)
    img.save("{}\\{}.png".format(currentPath,i))
    print("{}\\{}.png created".format(currentPath,i))

print("Done")