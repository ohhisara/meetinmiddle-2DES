import subkeyGen
import DES_tables as tables

#####DES
def DES(m,k,action):
	k=BitPadding(k) #por padding na chave -64 bits
	firstperm=Permutation(tables.IP,m) #permutação inicial na mensagem recebida
	l,r=SplitHalf(firstperm) #dividir mensagem permutada em duas metades
	keys=subkeyGen.GenerateSubkeys(k) #gerar 16 sub-chaves para usar em cada ronda
	res=Rounds(l,r,keys,action) #resultado de todas as rondas (rs[16]ls[16])
	result=Permutation(tables.FP,res) #permutar resultado com a tabela final
	return (result)

def Rounds(l,r,keys,action):
	ls,rs=[l],[r] #por nas listas valor inicial de l e r
	
	for i in range (1,17): #cada ronda
		if(action=="Enc"): #se estiver a cifrar, aplica as chaves por ordem crescente
			a=ls[i-1]
			ls.append(rs[i-1]) #ls[i] = rs[i-1]
			b=F_Function(rs[i-1],keys[i])
			c=xor(a,b).zfill(32)
			rs.append(c) #rs[1] = xor(ls[i-1],F(rs[i-1], chave da ronda))
			
		elif(action=="Dec"): #se estiver a decifrar, aplica as chaves por ordem decrescente
			a=ls[i-1]
			ls.append(rs[i-1])#ls[i] = rs[i-1]
			b=F_Function(rs[i-1],keys[17-i])
			c=xor(a,b).zfill(32)
			rs.append(c) #rs[1] = xor(ls[i-1],F(rs[i-1], chave da ronda))
			
		else:
			return "Algo se passa"
	return (ListtoString([rs[16],ls[16]])) #retornar o resultado da ultima ronda 

def F_Function(r,k): 
	expansion=Permutation(tables.e_table,r) #expandir r segundo a tabela de expansão
	xored=(xor(k,expansion)).zfill(48) #fazer xor da expansao com a chave
	blocks=SplitN(xored,6) #dividir resultado do xor em 8 blocos de 6 bits
	res=[]
	sboxes=tables.s_boxes
	for i in range(0,8): #por cada bloco
		res.append(Sboxes(blocks[i],sboxes[i])) #aplicar a função sboxes a cada block com a sbox correspondente
	result=''.join(res) #resultado é a junção de todas as aplicações das sboxes
	resultlist=StringtoList(result) #tranformar numa lista
	return(Permutation(tables.p_sboxes,resultlist)) #retornar o resultado permutado pela tabela a aplicar depois das sboxes

def Sboxes(b,s):
	block=StringtoList(b) 
	bini=ListtoString([block[0],block[5]]) #ir buscar valores que estao na posição 0 e 5 do bloco, junção dá um valor em binário
	binj=ListtoString([block[1],block[2],block[3],block[4]]) #ir buscar valores que estao na posição 1,2,3,4 do bloco, junção dá um valor em binário
	i=int(bini,2) #descobrir o primeiro valor em inteiro
	j=int(binj,2) #descobrir o segundo valor em inteiro
	res=bin(s[i][j])[2:].zfill(4) #procurar que valor se encontra na posição i,j da sbox recebida
	return res #retornar valor em binário

#####permutations
def Permutation(table,p): #implementação de permutação
	l=StringtoList(p)
	pp=[]
	for i in range (0,len(table)):
		pp.append(l[table[i]-1])
	spp=''.join(pp)
	return(spp)

#####aux functions
def SplitHalf(k): #dividir em dois
	left, right = k[:len(k)/2], k[len(k)/2:]
	return(left, right)

def SplitN(k,n): #didvidir k em blocos de n tamanho
	return [k[i:i+n] for i in range(0, len(k), n) ]

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



def BitPadding(b): #adicionar padding até aos 64 bits
	l=len(b)
	newbin=b
	if(l==64):
		return b
	else:
		while ((64-len(newbin))!=0) :
			newbin="1"+newbin
		return newbin

def xor(b1,b2): #fazer xor de 2 numeros binários
	x=bin(int(b1,2) ^ int(b2,2))[2:]
	return x