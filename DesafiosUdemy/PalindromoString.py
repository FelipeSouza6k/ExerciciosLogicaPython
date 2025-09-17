class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        x_string = str(x)
        x_invertido  = x_string[::-1]

        return x_string == x_invertido
         


solver = Solution()

resultado = solver.isPalindrome(121)
print(resultado)