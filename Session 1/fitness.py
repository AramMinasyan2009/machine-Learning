import matplotlib.pyplot as plt
counts = [5023,6201,7542,4908,7020,58352,4312,6789,5231,7392,9091,5667]
calories = [230,285,320,225,310,270,200,305,240,330,275,260]
dates = ["2022-01-01","2022-01-02","2022-01-03","2022-01-04","2022-01-05","2022-01-06","2022-01-07","2022-01-08","2022-01-09","2022-01-10","2022-01-11","2022-01-12"]
plt.bar(counts,calories,color =[ "red","blue","orange","red","blue","orange","red","blue","orange","red","blue","orange"])
plt.xlabel("qounts")
plt.ylabel("qalories")
plt.title("fitness data")

print(sum(counts) // sum(calories))
plt.show()
