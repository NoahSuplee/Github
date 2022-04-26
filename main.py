import pygame
import os
import sys
import time

print('test')

pygame.init()
pygame.display.set_caption('chess')
width, height = 400, 400
size = (width, height)
CLOCK = pygame.time.Clock()
FPS = 60

screen = pygame.display.set_mode(size)

title_screen = pygame.transform.scale(pygame.image.load(os.path.join('stuff', 'Title Screen.png')), (400,400))

rook = pygame.transform.scale(pygame.image.load(os.path.join('stuff', 'rook.png')), (50,50))

rook_2 = pygame.transform.scale(pygame.image.load(os.path.join('stuff', 'rook 2.png')), (50,50))

horse = pygame.transform.scale(pygame.image.load(os.path.join('stuff', 'horse.png')), (50,50))

horse_2 = pygame.transform.scale(pygame.image.load(os.path.join('stuff', 'horse 2.png')), (50,50))

bishop = pygame.transform.scale(pygame.image.load(os.path.join('stuff', 'bishop.png')), (50,50))

bishop_2 = pygame.transform.scale(pygame.image.load(os.path.join('stuff', 'bishop 2.png')), (50,50))

king = pygame.transform.scale(pygame.image.load(os.path.join('stuff', 'king.png')), (50,50))

king_2 = pygame.transform.scale(pygame.image.load(os.path.join('stuff', 'king 2.png')), (50,50))

queen = pygame.transform.scale(pygame.image.load(os.path.join('stuff', 'queen.png')), (50,50))

queen_2 = pygame.transform.scale(pygame.image.load(os.path.join('stuff', 'queen 2.png')), (50,50))

pawn = pygame.transform.scale(pygame.image.load(os.path.join('stuff', 'pawn.png')), (50,50))

pawn_2 = pygame.transform.scale(pygame.image.load(os.path.join('stuff', 'pawn 2.png')), (50,50))

class Button:
  def __init__(self, x, y, width, height):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
  
  def onButton(self, pos):
    if pos[0] >= self.x and pos[0] <= self.x + self.width and pos[1] >= self.y and pos[1] <= self.y + self.height:
      return True

class Pawns():
  def __init__(self, coord, piece, image, points, en_passantable, id):
    self.coord = coord
    self.piece = piece
    self.image = image
    self.points = points
    self.en_passantable = en_passantable
    self.id = id

  def legal_movement(self, coord, turn, board, auto=0):
    self.__moves = []
    self.__auto = []
    if turn % 2 == 0:
      try:
        if board[coord[0] - 1][coord[1]] == ' ':
          if auto == 0:
            if not pinning(self, turn, (coord[0]-1, coord[1])):
              self.__moves.append((coord[0]-1, coord[1]))
          else:
            self.__auto.append((coord[0]-1, coord[1]))
        if self.coord[0] == 6:
          if board[coord[0] - 1][coord[1]] == ' ' and board[coord[0] - 2][coord[1]] == ' ':
            if auto == 0:
              if not pinning(self, turn, (coord[0]-2, coord[1])):
                self.__moves.append((coord[0] - 2, coord[1]))
            else:
              self.__auto.append((coord[0] - 2, coord[1]))
      except:
        pass
      try:
        if board[coord[0] - 1][coord[1] + 1].upper() == board[coord[0] - 1][coord[1] + 1] and board[coord[0] - 1][coord[1] + 1] != ' ':
          if auto == 0:
            if not pinning(self, turn, (coord[0]-1, coord[1] + 1)):
              self.__moves.append((coord[0] - 1, coord[1] + 1)) 
          else:
            self.__auto.append((coord[0] - 1, coord[1] + 1))

      except:
        pass
      try:
        if board[coord[0] - 1][coord[1] - 1].upper() == board[coord[0] - 1][coord[1] - 1] and board[coord[0] - 1][coord[1] - 1] != ' ' and coord[1] - 1 >= 0:
          if auto == 0:
            if not pinning(self, turn, (coord[0]-1, coord[1]-1)):
              self.__moves.append((coord[0] - 1, coord[1] - 1))
          else:
            self.__auto.append((coord[0] - 1, coord[1] - 1))

      except:
        pass
      try:
        if board[coord[0]][coord[1] + 1] == 'P':
          for i in range(len(bpieces)):
            try:
                if bpieces[i].en_passantable and bpieces[i].coord == (coord[0], coord[1] + 1):
                  if auto == 0:
                    if not pinning(self, turn, (coord[0]-1, coord[1] + 1)):
                      self.__moves.append((coord[0] - 1, coord[1] + 1))
                  else:
                    self.__auto.append((coord[0] - 1, coord[1] + 1))

            except:
              pass
      except:
        pass
      try:
        if board[coord[0]][coord[1] - 1] == 'P':
          for i in range(len(bpieces)):
            try:
              if bpieces[i].en_passantable and bpieces[i].coord == (coord[0], coord[1] - 1):
                if auto == 0:
                  if not pinning(self, turn, (coord[0]-1, coord[1] - 1)):
                    self.__moves.append((coord[0] - 1, coord[1] - 1))
                else:
                  self.__auto.append((coord[0] - 1, coord[1] - 1))
            except:
              pass
      except:
        pass
    else:
      try:
        if board[coord[0] + 1][coord[1]] == ' ':
          if auto == 0:
            if not pinning(self, turn, (coord[0] + 1, coord[1])):
              self.__moves.append((coord[0] + 1, coord[1]))
          else:
            self.__auto.append((coord[0] + 1, coord[1]))
        if self.coord[0] == 1:
          if board[coord[0] + 1][coord[1]] == ' ' and board[coord[0] + 2][coord[1]] == ' ':
            if auto == 0:
              if not pinning(self, turn, (coord[0] + 2, coord[1])):
                self.__moves.append((coord[0] + 2, coord[1]))
            else:
              self.__auto.append((coord[0] + 2, coord[1]))
      except:
        pass

      try:
        if board[coord[0] + 1][coord[1] + 1].lower() == board[coord[0] + 1][coord[1] + 1] and board[coord[0] + 1][coord[1] + 1] != ' ':
          if auto == 0:
            if not pinning(self, turn, (coord[0] + 1, coord[1] + 1)):
              self.__moves.append((coord[0] + 1, coord[1] + 1)) 
          else:
            self.__auto.append((coord[0] + 1, coord[1] + 1))
      except:
        pass
        
      try:
        if board[coord[0] + 1][coord[1] - 1].lower() == board[coord[0] + 1][coord[1] - 1] and board[coord[0] + 1][coord[1] - 1] != ' ' and coord[1] - 1 >= 0:
          if auto == 0:
            if not pinning(self, turn, (coord[0] + 1, coord[1] - 1)):
              self.__moves.append((coord[0] + 1, coord[1] - 1))
          else:
            self.__auto.append((coord[0] + 1, coord[1] - 1))
      except:
        pass
      try:
        if board[coord[0]][coord[1] + 1] == 'p':
          for i in range(len(wpieces)):
            try:
              if wpieces[i].en_passantable and wpieces[i].coord == (coord[0], coord[1] + 1):
                if auto == 0:
                  if not pinning(self, turn, (coord[0] + 1, coord[1] + 1)):
                    self.__moves.append((coord[0] + 1, coord[1] + 1))
                else:
                  self.__auto.append((coord[0] + 1, coord[1] + 1))
            except:
              pass
      except:
        pass
      try:
        if board[coord[0]][coord[1] - 1] == 'p':
          for i in range(len(wpieces)):
            try:

              if wpieces[i].en_passantable and wpieces[i].coord == (coord[0], coord[1] - 1):
                if auto == 0:
                  if not pinning(self, turn, (coord[0] + 1, coord[1] - 1)):
                    self.__moves.append((coord[0] + 1, coord[1] - 1))
                else:
                  self.__auto.append((coord[0] + 1, coord[1] - 1))
            except:
              pass
      except:
        pass

    if auto == 0:
      for i in range(len(self.__moves)):
        if turn % 2 == 0:
          try:
            if board[self.__moves[i][0]][self.__moves[i][1]].lower() == board[self.__moves[i][0]][self.__moves[i][1]] and board[self.__moves[i][0]][self.__moves[i][1]] != ' ':
              self.__moves.remove(self.__moves[i])
          except:
            pass
        else:
          try:
            if board[self.__moves[i][0]][self.__moves[i][1]].upper() == board[self.__moves[i][0]][self.__moves[i][1]] and board[self.__moves[i][0]][self.__moves[i][1]] != ' ':
              self.__moves.remove(self.__moves[i])
          except:
            pass
      return self.__moves
    else:
      return self.__auto

  def move_piece(self, coord, new_coord, turn, board):
    if new_coord in self.legal_movement(coord, turn, board):
      chess_board[coord[0]][coord[1]] = ' '
      if turn % 2 == 0:
        for i in range(len(bpieces)):
          if bpieces[i].coord == new_coord:
            bpieces[i].coord = None
            bpieces[i].image = None
            trash_can.append(bpieces[i])
        
        try:
          if chess_board[coord[0]][coord[1] + 1] == 'P' and new_coord[0] == 2 and coord[0] != new_coord[0]:
            chess_board[coord[0]][coord[1] + 1] = ' '
            for i in range(len(bpieces)):
              print(bpieces[i].coord, (new_coord[0], new_coord[1]), 'test')
              if bpieces[i].coord == (new_coord[0] + 1, new_coord[1]) and bpieces[i].en_passantable:
                bpieces[i].coord = None
                bpieces[i].image = None
                trash_can.append(bpieces[i])
        except:
          pass
        try:
          if chess_board[coord[0]][coord[1] - 1] == 'P' and new_coord[0] == 2 and coord[0] != new_coord[0]:
            chess_board[coord[0]][coord[1] - 1] = ' '
            for i in range(len(bpieces)):
              print(bpieces[i].coord, (new_coord[0], new_coord[1]), 'test')
              if bpieces[i].coord == (new_coord[0] + 1, new_coord[1]) and bpieces[i].en_passantable:
                bpieces[i].coord = None
                bpieces[i].image = None
                trash_can.append(bpieces[i])
        except:
          pass

      else:
        for i in range(len(wpieces)):
          if wpieces[i].coord == new_coord:
            wpieces[i].coord = None
            wpieces[i].image = None
            trash_can.append(wpieces[i])
        try:
          if chess_board[coord[0]][coord[1] + 1] == 'p' and new_coord[0] == 5 and coord[0] != new_coord[0]:
            chess_board[coord[0]][coord[1] + 1] = ' '
            for i in range(len(wpieces)):
              print(wpieces[i].coord, (new_coord[0], new_coord[1]), 'test')
              if wpieces[i].coord == (new_coord[0] - 1, new_coord[1]) and wpieces[i].en_passantable:
                wpieces[i].coord = None
                wpieces[i].image = None
                trash_can.append(wpieces[i])
        except:
          pass
        try:
          if chess_board[coord[0]][coord[1] - 1] == 'p' and new_coord[0] == 5 and coord[0] != new_coord[0]:
            chess_board[coord[0]][coord[1] - 1] = ' '
            for i in range(len(wpieces)):
              print(wpieces[i].coord, (new_coord[0], new_coord[1]), 'test')
              if wpieces[i].coord == (new_coord[0] - 1, new_coord[1]) and wpieces[i].en_passantable:
                wpieces[i].coord = None
                wpieces[i].image = None
        except:
          pass

      chess_board[new_coord[0]][new_coord[1]] = self.piece
      self.coord = new_coord
      if self.coord[0] == 0 and turn % 2 == 0:
        print('aaa')
        self.promotion(turn)
      elif self.coord[0] == 7 and turn % 2 != 0:
        self.promotion(turn)
      try:
        print(coord)
        if coord[0] == 6 and new_coord[0] == 4 and turn % 2 == 0:
          self.en_passantable = True
        elif coord[0] == 1 and new_coord[0] == 3 and turn % 2 != 0:
          self.en_passantable = True
        else:
          self.en_passantable = False
      except:
        pass
      return True
    else:
      return False

  def promotion(self, turn):
    while True:
      CLOCK.tick(FPS)
      pos = pygame.mouse.get_pos()
      for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
          sys.exit()
      if turn % 2 == 0:
        square = translate_coord2board(self.coord)
        screen.blit(queen, (square[0], square[1] + 50))
        queen_button = Button(square[0], square[1] + 50, 50, 50)
        square = translate_coord2board(self.coord)
        screen.blit(rook, (square[0], square[1] + 100))
        rook_button = Button(square[0], square[1] + 100, 50, 50)
        square = translate_coord2board(self.coord)
        screen.blit(bishop, (square[0], square[1] + 150))
        bishop_button = Button(square[0], square[1] + 150, 50, 50)
        square = translate_coord2board(self.coord)
        screen.blit(horse, (square[0], square[1] + 200))
        horse_button = Button(square[0], square[1] + 200, 50, 50)

        if queen_button.onButton(pos) and pygame.mouse.get_pressed(3) == (1,0,0):
          for i in range(len(wpieces)):
            if wpieces[i].id == self.id:
              wpieces[i] = Queens(self.coord, 'q', queen, 90, wpieces[i].id)
              break
          break
        elif rook_button.onButton(pos) and pygame.mouse.get_pressed(3) == (1,0,0):
          for i in range(len(wpieces)):
            if wpieces[i].id == self.id:
              wpieces[i] = Rooks(self.coord, 'r', rook, 50, wpieces[i].id)
              break
          break
        elif bishop_button.onButton(pos) and pygame.mouse.get_pressed(3) == (1,0,0):
          for i in range(len(wpieces)):
            if wpieces[i].id == self.id:
              wpieces[i] = Bishops(self.coord, 'b', bishop, 30, wpieces[i].id)
              break
          break
        elif horse_button.onButton(pos) and pygame.mouse.get_pressed(3) == (1,0,0):
          for i in range(len(wpieces)):
            if wpieces[i].id == self.id:
              wpieces[i] = Horses(self.coord, 'h', horse, 30, wpieces[i].id)
            break
          break
        pygame.display.update()
        
      else:
        square = translate_coord2board(self.coord)
        screen.blit(queen_2, (square[0], square[1] - 50))
        queen_button = Button(square[0], square[1] - 50, 50, 50)
        square = translate_coord2board(self.coord)
        screen.blit(rook_2, (square[0], square[1] - 100))
        rook_button = Button(square[0], square[1] - 100, 50, 50)
        square = translate_coord2board(self.coord)
        screen.blit(bishop_2, (square[0], square[1] - 150))
        bishop_button = Button(square[0], square[1] - 150, 50, 50)
        square = translate_coord2board(self.coord)
        screen.blit(horse_2, (square[0], square[1] - 200))
        horse_button = Button(square[0], square[1]- 200, 50, 50)

        if queen_button.onButton(pos) and pygame.mouse.get_pressed(3) == (1,0,0):
          for i in range(len(bpieces)):
            if bpieces[i].id == self.id:
              bpieces[i] = Queens(self.coord, 'Q', queen_2, -90, bpieces[i].id)
              break
          break
        elif rook_button.onButton(pos) and pygame.mouse.get_pressed(3) == (1,0,0):
          for i in range(len(bpieces)):
            if bpieces[i].id == self.id:
              bpieces[i] = Rooks(self.coord, 'R', rook_2, -50, bpieces[i].id)
            break
          break
        elif bishop_button.onButton(pos) and pygame.mouse.get_pressed(3) == (1,0,0):
          for i in range(len(bpieces)):
            if bpieces[i].id == self.id:
              bpieces[i] = Bishops(self.coord, 'B', bishop_2, -30, bpieces[i].id)
            break
          break
        elif horse_button.onButton(pos) and pygame.mouse.get_pressed(3) == (1,0,0):
          for i in range(len(bpieces)):
            if bpieces[i].id == self.id:
              bpieces[i] = Horses(self.coord, 'Q', horse_2, -30, bpieces[i].id)
            break
          break
        pygame.display.update()

