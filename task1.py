try:
    file = open('sample.txt', 'r')
    lines = file.readlines()
    print("Reading file contents.")

    for i in range(0,len(lines)):

        print("Line",i, ":", lines[i])

    file.close()

except:

    print("Error: The file 'sample.txt' was not found.")

