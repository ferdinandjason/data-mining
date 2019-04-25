import itertools
import numpy as np
import matplotlib.pyplot as plt

# ensure the font has the required emojis!
import matplotlib
matplotlib.rc('font', family='DejaVu Sans')

EMOTIONS=["😐","😠","😏","😷","😨","😀","😢","😱"]

def get_face_label():
    global EMOTIONS
    return EMOTIONS

def plot_face(X, labels, title=None,xlabel=None, ylabel=None):
    global EMOTIONS
    x_min, x_max = np.min(X, 0), np.max(X, 0)
    X = (X - x_min) / (x_max - x_min)

    plt.figure()
    ax = plt.subplot(111)
    for i in range(X.shape[0]):
        plt.text(X[i, 0], X[i, 1], EMOTIONS[int(labels[i])],
                 color=plt.cm.Dark2((int(labels[i]) + 1) / 8.),
                 fontdict={'weight': 'bold', 'size': 20})

    if xlabel is not None:
        plt.xlabel(xlabel, fontsize=12)
    if ylabel is not None:
        plt.ylabel(ylabel, fontsize=12)
    if title is not None:
        plt.title(title, fontsize=15)

def plot_confusion_matrix(cm, classes, normalize=False, title='Confusion matrix', cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.figure()
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')