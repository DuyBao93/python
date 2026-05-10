
# Python program to illustrate the concept
# of threading
# importing the threading module
import threading
 
 
def print_cube(num, index):
    # function to print cube of given num
    for i in range(index):
        print("running process print_cube with %d times" %(i))
        print("%d times"%(i),"Cube: {}" .format(num * num * num))
    else:
        print("finish process print_cube")
 
 
def print_square(num, index):
    # function to print square of given num
    for i in range(index):
        print("running process print_square with %d times" %(i))
        print("%d times"%(i),"Square: {}" .format(num * num))
    else:
        print("finish process print_square")
 
 
if __name__ =="__main__":
    # creating thread
    t1 = threading.Thread(target=print_square, args=(10,10,))
    t2 = threading.Thread(target=print_cube, args=(10,10,))
 
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
 
    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
 
    # both threads completely executed
    print("Done!")