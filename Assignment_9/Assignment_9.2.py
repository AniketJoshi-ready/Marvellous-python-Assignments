import multiprocessing
result=[]
def square_list(LIST):
    global result
    for ele in LIST:
        ret=ele*ele
        result.append(ret)
    print(result)    
    return result
     
    
    
def main():
    data=[1,2,3,4,5,6]
    data2=[3,4,5,8,9,0,7,5]
    data3=[34,3,4,56,76,78,98,99]
    
    p1=multiprocessing.Process(target=square_list,args=(data,))
    p2=multiprocessing.Process(target=square_list,args=(data2,))
    p3=multiprocessing.Process(target=square_list,args=(data3,))

    p1.start()
    p1.join()


    p2.start()
    p2.join()


    p3.start()
    p3.join()





    print("end of main ")



if __name__=="__main__":
    main()