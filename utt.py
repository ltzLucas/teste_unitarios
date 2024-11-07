from collections import Counter

class UtilitariosAnaliseTexto:
    def __init__(self, text):
        self.text = text

    def contar_palavras_unicas(self):
        """Conta o número de palavras únicas na string."""
        return len(set(self.text.lower().split()))

    def frequencia_caracteres(self):
        """Retorna a frequência de cada caractere em um dicionário, ignorando espaços."""
        caracteres = [char.lower() for char in self.text if char.isalnum()]
        return dict(Counter(caracteres))

    def palavra_mais_longa(self):
        """Retorna a palavra mais longa na string. Em caso de empate, retorna a primeira."""
        palavras = self.text.split()
        return max(palavras, key=len) if palavras else ""

    def frequencia_palavras(self):
        """Retorna a frequência de cada palavra na string."""
        palavras = self.text.lower().split()
        return dict(Counter(palavras))

    def palavras_mais_comuns(self, n=3):
        """Retorna as `n` palavras mais comuns em um dicionário, incluindo suas frequências."""
        freq_dict = self.frequencia_palavras()
        palavras_ordenadas = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
        return dict(palavras_ordenadas[:n])

    def eh_anagrama(self, palavra1, palavra2):
        """Verifica se duas palavras são anagramas entre si, ignorando maiúsculas/minúsculas."""
        return sorted(palavra1.lower()) == sorted(palavra2.lower())

    def prefixo_comum(self, lista_palavras):
        """Encontra o prefixo comum mais longo em uma lista de palavras."""
        if not lista_palavras:
            return ""
        palavra_curta = min(lista_palavras, key=len)
        for i, char in enumerate(palavra_curta):
            if any(palavra[i] != char for palavra in lista_palavras):
                return palavra_curta[:i]
        return palavra_curta
