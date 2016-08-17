
var n_stars = 300;
var stars = [];

function setup() {
	createCanvas(
		window.innerWidth,
		window.innerHeight
	);
	background(0, 0, 0); 
	for( i = 0; i < n_stars; i++){
		var s = {x_3D: rand_range(-1*window.innerWidth/2, window.innerWidth/2),
				y_3D: rand_range(-1*window.innerHeight/2, window.innerHeight/2),
				z_3D: rand_range(50,100),
				speed: rand_range(1, 5)};
		stars.push(s);
	}
	noStroke();//tells js you won't use stroke(); just fill()

}

function draw(){
	background(0);
	for( i = 0; i < n_stars; i++){
		fill(255/stars[i].z_3D);
		x_screen = stars[i].x_3D/stars[i].z_3D + window.innerWidth/2;
		y_screen = stars[i].y_3D/stars[i].z_3D + window.innerHeight/2;

		rect(x_screen, y_screen,4,6);
		//speed
		stars[i].z_3D-=stars[i].speed;
		if(i==1){
			console.log(stars[i].z_3D);
			console.log(stars[i].speed);
		}
		if (stars[i].z_3D <= 0){
			stars[i] = {x_3D: rand_range(-1*window.innerWidth/2, window.innerWidth/2),
				y_3D: rand_range(-1*window.innerHeight/2, window.innerHeight/2),
				z_3D: rand_range(50,100),
				speed: rand_range(1, 5)};
		}

	}
}


function rand_range(start, end){
	return Math.floor(
		Math.random()*(end - start + 1) + start);
}