import arcade
import os
from player import PlayerCharacter

# Constants
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN_TITLE = "Crafter"


# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 5

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):
        """
        Initializer for the game
        """

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.lmb_pressed = False

        # These are 'lists' that keep track of our sprites. Each sprite should
        # go into a list.
        self.player_list = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """

        # Create the Sprite lists
        self.player_list = arcade.SpriteList()

        # Set up the player, specifically placing it at these coordinates.
        self.player_sprite = PlayerCharacter()

        self.player_sprite.center_x = SCREEN_WIDTH / 2
        self.player_sprite.center_y = SCREEN_HEIGHT / 2
        self.targetx = self.player_sprite.center_x
        self.targety = self.player_sprite.center_y
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()

        # Draw our sprites
        self.player_list.draw()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        """ Handle Mouse Clicks """
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.targetx = x
            self.targety = y
            self.lmb_pressed = True

    def on_mouse_motion(self, x, y, dx, dy):
        if self.lmb_pressed:
            self.targetx = x
            self.targety = y

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        """ Handle Mouse Clicks """
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.lmb_pressed = False

    def on_update(self, delta_time):
        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        # Move Sprite to mouse location
        if abs(self.player_sprite.center_x - self.targetx) < PLAYER_MOVEMENT_SPEED:
            self.player_sprite.center_x = self.targetx
        elif self.player_sprite.center_x < self.targetx:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
        elif self.player_sprite.center_x > self.targetx:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED

        if abs(self.player_sprite.center_y - self.targety) < PLAYER_MOVEMENT_SPEED:
            self.player_sprite.center_y = self.targety
        elif self.player_sprite.center_y < self.targety:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif self.player_sprite.center_y > self.targety:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED

        # Call update to move the sprite
        self.player_list.update()
        self.player_list.update_animation(delta_time)


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
