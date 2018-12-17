import random
import math


#Решето Эратосфена
def eratos(n):
	a = [0] * n
	for i in range(n):
		a[i] = i

	a[1] = 0
	m = 2
	while m < n:
		if a[m] != 0:
			j = m * 2
			while j < n:
				a[j] = 0
				j = j + m
		m += 1
	b = []
	for i in a:
		if a[i] != 0:
			b.append(a[i])
	del a
	return b[-1]

#Решето Аткина
def atkins(limit):
	primes = [False] * limit
	sqrt_limit = int( math.sqrt( limit ) )

	x_limit = int( math.sqrt( ( limit + 1 ) / 2 ) )
	for x in range( 1, x_limit ):
		xx = x*x

		for y in range( 1, sqrt_limit ):
			yy = y*y
			n = 3*xx + yy
			if n < limit and n%12 == 7:
				primes[n] = not primes[n]
			n += xx
			if n < limit and n%12 in (1,5):
				primes[n] = not primes[n]
			if x > y:
				n -= xx + 2*yy
				if n < limit and n%12 == 11:
					primes[n] = not primes[n]

	for n in range(5,limit):
		if primes[n]:
			for k in range(n*n, limit, n*n):
				primes[k] = False
	l = list(filter(primes.__getitem__, range(5, limit)))

	return l[-1]

#Генерация случайного простого числа
def generate_prime_eratos():
	n = random.randint(1000,100000)
	p = eratos(n)
	return p

def generate_prime_atkin():
	n = random.randint(1000,10000)
	p = atkins(n)
	return p

#Первообразный корень очень медленно
def get_primitive_root(p):
	phi = p - 1 #Так можно потому что по условию схемы Эль-Гамаля p всегда простое
	nu = []
	for i in range(int((p-1)/2),p):
		if pow(i,phi,p) == 1:
			lst = [1]
			for j in range(1,phi):
				lst.append(pow(i,j,p))
			lst = list(set(lst))
			if lst == list(range(1,p)):
				nu.append(i)
	i = random.randint(0,len(nu)-1)
	g =nu [i]
	return g

#Первообразный корень улучшенный
def get_primitive_root2(p):
	phi = p - 1#Так можно потому что по условию схемы Эль-Гамаля p всегда простое
	n = random.randint(1,(p-1)/2)
	k = 1
	r = 0
	for i in range(int((p-1)/2),p):
		if pow(i,phi,p) == 1:
			lst = [1]
			for j in range(1,phi):
				lst.append(pow(i,j,p))
			lst = list(set(lst))
			if lst == list(range(1,p)):
				r = i
			if k == n:
				break
			else:
				k = k + 1
	return r

#Генерация ключей
def get_keys():
	p = generate_prime_atkin()
	g = get_primitive_root2(p)
	x = random.randint(1,p-1)
	y = pow(g,x,p)
	open_key = [g,p,y]
	close_key = x
	return [close_key, open_key]

#Шифровани числа
def encrypt(message,open_k):
	p = open_k[1]
	g = open_k[0]
	y = open_k[2]
	k = random.randint(1, p)
	cipher = []
	#message = 764
	a = pow(g,k,p)
	b = ((y^k)* message)% p
	cipher.append(a)
	cipher.append(b)
	y = 0
	k = 0
	return (cipher, open_k, close_k)

#Дешифрование числа
def decipher(cipher,open_key,close_key):
	a = cipher[0]
	b = cipher[1]
	m = int(b / (a^int(close_key) % int(open_key[1])))
	return(m)

#Шифрование списка чисел
def encrypt_list(message,open_k,close_k):
	p = open_k[1]
	g = open_k[0]
	y = open_k[2]
	k = random.randint(1, p)
	cipher = []
	a = g^k % p
	b = y^k % p
	for i in message:
		r = []
		c = b* i
		r.append(a)
		r.append(c)
		cipher.append(r)
	y = 0
	k = 0
	return (cipher, open_k, close_k)

#Дешифрование списка чисел
def decipher_list(cipher,open_key,close_key):
	dem = []
	for i in cipher:
		a = i[0]
		b = i[1]
		m = int(b / (a^int(close_key) % int(open_key[1])))
		dem.append(m)
	return(dem)

#Шифрование строки
def encrypt_text(message,open_k):
	m = []
	for i in message:
		m.append(ord(i))
	p = open_k[1]
	g = open_k[0]
	y = open_k[2]
	k = random.randint(1, p)
	cipher = []
	a = g^k % p
	b = y^k % p
	for i in m:
		r = []
		c = b* i
		r.append(a)
		r.append(c)
		cipher.append(r)
	y = 0
	k = 0
	return cipher

#Дешифрование строки
def decipher_text(cipher,open_key,close_key):
	dem = []
	decipherment = ""
	for i in cipher:
		a = i[0]
		b = i[1]
		m = int(b / (a^int(close_key) % int(open_key[1])))
		dem.append(m)
	for i in dem:
		decipherment = decipherment + chr(i)
	return decipherment

#Преобразование строки в список
def from_str2lst(st):
	m = []
	for i in range(len(st)-1):
		if st[i] == "[":
			a = 0
			c = []
		if st[i] >= "0" and st[i] <= "9":
			a = a*10 + int(st[i])
			if st[i + 1] == ",":
				c.append(a)
				a = 0
			if st[i + 1] == "]":
				c.append(a)
				m.append(c)
	return m[:-1]

#Шифрование из текстового файла в текстовый файл
def encrypt_text_from_file2newfile(file,newfile,open_k):
	f = open(file, 'r')
	c = open(newfile, 'a')

	for line in f:
		l = encrypt_text(line,open_k)
		c.write(str(l[:-1]) + "\n")

	c.close()
	f.close()
	return

#Дешифрование из текстового файла в текстовый файл
def decipher_from_file2newfile(file,newfile,open_key,close_key):
	f = open(file, 'r')
	c = open(newfile, 'a')
	for l in f:
		a = from_str2lst(l)
		c.write(decipher_text(a,open_key,close_key) + "\n")
	f.close()
	c.close()

def str_open_key_2list(string):
	b = string.split(',')
	c1 = int(b[0][1:])
	c2 = int(b[1])
	c3 = int(b[2][:-1])
	return [c1,c2,c3]