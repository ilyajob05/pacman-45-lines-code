# -*- coding: utf-8 -*-

# загрузка библиотеки
import pygame

#инициализация библиотеки
pygame.init()

#установка размера экрана
sizeScr = (800, 600)
screen = pygame.display.set_mode(sizeScr)

#название для окна
pygame.display.set_caption('Pacman')
 
#создание таймера
clock = pygame.time.Clock()

#загрузка изображения для пакмана
privedenie = pygame.image.load('./pac1.png')
#изменяем размер -> 100х100 пикселей
privedenie = pygame.transform.scale(privedenie, (100,100))

#загрузка изображения для приведения
pacMan = pygame.image.load('./pac2.png')
#изменяем размер -> 100х100 пикселей
pacMan = pygame.transform.scale(pacMan, (100,100))

#координаты пакмана
pacX = 0
pacY = 0

#координаты приведения
privedenieX = 400
privedenieY = 400

# флаг для выхода из программы (необходим для корректного закрытия программы)
runApp = True
 
# --------  цикл программы  -----------
# выполнять пока runApp равен True
while runApp:
    # --- чтение списка событий
    for event in pygame.event.get():
        #если в списке есть событие QUIT то закрыть программу
        if event.type == pygame.QUIT:
            runApp = False
 
    #чтение нажатой клавиши
    keyP = pygame.key.get_pressed()
    #если нажата клавиша влево
    if keyP[pygame.K_LEFT]:
        #уменьшить координату по Х
        pacX = pacX - 3
    if keyP[pygame.K_RIGHT]:
        pacManPovernutii = pygame.transform.rotate(pacMan, 0)
        #увеличить координату по Х
        pacX = pacX + 3
    if keyP[pygame.K_UP]:
        pacManPovernutii = pygame.transform.rotate(pacMan, 90)
        pacY = pacY - 3
    if keyP[pygame.K_DOWN]:
        pacManPovernutii = pygame.transform.rotate(pacMan, 270)
        pacY = pacY + 3
 
    # --- логика иры
    # если пакман попадает в координаты приведения +/- 50 пикселей по Х а потом по У
    if (pacX > privedenieX - 50) & (pacX < privedenieX + 50) & (privedenieX == 400):
        if (pacY > privedenieY - 50) & (pacY < privedenieY + 50):
            # перенести приведение в коодинаты (0, 0)
            privedenieX = 0
            privedenieY = 0       
    elif (pacX > privedenieX - 50) & (pacX < privedenieX + 50) & (privedenieX != 400):
        if (pacY > privedenieY - 50) & (pacY < privedenieY + 50):
            # прибавить к координатам приведения 50 пикселей
            privedenieX += 50
            privedenieY += 50
       
 
    # --- Перерисовка экрана
    # Здесь рисуем фон
    screen.fill((200,200,200))
 
    # Здесь рисуем объекты
    screen.blit(privedenie, (privedenieX, privedenieY))
    screen.blit(pacMan, (pacX, pacY))
    
    # --- Обновдение экрана
    pygame.display.flip()
 
    # --- Ждем 60 тиков таймера
    clock.tick(60)
 
# выход из программы
pygame.quit()



