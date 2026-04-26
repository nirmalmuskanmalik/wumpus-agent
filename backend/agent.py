import random

class WumpusAgent:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.pos = (0, 0)

        self.inference_steps = 0
        self.grid = [['' for _ in range(cols)] for _ in range(rows)]
        self.visited = set()
        self.safe = set()

        self.place_hazards()

        self.game_over = False
        self.result = "Playing"

    def place_hazards(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if (i, j) != (0, 0):
                    if random.random() < 0.2:
                        self.grid[i][j] = 'P'

        # Place Wumpus
        while True:
            x = random.randint(0, self.rows - 1)
            y = random.randint(0, self.cols - 1)
            if (x, y) != (0, 0):
                self.grid[x][y] = 'W'
                break

                # Place Gold
while True:
    x = random.randint(0, self.rows - 1)
    y = random.randint(0, self.cols - 1)
    if (x, y) != (0, 0) and self.grid[x][y] == '':
        self.grid[x][y] = 'G'
        break

    def get_neighbors(self, x, y):
        moves = [(1,0),(-1,0),(0,1),(0,-1)]
        neighbors = []

        for dx, dy in moves:
            nx, ny = x+dx, y+dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols:
                neighbors.append((nx, ny))

        return neighbors

    def perceive(self):
        x, y = self.pos
        percepts = []

        for nx, ny in self.get_neighbors(x, y):
            if self.grid[nx][ny] == 'P':
                percepts.append('Breeze')
            if self.grid[nx][ny] == 'W':
                percepts.append('Stench')

        return percepts
    
    def move(self):
    if self.game_over:
        return

    self.visited.add(self.pos)

    x, y = self.pos

    # Check current cell
    if self.grid[x][y] == 'P':
        self.game_over = True
        self.result = "Fell into Pit 💀"
        return

    if self.grid[x][y] == 'W':
        self.game_over = True
        self.result = "Killed by Wumpus 👹"
        return

    if self.grid[x][y] == 'G':
        self.game_over = True
        self.result = "Found Gold 🎉"
        return

    # Move to next safe/unvisited
    for n in self.get_neighbors(x, y):
        if n not in self.visited:
            self.pos = n
            break

    self.inference_steps += 1

    def get_state(self):
        return {
            "position": self.pos,
            "visited": list(self.visited),
            "safe": list(self.safe),
            "percepts": self.perceive(),
            "steps": self.inference_steps,
            "grid": self.grid
        }