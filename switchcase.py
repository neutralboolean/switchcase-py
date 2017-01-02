def switchcase(switch, experiment=0):
    fallthru = False
    #output = 'Test {0}'.format(experiment)
    #print(output)
    if "case0" == switch or fallthru == True:
        fallthru = True
        #do the thing
        #print("In case zero")
    if "case1" == switch or fallthru == True:
        fallthru = True
        #do the thing     
        #print("In case one")   
    if "case2" == switch or fallthru == True:
        fallthru = True
        #do the thing
        #print("In case two")
        return
    if "case3" == switch or fallthru == True:
        fallthru = True
        #do the thing
        #print("In case three")
        return
    else:
        #do the default thing
        print("Defaulting...")

if __name__ == "__main__":
    switchcase("case0", 1);
    print()
    switchcase("case1", 2)
    print()
    switchcase("case2", 3)
    print()
    switchcase("case3", 4)
    print()
    switchcase("case27", 5)
