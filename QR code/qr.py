import qrcode

def qr_code(url, filename="qrcode.png"):
    qr = qrcode.QRCode(
        version=1,  
        error_correction=qrcode.constants.ERROR_CORRECT_L,  
        box_size=10,  
        border=4,  
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="blue", back_color="green")

    img.save(filename)
    print(f"QR Code saved as {filename}")

url = input("Enter the URL to generate a QR code: ")
qr_code(url)
