elevator_states = [
    # State @ t=1
    '''xx.x.x.xDxx
    xx.x.x.x.xx
    xx.x.x.x.xx
    xx.xBx.x.xx
    xx.x.xCx.xx
    xxAx.x.x.xx''',
    # State @ t=2
    '''xx.x.x.x.xx
    xx.x.x.x.xx
    xxAx.x.x.xx
    xx.xBx.x.xx
    xx.x.xCx.xx
    xx.x.x.xDxx''',
    # State @ t=3
    '''xx.x.xCx.xx
    xx.x.x.x.xx
    xx.x.x.x.xx
    xxAxBx.x.xx
    xx.x.x.x.xx
    xx.x.x.xDxx''',
    # State @ t=4
    '''xx.x.xCx.xx
    xx.x.x.x.xx
    xx.xBx.xDxx
    xx.x.x.x.xx
    xxAx.x.x.xx
    xx.x.x.x.xx''',
    # State @ t=5
    '''xx.x.xCx.xx
    xx.x.x.xDxx
    xx.x.x.x.xx
    xx.x.x.x.xx
    xxAxBx.x.xx
    xx.x.x.x.xx'''
]


def findElevatorPath(elevator_states: list, starting_elevator: str, final_destination: str) -> str:
    """finding path to the final destination from starting_elevator in elevator_states"""

    def parseStates(elevator_states: list) -> dict:
        """converting strings elevator states to dict[elevator][time]=floor"""
        result = {}
        for state in elevator_states:
            floores = state.split()
            t = 1
            for floor in reversed(floores):
                floor = floor.replace('x', '')
                floor = floor.replace('.', '')
                elevators = list(floor)
                for elevator in elevators:
                    if elevator not in result:
                        result[elevator] = []
                    result[elevator].append(t)
                t += 1
        return result

    states = parseStates(elevator_states)

    def makeMove() -> str:
        """iterating valid elevator positions"""
        move = getNextPoint()
        if not move:
            state['time'] -= 1
            state['path'] = state['path'][0:-1]
            move = getPrevPoint()
        if move:
            state['path'].append(move)
            state['time'] += 1
            if pathFound():
                return ''.join(state['path'])
            return makeMove()
        else:
            return 'NO SUCCESSFUL ROUTE'

    def pathFound() -> bool:
        """check if we found a path"""
        floor = states[state['path'][-1]][state['time'] - 1]
        if state['time'] == state['destination_time'] and floor == state['destination_floor']:
            return True
        return False

    def getNextPoint():
        """iterating forward"""
        active_time = state['time'] + 1
        active_elevator = state['path'][-1]
        result = None
        if active_time <= state['destination_time']:
            active_floor = states[active_elevator][active_time - 1]
            for elevator in states:
                if states[elevator][active_time - 1] == active_floor:
                    result = elevator
                    break
        return result

    def getPrevPoint():
        """iterating backward"""
        state['time'] -= 1
        active_time = state['time']
        active_elevator = state['path'][-1]
        state['path'] = state['path'][0:-1]
        result = None
        if active_time > 0:
            active_floor = states[active_elevator][active_time]
            for elevator in states:
                if elevator <= active_elevator:
                    continue
                if states[elevator][active_time] == active_floor:
                    result = elevator
                    break
            if not result:
                result = getPrevPoint()
        return result

    state = {
        'time': 1,
        'path': [starting_elevator],
        'destination_floor': int(final_destination.split('-')[0]),
        'destination_time': int(final_destination.split('-')[1])
    }
    if pathFound():
        return str(state['path'])
    result = makeMove()
    return result


result = findElevatorPath(elevator_states, 'A', '5-5')  # expected AABDD
# result = findElevatorPath(elevator_states, 'D', '2-5')  # expected DDDBA
# result = findElevatorPath(elevator_states, 'C', '6-3')  # expected CCC
# result = findElevatorPath(elevator_states, 'A', '4-5')  # NO SUCCESSFUL ROUTE

print(result)
