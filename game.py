import pygame
pygame.init()

from random import randint # Importa o método para gerar números aleatórios

# Definir a janela
largura = 1380
altura = 720
janela = pygame.display.set_mode ((largura, altura))
sair = 0	# Sair do jogo ao clicar no X da janela

# Coordenadas do carro principal
x = largura / 2
y = altura / 2 - 50
y_titulo = y	# Na tela de Título
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

#Imagens Tela de Título
fundo_telaTitulo = pygame.image.load ('pista_1.jpg')
nome_jogo = pygame.image.load ('Tela_1_Logo.png')
jogar = pygame.image.load ('Tela_2_Jogar.png')
como_jogar = pygame.image.load ('Tela_3_Como_Jogar.png')
sair_do_jogo = pygame.image.load ('Tela_4_Sair.png')
cursor = pygame.image.load ('Tela_5_Cursor.png')
teclaX = pygame.image.load ('Tela_6_Tecle_X.png')
cx_text_1 = pygame.image.load ('Caixa_Text_1.png')
info = pygame.image.load ('Info.png')
cx_text_2 = pygame.image.load ('Caixa_Text_2.png')

# Controles Tela de Título
setaX = -10; setaY = 80	# Coordenadas da Seta das opções
mover_seta = 0			# Controla a movimentação da Seta em X
opcoes = 1				# [1 == Jogar] --- [2 == Como Jogar] --- [3 == Sair] --- [0 == Na tela de COMO JOGAR]
controle_move = 0		# Controlar a movimentação da Seta/Cursor
move_tecleX = 595		# Usado para animar o "Tecle X"

# Nome do jogo
pygame.display.set_caption ("Fórmula 1 - 2022") 

# Musica
pygame.mixer.init ()
pygame.mixer.music.load ('TopGear.mp3')
pygame.mixer.music.play (-1)

# Efeitos Sonoros
som_cursor = pygame.mixer.Sound ('Cursor_02.mp3')
som_selecione = pygame.mixer.Sound ('Select_Sound.mp3')

# ──────────────────────────────────────────────────────────────────────────────────────

