x=14.99
no_round_problem = False
while no_round_problem==False:
    y=round(x,1) # 14.9
    if y-x>0:
        x=x-(y-x)
        no_round_problem=False
    else:
        no_round_problem=True


print(x)
print(y)


