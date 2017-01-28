import numpy as np
from matplotlib import pyplot as plt
order = 2
compressed = ['detector4_compressed_10.npy', 'detector4_compressed_30.npy', 'detector4_compressed_50.npy', 'detector4_compressed_70.npy', 'detector4_compressed_90.npy', 'detector4_compressed_100.npy']

avg_n = []
for m in range(1338):
    n = np.load('detector4_compressed_100.npy')
    #n_plus = np.linalg.norm(n[m].flatten(), order)
    n_plus = np.min(n[m])
    avg_n.append(n_plus)

for i in range(6):
    c = np.load(compressed[i])
    avg_matrix = []

    for j in range(1338):
        #b = np.linalg.norm(c[j].flatten(), order)
        b = np.min(c[j])
        avg_matrix.append(b)

    features = np.concatenate((avg_matrix, avg_n), 0)
    '''
    plt.subplot(1, 2, 1)
    plt.hist(avg_matrix)
    plt.subplot(1, 2, 2)
    plt.hist(avg_n)
    plt.show()
    '''
    binary_gt = np.concatenate((np.ones((len(c), 1)), np.zeros((len(avg_n), 1))), 0).astype(np.bool)
    #plt.hist(binary_gt)
    #plt.show()
    fp_rate = []
    tp_rate = []

    for tau in np.linspace(np.min(features), np.max(features), 100):
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

    plt.plot(fp_rate, tp_rate)
plt.title('Min Greater Vertical')
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.legend(('10', '30', '50', '70', '90', '100'))
plt.show()