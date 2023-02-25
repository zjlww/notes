#!/bin/bash

fswatch -o ./raw_content/ | xargs -n1 -I{} sh -c 'python3 -m preprocess &'

