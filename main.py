# variaveis de estado
tentativas = 3 
pontos = 0

#pergunta
pergunta = 'Quantos lados tem um triângulo?'

while tentativas > 0:
    resposta = int(input(pergunta))
    
    if resposta == 3:
        print("Certa resosta")
        pontos = pontos + 1
        print (f'pontuação: {pontos}.')
        break
    else:
        print ('Errou')
        tentativas = tentativas - 1
        print (f'{tentativas} Tentativas, tenta de novo' )