class Bishops:
  def __init__(self, coord, piece, image, points, id):
    self.coord = coord
    self.piece = piece
    self.image = image
    self.points = points
    self.id = id

  def legal_movement(self, coord, turn, board, auto=0):
    self.__moves = []
    self.__auto = []
    if turn % 2 == 0:
      # up right
      for i in range(1,8):
        try:
          if board[coord[0] - i][coord[1] + i] == ' ' and coord[0] - i >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] - i, coord[1] + i)):
                self.__moves.append((coord[0] - i, coord[1] + i))
            else:
              self.__auto.append((coord[0] - i, coord[1] + i))
          elif board[coord[0] - i][coord[1] + i].upper() == board[coord[0] - i][coord[1] + i] and coord[0] - i >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] - i, coord[1] + i)):
                self.__moves.append((coord[0] - i, coord[1] + i))
                break
            else:
              self.__auto.append((coord[0] - i, coord[1] + i))
              break
          else:
            break
        except:
          pass
      # up left
      for i in range(1,8):
        try:
          if board[coord[0] - i][coord[1] - i] == ' ' and coord[1] >= 0 and coord[0] - i >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] - i, coord[1] - i)):
                self.__moves.append((coord[0] - i, coord[1] - i))
            else:
              self.__auto.append((coord[0] - i, coord[1] - i))
          elif board[coord[0] - i][coord[1] - i].upper() == board[coord[0] - i][coord[1] - i] and coord[1] >= 0 and coord[0] - i >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] - i, coord[1] - i)):
                self.__moves.append((coord[0] - i, coord[1] - i))
                break
            else:
              self.__auto.append((coord[0] - i, coord[1] - i))
              break
          else:
            break
        except:
          pass
      # down right
      for i in range(1,8):
        try:
          if board[coord[0] + i][coord[1] + i] == ' ' and coord[0] >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] + i, coord[1] + i)):
                self.__moves.append((coord[0] + i, coord[1] + i))
            else:
              self.__auto.append((coord[0] + i, coord[1] + i))

          elif board[coord[0] + i][coord[1] + i].upper() == board[coord[0] + i][coord[1] + i] and coord[0] >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] + i, coord[1] + i)):
                self.__moves.append((coord[0] + i, coord[1] + i))
                break
            else:
              self.__auto.append((coord[0] + i, coord[1] + i))
              break
          else:
            break
        except:
          pass
      # down left
      for i in range(1,8):
        try:
          if board[coord[0] + i][coord[1] - i] == ' ' and coord[1] >= 0 and coord[0] >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] + i, coord[1] - i)):
                self.__moves.append((coord[0] + i, coord[1] - i))
            else:
              self.__auto.append((coord[0] + i, coord[1] - i))
          elif board[coord[0] + i][coord[1] - i].upper() == board[coord[0] + i][coord[1] - i] and coord[1] >= 0 and coord[0] - i >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] + i, coord[1] - i)):
                self.__moves.append((coord[0] + i, coord[1] - i))
                break
            else:
              self.__auto.append((coord[0] + i, coord[1] - i))
              break
          else:
            break
        except:
          pass
    else:
      # up right
      for i in range(1,8):
        try:
          if board[coord[0] - i][coord[1] + i] == ' ' and coord[0] - i >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] - i, coord[1] + i)):
                self.__moves.append((coord[0] - i, coord[1] + i))
            else:
              self.__auto.append((coord[0] - i, coord[1] + i))
          elif board[coord[0] - i][coord[1] + i].lower() == board[coord[0] - i][coord[1] + i]:
            if auto == 0:
              if not pinning(self, turn, (coord[0] - i, coord[1] + i)):
                self.__moves.append((coord[0] - i, coord[1] + i))
                break
            else:
              self.__auto.append((coord[0] - i, coord[1] + i))
              break
          else:
            break
        except:
          pass
      # up left
      for i in range(1,8):
        try:
          if board[coord[0] - i][coord[1] - i] == ' ' and coord[1] >= 0 and coord[0] - i >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] - i, coord[1] - i)):
                self.__moves.append((coord[0] - i, coord[1] - i))
            else:
              self.__auto.append((coord[0] - i, coord[1] - i))
          elif board[coord[0] - i][coord[1] - i].lower() == board[coord[0] - i][coord[1] - i] and coord[1] >= 0 and coord[0] >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] - i, coord[1] - i)):
                self.__moves.append((coord[0] - i, coord[1] - i))
                break
            else:
              self.__auto.append((coord[0] - i, coord[1] - i))
              break
          else:
            break
        except:
          pass
      # down right
      for i in range(1,8):
        try:
          if board[coord[0] + i][coord[1] + i] == ' ' and coord[0] >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] + i, coord[1] + i)):
                self.__moves.append((coord[0] + i, coord[1] + i))
            else:
              self.__auto.append((coord[0] + i, coord[1] + i))
          elif board[coord[0] + i][coord[1] + i].lower() == board[coord[0] + i][coord[1] + i] and coord[0] >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] + i, coord[1] + i)):
                self.__moves.append((coord[0] + i, coord[1] + i))
                break
            else:
              self.__auto.append((coord[0] + i, coord[1] + i))
              break
          else:
            break
        except:
          pass
      # down left
      for i in range(1,8):
        try:
          if board[coord[0] + i][coord[1] - i] == ' ' and coord[1] >= 0 and coord[0] >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] + i, coord[1] - i)):
                self.__moves.append((coord[0] + i, coord[1] - i))
            else:
              self.__auto.append((coord[0] + i, coord[1] - i))
          elif board[coord[0] + i][coord[1] - i].lower() == board[coord[0] + i][coord[1] - i] and coord[1] >= 0 and coord[0] >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] + i, coord[1] - i)):
                self.__moves.append((coord[0] + i, coord[1] - i))
                break
            else:
              self.__auto.append((coord[0] + i, coord[1] - i))
              break
          else:
            break
        except:
          pass
    if auto == 0:
      return self.__moves
    else:
      return self.__auto

  def move_piece(self, coord, new_coord, turn, board):
    if new_coord in self.legal_movement(coord, turn, board):
      chess_board[coord[0]][coord[1]] = ' '
      if turn % 2 == 0:
        for i in range(len(bpieces)):
          if bpieces[i].coord == new_coord:
            bpieces[i].coord = None
            bpieces[i].image = None
            trash_can.append(bpieces[i])
      else:
        for i in range(len(wpieces)):
          if wpieces[i].coord == new_coord:
            wpieces[i].coord = None
            wpieces[i].image = None
            trash_can.append(wpieces[i])
      chess_board[new_coord[0]][new_coord[1]] = self.piece
      self.coord = new_coord
      return True
    else:
      return False

