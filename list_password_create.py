import itertools
import os

def generate_passwords(length, characters):
    # Karakterlerin kombinasyonlarını oluştur
    combinations = itertools.product(characters, repeat=length)

    # Oluşan kombinasyonları stringlere dönüştür
    passwords = [''.join(combination) for combination in combinations]

    return passwords

def main():
    try:
        hanecount = int(input("Kaç haneli şifreler oluşturulsun? (En fazla 11 haneli): "))
        if hanecount < 1 or hanecount > 11:
            print("Hane sayısı 1 ile 11 arasında olmalıdır.")
            return
    except ValueError:
        print("Geçersiz giriş. Lütfen bir tam sayı girin.")
        return

    characters = input("Hangi rakam ve harflerden oluşacak şifreler (örneğin 01234abcdfg): ")

    file_path = input("Şifrelerin kaydedileceği dosya yolunu girin: ")

    file_size = len(characters) ** hanecount * 2 # Tahmini dosya boyutu

    size_units = ['bytes', 'KB', 'MB', 'GB']
    unit_index = 0
    while file_size >= 1024 and unit_index < len(size_units) - 1:
        file_size /= 1024
        unit_index += 1
    print(f"Oluşturulacak şifre dosyasının tahmini boyutu: {file_size:.2f} {size_units[unit_index]}")

    create_passwords = input("Şifre listesini oluşturmak istiyor musunuz? (evet/hayır): ").lower()

    if create_passwords == "evet":
        passwords = generate_passwords(hanecount, characters)

        with open(file_path, "w") as file:
            for password in passwords:
                file.write(password + "\n")

        print(f"{len(passwords)} adet şifre oluşturuldu ve {file_path} dosyasına kaydedildi.")
    else:
        print("Şifre listesi oluşturulmadı. İyi günler!")

if __name__ == "__main__":
    main()
