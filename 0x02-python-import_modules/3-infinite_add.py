#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    count = len(sys.argv) - 1
    for i in range(count):
        sum = sum + int(sys.argv[i + 1])
    print("{:d}".format(sum))
