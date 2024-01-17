
# BUBBLE SORTING ARRAY

def  Bubblearray(numbers):
#                                                               first we run a smooth loop for the turns, so it will compare i element within the array
    for turn in range(len(numbers)-1):
#                                                               for comparing with other elements we need to create a seconed loop.
        for comparing in range(len(numbers)-1-turn):
#                                                               for storing the numbers in order we just normally swap the values
            if numbers[comparing] < numbers[comparing+1]:
                temp= numbers[comparing]
                numbers[comparing] = numbers[comparing+1]
                numbers[comparing+1]= temp

#                                                               for printing the array we run now the code, in this case I created a new fun for better practice.
def Printarray(numbers):
    for array in range(len(numbers)):

        print(numbers[array], end=" ")


Array = [ 6 , 3 , 4 , 5 , 2 , 1 ] 

Bubblearray(Array)
Printarray(Array)