class Horses:
  def __init__(self, coord, piece, image, points, id):
    self.coord = coord
    self.piece = piece
    self.image = image
    self.points = points
    self.id = id

  def legal_movement(self, coord, turn, board, auto=0):
    self.__moves = []
    self.__auto = []
    if turn % 2 == 0:
      # up 2 left 1
      try:
        if board[coord[0] - 2][coord[1] - 1] == ' ' and coord[0] - 2 >= 0 and coord[1] - 1 >= 0:
          if auto == 0:
            if not pinning(self, turn, (coord[0] - 2, coord[1] - 1)):
              self.__moves.append((coord[0] - 2, coord[1] - 1))
          else:
            self.__auto.append((coord[0] - 2, coord[1] - 1))
        elif board[coord[0] - 2][coord[1] - 1].upper() == board[coord[0] - 2][coord[1] - 1] and coord[0] - 2 >= 0 and coord[1] - 1 >= 0:
          if auto == 0:
            if not pinning(self, turn, (coord[0] - 2, coord[1] - 1)):
              self.__moves.append((coord[0] - 2, coord[1] - 1))
          else:
            self.__auto.append((coord[0] - 2, coord[1] - 1))
        else:
          pass
      except:
        pass
      # up 2 right 1
      try:
        if board[coord[0] - 2][coord[1] + 1] == ' ' and coord[0] - 2 >= 0:
          if auto == 0:
            if not pinning(self, turn, (coord[0] - 2, coord[1] + 1)):
              self.__moves.append((coord[0] - 2, coord[1] + 1))
          else:
            self.__auto.append((coord[0] - 2, coord[1] + 1))
        elif board[coord[0] - 2][coord[1] + 1].upper() == board[coord[0] - 2][coord[1] + 1] and coord[0] - 2 >= 0:
          if auto == 0:
            if not pinning(self, turn, (coord[0] - 2, coord[1] + 1)):
              self.__moves.append((coord[0] - 2, coord[1] + 1))
          else:
            self.__auto.append((coord[0] - 2, coord[1] + 1))
        else:
          pass
      except:
        pass
      # down 2 left 1
      try:
        if board[coord[0] + 2][coord[1] - 1] == ' ' and coord[1] - 1 >= 0:
          if auto == 0:
            if not pinning(self, turn, (coord[0] + 2, coord[1] - 1)):
              self.__moves.append((coord[0] + 2, coord[1] - 1))
          else:
            self.__auto.append((coord[0] + 2, coord[1] - 1))
        elif board[coord[0] + 2][coord[1] - 1].upper() == board[coord[0] + 2][coord[1] - 1] and coord[1] - 1 >= 0:
          if auto == 0:
            if not pinning(self, turn, (coord[0] + 2, coord[1] - 1)):
              self.__moves.append((coord[0] + 2, coord[1] - 1))
          else:
            self.__auto.append((coord[0] + 2, coord[1] - 1))
        else:
          pass
      except:
        pass
      # down 2 right 1
      try:
        if board[coord[0] + 2][coord[1] + 1] == ' ':
          if auto == 0:
            if not pinning(self, turn, (coord[0] + 2, coord[1] + 1)):
              self.__moves.append((coord[0] + 2, coord[1] + 1))
          else:
            self.__auto.append((coord[0] + 2, coord[1] + 1))
        elif board[coord[0] + 2][coord[1] + 1].upper() == board[coord[0] + 2][coord[1] + 1]:
          if auto == 0:
            if not pinning(self, turn, (coord[0] + 2, coord[1] + 1)):
              self.__moves.append((coord[0] + 2, coord[1] + 1))
          else:
            self.__auto.append((coord[0] + 2, coord[1] + 1))
        else:
          pass
      except:
        pass
      # left 2 up 1
      try:
        if board[coord[0] - 1][coord[1] - 2] == ' ' and coord[0] - 1 >= 0 and coord[1] - 2 >= 0:
          if auto == 0:
            if not pinning(self, turn, (coord[0] - 1, coord[1] - 2)):
              self.__moves.append((coord[0] - 1, coord[1] - 2))
          else:
            self.__auto.append((coord[0] - 1, coord[1] - 2))
        elif board[coord[0] - 1][coord[1] - 2].upper() == board[coord[0] - 1][coord[1] - 2] and coord[0] - 1 >= 0 and coord[1] - 2 >= 0:
          if auto == 0:
            if not pinning(self, turn, (coord[0] - 1, coord[1] - 2)):
              self.__moves.append((coord[0] - 1, coord[1] - 2))
          else:
            self.__auto.append((coord[0] - 1, coord[1] - 2))
        else:
          pass
      except:
        pass
      # left 2 down 1
      try:
        if board[coord[0] + 1][coord[1] - 2] == ' ' and coord[1] - 2 >= 0:
          if auto == 0:
            if not pinning(self, turn, (coord[0] + 1, coord[1] - 2)):
              self.__moves.append((coord[0] + 1, coord[1] - 2))
          else:
            self.__auto.append((coord[0] + 1, coord[1] - 2))
        elif board[coord[0] + 1][coord[1] - 2].upper() == board[coord[0] + 1][coord[1] - 2] and coord[1] - 2 >= 0:
          if auto == 0:
            if not pinning(self, turn, (coord[0] + 1, coord[1] - 2)):
              self.__moves.append((coord[0] + 1, coord[1] - 2))
          else:
            self.__auto.append((coord[0] + 1, coord[1] - 2))
        else:
          pass
      except:
        pass
      # right 2 up 1
      try:
        if board[coord[0] - 1][coord[1] + 2] == ' ' and coord[0] - 1>= 0:
          if auto == 0:
            if not pinning(self, turn, (coord[0] - 1, coord[1] + 2)):
              self.__moves.append((coord[0] - 1, coord[1] + 2))
          else:
            self.__auto.append((coord[0] - 1, coord[1] + 2))
        elif board[coord[0] - 1][coord[1] + 2].upper() == board[coord[0] - 1][coord[1] + 2] and coord[0] - 1 >= 0:
          if auto == 0:
            if not pinning(self, turn, (coord[0] - 1, coord[1] + 2)):
              self.__moves.append((coord[0] - 1, coord[1] + 2))
          else:
            self.__auto.append((coord[0] - 1, coord[1] + 2))
        else:
          pass
      except:
        pass
      # right 2 down 1
      try:
        if board[coord[0] + 1][coord[1] + 2] == ' ':
          if auto == 0:
            if not pinning(self, turn, (coord[0] + 1, coord[1] + 2)):
              self.__moves.append((coord[0] + 1, coord[1] + 2))
          else:
            self.__auto.append((coord[0] + 1, coord[1] + 2))
        elif board[coord[0] + 1][coord[1] + 2].upper() == board[coord[0] + 1][coord[1] + 2]:
          if auto == 0:
            if not pinning(self, turn, (coord[0] + 1, coord[1] + 2)):
              self.__moves.append((coord[0] + 1, coord[1] + 2))
          else:
            self.__auto.append((coord[0] + 1, coord[1] + 2))
        else:
          pass
      except:
        pass
    else:
      # up 2 left 1
      try:
        if board[coord[0] - 2][coord[1] - 1] == ' ' and coord[0] - 2 >= 0 and coord[1] - 1 >= 0:
          if auto == 0:
            if not pinning(self, turn, (coord[0] - 2, coord[1] - 1)):
              self.__moves.append((coord[0] - 2, coord[1] - 1))
          else:
            self.__auto.append((coord[0] - 2, coord[1] - 1))
        elif board[coord[0] - 2][coord[1] - 1].lower() == board[coord[0] - 2][coord[1] - 1] and coord[0] - 2 >= 0 and coord[1] - 1 >= 0:
          if auto == 0:
            if not pinning(self, turn, (coord[0] - 2, coord[1] - 1)):
              self.__moves.append((coord[0] - 2, coord[1] - 1))
          else:
            self.__auto.append((coord[0] - 2, coord[1] - 1))
        else:
          pass
      except:
        pass
      # up 2 right 1
      try:
        if board[coord[0] - 2][coord[1] + 1] == ' ' and coord[0] - 2 >= 0:
          if auto == 0:
            if not pinning(self, turn, (coord[0] - 2, coord[1] + 1)):
              self.__moves.append((coord[0] - 2, coord[1] + 1))
          else:
            self.__auto.append((coord[0] - 2, coord[1] + 1))
        elif board[coord[0] - 2][coord[1] + 1].lower() == board[coord[0] - 2][coord[1] + 1] and coord[0] - 2 >= 0:
          if auto == 0:
            if not pinning(self, turn, (coord[0] - 2, coord[1] + 1)):
              self.__moves.append((coord[0] - 2, coord[1] + 1))
          else:
            self.__auto.append((coord[0] - 2, coord[1] + 1))
        else:
          pass
      except:
        pass
      # down 2 left 1
      try:
        if board[coord[0] + 2][coord[1] - 1] == ' ' and coord[1] - 1 >= 0:
          if auto == 0:
            if not pinning(self, turn, (coord[0] + 2, coord[1] - 1)):
              self.__moves.append((coord[0] + 2, coord[1] - 1))
          else:
            self.__auto.append((coord[0] + 2, coord[1] - 1))
        elif board[coord[0] + 2][coord[1] - 1].lower() == board[coord[0] + 2][coord[1] - 1] and coord[1] - 1 >= 0:
          if auto == 0:
            if not pinning(self, turn, (coord[0] + 2, coord[1] - 1)):
              self.__moves.append((coord[0] + 2, coord[1] - 1))
          else:
            self.__auto.append((coord[0] + 2, coord[1] - 1))
        else:
          pass
      except:
        pass
      # down 2 right 1
      try:
        if board[coord[0] + 2][coord[1] + 1] == ' ':
          if auto == 0:
            if not pinning(self, turn, (coord[0] + 2, coord[1] + 1)):
              self.__moves.append((coord[0] + 2, coord[1] + 1))
          else:
            self.__auto.append((coord[0] + 2, coord[1] + 1))
        elif board[coord[0] + 2][coord[1] + 1].lower() == board[coord[0] + 2][coord[1] + 1]:
          if auto == 0:
            if not pinning(self, turn, (coord[0] + 2, coord[1] + 1)):
              self.__moves.append((coord[0] + 2, coord[1] + 1))
          else:
            self.__auto.append((coord[0] + 2, coord[1] + 1))
        else:
          pass
      except:
        pass
      # left 2 up 1
      try:
        if board[coord[0] - 1][coord[1] - 2] == ' ' and coord[0] - 1 >= 0 and coord[1] - 2 >= 0:
          if auto == 0:
            if not pinning(self, turn, (coord[0] - 1, coord[1] - 2)):
              self.__moves.append((coord[0] - 1, coord[1] - 2))
          else:
            self.__auto.append((coord[0] - 1, coord[1] - 2))
        elif board[coord[0] - 1][coord[1] - 2].lower() == board[coord[0] - 1][coord[1] - 2] and coord[0] - 1 >= 0 and coord[1] - 2 >= 0:
          if auto == 0:
            if not pinning(self, turn, (coord[0] - 1, coord[1] - 2)):
              self.__moves.append((coord[0] - 1, coord[1] - 2))
          else:
            self.__auto.append((coord[0] - 1, coord[1] - 2))
        else:
          pass
      except:
        pass
      # left 2 down 1
      try:
        if board[coord[0] + 1][coord[1] - 2] == ' ' and coord[1] - 2 >= 0:
          if auto == 0:
            if not pinning(self, turn, (coord[0] + 1, coord[1] - 2)):
              self.__moves.append((coord[0] + 1, coord[1] - 2))
          else:
            self.__auto.append((coord[0] + 1, coord[1] - 2))
        elif board[coord[0] + 1][coord[1] - 2].lower() == board[coord[0] + 1][coord[1] - 2] and coord[1] - 2 >= 0:
          if auto == 0:
            if not pinning(self, turn, (coord[0] + 1, coord[1] - 2)):
              self.__moves.append((coord[0] + 1, coord[1] - 2))
          else:
            self.__auto.append((coord[0] + 1, coord[1] - 2))
        else:
          pass
      except:
        pass
      # right 2 up 1
      try:
        if board[coord[0] - 1][coord[1] + 2] == ' ' and coord[0] - 1>= 0:
          if auto == 0:
            if not pinning(self, turn, (coord[0] - 1, coord[1] + 2)):
              self.__moves.append((coord[0] - 1, coord[1] + 2))
          else:
            self.__auto.append((coord[0] - 1, coord[1] + 2))
        elif board[coord[0] - 1][coord[1] + 2].lower() == board[coord[0] - 1][coord[1] + 2] and coord[0] - 1 >= 0:
          if auto == 0:
            if not pinning(self, turn, (coord[0] - 1, coord[1] + 2)):
              self.__moves.append((coord[0] - 1, coord[1] + 2))
          else:
            self.__auto.append((coord[0] - 1, coord[1] + 2))
        else:
          pass
      except:
        pass
      # right 2 down 1
      try:
        if board[coord[0] + 1][coord[1] + 2] == ' ':
          if auto == 0:
            if not pinning(self, turn, (coord[0] + 1, coord[1] + 2)):
              self.__moves.append((coord[0] + 1, coord[1] + 2))
          else:
            self.__auto.append((coord[0] + 1, coord[1] + 2))
        elif board[coord[0] + 1][coord[1] + 2].lower() == board[coord[0] + 1][coord[1] + 2]:
          if auto == 0:
            if not pinning(self, turn, (coord[0] + 1, coord[1] + 2)):
              self.__moves.append((coord[0] + 1, coord[1] + 2))
          else:
            self.__auto.append((coord[0] + 1, coord[1] + 2))
        else:
          pass
      except:
        pass
    
    if auto == 0:
      return self.__moves
    else:
      return self.__auto

  def move_piece(self, coord, new_coord, turn, board):
    if new_coord in self.legal_movement(coord, turn, board):
      chess_board[coord[0]][coord[1]] = ' '
      if turn % 2 == 0:
        for i in range(len(bpieces)):
          if bpieces[i].coord == new_coord:
            bpieces[i].coord = None
            bpieces[i].image = None
            trash_can.append(bpieces[i])
      else:
        for i in range(len(wpieces)):
          if wpieces[i].coord == new_coord:
            wpieces[i].coord = None
            wpieces[i].image = None
            trash_can.append(wpieces[i])
      chess_board[new_coord[0]][new_coord[1]] = self.piece
      self.coord = new_coord
      return True
    else:
      return False

