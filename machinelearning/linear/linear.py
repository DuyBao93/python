import array as arr
import math
import matplotlib.pyplot as plt
import numpy as np 

# công thức tính Linear cho máy tự train

# Tính trung bình của 1 tập hợp
def do_average(arr):
    sum_arr = sum(arr)
    return sum_arr / len(arr)

# Tính phương sai của 1 tập hợp mảng theo công thức 
# Bước 1 :
#   tính trung bình của tập hợp số 
#   #   ví dụ [1, 2, 3, 4, 5] => trung bình là 3
# Bước 2 :
#   tạo 1 tập hợp mới với từng giá trị trong tập hợp trừ đi trung bình tập hợp 
#   #   ví dụ [1, 2, 3, 4, 5] trừ mỗi giá trị đi trung bình là 3 => [-2, -1, 0, 1, 2]
# Bước 3 :
#   tính tổng bình phương tất cả giá giá trị trong tập hợp 
#   #   ví dụ với tập hợp mới từ bước 2 [-2, -1, 0, 1, 2] => ta có ((-2)*(-2)) + ((-1)*(-1)) + ((0)*(0)) + ((1)*(1)) + ((2)*(2)) = 10
# Bước 4 :
#   Phương sai bằng kết quả bước 3 chia cho số lượng tập hợp trừ 1 
#   #   ví dụ ta có tập hợp [1, 2, 3, 4, 5] => ta só 5 phần tử nên công thức là 10/(5 -1) = 2.5
def do_variance(arr, average):
    variance_sum = 0
    for x in arr:
        variance_sum += ((x - average) *  (x - average))
    return variance_sum / (len(arr) - 1)
    

# Tính độ lệch chuẩn của 1 tập hợp
#   độ lệch chuẩn = căn bậc 2 từ kết quả mà độ lệnh chuẩn trả về
def do_standard_deviation(variance):
    return math.sqrt(variance)


# Tính độ hiệp phương sai của các tập hợp
def do_covariance(averageX, averageY, arrX, arrY) :
    covariance = 0
    for i in range(0, len(arrX)) :
        covariance += ((arrX[i] - averageX) * (arrY[i] - averageY))
    return covariance / (len(arrY) - 1)

# Tính hệ số tương quan của các tập hợp bằng công thức => độ tương quan = hiệp phương sai / ( dộ lệch chuẩn X * dộ lệch chuẩn Y )
def do_correlation(covariance, standardDeviationX, standardDeviationY):
    return covariance / (standardDeviationX * standardDeviationY)

# Tính Linear Regression ( Hồi Quy Tuyến Tính)
def linear_regression(arrX, arrY):
    averageX = do_average(arrX)
    averageY = do_average(arrY)
    # Tính phương sai
    varianceX = do_variance(arrX, averageX)
    varianceY = do_variance(arrY, averageY)
    # Tính độ lệch chuẩn
    standardDeviationX = do_standard_deviation(varianceX)
    standardDeviationY = do_standard_deviation(varianceY)
    # Tính hiệp phương sai
    covariance = do_covariance(averageX, averageY, arrX, arrY)
    # Tính độ tương quan bằng
    correlation = do_correlation(covariance, standardDeviationX, standardDeviationY)

    b1 = correlation * (standardDeviationY/standardDeviationX)
    b0 = averageY - (b1 * averageX)
    return ('d',[b0, b1])