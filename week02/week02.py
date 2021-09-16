"""
Name:
Class:
MSSV:

You should understand the code you write.
"""

import numpy as np
import cv2


def q_0(input_file, output_file, delay=1):
    """

    :param input_file:
    :param output_file:
    :param delay:
    :return:
    """
    img = cv2.imread(input_file, cv2.IMREAD_COLOR)
    cv2.imshow('Test img', img)
    cv2.waitKey(delay)

    cv2.imwrite(output_file, img)


def q_1():
    print("Task 1")


def q_2():
    print("Task 2")


if __name__ == "__main__":

    q_0('apple.png', 'test_apple.png', 1000)
    q_1()
    q_2()
