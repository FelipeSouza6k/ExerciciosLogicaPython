
class Solution(object):
    def validAnagram(self, s: str, t: str):
        validationInS = []
        validationInT = []
        for char in s:
            validationInS.append(char)
        for char in t:
            validationInT.append(char)
        validationInS.sort()
        validationInT.sort()
        if validationInT == validationInS:
            return True
        else:
            return False

solver = Solution()

resultado = solver.validAnagram("esteira", "esteira")

print(f"O resultado do teste é: {resultado}")