class Rooks:
  def __init__(self, coord, piece, image, points, castle, id):
    self.coord = coord
    self.piece = piece
    self.image = image
    self.points = points
    self.castle = castle
    self.id = id

  def legal_movement(self, coord, turn, board, auto=0):
    self.__moves = []
    self.__auto = []
    if turn % 2 == 0:
      # up
      try:
        for i in range(1, 8):
          if board[coord[0] - i][coord[1]] == ' ' and coord[0] - i >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] - i, coord[1])):
                self.__moves.append((coord[0] - i, coord[1]))
            else:
              self.__auto.append((coord[0] - i, coord[1]))
          elif board[coord[0] - i][coord[1]].upper() == board[coord[0] - i][coord[1]] and coord[0] - i >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] - i, coord[1])):
                self.__moves.append((coord[0] - i, coord[1]))
                break
            else:
              self.__auto.append((coord[0] - i, coord[1]))
              break
          else:
            break
      except:
        pass
      # down
      try:
        for i in range(1, 8):
          if board[coord[0] + i][coord[1]] == ' ':
            if auto == 0:
              if not pinning(self, turn, (coord[0] + i, coord[1])):
                self.__moves.append((coord[0] + i, coord[1]))
            else:
              self.__auto.append((coord[0] + i, coord[1]))
          elif board[coord[0] + i][coord[1]].upper() == board[coord[0] + i][coord[1]]:
            if auto == 0:
              if not  pinning(self, turn, (coord[0] + i, coord[1])):
                self.__moves.append((coord[0] + i, coord[1]))
                break
            else:
              self.__auto.append((coord[0] + i, coord[1]))
              break
          else:
            break
      except:
        pass
      # left
      try:
        for i in range(1, 8):
          if board[coord[0]][coord[1] - i] == ' ' and coord[1] - i >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0], coord[1] - i)):
                self.__moves.append((coord[0], coord[1] - i))
            else:
              self.__auto.append((coord[0], coord[1] - i))
          elif board[coord[0]][coord[1] - i].upper() == board[coord[0]][coord[1] - i] and coord[1] - i >= 0:
            if auto == 0:
              if not  pinning(self, turn, (coord[0], coord[1] - i)):
                self.__moves.append((coord[0], coord[1] - i))
                break
            else:
              self.__auto.append((coord[0], coord[1] - i))
              break
          else:
            break
      except:
        pass
      # right
      try:
        for i in range(1, 8):
          if board[coord[0]][coord[1] + i] == ' ':
            if auto == 0:
              if not pinning(self, turn, (coord[0], coord[1] + i)):
                self.__moves.append((coord[0], coord[1] + i))
            else:
              self.__auto.append((coord[0], coord[1] + i))
          elif board[coord[0]][coord[1] + i].upper() == board[coord[0]][coord[1] + i]:
            if auto == 0:
              if not pinning(self, turn, (coord[0], coord[1] + i)):
                self.__moves.append((coord[0], coord[1] + i))
                break
            else:
              self.__auto.append((coord[0], coord[1] + i))
              break
          else:
            break
      except:
        pass
    
    else:
      # up
        try:
          for i in range(1, 8):
            if board[coord[0] - i][coord[1]] == ' ' and coord[0] - i >= 0:
              if auto == 0:
                if not pinning(self, turn, (coord[0] - i, coord[1])):
                  self.__moves.append((coord[0] - i, coord[1]))
              else:
                self.__auto.append((coord[0] - i, coord[1]))
            elif board[coord[0] - i][coord[1]].lower() == board[coord[0] - i][coord[1]] and coord[0] - i >= 0:
              if auto == 0:
                if pinning(self, turn, (coord[0] - i, coord[1])):
                  self.__moves.append((coord[0] - i, coord[1]))
                  break
              else:
                self.__auto.append((coord[0] - i, coord[1]))
                break
            else:
              break
        except:
          pass
        # down
        try:
          for i in range(1, 8):
            if board[coord[0] + i][coord[1]] == ' ':
              if auto == 0:
                if not pinning(self, turn, (coord[0] + i, coord[1])):
                  self.__moves.append((coord[0] + i, coord[1]))
              else:
                self.__auto.append((coord[0] + i, coord[1]))
            elif board[coord[0] + i][coord[1]].lower() == board[coord[0] + i][coord[1]]:
              if auto == 0:
                if not pinning(self, turn, (coord[0] + i, coord[1])):
                  self.__moves.append((coord[0] + i, coord[1]))
                  break
              else:
                self.__auto.append((coord[0] + i, coord[1]))
                break
            else:
              break
        except:
          pass
        # left
        try:
          for i in range(1, 8):
            if board[coord[0]][coord[1] - i] == ' ' and coord[1] - i >= 0:
              if auto == 0:
                if not pinning(self, turn, (coord[0], coord[1] - i)):
                  self.__moves.append((coord[0], coord[1] - i))
              else:
                self.__auto.append((coord[0], coord[1] - i))
            elif board[coord[0]][coord[1] - i].lower() == board[coord[0]][coord[1] - i] and coord[1] - i >= 0:
              if auto == 0:
                if not pinning(self, turn, (coord[0], coord[1] - i)):
                  self.__moves.append((coord[0], coord[1] - i))
                  break
              else:
                self.__auto.append((coord[0], coord[1] - i))
                break
            else:
              break
        except:
          pass
        # right
        try:
          for i in range(1, 8):
            if board[coord[0]][coord[1] + i] == ' ':
              if auto == 0:
                if not pinning(self, turn, (coord[0], coord[1] + i)):
                  self.__moves.append((coord[0], coord[1] + i))
              else:
                self.__auto.append((coord[0], coord[1] + i))
            elif board[coord[0]][coord[1] + i].lower() == board[coord[0]][coord[1] + i]:
              if auto == 0:
                if not pinning(self, turn, (coord[0], coord[1] + i)):
                  self.__moves.append((coord[0], coord[1] + i))
                  break
              else:
                self.__auto.append((coord[0], coord[1] + i))
                break
            else:
              break
        except:
          pass
      
    if auto == 0:
      return self.__moves
    else:
      return self.__auto
  
  def move_piece(self, coord, new_coord, turn, board):
    if new_coord in self.legal_movement(coord, turn, board):
      chess_board[coord[0]][coord[1]] = ' '
      if turn % 2 == 0:
        for i in range(len(bpieces)):
          if bpieces[i].coord == new_coord:
            bpieces[i].coord = None
            bpieces[i].image = None
            trash_can.append(bpieces[i])
      else:
        for i in range(len(wpieces)):
          if wpieces[i].coord == new_coord:
            wpieces[i].coord = None
            wpieces[i].image = None
            trash_can.append(wpieces[i])
      chess_board[new_coord[0]][new_coord[1]] = self.piece
      self.castle = False
      self.coord = new_coord
      return True
    else:
      return False

