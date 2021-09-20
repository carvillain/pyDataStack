# #1 - Calculate the BMI (body mass index) on the two lists below using NDArrays...¶

import numpy as np
# formula = weight / (height**2) * 730
height = [69, 70, 71, 72, 73, 74, 75]
weight = [110, 120, 130, 140, 150, 160, 170]

# OUTPUT: [16.86620458 17.87755102 18.82562984 19.71450617 20.54794521 21.32943755
# 22.06222222]


def bmiCalc(list1, list2):
    return print(list(map(lambda x,y: (x/(y**2)*730), list1, list2)))

bmiCalc(weight, height)

weight = np.array(weight)
height = np.array(height)

formula = weight / (height**2) * 730
formula


# #2 - Create a function that will take in two parameters and will create a random matrix based off of those parameters. 
#      Extra: Have additional parameters taken in that allow the user to choose the shape and data type of the matrix


def makeMatrix(low,high,shape): 
    return np.random.uniform(low, high, shape)
    
makeMatrix(1, 10, (5,5))



# #3 - Extra: Open and load the data in the two text files that have the Boston Red Sox hitting data for the past seasons. 
#      Compare the difference in the two years by putting the data into an NDArray and running a differencial operation on it. The column to look for will be SLG.

#Use this function to actually open the data inside of a NDArray
import csv
import numpy as np
import statistics


"""
Example Result - Not the actual result
Boston 18 had more SLG in 2018
[0.404 0.443 0.392 0.403 0.482 0.424 0.402 0.459 0.429 0.354 0.387 0.333
 0.539 0.243 0.262 0.354 0.342 0.339 0.328 0.306 0.222 0.2   1.   ]
"""

FIELDS = ['Rk', 'Pos', 'Name', 'Age', 'G', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'SB', 'CS', 
          'BB', 'SO', 'BA', 'OBP', 'SLG', 'OPS', 'OPS+', 'TB', 'GDP', 'HBP', 'SH', 'SF', 'IBB']

DATATYPES = [('rk', 'i'), ('pos', '|S25'), ('name', '|S25'), ('age', 'i'), ('g', 'i'), ('pa', 'i'), ('ab', 'i'),
                ('r', 'i'), ('h', 'i'), ('2b', 'i'), ('3b', 'i'), ('hr', 'i'), ('rbi', 'i'), ('sb', 'i'), ('cs', 'i'),
                ('bb', 'i'), ('so', 'i'), ('ba', 'f'), ('obp', 'f'), ('slg', 'f'), ('ops', 'f'), ('opsp', 'i'),
                ('tb', 'i'), ('gdp', 'i'), ('hbp', 'i'), ('sh', 'i'), ('sf', 'i'), ('ibb', 'i')]



#Test to make sure you have the correct data

def load_data(filename, d = ','):
    data = np.genfromtxt(filename, delimiter = d, skip_header = 1,
                        usecols = np.arange(0,24), invalid_raise = False,
                        names = FIELDS, dtype = DATATYPES)
    return data

bs2017 = load_data('redsox_2017_hitting.txt')
bs2018 = load_data('redsox_2018_hitting.txt')

slg2017 = statistics.mean(bs2017['SLG'])
slg2018 = statistics.mean(bs2018['SLG'])

if slg2017 < slg2018:
    print(f'The SLG of 2017 is worse than 2018. The Red Sox SLG team average was {slg2018} in 2018!')
else:
    print(f'The SLG of 2017 is better than 2018. The Red Sox SLG team average was {slg2017} in 2017!')