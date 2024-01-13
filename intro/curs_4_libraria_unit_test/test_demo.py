import unittest


class TestDemo(unittest.TestCase):

    def setUp(self):
        print("Se ruleaza metoda setUp()")
        pass

    def tearDown(self):
        print("Se ruleaza metoda tearDown()\n")
        pass

    def test_1(self):
        print("Se ruleaza test_1")
        self.metoda_auxiliara()
        pass

    def test_2(self):
        print("Se ruleaza test_2")
        pass

    @unittest.skip
    def test_3(self):
        print("Se ruleaza test_3")
        pass

    def metoda_auxiliara(self):
        print("Se ruleaza metoda auxiliara (numai daca este apelata in teste)")
