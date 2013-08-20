#include <assert.h>
#include <string.h>
#include <stdio.h>
#include <ctype.h>

#define N_ALPHA 21

void msa_count(int* counts, int ncounts, unsigned char* msa, int nrow, int ncol) {

	int n, i, j;
	unsigned char a, b;


	assert(ncounts == ncol * ncol * N_ALPHA * N_ALPHA);
	memset(counts, 0, sizeof(int) * ncounts);

	for(n = 0; n < nrow; n++) {
		for(i = 0; i < ncol; i++) {
			a = msa[n * ncol + i];
			for(j = 0; j < ncol; j++) {
				b = msa[n * ncol + j];

				counts[((i * ncol + j) * N_ALPHA + a) * N_ALPHA + b]++;
			}
		}

	}

}


void msa_char_to_index(char* msa, int nrow, int ncol) {

	int amino_indices[29];
	int n, i;
	unsigned char c;

	// Make hash lookup table for amino acid characters to amino acid numbers
	// hash keys are the ASCII codes of the upper-case amino acids, modulo 29.
	// hash values are the amino acid numbers.
	//
	// aa   -  A  C  D  E  F  G  H  I  K  L  M  N  P  Q  R  S  T  V  W  Y
	// asc 45 65 67 68 69 70 71 72 73 75 76 77 78 80 81 82 83 84 86 87 89
	// mod 16  7  9 10 11 12 13 14 15 17 18 19 20 22 23 24 25 26 28  0  2
	for(c = 0; c < 29; c++) {
		amino_indices[c] = 0;
	}

	amino_indices[16] =  0;	// -
	amino_indices[ 7] =  1; // A
	amino_indices[ 9] =  2; // C
	amino_indices[10] =  3; // D
	amino_indices[11] =  4; // E
	amino_indices[12] =  5; // F
	amino_indices[13] =  6; // G
	amino_indices[14] =  7; // H
	amino_indices[15] =  8; // I
	amino_indices[17] =  9; // K
	amino_indices[18] = 10; // L
	amino_indices[19] = 11; // M
	amino_indices[20] = 12; // N
	amino_indices[22] = 13; // P
	amino_indices[23] = 14; // Q
	amino_indices[24] = 15; // R
	amino_indices[25] = 16; // S
	amino_indices[26] = 17; // T
	amino_indices[28] = 18; // V
	amino_indices[ 0] = 19; // W
	amino_indices[ 2] = 20; // Y


	for(n = 0; n < nrow; n++) {
		for(i = 0; i < ncol; i++) {
			msa[n * ncol + i] = amino_indices[ toupper(msa[n * ncol + i]) % 29 ];
		}
	}

}

