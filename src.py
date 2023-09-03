array = [] #our array
doInfo = open("info.txt", "a")

def decrement(a): #decrement sort algorithm
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j - 1] < a[j]:
            a[j - 1], a[j] = a[j], a[j - 1]
            j -= 1

def book(a):
    doInfo.write('early results:\n')
    for j in range(0, len(a)):
        doInfo.write(str(array[j]) + ', ')

    doInfo.write('\nAdd Descriptions: \n')

def book_desc(string):
        book(array)
        doInfo.write(string)

def function():
    num1 = input("Favorable cases: ") #get num1
    num2 = input("Total cases: ") #get num2
    division = int(num1)/int(num2) #make the division
    percent = division*100 #turn results of division in percent's
    array.extend([int(percent)]) #put the result in the end of the array
    again = input("Continue? (y/n): ") 
    if again == 'y': 
        function() #restart
    elif again == 'n': #here you can see your array in decrescent order
        print("Ok, here's your array:\n")
        #decrement 
        decrement(array)
        print(array)
        print("\n")
        desc = input("ADD DESCRIPTION: ")
        book_desc(desc)
    
    

function()
input("Press any key to exit...")
