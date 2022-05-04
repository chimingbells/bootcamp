import pandas as pd

from IPython.display import display, HTML

import pandas as pd
from numpy.random import randint

#dict = {'Name': ['Martha', 'Tim', 'Rob', 'Georgia'],
#        'Maths': [87, 91, 97, 95],
 #      'Science':[83,99,84,76]}

#df = pd.DataFrame(dict)

#display(df)

#df.loc[len(df.index)] = ["Amy", 89, 93]

#display(df)




#my example

df = pd.DataFrame({'Name': ['Colton', 'Javier', 'Buddy', 'Andypuss', 'Red'],
                'Burglary': [3, 1, 6, 0, 2],
                'Assault': [4, 1, 10, 1, 1],
                'Murder': [0, 0, 2, 35, 0]})

df2 = pd.DataFrame({'Name': ['Bobby', 'Sonny', 'Chorizo'],
                    'Burglary': [0, 0, 2],
                    'Assault': [1, 1, 0],
                    "Murder": [0, 1, 0]})

index_ = ['R1', 'R2', 'R3', 'R4', 'R5']

location_of_incarceration = ['Baltimore', 'Los Angeles', 'New York', 'Cleveland', 'Indianapolis']
df['Location of Incarceration'] = location_of_incarceration
df.index = index_

#df.loc[len(df.index)] = ['Butch', 9, 5, 1]
print(df)

df3 = pd.concat([df, df2], ignore_index = True)
df3.reset_index()
print(df3)