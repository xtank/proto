
#ifndef CLIENT_CMD_H
#define CLIENT_CMD_H

enum cli_cmd_t 
{
<?php

$argc = $_SERVER['argc'];
$argv = $_SERVER['argv'];

$filename = $argv[1];

$xml = simplexml_load_file($filename);

foreach ($xml as $section) {

    $attrs = array();

    foreach ($section->attributes() as $key => $val) {
        $attrs[$key] = $val;
    }

    $id = $attrs['id'];
    $count = 0;

    printf("/**** SECTION %s ****/\n", $attrs['des']);

    foreach ($section as $cmd) {

        $count++;

        $attrs = array();

        foreach ($cmd->attributes() as $key => $val) {
            $attrs[$key] = $val;
        }

        printf("\tcli_cmd_%s = %d, /* %s */\n", $attrs['name'], $attrs['id'], $attrs['des']);
    }

    printf("\n\n");
}

?>
};

#endif
