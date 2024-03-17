import numpy as np

# Функция для определения за сколько попыток программа угадывает число

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

# Функция, которая принимает на вход загаданное число и возвращает число попыток угадывания:

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0 # cчетчик попыток
    min_number = 1 # минимальная граница поиска
    max_number = 101 # максимальная граница поиска
    predict_number = np.random.randint(1, 101) 

    while number != predict_number:  # запускаем цикл пока загаданное число не будет равно предполагаемому
        if number < predict_number:  # если загаданное число меньше предполагаемого
            max_number = predict_number # максимальной границей диапозона, в котором осуществляем поиск, будет предпогаемое число число
            predict_number = (max_number + min_number) // 2 
        elif number > predict_number:   # если загаданное число больше предполагаемого
             min_number = predict_number  # минимальной границей диапозона, в котором осуществляем поиск, будет предпогаемое число число
             predict_number = (max_number + min_number) // 2

        count += 1


    return count
    
print('Run benchmarking for game_core_v3: ', end='')
if __name__ == "__main__":
    # RUN
        score_game(game_core_v3)
