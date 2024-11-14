import unittest
import module_12.homework_12_4.rt_with_exceptions as runner1
import logging

logging.basicConfig(
    level=logging.INFO,
    filemode = 'w',
    filename = 'runner_tests.log',
    encoding = 'utf-8',
    format = '%(asctime)s - '
             '[%(levelname)s]:\n'
             'Информация о предупреждении: %(message)s\n'
             'Файл: %(pathname)s\n'
             'Функция: %(funcName)s\n')

is_frozen = True

class RunnerTest(unittest.TestCase):

    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            test = runner1.Runner('Alice', -5)
            for _ in range(10):
                test.walk()

            self.assertEqual(test.distance, 50)
        except ValueError:
            logging.warning("Неверная скорость для Runner")

    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            test = runner1.Runner(['Alice', 'Maria'])
            for _ in range(10):
                test.run()

            self.assertEqual(test.distance, 100)
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")

    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test_1 = runner1.Runner('Maria')
        test_2 = runner1.Runner('Alice')
        for _ in range(10):
            test_1.run()
            test_2.walk()
        self.assertNotEqual(test_1.distance, test_2.distance)

if __name__ == '__main__':
    unittest.main()