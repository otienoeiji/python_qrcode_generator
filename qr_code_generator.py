import qrcode

def qr_code_generator():
    qrcode_in_text = input("Enter text to generate QRcode : ")
    
    generated_qrcode = qrcode.make(qrcode_in_text)
    
    generated_qrcode.save("QRcode_image.png")
    
    
if __name__ == '__main__':
    qr_code_generator()