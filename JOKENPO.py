def valida_int(pergunta, min, max): # valida se o valor digitado é um inteiro entre min e max
  x = int(input(pergunta))  # PERGUNTA AO USUÁRIO
  while x < min or x > max: # FUNÇÃO QUE VALIDA SE O VALOR DIGITADO ESTÁ ENTRE MIN E MAX
        print(f'Valor inválido! Digite um valor entre {min} e {max}.') # MENSAGEM DE ERRO
        x = int(input(pergunta)) # PERGUNTA AO USUÁRIO NOVAMENTE
  return x # RETORNA O VALOR DIGITADO PELO USUÁRIO

def vencedor(j1, j2): # PARAMENTROS: JOGADOR 1 E JOGADOR 2, DEF CRIA UMA FUNÇÃO QUE DETERMINA O VENCEDOR DO JOGO
    if j1 == j2: # IF PARA VERIFICAR SE OS JOGADORES EMPATARAM 
        print('Empate!') # print empate 
        return 'empate' # retorna do inicio da função vencedor
    elif (j1 == 1 and j2 == 3) or (j1 == 2 and j2 == 1) or (j1 == 3 and j2 == 2): # elif PARA VERIFICAR SE O JOGADOR 1 VENCEU
        print('Jogador 1 venceu!')     #print jogador 1 venceu
        return 'jogador 1' # retorna do inicio da função vencedor
    else: # else PARA VERIFICAR SE O JOGADOR 2 VENCEU
        print('Jogador 2 venceu!') # print jogador 2 venceu
        return 'jogador 2' # retorna do inicio da função vencedor

#programa principal 
print('jokenpo') 
print('1 - pedra')
print('2 - papel')
print('3 - tesoura')

jogadas = [] # lista para armazenar as jogadas dos jogadores
resultados = [] #   lista para armazenar os resultados das jogadas

from mimetypes import init
import random #     importa a biblioteca random para gerar números aleatórios

while True:  #              loop infinito para o jogo
    j1 = valida_int('escolha sua jogada:', 0, 3)    # escolha da jogada do jogador 1, usando a função valida_int para garantir que o valor digitado seja válido
    if not j1: # se o jogador 1 digitar 0, o jogo termina
        break #  encerra o jogo 

    j2 = random.randint(1, 3)   # escolha da jogada do jogador 2, usando a função randint da biblioteca random para gerar um número aleatório entre 1 e 3
    jogadas.append([j1, j2])    # adiciona a jogada dos jogadores na lista de jogadas
    resultado = vencedor(j1, j2) # chama a função vencedor para determinar o resultado da jogada e armazena o resultado na variável resultado
    resultados.append(resultado) # adiciona o resultado da jogada na lista de resultados

print('Jogadas realizadas:')    # PRINT JOGADAS REALIZADAS
for i, jogada in enumerate(jogadas): # FOR IRA CADA JOGADA REALIZADA, ENUMERANDO AS JOGADAS PARA MOSTRAR O NÚMERO DA RODADA
    print(f'Rodada {i+1}: Jogador 1 jogou {jogada[0]}, Jogador 2 jogou {jogada[1]} - Resultado: {resultados[i]}') # print mostrando o número da rodada
                                                                                                                # a jogada de cada jogador e o resultado da rodada

                                                                                                     