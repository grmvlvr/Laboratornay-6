# Функция получает количество критериев и возвращает весовые коэффициенты
def calculate_weights(count):
    matrica = [[1] * count for _ in range(count)]
    
# Ввод данных для попарного сравнения критериев
    for i in range(count):
        for j in range(i+1,count):
            while True:
                try:
                    krit = float(input(f"Введите отношение между критерием {i+1} и критерием {j+1} (от 1 до 9): "))
                    if krit < 1 or krit > 9:
                        raise ValueError
                    break
                except ValueError:
                    print("Ошибка ввода. Пожалуйста, введите число от 1 до 9.")
                    
            # Сохраняем значение в матрице для дальнейшей работы с ней
            matrica[j][i] = krit
            matrica[i][j] = 1 / krit

    # Создание новой матрицы, где каждый элемент делится на сумму строки
    normal_matrica = [[0] * count for _ in range(count)]
    for i in range(count):
        column_sum = sum(matrica[j][i] for j in range(count))
        for j in range(count):
            normal_matrica[j][i] = matrica[j][i] / column_sum
            
    # Вычисление весовых коэффициентов, суммируя все элементы в строке и делит их на количество критериев
    weights = [sum(row) / count for row in normal_matrica]
    return weights

# Функция main запрашивает количество критериев, чтобы сделать проверку ввода;
# сохраняет весовые коэффициенты, чтобы вывести на экран с округлением до 2х знаков
def main():
    while True:
        try:
            count = int(input("Введите количество критериев: "))
            if count < 2:
                raise ValueError
            break
        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите целое число больше 1.")
    
    weights = calculate_weights(count)
    
    print("Весовые коэффициенты:")
    for i, weight in enumerate(weights):
        print(f"Критерий {i+1}: {weight:.2f}")

if __name__ == "__main__":
    main()
