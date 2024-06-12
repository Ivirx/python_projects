import io
import qrcode


data = input('What to put in QR? ')

qr = qrcode.QRCode(
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_H
)
qr.add_data(data)
f = io.StringIO()
qr.print_ascii(out=f)
f.seek(0)

print(f.read())
