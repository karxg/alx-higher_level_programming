#!/bin/bash
# Display all HTTP methods the server of a given URL that will accept.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
