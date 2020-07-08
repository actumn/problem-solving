import queue

def check_diff(word_a, word_b):
    diff = 0
    for idx in range(len(word_a)):
        if word_a[idx] != word_b[idx]:
            diff += 1
        
    return diff

def make_2dvector(words):
    result = []
    for word in words:
        links = [0 for _ in range(len(words))]
        
        for idx, word2 in enumerate(words):
            if word is word2:
                links[idx] = 1
                continue
            
            if check_diff(word, word2) == 1:
                links[idx] = 1
            
        result.append(links)
        
    return result


# a = make_2dvector(["hit", "hot", "dot", "dog", "lot", "log", "cog"])
# for i in a:
#     print(i)



def solution(begin, target, words):
    if target not in words:
        return 0
    
    target_idx = words.index(target) + 1
    paths = make_2dvector([begin, *words])
    n = len(paths)
    
    distance = [-1 for _ in range(n)]
    path_queue = queue.Queue()
    path_queue.put(0)
    distance[0] = 0
    while not path_queue.empty():
        here = path_queue.get()
        for there in range(n):
            if paths[here][there] == 1 and distance[there] == -1:
                path_queue.put(there)
                distance[there] = distance[here] + 1
    
    return distance[target_idx]