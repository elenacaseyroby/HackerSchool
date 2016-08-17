var n_points = 150;
var points = [];

function setup() {
	createCanvas(
		window.innerWidth,
		window.innerHeight
	);
	background(0, 0, 0); 
	for( i = 0; i < n_points; i++){
		var point = {
			num: rand_range(0,200)*(.01),//angle of start point in circle
			a: rand_range(20,700),//diameter
			speed: (1,5)*.1
		};
		points.push(point);
	}
	noStroke();//tells js you won't use stroke(); just fill()
}

function draw(){

	background(0);
	for( i = 0; i < n_points; i++){
		fill(255*(points[i].a/700));//700 if we actually wanted it to hit white
			
		x = points[i].a  * cos(points[i].num*Math.PI) + window.innerWidth/2;
		y = points[i].a  * sin(points[i].num*Math.PI) + window.innerHeight/2;
			
		rect(x, y, 4,6);
		points[i].num += 1/points[i].a; //angle of point grows slower as diameter increases
		points[i].a  += 1*points[i].speed; //diameter of circle increases to create spiral

		if (points[i].a > 700){  //point resets when diameter is too big
			points[i] = {
				num: rand_range(0,200)*(.01),
				a: rand_range(20,700),
				speed: (1,5)*.1
			};
		}
	}
}

function rand_range(start, end){
	return Math.floor(
		Math.random()*(end - start + 1) + start);
}
