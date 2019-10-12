# https://leetcode.com/problems/two-city-scheduling/

def two_city_scheduling_cost(costs):
    costs.sort(key=lambda c: c[0]-c[1])
    total_cost = 0
    for i in range(len(costs)):
        if i < (len(costs) / 2):
            total_cost += costs[i][0]
        else:
            total_cost += costs[i][1]
    return total_cost


# print(two_city_scheduling_cost([[10, 20], [30, 200], [400, 50], [30, 20]]))
