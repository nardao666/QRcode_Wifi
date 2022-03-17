import qrcode

SSID = "Nome da Rede"
Pass = "Senha da Rede"
wifi_data = "WIFI:T:WPA;S:"+SSID+";P:"+Pass+";;"
qr = qrcode.QRCode()
qr.add_data(wifi_data)
qr.make(fit=True)
img = qr.make_image(fill_color="Black", background_color="gray")
img.save("qrcode.png")