import time
import matplotlib.pyplot as plt

def TopDownFibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return TopDownFibonacci(n-1) + TopDownFibonacci(n-2)
    
def BottomUpFibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1    
    else:
        f = [ 0 for i in range(n) ]
        f[0] = 1
        f[1] = 1

        for i in range(2, n):
            f[i] = f[i-1] + f[i-2]

        return f[-1]
    
# Question 1 #
t_topdown = []
t_bottomup = []
x = []

t0 = time.time()

for i in range(100):
    print(i)
    try:
        t1 = time.time()

        TopDownFibonacci(i+1)

        t2 = time.time()

        BottomUpFibonacci(i+1)

        t3 = time.time()
        t_topdown.append(t2 - t1)
        t_bottomup.append(t3 - t2)
        x.append(i+1)
    except:
        pass

    # 12hr * 60min/hr * 60s/min = 43200s
    if time.time() - t0 >= 43200:
        print('maximum value of n: {}'.format(i))
        break

plt.plot(x, t_topdown, 'ro-', label='Top Down')
plt.plot(x, t_bottomup, 'go-', label='Bottom Up')
plt.title('TopDown vs. BottomUp',fontsize=12)
plt.xlabel('n')  
plt.ylabel('time(s)')
plt.legend(loc='upper right')
plt.show()

# # Question 2 #

# # f(n) = f(n-3)f(4) + f(n-4)f(3)
# def CountFibonacci4(n):
#     # 求f(n-3)
#     return BottomUpFibonacci(n-3)

    
# countlist = [ 0 for i in range(5, 51) ]
# x = [ i for i in range(5, 51) ]

# for i in range(5, 51):

#     countlist[i-5] = CountFibonacci4(i)


# plt.plot(x, countlist, 'ro-')
# plt.title('The times are F(4) computed',fontsize=12)
# plt.xlabel('n')  
# plt.ylabel('count')
# plt.show()








