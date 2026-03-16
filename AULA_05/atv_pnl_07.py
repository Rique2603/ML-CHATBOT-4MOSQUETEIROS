# ATIVIDADE 7 - Classificador Simples de Intenção
# Objetivo: Detectar a intenção do usuário a partir de frases

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Conjunto de frases de treinamento
frases = [
    "quero comprar produto",
    "desejo fazer compra",
    "quero cancelar pedido",
    "cancelar minha compra",
    "qual horário funcionamento",
    "vocês abrem sábado"
]

# Intenções correspondentes
intencoes = [
    "comprar",
    "comprar",
    "cancelar",
    "cancelar",
    "horario",
    "horario"
]

# Criar vetorizador
vetorizador = CountVectorizer()

# Transformar frases em vetores
X = vetorizador.fit_transform(frases)

# Treinar modelo Naive Bayes
modelo = MultinomialNB()
modelo.fit(X, intencoes)

# Pedir frase do usuário
entrada = input("Digite sua mensagem: ")

# Transformar entrada em vetor
entrada_vetor = vetorizador.transform([entrada])

# Prever intenção
predicao = modelo.predict(entrada_vetor)

# Mostrar resultado
print("Intenção detectada:", predicao[0])