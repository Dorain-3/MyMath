# test
import math

import mymath
from mymath import *


def test_sin():
    difference = 0
    for i in range(3141):
        difference += abs(math.sin(i * 0.001) - mymath.sin(i * 0.001))
    print(difference / 3141)


def test_cos():
    difference = 0
    for i in range(3141):
        difference += abs(math.cos(i * 0.001) - mymath.cos(i * 0.001))
    print(difference / 3141)


def test_tan():
    difference = 0
    for i in range(3141):
        difference += abs(math.tan(i * 0.001) - mymath.tan(i * 0.001))
    print(difference / 3141)


def test_ln():
    difference = 0
    for i in range(1, 10000):
        difference += abs(math.log(i) - mymath.ln(i))
    print(difference / 10000)


def test_exp():
    difference = 0
    for i in range(1, 300):
        difference += (math.exp(i) - mymath.exp(i)) / math.exp(i)
    print(difference / 300)


def test_atan():
    difference = 0
    for i in range(1000):
        difference += abs(math.atan(i * 0.001) - mymath.atan(i * 0.001))
    print(difference / 1000)


def test_sinh():
    difference = 0
    for i in range(1000):
        difference += abs(math.sinh(i * 0.001) - mymath.sinh(i * 0.001))
    print(difference / 1000)


# test_cos()

# test_tan()

# test_exp()

# test_atan()

test_sinh()
