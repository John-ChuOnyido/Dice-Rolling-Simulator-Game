import pyqrcode

url = pyqrcode.create("https://github.com/John-ChuOnyido")
url.png("myqr.png", scale = 4)