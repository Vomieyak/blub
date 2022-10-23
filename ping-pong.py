from pygame import *
x1 = 100
y1 = 300
y2 = 300
x2 = 400

#создай окно игры
w = display.set_mode((700, 500))
display.set_caption('Догонялки')
#задай фон сцены
background = transform.scale(image.load('background.jpg'), (700, 500))

#создай 2 спрайта и размести их на сцене
krip1 = transform.scale(image.load('palka.png'), (100, 100))
krip2 = transform.scale(image.load('palka.png'), (100, 100))

#обработай событие «клик по кнопке "Закрыть окно"»
FPS = 60
clock = time.Clock()
game = True
while game == True:
    w.blit(background, (0, 0))
    w.blit(krip1, (x1, y1))
    w.blit(krip2, (x2, y2))
    clock.tick(FPS)
    display.update()
    keys_pressed = key.get_pressed()

    if keys_pressed[K_UP] and y1 != 0:
        y1 -= 10
    if keys_pressed[K_DOWN] and y1 != 400:
        y1 += 10
    if keys_pressed[K_w] and y2 != 0:
        y2 -= 10
    if keys_pressed[K_s] and y2 != 400:
        y2 += 10


    for e in event.get():
        if e.type == QUIT:
            game = False
    
