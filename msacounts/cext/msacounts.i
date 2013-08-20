%module msacounts
%{
#define SWIG_FILE_WITH_INIT
#include "msacounts.h"
%}

%include "numpy.i"
%init %{
import_array();
%}

%apply (unsigned char* INPLACE_ARRAY2, int DIM1, int DIM2) {(unsigned char* msa, int nrow, int ncol)};
%apply (int* ARGOUT_ARRAY1, int DIM1) {(int* counts, int ncounts)};

%include "msacounts.h"
