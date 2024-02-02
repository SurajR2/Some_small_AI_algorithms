def step_function(input, threshold):
    return 1 if input > threshold else 0

def perceptron(training_data, weights):
    weights.w1 = 0.3
    weights.w2 = 0.7
    threshold = 0.5
    learning_rate = 0.1
    training_flag = True

    print("W1\tW2")
    print("{:.2f}\t{:.2f}".format(weights.w1, weights.w2))

    while training_flag:
        training_flag = False

        for data in training_data:
            x1, x2, y = data
            ya = step_function((x1 * weights.w1 + x2 * weights.w2), threshold)
            yd = y
            err = yd - ya

            if err != 0:
                training_flag = True
                dw1 = learning_rate * x1 * err
                dw2 = learning_rate * x2 * err
                weights.w1 += dw1
                weights.w2 += dw2
                print("{:.2f}\t{:.2f}".format(weights.w1, weights.w2))

class Weights:
    def __init__(self, w1=0.0, w2=0.0):
        self.w1 = w1
        self.w2 = w2

if __name__ == "__main__":
    print("\nTraining Data:")
    training_data = [
        [0, 0, 0],
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]

    for data in training_data:
        print("\t".join(map(str, data)))

    weights = Weights()
    perceptron(training_data, weights)

    print(f"\nUpdated Weights: w1:{weights.w1:.2f}\tw2:{weights.w2:.2f}")

    print("\nTest Data:")
    test_data = [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ]

    for data in test_data:
        result = step_function(data[0] * weights.w1 + data[1] * weights.w2, 0.5)
        print(f"{data[0]}\t{data[1]}\t{result}")
