import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'Day': ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница'],
    'Temperature': [10, 12, 8, 14, 11],
    'Humidity': [80, 75, 78, 70, 82],
    'Wind Speed': [5, 6, 4, 7, 5]
})

mean_temperature = np.mean(data['Temperature'])
mean_humidity = np.mean(data['Humidity'])
mean_wind_speed = np.mean(data['Wind Speed'])

data['Отклонение температуры'] = data['Temperature'] - mean_temperature
hottest_day = data.loc[data['Temperature'].idxmax()]

print("Анализ данных о погоде с использованием Pandas и Numpy:")
print(f"Средняя температура: {mean_temperature}°C")
print(f"Средняя влажность: {mean_humidity}%")
print(f"Средняя скорость ветра: {mean_wind_speed} м/с")
print(f"Самый тёплый день: {hottest_day['Day']} с температурой {hottest_day['Temperature']}°C")

plt.figure(figsize=(8, 5))

plt.bar(data['Day'], data['Temperature'], color='skyblue', label='Температура')
plt.plot(data['Day'], data['Отклонение температуры'], color='red', marker='o', label='Отклонение температуры')

plt.title('Температура и отклонение от среднего значения в Москве')
plt.xlabel('День')
plt.ylabel('Температура (°C)')
plt.legend()
plt.grid(True)

plt.show()
