def solution(phone_book):
    phone_dict = set(phone_book)
    for phone in phone_book:
        for idx in range(1, 21):
            if idx >= len(phone):
                break
            
            if phone[:idx] in phone_dict:
                return False
        
    return True