import os

def main():
    str = os.getcwd()
    str = str + "/input.txt"

    with open(str) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    count = 0
    sum1 = int(lines[0]) + int(lines[1]) + int(lines[2])
    for i in range(3, len(lines)):
        sum_iter = int(lines[i - 2]) + int(lines[i - 1]) + int(lines[i])
        if sum_iter > sum1:
            count += 1
        sum1 = sum_iter
    print(count)

if __name__ == "__main__":
    main()