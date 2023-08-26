array = [] #our array

def decrement(a): #decrement sort algorithm
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j - 1] < a[j]:
            a[j - 1], a[j] = a[j], a[j - 1]
            j -= 1

def function():
    num1 = input("Number 1: ") #get num1
    num2 = input("Number 2: ") #get num2
    division = int(num2)/int(num1) #make the division
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
        
    else:
        print("Getting out...")
        return 0
    
function()
