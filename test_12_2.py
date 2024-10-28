import runner_and_tournament as rt
import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.r1 = rt.Runner('Усэйн', 10)
        self.r2 = rt.Runner('Андрей', 9)
        self.r3 = rt.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i, elem in enumerate(cls.all_results):
            print(elem)

    def test_tournament_1(self):
        t1 = rt.Tournament(90, self.r1, self.r3)
        t1_result = {k: str(x) for k, x in t1.start().items()}
        TournamentTest.all_results.append(t1_result)
        self.assertTrue(t1_result[2], 'Ник')

    def test_tournament_2(self):
        t2 = rt.Tournament(90, self.r2, self.r3)
        t2_result = {k: str(x) for k, x in t2.start().items()}
        TournamentTest.all_results.append(t2_result)
        self.assertTrue(t2_result[2], 'Ник')

    def test_tournament_3(self):
        t3 = rt.Tournament(90, self.r2, self.r1, self.r3)
        t3_result = {k: str(x) for k, x in t3.start().items()}
        TournamentTest.all_results.append(t3_result)
        self.assertTrue(t3_result[3], 'Ник')


if __name__ == "__main__":
    unittest.main()
