colors = ['red', 'blue', 'green']
states = ['a', 'b', 'c', 'd'] #a be andra, b be karnataka, c be tamil nadu and d be kerala
neighbors = {'a': ['b', 'c'], 'b': ['a', 'c', 'd'], 'c': ['a', 'b', 'd'], 'd': ['b', 'c']}
color_of_states = {}

def promising(state, color):
    for neighbor in neighbors.get(state, []):
        color_of_neighbor = color_of_states.get(neighbor)
        if color_of_neighbor == color:
            return False
    return True

def get_color_for_state(state):
    for color in colors:
        if promising(state, color):
            return color

def main():
    for state in states:
        color_of_states[state] = get_color_for_state(state)
    print("Colors assigned to states:")
    for state, color in color_of_states.items():
        print(f"{state}: {color}")

main()
