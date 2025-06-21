user_write = input("Enter text to write to the file:")

file = open("output.txt","w")

file.write(user_write)
print("Data succesfully written to output.txt.")


file.close()

user_append = input("Enter addition text to append:")

file = open("output.txt","a")

file.write(user_append)
print("Data successfully appended.")
file.close()

file = open("output.txt","r")
lines = file.readlines()
print("Final contents of 'output.txt")

for i in range(0,len(lines)):

    print("Line",i, ":", lines[i])

file.close()

