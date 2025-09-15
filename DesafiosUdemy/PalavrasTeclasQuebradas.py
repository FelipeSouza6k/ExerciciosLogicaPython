class Solution(object):
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ListaDepalavras = text.split(' ')
        teclasQuebradas = set(brokenLetters)
        contadorPalavras = 0
        for palavra in ListaDepalavras:
            palavraDigitavel = True
            for letra in palavra:
                if letra in teclasQuebradas:
                    palavraDigitavel = False
                    break

            if palavraDigitavel:
                contadorPalavras += 1
        
        return contadorPalavras


solver = Solution()
result = solver.canBeTypedWords('hello world', 'hw')
print(f"Palavras digitáveis: {result}")

result = solver.canBeTypedWords('leet code', 'lc')
print(f"Palavras digitáveis: {result}")

