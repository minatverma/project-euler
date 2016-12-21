def cycle_length(d):
    """Computes the length of the recurring cycle in the decimal representation
    of the rational number 1/d if any, 0 otherwise
    """
    if not isinstance(d, int) or d <= 0:
        raise ValueError("cycle_length(d): d must be a positive integer")
    rlist = []
    qlist_len = 0
    remainder = 1
    while remainder:
        remainder = remainder % d
        if remainder in rlist:
            return qlist_len - rlist.index(remainder)
        rlist.append(remainder)
        remainder *= 10
        qlist_len+=1
    return 0


if __name__ == '__main__':
    for d in range(1,20): #d = raw_input('d: ')
        try:
            print '1/%s =' % (d), cycle_length(int(d))
        except ValueError:
            print 'invalid input'
