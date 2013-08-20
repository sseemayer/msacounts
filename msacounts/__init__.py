import msacounts.cext.msacounts as msac
import numpy as np

def read_msa(f, return_indices=True):

    with open(f, 'r') as o:
        msa = o.readlines()

    msa = np.array([[ord(c) for c in x.strip()] for x in msa], dtype=np.uint8)

    if return_indices:
        index_msa(msa, in_place=True)

    return msa

def pair_counts(msa):
    nrow, ncol = msa.shape
    counts = msac.msa_count(ncol * ncol * 21 * 21, msa)
    return np.reshape(counts, (ncol, ncol, 21, 21))


def single_counts(counts):
    return np.sum(counts[np.diag_indices(74)], axis=2)


def pwm(counts, ignore_gaps=False):
    singles = single_counts(counts)

    if ignore_gaps:
        singles = singles[:, 1:]

    nrow = np.sum(singles, axis=1)

    return singles / nrow[:, np.newaxis]


def index_msa(msa, in_place=False):
    if in_place:
        msai = msa
    else:
        msai = msa.copy()

    msac.msa_char_to_index(msai)
    return msai