class Queens:
  def __init__(self, coord, piece, image, points, id):
    self.coord = coord
    self.piece = piece
    self.image = image
    self.points = points
    self.id = id

  def legal_movement(self, coord, turn, board, auto=0):
    self.__moves = []
    self.__auto = []
    if turn % 2 == 0:
      # up right
      for i in range(1,8):
        try:
          if board[coord[0] - i][coord[1] + i] == ' ' and coord[0] - i >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] - i, coord[1] + i)):
                self.__moves.append((coord[0] - i, coord[1] + i))
            else:
              self.__auto.append((coord[0] - i, coord[1] + i))
          elif board[coord[0] - i][coord[1] + i].upper() == board[coord[0] - i][coord[1] + i] and coord[0] - i >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] - i, coord[1] + i)):
                self.__moves.append((coord[0] - i, coord[1] + i))
                break
            else:
              self.__auto.append((coord[0] - i, coord[1] + i))
              break
          else:
            break
        except:
          pass
      # up left
      for i in range(1,8):
        try:
          if board[coord[0] - i][coord[1] - i] == ' ' and coord[1] >= 0 and coord[0] - i >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] - i, coord[1] - i)):
                self.__moves.append((coord[0] - i, coord[1] - i))
            else:
              self.__auto.append((coord[0] - i, coord[1] - i))
          elif board[coord[0] - i][coord[1] - i].upper() == board[coord[0] - i][coord[1] - i] and coord[1] >= 0 and coord[0] - i >= 0 and coord[1] - i >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] - i, coord[1] - i)):
                self.__moves.append((coord[0] - i, coord[1] - i))
                break
            else:
              self.__auto.append((coord[0] - i, coord[1] - i))
              break
          else:
            break
        except:
          pass
      # down right
      for i in range(1,8):
        try:
          if board[coord[0] + i][coord[1] + i] == ' ' and coord[0] >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] + i, coord[1] + i)):
                self.__moves.append((coord[0] + i, coord[1] + i))
            else:
              self.__auto.append((coord[0] + i, coord[1] + i))

          elif board[coord[0] + i][coord[1] + i].upper() == board[coord[0] + i][coord[1] + i] and coord[0] + i >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] + i, coord[1] + i)):
                self.__moves.append((coord[0] + i, coord[1] + i))
                break
            else:
              self.__auto.append((coord[0] + i, coord[1] + i))
              break
          else:
            break
        except:
          pass
      # down left
      for i in range(1,8):
        try:
          if board[coord[0] + i][coord[1] - i] == ' ' and coord[1] >= 0 and coord[0] >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] + i, coord[1] - i)):
                self.__moves.append((coord[0] + i, coord[1] - i))
            else:
              self.__auto.append((coord[0] + i, coord[1] - i))
          elif board[coord[0] + i][coord[1] - i].upper() == board[coord[0] + i][coord[1] - i] and coord[1] - i >= 0 and coord[0] >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] + i, coord[1] - i)):
                self.__moves.append((coord[0] + i, coord[1] - i))
                break
            else:
              self.__auto.append((coord[0] + i, coord[1] - i))
              break
          else:
            break
        except:
          pass
    else:
      # up right
      for i in range(1,8):
        try:
          if board[coord[0] - i][coord[1] + i] == ' ' and coord[0] - i >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] - i, coord[1] + i)):
                self.__moves.append((coord[0] - i, coord[1] + i))
            else:
              self.__auto.append((coord[0] - i, coord[1] + i))
          elif board[coord[0] - i][coord[1] + i].lower() == board[coord[0] - i][coord[1] + i] and  coord[0] - i >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] - i, coord[1] + i)):
                self.__moves.append((coord[0] - i, coord[1] + i))
                break
            else:
              self.__auto.append((coord[0] - i, coord[1] + i))
              break
          else:
            break
        except:
          pass
      # up left
      for i in range(1,8):
        try:
          if board[coord[0] - i][coord[1] - i] == ' ' and coord[1] >= 0 and coord[0] - i >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] - i, coord[1] - i)):
                self.__moves.append((coord[0] - i, coord[1] - i))
            else:
              self.__auto.append((coord[0] - i, coord[1] - i))
          elif board[coord[0] - i][coord[1] - i].lower() == board[coord[0] - i][coord[1] - i] and coord[1] - i >= 0 and coord[0] - i >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] - i, coord[1] - i)):
                self.__moves.append((coord[0] - i, coord[1] - i))
                break
            else:
              self.__auto.append((coord[0] - i, coord[1] - i))
              break
          else:
            break
        except:
          pass
      # down right
      for i in range(1,8):
        try:
          if board[coord[0] + i][coord[1] + i] == ' ' and coord[0] >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] + i, coord[1] + i)):
                self.__moves.append((coord[0] + i, coord[1] + i))
            else:
              self.__auto.append((coord[0] + i, coord[1] + i))
          elif board[coord[0] + i][coord[1] + i].lower() == board[coord[0] + i][coord[1] + i] and coord[0] >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] + i, coord[1] + i)):
                self.__moves.append((coord[0] + i, coord[1] + i))
                break
            else:
              self.__auto.append((coord[0] + i, coord[1] + i))
              break
          else:
            break
        except:
          pass
      # down left
      for i in range(1,8):
        try:
          if board[coord[0] + i][coord[1] - i] == ' ' and coord[1] >= 0 and coord[0] >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] + i, coord[1] - i)):
                self.__moves.append((coord[0] + i, coord[1] - i))
            else:
              self.__auto.append((coord[0] + i, coord[1] - i))
          elif board[coord[0] + i][coord[1] - i].lower() == board[coord[0] + i][coord[1] - i] and coord[1] - i >= 0 and coord[0] >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] + i, coord[1] - i)):
                self.__moves.append((coord[0] + i, coord[1] - i))
                break
            else:
              self.__auto.append((coord[0] + i, coord[1] - i))
              break
          else:
            break
        except:
          pass
    if turn % 2 == 0:
      # up
      try:
        for i in range(1, 8):
          if board[coord[0] - i][coord[1]] == ' ' and coord[0] - i >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] - i, coord[1])):
                self.__moves.append((coord[0] - i, coord[1]))
            else:
              self.__auto.append((coord[0] - i, coord[1]))
          elif board[coord[0] - i][coord[1]].upper() == board[coord[0] - i][coord[1]] and coord[0] - i >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] - i, coord[1])):
                self.__moves.append((coord[0] - i, coord[1]))
                break
            else:
              self.__auto.append((coord[0] - i, coord[1]))
              break
          else:
            break
      except:
        pass
      # down
      try:
        for i in range(1, 8):
          if board[coord[0] + i][coord[1]] == ' ':
            if auto == 0:
              if not pinning(self, turn, (coord[0] + i, coord[1])):
                self.__moves.append((coord[0] + i, coord[1]))
            else:
              self.__auto.append((coord[0] + i, coord[1]))
          elif board[coord[0] + i][coord[1]].upper() == board[coord[0] + i][coord[1]]:
            if auto == 0:
              if not  pinning(self, turn, (coord[0] + i, coord[1])):
                self.__moves.append((coord[0] + i, coord[1]))
                break
            else:
              self.__auto.append((coord[0] + i, coord[1]))
              break
          else:
            break
      except:
        pass
      # left
      try:
        for i in range(1, 8):
          if board[coord[0]][coord[1] - i] == ' ' and coord[1] - i >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0], coord[1] - i)):
                self.__moves.append((coord[0], coord[1] - i))
            else:
              self.__auto.append((coord[0], coord[1] - i))
          elif board[coord[0]][coord[1] - i].upper() == board[coord[0]][coord[1] - i] and coord[1] - i >= 0:
            if auto == 0:
              if not  pinning(self, turn, (coord[0], coord[1] - i)):
                self.__moves.append((coord[0], coord[1] - i))
                break
            else:
              self.__auto.append((coord[0], coord[1] - i))
              break
          else:
            break
      except:
        pass
      # right
      try:
        for i in range(1, 8):
          if board[coord[0]][coord[1] + i] == ' ':
            if auto == 0:
              if not pinning(self, turn, (coord[0], coord[1] + i)):
                self.__moves.append((coord[0], coord[1] + i))
            else:
              self.__auto.append((coord[0], coord[1] + i))
          elif board[coord[0]][coord[1] + i].upper() == board[coord[0]][coord[1] + i]:
            if auto == 0:
              if not pinning(self, turn, (coord[0], coord[1] + i)):
                self.__moves.append((coord[0], coord[1] + i))
                break
            else:
              self.__auto.append((coord[0], coord[1] + i))
              break
          else:
            break
      except:
        pass
    
    else:
      # up
      try:
        for i in range(1, 8):
          if board[coord[0] - i][coord[1]] == ' ' and coord[0] - i >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] - i, coord[1])):
                self.__moves.append((coord[0] - i, coord[1]))
            else:
              self.__auto.append((coord[0] - i, coord[1]))
          elif board[coord[0] - i][coord[1]].lower() == board[coord[0] - i][coord[1]] and coord[0] - i >= 0:
            if auto == 0:
              if pinning(self, turn, (coord[0] - i, coord[1])):
                self.__moves.append((coord[0] - i, coord[1]))
                break
            else:
              self.__auto.append((coord[0] - i, coord[1]))
              break
          else:
            break
      except:
        pass
      # down
      try:
        for i in range(1, 8):
          if board[coord[0] + i][coord[1]] == ' ':
            if auto == 0:
              if not pinning(self, turn, (coord[0] + i, coord[1])):
                self.__moves.append((coord[0] + i, coord[1]))
            else:
              self.__auto.append((coord[0] + i, coord[1]))
          elif board[coord[0] + i][coord[1]].lower() == board[coord[0] + i][coord[1]]:
            if auto == 0:
              if not pinning(self, turn, (coord[0] + i, coord[1])):
                self.__moves.append((coord[0] + i, coord[1]))
                break
            else:
              self.__auto.append((coord[0] + i, coord[1]))
              break
          else:
            break
      except:
        pass
      # left
      try:
        for i in range(1, 8):
          if board[coord[0]][coord[1] - i] == ' ' and coord[1] - i >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0], coord[1] - i)):
                self.__moves.append((coord[0], coord[1] - i))
            else:
              self.__auto.append((coord[0], coord[1] - i))
          elif board[coord[0]][coord[1] - i].lower() == board[coord[0]][coord[1] - i] and coord[1] - i >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0], coord[1] - i)):
                self.__moves.append((coord[0], coord[1] - i))
                break
            else:
              self.__auto.append((coord[0], coord[1] - i))
              break
          else:
            break
      except:
        pass
      # right
      try:
        for i in range(1, 8):
          if board[coord[0]][coord[1] + i] == ' ':
            if auto == 0:
              if not pinning(self, turn, (coord[0], coord[1] + i)):
                self.__moves.append((coord[0], coord[1] + i))
            else:
              self.__auto.append((coord[0], coord[1] + i))
          elif board[coord[0]][coord[1] + i].lower() == board[coord[0]][coord[1] + i]:
            if auto == 0:
              if not pinning(self, turn, (coord[0], coord[1] + i)):
                self.__moves.append((coord[0], coord[1] + i))
                break
            else:
              self.__auto.append((coord[0], coord[1] + i))
              break
          else:
            break
      except:
        pass

    if auto == 0:
      return self.__moves
    else:
      return self.__auto

  def move_piece(self, coord, new_coord, turn, board):
    if new_coord in self.legal_movement(coord, turn, board):
      chess_board[coord[0]][coord[1]] = ' '
      if turn % 2 == 0:
        for i in range(len(bpieces)):
          if bpieces[i].coord == new_coord:
            bpieces[i].coord = None
            bpieces[i].image = None
            trash_can.append(bpieces[i])
      else:
        for i in range(len(wpieces)):
          if wpieces[i].coord == new_coord:
            wpieces[i].coord = None
            wpieces[i].image = None
            trash_can.append(wpieces[i])
      chess_board[new_coord[0]][new_coord[1]] = self.piece
      self.coord = new_coord
      return True
    else:
      return False

