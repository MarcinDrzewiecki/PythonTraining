__author__ = 'drzewiec'

from unittest import TestCase
from fibonacci_kata.fibonacci import fib

class FibonacciTest(TestCase):

    def test_fib_for_0(self):
        self.assertEqual(fib(0),1)


    def test_fib_for_1(self):
        self.assertEqual(fib(1),1)

    def test_fib_for_2(self):
        self.assertEqual(fib(2),2)

    def test_fib_for_4(self):
        self.assertEqual(fib(4),5)

    def test_fib_for_100(self):
        self.assertEqual(fib(100),573147844013817084101)