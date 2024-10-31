import unittest
from functools import wraps

def skip_if_frozen(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return method(self, *args, **kwargs)
    return wrapper

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in list(self.participants):
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class RunnerTest(unittest.TestCase):
    is_frozen = False

    def setUp(self):
        self.runner = Runner("Тестовый бегун", speed=5)

    @skip_if_frozen
    def test_run(self):
        self.runner.run()
        self.assertEqual(self.runner.distance, 10)

    @skip_if_frozen
    def test_walk(self):
        self.runner.walk()
        self.assertEqual(self.runner.distance, 5)

    @skip_if_frozen
    def test_str(self):
        self.assertEqual(str(self.runner), "Тестовый бегун")

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_usain = Runner("Усэйн", 10)
        self.runner_andrey = Runner("Андрей", 9)
        self.runner_nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print({place: str(runner) for place, runner in result.items()})

    @skip_if_frozen
    def test_first_tournament(self):
        tournament = Tournament(90, self.runner_usain, self.runner_nick)
        result = tournament.start()
        self.__class__.all_results[1] = {place: runner for place, runner in result.items()}
        self.assertTrue(result[max(result.keys())] == "Ник")

    @skip_if_frozen
    def test_second_tournament(self):
        tournament = Tournament(90, self.runner_andrey, self.runner_nick)
        result = tournament.start()
        self.__class__.all_results[2] = {place: runner for place, runner in result.items()}
        self.assertTrue(result[max(result.keys())] == "Ник")

    @skip_if_frozen
    def test_third_tournament(self):
        tournament = Tournament(90, self.runner_usain, self.runner_andrey, self.runner_nick)
        result = tournament.start()
        self.__class__.all_results[3] = {place: runner for place, runner in result.items()}
        self.assertTrue(result[max(result.keys())] == "Ник")

if __name__ == "__main__":
    unittest.main()
