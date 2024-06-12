import qrcode
import qrcode.image.svg
import time


def make_qr(data, fill_color, is_svg):
    qr = qrcode.QRCode(
        version=6,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=36,
        border=4,
    )
    if is_svg:
        qr = qrcode.QRCode(
            version=6,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=36,
            border=4,
            image_factory=qrcode.image.svg.SvgFragmentImage,
        )

    qr.make(fit=True)
    qr.add_data(data)

    file_name = f'{int(time.time() * 1000)}.svg' if is_svg else f'{int(time.time() * 1000)}.png'
    try:
        if is_svg:
            img = qr.make_image(stroke=fill_color, fill=fill_color)
        else:
            img = qr.make_image(fill_color=fill_color, back_color=(220, 220, 220))
        img.save(f"QRs/{file_name}")

        print('\n-- QR Code is Generated --')
        print(f'Filename : {file_name}')

    except ValueError:
        print('\nError : Please Give correct color names!')

    except:
        print('Something went wrong!!')


data = input('What to put in QR? ')
fill_color = input('Any fill color? ')
is_svg = input('SVG? ')

if not fill_color:
    fill_color = 'black'
make_qr(data, fill_color, is_svg)
