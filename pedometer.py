import datetime as dt

FORMAT = "%H:%M:%S"

WEIGHT = 75  # Вес.
HEIGHT = 175  # Рост.
K_1 = 0.035  # Коэффициент для подсчета калорий.
K_2 = 0.029  # Коэффициент для подсчета калорий.
STEP_M = 0.65  # Длина шага в метрах.
storage_data = {}  # Словарь для хранения полученных данных.


def check_correct_data(data):
    """Проверка корректности полученного пакета."""
    if len(data) != 2:
        return False
    elif None in data:
        return False
    else:
        return True


def check_correct_time(time):
    """Проверка корректности параметра времени."""
    if storage_data and time <= max(storage_data.keys()):
        return False
    else:
        return True


def get_step_day(steps):
    """Получить количество пройденных шагов за этот день."""
    return sum(storage_data.values()) + steps


def get_distance(steps):
    """Получить дистанцию пройденного пути в км."""
    dist = (steps * STEP_M / 1000)
    
    return dist


def get_spent_calories(dist, current_time):
    """Получить значения потраченных калорий."""
    time = current_time.hour + current_time.minute/60
    mean_speed = (dist / time)
    return (
        (K_1 * WEIGHT + (mean_speed ** 2 / HEIGHT) * K_2 * WEIGHT) * time * 60
    )


def get_achievement(dist):
    """Получить поздравления за пройденную дистанцию."""
    if dist >= 6.5:
        message = "Отличный результат! Цель достигнута."
    elif 3.9 <= dist < 6.5:
        message = "Неплохо! День был продуктивным."
    elif 2 <= dist < 3.9:
        message = "Маловато, но завтра наверстаем!"
    elif dist < 2:
        message = "Лежать тоже полезно. Главное — участие, а не победа!"

    return message


def show_message(time, steps, dist, calories, achievement):
    """Вывести на экран результаты вычислений"""
    print(f'''
Время: {time}.
Количество шагов за сегодня: {steps}.
Дистанция составила {dist:.2f} км.
Вы сожгли {calories:.2f} ккал.
{achievement}
''')


def accept_package(data):
    """Обработать пакет данных."""

    if check_correct_data(data) is False:
        return 'Некорректный пакет'

    pack_time = dt.datetime.strptime(data[0], FORMAT).time()

    if check_correct_time(pack_time) is False:
        return 'Некорректное значение времени'

    day_steps = get_step_day(data[1])
    dist = get_distance(day_steps)
    spent_calories = get_spent_calories(dist, pack_time)
    achievement = get_achievement(dist)
    show_message(pack_time, day_steps, dist, spent_calories, achievement)
    storage_data[pack_time] = day_steps

    return storage_data


package_0 = ('2:00:01', 505)
package_1 = (None, 3211)
package_2 = ('9:36:02', 15000)
package_3 = ('9:36:02', 9000)
package_4 = ('8:01:02', 7600)

accept_package(package_0)
accept_package(package_1)
accept_package(package_2)
accept_package(package_3)
accept_package(package_4)