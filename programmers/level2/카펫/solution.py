def solution(brown, yellow):
    x_y_add = int((brown + 4) / 2)
    x_y_mul = 2*x_y_add + yellow - 4
    
    for y_prediction in range(1, int(x_y_add)):
        x_prediction = x_y_add - y_prediction
        if x_prediction * y_prediction == x_y_mul:
            return [x_prediction, y_prediction]
    
    # not reach here
    return []