#open file
myFile = open("nameslist.txt", "r+")

#read file
data = myFile.read()

#put file data into a list
words = data.split()

print('there is ', len(words), ' words in the file.')