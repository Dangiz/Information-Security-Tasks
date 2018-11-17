# -*- coding: utf-8 -*-
# Кодировка и раскодировка заданного сообщения методом Цезаря. Русский алфавит.


ALPHA = u'абвгдеёжзийклмнопрстуфхцчшщьъэюя'


def encode(text, step):
    return text.translate(
        str.maketrans(ALPHA, ALPHA[step:] + ALPHA[:step]))


def decode(text, step):
    return text.translate(
        str.maketrans(ALPHA[step:] + ALPHA[:step], ALPHA))
