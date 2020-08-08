#sprite classes for platform game
import pygame as pg
from settings import *
vec = pg.math.Vector2

class Spritesheet:
    #utility class for loading and parsing spritesheets
    def __init__(self, filename):
        self.spritesheet = pg.image.load(filename).convert()

    def get_image(self, x, y, width, height):
        #grab an image out of a larger spritesheet
        image = pg.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        return image

class Player(pg.sprite.Sprite):
    #this allows the player to know about the game (passing the game tot he player)
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.walking = False
        self.jumping = False
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        self.image = self.standing_frames[0]
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def load_images(self):
        self.standing_frames = [self.game.spritesheet.get_image(67, 196, 66, 92),
                               self.game.spritesheet.get_image(0, 196, 66, 92)]
        self.walk_frames_r = [self.game.spritesheet.get_image(73, 98, 72, 97),
                               self.game.spritesheet.get_image(146, 98, 72, 97),
                               self.game.spritesheet.get_image(219, 0, 72, 97),
                                self.game.spritesheet.get_image(292, 0, 72, 97)]
        self.walk_frames_l = []
        for frame in self.walk_frames_r:
            self.walk_frames_l.append(pg.transform.flip(frame, True, False))
        self.jump_frame_r = self.game.spritesheet.get_image(438, 93, 67, 94)
        self.jump_frame_l = pg.transform.flip(self.jump_frame_r, True, False)



    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -20


    def update(self):
        self.animate()
        self.acc = vec(0, GRAVITY)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.acc.x = PLAYER_ACC


        #apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        #equations of motion
        self.vel += self.acc
        if abs(self.vel.x) < 0.2:
            self.vel.x = 0
        if abs(self.vel.y) < 0.1:
            self.vel.y = 0
        self.pos += self.vel + 0.5 * self.acc
        #wrap around sides of screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        if self.pos.y > HEIGHT:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = HEIGHT

        self.rect.midbottom = self.pos

    def animate(self):
        # get ticks is a built in function
        now = pg.time.get_ticks()
        if self.vel.x != 0:
            self.walking = True
        else:
            self.walking = False
        if self.vel.y != 0:
            self.jumping = True
        else:
            self.jumping = False
        #show walk animation
        if self.walking:
            if now - self.last_update > 100:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.walk_frames_l)
                bottom = self.rect.bottom
                if self.vel.x  > 0:
                    self.image = self.walk_frames_r[self.current_frame]
                else:
                    self.image = self.walk_frames_l[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom
        if self.jumping:
            self.last_update = now
            bottom = self.rect.bottom
            if self.vel.x >= 0:
                self.image = self.jump_frame_r
            else:
                self.image = self.jump_frame_l
            self.rect = self.image.get_rect()
            self.rect.bottom = bottom
        #stand animation
        if not self.jumping and not self.walking:
            if now - self.last_update > 350:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.standing_frames)
                bottom = self.rect.bottom
                self.image = self.standing_frames[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom



class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill((RED))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y