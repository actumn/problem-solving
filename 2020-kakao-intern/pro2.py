def solution(s):
    tuple_list = parse_string(s)
    tuple_dict = {}
    answer_len = len(tuple_list)
    answer = [0 for _ in range(answer_len)]
    
    for tuple_item in tuple_list:
        check_dict(tuple_dict, tuple_item)
    
    for item, index in tuple_dict.items():
        answer[answer_len-index] = item
        
    print(tuple_dict)
    return answer

def check_dict(tuple_dict, tuple_item):
    for item in tuple_item:
        if item in tuple_dict:
            tuple_dict[item] += 1
        else:
            tuple_dict[item] = 1

def parse_string(s):
    split_s = s[2:-2].split('},{')
    
    result = []
    for split_item in split_s:
        result.append(list(map(int, split_item.split(','))))
        
    return result