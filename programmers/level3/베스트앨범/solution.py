from collections import defaultdict
import heapq

def solution(genres, plays):
    n = len(genres)
    play_dict = defaultdict(int)
    play_heap_dict = defaultdict(list)
    for i in range(n):
        genre = genres[i]
        play = plays[i]
        play_dict[genre] += play
        heapq.heappush(play_heap_dict[genre], (-play, i))

    sorted_play_dict = sorted(play_dict.items(), key=lambda i: i[1], reverse=True)

    answer = []
    for genres in sorted_play_dict:
        genre = genres[0]
        heap = play_heap_dict[genre]

        for _ in range(2):
            if len(heap) > 0:
                answer.append(heapq.heappop(heap)[1])

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
