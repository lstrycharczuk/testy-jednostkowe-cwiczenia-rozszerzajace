def sum_file(file):
    sum = 0
    try:
        with open(file, 'r') as file:
            data = file.read().strip().split(';')
            if len(data) == 1 and data[0] == '':
                return 0
            liczby = []
            for i, val in enumerate(data):
                if data[i].isalpha():
                    raise TypeError('Plik zawiera litery, a powinny być same liczby')

                if int(data[i]) < -10 or int(data[i]) > 10:
                    raise ValueError('Liczba musi być w przedziale od [-10; 10]')
                liczby.append(int(data[i]))
            for j in liczby:
                sum += j
    except FileNotFoundError:
        raise FileNotFoundError('Nie ma takiego pliku')
    return sum

print(sum_file('../tests/test_sum_input.txt'))


