# Advanced Encryption Standard
# Esse código ilustra o processo de criptografia usando algoritmo AES.
# AES é um algoritmo de criptografia simétrica amplamente utilizado.
# Ele opera em blocos de 128 bits e suporta chaves de 128, 192 ou 256 bits.

import os
from Crypto.Cipher import AES


# PKCS7 Padding
# O padding é utilizado para garantir que os dados tenham um tamanho
# que seja um múltiplo do tamanho do bloco de cifra.
def pad(data):
    # Calcula a quantidade de bytes necessários
    # para fazer o dado ser um múltiplo de 16.
    padding_length = 16 - len(data) % 16
    # Cria um array de bytes com o valor do comprimento do padding.
    padding = bytes([padding_length] * padding_length)
    return data + padding


def unpad(data):
    # Verifica quantos bytes de padding foram adicionados.
    padding_length = data[-1]
    # Verifica se o padding é válido.
    if padding_length < 1 or padding_length > 16:
        raise ValueError("Padding Inválido")
    return data[:-padding_length]


def encrypt_file(input_file, output_file):
    key = os.urandom(32)
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    try:
        with open(input_file, 'rb') as f:
            plaintext = f.read()
        padded_plaintext = pad(plaintext)
        ciphertext = cipher.encrypt(padded_plaintext)
        with open(output_file, 'wb') as f:
            f.write(ciphertext)
        encoded_key = key.hex()
        encoded_iv = iv.hex()
        return encoded_key, encoded_iv
    except Exception as e:
        print(f"Um erro ocorreu durante a encriptação: {e}")
        return None, None


def decrypt_file(key, iv, input_file, output_file):
    try:
        decoded_key = bytes.fromhex(key)
        iv_bytes = bytes.fromhex(iv)
        if len(decoded_key) != 32:
            raise ValueError("Incorrect AES key length")
        cipher = AES.new(decoded_key, AES.MODE_CBC, iv_bytes)
        with open(input_file, 'rb') as f:
            encrypted_data = f.read()
        decrypted_data = unpad(cipher.decrypt(encrypted_data))
        with open(output_file, 'wb') as f:
            f.write(decrypted_data)
    except Exception as e:
        print(f"Um erro ocorreu durante a encriptação: {e}")


if __name__ == "__main__":
    input_file = "ref/via_lactea_olavo_bilac.txt"
    encrypted_file = "Encrypted_File"
    decrypted_file = "Decrypted_File.txt"

    # Encriptar um arquivo
    key, iv = encrypt_file(input_file, encrypted_file)
    if key and iv:
        print("Arquivo encriptado com sucesso.")
        print("Chave:", key)
        print("IV:", iv)
        decrypt_file(key, iv, encrypted_file, decrypted_file)
        print("Arquivo decriptado com sucesso.")
    else:
        print("Encriptação falhou.")
