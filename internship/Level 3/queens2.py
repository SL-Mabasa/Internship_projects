#Queens Problem for chess 
#Board is NxN for N queens
#All queens must be in safe positions horizontally, vertically and diagonally
import random

def queens(N, n):

    selection = N
    mat = matrix(N)
    if selection < 4:
        print('Number of Queens must be greater than 3')
    else:
        queen_positions = []
        row_restrictions = []
        column_restrictions = []
        diagonal_restrictions = []

        m = 0
        q = 0
        end = False

        # Restart conditions
        restarts = 0
        max_restarts = 200

        while not end:
            # 1) Find all safe cells first
            candidates = safe_positions(selection, row_restrictions, column_restrictions, diagonal_restrictions, queen_positions)

            # 2) If no safe cells and not done, restart attempt
            if candidates == [] and q < selection:
                restarts += 1
                print(f"\nNo safe positions left, restarting \n")

                if restarts > max_restarts:
                    print("\nCould not find a solution after many restarts\n")
                    break

                # reset state
                queen_positions = []
                row_restrictions = []
                column_restrictions = []
                diagonal_restrictions = []
                m = 0
                q = 0
                continue

            # Stop condition if we have required queens
            if q == selection:
                end = True
                break

            # Random location
            pick_index = random.randint(0, len(candidates)-1)
            row = candidates[pick_index][0]
            column = candidates[pick_index][1]
            value = mat[row][column]
            validator = [row, column]

            if validator in queen_positions:
                continue

            row_restrictions_validator = horizontal(row, column, selection, mat)
            column_restrictions_validator = vertical(row, column, selection, mat)
            diagonal_restrictions_validator = diagonal(row, column, value, selection, mat)

            
            if validator in row_restrictions or validator in column_restrictions or validator in diagonal_restrictions:
                continue

            # Update
            queen_positions.append(validator)
            q += 1
            m += 1

            row_restrictions.extend(row_restrictions_validator)
            column_restrictions.extend(column_restrictions_validator)
            diagonal_restrictions.extend(diagonal_restrictions_validator)

            #Successful placements
            print(f"\nAfter sucessful loop {m}, {q} queens placed")
            print(f"Placed at {validator}\n")

        # Results
        print('\n RESULTS \n')
        print("Row restrictions:", row_restrictions, '\n')  
        print("Column restrictions:", column_restrictions, '\n')     
        print("Diagonal restrictions:", diagonal_restrictions, '\n')
        print(f'{q} Queen positions with {m} successful outputs\n')
        print("Queens:", queen_positions, '\n')

        # Print results
        if q == selection:
            print("\nFinal Board with Queens:\n")
            for i in range(selection):
                row_str = ""
                for j in range(selection):
                    if [i, j] in queen_positions:
                        row_str += " Q "
                    else:
                        row_str += " . "
                print(row_str)
        else:
            print("\nNo complete solution found.")

#Check for horizontal coordinates
def horizontal(row_h, column_h, selection, matrix_h):
    temp_list = []
    for y in range(0,selection):
        if y!=column_h:
            #print(matrix_h[row_h][y], ': ', row_h, y)
            holder = [row_h, y]
            temp_list.append(holder)
        
        else:
            pass
    return temp_list

#CHeck for vertical coordinates    
def vertical(row_v, column_v, selection, matrix_v):
    temp_list = []
    for x in range(0,selection):
        if x!=row_v:
            #print(matrix_v[x][column_v], ': ', x, column_v)
            holder = [x,column_v]
            temp_list.append(holder)
        
        else:
            pass
    return temp_list

#Checks diagonal coordinates
def diagonal(row_d, column_d, value_d, selection, matrix_d):
    temp_list = []
    x_holder_1 = row_d
    y_holder_1 = column_d
    x_holder_2 = row_d
    y_holder_2 = column_d
    k = selection - 1

    for x in range(0,selection):
        for y in range(0,selection):
            if x!=row_d and y!=column_d:
                check = matrix_d[x][y]
                if check==value_d:
                    #print(check,': ',x, ' ',y)
                    holder = [x,y]
                    temp_list.append(holder)

    #Backwards movement
    while True:

        if x_holder_1 == 0 or y_holder_1 == 0:
            break
        else:
            x_holder_1 -=1
            y_holder_1 -= 1
            check = matrix_d[x_holder_1][y_holder_1]
            #print(check, ': ', x_holder_1, ' ', y_holder_1)
            holder = [x_holder_1, y_holder_1]
            temp_list.append(holder)
    
    #Forward movement
    while True:

        if x_holder_2 == k or y_holder_2 == k:
            break
        else:
            x_holder_2 +=1
            y_holder_2 += 1
            check = matrix_d[x_holder_2][y_holder_2]
            #print(check, ': ', x_holder_2, ' ', y_holder_2)
            holder = [x_holder_2, y_holder_2]
            temp_list.append(holder)

    return temp_list

#Creates N x N matrix
def matrix(selection):
    row_m = selection - 1
    column_m = selection - 1
    matrix = []
    initial = 0
    order = 0
    for x in range(selection):
        initial = order
        temp_list=[]
        for y in range(selection):
            if x==0 and y==0:
                temp_list.append(initial)
                initial +=1
            else: 
                temp_list.append(initial)
                initial +=1
        order += 1
        matrix.append(temp_list)
        
    
    return matrix

# Search safe positions
def safe_positions(selection, row_rest, col_rest, diag_rest, queen_pos):
    candidates = []
    for i in range(selection):
        for j in range(selection):
            pos = [i, j]
            if pos in queen_pos:
                pass
            elif pos in row_rest:
                pass
            elif pos in col_rest:
                pass
            elif pos in diag_rest:
                pass
            else:
                candidates.append(pos)
    return candidates

# Main
print('This is a program that shows N queens on a N x N board')
print('Rules')
print('----------------------------------------------------------')
print('1. There should be N queens for N x N 2D board')
print('2. The queens should not be on the same horizontal line')
print('3. The queens should not be on the same vertical line')
print('4. The queens should not be on the same diagonal lines')
print('----------------------------------------------------------')
selection = int(input('Select the number to represent N\n-> '))
n = selection - 1
mat = matrix(selection)

print('Your Board\n')
for x in mat:
    print(x)
print('\n')

queens(selection, n)