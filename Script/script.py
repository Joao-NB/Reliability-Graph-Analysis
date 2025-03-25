import os
import numpy as np
import matplotlib.pyplot as plt

# Caminho da pasta "Image"
image_dir = os.path.join("..", "Image")

# Criar diretório "Image" se não existir
if not os.path.exists(image_dir):
    os.makedirs(image_dir)

# Valor fixo para o cálculo
VALOR_FIXO = 10  

# Solicitar dois valores ao usuário
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

# Realizar o cálculo
resultado = (valor1 + valor2) * VALOR_FIXO

# Exibir o resultado no terminal
print(f"\nO resultado da conta ({valor1} + {valor2}) * {VALOR_FIXO} é: {resultado}")

# Criar um intervalo de tempo proporcional ao resultado
tempo = np.linspace(0, resultado, 300)

# Função de confiabilidade
def confiabilidade(t, mtbf):
    return np.exp(-t / mtbf)

# Calcular a confiabilidade ao longo do tempo usando o resultado como MTBF
R_t = confiabilidade(tempo, resultado)

# Criar o gráfico
plt.figure(figsize=(8, 5))
plt.plot(tempo, R_t, label=f'MTBF = {resultado}', color='blue')

# Adicionar rótulos e título
plt.xlabel("Tempo")
plt.ylabel("Confiabilidade R(t)")
plt.title("Confiabilidade do Sistema ao Longo do Tempo")

# Adicionar grade e legenda
plt.grid()
plt.legend()

# Caminho completo para salvar o gráfico na pasta correta
caminho_arquivo = os.path.join(image_dir, "variacao_de_tempo_em_mtbf.png")
plt.savefig(caminho_arquivo)

# Exibir o gráfico
plt.show()

print(f"Gráfico salvo em '{caminho_arquivo}'.")
