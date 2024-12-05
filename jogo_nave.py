import pygame
from random import randint

pygame.init()

janela = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  
pygame.display.set_caption('Primeiro Jogo')

imagem_fundo = pygame.image.load(r'C:\Users\User\Desktop\jogo\space bg game.png')
nave_player = pygame.image.load(r'C:\Users\User\Desktop\jogo\sprite_nave_pequena.png')
nave_inimiga = pygame.image.load(r'C:\Users\User\Desktop\jogo\nave_inimiga_pequena.png')
missil_atirado = pygame.image.load(r'C:\Users\User\Desktop\jogo\pode_não-Photoroom.png')

largura_tela = janela.get_width()
altura_tela = janela.get_height()

imagem_fundo = pygame.transform.scale(imagem_fundo, (largura_tela, altura_tela))
nave_player = pygame.transform.scale(nave_player, (100, 100))  
nave_inimiga = pygame.transform.scale(nave_inimiga, (100, 100))  
missil_atirado = pygame.transform.scale(missil_atirado, (60, 40))  

pos_x_player = largura_tela // 2 - nave_player.get_width() // 2
pos_y_player = altura_tela - 100
vel_player = 10

misseis_jogador = []
misseis_inimigo = []
vel_missil = 7

pontuacao = 0
jogo_ativo = True

