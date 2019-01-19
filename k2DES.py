
import timeit
import itertools
import sys
import DES as des

start = timeit.default_timer()

#####gerar todas as chaves de l bits, em binário
def genPossibleKeys(l):

	possibleKeys=(''.join(x) for x in itertools.product('01', repeat=l))
	for x in possibleKeys:
		yield x


def findKeys(text,cipher,m1,c1,keylength):
	keys=genPossibleKeys(keylength)
	print("Depois de gerar keys:",timeit.default_timer()-start)

	dictEnc={}
	for i in keys:
		x1=des.DES(text,i,"Enc")
		#print("Depois fazer ", i, "DES Enc:",timeit.default_timer()-start)
		dictEnc[x1]=i
		#print("Depois preencher ", i, "Dict Enc:",timeit.default_timer()-start)
	
	print("Depois de preencher dicts:",timeit.default_timer()-start)
	candidates=[]
	keys=genPossibleKeys(keylength)
	for i in keys:
		x1=des.DES(cipher,i,"Dec")
		if x1 in dictEnc:
			candidates.append((dictEnc[x1],i))

	return candidates
	print("Depois de procurar candidatos:",timeit.default_timer()-start)

def check(l,message,cipher):
	l1=[]
	print(cipher)
	print(len(message))
	print(len(cipher))
	for a,b in l:
		m1=des.DES(message,a,"Dec")
		m2=des.DES(m1,b,"Dec")
		print(m2)
		if m2 ==cipher:
			l1.append((a,b)) 
	return l1

#####aux functions
def HextoBin(h):
	return bin(int(h, 16))[2:].zfill(64)

def BintoHex(b):
	return hex(int(b, 2))[2:]


def main():

    if str(sys.argv[1]) == '16': #29s
    	m=HextoBin('217430c48e3ab023')
    	c=HextoBin('783e3b789eb8f415')
    	m1=HextoBin('f0793f2aaee347c8')
    	c1=HextoBin('e7d6f26c1389f2e3')
    	print(findKeys(m,c,m1,c1,16),'Time: ', timeit.default_timer() - start)

    if str(sys.argv[1]) == '20': #482s
	    m=HextoBin('c19248fb642b5710')
	    c=HextoBin('8ba5d3a3a231db89')
	    m1=HextoBin('73cdb332c1737cb9')
	    c1=HextoBin('033e6056db3b2538')
	    print(findKeys(m,c,m1,c1,20),'Time: ', timeit.default_timer() - start)
    	#Chaves possíveis: [('fffffffffff91d3d', 'fffffffffff694ec'), ('fffffffffff91d3d', 'fffffffffff694ed'), ('fffffffffff91d3d', 'fffffffffff695ec'), ('fffffffffff91d3d', 'fffffffffff695ed'), ('fffffffffff91d3d', 'fffffffffff794ec'), ('fffffffffff91d3d', 'fffffffffff794ed'), ('fffffffffff91d3d', 'fffffffffff795ec'), ('fffffffffff91d3d', 'fffffffffff795ed')]

    if str(sys.argv[1]) == '24':
    	m=HextoBin('ae09a62a71e6fe3f')
    	c=HextoBin('915f2992ff699075')
    	m1=HextoBin('20b62c06243e6de9')
    	c1=HextoBin('f589dde349a78663')
    	print(findKeys(m,c,m1,c1,24),'Time: ', timeit.default_timer() - start)
		#Chaves possívels: [('ffffffffffc17975', 'ffffffffff3444d6'), ('ffffffffffc17975', 'ffffffffff3444d7'), ('ffffffffffc17975', 'ffffffffff3445d6'), ('ffffffffffc17975', 'ffffffffff3445d7'), ('ffffffffffc17975', 'ffffffffff3544d6'), ('ffffffffffc17975', 'ffffffffff3544d7'), ('ffffffffffc17975', 'ffffffffff3545d6'), ('ffffffffffc17975', 'ffffffffff3545d7')]

    if str(sys.argv[1]) == '28': 
    	print("ola")
    	m=HextoBin('f5915a9e3501f21e')
    	c=HextoBin('c7a64eadf5c57cd7')
    	m1=HextoBin('c42c48e9805d8fa9')
    	c1=HextoBin('d8bc4abfd70b8ba8')
    	print(findKeys(m,c,m1,c1,28),'Time: ', timeit.default_timer() - start)

if __name__ == "__main__":
    main()
