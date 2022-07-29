#importpyqrcode
import pyqrcode
import png 
from pyqrcode import QRCode
#string that stores the website
s = "www.google.org"
#generating the qrcode
url = pyqrcode.create(s)
#create svg file
url.svg("my qr.svg", scale = 8)
#create png file
url.png("my qr.png", scale = 6)
