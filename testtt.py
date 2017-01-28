import numpy as np
from PIL import Image
'''
block_0 = np.zeros((8, 8))
block_255 = 255*np.ones((8, 8))
block_h = np.hstack([block_255, block_0]*2)
block_v = np.hstack([block_0, block_255]*2)
matrix1 = np.concatenate((block_h, block_v), axis=0)
matrix = np.concatenate((matrix1, matrix1), axis=0)
img = Image.new("L", (32, 32))
'''
if __name__ == '__main__':
    g = np.asarray(dtype=np.dtype('uint8'), a=np.load('testImage.npy'))
    print(g)

    i = Image.fromarray(g, mode='L').convert('1')
    i.save('checker.jpg')



