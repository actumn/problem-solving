answer = []
def solution(k, room_number):
    tuple_list = [[1, k]]
    for room in room_number:
        tuple_index, tuple_item = check_room(tuple_list, room)
        check_in(tuple_list, room, tuple_index, tuple_item)
        
    return answer

def check_in(tuple_list, room, tuple_index, tuple_item):
    if room == tuple_item[0]:
        answer.append(tuple_item[0])
        tuple_item[0] += 1
        if tuple_item[0] > tuple_item[1]:
            del tuple_list[tuple_index]

        return
    
    if room == tuple_item[1]:
        answer.append(tuple_item[1])
        tuple_item[1] -= 1
        if tuple_item[0] > tuple_item[1]:
            del tuple_list[tuple_index]
        
        return
    
    if tuple_item[0] <= room and room <= tuple_item[1]:
        answer.append(room)
        del tuple_list[tuple_index]
        tuple_list[tuple_index:tuple_index] = [[tuple_item[0], room - 1], [room + 1, tuple_item[1]]]
        return
    
    if room < tuple_item[0]:
        answer.append(tuple_item[0])
        tuple_item[0] += 1
        if tuple_item[0] > tuple_item[1]:
            del tuple_list[tuple_index]
        
        return

def check_room(tuple_list, room):
    list_len = len(tuple_list)
    tuple_index = int(list_len / 2)
    while True:
        tuple_item = tuple_list[tuple_index]
        if tuple_item[0] <= room and room <= tuple_item[1]:
            return tuple_index, tuple_item
        
        if room < tuple_item[0]:
            if tuple_index == 0:
                return tuple_index, tuple_item
                
            left = tuple_list[tuple_index-1]
            if left[1] < room:
                return tuple_index, tuple_item
            
            tuple_index = int(tuple_index / 2)
            continue
        
        if tuple_item[1] < room:
            right = tuple_list[tuple_index+1]
            if room < right[0]:
                return tuple_index+1, right
            tuple_index = int((tuple_index + list_len) / 2)
            
        
    # not reached here
    return -1, [-1, -1]