import os

def main():
    str = os.getcwd()
    str = str + "/input.txt"

    with open(str) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    count = 0
    prev = lines[0]
    
    for i in range(1, len(lines)):
        if int(lines[i]) > int(prev):
            count += 1
        
        prev = lines[i]

    print(count)



if __name__ == "__main__":
    main()