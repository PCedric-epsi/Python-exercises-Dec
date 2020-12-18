
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lowerNumbers = []

#to check each item in the list being lower than given number
def checkValues(a, number):
    for i in a:
        if number > i:
            lowerNumbers.append(i)       

#to avoid wrong input values 
try:
    number = int(input("choose a number: "))
    checkValues(a, number)
    print("lower numbers are : " + ' '.join(map(str, lowerNumbers)))
except Exception as e:
    print("Error : Not a number")
    
