import unittest


class TestDemo(unittest.TestCase):

    def setUp(self):
        print("Se ruleaza metoda setUp()")
        pass

    def tearDown(self):
        print("Se ruleaza metoda tearDown()\n")
        pass

    def test_6(self):
        print("Se ruleaza test_6")
        self.metoda_auxiliara()
        pass

    def test_4(self):
        print("Se ruleaza test_4")
        pass

    def test_5(self):
        print("Se ruleaza test_5")
        pass

    def metoda_auxiliara(self):
        print("Se ruleaza metoda auxiliara (numai daca este apelata in teste)")
