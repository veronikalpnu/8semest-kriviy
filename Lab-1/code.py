class Graph:
    def __init__(self, num_of_nodes):
        self.m_v = num_of_nodes
        self.m_edges = []
        self.m_component = {}
        
    def add_edge(self, u, v, weight):
        self.m_edges.append([u, v, weight])
        
    def find_component(self, u):
        if self.m_component[u] == u:
            return u
        return self.find_component(self.m_component[u])

    def set_component(self, u):
        if self.m_component[u] == u:
            return
        else:
            for k in self.m_component.keys():
                self.m_component[k] = self.find_component(k)
    
    def union(self, component_size, u, v):
        if component_size[u] <= component_size[v]:
            self.m_component[u] = v
            component_size[v] += component_size[u]
            self.set_component(u)
        elif component_size[u] >= component_size[v]:
            self.m_component[v] = self.find_component(u)
            component_size[u] += component_size[v]
            self.set_component(v)
        print(self.m_component)
    
    def boruvkamin(self):
        component_size = []
        mst_weight = 0

        minimum_weight_edge = [-1] * self.m_v

        for node in range(self.m_v):
            self.m_component.update({node: node})
            component_size.append(1)

        num_of_components = self.m_v

        print("---------Min Tree------------")
        while num_of_components > 1:
            for i in range(len(self.m_edges)):

                u = self.m_edges[i][0]
                v = self.m_edges[i][1]
                w = self.m_edges[i][2]

                u_component = self.m_component[u]
                v_component = self.m_component[v]

                if u_component != v_component:
                    if minimum_weight_edge[u_component] == -1 or \
                            minimum_weight_edge[u_component][2] > w:
                        minimum_weight_edge[u_component] = [u, v, w]
                    if minimum_weight_edge[v_component] == -1 or \
                            minimum_weight_edge[v_component][2] > w:
                        minimum_weight_edge[v_component] = [u, v, w]

            for node in range(self.m_v):
                if minimum_weight_edge[node] != -1:
                    u = minimum_weight_edge[node][0]
                    v = minimum_weight_edge[node][1]
                    w = minimum_weight_edge[node][2]

                    u_component = self.m_component[u]
                    v_component = self.m_component[v]

                    if u_component != v_component:
                        mst_weight += w
                        self.union(component_size, u_component, v_component)
                        print("Added edge [" + str(u) + " - "
                              + str(v) + "]\n"
                              + "Added weight: " + str(w) + "\n")
                        num_of_components -= 1

            minimum_weight_edge = [-1] * self.m_v
        print("----------------------------------")
        print("The total weight of the minimal spanning tree is: " + str(mst_weight))
    
    def boruvkamax(self):
        component_size = []
        mst_weight = 0

        maximum_weight_edge = [-1] * self.m_v

        for node in range(self.m_v):
            self.m_component.update({node: node})
            component_size.append(1)

        num_of_components = self.m_v

        print("---------Max Tree------------")
        while num_of_components > 1:
            for i in range(len(self.m_edges)):

                u = self.m_edges[i][0]
                v = self.m_edges[i][1]
                w = self.m_edges[i][2]

                u_component = self.m_component[u]
                v_component = self.m_component[v]

                if u_component != v_component:
                    if maximum_weight_edge[u_component] == -1 or \
                            maximum_weight_edge[u_component][2] < w:
                        maximum_weight_edge[u_component] = [u, v, w]
                    if maximum_weight_edge[v_component] == -1 or \
                            maximum_weight_edge[v_component][2] < w:
                        maximum_weight_edge[v_component] = [u, v, w]

            for node in range(self.m_v):
                if maximum_weight_edge[node] != -1:
                    u = maximum_weight_edge[node][0]
                    v = maximum_weight_edge[node][1]
                    w = maximum_weight_edge[node][2]

                    u_component = self.m_component[u]
                    v_component = self.m_component[v]

                    if u_component != v_component:
                        mst_weight += w
                        self.union(component_size, u_component, v_component)
                        print("Added edge [" + str(u) + " - "
                              + str(v) + "]\n"
                              + "Added weight: " + str(w) + "\n")
                        num_of_components -= 1

            maximum_weight_edge = [-1] * self.m_v
        print("----------------------------------")
        print("The total weight of the maximal spanning tree is: " + str(mst_weight))

g = Graph(8)
g.add_edge(0, 2, 38)
g.add_edge(0, 3, 95)
g.add_edge(0, 5, 1)
g.add_edge(0, 6, 57)
g.add_edge(1, 6, 36)
g.add_edge(1, 4, 79)
g.add_edge(1, 7, 19)
g.add_edge(2, 3, 51)
g.add_edge(2, 6, 44)
g.add_edge(3, 5, 44)
g.add_edge(4, 7, 48)
g.add_edge(4, 6, 41)
g.add_edge(4, 5, 93)
g.add_edge(5, 6, 1)

g.boruvkamin()
g.boruvkamax()
