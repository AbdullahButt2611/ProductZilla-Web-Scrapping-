# string ="1423.92 sold"
# string = int(string.split(' ')[0])
# print(string)

Price = str("PKR 1423.92")
Price = float("".join(Price.split(' ')[1].split(',')))
print(Price)
