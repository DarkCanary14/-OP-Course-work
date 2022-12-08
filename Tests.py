import unittest
import main
import tkinter as tk


class TestHillCipher(unittest.TestCase):

    def test_1(self):
        t = [0, 0]
        win_test = main.MainForm(t)
        key = [[15, 4], [11, 3]]
        text = ['HE', 'LL', 'OZ']
        self.assertEqual(win_test.encrypt_decrypt(text, key), 'RLBYYV')

    def test_2(self):
        t = [0, 0]
        win_test = main.MainForm(t)
        key = [[3, -4], [-11, 15]]
        text = ['RL', 'BY', 'YV']
        self.assertEqual(win_test.encrypt_decrypt(text, key), 'HELLOZ')

    def test_3(self):
        t = [0, 0]
        win_test = main.MainForm(t)
        key = [[3, -4], [-11, 15]]
        text = ['']
        self.assertEqual(win_test.encrypt_decrypt(text, key), None)

    def test_4(self):
        t = [0, 0]
        win_test = main.MainForm(t)
        key = [[3, -4], [-11, 15]]
        text = [' ']
        self.assertEqual(win_test.encrypt_decrypt(text, key), None)

    def test_5(self):
        t = [0, 0]
        win_test = main.MainForm(t)
        text = '12'
        self.assertEqual(win_test.prepare_text(text, win_test.alpha), None)


if __name__ == '__main__':
    unittest.main()
