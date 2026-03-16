# ATIVIDADE 6 - Frequência de Palavras
# Objetivo: Contar a frequência de cada palavra em um texto

from collections import Counter

texto = "chatbot chatbot inteligência artificial chatbot aprendizado"

# Transformar texto em lista de palavras (tokenização simples)
palavras = texto.split()

# Calcular frequência de cada palavra
frequencia = Counter(palavras)

# Mostrar resultado
print(frequencia)