import numpy as np
from sklearn import linear_model
import joblib
import sys

outputname = './Output/lrmodel.pkl'

def read_data(n1, n2):
    file_name1 = './Output/' + n1 + '_trans.txt'
    file_name2 = './Output/' + n2 + '_trans.txt'

    id1 = []
    id2 = []

    with open(file_name1, 'r') as f1:
        lines = f1.readlines()
        for line in lines:
            id1.append(float(line.replace('\n', '')))

    with open(file_name2, 'r') as f2:
        lines = f2.readlines()
        for line in lines:
            id2.append(float(line.replace('\n', '')))

    id1 = np.array(id1).reshape(-1, 1)
    id2 = np.array(id2).reshape(-1, 1)
    
    return id1, id2

def train(n1, n2):
    x_data, y_data = read_data(n1, n2)
    
    reg = linear_model.LinearRegression()
    reg.fit(x_data, y_data)

    print('coefficient:', reg.coef_[0][0])
    print('y-intercept:', reg.intercept_[0])

    joblib.dump(reg, outputname)

if __name__ == '__main__':
    lrmodel = train(sys.argv[1], sys.argv[2])