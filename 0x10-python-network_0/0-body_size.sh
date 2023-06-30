#!/bin/bash
# Script takes in a URL, sends a request to that URL
# displays the size of the body of the response
# size of display in bytes
# curl is used

curl -s "$1" | wc -c
