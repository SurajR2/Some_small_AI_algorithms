import numpy as np
import math

values = [8,9,10,11,12,13]
frequencies = [7,10,21,23,14,8]
cumulative_frequency=[]
sum=0
sum_of_frequencies =0
diff=[]
x_sqaure = 0
y_square =0
print(' X2 Y2')
for i in range(len(values)):
    sum_of_frequencies += frequencies[i]
    cumulative_frequency.append(sum_of_frequencies)
    sum += values[i]*frequencies[i]
    print( '',pow(values[i],2),pow(frequencies[i],2) )
    
    mean = sum / sum_of_frequencies
    median = (sum_of_frequencies+1)/2



print('Mean:',round(mean,3))


for i in range(len(values)):
    diff.append(np.abs(cumulative_frequency[i]-median))
index = np.argmin(diff)
print('median:',values[index])


print('mode:', 3*values[index]-2*mean)



min_value = values[0]
max_value = values[0]
for i in range (len(values)):
    variance =pow((values[i] - mean),2)/(len(values)-1)
    if(values[i] < min_value):
        min_value= values[i]
    if(values[i] > max_value):
        max_value= values[i]


range = max_value - min_value
print ('variance:',variance)
print ('Standard Deviation:',math.sqrt(variance))
print('range:', range)





