# python3
import threading


def parallel_processing(n, m, data):
    output = []
    threads = [0]*n
    for i in data:
        nak=threads.index(min(threads))
        output.append((nak,threads[nak]))
        threads[nak]+=i
    return output
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n,m =map(int,input().split())
    data=list(map(int,input().split()))
    
    

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    #data = []

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for i in result:
        print(i[0],i[1])


if __name__ == "__main__":
    main()
