import unittest
import main


class TestHillCipher(unittest.TestCase):

    def test_1(self):
        win_test = main.MainForm()
        key = [[15, 4], [11, 3]]
        text = ['HE', 'LL', 'OZ']
        self.assertEqual(win_test.encrypt_decrypt(text, key), 'RLBYYV')

    def test_2(self):
        win_test = main.MainForm()
        key = [[3, -4], [-11, 15]]
        text = ['RL', 'BY', 'YV']
        self.assertEqual(win_test.encrypt_decrypt(text, key), 'HELLOZ')

    def test_3(self):
        win_test = main.MainForm()
        key = [[3, -4], [-11, 15]]
        text = ['']
        self.assertEqual(win_test.encrypt_decrypt(text, key), None)

    def test_4(self):
        win_test = main.MainForm()
        key = [[3, -4], [-11, 15]]
        text = [' ']
        self.assertEqual(win_test.encrypt_decrypt(text, key), None)

    def test_5(self):
        win_test = main.MainForm()
        text = '12'
        self.assertEqual(win_test.prepare_text(text, win_test.alpha), None)


if __name__ == '__main__':
    unittest.main()
