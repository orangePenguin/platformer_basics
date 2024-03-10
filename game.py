import arcade

# Screen Dimensions.
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Django's Escapades."
CHARACTER_SCALING = 1
TILE_SCALING = 0.5


# Main Class.
class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.player_list = None
        self.wall_list = None
        self.player_sprite = None

        arcade.set_background_color(arcade.color.BLACK_BEAN)

    # Call function to Restart the Game.
    def setup(self):
        # Sprite Lists.
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)

        # Co-ordinates for Sprite.
        image_source = ":resources:images/animated_characters/robot/robot_idle.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.player_list.append(self.player_sprite)

        # Create the Ground.
        # This shows using a loop to place multiple sprites horizontally.
        for x in range(0, 1200, 64):
            wall = arcade.Sprite(":resources:images/tiles/snowMid.png", TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)

    def on_draw(self):
        self.clear()
        self.wall_list.draw()
        self.player_list.draw()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
