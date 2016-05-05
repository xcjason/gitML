import sys
import pdb
import numpy


def input_data(file_name):
    with open(file_name) as f:
        return f.readlines()


def split_data(raw_data):
    header = raw_data[0].split()[1:]
    y, X = [], []
    for row in raw_data[1:]:
        row_data = row.strip().split('\t')
        y.append(row_data[0])
        x = []
        for col in row_data[1:]:
            try:
                x.append(float(col))
            except ValueError:
                x.append(col)
        X.append(x)
    return header, numpy.array(y), numpy.array(X)


def train_model():
    pass


def main():
    file_name = sys.argv[1]
    raw_data = input_data(file_name)
    pdb.set_trace()
    header, y, x = split_data(raw_data)
    pdb.set_trace()
    print ''


if __name__ == '__main__':
    main()
