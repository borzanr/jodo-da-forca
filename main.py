import random

nova_palavra = ""
letra = ""
mapa_palavra = []
indice_letra = 0
tamanho_palavra = 0
num_vidas = 5
palavra_completa = 0

def sortear_palavra():
    global nova_palavra
    palavra = ["banana","limao", "pera", "uva", "morango", "melao", "melancia", "abacaxi", "mexerica"]
    random.shuffle(palavra)
    nova_palavra = palavra[0]
    print(nova_palavra)
    
def montar_mapa_palavra():
    global mapa_palavra
    global nova_palavra
    global tamanho_palavra
    
    tamanho_palavra = len(nova_palavra)
   
    for caracter in range(0,tamanho_palavra):
        mapa_palavra.append("")
    
    print(mapa_palavra)
    
    
def perguntar_letra():
    global letra
    letra = input("Qual é a próxima letra?")
    print(f"A letra escolhida foi {letra}")
    
def verificar_letra():
    global tamanho_palavra
    global letra
    global nova_palavra
    global indice_letra
    
    tamanho_palavra = len(nova_palavra)
    indice_letra = 0

    for caracter in range(0,tamanho_palavra):
        if letra == nova_palavra[caracter]:
            indice_letra += 1
            mapa_palavra[caracter] = letra
    
    print(indice_letra)
    print(mapa_palavra)
    
def atualizar_forca():
    global indice_letra
    global num_vidas
    global palavra_completa
    
    if indice_letra == 0:
        num_vidas -= 1
    else:
        palavra_completa += indice_letra
    print(f"Número vidas: {num_vidas}")
    print(f"Palavra preenchida: {palavra_completa}")

def verifica_forca():
    if num_vidas == 0:
        print("Game Over, você se lascou!! Tente em uma próxima!")
    elif palavra_completa == tamanho_palavra:
        print("Parabéns, você acertou a palavra!! Fim de jogo!")

print("Bem vindo à forca!\n")
sortear_palavra()
montar_mapa_palavra()

while num_vidas > 0 and palavra_completa < tamanho_palavra:
    perguntar_letra()
    verificar_letra()
    atualizar_forca()
    verifica_forca()


    
