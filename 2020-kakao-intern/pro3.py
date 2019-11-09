def solution(user_id, banned_id):
    ban_match_list = check_match_list(user_id, banned_id)
    
    return calculate_match(ban_match_list)
    

def calculate_match(ban_match_list):
    match_list_all = []
    make_match(match_list_all, [], 0, ban_match_list)
    
    result = 0
    match_set_list = []
    for match in match_list_all:
        match_set = set(match)
        # 이미 체크한거면 pass
        if match_set in match_set_list:
            continue
        
        match_set_list.append(match_set)
        
    return len(match_set_list)
    
def make_match(match_list_all, calculated_list, depth, ban_match_list):
    if depth == len(ban_match_list):
        match_list_all.append(tuple(calculated_list))
        return
    
    ban_match = ban_match_list[depth]
    for item in ban_match:
        if item in calculated_list:
            continue
        calculated_list.append(item)
        make_match(match_list_all, calculated_list, depth+1, ban_match_list)
        del calculated_list[depth]
    

def check_match_list(user_id, banned_id):
    result = []
    for ban in banned_id: 
        match_list = []
        for user_index in range(len(user_id)):
            user = user_id[user_index]
            if check_match(user, ban):
                match_list.append(user_index)
        
        result.append(match_list)
    
    return result

def check_match(user, ban):
    if len(user) != len(ban):
        return False
    
    for index in range(len(user)):
        user_char = user[index]
        ban_char = ban[index]
        
        if ban_char == '*':
            continue
        
        if user_char != ban_char:
            return False
        
    return True