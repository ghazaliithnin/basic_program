import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f"Sleeping {seconds} Second..")
    time.sleep(seconds)
    return (f"Done Sleeping..{seconds}")


if __name__ == "__main__":
    results =[]
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5,4,3,2,1]
        #secs = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,40,50,60]

        for sec in secs:
            f1=executor.submit(do_something,sec)
            #results.append(f1)
            #print(f1.result())
        # for f in concurrent.futures.as_completed(results):
        #     print(f.result())

        
    finish = time.perf_counter()
        
    print(f"Finished in {round(finish-start, 2)} seconds(s)")

# if __name__ == "__main__":

#     finish = time.perf_counter()
    
#     print(f"Finished in {round(finish-start, 2)} seconds(s)")