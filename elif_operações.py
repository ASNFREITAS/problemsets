#!/usr/bin/env python3
import sys

X = sys.argv[1] # pega o valor de X
X = int(X)

if X > 0:
	if X > 50:
		if X%3 ==0:
			print(X,'é positivo, maior que 50 e divisivel por 3')
		else:
			print(X,'é positivo, maior que 50 e não divisivel por 3')
	else:
		print(X,'é positivo e menor ou igual a 50')
elif X == 0 :
	print(X,'é 0')
else:
	print(X,'é negativo')

