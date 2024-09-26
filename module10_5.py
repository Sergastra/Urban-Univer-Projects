import multiprocessing
import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            else:
                all_data.append(line)


filenames = [f'./example{number}.txt' for number in range(1, 5)]

# линейный
start = datetime.datetime.now()
for name in filenames:
    read_info(name)
end = datetime.datetime.now()
print(f'{end - start} - (линейный)')

# многопроцессный
if __name__ == '__main__':
    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=8) as pool:
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(f'{end - start} - (многопроцессорный)')
