import arcade

# Constants used to track if the player is facing left or right
RIGHT_FACING = 0
LEFT_FACING = 1

CHARACTER_SCALING = 2


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
        self.cur_texture = 0
        self.scale = CHARACTER_SCALING

        # --- Load Textures ---
        main_path = ":resources:images/animated_characters/male_person/malePerson"

        # Load textures for idle standing
        self.idle_texture_pair = load_texture_pair(f"images/2 Owlet_Monster/Owlet_Monster.png")
        self.fall_texture_pair = load_texture_pair(f"images/2 Owlet_Monster/Owlet_Monster.png")

        # Walk Right Textures
        self.walk_textures = []
        texture = arcade.load_spritesheet(f"images/2 Owlet_Monster/Owlet_Monster_Walk_62.png", 32, 32, 6, 6)
        self.walk_textures.append(texture)

        # Walk Left Textures
        texture = arcade.load_spritesheet(f"images/2 Owlet_Monster/Owlet_Monster_Walk_6.png", 32, 32, 6, 6)
        self.walk_textures.append(texture)


        # Set the initial texture
        self.texture = self.idle_texture_pair[0]

    def update_animation(self, delta_time: float = 1 / 60):

        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING

        # Idle animation
        if self.change_x == 0 and self.change_y == 0:
            self.texture = self.idle_texture_pair[self.character_face_direction]
            return

        # Walking animation
        self.cur_texture += 1
        if self.cur_texture > 5:
            self.cur_texture = 0
        self.texture = self.walk_textures[self.character_face_direction][self.cur_texture]
