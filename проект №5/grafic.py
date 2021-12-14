import matplotlib.pyplot as plt

potato_price = [45,45,40,35,35,40]
cabbage_price = [50,45,40,30,35,35]
onion_price = [70,60,60,45,45,60]
apple_price = [55,50,46.67,36.67,38.33,45]
year = [1,2,3,4,5,6]

plt.plot(year,potato_price,label = "Картопля")
plt.plot(year,cabbage_price,label = "Капуста")
plt.plot(year,onion_price,label = "Цибуля")


plt.plot(year,apple_price,label = "Середня ціна")
plt.xlabel("Дата")
plt.ylabel("Ціна")
plt.legend()
plt.grid(True)

plt.show()