class Kings:
  def __init__(self, coord, piece, image, points, checked, id):
    self.coord = coord
    self.piece = piece
    self.image = image
    self.points = points
    self.checked = checked  
    self.id = id
  def legal_movement(self, coord, turn, board, auto=0):
    self.__moves = []
    self.__auto = []
    if turn % 2 == 0:
      # up left to right
      for i in range(3):
        try:
          if board[coord[0] - 1][coord[1] - 1 + i] == ' ' and coord[0] - 1 >= 0 and coord[1] - 1 + i >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] - 1, coord[1] - 1 + i)):
                self.__moves.append((coord[0] - 1, coord[1] - 1 + i))
            else:
              self.__auto.append((coord[0] - 1, coord[1] - 1 + i))
          elif board[coord[0] - 1][coord[1] - 1 + i].upper() == board[coord[0] - 1][coord[1] - 1 + i] and coord[0] - 1 >= 0 and coord[1] - 1 >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] - 1, coord[1] - 1 + i)):
                self.__moves.append((coord[0] - 1, coord[1] - 1 + i))
            else:
              self.__auto.append((coord[0] - 1, coord[1] - 1 + i))
          else:
            pass
        except:
          pass

      # down left to right
      for i in range(3):
        try:
          if board[coord[0] + 1][coord[1] - 1 + i] == ' ' and coord[1] - 1 + i >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] + 1, coord[1] - 1 + i)):
                self.__moves.append((coord[0] + 1, coord[1] - 1 + i))
            else:
              self.__auto.append((coord[0] + 1, coord[1] - 1 + i))
          elif board[coord[0] + 1][coord[1] - 1 + i].upper() == board[coord[0] + 1][coord[1] - 1 + i] and coord[1] - 1 >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] + 1, coord[1] - 1 + i)):
                self.__moves.append((coord[0] + 1, coord[1] - 1 + i))
            else:
              self.__auto.append((coord[0] + 1, coord[1] - 1 + i))
          else:
            pass
        except:
          pass

      # left
      try:
        if board[coord[0]][coord[1] - 1] == ' ' and coord[1] - 1 >= 0:
          if auto == 0:
            if not pinning(self, turn, (coord[0], coord[1] - 1)):
              self.__moves.append((coord[0], coord[1] - 1))
              if board[coord[0]][coord[1] - 2] == ' ' and board[coord[0]][coord[1] - 3] == ' ' and coord[1] - 1 >= 0 and wrook1.castle:
                if not pinning(self, turn, (coord[0], coord[1] - 2)):
                  self.__moves.append((coord[0], coord[1] - 2))
          else:
            self.__auto.append((coord[0], coord[1] - 1))
            if board[coord[0]][coord[1] - 2] == ' ' and board[coord[0]][coord[1] - 3] == ' ' and coord[1] - 1 >= 0 and wrook1.castle:
              self.__auto.append((coord[0], coord[1] - 2))
        elif board[coord[0]][coord[1] - 1].upper() == board[coord[0]][coord[1] - 1] and coord[1] - 1 >= 0:
          if auto == 0:
            if not pinning(self, turn, (coord[0], coord[1] - 1)):
              self.__moves.append((coord[0], coord[1] - 1))
          else:
            self.__auto.append((coord[0], coord[1] - 1))
      except:
        pass
    
      # right
      try:
        if board[coord[0]][coord[1] + 1] == ' ':
          if auto == 0:
            if not pinning(self, turn, (coord[0], coord[1] + 1)):
              self.__moves.append((coord[0], coord[1] + 1))
              if board[coord[0]][coord[1] + 2] == ' ' and coord[1] - 1 >= 0 and wrook2.castle:
                if not pinning(self, turn, (coord[0], coord[1] + 2)):
                  self.__moves.append((coord[0], coord[1] + 2))
          else:
            self.__auto.append((coord[0], coord[1] + 1))
            if board[coord[0]][coord[1] + 2] == ' ' and coord[1] - 1 >= 0 and wrook2.castle:
              self.__auto.append((coord[0], coord[1] + 2))
        elif board[coord[0]][coord[1] + 1].upper() == board[coord[0]][coord[1] + 1]:
          if auto == 0:
            if not pinning(self, turn, (coord[0], coord[1] + 1)):
              self.__moves.append((coord[0], coord[1] + 1))
          else:
            self.__auto.append((coord[0], coord[1] + 1))
      except:
        pass

    else:
      # up left to right
      for i in range(3):
        try:
          if board[coord[0] - 1][coord[1] - 1 + i] == ' ' and coord[0] - 1 >= 0 and coord[1] - 1 + i >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] - 1, coord[1] - 1 + i)):
                self.__moves.append((coord[0] - 1, coord[1] - 1 + i))
            else:
              self.__auto.append((coord[0] - 1, coord[1] - 1 + i))
          elif board[coord[0] - 1][coord[1] - 1 + i].lower() == board[coord[0] - 1][coord[1] - 1 + i] and coord[0] - 1 >= 0 and coord[1] - 1 >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] - 1, coord[1] - 1 + i)):
                self.__moves.append((coord[0] - 1, coord[1] - 1 + i))
            else:
              self.__auto.append((coord[0] - 1, coord[1] - 1 + i))
          else:
            pass
        except:
          pass

      # down left to right
      for i in range(3):
        try:
          if board[coord[0] + 1][coord[1] - 1 + i] == ' ' and coord[1] - 1 + i >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] + 1, coord[1] - 1 + i)):
                self.__moves.append((coord[0] + 1, coord[1] - 1 + i))
            else:
              self.__auto.append((coord[0] + 1, coord[1] - 1 + i))
          elif board[coord[0] + 1][coord[1] - 1 + i].lower() == board[coord[0] + 1][coord[1] - 1 + i] and coord[1] - 1 >= 0:
            if auto == 0:
              if not pinning(self, turn, (coord[0] + 1, coord[1] - 1 + i)):
                self.__moves.append((coord[0] + 1, coord[1] - 1 + i))
            else:
              self.__auto.append((coord[0] + 1, coord[1] - 1 + i))
          else:
            pass
        except:
          pass

      # left
      try:
        if board[coord[0]][coord[1] - 1] == ' ' and coord[1] - 1 >= 0:
          if auto == 0:
            if not pinning(self, turn, (coord[0], coord[1] - 1)):
              self.__moves.append((coord[0], coord[1] - 1))
              if board[coord[0]][coord[1] - 2] == ' ' and board[coord[0]][coord[1] - 3] == ' ' and coord[1] - 1 >= 0 and brook1.castle:
                if not pinning(self, turn, (coord[0], coord[1] - 2)):
                  self.__moves.append((coord[0], coord[1] - 2))
          else:
            self.__auto.append((coord[0], coord[1] - 1))
            if board[coord[0]][coord[1] - 2] == ' ' and board[coord[0]][coord[1] - 3] == ' ' and coord[1] - 1 >= 0 and brook1.castle:
              self.__auto.append((coord[0], coord[1] - 2))
        elif board[coord[0]][coord[1] - 1].lower() == board[coord[0]][coord[1] - 1] and coord[1] - 1 >= 0:
          if auto == 0:
            if not pinning(self, turn, (coord[0], coord[1] - 1)):
              self.__moves.append((coord[0], coord[1] - 1))
          else:
            self.__auto.append((coord[0], coord[1] - 1))
      except:
        pass
    
      # right
      try:
        if board[coord[0]][coord[1] + 1] == ' ':
          if auto == 0:
            if not pinning(self, turn, (coord[0], coord[1] + 1)):
              self.__moves.append((coord[0], coord[1] + 1))
              if board[coord[0]][coord[1] + 2] == ' ' and coord[1] - 1 >= 0 and brook1.castle:
                if not pinning(self, turn, (coord[0], coord[1] + 2)):
                  self.__moves.append((coord[0], coord[1] + 2))
          else:
            self.__auto.append((coord[0], coord[1] + 1))
            if board[coord[0]][coord[1] - 2] == ' ' and board[coord[0]][coord[1] - 3] == ' ' and coord[1] - 1 >= 0 and brook1.castle:
              self.__moves.append((coord[0], coord[1] - 2))
        elif board[coord[0]][coord[1] + 1].lower() == board[coord[0]][coord[1] + 1]:
          if auto == 0:
            if not pinning(self, turn, (coord[0], coord[1] + 1)):
              self.__moves.append((coord[0], coord[1] + 1))
          else:
            self.__auto.append((coord[0], coord[1] + 1))
      except:
        pass
    if auto == 0:
      return self.__moves
    else:
      return self.__auto

  def move_piece(self, coord, new_coord, turn, board):
    if new_coord in self.legal_movement(coord, turn, board):
      chess_board[coord[0]][coord[1]] = ' '
      if turn % 2 == 0:
        wrook1.caslte = False
        wrook2.castle = False
        if coord[1] - new_coord[1] == 2:
          chess_board[wrook1.coord[0]][wrook1.coord[1]] = ' '
          chess_board[wrook1.coord[0]][wrook1.coord[1] + 3] = wrook1.piece
          wrook1.coord = (wrook1.coord[0], wrook1.coord[1] + 3)
        if coord[1] - new_coord[1] == -2:
          chess_board[wrook2.coord[0]][wrook2.coord[1]] = ' '
          chess_board[wrook2.coord[0]][wrook2.coord[1] - 2] = wrook2.piece
          wrook2.coord = (wrook2.coord[0], wrook2.coord[1] - 2)
        for i in range(len(bpieces)):
          if bpieces[i].coord == new_coord:
            bpieces[i].coord = None
            bpieces[i].image = None
            trash_can.append(bpieces[i])
      else:
        brook1.castle = False
        brook2.castle = False
        if coord[1] - new_coord[1] == 2:
          chess_board[brook1.coord[0]][brook1.coord[1]] = ' '
          chess_board[brook1.coord[0]][brook1.coord[1] + 3] = brook1.piece
          brook1.coord = (brook1.coord[0], brook1.coord[1] + 3)
        if coord[1] - new_coord[1] == -2:
          chess_board[brook2.coord[0]][brook2.coord[1]] = ' '
          chess_board[brook2.coord[0]][brook2.coord[1] - 2] = brook2.piece
          brook2.coord = (brook2.coord[0], brook2.coord[1] - 2)
        for i in range(len(wpieces)):
          if wpieces[i].coord == new_coord:
            wpieces[i].coord = None
            wpieces[i].image = None
            trash_can.append(wpieces[i])
      chess_board[new_coord[0]][new_coord[1]] = self.piece
      self.coord = new_coord
      return True
    else:
      return False
  

