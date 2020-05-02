import arcade


SPRITE_SCALING = 2

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

MOVEMENT_SPEED = 5
UPDATES_PER_FRAME = 7

RIGHT_FACING = 1
LEFT_FACING = 0


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.textures = []

        texture = arcade.load_texture(
            "images/2 Owlet_Monster/Owlet_Monster.png"
        )
        self.textures.append(texture)
        texture = arcade.load_texture(
            "images/2 Owlet_Monster/Owlet_Monster.png", mirrored=True
        )
        self.textures.append(texture)

        self.scale = SPRITE_SCALING

        # By default, face right.
        self.set_texture(LEFT_FACING)

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Figure out if we should face left or right
        if self.change_x < 0:
            self.texture = self.textures[RIGHT_FACING]
        elif self.change_x > 0:
            self.texture = self.textures[LEFT_FACING]

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1
