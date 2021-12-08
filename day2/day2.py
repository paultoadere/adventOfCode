import os

def main():
    str = os.getcwd()
    str = str + "/input.txt"

    with open(str) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    depth=0
    horizontal=0
    aim=0

    for i in range(0, len(lines)):
        row=(lines[i].split(" "))
        if row[0] == "forward":
            horizontal += int(row[1])
            depth += (int(row[1]) * aim)
        elif row[0] == "down":
            aim += int(row[1])
        else: 
            aim -= int(row[1])

    print(horizontal * depth)



if __name__ == "__main__":
    main()