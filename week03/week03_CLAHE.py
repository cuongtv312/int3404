"""
Name:
Class:
MSSV:

You should understand the code you write.
"""

import numpy as np
import cv2
import argparse


def apply_CLAHE(input_file, output_file):
    """
    Performs a CLAHE on the input image.
    """
    img = cv2.imread(input_file, 0)

    # Convert image to gray channgel
    img_eq = None

    cv2.imwrite(output_file, img_eq)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", "-i", type=str, help="Path to input image")
    parser.add_argument("--output_file", "-o", type=str, help="Path to output image")

    args = parser.parse_args()

    apply_CLAHE(input_file=args.input_file, output_file=args.output_file)
