import qrcode
qr= qrcode.QRCode(version=1, box_size=10, border=5)
data= input("Enter Link :")
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="pink  ")
img.save("firedaisigit.png")