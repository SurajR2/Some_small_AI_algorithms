#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define N 3

// Structure to represent a puzzle state
typedef struct {
    int puzzle[N][N];
} PuzzleState;

// Node structure for the priority queue
typedef struct {
    int priority;
    int cost;
    PuzzleState state;
} Node;

// Function to calculate the Manhattan distance heuristic
int manhattan_distance(PuzzleState state, PuzzleState goal_state) {
    int distance = 0;
    int i, j;
    for ( i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            if (state.puzzle[i][j] != -99) {
                int value = state.puzzle[i][j];
                int goal_i, goal_j;
                for (goal_i = 0; goal_i < N; goal_i++) {
                    for (goal_j = 0; goal_j < N; goal_j++) {
                        if (value == goal_state.puzzle[goal_i][goal_j])
                            break;
                    }
                    if (goal_j < N)
                        break;
                }
                distance += abs(i - goal_i) + abs(j - goal_j);
            }
        }
    }
    return distance;
}

// Function to swap two puzzle elements
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Function to perform A* algorithm
PuzzleState astar(PuzzleState initial_state, PuzzleState goal_state) {
    Node priority_queue[N * N * N * N];
    int i , j;
    int front = 0, rear = 0;

    priority_queue[rear].priority = manhattan_distance(initial_state, goal_state);
    priority_queue[rear].cost = 0;
    priority_queue[rear].state = initial_state;
    rear++;

    PuzzleState visited[N * N * N * N];
    int visitedCount = 0;

    while (front < rear) {
        Node current = priority_queue[front++];
        PuzzleState current_state = current.state;

        printf("Step: %d\n", current.cost);
        for ( i = 0; i < N; i++) {
            for ( j = 0; j < N; j++) {
                printf("%d ", current_state.puzzle[i][j]);
            }
            printf("\n");
        }
        printf("\n");

        if (memcmp(&current_state, &goal_state, sizeof(PuzzleState)) == 0) {
            return current_state;
        }
		int k;
        int visitedFlag = 0;
        for (k = 0; k < visitedCount; k++) {
            if (memcmp(&current_state, &visited[k], sizeof(PuzzleState)) == 0) {
                visitedFlag = 1;
                break;
            }
        }

        if (visitedFlag)
            continue;

        visited[visitedCount++] = current_state;
		
        for ( i = 0; i < N; i++) {
            for ( j = 0; j < N; j++) {
                if (current_state.puzzle[i][j] == -99) {
                    for (char d : "UDLR") {
                        PuzzleState next_state = current_state;

                        if ((d == 'U' && i > 0) || (d == 'D' && i < N - 1) ||
                            (d == 'L' && j > 0) || (d == 'R' && j < N - 1)) {
                            int new_i = i + (d == 'D') - (d == 'U');
                            int new_j = j + (d == 'R') - (d == 'L');
                            swap(&next_state.puzzle[i][j], &next_state.puzzle[new_i][new_j]);

                            int visitedFlag = 0;
                            for (int k = 0; k < visitedCount; k++) {
                                if (memcmp(&next_state, &visited[k], sizeof(PuzzleState)) == 0) {
                                    visitedFlag = 1;
                                    break;
                                }
                            }

                            if (!visitedFlag) {
                                priority_queue[rear].priority = current.cost + 1 + manhattan_distance(next_state, goal_state);
                                priority_queue[rear].cost = current.cost + 1;
                                priority_queue[rear].state = next_state;
                                rear++;
                            }
                        }
                    }
                }
            }
        }
    }

    // Return the original state if no solution is found
    return initial_state;
}

int main() {
    // Initial and goal states
    PuzzleState initial_state = {{1, 2, 3}, {5, 6, -99}, {4, 7, 8}};
    PuzzleState goal_state = {{1, 2, 3}, {4, 5, 6}, {7, 8, -99}};

    // Run A* algorithm
    PuzzleState solution_state = astar(initial_state, goal_state);

    return 0;
}

