import edlib
import pysam as ps
import time




seq1 = "TCGGGGTAAGAAAAAAAAACCGGGGTACGTTAGATGCTAGGTTCATGAGGAGGGAAGGGCAGGGGGCCAGCAGGAGTGCTGTGGCCGTCCAGACGAGGCC"
seq2 = "TCGGGGTAAGAAAAAAAA"


print(edlib.align(seq1, seq2, mode='HW', task='path'))



