def asal(e):
    if e<=1:return False
    for i in range(2,e):
        if e%i==0:
            return False
    return True
