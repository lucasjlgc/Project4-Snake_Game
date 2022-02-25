import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

# Variavel Cor
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
preto = (0, 0, 0)
branco = (255, 255, 255)

# Medidas da tela
largura = 640
altura = 480

# Posição da cobra
x = 320
y = 240

# Variavel Tamanho da cobra
tamanho_cobra_x = 20
tamanho_cobra_y = 20

# Posição da Maçã
x_m = randint(40, 300)
y_m = randint(50, 400)

# Variavel de controle
x_controle = 20
y_controle = 0

# Variavel de Pontos
pontos = 0

# Variavel
velocidade = 3

# Criando Musica
#pygame.mixer.music.set_volume(0.7)
#pygame.mixer.music.load('BoxCat Games - Mission.mp3')
#pygame.mixer.music.play(-1)

# Criando Som de Colisões
#toque = pygame.mixer.Sound('smw_lemmy_wendy_correct.wav')

# Criando Tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da cobrinha')

# Criando quantidade de frames por segundo
relogio = pygame.time.Clock()

# Criando texto na tela
fonte = pygame.font.SysFont('arial', 30, True, True)

# Lista cobra deve ficar fora do loop para que não reinicie a cada interação
lista_cobra = []

# Tamanho inicial da cobra
tamanho_inicial = 5

# Variavel morreu caso a cobra se toque
morreu = False


# Função que cria o corpo da cobra
def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        # XeY = []
        # XeY[0] = x
        # XeY[1] = y
        pygame.draw.rect(tela, verde, (XeY[0], XeY[1], tamanho_cobra_x, tamanho_cobra_y))


def reiniciar_jogo():
    global pontos, tamanho_inicial, x, y, lista_cobra, lista_cabeca, x_m, y_m, morreu
    pontos = 0
    tamanho_inicial = 5
    x = largura / 2
    y = altura / 2
    lista_cobra = []
    lista_cabeca = []
    x_m = randint(40, 300)
    y_m = randint(50, 400)
    morreu = False


# Criando Loop do jogo


while True:
    tela.fill(branco)
    relogio.tick(100)
    msg = f'Pontos: {pontos}'
    exposto = fonte.render(msg, True, preto, branco)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = - velocidade
                    y_controle = 0

            if event.key == K_RIGHT:
                if x_controle == - velocidade:
                    pass
                else:
                    x_controle = +velocidade
                    y_controle = 0

            if event.key == K_UP:
                if y_controle == velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = -velocidade

            if event.key == K_DOWN:
                if y_controle == velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = +velocidade

    # No loop for eu faço a posição da cobra sempre receber mais o valor da variavel x ou y controle
    x += x_controle
    y += y_controle

    # Criando objetos
    cobra = pygame.draw.rect(tela, verde, (x, y, tamanho_cobra_x, tamanho_cobra_y))
    if x > 640:
        x = 0
    elif x < 0:
        x = 640
    if y > 480:
        y = 0
    elif y < 0:
        y = 480
    maca = pygame.draw.rect(tela, vermelho, (x_m, y_m, 20, 20))

    """
       # Adicionando funcionalidade aos Botões
       if pygame.key.get_pressed()[K_LEFT]:
           x -= 20
       if pygame.key.get_pressed()[K_RIGHT]:
           x += 20
       if pygame.key.get_pressed()[K_DOWN]:
           y += 20
       if pygame.key.get_pressed()[K_UP]:
           y -= 20
       """

    if cobra.colliderect(maca):
        x_m = randint(20, 610)
        y_m = randint(20, 450)
        tamanho_inicial += 20
        pontos += 1
        #toque.play()

    # Lista que armazena dentro de uma lista as ultimas POSIÇÕES da cobra
    lista_cabeca = list()
    lista_cabeca.append(x)
    lista_cabeca.append(y)

    # Lista que armazena outra lista com as posições x e y da cobra desde o inicio
    # A Lista cobra esta fora do loop, pois se não ela reinicia toda vez
    lista_cobra.append(lista_cabeca)

    # Se a cobra se tocar o jogo acaba

    if lista_cobra.count(lista_cabeca) > 1:
        morreu = True
        fonte2 = pygame.font.SysFont('arial', 40, True, False)
        fonte3 = pygame.font.SysFont('arial', 20, True, True)
        mensa = ' GAME OVER '
        mensa2 = 'Aperte (r) e tente de novo!'

        texto = fonte2.render(mensa, True, branco)
        texto2 = fonte3.render(mensa2, True, branco, verde)

        while morreu:
            tela.fill(preto)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            tela.blit(texto, (170, 170))
            tela.blit(texto2, (170, 220))
            pygame.display.update()

    # Comando necessário para a cobra não ficar crescendo indefinidademente.

    if len(lista_cobra) > tamanho_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)

    tela.blit(exposto, (430, 10))
    pygame.display.update()