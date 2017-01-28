import numpy as np
from matplotlib import pyplot as plt
order = 10
compressed = ['detector3_compressed_10.npy', 'detector3_compressed_30.npy', 'detector3_compressed_50.npy', 'detector3_compressed_70.npy', 'detector3_compressed_90.npy', 'detector3_compressed_100.npy']
compressed2 = ['detector4_compressed_10.npy', 'detector4_compressed_30.npy', 'detector4_compressed_50.npy', 'detector4_compressed_70.npy', 'detector4_compressed_90.npy', 'detector4_compressed_100.npy']

avg_combine = []

for a in range(1338):
    n = np.load('detector3_compressed_100.npy')
    m = np.load('detector4_compressed_100.npy')
    combine_original = n + m
    #combine_plus = np.linalg.norm(combine_original[a].flatten(), order)
    combine_plus = np.max(combine_original[a])
    avg_combine.append(combine_plus)

for i in range(6):
    c = np.load(compressed[i]) + np.load(compressed2[i])
    avg_matrix = []

    for j in range(1338):
        #b = np.linalg.norm(c[j].flatten(), order)
        b = np.max(c[j])
        avg_matrix.append(b)

    features = np.concatenate((avg_matrix, avg_combine), 0)
    '''
    plt.figure()
    #plt.subplot(1, 2, 1)
    plt.hist(avg_matrix)
   # plt.subplot(1, 2, 2)
    plt.hist(avg_n)
    plt.show()
'''
    binary_gt = np.concatenate((np.ones((len(c), 1)), np.zeros((len(avg_combine), 1))), 0).astype(np.bool)
    # plt.hist(binary_gt)
    # plt.show()
    fp_rate = []
    tp_rate = []

    for tau in np.linspace(np.min(features), np.max(features), 100):
        binary_prediction = np.greater(features, tau)
        confusion_matrix = np.zeros((2, 2), np.int)
        for t, p in zip(binary_gt, binary_prediction):
            confusion_matrix[int(t), int(p)] += 1

        # print "TP: {} TN: {} FP: {} FN: {}".format(confusion_matrix[1, 1], confusion_matrix[0, 0], confusion_matrix[0, 1], confusion_matrix[1, 0])
        fpr = confusion_matrix[0, 1].astype(float) / (confusion_matrix[0, 1] + confusion_matrix[0, 0]).astype(float)
        tpr = confusion_matrix[1, 1].astype(float) / (confusion_matrix[1, 1] + confusion_matrix[1, 0]).astype(float)
        # print "Tau: {} FPr: {} TPr: {}".format(tau, fpr, tpr)
        fp_rate.append(fpr)
        tp_rate.append(tpr)

    plt.plot(fp_rate, tp_rate)
plt.title('Norm = 10 Greater Combined')
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.legend(('10', '30', '50', '70', '90', '100'))
plt.show()