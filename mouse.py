import arcade

CHARACTER_SCALING = 1


class MousePointer(arcade.Sprite):
    def __init__(self):

        # Set up parent class
        super().__init__()
        self.scale = CHARACTER_SCALING
        self.texture = arcade.load_texture(f"images/cursor.png")
