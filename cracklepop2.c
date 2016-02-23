#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

int main(){

	double remainder1, remainder2, integer1, integer2, i;

	for(i=1; i<=100; i++){
		//find remainder of i/3
		remainder1 = modf(i/3, &integer1);
		//find remainder of i/5
		remainder2 = modf(i/5, &integer2);
		printf("\n");
		//if remainder of i/3 = 0, then it's divisible by 3 -> print "Crackle"
		if(remainder1 == 0){
			printf("Crackle");
		}
		//if remainder of i/5 = 0, then it's divisible by 5 -> print "Pop"
		if(remainder2 == 0){
			printf("Pop");
		}
		//if neither remainder = 0, print integer 
		if(remainder1 != 0 && remainder2 != 0){
			printf("%2.0f", i);
		}
	}
	printf("\n");
}