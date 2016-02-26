#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
/* 

Program Description:
This program uses Newton's Method to find the real roots of a 2nd degree polynomial.  
It only accepts 2nd degree polynomials with integer valued coefficients. 
Learn more about Newton's Method here: 
http://tutorial.math.lamar.edu/Classes/CalcI/NewtonsMethod.aspx

Test Cases:
1. y = 1x^2 + 4 + 4 root is x = -2
2. y = -3x^2 + 4x + 4 roots are x = 2 x = -.6666666667
3. y = -10x^2 + 54x + 0 roots are x = 0 and x = 5.4
4. y = 1x^2 + 23x - 108 roots are x = -27 and x = 4 
5. y = 1x^2 + 0x + 6 should have no real roots.

*/

double find_root(double x_intercept_tan, double x_vertex, double a, double b, double c);

int main( ) {

	double a, b, c, d, e, x1, x2, x_intercept_tan, y, x_vertex, y_vertex, difference;
	char *correct_coefficient_answer; 
	int correct_type, correct_coefficient, i;

	correct_coefficient = 0;
	correct_type = 0;
	x_intercept_tan = rand() % 100;

	while(correct_coefficient == 0){ 

		//user enters integer values for coeffients of second degree polynomial
		printf("\nEnter the coefficients of a 2nd degree \npolynomial to find it's roots. \nIf the polynomial is ax^2 + bx +c, \nenter the integer value for coefficient a:\n");
	   	scanf("%lf", &a);
	   	a = floor(a);
		
		printf("Enter the integer value for coefficient b:\n");
		scanf("%lf", &b);
		b = floor(b);

		printf("Enter the integer value for coefficient c:\n");
		scanf("%lf", &c);
		c = floor(c);

		//Verify that user has entered the correct coefficients. 
		//Repeat question until user answers with "1" or "0". Warning: entering non int value breaks program.
		correct_type = 0;
		while(correct_type == 0){ 
			
			printf("Do you want to find a root for this polynomial: %6.0fx^2 + %6.0fx + %6.0f ? \nPlease enter '1' for yes or '0' for no:\n", a, b, c);
			
			scanf("%d", &correct_coefficient); 
			
			if (correct_coefficient == 1 || correct_coefficient == 0){ 
				correct_type = 1;
				
			}
		}
	}
	//Find value of x at parabola's vertex.  Make sure x_intercept_tan is never assigned that value
	//otherwise it will break the program because there will be no x intercept of the tangent 
	//line at that x value
	x_vertex = -(b/(2*a)); 

	//find value of y at vertex
	y_vertex = a*x_vertex*x_vertex + b*x_vertex +c;

	if(y_vertex == 0){//then root is x value at vertex

		printf("\n\nx = %10.10f is the only root of y = %6.0fx^2 + %6.0fx + %6.0f \n\n\n", x_vertex, a, b, c);  

	}else if((a>0 && y_vertex<0) || (a<0 && y_vertex>0)){//then there are two roots

		//find the first root of the 2nd degree polynomial
		x1 = find_root(x_intercept_tan, x_vertex, a, b, c); //won't return double

		//to find the second x intercept, make sure the new x_intercept_tan starts on the other side of the 
		//parabola's vertex, so that it will interate to find a different x intercept
		difference = x_vertex - x1;
		x_intercept_tan = x_vertex + difference;

		//find the second root of the 2nd degree polynomial:
		x2 = find_root(x_intercept_tan, x_vertex, a, b, c);

		//print results:
		printf("\n\nx = %10.10f and x = %10.10f are the roots of y = %6.0fx^2 + %6.0fx + %6.0f \n\n\n", x1, x2, a, b, c);  

	}else{//then there are no real roots
		printf("\n\n There are no real roots, this 2nd degree polynomial does not intersect with the x-axis.\n");
	}
   return 0;
}

double find_root(double x_intercept_tan, double x_vertex, double a, double b, double c){
	
	double yfloor, x, y;
	
	printf("\n\nx and y values as function iterates and y gets closer to 0:\n");

	//find y at first value of x_intercept_tan
	y = a*x_intercept_tan*x_intercept_tan + b*x_intercept_tan +c;
	x = x_intercept_tan;

	printf("\n x = %10.10f y = %10.10f", x, y);

	//multiply y by 10000000000 and round to find value of y to the 10th decimal place
	yfloor = floor(y * 10000000000);

	//we want value of x as y approaches 0, so we keep iterating until y is 0 up to the 10th decimal place
	while( yfloor != 0){ 

		if (x_intercept_tan == x_vertex){
			x_intercept_tan = rand() % 100;
		}
		//find the tangent line at x = x_intercept_tan 
		//then find the value of x on the tangent line when y = 0
		x = -((a*x_intercept_tan*x_intercept_tan + b*x_intercept_tan +c)/(2*a*x_intercept_tan+b)) + x_intercept_tan;

		//plug the new value of x into our 2nd degree polynomial to find the value of y 
		y = a*x*x + b*x +c;
		yfloor = floor(y * 10000000000); 

		//print value of x and y at each iteration so we can see y approach 0 as x approaches the root
		printf("\n x = %10.10f y = %10.10f", x, y);
		//the value of x becomes our new value of x_intercept_tan and we start over
		x_intercept_tan = x;

	}

   	return x; 
}