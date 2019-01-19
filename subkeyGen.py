#gerar 16 sub-chaves de tamanho 48
def GenerateSubkeys(k):
	firstperm=InitialPermutation(k) #permutação inicial das chaves
	l,r=DivideKey(firstperm) #dividir chave principal em duas com metade do tamanho
	key_pairs=[]
	key_pairs=InitialShift(l,r) #fazer o shift inicial
	keys=[]
	for a,b in key_pairs:
		keys.append(FinalPermutation(a+b)) #fazer a permutação final a cada junção de cada pares de chaves
	return keys 

def DivideKey(k):#dividir chave em duas metades
	left, right = k[:len(k)/2], k[len(k)/2:]
	return(left, right)

def InitialPermutation(k): #permutação inicial segundo a tabela 
	kl=StringtoList(k)
	kp=[]
	pertable=[57, 49, 41,   33,    25,    17,    9,
               1,   58,    50,   42,    34,    26,   18,
              10,    2,    59,   51,    43,    35,   27,
              19,   11,     3,   60,    52,    44,   36,
              63,   55,    47,   39,    31,    23,   15,
               7,   62,    54,   46,    38,    30,  22,
              14,    6,    61,   53,    45,    37,   29,
              21,   13,     5,   28,    20,    12,    4]
	for i in range (0,len(pertable)):
		kp.append(kl[pertable[i]-1])
	skp=''.join(kp)
	return(skp)

def FinalPermutation(k): #permutação final segundo a tabela
	kl=StringtoList(k)
	kp=[]
	pertable=[14,    17,   11,    24,     1,    5,
                  3,    28,   15,     6,    21,   10,
                 23,    19,   12,     4,    26,    8,
                 16,     7,   27,    20,    13,    2,
                 41,    52,   31,    37,    47,   55,
                 30,    40,   51,    45,    33,  48,
                 44,   49,   39,    56,    34,  53,
                 46,    42,   50,   36,    29,  32]       
	for i in range (0,len(pertable)):
		kp.append(kl[pertable[i]-1])
	skp=''.join(kp)
	return(skp)

def InitialShift(c,d): #fazer shift a cada metade de chave para gerar as 16 subchaves
	pairs=[(c,d)] #por o primeiro par na lista
	newc=ListtoString(list(c))
	newd=ListtoString(list(d))
	for i in range (0,16): #fazer 16 vezes
		#aplicar left shift ao valor anterior na lista de pares
		if(i==0 or i==1 or i==8 or i == 15): #se estivermos numa destas rondas aplciar o left shit so uma vez
			newc=LeftShift(list(newc))
			newd=LeftShift(list(newd))
		else: #se estivermos em todas as outras rondas aplciar o left shift duas vez
			newc=LeftShift(list(LeftShift(list(newc))))
			newd=LeftShift(list(LeftShift(list(newd))))
		pairs.append((newc,newd)) #acrescentar resultado a lista de pares		
	return pairs

def LeftShift(l): #fazer left shift a uma lista 
	length=len(l)
	l0=l[0] #guardar valor inicial
	for i in range (0,length):
		if(i==length-1):
			l[i]=l0 #se estivermos no ultimo valor da lista, esse passa a ser o inicial
		else:
			l[i]=l[i+1] #se não, o valor na posição atual passa a ser valor que estava na posição a seguir
	return(ListtoString(l))

def StringtoList(s):
	l=[]
	for c in s:
		l.append(c)
	return l

def ListtoString(l):
	s=""
	for i in range (0,len(l)):
		s=s+str(l[i])
	return s

#print(GenerateSubkeys("0001001100110100010101110111100110011011101111001101111111110001"))



#####################################para testar com exemplo
def equalsString(s1,s2):
	if s1 == s2:
		return True
	else:
		return False

def checkKeys(k1,k2):
	l=[]
	for i in range (0,len(k1)):
		l.append(equalsString(k1[i],k2[i]))
	return l

def deleteSpace(s):
	new=[]
	for i in s:
	    j = i.replace(' ','')
	    new.append(j)
	return new

stringList=['000110110000001011101111111111000111000001110010', '011110011010111011011001110110111100100111100101', '010101011111110010001010010000101100111110011001', '011100101010110111010110110110110011010100011101', '011111001110110000000111111010110101001110101000', '011000111010010100111110010100000111101100101111', '111011001000010010110111111101100001100010111100', '111101111000101000111010110000010011101111111011', '111000001101101111101011111011011110011110000001', '101100011111001101000111101110100100011001001111', '001000010101111111010011110111101101001110000110', '011101010111000111110101100101000110011111101001', '100101111100010111010001111110101011101001000001', '010111110100001110110111111100101110011100111010', '101111111001000110001101001111010011111100001010', '110010110011110110001011000011100001011111110101']
#print(checkKeys(stringList,GenerateSubkeys("0001001100110100010101110111100110011011101111001101111111110001")))
#print(GenerateSubkeys("0001001100110100010101110111100110011011101111001101111111110001"))
######################################



