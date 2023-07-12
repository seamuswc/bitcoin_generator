import qrcode

class QR:

    def qr(address):
        # Create a QR code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        # Add the Bitcoin address to the QR code
        qr.add_data(address)
        qr.make(fit=True)

        # Generate the QR code as ASCII output
        qr.print_ascii()

