import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

#pd.get_dummies(data['whoAmI'])

def my_dummies(data):
    unique_val = set(data)
    out_dict = {}
    for val in unique_val:
        lst = []
        for curr_val in data:
            lst.append(curr_val == val)
        out_dict[val] = lst
    return pd.DataFrame(out_dict)
    

print(my_dummies(data['whoAmI']))