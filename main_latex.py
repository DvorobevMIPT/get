import matplotlib.pyplot as plt
import pandas as pd

fig = plt.figure()
ax = fig.add_subplot()
ax1 = fig.add_subplot()
twenty = pd.read_excel(io = 'Book.xlsx', engine='openpyxl', usecols = 'A:B', header = 0, nrows = 30 ) #считываем эксельки
fraction = twenty['fraction']       #делаем столбцы одноименными массивами
triggers = twenty['triggers']
fourty = pd.read_excel(io = 'book1.xlsx', engine='openpyxl', usecols = 'A:B', header = 0, nrows = 40)
print(fourty.head(40))      #надеюсь я это удалю
fraction1 = fourty['fraction']
triggers1 = fourty['triggers']
plt.step(triggers+0.5, fraction, color = 'black')   #делаем обводку гистограммы 10 сек, +5 отвечает за съезд
ax1.bar(triggers1, fraction1, width = 0.25, color = 'orange')   #делаем гистограмму 40 сек и ее обводку
#ax1.step(triggers1 + 0.125, fraction1, color = 'red')    #Надеюсь я это починю


ax.set_ylim(ymin=0)
plt.show()