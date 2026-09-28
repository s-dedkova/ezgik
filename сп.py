import math
s = input('Введите строку параметров пуска: ')
speed = float(s.split('|')[1].split('=')[1].split()[0])
angle_deg = float(s.split('|')[2].split('=')[1].split()[0])
angle_rad = math.radians(angle_deg)
height = math.pow(speed, 2) * math.pow(math.sin(angle_rad), 2) / (2 * 9.81)
print(f'Высотап подъема: {round(height)} м')