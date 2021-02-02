import multiprocessing
import time

start = time.perf_counter()

def do_something():
    print("Sleeping 5 Second..")
    time.sleep(5)
    print ("Done Sleeping..")

t1 = multiprocessing.Process(target = do_something)
t2 = multiprocessing.Process(target = do_something)



if __name__ == "__main__":

    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    #do_something()
    finish = time.perf_counter()
    
    print(f"Finished in {round(finish-start, 2)} seconds(s)")