def tela_final(janela, pontuacao):
    font = pygame.font.Font(None, 74)
    texto_final = font.render('Você Perdeu!', True, (255, 0, 0))
    texto_pontuacao = font.render(f'Pontuação: {pontuacao}', True, (255, 255, 255))
    
    font_tentar_novamente = pygame.font.Font(None, 36)  
    texto_tentar_novamente = font_tentar_novamente.render('Tentar Novamente', True, (255, 255, 255))
    
    button_rect = pygame.Rect(largura_tela // 2 - 110, altura_tela // 2 + 50, 220, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):  
                    return  

        janela.fill((0, 0, 0))  
        janela.blit(texto_final, (largura_tela // 2 - texto_final.get_width() // 2, 200))
        janela.blit(texto_pontuacao, (largura_tela // 2 - texto_pontuacao.get_width() // 2, 300))
        
        pygame.draw.rect(janela, (0, 255, 0), button_rect)  
        janela.blit(texto_tentar_novamente, 
                    (button_rect.x + (button_rect.width - texto_tentar_novamente.get_width()) // 2, 
                     button_rect.y + (button_rect.height - texto_tentar_novamente.get_height()) // 2))

        pygame.display.update()

def tela_pausa(janela):
    font = pygame.font.Font(None, 74)
    texto_pausa = font.render('PAUSADO', True, (255, 0, 0))
    font_tentar_novamente = pygame.font.Font(None, 36)
    texto_continuar = font_tentar_novamente.render('Pressione P para continuar', True, (255, 255, 255))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  
                    return  

        janela.fill((0, 0, 0))  
        janela.blit(texto_pausa, (largura_tela // 2 - texto_pausa.get_width() // 2, altura_tela // 2 - 50))
        janela.blit(texto_continuar, (largura_tela // 2 - texto_continuar.get_width() // 2, altura_tela // 2 + 10))
        pygame.display.update()

def tela_inicio(janela):
    font = pygame.font.Font(None, 74)
    texto_inicio = font.render('Aperte SPACE para iniciar', True, (255, 255, 255))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  
                    return 

        janela.fill((0, 0, 0))  
        janela.blit(texto_inicio, (largura_tela // 2 - texto_inicio.get_width() // 2, altura_tela // 2 - 50))
        pygame.display.update()

loop = True
while loop:
    tela_inicio(janela)

    pos_x_player = largura_tela // 2 - nave_player.get_width() // 2
    pos_y_player = altura_tela - 100
    pontuacao = 0  
    misseis_jogador.clear()  
    misseis_inimigo.clear() 
    jogo_ativo = True  

    pos_x_inimigo = randint(0, largura_tela - nave_inimiga.get_width())
    pos_y_inimigo = 50
    vel_inimigo = 6
    contador_disparo_inimigo = 0
    intervalo_disparo_inimigo = 40  
    intervalo_disparo_minimo = 10  

    tempo_ultimo_disparo_jogador = 0
    intervalo_disparo_jogador = 350  

    while jogo_ativo:  
        tempo_atual = pygame.time.get_ticks()  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                jogo_ativo = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and (tempo_atual - tempo_ultimo_disparo_jogador >= intervalo_disparo_jogador):  
                    misseis_jogador.append([pos_x_player + 45, pos_y_player])  
                    tempo_ultimo_disparo_jogador = tempo_atual  
                if event.key == pygame.K_ESCAPE:  
                    jogo_ativo = False  
                if event.key == pygame.K_p: 
                    tela_pausa(janela)  

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP]:
            pos_y_player -= vel_player
        if teclas[pygame.K_DOWN]:
            pos_y_player += vel_player
        if teclas[pygame.K_LEFT]:
            pos_x_player -= vel_player
        if teclas[pygame.K_RIGHT]:
            pos_x_player += vel_player

        pos_y_player = max(0, min(pos_y_player, altura_tela - nave_player.get_height()))
        pos_x_player = max(0, min(pos_x_player, largura_tela - nave_player.get_width()))

        if pos_x_inimigo < pos_x_player:
            pos_x_inimigo += vel_inimigo
        elif pos_x_inimigo > pos_x_player:
            pos_x_inimigo -= vel_inimigo

        for misil in misseis_jogador[:]:
            misil[1] -= vel_missil
            if misil[1] < 0:  
                misseis_jogador.remove(misil)

        for misil in misseis_jogador[:]:
            if (pos_x_inimigo < misil[0] < pos_x_inimigo + nave_inimiga.get_width()) and (pos_y_inimigo < misil[1] < pos_y_inimigo + nave_inimiga.get_height()):
                misseis_jogador.remove(misil)
                pontuacao += 1  
                pos_x_inimigo = randint(0, largura_tela - nave_inimiga.get_width())  
                pos_y_inimigo = 50  

        contador_disparo_inimigo += 1
        if contador_disparo_inimigo >= intervalo_disparo_inimigo:  
            disparo_x = pos_x_player - (pos_x_inimigo + 20)  
            disparo_y = pos_y_player - (pos_y_inimigo + nave_inimiga.get_height())

            dist = (disparo_x ** 2 + disparo_y ** 2) ** 0.5
            if dist != 0:  
                disparo_x /= dist
                disparo_y /= dist

            misseis_inimigo.append([pos_x_inimigo + 20, pos_y_inimigo + nave_inimiga.get_height(), disparo_x, disparo_y])
            contador_disparo_inimigo = 0 

            intervalo_disparo_inimigo = max(intervalo_disparo_minimo, 40 - pontuacao // 2)  

        for misil in misseis_inimigo[:]:
            misil[1] += vel_missil * misil[3]  
            misil[0] += vel_missil * misil[2]  
            if misil[1] > altura_tela or misil[0] < 0 or misil[0] > largura_tela:  
                misseis_inimigo.remove(misil)

        for misil in misseis_inimigo[:]:
            if (pos_x_player < misil[0] < pos_x_player + nave_player.get_width()) and (pos_y_player < misil[1] < pos_y_player + nave_player.get_height()):
                print("Você foi atingido!")
                jogo_ativo = False  

        janela.blit(imagem_fundo, (0, 0))
        janela.blit(nave_player, (pos_x_player, pos_y_player))
        janela.blit(nave_inimiga, (pos_x_inimigo, pos_y_inimigo))

        for misil in misseis_jogador:
            janela.blit(missil_atirado, (misil[0], misil[1]))  

        for misil in misseis_inimigo:
            janela.blit(missil_atirado, (misil[0], misil[1]))  

        font = pygame.font.Font(None, 36)   
        texto = font.render(f'Pontuação: {pontuacao}', True, (255, 255, 255))
        janela.blit(texto, (10, 10))

        pygame.display.update()

    tela_final(janela, pontuacao)  

pygame.quit()
