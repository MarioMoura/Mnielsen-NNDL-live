import numpy as np
import struct
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter
import network

def imageprepare(argv):
    im = Image.open(argv).convert('L')
    pl = np.array(list(im.getdata()))
    pl = 255 - pl.reshape(784, 1)
    pl = pl / 256
    return pl

def array_print(argv):
    plt.imshow(argv.reshape(28,28), cmap="gray")
    plt.show()

def img_eval(arg):
    print(net.eval_one(imageprepare(arg)))

def vectorized_result(j):
    e = np.zeros((10, 1))
    e[j] = 1.0
    return e

with open('data/t10k-images-idx3-ubyte','rb') as f:
    magic, size = struct.unpack(">II", f.read(8))
    nrows, ncols = struct.unpack(">II", f.read(8))
    data = np.fromfile(f, dtype=np.dtype(np.uint8).newbyteorder('>'))
    data = data.reshape((size, 784, 1))
    data = data / 256

uniq_test = np.copy(data[0])

with open('data/t10k-labels-idx1-ubyte','rb') as f:
    l_magic, l_size = struct.unpack(">II", f.read(8))
    l_data = np.fromfile(f, dtype=np.dtype(np.uint8).newbyteorder('>'))
test_data = zip(data,l_data)
val_data = zip(data,l_data)

with open('data/train-images-idx3-ubyte','rb') as f:
    magic, size = struct.unpack(">II", f.read(8))
    nrows, ncols = struct.unpack(">II", f.read(8))
    data = np.fromfile(f, dtype=np.dtype(np.uint8).newbyteorder('>'))
    data = data.reshape((size, 784, 1))
    data = data / 256
with open('data/train-labels-idx1-ubyte','rb') as f:
    l_magic, l_size = struct.unpack(">II", f.read(8))
    l_data = np.fromfile(f, dtype=np.dtype(np.uint8).newbyteorder('>'))

vec_l_data = [vectorized_result(y) for y in l_data ]

j_data = zip(data,vec_l_data)
j_data = list(j_data)

net = network.Network([784, 10, 10])
net.SGD(j_data, 5, 10, 0.7, test_data=test_data)

# val_data = list(val_data)
# print(net.evaluate(val_data) )

# print(net.eval_one(uniq_test))

# array_print(image_t)

