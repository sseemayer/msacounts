import msacounts.cext.msacounts as msac
import numpy as np

def read_msa(f, return_indices=True):

    with open(f, 'r') as o:
        msa = o.readlines()

    msa = np.array([[ord(c) for c in x.strip()] for x in msa], dtype=np.uint8)

    if return_indices:
        index_msa(msa, in_place=True)

    return msa

def count(msa):
    nrow, ncol = msa.shape
    counts = msac.msa_count(ncol * ncol * 21 * 21, msa)
    return np.reshape(counts, (ncol, ncol, 21, 21))

def index_msa(msa, in_place=False):
    if in_place:
        msai = msa
    else:
        msai = msa.copy()

    msac.msa_char_to_index(msai)
    return msai

