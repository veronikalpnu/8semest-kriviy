graph =                 [[0, 22, 98, 0, 0, 0, 0, 81], 
                        [22, 0, 0, 62, 87, 0, 0, 99], 
                        [98, 0, 0, 0, 0, 81, 82, 70], 
                        [0, 62, 0, 0, 99, 0, 97, 70], 
                        [0, 87, 0, 99, 0, 0, 13, 0], 
                        [0, 0, 81, 0, 0, 0, 9, 59], 
                        [0, 0, 82, 97, 13, 9, 0, 80], 
                        [81, 99, 70, 70, 0, 59, 80, 0]
                    ]; 


def sum_edges(graph):
    w_sum = 0
    l = len(graph)
    for i in range(l):
        for j in range(i,l):
            w_sum += graph[i][j]
    return w_sum
            

def dijktra(graph, source, dest):
    shortest = [0 for i in range(len(graph))]
    selected = [source]
    l = len(graph)
    #Base case from source
    inf = 10000000
    min_sel = inf
    for i in range(l):
        if(i==source):
            shortest[source] = 0 #graph[source][source]
        else:
            if(graph[source][i]==0):
                shortest[i] = inf
            else:
                shortest[i] = graph[source][i]
                if(shortest[i] < min_sel):
                    min_sel = shortest[i]
                    ind = i
                
    if(source==dest):
        return 0
    # Dijktra's in Play
    selected.append(ind) 
    while(ind!=dest):
        #print('ind',ind)
        for i in range(l):
            if i not in selected:
                if(graph[ind][i]!=0):
                    #Check if distance needs to be updated
                    if((graph[ind][i] + min_sel) < shortest[i]):
                        shortest[i] = graph[ind][i] + min_sel
        temp_min = 1000000
        #print('shortest:',shortest)
        #print('selected:',selected)
        
        for j in range(l):
            if j not in selected:
                if(shortest[j] < temp_min):
                    temp_min = shortest[j]
                    ind = j
        min_sel = temp_min
        selected.append(ind)
    
    return shortest[dest]
                            
#Finding odd degree vertices in graph

def get_odd(graph):
    degrees = [0 for i in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph)):
                if(graph[i][j]!=0):
                    degrees[i]+=1
                
    #print(degrees)
    odds = [i for i in range(len(degrees)) if degrees[i]%2!=0]
    #print('odds are:',odds)
    return odds

#Function to generate unique pairs
def gen_pairs(odds):
    pairs = []
    for i in range(len(odds)-1):
        pairs.append([])
        for j in range(i+1,len(odds)):
            pairs[i].append([odds[i],odds[j]])
        
    #print('pairs are:',pairs)
    #print('\n')
    return pairs


#Final Compiled Function
def Chinese_Postman(graph):
    odds = get_odd(graph)
    if(len(odds)==0):
        return sum_edges(graph)
    pairs = gen_pairs(odds)
    l = (len(pairs)+1)//2
    
    pairings_sum = []
    
    def get_pairs(pairs, done = [], final = []):
        
        if(pairs[0][0][0] not in done):
            done.append(pairs[0][0][0])
            
            for i in pairs[0]:
                f = final[:]
                val = done[:]
                if(i[1] not in val):
                    f.append(i)
                else:
                    continue
                
                if(len(f)==l):
                    pairings_sum.append(f)
                    return 
                else:
                    val.append(i[1])
                    get_pairs(pairs[1:],val, f)
                    
        else:
            get_pairs(pairs[1:], done, final)
            
    get_pairs(pairs)
    min_sums = []
    
    for i in pairings_sum:
        s = 0
        for j in range(len(i)):
            s += dijktra(graph, i[j][0], i[j][1])
        min_sums.append(s)
    
    added_dis = min(min_sums)
    chinese_dis = added_dis + sum_edges(graph)
    return chinese_dis    
    
    
print('Chinese Postman Distance is:',Chinese_Postman(graph))
