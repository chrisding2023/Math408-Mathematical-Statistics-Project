import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import norm

normal_rv1 = np.random.normal(0,1,100)
normal_rv2 = np.random.normal(0,1.5,100)
cauchy_rv1 = np.random.normal(0,1,100)/np.random.normal(0,1,100)
cauchy_rv2 = (1.5*np.random.normal(0,1,100))/np.random.normal(0,1,100)
D_normal_rv1 = np.log(abs(normal_rv1))
D_normal_rv2 = np.log(abs(normal_rv2))
D_cauchy_rv1 = np.log(abs(cauchy_rv1))
D_cauchy_rv2 = np.log(abs(cauchy_rv2))

def procedureA(a,b):
    count = 0
    for i in range(0,100):
        if abs(a[i])<abs(b[i]):
            count += 1
    print("The probability is ", count/100)

def procedureB(a,b):
    sum_s_rv1 = 0
    sum_s_rv2 = 0
    for num in a:
        sum_s_rv1 += num**2
    for num in b:
        sum_s_rv2 += num**2
    if sum_s_rv1 < sum_s_rv2:
        print("True")
        return True
    if sum_s_rv1 > sum_s_rv2:
        print("False")
        return False

def procedureC(a,b):
    std_v1 = 0
    std_v2 = 0
    mean_v1 = sum(a)/200
    mean_v2 = sum(b)/100
    for num in a:
        std_v1 += (num-mean_v1)**2
    for nm in b:
        std_v2 += (nm-mean_v2)**2
    std_v1 = math.sqrt(std_v1/(100-1))
    std_v2 = math.sqrt(std_v2/(100-1))
    if std_v1 < std_v2:
        print("True")
        return True
    if std_v1 > std_v2:
        print("False")
        return False

# use 5% significance level fo the sign test
def procedureD_sign_test(a,b):
    neg = 0
    pos = 0
    diff = b-a
    for num in diff:
        if num>0:
            pos += 1
        if num<0:
            neg += 1
    number_of_examples = neg + pos
    dof = max([neg, pos])
    print("Number of correct Cases for sign test", pos)
    print("Number of false Cases for sign test", neg)

def Convert(tup,di):
    di = dict(tup)
    return di

def procedureD_rank_test(a,b):
    diff = b-a
    diff_pair ={}
    sum_of_neg = 0
    sum_of_pos = 0
    for key in diff:
        diff_pair[abs(key)] = key
    dic = {}
    diff_pair_sort = Convert(sorted(diff_pair.items(), key = lambda x :x[0]),dic)

    Index = {}
    for i in range(0,100):
        Index[i+1] = list(diff_pair_sort.values())[i]
    for key, value in Index.items():
        if value < 0:
            sum_of_neg += key
        if value > 0:
            sum_of_pos += key
    print("Number of correct Cases for wilcoxon signed-rank test", sum_of_pos)
    print("Number of false Cases for wilcoxon signed-rank test", sum_of_neg)

print("For cases where rv1 is standard normal variables, and rv2 is normal variable")
procedureA(normal_rv1,normal_rv2)
procedureB(normal_rv1,normal_rv2)
procedureC(normal_rv1,normal_rv2)
procedureD_sign_test(D_normal_rv1,D_normal_rv2)
procedureD_rank_test(D_normal_rv1,D_normal_rv2)
print("")
print("For case where rv1 is standard cauchy variables, and rv2 is cauchy variable")
procedureA(cauchy_rv1,cauchy_rv2)
procedureB(cauchy_rv1,cauchy_rv2)
procedureC(cauchy_rv1,cauchy_rv2)
procedureD_sign_test(D_cauchy_rv1,D_cauchy_rv2)
procedureD_rank_test(D_cauchy_rv1,D_cauchy_rv2)

cauchy_rv3 = np.random.normal(0,1,100000)/np.random.normal(0,1,100000)
cauchy_rv4 = np.random.normal(0, math.sqrt(1.5),100000)/np.random.normal(0,math.sqrt(1.5))
plt.hist(cauchy_rv3,bins=40,range=(-10,10))
plt.show()
plt.hist(cauchy_rv4,bins=40,range=(-10,10))
plt.show()
mean, std = norm.fit(cauchy_rv3)
print(mean, std)