from typing import List
import random

class Agent:

    def __init__(self, start_x: int, start_y: int) -> None:

        """ 座標 """
        self.__x__: int = start_x
        self.__y__: int = start_y

        self.__steps__: int = 0

    def step(self, q_table: List[List[List[float]]]) -> None:
        self.__x__ -= 1


        self.__steps__ += 1


    def get_here(self, maze: List[str]) -> str:
        return maze[self.__y__][self.__x__]

    def get_position(self) -> tuple[int, int]:
        return self.__x__, self.__y__
    
    def get_steps(self) -> int:
        return self.__steps__


    

    