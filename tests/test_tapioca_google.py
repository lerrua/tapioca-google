# coding: utf-8

import unittest

from tapioca_google import Google


class TestTapiocaGoogle(unittest.TestCase):

    def setUp(self):
        self.wrapper = Google()


if __name__ == '__main__':
    unittest.main()
