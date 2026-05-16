def xor_bytes(data, key):
    result = bytearray()

    for i in range(len(data)):
        result.append(data[i] ^ key[i])

    return bytes(result)


print(" Однократное гаммирование")

print("\n1 - Шифрование")
print("2 - Дешифрование")
print("3 - Найти ключ")

choice = input("\nВыберите действие: ")

if choice == "1":

    text = input("Введите открытый текст: ")
    key = input("Введите ключ такой же длины: ")

    if len(text) != len(key):
        print("Ошибка: длины текста и ключа должны совпадать!")
        exit()

    text_bytes = text.encode("utf-8")
    key_bytes = key.encode("utf-8")

    cipher = xor_bytes(text_bytes, key_bytes)

    print("\nШифротекст (HEX):")
    print(cipher.hex())



elif choice == "2":

    cipher_hex = input("Введите шифротекст HEX: ")
    key = input("Введите ключ: ")

    cipher_bytes = bytes.fromhex(cipher_hex)
    key_bytes = key.encode("utf-8")

    if len(cipher_bytes) != len(key_bytes):
        print("Ошибка: длины ключа и шифротекста должны совпадать!")
        exit()

    decrypted = xor_bytes(cipher_bytes, key_bytes)

    print("\nОткрытый текст:")
    print(decrypted.decode("utf-8"))



elif choice == "3":

    text = input("Введите открытый текст: ")
    cipher_hex = input("Введите шифротекст HEX: ")

    text_bytes = text.encode("utf-8")
    cipher_bytes = bytes.fromhex(cipher_hex)

    if len(text_bytes) != len(cipher_bytes):
        print("Ошибка: длины должны совпадать!")
        exit()

    key = xor_bytes(text_bytes, cipher_bytes)

    print("\nНайденный ключ:")
    print(key.decode("utf-8"))


else:
    print("Неверный выбор!")
