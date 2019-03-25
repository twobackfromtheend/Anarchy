import base64
import math
import random
from random import triangular as triforce
import webbrowser
from rlbot.agents.base_agent import BaseAgent, SimpleControllerState
from rlbot.utils.structures.game_data_struct import GameTickPacket
# Anarchy requires the newest rlutilities which cannot be pip installed via `pip install rlutilities` because it is not on PyPI. You must install it via `pip install -e .` after cloning the RLUtilities repository at: https://github.com/samuelpmish/RLUtilities.
'''from rlutilities.linear_algebra import *
from rlutilities.mechanics import Aerial
from rlutilities.simulation import Game, Ball'''
from utils import *
from vectors import *
from typing import Optional


# first!

class Anarchy(BaseAgent):
    def __init__(self, name, team, index):
        super().__init__(name, team, index)
        '''
        Game.set_mode("soccar")
        ie = webbrowser.get('windows-default')
        ie.open('https://www.twitch.tv/donutkiller_pro')

        self.game: Game = Game(index, team)
        self.aerial: Optional[Aerial] = None
        '''
        self.controller: SimpleControllerState = SimpleControllerState()
        #self.state: State = State.NOT_AERIAL

    def initialize_agent(self):
        pass

    def get_output(self, packet: GameTickPacket) -> SimpleControllerState:
        '''
        self.game.read_game_information(packet, self.get_rigid_body_tick(), self.get_field_info())

        # Handle aerialing
        if self.game.ball.location[2] > 250:
            if self.state == State.AERIAL:
                self.aerial.step(self.game.time_delta)
                if self.aerial.finished:
                    self.state = State.NOT_AERIAL
                return self.aerial.controls
            else:
                self.aerial = Aerial(self.game.my_car)
                self.aerial.up = normalize(vec3(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)))
                # predict where the ball will be
                prediction = Ball(self.game.ball)
                for i in range(100):
                    prediction.step(0.016666)
                    if prediction.location[2] > 500:
                        self.aerial.target = prediction.location
                        self.aerial.arrival_time = prediction.time
                        if self.aerial.is_viable():
                            self.aerial.target = prediction.location
                            self.aerial.arrival_time = prediction.time
                            self.state = State.AERIAL
                            break
        '''
        ball_location = Vector2(packet.game_ball.physics.location.x, packet.game_ball.physics.location.y)        

        my_car = packet.game_cars[self.index]
        car_location = Vector2(my_car.physics.location.x, my_car.physics.location.y)
        car_direction = get_car_facing_vector(my_car)
        ball_location.y -= abs((ball_location - car_location).y) / 2 * (1 if self.team == 0 else - 1)
        car_to_ball = ball_location - car_location
        # Hi robbie!

        # The,type;of,punctuation;matters!
        true = shreck is love, shreck is life
        main(9)
        if true:
            print("https://www.twitch.tv/TehRedox is the best twitch channel")

        self.renderer.begin_rendering(str(y))
        # commented out due to performance concerns
        # self.renderer.draw_polyline_3d([[car_location.x+triforce(-20,20), car_location.y+triforce(-20,20), triforce(shreck(200),200)] for i in range(40)], self.renderer.cyan())
        self.renderer.draw_rect_2d(0, 0, 3840, 2160, True, self.renderer.create_color(64, 246, 74,
                                                                                      138))  # first bot that supports 4k resolution!
        self.renderer.draw_string_2d(triforce(0, 100), triforce(0, 10), 8, 8, 'ZERO TWO IS BEST GIRL', self.renderer.lime())
        self.renderer.draw_string_2d(triforce(0, 100), triforce(100, 110), 8, 8,
                                     'SCRATCH IS \n ASSEMBLY \n (also banormies) \n https://www.twitch.tv/donutkiller_pro', self.renderer.red())
        self.renderer.end_rendering()

        steer_correction_radians = car_direction.correction_to(car_to_ball)
        turn = clamp11(steer_correction_radians * 3)

        self.controller.throttle = 1
        self.controller.steer = turn
        self.controller.boost = (abs(turn) < 0.2 and not my_car.is_super_sonic)
        self.controller.handbrake = (abs(turn) > 1.5 and not my_car.is_super_sonic)

        return self.controller


def get_car_facing_vector(car):
    pitch = float(car.physics.rotation.pitch)
    yaw = float(car.physics.rotation.yaw)

    facing_x = math.cos(pitch) * math.cos(yaw)
    facing_y = math.cos(pitch) * math.sin(yaw)

    return Vector2(facing_x, facing_y)