chess_board = [
  ['R', 'H', 'B', 'Q', 'K', 'B', 'H', 'R'],
  ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
  ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
  ['r', 'h', 'b', 'q', 'k', 'b', 'h', 'r']
]

turn = 0

wpawn1 = Pawns((6, 0), 'p', pawn, 10, False, 1)
wpawn2 = Pawns((6, 1), 'p', pawn, 10, False, 2)
wpawn3 = Pawns((6, 2), 'p', pawn, 10, False, 3)
wpawn4 = Pawns((6, 3), 'p', pawn, 10, False, 4)
wpawn5 = Pawns((6, 4), 'p', pawn, 10, False, 5)
wpawn6 = Pawns((6, 5), 'p', pawn, 10, False, 6)
wpawn7 = Pawns((6, 6), 'p', pawn, 10, False, 7)
wpawn8 = Pawns((6, 7), 'p', pawn, 10, False, 8)

wbishop1 = Bishops((7, 2), 'b', bishop, 30, 9)
wbishop2 = Bishops((7, 5), 'b', bishop, 30, 10)

wknight1 = Horses((7, 1), 'h', horse, 30, 11)
wknight2 = Horses((7, 6), 'h', horse, 30, 12)

wrook1 = Rooks((7, 0), 'r', rook, 50, True, 13)
wrook2 = Rooks((7, 7), 'r', rook, 50, True, 14)

wqueen1 = Queens((7, 3), 'q', queen, 90, 15)
wking1 = Kings((7, 4), 'k', king, 900, False, 16)

wpieces = [wpawn1, wpawn2, wpawn3, wpawn4, wpawn5, wpawn6, wpawn7, wpawn8, wbishop1, wbishop2, wknight1, wknight2, wrook1, wrook2, wqueen1, wking1]

bpawn1 = Pawns((1, 0), 'P', pawn_2, -10, False, 1)
bpawn2 = Pawns((1, 1), 'P', pawn_2, -10, False, 2)
bpawn3 = Pawns((1, 2), 'P', pawn_2, -10, False, 3)
bpawn4 = Pawns((1, 3), 'P', pawn_2, -10, False, 4)
bpawn5 = Pawns((1, 4), 'P', pawn_2, -10, False, 5)
bpawn6 = Pawns((1, 5), 'P', pawn_2, -10, False, 6)
bpawn7 = Pawns((1, 6), 'P', pawn_2, -10, False, 7)
bpawn8 = Pawns((1, 7), 'P', pawn_2, -10, False, 8)

bbishop1 = Bishops((0, 2), 'B', bishop_2, -30, 9)
bbishop2 = Bishops((0, 5), 'B', bishop_2, -30, 10)

bknight1 = Horses((0, 1), 'H', horse_2, -30, 11)
bknight2 = Horses((0, 6), 'H', horse_2, -30, 12)

brook1 = Rooks((0, 0), 'R', rook_2, -50, True, 13)
brook2 = Rooks((0, 7), 'R', rook_2, -50, True, 14)

bqueen1 = Queens((0, 3), 'Q', queen_2, -90, 15)
bking1 = Kings((0, 4), 'K', king_2, -900, False, 16)

bpieces = [bpawn1, bpawn2, bpawn3, bpawn4, bpawn5, bpawn6, bpawn7, bpawn8, bbishop1, bbishop2, bknight1, bknight2, brook1, brook2, bqueen1, bking1]

trash_can = []


two_player_button = Button(0, 350, 100, 50)
one_player_button = Button(300, 300, 100, 50)
gambits = Button(300, 350, 100, 50)

def move(coords, turn= None, piece= None, where= None):
  if piece == None:
    if turn % 2 == 0:
      for i in range(len(wpieces)):
        if coords == wpieces[i].coord:
          return wpieces[i]
      return None
    else:
      for i in range(len(bpieces)):
        if coords == bpieces[i].coord:
          return bpieces[i]
      return None
  else:
    moved = piece.move_piece(coords, where, turn, chess_board)
    return moved


def translate_xy_coord(x, y):
  x_coord = 0
  y_coord = 0
  if y <= 400:
    if y >= 0 and y < 50:
      x_coord = 0
    elif y >= 50 and y < 100:
      x_coord = 1
    elif y >= 100 and y < 150:
      x_coord = 2
    elif y >= 150 and y < 200:
      x_coord = 3
    elif y >= 200 and y < 250:
      x_coord = 4
    elif y >= 250 and y < 300:
      x_coord = 5
    elif y >= 300 and y < 350:
      x_coord = 6
    elif y >= 350 and y < 400:
      x_coord = 7
    
    if x >= 0 and x < 50:
      y_coord = 0
    elif x >= 50 and x < 100:
      y_coord = 1
    elif x >= 100 and x < 150:
      y_coord = 2
    elif x >= 150 and x < 200:
      y_coord = 3
    elif x >= 200 and x < 250:
      y_coord = 4
    elif x >= 250 and x < 300:
      y_coord = 5
    elif x >= 300 and x < 350:
      y_coord = 6
    elif x >= 350 and x < 400:
      y_coord = 7
  return(x_coord, y_coord)

def translate_coord2board(coord):
  x = coord[0] * 50
  y = coord[1] * 50

  return (y, x)

def show_screen():
  screen.blit(title_screen, (0,0))
  pygame.display.update()
  
def draw_screen():
  x = 0
  y = 0
  for e in range(8):
    if e % 2:
      for i in range(8):
        if i % 2 != 0:
          pygame.draw.rect(screen, (217, 246, 255), (x, y,50,50))

        elif i % 2 == 0:
          pygame.draw.rect(screen, (255, 255, 255), (x, y,50,50))
        x += 50
      x = 0
    else:
      for i in range(8):
        if i % 2 != 0:
          pygame.draw.rect(screen, (255, 255, 255), (x, y,50,50))

        elif i % 2 == 0:
          pygame.draw.rect(screen, (217, 246, 255), (x, y,50,50))
        x += 50
      x = 0
    y += 50

  for i in range(len(wpieces)):
    try:
      square = translate_coord2board(wpieces[i].coord)
      screen.blit(wpieces[i].image, square)
    except:
      pass
  for i in range(len(bpieces)):
    try:
      square = translate_coord2board(bpieces[i].coord)
      screen.blit(bpieces[i].image, square)
    except:
      pass

  pygame.display.update()

def move_show(piece, turn):
  legal_moves = piece.legal_movement(piece.coord, turn, chess_board)
  piece_coord = translate_coord2board(piece.coord)

  for i in range(len(legal_moves)):
    square = translate_coord2board(legal_moves[i])
    pygame.draw.rect(screen, (25, 0, 186), (square[0],square[1] + 45, 50,5))
  pygame.draw.rect(screen, (38, 255, 0), (piece_coord[0],piece_coord[1] + 45, 50,5))
  pygame.display.update()

