import qrcode

def generate_qr_code(text, file_name):
    qr = qrcode.QRCode(  # Renamed the local variable to 'qr'
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )           
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="green")
    img.save(file_name)


text = "https://b001.io"

file_name = "MM_QRcode.png"

generate_qr_code(text, file_name)
print(terminal("QR code generated successfully!"))