#include<stdio.h>
#include<conio.h>
#include<stdlib.h>


void CalculateHeurisitc(int InitialState[3][3] , int GoalState[3][3]){
	int i ,j;
	int distance = 0;
	for(i=0; i<3; i++){
		for(j=0; j<3; j++){
			int value = InitialState[i][j];
			int goal_i,goal_j;
			if(value != 0){
				for(goal_i=0;goal_i<3; goal_i++){
					for(goal_j=0; goal_j<3; goal_j++){
						if(value == GoalState[goal_i][goal_j]){
							distance += abs(i-goal_i)+abs(j-goal_j)	;						
							printf("Manhattan Distance for Element %d is %d\n",value,distance);
						}
					}	
				}
			}
		}
	}
}

int main(){
	int InitialState[3][3]={{5,6,7},{2,3,8},{1,4,0}};
	int GoalState[3][3]={{1,2,3},{4,5,6},{7,8,0}};
	CalculateHeurisitc(InitialState,GoalState);
	
	getch();
	return 0;
}
