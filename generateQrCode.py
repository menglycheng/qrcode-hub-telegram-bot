import wifi_qrcode_generator as qr


def createWifiQrCode(wifi_name, password):
    wifi_qr = qr.wifi_qrcode(wifi_name, False, 'WPA', password)
    tmp_filename = "tmp_qrcode.png"
    wifi_qr.save(tmp_filename)

    return tmp_filename