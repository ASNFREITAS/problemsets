#!/usr/bin/env python3
import sys

dna = 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
Codon = sys.argv[1] # get first command line parameter
if Codon in dna:
  message = 'contem'
  print(message)
else:
  message ='não contem'
  print(message)
