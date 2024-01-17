


N= int(input("Print any number for butterfly: "))

#printing line
for i in range (N+1):
    #=====================================================================================For printing i stars
    for j in range(i):
        print("* ", end=(" "))
        j+=1
        #=============================================================================for printing double spaces
    for k in range((N-i)*2):
        print("  ", end=(" "))
        k+=1
        #===============================================================================for printing again stars
    for w in range(i):
        print("* ", end=(" "))
    print()
    i+=1
    
#======================================================================the same code applies just the converted version of it, (N, 0, -1) it is downgrading N by one
for i in range(N, 0, -1) :
    #=====================================================================================For printing i stars
    for j in range(i):
        print("* ", end=(" "))
        j+=1
            #=============================================================================for printing double spaces

    for k in range((N-i)*2):
        print("  ", end=(" "))
        k+=1
               #===============================================================================for printing again stars
 
    for w in range(i):
        print("* ", end=(" "))
        # for continuing to the next line
    print()
    i-=1