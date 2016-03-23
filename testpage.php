<!DOCTYPE html>

<?php

function check_keyword($keyword){

	$keywords = explode( ' ', $keyword );

	if(isset($keywords[1])){
		$errormessage = "Error: Can only search one keyword. Please enter the keyword you'd like to search for. <br> Make sure there are no spaces before or after the word.";
	}

	return $errormessage;
}


function search_text($keyword, $textblock){
	//break up text block into words
	$textblockarray = explode( ' ', $textblock );
	
	$savesentence = 0;
	$arraycounter = 0;
	$sentencecounter = 1;

	foreach($textblockarray as $word){

		if(strtolower( $word) == strtolower($keyword)){
			$savesentence = 1;
		}

		$output[$arraycounter] = $output[$arraycounter]." ".$word;

		$strlen = strlen( $word) - 1;
		$lastcharacter = substr( $word, $strlen, 1 );

		if($lastcharacter == "."){
			$word = substr_replace($word, "", -1);

			echo "<br> last word of sentence: ". $word;

			if(strtolower($word) == strtolower($keyword)){
				$savesentence = 1;
			}

			if($savesentence == 1){
				$output[$arraycounter] = "sentence #".$sentencecounter.": <br>".$output[$arraycounter];

				$arraycounter++;

			}else{
				$output[$arraycounter] = "";
			}

			$savesentence = 0;
			$sentencecounter++;

		}

		//1. check if word is the same as $keyword if so, mark $savesentence = 1
		//2. add word to output array
		//3. check if word has "." at end.  if yes & $savesentence = 1, save string to output array and bump up $arraycounter and $sentencecounter and set $savesentence = 0. 
		//else clear output array and bump up sentence counter and set $savesentence = 0.

	}

	if($output[0] == ""){
		$output[0] = "<font color='red'>Your keyword could not be found in the text below.</font>";
	}
	

	return $output;

}
?>


<body>
<form action = "" method = "get">
Search text for keyword: <input type="text" name="keyword" value=<?= isset($_GET['keyword'])? $_GET['keyword'] : "keyword" ?>><br>
<input type="Submit" value="Search">
</form>

<?php 
$textblock = "For a long time, the story goes, we supported a Victorian
regime, and we continue to be dominated by it even today. Thus the image of the imperial prude is emblazoned on our
restrained, mute, and hypocritical sexuality. At the beginning of the seventeenth century a certain
frankness was still common, it would seem. Sexual practices
had little need of secrecy; words were said without undue
reticence, and things were done without too much concealment;
one had a tolerant familiarity with the illicit. Codes
regulating the coarse, the obscene, and the indecent were
quite lax compared to those ofthe nineteenth century. It was
a time of direct gestures, shameless discourse, and open
transgressions, when anatomies were shown and intermingled
at will, and knowing children hung about amid the
laughter of adults: it was a period when bodies 'made a
display of themselves.' But twilight soon fell upon this bright day, followed by the
monotonous nights of the Victorian bourgeoisie. Sexuality
was carefully confined; it moved into the home. The conjugal
family took custody of it and absorbed it into the serious
function of reproduction. On the subject of sex, silence became
the rule. The legitimate and procreative couple laid
down the law. The couple imposed itself as model, enforced
the norm, safeguarded the truth, and reserved the right to
speak while retaining the principle of secrecy. A single locus
of sexuality was acknowledged in social space as well as at
the heart of every household, but it was a utilitarian and
fertile one: the parents' bedroom. The rest had only to remain
vague; proper demeanor avoided contact with other
bodies, and verbal decency sanitized one's speech."; 

$keyword = $_GET['keyword'];

if(isset($keyword)  && isset($textblock)){
	$errormessage = check_keyword($keyword);
	if (!empty($errormessage)){
		echo "<font color='red'>".$errormessage."</font>";
	}else{
		echo "<h3>Keyword '".$keyword."' found in the following sentences:</h3>";
		$sentences = search_text($keyword, $textblock);
		foreach($sentences as $sentence){
			echo "<br>".$sentence;
		}
	}
}
?>


<h3> Text: </h3>
<p>

<?php echo $textblock; ?>

</p>

</body>

</html>


