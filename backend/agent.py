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

        self.game_over = False
        self.result = "Playing"

        self.place_hazards()

    # ------------------------
    # PLACE PITS + WUMPUS + GOLD
    # ------------------------
    def place_hazards(self):
        # Pits
        for i in range(self.rows):
            for j in range(self.cols):
                if (i, j) != (0, 0):
                    if random.random() < 0.2:
                        self.grid[i][j] = 'P'

        # Wumpus
        while True:
            x = random.randint(0, self.rows - 1)
            y = random.randint(0, self.cols - 1)
            if (x, y) != (0, 0) and self.grid[x][y] == '':
                self.grid[x][y] = 'W'
                break

        # Gold
        while True:
            x = random.randint(0, self.rows - 1)
            y = random.randint(0, self.cols - 1)
            if (x, y) != (0, 0) and self.grid[x][y] == '':
                self.grid[x][y] = 'G'
                break

    # ------------------------
    # NEIGHBORS
    # ------------------------
    def get_neighbors(self, x, y):
        moves = [(1,0), (-1,0), (0,1), (0,-1)]
        neighbors = []

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols:
                neighbors.append((nx, ny))

        return neighbors

    # ------------------------
    # MOVE FUNCTION (FIXED INDENTATION)
    # ------------------------
    def move(self):
        if self.game_over:
            return

        self.visited.add(self.pos)

        x, y = self.pos

        # PIT
        if self.grid[x][y] == 'P':
            self.game_over = True
            self.result = "Fell into Pit 💀"
            return

        # WUMPUS
        if self.grid[x][y] == 'W':
            self.game_over = True
            self.result = "Killed by Wumpus 👹"
            return

        # GOLD
        if self.grid[x][y] == 'G':
            self.game_over = True
            self.result = "Found Gold 🎉"
            return

        # MOVE LOGIC
        moved = False
        for n in self.get_neighbors(x, y):
            if n not in self.visited:
                self.pos = n
                moved = True
                break

        # if stuck → stop
        if not moved:
            self.game_over = True
            self.result = "No moves left 😐"

        self.inference_steps += 1

    # ------------------------
    # STATE FOR FRONTEND
    # ------------------------
    def get_state(self):
        return {
            "position": self.pos,
            "visited": list(self.visited),
            "safe": list(self.safe),
            "steps": self.inference_steps,
            "grid": self.grid,
            "game_over": self.game_over,
            "result": self.result
        }