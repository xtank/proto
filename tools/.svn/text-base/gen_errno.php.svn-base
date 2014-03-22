
#ifndef CLIENT_ERRNO_H
#define CLIENT_ERRNO_H

enum cli_errno_t 
{
<?php

$argc = $_SERVER['argc'];
$argv = $_SERVER['argv'];

$filename = $argv[1];

$xml = simplexml_load_file($filename);

foreach ($xml as $err) {

    $attrs = array();

    foreach ($err->attributes() as $key => $val) {
        $attrs[$key] = $val;
    }

    printf("\tcli_err_%s = %d, /* %s */\n", $attrs['name'], $attrs['id'],
            $attrs['des']);
}

?>
};

#endif
