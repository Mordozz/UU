import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walker = Runner("Алекс")
        for _ in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    def test_run(self):
        runner = Runner("Влад")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner = Runner("Ильич")
        walker = Runner("Каплан")
        for _ in range(10):
            runner.run()
            walker.walk()
        self.assertNotEqual(runner.distance, walker.distance, "Ильич не убежал от Каплан")


if __name__ == "main":
    unittest.main()
