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