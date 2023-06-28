import matplotlib.pyplot
import matplotlib.pyplot as plt
tarer = ["A","B","C","D","E"]
tver = [11,13,10,12,-13]
plt.bar(tarer,tver,color=["red","blue","orange","green","gray"])
plt.xlabel("tarer")
plt.ylabel("tver")
plt.title("data")
plt.legend(["imac","iphone","samsund","chromebook","desktop"])
plt.show()
