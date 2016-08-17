// you always need a setup function in p5.js
// this is the initial setup that gets applied
// before you begin drawing
var yRect = 0;
var squaresArray = [];

function setup() {
	createCanvas(
		window.innerWidth,
		window.innerHeight//makes color fill screen

		/*500, //x param
		500  //y param makes color fill square*/

	);
	background(255, 0, 255); //r,g,b params

	for( var i = 0; i <= 50; i++){
		var s = new FallingSquare;
		squaresArray.push(s);

	}

}

// you always need a draw function in p5.js
// this is the function that gets called continuously in the background
// you can think of this function as what gets applied in each frame
function draw() {

	background(255, 0, 255);
	squaresArray.forEach(function(square)){
		fill(square.color);
		rect( square.y, square.x, )
	}

	fill(0, 200, 0);
	stroke(0,200, 150);
	yRect = 200;

	rect(
		(window.innerWidth/2) - 15,
		yRect,
		30,
		30
	);

	fill(123);
	stroke(15,0,0);
	rect(
		(window.innerWidth/2) - 15,
		yRect,
		30,
		30

	);
	yRect += 10;

	ellipse(
		mouseX,
		mouseY,
		30,
		30
	);

}

function FallingSquare() { //object
	this.speed = random(0,20);
	this.y = 0;
	this.x = random(0, windo.innerWidth);
	this.width = 20;
	this.height = 20;
	this.color = color(
		random(0, 255), 
		random(0, 255), 
		random(0, 255)
	);
}

/*
function mouseClicked(){
	background(
		random(0,100),
		random(0,100),
		random(0, 100)
	);

}*/

//in javascript you can use 
//debugger;
//if you put it in your code it will capture where you are in your code at this time
//comand+option+i to pull up console and debug from there

//open -a Google Chrome [filename]