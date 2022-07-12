from sklearn import metrics
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

actual =     ["p", "n", "n", "p", "n"]
prediction = ["p", "n", "p", "p", "n"]


print("\n")

mx = metrics.confusion_matrix(actual, prediction, labels=["p", "n"])
print(mx)
print(metrics.classification_report(actual, prediction, labels=["p", "n"]))

mx = mx.astype('float') / mx.sum(axis=1)[:, np.newaxis]
fig, ax = plt.subplots(figsize=(5, 5))
sns.heatmap(mx, annot=True, fmt='.2f', xticklabels=["p", "n"], yticklabels=["p", "n"])
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.show(block=True)
