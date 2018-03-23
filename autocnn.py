import os
import pandas as pd
import numpy as np
import numpy as np
import keras as k
import pandas as pd
import time
import matplotlib.pyplot as plt
from keras.models import Model
from keras.layers import Dense, Dropout, Flatten, merge, Input, Conv2D,Reshape
from keras.layers.convolutional import Convolution2D, MaxPooling2D, ZeroPadding2D, UpSampling2D
from keras.utils import np_utils
from keras.optimizers import SGD, Adadelta, Adam
from keras.layers.normalization import BatchNormalization
from keras.callbacks import EarlyStopping
from sklearn.model_selection import StratifiedKFold

name = os.listdir("/home/someone/桌面/phm/training")
train = pd.read_csv("/home/someone/桌面/phm/training.csv")
train = np.array(train[train.columns[1:3]])
feature = np.repeat(train[0,:].reshape(1,2),50,axis=0)



k = 0
dd = []
for i in name:
    data = pd.read_csv("/home/someone/桌面/phm/training/"+i)
    npdata = np.array(data)
    feature = np.repeat(train[k,:].reshape(1,2),50,axis=0)
    if npdata.shape[0]==216:
        dd.append(np.concatenate((npdata[0:50,:],feature),axis=1))
        dd.append(np.concatenate((npdata[50:100,:],feature),axis=1))
        dd.append(np.concatenate((npdata[100:150,:],feature),axis=1))
        dd.append(np.concatenate((npdata[150:200,:],feature),axis=1))
    else :
        dd.append(np.concatenate((npdata[0:50,:],feature),axis=1))
        dd.append(np.concatenate((npdata[50:100,:],feature),axis=1))
        dd.append(np.concatenate((npdata[100:150,:],feature),axis=1))
        dd.append(np.concatenate((npdata[150:200,:],feature),axis=1))       
        dd.append(np.concatenate((npdata[200:250,:],feature),axis=1)) 
        dd.append(np.concatenate((npdata[250:300,:],feature),axis=1)) 
        dd.append(np.concatenate((npdata[300:350,:],feature),axis=1)) 
    k = k+1
traindata  = np.array(dd)

traindata = traindata.reshape(traindata.shape[0],traindata.shape[1],traindata.shape[2],1)

name2 = os.listdir("/home/someone/桌面/phm/testing")
test = pd.read_csv("/home/someone/桌面/phm/testing.csv")
test = np.array(test[test.columns[1:3]])
feature2 = np.repeat(test[0,:].reshape(1,2),50,axis=0)
ddd = []
k = 0
for i in name:
    data = pd.read_csv("/home/someone/桌面/phm/testing/"+i)
    npdata = np.array(data)
    feature2 = np.repeat(test[k,:].reshape(1,2),50,axis=0)
    ddd.append(np.concatenate((npdata,feature),axis=1))
    k = k+1
    
testdata  = np.array(ddd)

testdata = testdata.reshape(testdata.shape[0],testdata.shape[1],testdata.shape[2],1)


#traindata = traindata.reshape(traindata.shape[0],traindata.shape[1]*traindata.shape[2])
#testdata = testdata.reshape(testdata.shape[0],testdata.shape[1]*testdata.shape[2])



nb_epoch = 500
batch_size = 50
train_label = traindata

input_1 = Input(shape=(50,92,1))
encoded = Convolution2D(	32,
				nb_row=5,
				nb_col=5,
				init = "orthogonal",
				border_mode = 'same',
				input_shape = (50, 92, 1),
				activation = "relu"
				)(input_1)
encoded = Convolution2D(	64,
				nb_row=3,
				nb_col=3,
				init = "orthogonal",
				border_mode = 'same',
				activation = "relu"
				)(encoded)

encoded = MaxPooling2D(pool_size=(2, 2), strides=None, border_mode='valid')(encoded)
encoded = Flatten()(encoded)
encoded = Dense(512, activation='relu')(encoded)
encoded = Dense(256, activation='relu')(encoded)


decoded = Dense(512, activation='relu')(encoded)
decoded = Dense(25*46, activation='relu')(decoded)
decoded = Reshape((25,46,1))(decoded)
decoded = UpSampling2D((2, 2))(decoded)
decoded = Convolution2D(	64,
				nb_row=3,
				nb_col=3,
				init = "orthogonal",
				border_mode = 'same',
				activation = "relu"
				)(decoded)
decoded = Convolution2D(	32,
				nb_row=3,
				nb_col=3,
				init = "orthogonal",
				border_mode = 'same',
				activation = "relu"
				)(decoded)
decoded = Convolution2D(	1,
				nb_row=3,
				nb_col=3,
				init = "orthogonal",
				border_mode = 'same',
				activation = "relu"
				)(decoded)




autoencoder = Model(input_1, decoded)

autoencoder.summary()
autoencoder.compile(optimizer='adadelta', loss='binary_crossentropy')

autoencoder.fit(traindata, traindata,
                epochs=500,
                batch_size=50,
                shuffle=True,
                validation_data=(traindata, traindata))

answer = autoencoder.predict(testdata)
answer = np.array(answer)
np.save("autocnnpre.npy",answer)
