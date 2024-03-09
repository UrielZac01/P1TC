from itertools import product

def potencia_alfabeto(sigma, k):
    if k < 0:
        return "El valor de k debe ser no negativo."

    sigma_k = [''.join(p) for p in product(sigma, repeat=k)]
    return sigma_k

if __name__ == "__main__":
    sigma_usuario = input("Ingrese su alfabeto Σ separado por comas (por ejemplo, A,B,1,2,?,#): ").split(',')
    k_usuario = int(input("Ingrese el valor de k (no negativo): "))

    simbolos_aceptados = set(sigma_usuario)

    resultado_potencia = potencia_alfabeto(simbolos_aceptados, k_usuario)
    print(f"Σ^{k_usuario}: {resultado_potencia}")