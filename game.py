import pygame
pygame.init()

from random import randint # Importa o método para gerar números aleatórios

# Definir a janela
largura = 1380
altura = 720
janela = pygame.display.set_mode ((largura, altura))

# Coordenadas do carro principal
x = largura / 2
y = altura / 2 - 50
velocidade = 10 # movimento do carro (em pixel)

# Coordenadas para os carros inimigos
posX_inimigo_1 = 510;  posY_inimigo_1 = 1000	# Azul
posX_inimigo_2 = 690;  posY_inimigo_2 = 1100	# Branco
posX_inimigo_3 = 870;  posY_inimigo_3 = 1200	# Vermelho
posX_inimigo_4 = 1030; posY_inimigo_4 = 1300	# Azure
velocidade_inimigos = 5 # velocidade dos demais carros

# Imagens do jogo
fundo = pygame.image.load ('pista_2.png')
carro = pygame.image.load ('carro_principal.png')
inimigo_1 = pygame.image.load ('inimigo_1.png')
inimigo_2 = pygame.image.load ('inimigo_2.png')
inimigo_3 = pygame.image.load ('inimigo_3.png')
inimigo_4 = pygame.image.load ('inimigo_4.png')
gameOver = pygame.image.load ('GameOver.jpg')

# Nome do jogo
pygame.display.set_caption ("Fórmula 1 - 2022") 

# Musica
pygame.mixer.init ()
pygame.mixer.music.load ('TopGear.mp3')
pygame.mixer.music.play (-1)

# Texto: Fonte etc
fonte = pygame.font.SysFont ('arial', 38)
texto = fonte.render ("Pontos: ", True, (255,255,255), (0,0,0))
pos_texto = texto.get_rect ()
pos_texto.center = (65,50)

# Pontuação e outros dados de jogo
pontos = 0
game_over = 0

# O jogo
janela_aberta = True
while janela_aberta :	# Enquanto a janela for true
    pygame.time.delay (50)	# Atualizar a tela após 50 milisegundos
    
    # Fechar a janela
    for event in pygame.event.get () :  # Fecha o jogo no botão X da janela
        if event.type == pygame.QUIT :
            janela_aberta = False
    
    # Comandos de movimento e colisão nas laterais da pista
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_RIGHT] and (x <= 1100):
        x += velocidade
    if comandos[pygame.K_LEFT] and (x >= 475):
        x -= velocidade
    
    # A Colisão entre os carros
    # Carro 1
    if ((x - 130 < posX_inimigo_1) and ((y + 130 >= posY_inimigo_1) and (y - 70 <= posY_inimigo_1))) :
        game_over = 1
        janela_aberta = False
    
    # Carro 2
    if ((x + 140 > posX_inimigo_2) and (x - 140 < posX_inimigo_2) and ((y + 130 >= posY_inimigo_2) and (y - 70 <= posY_inimigo_2))) :
        game_over = 1
        janela_aberta = False
    
    # Carro 3
    if ((x + 145 > posX_inimigo_3) and (x - 145 < posX_inimigo_3) and ((y + 130 >= posY_inimigo_3) and (y - 70 <= posY_inimigo_3))) :
        game_over = 1
        janela_aberta = False
    
    # Carro 4
    if ((x + 140 > posX_inimigo_4) and ((y + 130 >= posY_inimigo_4) and (y - 70 <= posY_inimigo_4))) :
        game_over = 1
        janela_aberta = False
        
    # Movimento dos carros inimigos e reposicionamento aleatório
    if (posY_inimigo_1 <= -200) :
        posY_inimigo_1 = randint (800, 1500)
        pontos += 1
            
    if (posY_inimigo_2 <= -200) :
        posY_inimigo_2 = randint (800, 1700)
        pontos += 5
    
    if (posY_inimigo_3 <= -200) :
        posY_inimigo_3 = randint (800, 2000)
        pontos += 2
    
    if (posY_inimigo_4 <= -200) :
        posY_inimigo_4 = randint (700, 1400)
        pontos += 2
    
    texto = fonte.render ("Pontos: "+ str(pontos), True, (255,255,255), (0,0,0)) # Atualizar a pontuação
    
    # Atualizar a posição dos carros
    posY_inimigo_1 -= velocidade_inimigos
    posY_inimigo_2 -= velocidade_inimigos + 7
    posY_inimigo_3 -= velocidade_inimigos + 6
    posY_inimigo_4 -= velocidade_inimigos + 2
    
    # Exibir imagens
    janela.blit (fundo, (0, 0))
    janela.blit (carro, (x,y))
    janela.blit (inimigo_1, (posX_inimigo_1, posY_inimigo_1))
    janela.blit (inimigo_2, (posX_inimigo_2, posY_inimigo_2))
    janela.blit (inimigo_3, (posX_inimigo_3, posY_inimigo_3))
    janela.blit (inimigo_4, (posX_inimigo_4, posY_inimigo_4))
    janela.blit (texto, pos_texto) # Exibe a janela de pontos
    
    pygame.display.update () # Atualiza a tela

# Fim do jogo - Tela de GameOver e fecha o jogo
if (game_over == 1) :
	janela.blit (gameOver, (0, 0))						#Desenha a tela de gameOver
	pos_texto.center = (largura / 2, altura / 2 + 100)	#Posiciona o texto de pontos
	janela.blit (texto, pos_texto)						#Exibe os pontos após o gameOver
	pygame.display.update ()							#Atualiza a tela (exibir a imagem)
	pygame.time.delay (5000)							#Tempo de espera para fechar a janela automaticamente

pygame.quit () # Fecha a janela
