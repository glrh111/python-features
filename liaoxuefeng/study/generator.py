#! /usr/bin/python
# -*- coding: utf-8 -*-

# Generator 简介
# 断言
# 生成器是迭代器，但不仅仅是迭代器，非常方便自定义迭代器iterator

# test 1

# 包含yield关键字，使它成为一个generator


def generator1():
    yield 0
    yield 1
    yield 2
    yield 3
    yield 4

# 计算fabonacci数列


def fabonacci():
    a = b = 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b


for i in fabonacci():
    if i > 100:
        break
    print i
