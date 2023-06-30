#!/bin/bash
# Script takes in a URL and displays all HTTP methods the server will accept
# curl is used

curl -sI "$1" | grep Allow | cut -d ' ' -f2-
