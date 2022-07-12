
import numpy as np
from random import randrange


def NormalizeData(data):
    if np.max(data) == np.min(data):
        return np.full(data.shape, 1 / data.__len__())
    return (data + min(data)) / sum(data + min(data))


def randomClass(student: list):
    while True:
        rand = randrange(0, 30)
        if "c" + rand.__str__() not in student:
            return "c" + rand.__str__()
