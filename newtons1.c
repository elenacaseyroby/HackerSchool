#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main( ) {
	//This program allows you to enter any 2nd degree polynomial to 
	//find one of its roots using newton's method: 
	//http://tutorial.math.lamar.edu/Classes/CalcI/NewtonsMethod.aspx

	double a, b, c, d, e, x, x_root_approx, y, yfloor;
	char *correct_coefficient_answer; //needed *!!
	int correct_type, correct_coefficient, i;

	correct_coefficient = 0;
	correct_type = 0;
	x_root_approx = rand() % 100;
	

	while(correct_coefficient == 0){ //figure out how to make sure user enters the right data type before assigning it to a variable


		//user enters coeffients to second degree polynomial
		printf("Enter the coefficients for a second degree \npolynomial to find one of it's roots. \nIf the polynomial is ax^2 + bx +c, \nenter the integer value for coefficient a:\n");
	   	scanf("%lf", &a);
		
		printf("Enter the integer value for coefficient b:\n");
		scanf("%lf", &b);

		printf("Enter the integer value for coefficient c:\n");
		scanf("%lf", &c);

		//repeat question until user answers w correct data type 1 or 0
		correct_type = 0;
		while(correct_type == 0){ 
			
			printf("Do you want to find a root for this polynomial: %6.0fx^2 + %6.0fx + %6.0f ? \nPlease enter '1' for yes or '0' for no:\n", a, b, c);
			scanf("%d", &correct_coefficient); //breaks program if a non-integer value is entered

			
			if (correct_coefficient == 1 || correct_coefficient == 0){ 
				correct_type = 1;
				
			}
		}

	}
	
	//find y at first value of x_root_approx
	y = a*x_root_approx*x_root_approx + b*x_root_approx +c;
	x= x_root_approx;

	//multiply y by 10000000000 and round to find value of y to the 10th dec place
	yfloor = floor(y * 10000000000);
	//we want value of x as y approaches 0, so we keep iterating until y is 0 up to the 10th decimal place
	while( yfloor != 0){ 
		//find the tangent line at x = x_root_approx 
		//then find the value of x on the tangent line when y = 0
		x = -((a*x_root_approx*x_root_approx + b*x_root_approx +c)/(2*a*x_root_approx+b)) + x_root_approx;
		//find the value of y at the new value of x
		y = a*x*x + b*x +c;
		yfloor = floor(y * 10000000000); 

		//print value of x and y at each iteration 
		printf("\n x = %10.10f y = %10.10f", x, y);
		//the value of x becomes our new value of x_root_approx and we start over
		x_root_approx = x;


	}
   printf("\nx = %10.10f is a root of %6.0fx^2 + %6.0fx + %6.0f \n", x, a, b, c);   

   return 0;
}