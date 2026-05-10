def handle_float_sqrt(number, n):
    result = resultN  = checkResult = 1.0
    EPSILON = 0.000000000000001
    while (abs((checkResult)  - number) / number >= EPSILON):
        resultN = resultN/result
        result = (number / resultN  - result) / n + result
        checkResult = resultN = result
        for i in range (1, n):
            checkResult = checkResult * result
            resultN = resultN * result 
    return result
def my_sqrt(number, n):
    if (number == 1):
        return 1
    for i in range (2, int(number/n) + 1):
        resultPow = i
        for j in range (1, n):
            resultPow = resultPow * i
        if resultPow == number:
            return  i
    return handle_float_sqrt(number, n)
def main():
    n = 33
    print(n ** (1/5))
    result = my_sqrt(n, 5)
    print(" Ket qua can cua " + str(n) + " la : " + str(result))

if __name__ == "__main__":
    main()
