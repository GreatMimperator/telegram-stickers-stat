import pandas as pd
import matplotlib.pyplot as plt

# Чтение данных из CSV файла
data = pd.read_csv('statistics.csv')

# Преобразование столбца с датами в формат datetime
data['date'] = pd.to_datetime(data['date'], format='%m/%d/%Y')

# Определение выходных дней (пятница и суббота)
weekends = data['date'].dt.weekday.isin([4, 5])

# Построение графиков
plt.figure(figsize=(14, 8))

# График использования
plt.subplot(3, 1, 1)
plt.plot(data['date'], data['usage'], marker='o', color='b', label='Usage')
plt.fill_between(data['date'], data['usage'], where=weekends, color='red', alpha=0.3)
plt.title('Usage Over Time')
plt.xlabel('Date')
plt.ylabel('Usage')
plt.grid(True)
plt.legend()

# График установок
plt.subplot(3, 1, 2)
plt.plot(data['date'], data['installed'], marker='o', color='g', label='Installed')
plt.fill_between(data['date'], data['installed'], where=weekends, color='red', alpha=0.3)
plt.title('Installed Over Time')
plt.xlabel('Date')
plt.ylabel('Installed')
plt.grid(True)
plt.legend()

# График удалений
plt.subplot(3, 1, 3)
plt.plot(data['date'], data['removed'], marker='o', color='r', label='Removed')
plt.fill_between(data['date'], data['removed'], where=weekends, color='red', alpha=0.3)
plt.title('Removed Over Time')
plt.xlabel('Date')
plt.ylabel('Removed')
plt.grid(True)
plt.legend()

# Автоматическое выравнивание осей
plt.tight_layout()
plt.show()
