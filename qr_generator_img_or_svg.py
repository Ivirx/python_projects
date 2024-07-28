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

    file_name = f'{int(time.time() * 1000)
                   }.svg' if is_svg else f'{int(time.time() * 1000)}.png'
    try:
        if is_svg:
            img = qr.make_image(stroke=fill_color, fill=fill_color)
        else:
            img = qr.make_image(fill_color=fill_color,
                                back_color=(220, 220, 220))
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

# QR Image Generator
"""

import qrcode
import time
import re


def make_qr(data, fill_color, back_color):
	qr = qrcode.QRCode(
	 version=8,
	 error_correction=qrcode.constants.ERROR_CORRECT_H,
	 box_size=40,
	 border=4,
	)

	qr.make(fit=True)
	qr.add_data(data)

	filename = f'{int(time.time() * 1000)}.png'

	img = qr.make_image(fill_color=fill_color, back_color=back_color)
	img.save(f"QRs/{filename}")

	print('\n-- QR Code has been Generated --')
	print(f'Saved As : {filename}')


data = input('What to put in QR? ')

pattern = '(^\d{1,3},\d{1,3},\d{1,3}$)|^$'
while True:
	print('\nColors should be comma separated values, eg: 0,0,0')
	fill_color = input('Any fill color? default(0,0,0): ')
	back_color = input('Any Back color? default(256,256,256): ')

	fill_matches = re.search(pattern, fill_color)
	back_matches = re.search(pattern, back_color)

	if (fill_matches and back_matches):
		break

	print('--- Invalid Input! Try Again! ---')

fill_color = tuple([int(val) for val in fill_color.split(',')]) if fill_color else (0, 0, 0)
back_color = tuple([int(val) for val in back_color.split(',')]) if back_color else (256, 256, 256)

make_qr(data, fill_color, back_color)

"""
