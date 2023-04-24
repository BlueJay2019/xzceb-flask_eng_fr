from machinetranslation import translator
import unittest

class TestMachineTranslation(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertAlmostEqual(translator.englishToFrench(None), None)
        self.assertAlmostEqual(translator.englishToFrench('Hello'), 'Bonjour')

    def test_frenchToEnglish(self):
        self.assertAlmostEqual(translator.frenchToEnglish(None), None)
        self.assertAlmostEqual(translator.frenchToEnglish('Bonjour'), 'Hello')

unittest.main()