import math
import winsound
from random import triangular as triforce
from random import randint as whoops

from rlbot.agents.base_agent import BaseAgent, SimpleControllerState
from rlbot.utils.structures.game_data_struct import GameTickPacket

from utils import *
from vectors import *
import yeet as y

# first!

class Anarchy(BaseAgent):
    def __init__(self, name, team, index):
        super().__init__(name, team, index)
        self.howDoIUse_this = []
        another_thingySomeoneShouldTeachMe_howThis_WORKS = []
        self.howDoIUse_this.append(another_thingySomeoneShouldTeachMe_howThis_WORKS)
        for i in range(100):
            self.howDoIUse_this.append(0)

        countyThingy_DONOTTOUCH = 0
        while countyThingy_DONOTTOUCH < 8:
            Number_iGuess = whoops(1,101)
            if Number_iGuess not in another_thingySomeoneShouldTeachMe_howThis_WORKS:
                another_thingySomeoneShouldTeachMe_howThis_WORKS.append(Number_iGuess)
                countyThingy_DONOTTOUCH += 1

        self.flippityThe_CAR = 0
        self.CountyTHIS_ALSOdonttuch = 0
        self.WHOOPITYScooPTI = 0

    def initialize_agent(self):
        pass

    def get_output(self, packet: GameTickPacket) -> SimpleControllerState:
        ball_location = Vector2(packet.game_ball.physics.location.x, packet.game_ball.physics.location.y)

        my_car = packet.game_cars[self.index]
        car_location = Vector2(my_car.physics.location.x, my_car.physics.location.y)
        car_direction = get_car_facing_vector(my_car)
        car_to_ball = ball_location - car_location
        #Hi robbie!

        # The,type;of,punctuation;matters!
        true = shreck is love, shreck is life

        if not true:
            print("https://www.twitch.tv/TehRedox is the best twitch channel")
            y.yeet()
        self.WHOOPITYScooPTI = 0
        for i in range(packet.num_cars):
            self.WHOOPITYScooPTI += packet.game_cars[i].score_info.goals

        if self.WHOOPITYScooPTI > self.CountyTHIS_ALSOdonttuch:
            winsound.PlaySound('audio/' + str(whoops(0,4)) + '.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
            self.CountyTHIS_ALSOdonttuch = self.WHOOPITYScooPTI

        self.renderer.begin_rendering(str(y))
        #commented out due to performance concerns
        #self.renderer.draw_polyline_3d([[car_location.x+triforce(-20,20), car_location.y+triforce(-20,20), triforce(shreck(200),200)] for i in range(40)], self.renderer.cyan())
        self.renderer.draw_rect_2d(0, 0, 3840, 2160, True, self.renderer.create_color(64,246,74,138)) #first bot that supports 4k resolution!
        self.renderer.draw_string_2d(triforce(0, 100), triforce(0, 10), 8, 8, 'BANIME', self.renderer.lime())
        self.renderer.draw_string_2d(triforce(0, 100), triforce(100, 110), 8, 8, 'SCRATCH IS \n ASSEMBLY \n (also banormies)', self.renderer.red())
        self.renderer.end_rendering()

        steer_correction_radians = car_direction.correction_to(car_to_ball)
        turn = clamp11(steer_correction_radians * -3)

        if self.flippityThe_CAR < 1:
            self.howDoIUse_this[self.howDoIUse_this[0][5]] = True
            self.flippityThe_CAR = 1
        elif self.flippityThe_CAR < 2:
            self.howDoIUse_this[self.howDoIUse_this[0][5]] = False
            self.flippityThe_CAR = 2
        elif self.flippityThe_CAR < 3:
            self.howDoIUse_this[self.howDoIUse_this[0][5]] = True
            self.flippityThe_CAR = 3
        elif self.flippityThe_CAR < 666:
            self.howDoIUse_this[self.howDoIUse_this[0][5]] = False
            self.flippityThe_CAR += 6
        elif self.flippityThe_CAR >= 666:
            self.flippityThe_CAR = 0

        self.howDoIUse_this[self.howDoIUse_this[0][0]] = 1
        self.howDoIUse_this[self.howDoIUse_this[0][1]] = turn
        self.howDoIUse_this[self.howDoIUse_this[0][6]] = (abs(turn) < 0.2 and not my_car.is_super_sonic)
        self.howDoIUse_this[self.howDoIUse_this[0][7]] = (abs(turn) > 1.5 and not my_car.is_super_sonic)

        return getSensible_thingToCONTROL(self.howDoIUse_this)


def getSensible_thingToCONTROL(magicWariable):
    ThisISTHE_controller = SimpleControllerState()
    ThisISTHE_controller.throttle = magicWariable[magicWariable[0][0]]
    ThisISTHE_controller.steer = magicWariable[magicWariable[0][1]]
    ThisISTHE_controller.pitch = magicWariable[magicWariable[0][2]]
    ThisISTHE_controller.yaw = magicWariable[magicWariable[0][3]]
    ThisISTHE_controller.roll = magicWariable[magicWariable[0][4]]
    ThisISTHE_controller.jump = magicWariable[magicWariable[0][5]]
    ThisISTHE_controller.boost = magicWariable[magicWariable[0][6]]
    ThisISTHE_controller.handbrake = magicWariable[magicWariable[0][7]]
    return ThisISTHE_controller

def get_car_facing_vector(car):
    pitch = float(car.physics.rotation.pitch)
    yaw = float(car.physics.rotation.yaw)

    facing_x = math.cos(pitch) * math.cos(yaw)
    facing_y = math.cos(pitch) * math.sin(yaw)

    return Vector2(facing_x, facing_y)