# A Tela de Título
telaTitulo = True
while telaTitulo :	# Enquanto a janela for true
    pygame.time.delay (50)	# Atualizar a tela após 50 milisegundos
    
    # Fechar a janela
    for event in pygame.event.get () :  # Fecha o jogo no botão X da janela
        if event.type == pygame.QUIT :
            sair = 1
            telaTitulo = False
    
    # Movimento dos carros inimigos e reposicionamento aleatório
    if (y_titulo <= -200) :
        y_titulo = randint (800, 1000)
    
    # Movimento do carro
    y_titulo -= velocidade - 5
    
    # Animação da Seta / Cursor em X --- Animação do "Tecle X"
    if (mover_seta == 0) :
        setaX += 2
        move_tecleX += 3
        if (setaX >= 15) :
            mover_seta = 1
    
    if (mover_seta == 1) :
        setaX -= 2
        move_tecleX -= 3
        if (setaX <= -10) :
            mover_seta = 0
    
    # Mover a Seta/Curso entre as opções
    # Selecionado a Opção → JOGAR
    if (opcoes == 1) :
        teclar = pygame.key.get_pressed()
        if (teclar[pygame.K_x]) :			# Teclou X: Inicia o jogo
            som_selecione.play()
            telaTitulo = False
        
        if teclar[pygame.K_DOWN] :
            som_cursor.play()
            setaY += 80
            opcoes = 2
            controle_move = 1
    
    # Selecionado a Opção → COMO JOGAR
    if (opcoes == 2) :
        teclar = pygame.key.get_pressed()
        if (teclar[pygame.K_x]) :
            som_selecione.play()
            opcoes = 0
        
        teclar = pygame.key.get_pressed()
        if teclar[pygame.K_UP] :
            som_cursor.play()
            setaY -= 80
            opcoes = 1
        
        if teclar[pygame.K_DOWN] and (controle_move == 0) :
            som_cursor.play()
            setaY += 80
            opcoes = 3
    
    # Selecionado a Opção → SAIR
    if (opcoes == 3) :
        teclar = pygame.key.get_pressed()
        if (teclar[pygame.K_x]) :				# Tecou X: Sai do jogo
            som_selecione.play()
            sair = 1
            telaTitulo = False
        
        if teclar[pygame.K_UP] :
            som_cursor.play()
            setaY -= 80
            opcoes = 2
    
    # Exibir imagens
    janela.blit (fundo_telaTitulo, (0, 0))
    janela.blit (carro, (x - 75, y_titulo + 125))
    janela.blit (nome_jogo, (25, 25))
    janela.blit (jogar, (100, 120))
    janela.blit (como_jogar, (100, 200))
    janela.blit (sair_do_jogo, (100, 280))
    janela.blit (cursor, (setaX, setaY))
    cx_text_1.set_alpha(127)						# Aplica Opacidade na imagem cx_text_1
    janela.blit (cx_text_1, (0, 595))
    janela.blit (teclaX, (move_tecleX, 630))
    
    # Opção == 0 Quando selecionar a Opção "COMO JOGAR"
    if (opcoes == 0) :
        cx_text_2.set_alpha(150)	
        janela.blit (cx_text_2, (210, 260))
        janela.blit (info, (250, 350))
        teclar = pygame.key.get_pressed()
        if (teclar[pygame.K_y]) :
            som_selecione.play()
            janela.blit (cx_text_2, (210, 2260))
            janela.blit (info, (250, 2350))
            opcoes = 2
    
    # Controla a movimentação da Seta/Cursor para não mover imediatamente até a opção 3
    if (opcoes == 2) :
        controle_move = 0
    
    pygame.display.update () # Atualiza a tela

# Ao clicar em sair, encerrará todo o progresso aqui
if (sair == 1) :
    pygame.quit () # Fecha a janela

# ──────────────────────────────────────────────────────────────────────────────────────

# Texto: Fonte etc
fonte = pygame.font.SysFont ('arial', 38)
texto = fonte.render ("Pontos: ", True, (255,255,255), (0,0,0))
pos_texto = texto.get_rect ()
pos_texto.center = (65,50)

# Pontuação e outros dados de jogo
pontos = 0

# ──────────────────────────────────────────────────────────────────────────────────────

# O jogo
gamePlay = True
while gamePlay :	# Enquanto a janela for true
    pygame.time.delay (50)	# Atualizar a tela após 50 milisegundos
    
    # Fechar a janela
    for event in pygame.event.get () :  # Fecha o jogo no botão X da janela
        if event.type == pygame.QUIT :
            gamePlay = False
    
    # Comandos de movimento e colisão nas laterais da pista
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_RIGHT] and (x <= 1100):
        x += velocidade
    if comandos[pygame.K_LEFT] and (x >= 475):
        x -= velocidade
    
    # A Colisão entre os carros
    # Carro 1
    if ((x - 130 < posX_inimigo_1) and ((y + 130 >= posY_inimigo_1) and (y - 70 <= posY_inimigo_1))) :
        y = 1200
    
    # Carro 2
    if ((x + 140 > posX_inimigo_2) and (x - 140 < posX_inimigo_2) and ((y + 130 >= posY_inimigo_2) and (y - 70 <= posY_inimigo_2))) :
        y = 1200
    
    # Carro 3
    if ((x + 145 > posX_inimigo_3) and (x - 145 < posX_inimigo_3) and ((y + 130 >= posY_inimigo_3) and (y - 70 <= posY_inimigo_3))) :
        y = 1200
    
    # Carro 4
    if ((x + 140 > posX_inimigo_4) and ((y + 130 >= posY_inimigo_4) and (y - 70 <= posY_inimigo_4))) :
        y = 1200
        
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


pygame.quit () # Fecha a janela