#!/bin/bash
# A script that takes in a URL,sends a request
# to the URL and displays the size of the body of the response
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2

