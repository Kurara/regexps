import unittest
from main import RegExFormatter


class PythonTests(unittest.TestCase):

    def setUp(self):
        self.text = """L'Italia è prima in Europa per numero di morti 
        legato all'antibiotico-resistenza: dei 33.000 decessi che avvengono nei 
        Paesi Ue ogni anno per infezioni causate da batteri resistenti agli antibiotici, 
        oltre 10.000 si registrano infatti nel nostro Paese.

        E' il quadro aggiornato fornito dall'Istituto superiore di sanità (Iss) in occasione 
        della Settimana mondiale per l'uso consapevole degli antibiotici, dal 18 al 24 novembre.


        In Italia, nel 2018, le percentuali di resistenza alle principali classi di antibiotici 
        per gli otto patogeni sotto sorveglianza (Staphylococcus aureus, Streptococcus pneumoniae, 
        Enterococcus faecalis, Enterococcus faecium, Escherichia coli, Klebsiella pneumoniae, 
        Pseudomonas aeruginosa e Acinetobacter species), spiega l'Istituto sul proprio sito, 
        "si mantengono dunque più alte rispetto alla media europea, pur nell'ambito di un trend 
        in calo rispetto agli anni precedenti".


        L'Italia centrale è l'area con maggiore incidenza di casi segnalati ed è l'unica ad aver 
        mostrato un aumento del tasso di incidenza rispetto al 2017: 4,4 casi su 100.000 residenti 
        (nel 2017 erano 3,8 su 100.000), seguita dal Sud e dalle Isole (3,1 su 100.000 residenti) 
        e dal Nord (2,8 su 100.000 residenti). Nel Centro, la Regione con la più alta incidenza è 
        il Lazio (5,9 su 100.000 residenti), nel Sud e Isole la Puglia (6 su 100.000 residenti) e 
        nel Nord l'Emilia-Romagna (5,2 su 100.000 residenti).


        I soggetti maggiormente coinvolti sono maschi (65,2%), tra 60 e 79 anni (48,5%), 
        ospedalizzati (86,1%) e, tra questi, la maggioranza si trova nei reparti di terapia 
        intensiva (38,3%). Il patogeno più diffuso è Klebsiella pneumoniae (97,7%), ma dalla fine 
        del 2018 si osserva un aumento di altri enzimi, in particolare il batterio New Delhi.


        Sempre nel 2018 sono state inviate segnalazioni di antibiotico-resistenza da 19 Regioni, 
        ma non hanno segnalato casi il Molise e la Basilicata che, insieme alla Valle d'Aosta, 
        non avevano segnalato casi neanche nel 2017.
        """
        
    def test_has_numbers(self):
        tester = RegExFormatter(self.text)
        self.assertTrue(tester.has_numbers())

    def test_has_whole_word(self):
        tester = RegExFormatter(self.text)
        self.assertFalse(tester.has_whole_word('piega'))
        self.assertTrue(tester.has_whole_word('Italia'))
        self.assertTrue(tester.has_whole_word('Europa'))

    def test_count_Italia(self):
        """ Count word "Italia"
        """
        tester = RegExFormatter(self.text)
        words = tester.count_word("Italia")
        self.assertEqual(words, 3)

    def test_count_italia_case_insensitive(self):
        """ Count word "italia"
        """
        tester = RegExFormatter(self.text)
        words = tester.count_word2("italia")
        self.assertEqual(words, 3)

    def test_count_words(self):
        """ Contare le parole intere, 
        i numeri non splittarli, 
        e le parole con la virgola considerarle una.
        """
        tester = RegExFormatter(self.text)
        words = tester.count_all_words()
        self.assertEqual(words, 313)

if __name__ == '__main__':
    unittest.main()