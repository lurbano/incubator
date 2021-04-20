<?php

$data=json_encode($_REQUEST);
$dataObj = json_decode($data);
echo($dataObj->filename);
$filename = "T.log" ;

file_put_contents($filename, $dataObj->data);

?>
