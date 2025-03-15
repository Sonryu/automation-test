import pygame   #importar a biblioteca

pygame.init()   #inicializar a biblioteca
pygame.joystick.init()  #inicializar o controle

#Verifica se há um controle conectado

if pygame.joystick.get_count() == 0: #verifica se tem pelo menos 1 controle conectado
    print("Nenhum controle conectado!")
    pygame.quit()
    exit()

# Pega o primeiro controle
controle = pygame.joystick.Joystick(0)
controle.init() #ativa o controle detectado

#loop para testar os analogicos
rodando = True

import time #NÃO É OBRIGATORIO, COLOQUEI APENAS PARA PODER LER OS VALORES ENTRE UM LOOP E OUTRO

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    eixo_x = controle.get_axis(0) #Analogico esquerdo - horizontal
    eixo_y = controle.get_axis(1) #Analogico esquerdo - vertical

    if abs(eixo_x) > 0.1:   #Só mostra o valor se e somente si os valores dos Eixos X forem maiores que a DEADZONE que esta definida em 0.1
        print(f'Eixo X: {eixo_x:.2f}') #limitando as casas decimais em 2 casa decimais usando '.:2f' 
    else:
        print('Eixo X: 0.0')

    if abs(eixo_y) > 0.1:   #Só mostra o valor se e somente si os valores dos Eixos Y forem maiores que a DEADZONE que esta definida em 0.1
        print(f'Eixo Y: {eixo_y:.2f}\n') #limitando as casas decimais em 2 casa decimais usando '.:2f' 
    else:
        print('Eixo Y: 0.0')

    #print(f"Eixo X: {eixo_x:.1f}, Eixo Y:{eixo_y:.1f}") #Mostra os valores no terminal
    time.sleep(0.8) #se comentar a TIME, comente isso tbm, coloquei um tempo em segundos para poder ler o que aparece no terminal

pygame.quit()