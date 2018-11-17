# -*- coding: utf-8 -*-

alpha = u'абвгдеёжзийклмнопрстуфхцчшщьъэюя1234567890.,?!:'


def encode(text, step):
    return text.lower().translate(
        str.maketrans(alpha, alpha[step:] + alpha[:step]))


def decode(text, step):
    return text.lower().translate(
        str.maketrans(alpha[step:] + alpha[:step], alpha))
