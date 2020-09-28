import numpy as np
from sklearn import linear_model
import joblib
import matplotlib.pyplot as plt
import os, sys

modeldata = './Output/lrmodel.pkl'

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

def plot_model(n1, n2):
    x_data, y_data = read_data(n1, n2)
    reg = joblib.load(modeldata)
    
    # to plot
    plt.figure(figsize = (10, 8))
    plt.title('Linear Regression:' + n1 + ' - ' + n2, fontsize = 15)
    plt.xlabel(n1, fontsize = 15)
    plt.ylabel(n2, fontsize = 15)
    plt.scatter(x_data, y_data, label = "data")

    # to plot a straight line (fitted line)
    xp = np.arange(85, 100, 1).reshape(-1, 1)
    plt.plot(xp, reg.predict(xp), 'tab:red', linewidth = 1, label = "regression")
    plt.grid(alpha = 0.3)

    # output the image file
    plt.savefig('./Output/graph.png')
    plt.savefig('./WAS/graph.png')
    
    
# def pred_point(n1, n2, x):
#     x_data, y_data = read_data(n1, n2)
#     reg = joblib.load(modeldata)

#     x = np.array([[x]])
#     pred = reg.predict(x)

#     print('predicted {0} for {1} = {2}: {3}'.format(n2, n1, x[0][0], pred[0][0]))
    
#     # to plot
#     plt.figure(figsize = (10, 8))
#     plt.title('Linear Regression:' + n1 + ' - ' + n2, fontsize = 15)
#     plt.xlabel(n1, fontsize = 15)
#     plt.ylabel(n2, fontsize = 15)
#     plt.scatter(x_data, y_data, label = "data")
    
#     # to plot a straight line (fitted line)
#     xp = np.arange(85, 100, 1).reshape(-1, 1)
#     plt.plot(xp, reg.predict(xp), 'tab:purple', linewidth = 1, label = "regression")
    
#     # to plot a test point
#     plt.scatter(x, pred, s = 100, label = "prediction")
#     plt.grid(alpha = 0.3)
#     # plt.show()
#     plt.savefig('./Output/graph.png')
#     plt.savefig('./WAS/graph.png')

if __name__ == '__main__':
    plot_model(sys.argv[1], sys.argv[2])
    # pred_point(sys.argv[1], sys.argv[2], sys.argv[3])