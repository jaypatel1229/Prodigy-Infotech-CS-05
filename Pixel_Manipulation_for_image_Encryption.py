
# Develop a simple image encryption tool using pixel manipulation.
# You can perform operations like swapping pixel values or applying a basic mathematical operation to each pixel allow users to encrypt and decrypt images.

from PIL import Image

def encrypt_image(input_path, output_path,key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r,g,b = pixels[x,y]

            encrypted_pixel = (b,g,r)
            pixels[x,y] = encrypted_pixel

    img.save(output_path)
    print("Image Encrypt Done")

def decrypt_image(input_path,output_path,key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r,g,b = pixels[x,y]

            decrypt_pixel = (g,b,r)
            pixels[x,y] = decrypt_pixel

    img.save(output_path)
    print("Image Decrypt Done")

input_image = r"C:\Users\Jerry\Data Anonymization\Prodigy_Infotech\.venv\Phishing.jpg"
encrypted_image = r"C:\Users\Jerry\Data Anonymization\Prodigy_Infotech\.venv\one.jpg"
decrypted_image = r"C:\Users\Jerry\Data Anonymization\Prodigy_Infotech\.venv\two.jpg"

encrypt_image(input_image,encrypted_image,key=None)
decrypt_image(encrypted_image,decrypted_image,key=None)


