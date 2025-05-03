import pygame

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("Nenhum controle detectado")
    exit()

controle = pygame.joystick.Joystick(0)
controle.init()

LARGURA, ALTURA = 500, 500
tela = pygame.display.set_mode((ALTURA, LARGURA))

BRANCO = (255, 255, 255)
AZUL = (0,0, 255)

pos_x, pos_y = LARGURA // 2, ALTURA //2

RAIO = 20

velocidade = 2 #velocidade de movimento

#loop incial
RODANDO = True

while RODANDO:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            RODANDO = False
    eixo_x = controle.get_axis(0) #Esquerda-Direita
    eixo_y = controle.get_axis(1) #Cima-Baixo

    #ajuste de movimentação
    DEADZONE = 0.1 #Para retirar valores indesejados.

    if abs(eixo_x) > DEADZONE: #Se for detectado movimento dentro do eixo X, o circulo da animação vai se mover em funcao do X
        pos_x += int(eixo_x * velocidade)
    else: pos_x = int((eixo_x * velocidade) + (LARGURA/2)) #Se o analogico for solto, o circuo voltara para o centro da tela, que nesse caso, o X dele é a metade do tamanho da janela

    if abs(eixo_y) > DEADZONE: #Se for detectado movimento dentro do eixo Y, o circulo da animação vai se mover em funcao do Y
        pos_y += int(eixo_y * velocidade)
    else: pos_y = int((eixo_y * velocidade) + (ALTURA/2)) #Se o analogico for solto, o circuo voltara para o centro da tela, que nesse caso, o Y dele é a metade do tamanho da janela
 
    pos_x = max(RAIO, min(LARGURA - RAIO, pos_x))
    pos_y = max(RAIO, min(ALTURA - RAIO, pos_y))

    #desenhando na tela
    tela.fill(BRANCO)
    pygame.draw.circle(tela, AZUL, (pos_x, pos_y), RAIO)
    pygame.display.flip()

pygame.quit()