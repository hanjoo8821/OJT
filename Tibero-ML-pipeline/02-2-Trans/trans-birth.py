import sys

def trans_birth(n):
    file_name = './Output/' + n + '.txt'
    file_name_trans = './Output/' + n + '_trans.txt'

    with open(file_name, 'r') as f:
        with open(file_name_trans, 'w') as f_trans:
            lines = f.readlines()
            for line in lines:
                print(line.replace('\n', ''))
                line = line[2:10].replace('-', '')
                line = float(line) / 10000
                f_trans.write(str(line) + '\n')

    print("")

    with open(file_name_trans, 'r') as f_trans:
        lines = f_trans.readlines()
        for line in lines:
            print(line.replace('\n', ''))

if __name__ == '__main__':
    trans_birth(sys.argv[1])