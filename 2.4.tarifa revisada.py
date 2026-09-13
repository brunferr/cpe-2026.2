TAXA_POR_KM = 0.50      #professor nessa questao eu pedi uma ajudinha do claude, nao vou mentir
TAXA_MINIMA = 30.0
LIMITE_DESCONTO = 300
PERCENTUAL_DESCONTO = 0.05

def calcular_tarifa(km):
    """Calcula a tarifa do aluguel com taxa mínima e desconto acima de 300 km."""
    tarifa = max(TAXA_MINIMA, km * TAXA_POR_KM)
    
    if km > LIMITE_DESCONTO:
        tarifa *= (1 - PERCENTUAL_DESCONTO)
        observacao = "Taxa mínima + 5% desconto" if km * TAXA_POR_KM < TAXA_MINIMA else "5% desconto aplicado"
    else:
        observacao = "Taxa mínima aplicada" if km * TAXA_POR_KM < TAXA_MINIMA else "Tarifa normal"
    
    return tarifa, observacao


testes = [0, 50, 150, 300]

print(f"{'Quilometragem':<15}{'Tarifa calculada':<20}{'Observação'}")
print("-" * 55)
for km in testes:
    tarifa, obs = calcular_tarifa(km)
    print(f"{km} km{'':<10}R$ {tarifa:.2f}{'':<10}{obs}")