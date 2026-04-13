
months = [1,2,3,4,5]
profit = [100000,110000,115000,125000,127000]


n = len(months)
sum_x = sum(months)
sum_y = sum(profit)
sum_xy = sum(months[i] * profit[i] for i in range(n))
sum_xx = sum(months[i] ** 2 for i in range(n))

w = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x ** 2)
b = (sum_y - w * sum_x) / n

print(f"w = {w:.0f}")
print(f"b = {b:.0f}")

# التوقع 
def predict(month):
    return w * month + b 

print(f"month 6 : {predict(6):.0f}")
print(f"month 12 : {predict(12):.0f}")

