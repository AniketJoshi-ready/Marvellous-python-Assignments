def chkprime(num):
    label=True                                 # must must must step bhiduuu should globally declare 
    if num==1 or num==0:
        pass              # this is necessery becoz when i call this function aand if list contain 1 or 0 then it should be skipped samje kya bhiduuu
        #print(" 0 and 1 are not considered as prime number ")
    else:
        for i in range (2,num):
            if num%i==0:
                label=False
        return label
    '''if label==False:
        print(num, "  not a  prime number")
    else:
        print(num," is  prime number")    '''


    