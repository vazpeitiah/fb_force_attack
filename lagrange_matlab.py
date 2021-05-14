def Div_mod(q, a, b): # (a/b) mod q
  for i in np.arange(1, b):
    y = ( q * i + a) / b
    if y == round(y):
      return y

def lagrange_poly(xi, fi, k):
  q = math.pow(2, 16) + 1
  signo = math.pow(-1, k)

  numerador = np.ones(k + 1, dtype = np.float64) 
  for i in range(k + 1):
    for j in range(k + 1):
      if(i != j):
        numerador[i] = (numerador[i] * xi[j]) % q
    numerador[i] = (numerador[i] * fi[j]) % q
  
  denominador = np.ones(k + 1, dtype = np.float64) 
  for i in range(k + 1):
    for j in range(k + 1):
      if(i != j):
        sub = (xi[i] - xi[j]) % q
        denominador[i] = (denominador[i] * sub) % q

  s = 0
  part = np.zeros(k + 1, dtype=np.float64) 
  for i in range(k + 1):
    part[i] = Div_mod(q, numerador[i], denominador[i])
    s = (s + part[i]) % q
  s = (signo * s) % q
  return s

def lagrange_poly_iter(xi, fi, k):
  q = math.pow(2, 16) + 1
  s = np.zeros(k + 1, dtype = int) 
  s[0] = lagrange_poly(xi, fi, k)

  gi = np.array(fi)
  
  for t in range(1, k+1):
    for i in range(k + 1):
      print(gi)
      print(s)
      gi[i] = Div_mod(q, gi[i]-s[t-1] % q, xi[i])
    s[t] = lagrange_poly(gi, xi, k-t)
  return s