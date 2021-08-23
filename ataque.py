import hashlib
from lagrange_matlab2 import lagrange
from lagrange_matlab import lagrange_poly_iter
import itertools
#from scipy.interpolate import lagrange
from lagrange_matlab2 import lagrange

def readVault(textFile):  # lee el vault capturado en un archivo de texto
    vault = []
    with open(textFile) as file:
        vault = [tuple(map(int, line.split(' '))) for line in file]
    return vault

N = 8 # Grado del polinomio original
#Genuinos = [(27018, 39554),(20891, 49661),(42425, 26105),(15804, 21327),(21004, 49378),(53768, 17152),(9855, 59927),(30186, 42482),(47639, 31242),(29507, 18676),(7727, 35952),(50790, 64406),(39479, 63594),(27327, 25035),(18047, 1284),(37527, 53537),(32410, 10681),(24290, 22945),(36596, 25062),(4898, 13405),(14098, 18283),(20339, 64551),(58952, 38998),(59059, 18972),(59266, 6786)]

xG = [20891, 20339, 4898, 59059, 59266, 39479, 18047, 9855, 29507] # Puntos genuinos x
yG = [49661, 64551, 13405, 18972, 6786, 63594, 1284, 59927, 18676] # Puntos genuinos y

F = lagrange_poly_iter(xG, yG, N+1, N+1) # Coeficientes del polinomio origianl
hF = hashlib.sha256(F.__str__().encode('utf-8')).hexdigest() # valor hash del polinomio original (Este valor es conocido por el atacante)

r = readVault("vault/Vault.txt")
#print(F)
print("Iniciando ataque de fuerza bruta")

for k in range(2, 9): # calcula el polinomio de lagrange con k + 1 puntos tomados del vault con k = 2, 3, 4, 5, 6, 7, 8
    print("Probando combinaciones para k=", k)

    kCombinations = itertools.combinations(r, k + 1)
    for subset in kCombinations:
        xi = []
        fi = []
        for t in subset:
            aux = list(t)
            xi.append(aux[0])
            fi.append(aux[1])
        #print("xi = ", xi)
        #print("fi = ", fi)
        fa = lagrange_poly_iter(xi, fi, k+1, k+1)
        #fa = lagrange(xi, fi)
        hfa = hashlib.sha256(fa.__str__().encode('utf-8')).hexdigest()

        print(fa)
        if(hfa == hF):
            print("Se encontro el polinomio correcto:")
            print(fa)
            exit()