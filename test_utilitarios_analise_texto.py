import unittest
from utt import UtilitariosAnaliseTexto

class TestUtilitariosAnaliseTexto(unittest.TestCase):
    def setUp(self):
        self.utilitarios = UtilitariosAnaliseTexto("Testando testes de texto e mais testes de texto")

    def test_contar_palavras_unicas(self):
        self.assertEqual(self.utilitarios.contar_palavras_unicas(), 6)

    def test_frequencia_caracteres(self):
        expected = {'t': 10, 'e': 10, 's': 6, 'a': 2, 'n': 1, 'd': 3, 'o': 3, 'x': 2, 'm': 1, 'i': 1}
        self.assertEqual(self.utilitarios.frequencia_caracteres(), expected)

    def test_palavra_mais_longa(self):
        self.assertEqual(self.utilitarios.palavra_mais_longa(), "Testando")

    def test_palavras_mais_comuns(self):
        expected = {"testes": 2, "de": 2, "texto": 2}
        self.assertEqual(self.utilitarios.palavras_mais_comuns(), expected)

    def test_eh_anagrama(self):
        self.assertTrue(self.utilitarios.eh_anagrama("amor", "roma"))
        self.assertTrue(self.utilitarios.eh_anagrama("amor", "ramo"))

    def test_prefixo_comum(self):
        self.assertEqual(self.utilitarios.prefixo_comum(["testando", "teste", "testemunho"]), "test")
        self.assertEqual(self.utilitarios.prefixo_comum(["carro", "carteira", "caracol"]), "car")
        self.assertEqual(self.utilitarios.prefixo_comum(["livro", "livre", "livramento"]), "livr")
        self.assertEqual(self.utilitarios.prefixo_comum(["livro", "mesa", "caderno"]), "")

if __name__ == "__main__":
    unittest.main()
