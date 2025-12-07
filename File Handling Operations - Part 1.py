# write in file using with()function
with open('Python/Codingal.txt','w') as file:
    file.write("Hi! I am penguin I am 1 yr old.")
file.close()

# split file into words
with open('Python/Codingal.txt','r') as file:
    data = file.readlines()
    print("Words in the this file are ....")
    for line in data:
        word = line.split()
        print (word)
file.close()