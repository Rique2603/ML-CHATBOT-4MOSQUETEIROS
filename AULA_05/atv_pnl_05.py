# ATIVIDADE 5 - Contador de Palavras
# Objetivo: Contar quantas palavras existem em um texto

texto = "machine learning é importante para inteligência artificial"

# Dividir o texto em palavras (tokenização simples)
palavras = texto.split()

# Contar quantas palavras existem
quantidade = len(palavras)

# Mostrar resultado
print("Número de palavras:", quantidade)