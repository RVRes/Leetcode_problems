# There is a road consisting of N segments, numbered from 0 to N-1,
# represenrtted by a string S. Segment S[K] of the road may contain a pothole,
# denoted by a single uppercase 'X' character, or may be a good segment without any potholes.
# Fixing machine can patch over three consecutive segments at once with asphalt and repair all the potholes
# located within each of these segments.
# Your task is to compute the minimum number of patches required to repair all the potholes in the road.

def solution(S):
    '''function to count minimum road (string .X.) patches'''
    patches_count = 0
    patch_place = 0
    road_len = len(S)
    while patch_place < road_len:
        try:
            patch_place = S.index('X')
        except ValueError:
            return patches_count
        else:
            patches_count += 1
            patch_place += 3
            if len(S) <= patch_place:
                break
            S = S[patch_place::]
    return patches_count


S = '.X..X'
print(2, solution(S), S)

S = 'X.XXXXX.X.'
print(3, solution(S), S)

S = 'XX.XXX..'
print(2, solution(S), S)

S = 'XXXX'
print(2, solution(S), S)

S = ''
print(0, solution(S), S)

S = '.'
print(0, solution(S), S)

S = 'X'
print(1, solution(S), S)

S = 'XXX'
print(1, solution(S), S)
S = '.XXX'
print(1, solution(S), S)
S = '.XXX.'
print(1, solution(S), S)
S = 'XXX.'
print(1, solution(S), S)
S = '.X'
print(1, solution(S), S)
S = 'X.'
print(1, solution(S), S)
S = 'X'
print(2, solution(S), S)
S = 'XXXXXXXXX.XXX'
print(4, solution(S), S)
S = '.....................................X'
print(1, solution(S), S)
