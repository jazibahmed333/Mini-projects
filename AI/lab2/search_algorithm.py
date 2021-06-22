import numpy as np
import math
import heapq
import random

# Priority Queue based on heapq
class PriorityQueue:
    def __init__(self):
        self.elements = []
    def isEmpty(self):
        return len(self.elements) == 0
    def add(self, item, priority):
        heapq.heappush(self.elements,(priority,item))
    def remove(self):
        return heapq.heappop(self.elements)[1]
    def backremove(self):
        return heapq._heappop_max(self.elements)[1]

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def valid(x, y,map):
    if (x < 0 or x >= len(map) or y < 0 or y >= len(map[x])):
        return False
    #elif ((map[x][y]) != 0):
     #   return False
    return (map[x][y] == 0)


# An example of search algorithm, feel free to modify and implement the missing part
def search(map, start, goal,info, typeofSearch):
    map_Temp = np.array(map)
    # cost moving to another cell
    moving_cost = 1
    exp_nodes = []
    delta_x = [-1, 1, 0, 0]
    delta_y = [0, 0, 1, -1]

    if typeofSearch == 'Random':
        select = random.randint(1, 5)
        print(select)
        if ( select == 1):
            typeofSearch = "BFS"
            print("Random search found BFS")
        elif (select == 2):
            typeofSearch = "DFS"
            print("Random search found DFS")
        elif (select == 3):
            typeofSearch = "Greedy"
            print("Random search found Greedy")
        elif (select == 4):
            typeofSearch = "aStarE"
            print("Random search found aStarE")
        elif (select == 5):
            typeofSearch = "aStarM"
            print("Random search found aStarM")
    # init. starting node
    #start.parent = None
    #start.g = 0
    dist = dict()
    dist[start] = (0, [start])

    if typeofSearch == 'BFS':
        # open list
        frontier = PriorityQueue()
        # add starting cell to open list
        frontier.add(start, 0)
        # if there is still nodes to open
        while not frontier.isEmpty():
            current = frontier.remove()
            cost, came_from = dist[current]
            # check if the goal is reached
            if current == goal:
                break

        # for each neighbour of the current cell
        # Implement get_neighbors function (return nodes to expand next)
        # (make sure you avoid repetitions!)
        #for next in get_neighbors(current):
            for dx, dy in zip(delta_x, delta_y):
                # compute cost to reach next cell
                # Implement cost function
                next = current[0] + dx, current[1] + dy
                if not valid(next[0], next[1],map) or next in dist.keys():
                    continue

                # Make sure walkable terrain
                #cost = cost_function(dist,next,moving_cost)
                #cost = cost+ moving_cost
                dist[next] = cost + moving_cost, came_from+[next]
                # add next cell to open list
                frontier.add(next, cost+1)
                #print(next[0],next[1])
                map_Temp[next[0],next[1]] = cost + moving_cost
                exp_nodes.append([next[0], next[1]])
        #print("Explored Nodes: ", exp_nodes)
        print("Length of Explored Nodes BFS: ", len(exp_nodes))
        return came_from, cost,map_Temp


    elif typeofSearch == 'DFS':

        open = []
        closed = []

        # Add the start node

        open.append(start)
        # Loop until the open list is empty
        while len(open) > 0:

            # Get the last node (LIFO)
            current_node = open.pop(-1)

            # Add the current node to the closed list
            closed.append(current_node)

            cost, came_from = dist[current_node]
            # Check if we have reached the goal, return the path

            if current_node == goal:
                break

            (x, y) = current_node
            # Get neighbors
            neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

            # Loop neighbors

            for next in neighbors:

                if not valid(next[0], next[1], map) or next in closed:
                    continue

                # Create a neighbor node

                dist[next] = cost + moving_cost, came_from + [next]
                neighbor = next  # Check if the neighbor is in the closed list
                if (neighbor in closed):
                    continue
                # Everything is green, add the node if it not is in open
                if (neighbor not in open):
                    open.append(neighbor)

                map_Temp[neighbor[0], neighbor[1]] = cost + moving_cost
                exp_nodes.append([next[0], next[1]])

                if (neighbor == goal):
                    break
        #print("Explored Nodes: ",exp_nodes)
        print("Length of Explored Nodes DFS: ",len(exp_nodes))
        return came_from, cost, map_Temp

    elif (typeofSearch == 'Greedy'):
        # return None
        # Create start and end node
        start_node = Node(None, start)
        start_node.h = 0
        goal_node = Node(None, goal)
        goal_node.h = 0

        # Initialize both open and closed list
        open_list = []
        closed_list = []

        # Add the start node
        open_list.append(start_node)

        # Loop until you find the end
        while len(open_list) > 0:

            # Get the current node
            current_node = open_list[0]
            current_index = 0
            for index, item in enumerate(open_list):
                if item.h < current_node.h:
                    current_node = item
                    current_index = index

            # Pop current off open list, add to closed list
            open_list.pop(current_index)
            closed_list.append(current_node)

            # Found the goal
            if current_node == goal_node:
                came_from = []
                cost = 0
                current = current_node
                #print("Explored Nodes: ", exp_nodes)
                print("Length of Explored Nodes Greedy: ", len(exp_nodes))

                while current is not None:
                    came_from.append(current.position)
                    cost += current.h
                    current = current.parent

                return came_from[::-1], cost, map_Temp  # Return reversed path

            # Generate children
            children = []

            for dx, dy in zip(delta_x, delta_y):  # Adjacent squares
                Temp_check_CL = 0
                Temp_check_OL = 0
                # Get node position
                next = (current_node.position[0] + dx, current_node.position[1] + dy)
                if not valid(next[0], next[1], map):
                    continue
                for repeat_list in closed_list:
                    if next == repeat_list.position:
                        Temp_check_CL = 1
                for repeat_list in open_list:
                    if next == repeat_list.position:
                        Temp_check_OL = 1
                if (Temp_check_CL != 1) & (Temp_check_OL != 1):
                    # Create new node
                    new_node = Node(current_node, next)
                    # Append
                    children.append(new_node)


            # Loop through children
            for child in children:

                # Child is on the closed list
                for closed_child in closed_list:
                    if child == closed_child:
                        continue
                # cost function
                # Create the f, g, and h values

                child.h = (abs(child.position[0] - goal_node.position[0])) + (abs(child.position[1] - goal_node.position[1]))
                map_Temp[child.position] =child.h
                #map_Temp[next[1], next[0]] = child.h
                exp_nodes.append([child.position])
                # Add the child to the open list
                open_list.append(child)


    elif typeofSearch == 'aStarE':
        #return None
        # Create start and end node
        start_node = Node(None, start)
        start_node.g = start_node.h = start_node.f = 0
        goal_node = Node(None, goal)
        goal_node.g = goal_node.h = goal_node.f = 0

        # Initialize both open and closed list
        open_list = []
        closed_list = []

        # Add the start node
        open_list.append(start_node)


        # Loop until you find the end
        while len(open_list) > 0:

            # Get the current node
            current_node = open_list[0]
            current_index = 0
            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index

            # Pop current off open list, add to closed list
            open_list.pop(current_index)
            closed_list.append(current_node)

            # Found the goal
            if current_node == goal_node:
                came_from = []
                cost=0
                current = current_node
                #print("Explored Nodes: ", exp_nodes)
                print("Length of Explored Nodes aStarE: ", len(exp_nodes))
                while current is not None:
                    came_from.append(current.position)
                    cost+=current.f
                    current = current.parent

                    #print('Cost Matrix:',map_Temp)
                return came_from[::-1],cost,map_Temp  # Return reversed path

            # Generate children
            children = []

            for dx, dy in zip(delta_x, delta_y):  # Adjacent squares
                Temp_check_CL = 0
                Temp_check_OL = 0
                # Get node position
                next = (current_node.position[0] + dx, current_node.position[1] + dy)
                if not valid(next[0], next[1],map):
                    continue
                for repeat_list in closed_list:
                    if next == repeat_list.position:
                        Temp_check_CL=1
                for repeat_list in open_list:
                    if next == repeat_list.position:
                        Temp_check_OL=1
                if (Temp_check_CL !=1) & (Temp_check_OL !=1):
                    # Create new node
                    new_node = Node(current_node, next)
                    # Append
                    children.append(new_node)


            # Loop through children
            for child in children:

                # Child is on the closed list
                for closed_child in closed_list:
                    if child == closed_child:
                        continue
                # cost function
                # Create the f, g, and h values
                child.g = current_node.g + 1
                child.h = ((child.position[0] - goal_node.position[0]) ** 2) + ((child.position[1] - goal_node.position[1]) ** 2)
                child.f = child.g + child.h

                # Child is already in the open list
                for open_node in open_list:
                    if child == open_node and child.g > open_node.g:
                        continue
                map_Temp[child.position] =child.f
                exp_nodes.append([child.position])

                # Add the child to the open list
                open_list.append(child)

    elif typeofSearch == 'aStarM':
        #return None
        # Create start and end node
        start_node = Node(None, start)
        start_node.g = start_node.h = start_node.f = 0
        goal_node = Node(None, goal)
        goal_node.g = goal_node.h = goal_node.f = 0

        # Initialize both open and closed list
        open_list = []
        closed_list = []

        # Add the start node
        open_list.append(start_node)
        # Loop until you find the end
        while len(open_list) > 0:

            # Get the current node
            current_node = open_list[0]
            current_index = 0
            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index

            # Pop current off open list, add to closed list
            open_list.pop(current_index)
            closed_list.append(current_node)

            # Found the goal
            if current_node == goal_node:
                came_from = []
                cost=0
                current = current_node
                #print("Explored Nodes: ", exp_nodes)
                print("Length of Explored Nodes aStarM: ", len(exp_nodes))
                while current is not None:
                    came_from.append(current.position)
                    cost+=current.f
                    current = current.parent

                    #print('Cost Matrix:',map_Temp)
                return came_from[::-1],cost,map_Temp  # Return reversed path

            # Generate children
            children = []

            for dx, dy in zip(delta_x, delta_y): # Adjacent squares
                Temp_check_CL = 0
                Temp_check_OL = 0
                # Get node position
                next = (current_node.position[0] + dx, current_node.position[1] + dy)
                if not valid(next[0], next[1],map):
                    continue
                for repeat_list in closed_list:
                    if next == repeat_list.position:
                        Temp_check_CL=1
                for repeat_list in open_list:
                    if next == repeat_list.position:
                        Temp_check_OL=1
                if (Temp_check_CL !=1) & (Temp_check_OL !=1):
                    # Create new node
                    new_node = Node(current_node, next)
                    # Append
                    children.append(new_node)


            # Loop through children
            for child in children:

                # Child is on the closed list
                for closed_child in closed_list:
                    if child == closed_child:
                        continue
                # cost function
                # Create the f, g, and h values
                child.g = current_node.g + 1
                child.h = (abs(child.position[0] - goal_node.position[0])) + (abs(child.position[1] - goal_node.position[1]))
                child.f = child.g + child.h

                # Child is already in the open list
                for open_node in open_list:
                    if child == open_node and child.g > open_node.g:
                        continue
                map_Temp[child.position] =child.f
                exp_nodes.append([child.position])
                # Add the child to the open list
                open_list.append(child)
        #return None

    elif typeofSearch == 'aStarCustomized':
        if start[0] > (abs(info[1] - info[0])//2):
            ObsCheck = 1
            Temp_P = (info[1], info[2])
        else: #move upward
            ObsCheck = 0
            Temp_P = (info[0], info[2])
        '''    
        dist_top = (math.sqrt((start[0] - info[0]) ** 2)) + (math.sqrt((start[1] - info[2]) ** 2))
        dist_bot = (math.sqrt((start[0] - info[1]) ** 2)) + (math.sqrt((start[1] - info[2]) ** 2))
        if dist_top > dist_bot: #move upward
            ObsCheck = 1
            Temp_P = (info[1], info[2])
        else: #move downward
            ObsCheck = 0
            Temp_P = (info[0], info[2])
            '''
        start_node = Node(None, start)
        start_node.g = start_node.h = start_node.f = 0
        goal_node = Node(None, goal)
        goal_node.g = goal_node.h = goal_node.f = 0

        # Initialize both open and closed list
        open_list = []
        closed_list = []

        # Add the start node
        open_list.append(start_node)

        # Loop until you find the end
        while len(open_list) > 0:

            # Get the current node
            current_node = open_list[0]
            current_index = 0
            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index

            # Pop current off open list, add to closed list
            open_list.pop(current_index)
            closed_list.append(current_node)

            # Found the goal
            if current_node == goal_node:
                came_from = []
                cost = 0
                current = current_node
                #print("Explored Nodes: ", exp_nodes)
                print("Length of Explored Nodes aStarCustomized: ", len(exp_nodes))

                while current is not None:
                    came_from.append(current.position)
                    cost += current.f
                    current = current.parent

                    # print('Cost Matrix:',map_Temp)
                return came_from[::-1], cost, map_Temp  # Return reversed path

            # Generate children
            children = []
            icheck = 0
            jcount=0
            if ObsCheck == 0: #move upward (down)
               delta_x = [ -1,0,0,1]
               delta_y = [ 0,-1,1,0]
            elif ObsCheck == 1: #move downward (up)
                delta_x = [0,0,1,-1]
                delta_y = [-1,1,0,0]

            icheck =0
            icheckL = 0
            for dx, dy in zip(delta_x, delta_y):  # Adjacent squares
                Temp_check_CL = 0
                Temp_check_OL = 0
                # Get node position
                next = (current_node.position[0] + dx, current_node.position[1] + dy)
                if not valid(next[0], next[1], map):
                    jcount+=1
                    continue

                if (((dx == delta_x[1] & dy == delta_y[1]) & (jcount >=3)) & (icheck==0)):
                   continue
                #if (((dx == delta_x[-1] & dy == delta_y[-1]) & (jcount < 3)) & (icheck==0)):
                #    continue

                if (((math.sqrt((next[0] - info[0]) ** 2)) + (math.sqrt((next[1] - info[2]) ** 2)) < 10) & (icheckL==0)):
                    icheck=1
                    icheckL=0
                    continue

                for repeat_list in closed_list:
                    if next == repeat_list.position:
                        Temp_check_CL = 1
                for repeat_list in open_list:
                    if next == repeat_list.position:
                        Temp_check_OL = 1
                if (Temp_check_CL != 1) & (Temp_check_OL != 1):
                    # Create new node
                    new_node = Node(current_node, next)
                    # Append
                    children.append(new_node)

            # Loop through children
            for child in children:

                # Child is on the closed list
                for closed_child in closed_list:
                    if child == closed_child:
                        continue
                # cost function
                # Create the f, g, and h values
                child.g = current_node.g + 1
                #child.h = (abs(child.position[0] - goal_node.position[0])) + (abs(child.position[1] - goal_node.position[1]))
                child.h = ((child.position[0] - goal_node.position[0]) ** 2) + ((child.position[1] - goal_node.position[1]) ** 2)
                child.f = child.g + child.h
                map_Temp[child.position] = child.f
                exp_nodes.append([child.position])
                # Add the child to the open list
                open_list.append(child)



