class Node
  attr_accessor :neighbors, :val

  def initialize(val)
    @val = val
    @neighbors = []
  end


end

a = Node.new('a')
b = Node.new('b')
c = Node.new('c')
d = Node.new('d')
e = Node.new('e')
f = Node.new('f')

a.neighbors = [b, d]
b.neighbors = [c]
c.neighbors = [e, f]
d.neighbors = [b, f]

unvisited = [a, b, c, d, e, f]
visited = []
distance = {
  'a' => 0,
  'b' => Float::INFINITY,
  'c' => Float::INFINITY,
  'd' => Float::INFINITY,
  'e' => Float::INFINITY,
  'f' => Float::INFINITY,
}

def dijkstras(current_node, target_node, unvisited, visited, distance)

  until visited.include?(target_node) # keep running until visited target
    curr = unvisited.sort_by { |node| distance[node.val] }[0]

    curr.neighbors.each do |neighbor|
      if unvisited.include?(neighbor)
        distance[neighbor.val] = [distance[curr.val] + 1, distance[neighbor.val]].min
      end
    end

    visited += [ curr ] # add curr to visited
    unvisited -= [ curr ] # remove curr from unvisited
  end
end

def dijkstras_recurr(start_node, target_node, unvisited, visited, distance)
  return if visited.include?(target_node)

  start_node.neighbors.each do |neighbor|
    if unvisited.include?(neighbor)
      distance[neighbor.val] = [distance[start_node.val] + 1, distance[neighbor.val]].min
    end
  end

  visited += [ start_node ] # add start_node to visited
  unvisited -= [ start_node ] # remove start_node from unvisited

  sorted = unvisited.sort_by { |node| distance[node.val] }
  chosen = sorted[0]
  dijkstras_recurr(chosen, target_node, unvisited, visited, distance)
end

# dijkstras(a, f, unvisited, visited, distance)
# p distance

dijkstras_recurr(a, f, unvisited, visited, distance)
p distance
