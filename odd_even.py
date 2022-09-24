'''this is costom function'''
def number(*num):
    even=[]
    odd=[]
    for i in num:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return even , odd
