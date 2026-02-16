import pandas as pd

temperatures = pd.Series([20, 22, 25, 23, 21, 19, 24], 
                         index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])

# Update your code below this line
warmer = temperatures + 2
avg_temp = temperatures.mean()
diff_from_avg = warmer - avg_temp

print(warmer)
print(avg_temp)
print(diff_from_avg)