# There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.
#
# You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.
#
#
#
#
#
#


# Example
# 1:
#
# Input: n = 3, flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]], src = 0, dst = 2, k = 1
# Output: 200
# Explanation: The
# graph is shown.
# The
# cheapest
# price
# from city
#
# 0
# to
# city
# 2
# with at most 1 stop costs 200, as marked red in the picture.
# Example
# 2:
#
# Input: n = 3, flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]], src = 0, dst = 2, k = 0
# Output: 500
# Explanation: The
# graph is shown.
# The
# cheapest
# price
# from city
#
# 0
# to
# city
# 2
# with at most 0 stop costs 500, as marked blue in the picture.
#
# Constraints:
#
# 1 <= n <= 100
# 0 <= flights.length <= (n * (n - 1) / 2)
# flights[i].length == 3
# 0 <= fromi, toi < n
# fromi != toi
# 1 <= pricei <= 104
# There
# will
# not be
# any
# multiple
# flights
# between
# two
# cities.
# 0 <= src, dst, k < n
# src != dst
from collections import deque


class Solution:
    # def findCheapestPrice(self, n: int, flights: list, src: int, dst: int, k: int) -> int:
    #     prices = [0]
    #     startpoints = [src]
    #     routes = [[src]]
    #     map_built = False
    #     while not map_built:
    #         map_built = True
    #         for fl in flights:
    #             if fl[0] in startpoints:
    #                 idxS = -1
    #                 for i in range(startpoints.count(fl[0])):
    #                     idxS = startpoints.index(fl[0], idxS+1)
    #                     if fl[1] not in startpoints:
    #                         if len(routes[idxS]) - 1 <= k:
    #                             startpoints.append(fl[1])
    #                             prices.append(prices[idxS] + fl[2])
    #                             rt = routes[idxS].copy()
    #                             rt.append(fl[1])
    #                             routes.append(rt)
    #                             map_built = False
    #                 else:
    #                     idxE = 0
    #                     for i in range(startpoints.count(fl[1])):
    #                         idxE = startpoints.index(fl[1], idxE)
    #                         idxS = -1
    #                         for j in range(startpoints.count(fl[0])):
    #                             idxS = startpoints.index(fl[0], idxS + 1)
    #                             rt = routes[idxS].copy()
    #                             rt.append(idxE)
    #                             if len(routes[idxS]) - 1 <= k and not rt in routes:
    #                                 startpoints.append(fl[1])
    #                                 prices.append(prices[idxS] + fl[2])
    #                                 routes.append(rt)
    #                                 map_built = False
    #     if not dst in startpoints:
    #         return -1
    #     else:
    #         result = prices[startpoints.index(dst)]
    #         idx = -1
    #         for i in range(startpoints.count(dst)):
    #             idx = startpoints.index(dst, idx + 1)
    #             price = prices[idx]
    #             if price < result:
    #                 result = price
    #         return result
    # def findCheapestPrice(self, n: int, flights: list, src: int, dst: int, k: int) -> int:
    #     routes = [[src]]
    #     prices = [0]
    #     map_built = False
    #     while not map_built:
    #         map_built = True
    #         for fl in flights:
    #             for idx, rt in enumerate(routes):
    #                 new_rt = rt.copy()
    #                 new_rt.append(fl[1])
    #                 if rt[-1] == fl[0] and len(rt)-1 <= k and fl[1] not in rt and new_rt not in routes:
    #                     new_price = prices[idx] + fl[2]
    #                     for idx, rt in enumerate(routes):
    #                         if rt[-1] == new_rt[-1] and len(rt) > len(new_rt) and prices[idx] > new_price:
    #                             routes.pop(idx)
    #                             prices.pop(idx)
    #                     routes.append(new_rt)
    #                     prices.append(new_price)
    #                     map_built = False
    #
    #
    #
    #
    #     print(routes)
    #     route_found = False
    #     price = max(prices)
    #     for idx, rt in enumerate(routes):
    #         if rt[-1] == dst and prices[idx] <= price:
    #             price = prices[idx]
    #             route_found = True
    #     return price if route_found else -1




    def findCheapestPrice(self, n: int, flights, src: int, dst: int, k: int) -> int:
        #make an adjaceny matrix
        #this will follow modified dijkatra's algo
        adj_matrix=[[] for i in range(n)]
        for u,v,w in flights:
            adj_matrix[u].append((v,w))
        #initialize infinite values for all nodes
        output=[float('inf') for i in range(n)]
        #start with source and hence mark it's weight as 0
        output[src]=0
        #construct graph
        graph=deque()
        #append the src , -1 as strp and 0 as cost to graph
        graph.append((src,-1,0))
        #now iterate over graph
        while graph:
            u,step,cost=graph.popleft()
            #if i have exhausted all steps
            if step>=k:
                continue
            for v,w in adj_matrix[u]:
                #classic dijkatr's algo
                if cost+w<output[v]:
                    output[v]=cost+w
                    graph.append((v,step+1,cost+w))
        if output[dst]==float('inf'):
            return -1
        return output[dst]



