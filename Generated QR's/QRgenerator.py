# Importing library
import qrcode

USN = {"4NI20EC093", "4NI20EC072", "4NI20EC099",
     "4NI20EC109", "4NI20EC116", "4NI20EC071", "4NI20EC068", "4NI20EC107", "4NI20EC115", "4NI20EC081"}

i = 1

for s in USN:
    # Data to be encoded
    data = s

    # Encoding data using make() function
    img = qrcode.make(data)

    # Saving as an image file
    img.save("MyQRCode{}.png".format(i))
    i += 1