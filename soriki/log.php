<?php

$data=json_encode($_REQUEST);
$dataObj = json_decode($data);
$filename = "T.log" ;

file_put_contents($filename, $dataObj->Tdata);

echo "logged Tdata";

?>
