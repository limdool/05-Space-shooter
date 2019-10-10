import sys, logging, arcade

#check to make sure we are running the right version of Python
version = (3,7)
assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0],version[1])

#turn on logging, in case we have to leave ourselves debugging messages
logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "2D Shooter"

NUM_ENEMIES = 5
STARTING_LOCATION = (200,100)
BULLET_DAMAGE = 10
ENEMY_HP = 100 
HIT_SCORE = 10
KILL_SCORE = 1000
BACKGROUND_Image = "Background-3.png"

class Bullet(arcade.Sprite):
    def __init__(self, position, velocity, damage):
        ''' 
        initializes the bullet
        Parameters: position: (x,y) tuple
            velocity: (dx, dy) tuple
            damage: int (or float)
        '''
        super().__init__("assets/spaceBullet_003.png", 0.5)
        (self.center_x, self.center_y) = position
        (self.dx, self.dy) = velocity
        self.damage = damage

    def update(self):
        '''
        Moves the bullet
        '''
        self.center_x += self.dx
        self.center_y += self.dy


class Window(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_mouse_visible(True)  

        arcade.set_background_color((0,0,0)) 
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.player = arcade.Sprite("assets/spaceShips_005.png",1)
        self.player.center_x = 400
        self.player.center_y = 100
        self.player_list.append(self.player)
        self.score = 0
        
        self.enemy = arcade.Sprite("assets/shipBeige_manned.png", 0.5)
        self.enemy.center_x = 650
        self.enemy.center_y = 400
        self.enemy.hp = ENEMY_HP
        self.enemy_list.append(self.enemy)

        self.enemy = arcade.Sprite("assets/shipBlue_manned.png", 0.5)
        self.enemy.center_x = 550
        self.enemy.center_y = 400
        self.enemy.hp = ENEMY_HP
        self.enemy_list.append(self.enemy)

        self.enemy = arcade.Sprite("assets/shipGreen_manned.png", 0.5)
        self.enemy.center_x = 450
        self.enemy.center_y = 400
        self.enemy.hp = ENEMY_HP
        self.enemy_list.append(self.enemy)

        self.enemy = arcade.Sprite("assets/shipPink_manned.png", 0.5)
        self.enemy.center_x = 350
        self.enemy.center_y = 400
        self.enemy.hp = ENEMY_HP
        self.enemy_list.append(self.enemy)

        self.enemy = arcade.Sprite("assets/shipYellow_manned.png", 0.5)
        self.enemy.center_x = 250
        self.enemy.center_y = 400
        self.enemy.hp = ENEMY_HP
        self.enemy_list.append(self.enemy)
        '''
        self.enemy = arcade.Sprite("assets/shipBiege_manned.png", 0.5)
        self.enemy = arcade.Sprite("assets/shipBlue_manned.png", 0.5)
        self.enemy = arcade.Sprite("assets/shipGreen_manned.png", 0.5)
        self.enemy = arcade.Sprite("assets/shipPink_manned.png", 0.5)
        self.enemy = arcade.Sprite("assets/shipYellow_manned.png", 0.5)
        '''
        self.hp = ENEMY_HP  

    def setup(self):
        '''
        Set up enemies
        ''' 
        pass


    def update(self, delta_time):
        self.bullet_list.update()
        for e in self.enemy_list:
            damage = arcade.check_for_collision_with_list (e, self.bullet_list)
            for d in damage:
                e.hp = e.hp - d.damage
                d.kill()
                if e.hp <= 0:
                    e.kill()
                    self.score = self.score + KILL_SCORE
                else:
                    self.score = self.score + HIT_SCORE 

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(str(self.score), 20, SCREEN_HEIGHT - 40, (255,255,255), 16)
        self.player_list.draw()
        self.bullet_list.draw()
        self.enemy_list.draw()


    def on_mouse_motion(self, x, y, dx, dy):
        """ 
        The player moves left and right with the mouse.
        """
        self.player.center_x = x

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            x = self.player.center_x
            y = self.player.center_y + 15
            bullet = Bullet((x,y),(0,10),BULLET_DAMAGE)
            self.bullet_list.append(bullet)
  


def main():
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()