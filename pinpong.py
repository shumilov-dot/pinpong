from pygame import *
from random import randint

img_back = 'background.jpg'
#музыка
mixer.init()
#mixer.music.load('')
#mixer.music.play()

game_over = False
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):

        sprite.Sprite.__init__(self)


        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed



        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= self.speed
        if keys[K_RIGHT]:
            self.rect.x += self.speed
class Enemy(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a]:
            self.rect.x -= self.speed
        if keys[K_d]:
            self.rect.x += self.speed
class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, speed_x, speed_y):
        super().__init__(player_image, player_x, player_y, size_x, size_y, 0) # Скорость для мяча будет задаваться отдельно
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        
        if self.rect.x < 0 or self.rect.right > win_width:
            self.speed_x *= -1
        if self.rect.y < 0 or self.rect.bottom > win_height:
            self.speed_y *= -1


win_width = 700       
win_height = 500
window = display.set_mode((win_width,win_height))
display.set_caption("Pinpong")
background = transform.scale(image.load(img_back), (win_width, win_height))

desk = Player('neon.webp',250,465,130,40,10)
desk2 = Enemy('neon.webp',250,0,130,40,10)
ball = Ball('ball.png', 350, 250, 30, 30, 5, 5)
finish = False

run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

            
  
    if not game_over:
        window.blit(background, (0, 0))
        
        desk.update()
        desk.reset()
        desk2.update()
        desk2.reset()
        ball.update() 
        ball.reset()
        if sprite.collide_rect(ball, desk) or sprite.collide_rect(ball, desk2):
            ball.speed_y *= -1
        if ball.rect.bottom > win_height or ball.rect.top < 0:
            game_over = True
            print("Game Over!")
    time.delay(20)
    display.update()
    