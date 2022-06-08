import cv2
from pyzbar.pyzbar import decode
from extra import bcolors as bc, pvar as pv
import os

import tkinter as tk
from tkinter import filedialog

#from urllib.parse import unquote
from base45 import b45decode
import zlib
import cbor2
from pprint import pprint

root = tk.Tk()
root.wm_withdraw()

def input_op():
    inp = input()
    if inp == 'file':
        file()
    if inp == 'wcam':
        wcam()

def file():
    file = filedialog.askopenfilename(title='Select Image', filetypes=pv.filetypes)
    filename = os.path.abspath(file)
    filename = filename.replace('\\', '/')
    if filename != None:
        decode_qr(filename)
    else:
        print(bc.FAIL+"ERROR"+bc.ENDC + "Try again?")
        tryag = input()
        if tryag == 'yes':
            restart('file')


def wcam():
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()
    while True:
        _, img = cap.read()
        data, one, _ = detector.detectAndDecode(img)
        if data:
            dat = data
            dat = dat.replace("b'HC1:", "")
            dat = dat.replace("'", "")
            zdata = b45decode(dat)
            databytes = bytes(zdata)
            deco = zlib.decompress(databytes)
            decoded = cbor2.loads(deco)
            pprint(cbor2.loads(decoded.value[2]))
            break
        cv2.imshow('QR Code Scanner', img)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def decode_qr(filename):
    image = cv2.imread(filename)
    for barcode in decode(image):
        print("["+bc.OKGREEN+"OK"+bc.ENDC + "] QR decoded successfully")
        data = str(barcode.data)
        data = data.replace("b'HC1:", "")
        data = data.replace("'", "")
        zdata = b45decode(data)
        databytes = bytes(zdata)
        deco = zlib.decompress(databytes)
        decoded = cbor2.loads(deco)
        pprint(cbor2.loads(decoded.value[2]))

def restart(func) :
    if func == 'file' :
        file()
    if func == 'wcam' :
        wcam()

print("This app is by default in english, but you can also set other languages. Set one of the following:")
print("English [en], Spanish [es]: ")
lang = input()
if lang == 'es':
    print("¡Hola! Esto es un Escáner del Certificado COVID Digital Europeo. ¡Puedes abrir una imagen o incluso usar la cámara!")
    print("Si prefieres la images, escribe file, pero si prefieres la cámara, escribe wcam")
if lang == 'en':
    print("Hi! This is a European COVID Digital Certificate scanner. You can attach a file or use your webcam!")
    print("If you want to decode an existing image, type file, and if you want to scan through your webcam, type wcam")
input_op()