#open files to read
firstFile = open("primenumbers.txt", "r+")
secondFile = open("happynumbers.txt", "r+")

#read files
firstData = firstFile.read()
secondData = secondFile.read()
  
#put each file datas into a list
firstFileNumbers = firstData.split()
secondFileNumbers = secondData.split()

#check overlapping numbers
overlappingNumbers = sorted(set(firstFileNumbers).intersection(secondFileNumbers))

print('overlapping numbers are :', ' '.join(map(str, overlappingNumbers)))