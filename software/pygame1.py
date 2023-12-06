import pygame
import sys
import json

class RobotGame:
    def __init__(self):
        pygame.init()

        # Define colors
        self.WHITE = (246, 246, 246)
        self.BLACK = (0, 0, 0)

        # Grid size
        self.GRID_SIZE = 50

    def load_images(self):
        images = {}
        for piece in ["2", "3", "5", "7", "11"]:
            img_path = f"./software/GridWorldModel/images/{piece}.png"
            image = pygame.image.load(img_path)
            image = pygame.transform.scale(image, (self.GRID_SIZE, self.GRID_SIZE))
            images[piece] = image
        return images

    def draw_grid(self, screen, num_rows, num_columns):
        for x in range(0, num_columns * self.GRID_SIZE, self.GRID_SIZE):
            pygame.draw.line(screen, self.BLACK, (x, 0), (x, num_rows * self.GRID_SIZE))
        for y in range(0, num_rows * self.GRID_SIZE, self.GRID_SIZE):
            pygame.draw.line(screen, self.BLACK, (0, y), (num_columns * self.GRID_SIZE, y))

    def draw_pieces(self, screen, matrix, images):
        for index_i, row in enumerate(matrix):
            for index_j, piece in enumerate(row):
                if piece != "0":
                    screen.blit(images.get(piece, images["2"]), (index_j * self.GRID_SIZE, index_i * self.GRID_SIZE))

    def move_robot(self, matrix, from_pos, to_pos, door_info):
        current_piece = matrix[from_pos[0]][from_pos[1]]

        if 0 <= to_pos[0] < len(matrix) and 0 <= to_pos[1] < len(matrix[0]):
            target_piece = matrix[to_pos[0]][to_pos[1]]

            if current_piece == "11":
                if target_piece == "3":
                    matrix[to_pos[0]][to_pos[1]] = current_piece
                    matrix[from_pos[0]][from_pos[1]] = "0"
                elif target_piece == "0":
                    matrix[to_pos[0]][to_pos[1]] = current_piece
                    matrix[from_pos[0]][from_pos[1]] = "0"
                else:
                    matrix[from_pos[0]][from_pos[1]] = current_piece

    def initialize_game(self):
        with open('./environmentBackup.json', 'r') as input_file:
            data = json.load(input_file)
            matrix = data["grid"]
            door_info = data.get("door", {})

        num_rows = len(matrix)
        num_columns = len(matrix[0]) if num_rows > 0 else 0

        WINDOW_WIDTH = num_columns * self.GRID_SIZE
        WINDOW_HEIGHT = num_rows * self.GRID_SIZE

        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Interface with Mobile Image")

        images = self.load_images()

        return screen, matrix, door_info, num_rows, num_columns, images

    def run_game(self):
        robot_pos = [10, 11]  # Initial robot position

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                new_pos = [robot_pos[0] - 1, robot_pos[1]]
                self.move_robot(matrix, robot_pos, new_pos, door_info)
                robot_pos = new_pos
            elif keys[pygame.K_DOWN]:
                new_pos = [robot_pos[0] + 1, robot_pos[1]]
                self.move_robot(matrix, robot_pos, new_pos, door_info)
                robot_pos = new_pos
            elif keys[pygame.K_LEFT]:
                new_pos = [robot_pos[0], robot_pos[1] - 1]
                self.move_robot(matrix, robot_pos, new_pos, door_info)
                robot_pos = new_pos
            elif keys[pygame.K_RIGHT]:
                new_pos = [robot_pos[0], robot_pos[1] + 1]
                self.move_robot(matrix, robot_pos, new_pos, door_info)
                robot_pos = new_pos

            for index_i, row in enumerate(matrix):
                for index_j, piece in enumerate(row):
                    pygame.draw.rect(screen, self.WHITE, (index_j * self.GRID_SIZE, index_i * self.GRID_SIZE, self.GRID_SIZE, self.GRID_SIZE))

            self.draw_grid(screen, num_rows, num_columns)
            self.draw_pieces(screen, matrix, images)
            pygame.display.flip()
            pygame.time.Clock().tick(10)

if __name__ == "__main__":
    game = RobotGame()
    screen, matrix, door_info, num_rows, num_columns, images = game.initialize_game()
    game.run_game()
