import random

count = 0
def step_function(input,theta):
    if(input >= theta):
        return 1
    return 0


def and_gate_perceptron():
    training_data=[[0,0,0],[0,1,0],[1,0,0],[1,1,1]]
    print(f'\t x \t y \t o')
    print(f'\t -----------------')
    for i in range(4):
        for j in range(3):
            print(f'\t',training_data[i][j] , end='')
        print()
    training(training_data)


def training(training_data):
    training_flag = True 
    w1 = 0.2
    w2 = 0.7
    thresold =0.5
    learning_rate=0.5
    while(training_flag==True):
        print (f'\t w1 \t w2')
        for i in range(4):
            for j in range(3):
                ya = step_function(training_data[i][0]*w1+training_data[i][1]*w2,thresold)
                yd = training_data[i][2]
                e = yd-ya
                training_flag=False
                if(e !=0):
                    training_flag = True
                    dw1 = learning_rate*training_data[i][0]*e
                    dw2 = learning_rate*training_data[i][1]*e
                    w1 += dw1
                    w2 += dw2
                    print(f'\t',round(w1,2),f'\t',round(w2,2))   
and_gate_perceptron()