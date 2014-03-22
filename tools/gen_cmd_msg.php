#include "cmd_msg.h"

cmd_msg_t cmd_msg_arr[] = 
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
        $in = $attrs['name'];
        $out = $attrs['name'];
        $bef = strstr($out, '_');
        $out = "sc".$bef;
        printf("\t{\"onlineproto.%s\", \"onlineproto.%s\", %d}, /* %s */\n", $in, $out, $attrs['id'], $attrs['des']);
    }

    printf("\n\n");
}

?>
};
uint32_t cmd_msg_arr_size = sizeof(cmd_msg_arr) / sizeof(cmd_msg_t);
