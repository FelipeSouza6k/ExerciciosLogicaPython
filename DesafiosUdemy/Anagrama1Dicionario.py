class Solution(object):
    def validAnagram(self, s: str, t: str):
        contagem = {}

        for char in s:
            contagem[char] = contagem.get(char, 0)  + 1
        
        for char in t:
            # A letra existe no banco E o saldo dela é positivo?
            if char not in contagem or contagem[char] == 0:
                # Se não existe ou o saldo zerou, não é um anagrama.
                return False
            
            # Se passou na verificação, fazemos a retirada.
            contagem[char] -= 1

        return True
        

        