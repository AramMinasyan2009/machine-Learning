import matplotlib.pyplot as plt
years = [2010,2012,2014,2016,2018,2020]
population = [8.5,4.5,1.9,6.5,4.8,7.5]
plt.plot(years, population, marker = "o", linestyle= "--", color = "green")
plt.xlabel("years")
plt.ylabel("population")
plt.title("population in yers")
plt.show()
