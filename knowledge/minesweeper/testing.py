from minesweeper import MinesweeperAI

def print_ai_status():
    print(f'\nAfter move:{move} with nearby_count:{nearby_count}')
    if ai.knowledge:
        print('Sentences in Knowledge Base:')
        for cnt, s in enumerate(ai.knowledge):
            #print(f'S#{cnt}: {s}')
            # create list from cell set with moves ordered by row/column
            s_as_l = sorted(list(s.cells), key=lambda t: (t[0], t[1]))
            print(f'S#{cnt}: {s_as_l} = {s.count}')
    else:
        print('NO Sentences in Knowledge Base.')       
    print(f'Safe Cells: {sorted(list(ai.safes))}')
    print(f'Mine Cells: {sorted(list(ai.mines))}')    
    
# Create AI agent
HEIGHT, WIDTH, MINES = 8, 8, 8
ai = MinesweeperAI(height=HEIGHT, width=WIDTH)

# Test new sentence logic (3rd requirement)
move, nearby_count = (1,1), 0
ai.add_knowledge(move,nearby_count)
print_ai_status()

move, nearby_count = (2,2), 2
ai.add_knowledge(move,nearby_count)
print_ai_status()

# Test inference logic for new safes or mines (4th requirement)
move, nearby_count = (3,3), 0
ai.add_knowledge(move,nearby_count)
print_ai_status()