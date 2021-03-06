# -*- coding: utf-8 -*-
"""Titanic Deaths

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-zwpmkKqJuIvS2MBNyum8MDs0jnmChaQ
"""

from tensorflow import keras 
import tensorflow as tf
import numpy as np
import csv
print(tf.__version__)

num_features = 5
#getting the data
x_train = np.zeros((891, num_features), dtype=np.int8)
y_train = np.zeros((891, 1), dtype=np.int8)
mapsex = {"male":0, "female":1}
mapenter = {"S":0,"C":1,"Q":2}
with open("train.csv", newline='' ) as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  rowline=0
  for row in reader:
    if (rowline==0):
      rowline +=1
      next
    else:
      y_train[rowline-1,0]= int(row[1])
      x_train[rowline-1,0]=int(row[2]) 
      x_train[rowline-1, 1]= int(mapsex[row[4]])
      x_train[rowline-1, 2]= int(row[6])
      x_train[rowline-1, 3]= int(row[7])
      if row[11]=="":
        pass
      else:

        x_train[rowline-1, 4]= int(mapenter[row[11]])
      #string1 = str(row[9])
      #string1 = string1.replace(".","")  
      #x_train[rowline-1, 5]= float(string)
      rowline +=1

#getting test data
x_test = np.zeros((418,num_features),dtype=np.int64)
with open("test - test.csv", newline='' ) as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  rowline=0
  for row in reader:
    if (rowline==0):
      rowline +=1
      next
    else:
      x_test[rowline-1,0]=int(row[1]) 
      x_test[rowline-1, 1]= int(mapsex[row[3]])
      x_test[rowline-1, 2]= int(row[5])
      x_test[rowline-1, 3]= int(row[6])
      if row[10]=="":
        pass
      else:
        x_test[rowline-1, 4]= int(mapenter[row[10]])
      #string = str(row[8])
      #string = string.replace(".","")  
      #x_test[rowline-1, 5]= float(string) 
      
      rowline +=1

print(x_test)

model = keras.Sequential([
    keras.layers.Dense(64, activation=tf.nn.relu),
    keras.layers.Dense(64, activation=tf.nn.relu),
    keras.layers.Dense(2, activation=tf.nn.softmax)
])

model.compile(optimizer=tf.train.AdamOptimizer(),
             loss='sparse_categorical_crossentropy',
             metrics=['accuracy'])

model.fit(x_train, y_train, epochs=100)

predictions = model.predict(x_test)
submission = np.zeros((418,2),dtype=np.int32)
for z in range(892, 1310):
  submission[z-892, 0] = z
for i in range(1,417):
  
  if predictions[i, 0]< predictions[i, 1]:
    submission[i, 1] = 1
  else:
    submission[i, 1] = 0
    
for i in range(0, 418):
  print(submission[i, 0],end= "")
  print(",",end="")
  print(submission[i, 1])