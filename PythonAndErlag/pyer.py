def sum(N):
    T = ""
    for i in range(5):
        if i == 4:
            T = T + str(int((N[i]*(N[i]+1))/2))
        else:
            T = T + str(int((N[i]*(N[i]+1))/2)) + ","
    export_file("E:\PythonAndErlag\sum.txt", T)
    print("Export Done")

def export_file(File , S):
    with open(File, 'w') as f:
        f.write(S)

if __name__ == "__main__":
    sum([5,3,10,20,21])
