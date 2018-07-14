
def countNumOfUnique(int_list):
    a = set()
    for i in int_list:
        a.add(i)
    num_of_uniq = len(a)
    return num_of_uniq

