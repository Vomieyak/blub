from pygame import *
font.init()
x1 = 0
y1 = 250
y2 = 250
x2 = 600
speed_x = 3
speed_y = 3
a = 0
c = 0
#создай окно игры
w = display.set_mode((700, 500))
display.set_caption('Догонялки')
#задай фон сцены
background = transform.scale(image.load('background.jpg'), (700, 500))

#создай 2 спрайта и размести их на сцене


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.size_x = size_x
        self.size_y = size_y
    def reset(self):
        w.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y !=  480 - 80:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y != 480 - 80:
            self.rect.y += self.speed


krip1 = Player2('palka.png', 0, 250, 5, 100, 100)
krip2 = Player1('palka.png', 625, 250, 5, 100, 100)
b = GameSprite('ball.jpg', 350, 250, 1, 15, 15)
f1 = font.SysFont('Arial', 70)
win = f1.render('YOU WIN', True, (180, 0, 0))
f2 = font.SysFont('Arial', 70)
FPS = 60
clock = time.Clock()
game = True
finish = False
sc = f1.render('Счёт:'+str(a), True, (255, 255, 255))
sc2 = f2.render('Счёт:'+str(c), True, (255, 255, 255))
while game == True:
    w.blit(background, (0, 0))
    w.blit(sc, (10,10))
    w.blit(sc2, (690, 490))
    krip1.reset()
    krip2.reset()
    krip1.update()
    krip2.update()
    b.reset()
    b.update()
    clock.tick(FPS)
    display.update()
    keys_pressed = key.get_pressed()

    if finish != True:
        b.rect.x += speed_x
        b.rect.y += speed_y
        
    if b.rect.y > 500-50 or b.rect.y < 0:
        speed_y *= -1

    if sprite.collide_rect(krip1, b) or sprite.collide_rect(krip2, b):
        speed_x *= -1

    if b.rect.x <= 0:
        b.rect.x = 350
        b.rect.y = 250
        a += 1

    if b.rect.x >= 700:
        b.rect.x = 350
        b.rect.y = 250
        c += 1


    for e in event.get():
        if e.type == QUIT:
            game = False
    
