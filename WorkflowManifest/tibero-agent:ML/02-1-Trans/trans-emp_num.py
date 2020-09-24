import sys

def trans_emp_num(n):
    file_name = './Output/' + n + '.txt'
    file_name_trans = './Output/' + n + '_trans.txt'

    with open(file_name, 'r') as f:
        with open(file_name_trans, 'w') as f_trans:
            lines = f.readlines()
            for line in lines:
                line = line[2:]
                f_trans.write(line + '\n')

if __name__ == '__main__':
    trans_emp_num(sys.argv[1])