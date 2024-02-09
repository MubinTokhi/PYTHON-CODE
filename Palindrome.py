


def polindorme_num(Number):
    num_str = str(Number)
    len_num = len(num_str)

    for i in range(len_num // 2 ):

        if num_str[i] != num_str[len_num - i - 1]:
            return False
    
    return True


n = int(input("Please enter a number: "))
result=polindorme_num(n)
print(result)