test = [
    ((3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1) , 200),
    ((3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0), 500),
    ((5, [[4, 1, 1], [1, 2, 3], [0, 3, 2], [0, 4, 10], [3, 1, 1], [1, 4, 3]], 2, 1, 1), -1),
    ((5, [[1, 2, 10], [2, 0, 7], [1, 3, 8], [4, 0, 10], [3, 4, 2], [4, 2, 10], [0, 3, 3], [3, 1, 6], [2, 4, 5]], 0, 4, 1), 5),
    ((4, [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], 0, 3, 1), 6),
    ((5, [[0, 1, 5], [1, 2, 5], [0, 3, 2], [3, 1, 2], [1, 4, 1], [4, 2, 1]], 0, 2, 2), 7),
    ((4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 2, 100]], 0, 3, 1), 101),
    ((10, [[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]], 6, 0, 7), 14),
    ((17, [[0,12,28],[5,6,39],[8,6,59],[13,15,7],[13,12,38],[10,12,35],[15,3,23],[7,11,26],[9,4,65],[10,2,38],[4,7,7],[14,15,31],[2,12,44],[8,10,34],[13,6,29],[5,14,89],[11,16,13],[7,3,46],[10,15,19],[12,4,58],[13,16,11],[16,4,76],[2,0,12],[15,0,22],[16,12,13],[7,1,29],[7,14,100],[16,1,14],[9,6,74],[11,1,73],[2,11,60],[10,11,85],[2,5,49],[3,4,17],[4,9,77],[16,3,47],[15,6,78],[14,1,90],[10,5,95],[1,11,30],[11,0,37],[10,4,86],[0,8,57],[6,14,68],[16,8,3],[13,0,65],[2,13,6],[5,13,5],[8,11,31],[6,10,20],[6,2,33],[9,1,3],[14,9,58],[12,3,19],[11,2,74],[12,14,48],[16,11,100],[3,12,38],[12,13,77],[10,9,99],[15,13,98],[15,12,71],[1,4,28],[7,0,83],[3,5,100],[8,9,14],[15,11,57],[3,6,65],[1,3,45],[14,7,74],[2,10,39],[4,8,73],[13,5,77],[10,0,43],[12,9,92],[8,2,26],[1,7,7],[9,12,10],[13,11,64],[8,13,80],[6,12,74],[9,7,35],[0,15,48],[3,7,87],[16,9,42],[5,16,64],[4,5,65],[15,14,70],[12,0,13],[16,14,52],[3,10,80],[14,11,85],[15,2,77],[4,11,19],[2,7,49],[10,7,78],[14,6,84],[13,7,50],[11,6,75],[5,10,46],[13,8,43],[9,10,49],[7,12,64],[0,10,76],[5,9,77],[8,3,28],[11,9,28],[12,16,87],[12,6,24],[9,15,94],[5,7,77],[4,10,18],[7,2,11],[9,5,41]], 13, 4, 13), 0)
]
s = Solution()
for t in test:
    print(s.findCheapestPrice(*t[0]), t[1])
