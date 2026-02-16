# Update your code below this line
import pandas as  pd 
import numpy as np

s1 =pd.Series([ 'apple', 'banana', 'cherry', 'date'])

s2 = pd.Series(np.array( [0.5, 0.3, 0.8, 0.6]))

s3 = pd.Series({'apple': 0.5, 'banana': 0.3, 'cherry': 0.8, 'date': 0.6})

print(s1,s2,s3)
