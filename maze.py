from typing import List
import Global as G
import function as func
from Agent import Agent

def main():

    # マップ生成
    # 縦10 x 横20 のマップ
    # SからスタートしてGに辿り着く
    # -は壁、#は崖
    maze: List[str] = [
        "####################",
        "#                  #",
        "#    G             #",
        "#   ------------   #",
        "#       -          #",
        "#       -          #",
        "#       -     S    #",
        "#       -          #",
        "#                  #",
        "####################",
    ]
    func.print_maze(maze)

    """ スタートとゴールの座標 """

    start_x: int
    start_y: int
    goal_x: int
    goal_y: int
    
    start_x, start_y = func.get_point(maze, 'S')
    goal_x, goal_y = func.get_point(maze, 'G')

    print(f"start: ({start_x}, {start_y})")
    print(f"goal : ({goal_x}, {goal_y})")


    """ Q値のテーブルを生成 """

    q_table: List[List[List[float]]] = [[[0. for _ in range(len(maze[0]))] for _ in range(len(maze))] for _ in range(4)]

    for i in range(len(q_table)):
        for j in range(len(q_table)):
            print(q_table[i][j])
        print()
    print()


    """ 学習開始 """

    print("Learning in Progress ...")

    for _ in range(G.TIMES_LEARNING):

        agent: Agent = Agent(start_x, start_y)

        while True:
            agent.step(q_table)



            reward: float = func.reward(agent, maze)
            print(reward)


            if func.agent_end(agent, maze):
                break

    print("Done!")

    """ 学習結果 """

    print()




















if __name__ == '__main__':
    main()