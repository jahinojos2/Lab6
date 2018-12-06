class EdgeWeight:
    def __init__(self, from_vertex, to_vertex, weight):
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
        self.weight = weight

    # Only edge weights are used in the comparisons that follow

    def __eq__(self, other):
        return self.weight == other.weight

    def __ge__(self, other):
        return self.weight >= other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __le__(self, other):
        return self.weight <= other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __ne__(self, other):
        return self.weight != other.weight


# Stores a collection of vertex sets, which collectively store all vertices in a
# graph. Each vertex is in only one set in the collection.
class VertexSetCollection:
    def __init__(self, all_vertices):
        self.vertex_map = dict()
        for vertex in all_vertices:
            vertex_set = set()
            vertex_set.add(vertex)
            self.vertex_map[vertex] = vertex_set

    def __len__(self):
        return len(self.vertex_map)

    # Gets the set containing the specified vertex
    def get_set(self, vertex):
        return self.vertex_map[vertex]

    # Merges two vertex sets into one
    def merge(self, vertex_set1, vertex_set2):
        # First create the union
        merged = vertex_set1.union(vertex_set2)
        # Now remap all vertices in the merged set
        for vertex in merged:
            self.vertex_map[vertex] = merged