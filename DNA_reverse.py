#!/usr/bin/env python3


# importing the module
import ast

# reading the data from the file
file_object = open('Python_06.seq.txt', 'r') 
f = open('Python_06.seq.dicionario.txt', 'x')


for line in file_object:      # adicionando  ":" entre a key e o dna para poder transformar o txt em dict
    line = line.replace("\t",":")
    f.write(line)
 
file_object.close()
f.close()
d ={}
f = open('Python_06.seq.dicionario.txt', 'r')


for line in f.readlines():        # usando for e linesplit separar o codigo e a sequencia em dicionario
    codigo,sequencia = line.split(":")
    d[codigo] = str(sequencia)

for codigo in d:
    seq = d[codigo]
    seq = seq.replace("A","M")
    seq = seq.replace("T","A")
    seq = seq.replace("M","T")
    seq = seq.replace("G","M")
    seq = seq.replace("C","G")
    seq = seq.replace("M","C")
    print(seq)


