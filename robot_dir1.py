class Node:
    def __init__(self, direction):
        self.direction = direction
        self.prev = None
        self.next = None

class DirectionList:
    def __init__(self):
        self.head = Node('N')
        e_node = Node('E')
        s_node = Node('S')
        w_node = Node('W')

        # связка узлов
        self.head.next = e_node
        e_node.prev = self.head
        e_node.next = s_node
        s_node.prev = e_node
        s_node.next = w_node
        w_node.prev = s_node
        w_node.next = self.head  # замыкание
        self.head.prev = w_node  # замыкание

    def turn_left(self, current_node):
        return current_node.prev

    def turn_right(self, current_node):
        return current_node.next

def robot_direction(initial_direction, commands):
    direction_list = DirectionList()

    current_node = direction_list.head
    while current_node.direction != initial_direction:
        current_node = current_node.next

    for command in commands:
        if command == 'L':
            current_node = direction_list.turn_left(current_node)  # поворот налево
        elif command == 'R':
            current_node = direction_list.turn_right(current_node)  # поворот направо
        elif command == 'F':
            pass  # движение вперёд (направление не меняется) -- не учитываем
        elif command == 'B':
            pass  # движение назад (направление не меняется) -- не учитываем

    return current_node.direction


initial_direction = input()
commands = input()

final_direction = robot_direction(initial_direction, commands)
print(final_direction)

