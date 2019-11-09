def solution(board, moves):
    stack = Stack()
    
    for move in moves:
        item = choose(board, move-1)
        if item == 0:
            continue
            
        stack.push(item)
    
    answer = stack.score
    return answer

def choose(board, move):
    choose = 0
    for index in range(len(board)):
        if board[index][move] != 0:
            choose = board[index][move]
            board[index][move] = 0
            break
    
    return choose

class Stack:
    def __init__(self):
        self.score = 0
        self.items = []
        
    def push(self, item):
        if len(self.items) > 0 and self.items[-1] == item:
            self.pop()
            self.score += 2
        else:
            self.items.append(item)
    
    def pop(self):
        return self.items.pop()