## Implementation of KNN algorithms form scratch


"""for every example in the training set, calculate eucledien distance against the test example
sort distances in ascending order
get top k nearest neighbours
get index of the minimum distances
check which label has majority
return label with majority occurence """


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from functools import reduce
from math import sqrt
from collections import Counter
from numpy.ma.extras import average
from collections import defaultdict

res = defaultdict(dict)


def accuracy(TP, TN, FP, FN, **other):
    return (TP + TN) / (TP + TN + FP + FN)


def precision(TP, TN, FP, FN, **other):
    return TP / (TP + FP)


def recall(TP, TN, FP, FN, **other):
    return TP / (TP + FN)


def getMetrics():
    for i in range(3):
        res[i] = get_confusion_table(i)

        res[i]['accuracy'] = accuracy(**res[i])
        res[i]['precision'] = precision(**res[i])
        res[i]['recall'] = recall(**res[i])

    res["total_acc"] = average([(v['accuracy']) for k, v in res.items()])
    res["total_precision"] = average([(v['precision']) for k, v in res.items() if k in range(3)])
    res["total_recall"] = average([(v['recall']) for k, v in res.items() if k in range(3)])

    # Accuracy =  (TP +TN ) / (TP +TN+FP+FN)
    # Precision = TP / (TP+FP)
    # Recall = TP / (TP+FN)


def get_confusion_table(class_num):
    cls = class_num
    TPs = [(e, t) for e, t in zip(y_estimat, y_test) if e == t and t == cls]
    # Wrongly get classified as True for class c
    FPs = [(e, t) for e, t in zip(y_estimat, y_test) if e == t and t != cls]
    # correctly get classified as Flase for class c
    TNs = [(e, t) for e, t in zip(y_estimat, y_test) if e != t and t != cls]
    # wrongly estimated as False for class c
    FNs = [(e, t) for e, t in zip(y_estimat, y_test) if e != t and t == cls]
    return {'TP': len(TPs), 'TN': len(TNs), 'FP': len(FPs), 'FN': len(FNs)}

def eucledian_dist(x,y):
    return sqrt(reduce(lambda x,y:x+y ,[(x-y)**2 for x,y in zip(x,y)]))

def KNN(nPoint , k = 5):
    dist_vector = { i:eucledian_dist(d,nPoint) for i,d in enumerate(x_train)}
    #sort them based on minimum distance
    dist_vector = sorted(dist_vector.items() , key= lambda x: x[1])
    # Get insex of k nearest samples
    labels, dist = list(zip(*dist_vector[:k]))
    # # Get labels of k nearest samole
    k_n_l = y_train[list(labels)]
    ## Get the moset frequent label
    maxVotKnn = sorted(Counter(k_n_l).items(), key= lambda x:x[1], reverse=True )[0][0]
    # return knn
    return maxVotKnn



# Loading the IRIS
iris = load_iris()
print(iris.DESCR)
print("Features:       " , iris.feature_names)
print("Target classes: ",iris.target_names)
x_train,x_test, y_train , y_test =  train_test_split(iris.data ,iris.target , test_size= 0.7 , random_state = 20)
y_estimat = [KNN(q) for q in x_test]
getMetrics()

print(f"Train set is {(x_train.shape[0] / iris.data .shape[0])*100 :.2f} % whole dataset.")
print(f"Test  set is {(x_test.shape[0] / iris.data .shape[0])*100 :.2f} % whole dataset.")


