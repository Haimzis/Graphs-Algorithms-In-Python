from GraphAlgorithms import sorts, searches


def take_input():
    user_input = ''
    while True:
        user_input = input("would you like to continue? [Y - yes / N - No]\n")
        if user_input.lower() == 'n' or user_input.lower() == 'y':
            break
        else:
            print("wrong input!")
            continue
    return user_input


def print_graph(graph):
    print("The vertex of the graph are:")
    for counter, vertex in enumerate(graph.keys()):
        print(f"{counter+1}. {vertex}:")
        for adj in graph[vertex]:
            print(f"({vertex},{adj})")


def create_graph():
    end_of_input = 'y'
    graph = {}
    print("Enter Vertexes:")
    counter = 0
    while end_of_input == 'y':
        new_vertex = input(f"vertex number {counter}\n")
        add_vertex(graph, new_vertex)
        end_of_input = take_input()
        counter += 1
    end_of_input = 'y'
    counter = 0
    while end_of_input == 'y':
        print(f"edge number {counter}, enter (vertex,adjacent)")
        a = input("enter vertex\n")
        b = input("enter adjacent\n")
        add_edge(graph, a, b)
        end_of_input = take_input()
        counter += 1
    return graph


def add_edge(graph,vertex,adjacent):
    graph[vertex].append(adjacent)


def add_vertex(graph,new_vertex):
    graph[new_vertex] = []


if __name__ == '__main__':
    my_graph = create_graph()
    print_graph(my_graph)
    print(sorts.topological_sorting(my_graph))
    print(searches.dfs(my_graph))
    print(searches.bfs(my_graph, 'a'))
