






class my_name:
    def number(self, n):
        if n == 0:
            return 1
        
        return n * self.number(n - 1)

# Example usage
n = 10
answer = my_name()
result = answer.number(n)
print(f"The factorial of {n} is: {result}")
