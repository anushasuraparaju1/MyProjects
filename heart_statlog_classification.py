import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset=pd.read_csv("heart_statlog_cleveland_hungary_final.csv")
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values

#print(dataset.info())

from sklearn.model_selection import train_test_split as tts
x_train,x_test,y_train,y_test=tts(x,y,test_size=0.2,random_state=0)


from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.fit_transform(x_test)

'''print("----------LOGISTIC REGRESSION------------------")
from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression(random_state=0)'''



'''print("----------K NEAREST NEIGHBORS------------------")
from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=5)'''


'''print("-----------SUPPORT VECTOR CLASSIFICATION-----------")
print("****POLY KERNEL****")
from sklearn.svm import SVC
classifier=SVC(kernel="poly",random_state=0)'''

'''print("----------------NAIVE BAYESIAN------------------")
from sklearn.naive_bayes import GaussianNB
classifier=GaussianNB()'''

'''print("-------------------DECISION TREE-------------------")
from sklearn.tree import DecisionTreeClassifier
classifier=DecisionTreeClassifier(criterion="entropy",random_state=0)'''

print("----------------------RANDOM FOREST-------------------")
from sklearn.ensemble import RandomForestClassifier
classifier=RandomForestClassifier(n_estimators=15,criterion="entropy",random_state=0)

classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test)

from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,y_pred))

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,y_pred))
