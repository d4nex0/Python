def print_board(board):
  for row in board:
      print(" | ".join(row))
      print("-" * 9)

def check_winner(board):
  # Проверка строк и столбцов
  for i in range(3):
      if board[i][0] == board[i][1] == board[i][2] != ' ':
          return True
      if board[0][i] == board[1][i] == board[2][i] != ' ':
          return True

  # Проверка диагоналей
  if board[0][0] == board[1][1] == board[2][2] != ' ':
      return True
  if board[0][2] == board[1][1] == board[2][0] != ' ':
      return True

  return False

def tic_tac_toe():
  board = [[' ' for _ in range(3)] for _ in range(3)]
  current_player = 'X'
  moves = 0

  while moves < 9:
      print_board(board)
      row = int(input(f"Игрок {current_player}, введите строку (0-2): "))
      col = int(input(f"Игрок {current_player}, введите столбец (0-2): "))

      if board[row][col] == ' ':
          board[row][col] = current_player
          moves += 1

          if check_winner(board):
              print_board(board)
              print(f"Игрок {current_player} выиграл!")
              return

          current_player = 'O' if current_player == 'X' else 'X'
      else:
          print("Эта клетка уже занята, попробуйте снова.")

  print_board(board)
  print("Ничья!")

# Запуск игры
tic_tac_toe()
