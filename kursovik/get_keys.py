#генерация ключей
import random
from eratos import primes

def generate_prime():
	n = random.randint(3,100)
	p = primes(n)
	return p

def get_primitive_root(p):
	p = generate_prime()
	phi = p - 1
	nu = []
	for i in range(2,p):
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

#Первообразный корень от Лёши
def primitive_root(m):
    '''Gives a minimal prime root modulo m.

    m -- an integer
    m could be p^a or 2*p^a where p is a prime number and a is a positive integer. 

    >>> primitive_root(7)
    3
    >>> primitive_root(14)
    3

    '''
    t = euler_phi(m)
    lst = prime_divisors(t)
    for i in range(1, m):
        if is_coprime(i, m):
            for l in lst:
                if power_mod(i, t//l, m) == 1:
                    break
            else:
                return i


def get_keys():
	p = generate_prime()
	g = get_primitive_root(p)
	x = random.randint(1,p-1)
	y = g^x % p
	open_key = [g,p,y]
	close_key = x
	return (close_key, open_key)

#k = get_keys()
#print("Закрытый ключ: ",k[0],"\nОткрытый ключ: ", k[1])