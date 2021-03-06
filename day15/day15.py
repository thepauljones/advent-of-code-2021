from adjacents import get_adjacent

with open('data.dat') as file:
    raw_data = [line.strip() for line in file]

field = []
for line in raw_data:
    field.append(map(int, list(line)))


# PART TWO starts here, abandon all hope ye who enter

def increment(num):
    result = num + 1
    return result if result < 10 else 1

limitX = len(field[0])
limitY = len(field)

# Expand this bitch outwards x5 with incremental rule changes
for j in range(0, limitY):
    for i in range(0, 4):
        for x in range(0, limitX):
            field[j].append(increment(field[j][limitX * i + x]))

for y in range(0, 4):
    for j in range(0, limitY):
        field.append(map(increment, field[y * limitY + j]))

# PART TWO mappery ends

def print_grid(field):
    for line in field:
        print(''.join(str(line)))

# print_grid(field)

FieldGraph = {}

for j in range(0, len(field)):
    for i in range(0, len(field[0])):
        FieldGraph[(j, i)] = float('inf')

#print(FieldGraph)

#print_grid(field)

def find_path(start, end, field):
    frontier = []

    frontier.append((0, start))
    came_from = {}
    cost = {}
    came_from[start] = None
    cost[start] = 0

    while len(frontier) > 0:
        _, current = frontier.pop(0)

        if current == end:
            break

        for next_cost, next_pos in get_adjacent(current[0], current[1], field):
            new_cost = cost[current] + next_cost
            if next_pos not in cost or new_cost < cost[next_pos]:
                cost[next_pos] = new_cost
                came_from[next_pos] = current
                frontier.append((new_cost, next_pos))
                frontier.sort()


    # traversed grid, now recreate path
    path = []
    path_cost = 0
    current = end

    while current != start:
        path.append(current)
        path_cost += cost[current]
        current = came_from[current]

    path.append(start)

    for j, i in path:
        field[j][i] = '0'

    # print_grid(field)
    path.reverse()
    print(cost[end])

find_path((0,0), (len(field) - 1, len(field[0]) - 1), field)

