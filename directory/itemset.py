# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 21:07:13 2020

@author: Rowland Zhang
"""

class ItemSet:
    # Class Attribues
    tuple_length = 14;

    # Initializer
    def __init__(self, size):
        self.size = size
        
    # Instance method
    def to_string(self):
        print('itemset to string')
       
"""
age: continuous.
workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.
fnlwgt: continuous.
education: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.
education-num: continuous.
marital-status: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.
occupation: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.
relationship: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.
race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.
sex: Female, Male.
capital-gain: continuous.
capital-loss: continuous.
hours-per-week: continuous.
native-country: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.
"""
        
class Age:
    # Initializer
    def __init__(self, param):
        self.value = param

class Workclass:
    # Initializer
    def __init__(self, param):
        switcher = {
                'Private': 2,
                'Self-emp-not-inc': 3,
                'Federal-gov': 4,
                'Local-gov': 5,
                'State-gov': 6,
                'Without-pay': 7,
                'Never-worked': 8
                }
        val = switcher.get(param, 'invalid construction')
        if val == 'invalid construction':
            print('-->Error: rejected contructor input for %s: %s' % (type(self).__name__, param))
            self.value = 'error'
            return
        self.value = val

class Fnlwgt:
    def __init__(self, param):
        self.value = param

class Education:
    # Initializer
    def __init__(self, param):
        switcher = {
                'Bachelors': 2,
                'Some-college': 3,
                '11th': 4,
                'HS-grad': 5,
                'Prof-school': 6,
                'Assoc-acdm': 7,
                'Assoc-voc': 8,
                '9th': 9,
                '7th-8th': 10,
                '12th': 11,
                'Masters': 12,
                '1st-4th': 13,
                '10th': 14,
                'Doctorate': 'd',
                '5th-6th': 56,
                'Preschool': 'p'
                }
        val = switcher.get(param, 'invalid construction')
        if val == 'invalid construction':
            print('-->Error: rejected contructor input for %s: %s' % (type(self).__name__, param))
            self.value = 'error'
            return
        self.value = val

class Education_num:
    def __init__(self, param):
        self.value = param

class Marital_status:
    # Initializer
    def __init__(self, param):
        switcher = {
                'Married-civ-spouse': 2,
                'Divorced': 3,
                'Never-married': 4,
                'Separated': 5,
                'Widowed': 6,
                'Married-spouse-absent': 7,
                'Married-AF-spouse': 8
                }
        val = switcher.get(param, 'invalid construction')
        if val == 'invalid construction':
            print('-->Error: rejected contructor input for %s: %s' % (type(self).__name__, param))
            self.value = 'error'
            return
        self.value = val

class Occupation:
    # Initializer
    def __init__(self, param):
        switcher = {
                'Tech-support': 2,
                'Craft-repair': 3,
                'Other-service': 4,
                'Sales': 5,
                'Exec-managerial': 6,
                'Prof-specialty': 7,
                'Handlers-cleaners': 8,
                'Machine-op-inspct': 9,
                'Adm-clerical': 10,
                'Farming-fishing': 11,
                'Transport-moving': 12,
                'Priv-house-serv': 13,
                'Protective-serv': 14,
                'Armed-Forces': 'd'
                }
        val = switcher.get(param, 'invalid construction')
        if val == 'invalid construction':
            print('-->Error: rejected contructor input for %s: %s' % (type(self).__name__, param))
            self.value = 'error'
            return
        self.value = val

class Relationship:
    # Initializer
    def __init__(self, param):
        switcher = {
                'Wife': 2,
                'Own-child': 3,
                'Husband': 'h',
                'Not-in-family': 'n',
                'Other-relative': 4,
                'Unmarried': 78
                }
        val = switcher.get(param, 'invalid construction')
        if val == 'invalid construction':
            print('-->Error: rejected contructor input for %s: %s' % (type(self).__name__, param))
            self.value = 'error'
            return
        self.value = val

class Race:
    # Initializer
    def __init__(self, param):
        switcher = {
                'White': 2,
                'Asian-Pac-Islander': 3,
                'Amer-Indian-Eskimo': 5,
                'Other': 89,
                'Black': 6
                }
        val = switcher.get(param, 'invalid construction')
        if val == 'invalid construction':
            print('-->Error: rejected contructor input for %s: %s' % (type(self).__name__, param))
            self.value = 'error'
            return
        self.value = val

class Sex:
    # Initializer
    def __init__(self, param):
        switcher = {
                'Male': 2,
                'Female': 3
                }
        val = switcher.get(param, 'invalid construction')
        if val == 'invalid construction':
            print('-->Error: rejected contructor input for %s: %s' % (type(self).__name__, param))
            self.value = 'error'
            return
        self.value = val

class Capital_gain:
    def __init__(self, param):
        self.value = param

class Capital_loss:
    def __init__(self, param):
        self.value = param

class Hours_per_week:
    def __init__(self, param):
        self.value = param

class Native_country:
    # Initializer
    def __init__(self, param):
        switcher = {
                'United-States': 1, 
                'Cambodia': 2, 
                'England': 3, 
                'Puerto-Rico': 4, 
                'Canada': 5, 
                'Germany': 6, 
                'Outlying-US(Guam-USVI-etc)': 7, 
                'India': 8, 
                'Japan': 9, 
                'Greece': 10, 
                'South': 11, 
                'China': 12, 
                'Cuba': 13, 
                'Iran': 14, 
                'Honduras': 15, 
                'Philippines': 16, 
                'Italy': 17, 
                'Poland': 18, 
                'Jamaica': 19, 
                'Vietnam': 20, 
                'Mexico': 21, 
                'Portugal': 22, 
                'Ireland': 23, 
                'France': 24, 
                'Dominican-Republic': 25, 
                'Laos': 26, 
                'Ecuador': 27, 
                'Taiwan': 28, 
                'Haiti': 29, 
                'Columbia': 30, 
                'Hungary': 31, 
                'Guatemala': 32, 
                'Nicaragua': 33, 
                'Scotland': 34, 
                'Thailand': 35, 
                'Yugoslavia': 36, 
                'El-Salvador': 37, 
                'Trinadad&Tobago': 38, 
                'Peru': 39, 
                'Hong': 40, 
                'Holand-Netherlands': 41
                }
        val = switcher.get(param, 'invalid construction')
        if val == 'invalid construction':
            print('-->Error: rejected contructor input for %s: %s' % (type(self).__name__, param))
            self.value = 'error'
            return
        self.value = val

if __name__ == '__main__':
    print("running itemset.py")
    temp = Workclass('Private')
    print(temp.value)
    temp2 = Workclass('personal')
    print(temp2.value)
    temp3 = Education('10th')
    print(temp3.value)
    country = Native_country('El-Salvador')
    print(country.value)


