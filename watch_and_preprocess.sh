#!/bin/bash

fswatch -o ./notes/ -o ./README.md | xargs -n1 -I{} sh -c 'python3 -m preprocess &'
