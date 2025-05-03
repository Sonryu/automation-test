import pygame   #importando a biblioteca

pygame.init() #ativando

ALTURA, LARGURA = 500, 500  #definindo tamanho de tela

tela = pygame.display.set_mode((ALTURA, LARGURA)) #criando a tela
pygame.display.set_caption("Bolinha")   #definindo nome da tela

#cor e posição inicial:
BRANCO = (255, 255, 255)    #Cor
AZUL = (0, 0, 255)  #Cor

posicao_x, posicao_y = LARGURA // 2, ALTURA // 2    #posição
raio = 20   #tamanho da bolinha

#Loop principal

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    #Limpa a tela
    tela.fill(BRANCO)

    #Desenha a bolinha:
    pygame.draw.circle(tela, AZUL, (posicao_x, posicao_y), raio)

    #atualiza a tela
    pygame.display.flip()

pygame.quit


