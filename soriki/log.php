<?php

$data=json_encode($_REQUEST);
// $dataObj = json_decode($data);
$filename = "T.log" ;

file_put_contents($filename, $data);

echo $data;

?>
