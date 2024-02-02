#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

// Define a structure to hold weights
typedef struct {
    float w1;
} Weights;

// Step function
int stepFunction(float input, float threshold) {
    if (input > threshold) {
        return 1;
    } else {
        return 0;
    }
}

// Perceptron learning algorithm
void perceptron(int trainingData[2][2], Weights *weights) { 
    int i, x, y;
    weights->w1 = 0.7; 
    float threshold = 0.25, learningRate = 1;
    float ya, yd, err, dw1;
    int trainingFlag = true;
    int maxIterations = 1000; // Maximum number of iterations
    int iterationCount = 0; // Counter for iterations

    printf("Initial Weight: %0.2f\n", weights->w1);

    while (trainingFlag && iterationCount < maxIterations) {
        trainingFlag = false;

        for (i = 0; i < 2; i++) {
            x = trainingData[i][0];
            y = trainingData[i][1];
            ya = stepFunction((x * weights->w1), threshold);
            yd = y;
            err = yd - ya;

            if (err != 0) {
                trainingFlag = true;
                dw1 = (float)learningRate * x * err;
                weights->w1 += dw1;
                printf("Updated Weight: %0.2f\n", weights->w1);
            }
        }

        iterationCount++;
    }
}

int main() {
    int i,j;

    Weights weights;  // Declare a structure variable

    printf("\nTraining Data for NOT Gate:\n");

    int trainingData[2][2] = {{0, 1}, {1, 0}};

    printf("X\tOutput\n");
    for (i = 0; i < 2; i++) {
        for ( j = 0; j < 2; j++) {
            printf("%d\t", trainingData[i][j]);
        }
        printf("\n");
    }

    perceptron(trainingData, &weights);  // Pass the address of the weights structure

    printf("Updated Weight: %0.2f\n", weights.w1);

    printf("\nTest Data for NOT Gate:\n");
    printf("X\tOutput\n");

    int testData[2] = {0, 1};

    for (i = 0; i < 2; i++) {
        int result = stepFunction(testData[i] * weights.w1, 1.25);
        printf("%d\t%d\n", testData[i], result);
    }

    return 0;
}

