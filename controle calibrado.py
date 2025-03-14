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
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    eixo_x = controle.get_axis(0) #Analogico esquerdo - horizontal
    eixo_y = controle.get_axis(1) #Analogico esquerdo - vertical

    print(f"Eixo X: {eixo_x:.1f}, Eixo Y:{eixo_y:.1f}") #Mostra os valores no terminal

pygame.quit()