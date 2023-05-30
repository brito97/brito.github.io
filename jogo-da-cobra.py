import pygame
import time
import random

# Inicialização do pygame
pygame.init()

# Configurações da tela
largura = 600
altura = 600
tamanho_bloco = 20

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobra")
clock = pygame.time.Clock()

# Cores
cor_fundo = (0, 0, 0)
cor_cobra = (0, 255, 0)
cor_comida = (255, 0, 0)
cor_obstaculo = (255, 255, 255)
cor_botao = (255, 255, 255)
cor_botao_hover = (150, 150, 150)

# Função principal do jogo
def jogo():
    game_over = False
    game_exit = False

    # Posição inicial da cobra
    pos_x = largura // 2
    pos_y = altura // 2

    # Movimento inicial da cobra
    mov_x = 0
    mov_y = 0

    # Lista de segmentos da cobra
    cobra = []
    tamanho_cobra = 1

    # Posição inicial da comida
    comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0

    # Lista de coordenadas dos obstáculos
    obstaculos = []
    num_obstaculos = 10

    for _ in range(num_obstaculos):
        obstaculo_x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
        obstaculo_y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0
        obstaculos.append((obstaculo_x, obstaculo_y))

    def botao_reiniciar():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos_mouse = pygame.mouse.get_pos()
                    if 220 <= pos_mouse[0] <= 380 and 350 <= pos_mouse[1] <= 400:
                        jogo()

            tela.fill(cor_fundo)
            fonte = pygame.font.SysFont(None, 50)
            mensagem = fonte.render("Game Over!", True, (255, 255, 255))
            tela.blit(mensagem, (200, 250))

            # Botão de reinício
            pygame.draw.rect(tela, cor_botao, [220, 350, 160, 50])
            fonte_botao = pygame.font.SysFont(None, 30)
            texto_botao = fonte_botao.render("Reiniciar", True, cor_fundo)
            tela.blit(texto_botao, (240, 360))

            pygame.display.update()

    while not game_exit:
        while game_over:
            botao_reiniciar()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and mov_x != tamanho_bloco:
                    mov_x = -tamanho_bloco
                    mov_y = 0
                elif event.key == pygame.K_RIGHT and mov_x != -tamanho_bloco:
                    mov_x = tamanho_bloco
                    mov_y = 0
                elif event.key == pygame.K_UP and mov_y != tamanho_bloco:
                    mov_x = 0
                    mov_y = -tamanho_bloco
                elif event.key == pygame.K_DOWN and mov_y != -tamanho_bloco:
                    mov_x = 0
                    mov_y = tamanho_bloco

        if pos_x >= largura or pos_x < 0 or pos_y >= altura or pos_y < 0:
            game_over = True

        pos_x += mov_x
        pos_y += mov_y
        tela.fill(cor_fundo)
        pygame.draw.rect(tela, cor_comida, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])
        pygame.draw.rect(tela, cor_cobra, [pos_x, pos_y, tamanho_bloco, tamanho_bloco])

        cabeca_cobra = []
        cabeca_cobra.append(pos_x)
        cabeca_cobra.append(pos_y)
        cobra.append(cabeca_cobra)

        if len(cobra) > tamanho_cobra:
            del cobra[0]

        for segmento in cobra[:-1]:
            if segmento == cabeca_cobra:
                game_over = True

        for segmento in cobra:
            pygame.draw.rect(tela, cor_cobra, [segmento[0], segmento[1], tamanho_bloco, tamanho_bloco])

        for obstaculo in obstaculos:
            pygame.draw.rect(tela, cor_obstaculo, [obstaculo[0], obstaculo[1], tamanho_bloco, tamanho_bloco])

        pygame.display.update()

        if pos_x == comida_x and pos_y == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
            comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0
            tamanho_cobra += 1

        for obstaculo in obstaculos:
            if pos_x == obstaculo[0] and pos_y == obstaculo[1]:
                game_over = True

        clock.tick(2)

    pygame.quit()
    quit()

# Executa o jogo
jogo()