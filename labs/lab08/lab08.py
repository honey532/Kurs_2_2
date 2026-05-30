def xor_bytes(data, key):
    return bytes(a ^ b for a, b in zip(data, key))


# Исходные тексты
P1 = "НаВашисходящийот1204"
P2 = "ВСеверныйфилиалБанка"

# Ключ
key_hex = "05 0C 17 7F 0E 4E 37 D2 94 10 09 2E 22 57 FF C8 0B B2 70 54"
K = bytes.fromhex(key_hex)

# Перевод в байты (1 символ = 1 байт)
P1_bytes = P1.encode("cp1251")
P2_bytes = P2.encode("cp1251")

print("Исходные тексты:")
print("P1 =", P1)
print("P2 =", P2)


# Шифрование

C1 = xor_bytes(P1_bytes, K)
C2 = xor_bytes(P2_bytes, K)

print("\nШифротексты:")
print("C1 =", C1.hex().upper())
print("C2 =", C2.hex().upper())

# Дешифрование
P1_dec = xor_bytes(C1, K).decode("cp1251")
P2_dec = xor_bytes(C2, K).decode("cp1251")

print("\nРасшифровка:")
print("P1 =", P1_dec)
print("P2 =", P2_dec)


# Атака без знания ключа

print("\nАтака при повторном использовании ключа")

# C1 XOR C2 = P1 XOR P2
P1_xor_P2 = xor_bytes(C1, C2)

print("C1 XOR C2 =", P1_xor_P2.hex().upper())

# Предполагаем, что злоумышленник знает P1
Recovered_P2 = xor_bytes(P1_xor_P2, P1_bytes)

print("\nВосстановленный P2 без знания ключа:")
print(Recovered_P2.decode("cp1251"))

# Проверка
if Recovered_P2.decode("cp1251") == P2:
    print("\nАтака успешна.")
else:
    print("\nОшибка восстановления.")
