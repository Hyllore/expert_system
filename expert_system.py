import sys

def filsdeputs(o):
    print o

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
            content = f.readlines()
    content = [x.strip() for x in content]
    filsdeputs(content)


