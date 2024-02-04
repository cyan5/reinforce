from typing import List, Tuple
from Agent import Agent

def get_point(maze: List[str], chara: str) -> Tuple[int, int]:
    """
    
    """
    let_x: int = -1
    let_y: int = -1
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == chara:
                let_x = x
                let_y = y
                break
    if let_x == -1 or let_y == -1:
        print("chara '{chara}' not found")
        exit(1)
    return let_x, let_y

def agent_end(agent: Agent, maze: List[str]) -> bool:
    """
    学習の終了条件
    100ステップ経過する、またはG#-いずれかのマスに止まる
    """
    if agent.get_steps() > 100:
        return True
    elif agent.get_here(maze) in 'G#-':
        return True
    else:
        return False

def reward(agent: Agent, maze: List[str]) -> float:
    score: float = 0.0
    if agent.get_here(maze) == 'G':
        score += 100.0
    if agent.get_here(maze) in '-#':
        score -= 100.0
    score -= float(agent.get_steps())

    return score

def print_maze(maze: List[str]):
    for row in maze:
        print(row)
    print()