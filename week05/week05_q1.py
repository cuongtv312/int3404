"""
Name:
Class:
MSSV:

You should understand the code you write.
"""

import cv2
import numpy as np
import argparse
import time


def conv_sum(a, b):
    s = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            s += a[i][j]*b[i][j]
    return s


def my_convolution(I, g, mode='valid', boundary='zero_padding'):
    h, w = len(g), len(g[0])
    H, W = I.shape[0], I.shape[1]

    if mode == 'valid':
        output_h = H - (h - 1)
        output_w = W - (w - 1)
    else:
        output_h = H
        output_w = W

    output = [[0 for _ in range(output_w)] for _ in range(output_h)]
    for i in range(output_h):
        for j in range(output_w):
            output[i][j] = conv_sum(I[i:i + h, j:j + w], g)

    return output


def init_kernel(sz=3):
    s = sz*sz
    g = [[1.0/s for i in range(sz)] for i in range(sz)]

    return g


def mean_filter(input_file, output_file, kernel_size):
    # Read input file with gray value
    img = cv2.imread(input_file, 0)
    g = init_kernel(kernel_size)

    start_time = time.time()
    output_img = my_convolution(img, g)
    run_time = time.time() - start_time

    # for input/output
    cv2.imwrite(output_file, np.array(output_img))
    print("Run convolution in: %.2f s" % run_time)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", "-i", type=str, help="Path to input image")
    parser.add_argument("--output_file", "-o", type=str, help="Path to output image")
    parser.add_argument("--filter_type", "-t", type=str, default='mean', help="One of mean/median/sharpness")
    parser.add_argument("--size", "-s", type=int, default=3, help="Size of filter")
    parser.add_argument("--alpha", "-a", type=float, default=0.2, help="Strengh of sharpen operator")

    args = parser.parse_args()
    if args.filter_type == 'mean':
        mean_filter(args.input_file, args.output_file, args.size)