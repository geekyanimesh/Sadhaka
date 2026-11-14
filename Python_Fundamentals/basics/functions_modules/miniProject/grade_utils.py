
def calculate_average(marks):
    sum=0
    for i in marks:
        sum+=i
    k=len(marks)
    return sum/k

def get_result(average):
    if average>=40:
        return True
    else:
        return False

