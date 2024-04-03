from PIL import Image

def encrypt_image(image_path, key):
    with Image.open(image_path, 'r') as img:
        pixels = img.load()
        width, height = img.size

        for py in range(height):
            for px in range(width):
                pixels[px, py] = (pixels[px, py][0] ^ key, pixels[px, py][1] ^ key, pixels[px, py][2] ^ key)

    img.save('encrypted_image.png')

def decrypt_image(image_path, key):
    with Image.open(image_path, 'r') as img:
        pixels = img.load()
        width, height = img.size

        for py in range(height):
            for px in range(width):
                pixels[px, py] = (pixels[px, py][0] ^ key, pixels[px, py][1] ^ key, pixels[px, py][2] ^ key)

    img.save('decrypted_image.png')

if __name__ == "__main__":
    image_path = input("Enter path of Image: ")
    key = int(input("Enter Key for encryption/decryption of Image: "))

    encrypt_image(image_path, key)
    print("Encryption done...")

    decrypt_image('encrypted_image.png', key)
    print("Decryption done...")
