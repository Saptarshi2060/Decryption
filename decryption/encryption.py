import numpy as np
from PIL import Image

def xor_encrypt_decrypt(img_array, key_array):
    # Perform XOR operation for encryption/decryption
    return np.bitwise_xor(img_array, key_array)

def process_image(image_path, key_path=None, encrypt=True):
    img = Image.open(image_path)
    img_array = np.array(img)
    
    if encrypt:
        key_array = generate_key(img_array.shape)
        encrypted_array = xor_encrypt_decrypt(img_array, key_array)
        encrypted_img = Image.fromarray(encrypted_array)
        encrypted_img.save('encrypted_image.png')
        np.save('key.npy', key_array)
        return key_array
    else:
        key_array = np.load(key_path)
        decrypted_array = xor_encrypt_decrypt(img_array, key_array)
        decrypted_img = Image.fromarray(decrypted_array)
        decrypted_img.save('decrypted_image.png')
        return None

def generate_key(shape):
    # Generate a random key of the same shape as the image array
    return np.random.randint(0, 256, size=shape, dtype=np.uint8)
