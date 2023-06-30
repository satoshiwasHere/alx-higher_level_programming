#!/bin/bash
# Script sends DELETE request to the URL passed as
# the first argument and displays the body of the response
# curl is utilized

curl -sX DELETE "$1"
