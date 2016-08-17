<!DOCTYPE html>

<?php
//PHP FUNCTIONS HERE
//return 'true' if string contains '.' and 'false' if it does not containg '.'
function check_end_of_sentence($word){
	$letters = explode( '.', $word);
	if(isset($letters[1])){
		$return = true;
	}else{
		$return = false;
	}
	return $return;
}
//return error message if user does not enter exactly one word
function check_keyword($keyword){
	$keywords = explode( ' ', $keyword );
	if(isset($keywords[1]) || $keyword == ""){
		$errormessage = "Error: Must enter exactly one keyword. Please enter the keyword you'd like to search for. <br> Make sure there are no spaces before or after the word.";
	}
	return $errormessage;
}
//returns array with each sentence from the text block that contains the keyword
function search_text($keyword, $textblock, $boldsentence = false){
	//break up text block into words
	$textblockarray = explode( ' ', $textblock );
	
	$savesentence = 0;
	$arraycounter = 0;
	$sentencecounter = 1;
	foreach($textblockarray as $word){
		//replace all characters that are NOT lowercase or uppercase letters with ""
		//so word can still be recognized if ends in period or quotes, etc.
		$wordnochar = preg_replace("/[^a-zA-Z]/", "", $word);
		//check for plural words that might match keyword
		$strlen = strlen( $wordnochar) - 1;
		$lastcharacter = substr( $wordnochar, $strlen, 1 );
		if($lastcharacter == 's'){
			$wordnochar = substr( $wordnochar, 0, $strlen );
		}
		//save sentence if word matches keyword. underline keyword.
		if(strtolower($wordnochar) == strtolower($keyword)){
			$savesentence = 1;
			$output[$arraycounter] = $output[$arraycounter]." <u>".$word."</u>";
		}else{
			$output[$arraycounter] = $output[$arraycounter]." ".$word;
		}
		
		$endofsentence = check_end_of_sentence($word);
		//if you reach end of sentence with keyword, store it in array.  else clear sentence from array.
		if($endofsentence){
			

			if($savesentence == 1){
				if($boldsentence){
					$output[$arraycounter] = "<b>".$output[$arraycounter]."</b>";
				}else{
					$output[$arraycounter] = "sentence #".$sentencecounter.": <br>".$output[$arraycounter]."<br><br>";
				}
				$arraycounter++;
			}else{

				if($boldsentence){
					$output[$arraycounter] = $output[$arraycounter];
					$arraycounter++;
				}
				$output[$arraycounter] = "";

			}
			$savesentence = 0;
			$sentencecounter++;

		}

	}
	echo "<br><br>output = ".$output[0];
	//if no sentences are saved, keyword could not be found in text block
	if($output[0] == ""){
		$output[0] = "<font color='red'>Your keyword could not be found in the text below.</font>";
	}
	
	return $output;
}
?>

<!--FORM HERE-->

<body>
<form action = "" method = "get">
Search text for keyword: <input type="text" name="keyword" value="<?= isset($_GET['keyword'])? $_GET['keyword'] : 'Enter keyword here' ?>"><br>
Enter text block: <textarea name="textblock" rows=4 cols=60> <?= isset($_GET['textblock'])? $_GET['textblock'] : 'Paste text block here' ?></textarea>
<input type="Submit" value="Search">
</form>

<?php 
$textblock = $_GET['textblock'];
$keyword = $_GET['keyword'];
if(isset($keyword)  && isset($textblock)){
	$errormessage = check_keyword($keyword);
	if (!empty($errormessage)){
		echo "<font color='red'>".$errormessage."</font>";
	}else{
		echo "<h3>Keyword '".$keyword."' found in the following sentences:</h3>";
		$sentences = search_text($keyword, $textblock);
		echo "<p>";
		foreach($sentences as $sentence){
			echo "<br>".$sentence;
		}
		echo "</p>";
	}
}
?>

<h3> Text: </h3>
<p>

<?php 

$textblockbolds = search_text($keyword, $textblock, $boldsentence = true);

foreach($textblockbolds as $textblockbold){
	echo $textblockbold; 

}

?>

</p>

</body>

</html>