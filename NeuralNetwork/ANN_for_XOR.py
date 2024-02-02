import numpy as np
#using sigmoid activation function
def sigmoid(x):
    sig = 1 / (1 + np.exp(-x))
    return sig
#function for forward _propagation
def forward_propagation(inputs,Wij,Wjk,threshold):
     hidden_inputs = np.dot(inputs, Wij) - threshold       
     hidden_outputs = sigmoid(hidden_inputs)
     
     final_inputs =np.dot(hidden_outputs,Wjk) -threshold
     final_outputs= sigmoid(final_inputs)
     return final_outputs 
#calculating the error gradient of each nodes    
def error_gradient(predicted_output ,traget_output):
     error= traget_output - predicted_output
     return error

def back_propagation(inputs,hidden_outputs,final_outputs,error,Wjk,Wij):
    #calculating delta k
    output_error = error * final_outputs * (1-final_outputs)
    #calculating delta j 
    hidden_error = hidden_outputs*(1-hidden_outputs)* np.dot(Wjk,output_error[0])
     
    delta_wjk = alpha * hidden_outputs.reshape(-1, 1) * output_error
    Wjk += delta_wjk.flatten()

    delta_wij = alpha * np.outer(inputs, hidden_error)
    Wij += delta_wij
    
    return Wij, Wjk
#initialization 
alpha = 0.5
Wij= [[-0.289, 0.491], [-0.127, 0.567]]
Wjk = [-1.2, 1.2]
threshold = 0.5

#training data
inputs = [[0, 0],[0,1],[1,0],[1,1]]
outputs =[[0],[1],[1],[0]]

#training the artifical Neural Network
for epcoch in range(1000):
    for input_set, target_output in zip(inputs,outputs):
        input_set = np.array(input_set)
        hidden_inputs = np.dot(input_set, Wij)        
        hidden_outputs = sigmoid(hidden_inputs)
        final_outputs = forward_propagation(input_set,Wij,Wjk,threshold)

        error = error_gradient(final_outputs, target_output)
        Wij,Wjk=back_propagation(input_set, hidden_outputs, final_outputs, error,Wjk ,Wij)


test_inputs =[[0, 0],[0,1],[1,0],[1,1]]
correct_predictions=0
for test_input in test_inputs :
     predicted_output = forward_propagation(test_input,Wij,Wjk,threshold)

     print(f"Input: {test_input}, Predicted Output: {predicted_output}")


print("Updated Weights:")
print("Wjk:", Wjk)
print("Wij:", Wij)
