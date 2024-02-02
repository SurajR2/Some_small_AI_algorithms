#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<stdbool.h>

// Define a structure to hold weights
typedef struct {
    float w1;
    float w2;
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
void perceptron(int trainingData[4][3], Weights *weights) { 
    int i, x1, x2, y;
    weights->w1 = 0.3; 
    weights->w2 = 0.7;
    float threshold = 0.5, learningRate = 0.1;
    float ya, yd, err, dw1, dw2;
    int trainingFlag = true;

    printf("W1\tW2\n");
    printf("%0.2f\t%0.2f\n", weights->w1, weights->w2);

    do {
        trainingFlag = false;

        for (i = 0; i < 4; i++) {
            x1 = trainingData[i][0];
            x2 = trainingData[i][1];
            y = trainingData[i][2];
            ya = stepFunction((x1 * weights->w1 + x2 * weights->w2), threshold);
            yd = y;
            err = yd - ya;

            if (err != 0) {
                trainingFlag = true;
                dw1 = (float)learningRate * x1 * err;
                dw2 = (float)learningRate * x2 * err;
                weights->w1 += dw1;
                weights->w2 += dw2;
                printf("%0.2f\t%0.2f\n", weights->w1, weights->w2);
            }
        }
    } while (trainingFlag == true);
}

int main() {
    int i, j;

    Weights weights;  // Declare a structure variable
    float threshold = 0.5;

    printf("\nTraining Data:\n");

    int trainingData[4][3] = {{0, 0, 0}, {0, 1,1 }, {1, 0,1 }, {1, 1, 1}};

    printf("X\tY\tOutput\n");
    for (i = 0; i < 4; i++) {
        for (j = 0; j < 3; j++) {
            printf("%d\t", trainingData[i][j]);
        }
        printf("\n");
    }

    perceptron(trainingData, &weights);  // Pass the address of the weights structure

    printf("Updated Weights: w1:%0.2f\tw2:%0.2f\n", weights.w1, weights.w2);

    int testData[4][2] = {{0, 0}, {0, 1}, {1, 0}, {1, 1}};

    printf("\nTest Data:\n");
    printf("X\tY\tOutput\n");

    for (i = 0; i < 4; i++) {
        int result = stepFunction(testData[i][0] * weights.w1 + testData[i][1] * weights.w2, threshold);
        printf("%d\t%d\t%d\n", testData[i][0], testData[i][1], result);
    }

    getch();
    return 0;
}

