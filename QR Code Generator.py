import pyqrcode
from PIL import Image

def generate_qr_code(text, filename):
    qr = pyqrcode.create(text)
    qr.png(filename, scale=8)

if __name__ == "__main__":
    text = input("Enter the text to generate the QR code: ")
    filename = input("Specify the file name and extension (e.g., code.png): ")
    generate_qr_code(text, filename)
    print(f"{filename} QR code has been generated.")
