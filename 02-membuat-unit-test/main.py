from calculator import get_numbers, addition, subtraction, multiplication, division
import sys


def main():
    while True:
        operations = {
            "1": ("Penjumlahan", addition),
            "2": ("Pengurangan", subtraction),
            "3": ("Perkalian", multiplication),
            "4": ("Pembagian", division)
        }
        print("==========================")
        print("Aplikasi Kalkulator")
        print("==========================")
        print("Pilih operasi aritmetika!")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")
        print("==========================")

        choice = input("PILIH OPERASI => Masukkan Pilihan Anda: ")
        if choice not in operations.keys():
            sys.exit("Keluar Program!")

        try:
            numbers = get_numbers()

            operation_name, function_name = operations[choice]
            result = function_name(numbers)
            print(f"Hasil: {result}")
            break
        except ValueError as ve:
            print(f"Terjadi kesalahan ValueError: {ve}")
            break
        except ZeroDivisionError as ze:
            print(f"Terjadi kesalahan ZeroDivisionError: {ze}")
            break
        except Exception as e:
            print(f"Terjadi kesalahan {e}")
            break


if __name__ == "__main__":
    main()
