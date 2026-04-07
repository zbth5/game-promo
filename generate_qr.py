import qrcode
from PIL import Image

# 创建二维码
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data('https://zbth5.github.io/game-promo/')
qr.make(fit=True)

# 生成图像
img = qr.make_image(fill_color='black', back_color='white')
img.save('qrcode.png')
print('二维码已生成: qrcode.png')
