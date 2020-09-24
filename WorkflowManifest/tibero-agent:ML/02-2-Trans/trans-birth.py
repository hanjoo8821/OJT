import sys

def trans_birth(n):
    file_name = './Output/' + n + '.txt'
    file_name_trans = './Output/' + n + '_trans.txt'

    with open(file_name, 'r') as f:
        with open(file_name_trans, 'w') as f_trans:
            lines = f.readlines()
            for line in lines:
                f_trans.write(line + '\n')

if __name__ == '__main__':
    trans_birth(sys.argv[1])