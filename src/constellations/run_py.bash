#!/bin/bash

# Run each .py file in the current directory
for file in ./*.py; do
    if [ -f "$file" ]; then
#        echo "Executing $file..."
        python "$file"
        echo "$file Executed"
    fi
done
