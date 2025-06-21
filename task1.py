try:
    file = open('sample.txt', 'r')
    lines = file.readlines()
    for i in range(0,len(lines)):
        print(lines[i])

except:
    print("no such file exists.")

