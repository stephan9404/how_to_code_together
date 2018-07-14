def deleteOutlier(int_list):
    """Delelte outlier (not 10-20) int
    
    Arguments:
        int_list {[list of int]} -- [input list]
    
    Returns:
        [list of int] -- [outlier deleted list]
    """
    return [x for x in int_list if 10<=x and x<=20]