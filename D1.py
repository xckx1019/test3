import numpy as np
from matplotlib import pyplot as plt

compressed = ['detector1_compressed_10.npy', 'detector1_compressed_30.npy', 'detector1_compressed_50.npy', 'detector1_compressed_70.npy', 'detector1_compressed_90.npy', 'detector1_compressed_100.npy']

for i in range(6):
    c = np.load(compressed[i])
    n = np.load('detector1_compressed_100.npy')
    features = np.concatenate((c, n), 0)
    #plt.hist(features)
    binary_gt = np.concatenate((np.ones((len(c), 1)), np.zeros((len(n), 1))), 0).astype(np.bool)
    fp_rate = []
    tp_rate = []


    for tau in np.arange(0, 3, 0.005):
        binary_prediction = np.greater(features, tau)
        confusion_matrix = np.zeros((2, 2), np.int)
        for t, p in zip(binary_gt, binary_prediction):
            confusion_matrix[int(t), int(p)] += 1

        #print "TP: {} TN: {} FP: {} FN: {}".format(confusion_matrix[1, 1], confusion_matrix[0, 0], confusion_matrix[0, 1], confusion_matrix[1, 0])
        fpr = confusion_matrix[0, 1].astype(float) / (confusion_matrix[0, 1] + confusion_matrix[0, 0]).astype(float)
        tpr = confusion_matrix[1, 1].astype(float) / (confusion_matrix[1, 1] + confusion_matrix[1, 0]).astype(float)
        #print "Tau: {} FPr: {} TPr: {}".format(tau, fpr, tpr)
        fp_rate.append(fpr)
        tp_rate.append(tpr)

    #plt.figure()

    plt.plot(fp_rate, tp_rate)

plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.legend(('10', '30', '50', '70', '90', '100'))
plt.show()
