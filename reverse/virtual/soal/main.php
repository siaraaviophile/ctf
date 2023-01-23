<?php
echo "Welcome to Virtual Sheel\nSilahkan Login untuk Melanjutkan!\n";

echo "Input your Name: ";
$u = trim(fgets(STDIN));
echo "Input yout Password: ";
$p = trim(fgets(STDIN));
// echo strlen ($u). " ". strlen($p)

if($u == 'admin' && $p == 'admin'){
    echo "Input Your IP Address for ping: ";
    $ip = trim(fgets(STDIN));
    $cmd = "ping -c 5 {$ip}";
    echo system($cmd);
}else{
    echo 'Username / Password Wrong';
    exit;
}
?>
