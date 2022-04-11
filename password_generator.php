<?php
function password_generator() {
    $assets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+=?><[]{}';
    $password = array();
    for($i = 0; $i < 8; $i++) { // change limit of i for biggest password
        $n = rand(0, strlen($assets));
        $password[] = $assets[$n];
    }
    return implode($password);
}

echo "password = " . password_generator();
?>
