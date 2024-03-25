import math
import random
import matplotlib.pyplot as plt


a = 0.9  # hệ số làm lạnh
T = 200 # Nhiệt độ ban đầu
min_toancuc = T  # Khởi tạo giải pháp tối ưu toàn cục
min_x = 0 # Giải pháp tối ưu toàn cục tương ứng với tọa độ X
n = 0  # số lần luyện
listn = []
list_min = []

def fun_obj(x1):  # hàm đối tượng
    tmp = (x1-2)**4 - 2.3*(x1-1)**3 - 15*((x1/5)**2) + 1
    #tmp = (x1**x1 -5*x1) * np.sin(x1**2)
    return tmp

while T > 1:  # Điều kiện chấm dứt

    min_cucbo = T
    t = T
    min_x1 = random.randint(0, 50)
    print("giá trị min x1: ", min_x1)
    for i in range(2):
        x1 = min_x1 + random.randint(-10, 10)
        y1 = fun_obj(x1)
        dt = y1 - min_cucbo
        if dt < 0 or dt == 0:
            t = y1
            min_x1 = x1
        else:
            index = -dt/t
            m = math.exp(index)
            n = random.randint(0, 100)
            if n <= m:
                t = y1
                min_x1 = x1
        min_cucbo = t
 

    if min_cucbo <= min_toancuc:
        min_toancuc = min_cucbo
        min_x = min_x1

    print('Giải pháp tối ưu cục bộ:', min_cucbo)
    T = T * a

    n += 1
    listn.append(T)
    list_min.append(min_cucbo)

print('Giải pháp tối ưu toàn cục:', min_toancuc)
print('Giá trị của X khi giải pháp tối ưu:', min_x)
print('Số lần luyện:',n)

X = list_x = []
Y = list_y = []
c = 0
for i in range(500):
    list_x.append(i/100)
    list_y.append(fun_obj(i/100))

#Show giải pháp tối ưu
plt.subplot(121)
plt.plot(X, Y)
plt.scatter(min_x, min_toancuc, c='b', label='Giải pháp tối ưu toàn cục')
plt.legend()

#Show Quá trình luyện kim
plt.subplot(122)
plt.plot(listn, list_min)
plt.gca()
plt.show()

