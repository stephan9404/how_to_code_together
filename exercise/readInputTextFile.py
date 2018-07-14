def readInputTextFile(filename):
    """Read input file(filename) and return list of int
    
    Arguments:
        filename {[string]} -- [name of input file]
    
    Returns:
        [list of int] -- [input list]
    """

    f = open(filename,'r')

    read = f.readline()
    res = read.split(" ")

    res = list(map(lambda x: int(x), res))
    
    return res

print(readInputTextFile('input_ex.txt'))
