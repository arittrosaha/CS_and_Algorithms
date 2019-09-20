# https://leetcode.com/problems/evaluate-division/

def evaluate_division(equations, values, queries):
    def dfs_solve(operand1, operand2, visited):
        if operand1 not in graph or operand2 not in graph:
            return -1
        if operand1 == operand2:
            return graph[operand1][operand2] 
        if len(visited) == len(graph):
            return -1
        children = [*graph[operand1]]
        for child in children:
            if child not in visited:
                visited.add(operand1)
                prev_result = dfs_solve(child, operand2, visited)
                if prev_result is -1:
                    return prev_result
                else:
                    return prev_result * graph[operand1][child]


    graph = {}
    for idx, equation in enumerate(equations):
        operand1, operand2 = equation[0], equation[1]
        value = values[idx]

        if operand1 not in graph:
            graph[operand1] = {}
            graph[operand1][operand1] = 1
        graph[operand1][operand2] = value
        
        if operand2 not in graph:
            graph[operand2] = {}
            graph[operand2][operand2] = 1
        graph[operand2][operand1] = 1/value

    result = []
    for query in queries:
        result.append(dfs_solve(query[0], query[1], set()))
    print(graph)
    return result

print(evaluate_division(
    [["a", "b"], ["b", "c"]], 
    [2.0, 3.0], 
    [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
))

# DFS Find:
# ref -> https://www.youtube.com/watch?v=e2TYsOs-Sfw&list=PLT60GvW9iSsFB0tzLXbxg4B-bavCPNUrk&index=11&t=2611s

# Union Find:
# ref -> https://zxi.mytechroad.com/blog/graph/leetcode-399-evaluate-division/
# ref -> https://www.youtube.com/watch?v=wU6udHRIkcc&list=PLT60GvW9iSsFB0tzLXbxg4B-bavCPNUrk&index=10&t=0s
