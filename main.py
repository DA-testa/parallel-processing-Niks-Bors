# python3
import threading


def parallel_processing(n, m, data):
    output = [] #izveido sarakstu
    threads = [0]*n # saraksts ar n pavedieniem
    for i in data: #izveido ciklu
        nak=threads.index(min(threads)) # meklē pavedienu ar mazāki izpildes laiku
        output.append((nak,threads[nak])) # pievieno pāri izvades sarakstam ar pavediena numuru un izpildes laiku
        threads[nak]+=i #piešķir izpildes laiku pavedienam
    return output
    

    

def main():
    
    n,m =map(int,input().split()) #ievadīto datu lasīšana
    data=list(map(int,input().split()))
    
    

    

    
    result = parallel_processing(n,m,data) # izsauc funkciju ar ievades datiem
    
   
    for i in result: #izprintē rezultātu
        print(i[0],i[1])


if __name__ == "__main__":
    main()
