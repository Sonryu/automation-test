import pygame

pygame.init()

#inicializando o controle
pygame.joystick.init()
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Controle detectado: {joystick.get_name()}")
else: 
    print("Nenhum controle detectado!")

#configurando janela:
WIDTH, HEIGTH = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("Leitura de MNK e PS4 Roller")

#Loop principal
done = False

while not done:
    screen.fill((0, 0, 0)) #limpa a tela com preto

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        elif event.type == pygame.KEYDOWN: #Quando uma tecla for pressionada
            print(f"Tecla pressionada: {pygame.key.name(event.key)}")

        elif event.type == pygame.MOUSEBUTTONDOWN: #Quando o mouse for pressionado
            print(f"Mouse pressionado: Botão {event.button} em {event.pos}")
        
        elif event.type == pygame.JOYBUTTONDOWN: #quando um botão do controle for pressionado
            print(f"Botão do controle pressionado: {event.button}")

        elif event.type == pygame.JOYAXISMOTION: #Quando um eico do joystick se mover
            print(f"Eixo {event.axis} movido para {event.value}")

    pygame.display.flip() #atualiza a tela

pygame.quit()