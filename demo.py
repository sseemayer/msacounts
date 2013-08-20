#!/usr/bin/env python

"""msacounts demo

Compile the C extensions using `python setup.py build_ext --inplace` before running this!
"""

import msacounts
import sys
import numpy as np

def main():

    aln = msacounts.read_msa('data/1atzA.aln')
    counts = msacounts.pair_counts(aln)

    pwm = msacounts.pwm(counts)

    np.savetxt('pwm.txt', pwm)


if __name__ == '__main__':
    main()
