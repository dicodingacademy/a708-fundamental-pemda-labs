def get_numbers():
    numbers = input("MASUKAN ANGKA => Masukkan angka dengan spasi sebagai pemisahnya (gunakan titik '.' jika ingin "
                    "menggunakan desimal): ")

    # Memisahkan dan mengonversi angka menjadi tipe data float.
    try:
        number_list = [float(numbers) for numbers in numbers.split()]
    except ValueError:
        raise ValueError("Masukkan angka dengan spasi sebagai pemisah dan gunakan '.' ketika menggunakan desimal.")

    # Menangani input kurang dari 1.
    if len(number_list) <= 1:
        raise ValueError("Harap masukkan Angka lebih dari satu!")

    return number_list


def addition(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result += number
    return round(result, 2)


def subtraction(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result -= number
    return round(result, 2)


def multiplication(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result *= number
    return round(result, 2)


def division(numbers):
    result = numbers[0]
    try:
        for number in numbers[1:]:
            result /= number
    except ZeroDivisionError:
        raise ZeroDivisionError("Anda tidak bisa membagi bilangan dengan angka 0!")

    return round(result, 2)
