import numpy as np
import matplotlib.pyplot
import time

backLegSensorValues = np.load('./data/values.npy')
lst = backLegSensorValues.files

for item in lst:
    print(item)
    print(backLegSensorValues[item])

frontLegSensorValues = np.load('./data/fvalues.npy')
flst = frontLegSensorValues.files

for item in flst:
    print(item)
    print(frontLegSensorValues[item])

matplotlib.pyplot.plot(backLegSensorValues)
matplotlib.pyplot.plot(frontLegSensorValues)

matplotlib.pyplot.show()