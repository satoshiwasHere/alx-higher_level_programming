#!/bin/bash
# Script takes in a URL, sends a request to that URl
curl -s "$1" | wc -c
