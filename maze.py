#создай игру "Лабиринт"!
# импорт модулей
from pygame import *
mixer.init()
# класс GameSprite и его друзья
class GameSprite(sprite.Sprite):
    def __init__(self, pl_image, pl_speed, pl_w, pl_h, pl_x, pl_y):
        super().__init__()
        self.image = transform.scale(image.load(pl_image), (pl_w, pl_h))
        self.speed = pl_speed
        self.rect = self.image.get_rect()
        self.rect.x = pl_x
        self.rect.y = pl_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 600:
            self.rect.x += self.speed
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed
class Enemy(GameSprite):
    def __init__(self, image_path, speed, width, height, x, y):
        super().__init__(image_path, speed, width, height, x, y)
        self.direction = 'left'

    def update(self):
        if self.direction == 'left':
            self.rect.x -= self.speed
            if self.rect.x <= 100:
                self.direction = 'right'
        else:
            self.rect.x += self.speed
            if self.rect.x >= 635:
                self.direction = 'left'
class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, width, height, x, y):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill((color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
blue = Player('hero.png', 5, 65, 65, 5, 420)
terminator = Enemy('cyborg.png', 2, 65, 65, 500, 250)
terminator2 = Enemy('cyborg.png', 2, 65, 65, 100, 140)
treasure = GameSprite('treasure.png', 5, 65, 65, 625, 400)
wall1 = Wall(160, 255, 156, 650, 10, 50, 10)
wall2 = Wall(160, 255, 156, 10, 400, 50, 10)
wall3 = Wall(160, 255, 156, 550, 10, 50, 490)
wall4 = Wall(160, 255, 156, 10, 900, 150, 320)
wall5 = Wall(160, 255, 156, 10, 400, 365, 400)
wall6 = Wall(160, 255, 156, 10, 1000, 550, 320)
wall7 = Wall(160, 255, 156, 10, 300, 250, 0)
wall8 = Wall(160, 255, 156, 10, 300, 450, 0)
# создание окна
window = display.set_mode((700, 500))
display.set_caption('Maze')
# создание сцены
background = transform.scale(image.load('background.jpg'), (700, 500))
# создание музыки mixer
mixer.music.load('jungles.ogg')
kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')
mixer.music.play()
# игровой цикл
font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (236, 226, 156))
lose = font.render('YOU LOST!', True, (255, 129, 124))
try_again = font.render('PRESS SPACE TO RESTART!', True, (255, 129, 124))
fps = 60
speed = 10
clock = time.Clock()
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN and e.key == K_SPACE and finish:
            blue.rect.x, blue.rect.y = 5, 420
            terminator.rect.x, terminator.rect.y = 500, 250
            terminator2.rect.x, terminator2.rect.y = 100, 140
            finish = False
    if finish != True:
        blue.update()
        terminator.update()
        terminator2.update()
        window.blit(background, (0, 0))
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()
        wall7.draw_wall()
        wall8.draw_wall()
        blue.reset()
        terminator.reset()
        terminator2.reset()
        treasure.reset()
        if sprite.collide_rect(blue, treasure):
            finish = True
            window.blit(win, (230, 230))
            display.update()
            money.play()
        elif sprite.collide_rect(blue, terminator) or sprite.collide_rect(blue, terminator2):
            finish = True
            window.blit(lose, (230, 230))
            window.blit(try_again, (20, 270))
            display.update()
            kick.play()
        elif sprite.collide_rect(blue, wall1) or sprite.collide_rect(blue, wall2) or sprite.collide_rect(blue, wall3) or sprite.collide_rect(blue, wall4) or sprite.collide_rect(blue, wall5) or sprite.collide_rect(blue, wall6) or sprite.collide_rect(blue, wall7) or sprite.collide_rect(blue, wall8):
            finish = True
            window.blit(lose, (230, 210))
            window.blit(try_again, (20, 270))
            display.update()
            kick.play()
    display.update()
    clock.tick(fps)