import qrcode

def generate_qr_code(data, output_filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_filename)

def main():
    data_input = input("Enter the text or data to encode in the QR code: ")
    output_file = input("Enter the name of the output QR code image file (with extension): ")

    try:
        generate_qr_code(data_input, output_file)
        print(f"QR code generated and saved as {output_file}")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()
