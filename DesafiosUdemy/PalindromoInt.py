class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x > 0 and x % 10 == 0:
            return False

        if x == 0:
            return True

        numero_revertido = 0

        numero_original = x

        while x > 0:
                    
            ultimo_digito = x % 10

            numero_revertido = (numero_revertido * 10) + ultimo_digito

            x = x // 10

        return numero_original == numero_revertido
    
solver = Solution()

resultado = solver.isPalindrome(203)
print(resultado)