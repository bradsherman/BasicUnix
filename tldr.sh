#!/bin/sh

if [ $# != 1 ]; then
    echo "usage: $0 command"
    exit 1
fi

path=$(find . -iname "$@.md" | head -n 1)

if [ -z "$path" ]; then
    echo "Unknown command: $@"
    exit 2
fi

exec ./mdview.sh $path
