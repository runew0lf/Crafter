import arcade
from PIL import Image

# Constants used to track if the player is facing left or right
RIGHT_FACING = 0
LEFT_FACING = 1

CHARACTER_SCALING = 2

WALK_ANIMATION_DELAY = 3
IDLE_ANIMATION_DELAY = 15

def load_texture_pair(filename):
    """
    Load a texture pair, with the second being a mirror image.
    """
    return [arcade.load_texture(filename), arcade.load_texture(filename, mirrored=True)]


class PlayerCharacter(arcade.Sprite):
    def __init__(self):

        # Set up parent class
        super().__init__()

        # Default to face-right
        self.character_face_direction = RIGHT_FACING

        # Used for flipping between image sequences
        self.scale = CHARACTER_SCALING
        self.cur_walk_texture = 0
        self.walk_animation_delay = 0
        self.cur_idle_texture = 0
        self.idle_animation_delay = 0

        ### --- Load Textures --- ###
        # Load textures for idle standing
        self.fall_texture_pair = load_texture_pair(f"images/2 Owlet_Monster/Owlet_Monster.png")

        self.idle_textures = []
        texture = arcade.load_spritesheet(f"images/2 Owlet_Monster/Owlet_Monster_Idle_4.png", 32, 32, 4, 4)
        self.idle_textures.append(texture)
        texture = arcade.load_spritesheet(f"images/2 Owlet_Monster/Owlet_Monster_Idle_42.png", 32, 32, 4, 4)
        self.idle_textures.append(texture)

        # Walk Right Textures
        self.walk_textures = []
        texture = arcade.load_spritesheet(f"images/2 Owlet_Monster/Owlet_Monster_Walk_62.png", 32, 32, 6, 6)
        self.walk_textures.append(texture)

        # Walk Left Textures
        texture = arcade.load_spritesheet(f"images/2 Owlet_Monster/Owlet_Monster_Walk_6.png", 32, 32, 6, 6)
        self.walk_textures.append(texture)


        # Set the initial texture
        self.texture = self.idle_textures[0][0]

    def update_animation(self, delta_time):

        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING

        if self.change_x == 0 and self.change_y == 0:
            # Idle animation
            self.idle_animation_delay += 1
            if self.idle_animation_delay == IDLE_ANIMATION_DELAY:
                self.cur_idle_texture += 1
                self.idle_animation_delay = 0
            if self.cur_idle_texture > 3:
                self.cur_idle_texture = 0
            self.texture = self.idle_textures[self.character_face_direction][self.cur_idle_texture]
        else:
            # Walking animation
            self.walk_animation_delay += 1
            if self.walk_animation_delay == WALK_ANIMATION_DELAY:
                self.cur_walk_texture += 1
                self.walk_animation_delay = 0
            if self.cur_walk_texture > 5:
                self.cur_walk_texture = 0
            self.texture = self.walk_textures[self.character_face_direction][self.cur_walk_texture]
