var n_stars = 40;
var stars = [];

function setup() {
	createCanvas(
		window.innerWidth,
		window.innerHeight//makes color fill screen
	);
	background(0, 0, 0); 
	for( i = 0; i < n_stars; i++){
		var s = {x: rand_range(0,window.innerWidth),
				y: rand_range(0, window.innerHeight),
				plane: rand_range(0, 5)};
		stars.push(s);
	}
	noStroke();//tells js you won't use stroke(); just fill()

}

function draw(){
	background(0);
	for( i = 0; i < n_stars; i++){
		fill(255/5*stars[i].plane);
		rect(stars[i].x, stars[i].y,4,6);
		//speed
		stars[i].x+=.5*stars[i].plane;
		if (stars[i].x > window.innerWidth){
			stars[i].x = 0;
			stars[i].y = rand_range(0, window.innerHeight);
		}

	}
}


function rand_range(start, end){
	return Math.floor(
		Math.random()*(end - start + 1) + start);
}

