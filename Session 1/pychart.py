import matplotlib.pyplot as plt
categoris = ["1","2","3","4"]
togos = [25,25,25,25]
explode = [0,0.1,0,0]
colors = ["red","green","blue","red"]

plt.pie(togos, explode = explode, labels = categoris, colors = colors, shadow = True)
plt.title("sd'lhf;aj")
plt.legend(categoris)
plt.show()

