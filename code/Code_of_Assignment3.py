iteration=int(input('Enter total number of iteration: '))
for i in range(iteration):
    # total number of children in family
    n=int(input("Enter total number of children in family: "))
    # totla element in sample space
    s=2**n
    # probability of being all the children boys
    E=1/s
    # probability of at least one of them is boy
    F=(s-1)/s
    # probability of E intersectonn F
    EF=1/s
    E_given_F=EF/F
    print('Probaility of all the children are boys given that at least one of them is a boy:',E_given_F)