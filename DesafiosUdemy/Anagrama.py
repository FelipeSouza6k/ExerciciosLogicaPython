class Solution(object):
    def validAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        contagem_s = {}
        contagem_t = {}

        for char in s:
            contagem_s[char] = contagem_s.get(char, 0) + 1

        for char in t:
            contagem_t[char] = contagem_t.get(char,0 ) + 1

        return  contagem_s == contagem_t


solver = Solution()

resultado = solver.validAnagram("amor", "amot")

print(f"O resultado do teste é: {resultado}")