def show_check():
  if bking1.checked:
    underline = translate_coord2board(bking1.coord)
    pygame.draw.rect(screen, (255, 125, 125), (underline[0], underline[1] + 45, 50,5))
  elif wking1.checked:
    underline = translate_coord2board(wking1.coord)
    pygame.draw.rect(screen, (255, 125, 125), (underline[0], underline[1] + 45, 50,5))

  pygame.display.update()

def find_move(turn):
  if p1:
    if turn % 2 != 0:
      return None
  finding = True
  while finding:
    CLOCK.tick(FPS)
    show_check()
    for event in pygame.event.get():
      pos = pygame.mouse.get_pos()

      if event.type == pygame.QUIT:
        sys.exit()
    try:
      if pygame.mouse.get_pressed(3) == (1,0,0):
        time.sleep(.1)
        first = translate_xy_coord(pos[0], pos[1])
        piece = move(first, turn)
        time.sleep(.2)
        if piece != None:
          finding = False
  
    except:
      pass

    draw_screen()

  while True:
    CLOCK.tick(FPS)
    show_check()
    move_show(piece, turn)
    for event in pygame.event.get():
      pos = pygame.mouse.get_pos()

      if event.type == pygame.QUIT:
        sys.exit()

    if pygame.mouse.get_pressed(3) == (1,0,0):
      second = translate_xy_coord(pos[0], pos[1])
      moved = move(first, turn, piece, second)
      return moved
      time.sleep(.1)
      draw_screen()

p2 = False
p1 = False
gambit = False

def check(turn, board, second_piece=None):
  possible_moves = []
  if turn % 2 == 0:
    for i in range(len(wpieces)):
      try:
        lists = wpieces[i].legal_movement(wpieces[i].coord, turn, board, 1)
      except:
        pass
      for e in range(len(lists)):
        if lists[e][0] >= 0 and lists[e][1] >= 0:
          if wpieces[i].piece != 'p' and wpieces[i].coord != (lists[e][0]+2,lists[e][1]) or wpieces[i].coord != (lists[e][0]+1,lists[e][1]):
            if wpieces[i].coord != second_piece:
              possible_moves.append(lists[e])
    for i in range(len(possible_moves)):
      if board[possible_moves[i][0]][possible_moves[i][1]] == bking1.piece:
        if possible_moves[i] == bking1.coord:
          bking1.checked = True
        return True
    bking1.checked = False
    return False
  else:
    for i in range(len(bpieces)):
      try:
        lists = bpieces[i].legal_movement(bpieces[i].coord, turn, board, 1)
      except:
        pass
      for e in range(len(lists)):
        if lists[e][0] >= 0 and lists[e][1] >= 0:
          if bpieces[i].piece != 'P' and bpieces[i].coord != (lists[e][0]+2,lists[e][1]) or bpieces[i].coord != (lists[e][0]+1,lists[e][1]):
            if bpieces[i].coord != second_piece:
              possible_moves.append(lists[e])
    for i in range(len(possible_moves)):
      if board[possible_moves[i][0]][possible_moves[i][1]] == wking1.piece:
        if possible_moves[i] == wking1.coord:
          wking1.checked = True
        return True
    wking1.checked = False
    return False

def board_print(board):
  for space in range(len(board)):
    print(' '.join([(x) for x in board[space]]))

def pinning(piece, turn, where):
  try:
    board_copy = []
    for i in range(len(chess_board)):
      what = chess_board[i].copy()
      board_copy.append(what)
    board_copy[piece.coord[0]][piece.coord[1]] = ' '
    board_copy[where[0]][where[1]] = piece.piece
    return check(turn + 1, board_copy, (where[0],where[1]))
  except:
    pass

def check_mates(turn, board):
  possible_moves = []
  if turn % 2 == 0:
    for i in range(len(bpieces)):
      lists = bpieces[i].legal_movement(bpieces[i].coord, turn + 1, board)
      for e in range(len(lists)):
        possible_moves.append(lists[e])
  else:
    for i in range(len(wpieces)):
      lists = wpieces[i].legal_movement(wpieces[i].coord, turn + 1, board)
      for e in range(len(lists)):
        possible_moves.append(lists[e])
  if len(possible_moves) == 0:
    return True
  else:
    return False
    

while True:
  CLOCK.tick(FPS)
  for event in pygame.event.get():
    pos = pygame.mouse.get_pos()
    if event.type == pygame.QUIT:
      sys.exit()
  
  if p2:
    moved = find_move(turn)
    if moved:
      print('moved')
      if turn % 2 == 0:
        for i in range(len(bpieces)):
          try:
            bpieces[i].en_passantable = False
          except:
            pass
        
      else:
        for i in range(len(wpieces)):
          try:
            wpieces[i].en_passantable = False
          except:
            pass
      turn += 1
    a = 0
    for i in range(len(wpieces)):
      try:
        if wpieces[i].coord != None:
          a += wpieces[i].points
      except:
        pass
    for i in range(len(bpieces)):
      try:
        if bpieces[i].coord != None:
          a += bpieces[i].points
      except:
        pass
    print('points', a)
    draw_screen()
  
  elif check_mates(turn + 1, chess_board):
    p2 = False
    p1 = False
    gambit = False
    chess_board = [['R', 'H', 'B', 'Q', 'K', 'B', 'H', 'R'],['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],['r', 'h', 'b', 'q', 'k', 'b', 'h', 'r']]

    turn = 0

    wpawn1 = Pawns((6, 0), 'p', pawn, 10, False, 1)
    wpawn2 = Pawns((6, 1), 'p', pawn, 10, False, 2)
    wpawn3 = Pawns((6, 2), 'p', pawn, 10, False, 3)
    wpawn4 = Pawns((6, 3), 'p', pawn, 10, False, 4)
    wpawn5 = Pawns((6, 4), 'p', pawn, 10, False, 5)
    wpawn6 = Pawns((6, 5), 'p', pawn, 10, False, 6)
    wpawn7 = Pawns((6, 6), 'p', pawn, 10, False, 7)
    wpawn8 = Pawns((6, 7), 'p', pawn, 10, False, 8)

    wbishop1 = Bishops((7, 2), 'b', bishop, 30, 9)
    wbishop2 = Bishops((7, 5), 'b', bishop, 30, 10)

    wknight1 = Horses((7, 1), 'h', horse, 30, 11)
    wknight2 = Horses((7, 6), 'h', horse, 30, 12)

    wrook1 = Rooks((7, 0), 'r', rook, 50, True, 13)
    wrook2 = Rooks((7, 7), 'r', rook, 50, True, 14)

    wqueen1 = Queens((7, 3), 'q', queen, 90, 15)
    wking1 = Kings((7, 4), 'k', king, 900, False, 16)

    wpieces = [wpawn1, wpawn2, wpawn3, wpawn4, wpawn5, wpawn6, wpawn7, wpawn8, wbishop1, wbishop2, wknight1, wknight2, wrook1, wrook2, wqueen1, wking1]

    bpawn1 = Pawns((1, 0), 'P', pawn_2, -10, False, 1)
    bpawn2 = Pawns((1, 1), 'P', pawn_2, -10, False, 2)
    bpawn3 = Pawns((1, 2), 'P', pawn_2, -10, False, 3)
    bpawn4 = Pawns((1, 3), 'P', pawn_2, -10, False, 4)
    bpawn5 = Pawns((1, 4), 'P', pawn_2, -10, False, 5)
    bpawn6 = Pawns((1, 5), 'P', pawn_2, -10, False, 6)
    bpawn7 = Pawns((1, 6), 'P', pawn_2, -10, False, 7)
    bpawn8 = Pawns((1, 7), 'P', pawn_2, -10, False, 8)

    bbishop1 = Bishops((0, 2), 'B', bishop_2, -30, 9)
    bbishop2 = Bishops((0, 5), 'B', bishop_2, -30, 10)

    bknight1 = Horses((0, 1), 'H', horse_2, -30, 11)
    bknight2 = Horses((0, 6), 'H', horse_2, -30, 12)

    brook1 = Rooks((0, 0), 'R', rook_2, -50, True, 13)
    brook2 = Rooks((0, 7), 'R', rook_2, -50, True, 14)

    bqueen1 = Queens((0, 3), 'Q', queen_2, -90, 15)
    bking1 = Kings((0, 4), 'K', king_2, -900, False, 16)

    bpieces = [bpawn1, bpawn2, bpawn3, bpawn4, bpawn5, bpawn6, bpawn7, bpawn8, bbishop1, bbishop2, bknight1, bknight2, brook1, brook2, bqueen1, bking1]

    trash_can = []

  # elif p1:
    
  #   moved = find_move(turn)
  #   if moved == None:
  #     engine_move = (engine(wpieces, bpieces, chess_board, 3, True, 1))
  #     for i in range(len(bpieces)):
  #       if bpieces[i].id == engine_move[1]:
  #         moved = bpieces[i].move_piece(bpieces[i].coord, engine_move[0], turn, chess_board)
  #         board_print(chess_board)
  #         break

  #   if moved:
  #     print('moved')
  #     if turn % 2 == 0:
  #       for i in range(len(bpieces)):
  #         try:
  #           bpieces[i].en_passantable = False
  #         except:
  #           pass
        
  #     else:
  #       for i in range(len(wpieces)):
  #         try:
  #           wpieces[i].en_passantable = False
  #         except:
  #           pass
  #     turn += 1
  #   a = 0
  #   for i in range(len(wpieces)):
  #     try:
  #       if wpieces[i].coord != None:
  #         a += wpieces[i].points
  #     except:
  #       pass
  #   for i in range(len(bpieces)):
  #     try:
  #       if bpieces[i].coord != None:
  #         a += bpieces[i].points
  #     except:
  #       pass
  #   print('points', a)
  #   draw_screen()

  else:
    
    show_screen()
    screen.blit(pawn, (50,50))
    if pygame.mouse.get_pressed(3) == (1,0,0):
      if two_player_button.onButton(pos):
        print('two player')
        p2 = True
      elif one_player_button.onButton(pos):
        print('one player')
        p1 = True
      elif gambits.onButton(pos):
        print('gambits')
        p2 = True
      two_player_button = Button(400, 400, 100, 50)
      one_player_button = Button(400, 400, 100, 50)
      gambits = Button(400, 400, 100, 50)
