from rlbot.agents.base_agent import BaseAgent, SimpleControllerState
from rlbot.utils.structures.game_data_struct import GameTickPacket

# first! 

class Anarchy(BaseAgent):
    def __init__(self, name, team, index):
        super().__init__(name, team, index)
        self.controller = SimpleControllerState()

    def initialize_agent(self):
        pass

    def get_output(self, packet: GameTickPacket) -> SimpleControllerState:
        return self.controller
