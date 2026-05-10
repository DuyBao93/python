#!/bin/sh
# if [ "$1" = "test" ]
# then
#     python ./test.py
# elif [ "$1" = "main" ]
# then
#     python ./main.py
# else
#     echo "Don't have this file"
# fi

if [[ -f "./$1.py" ]]
then
    python ./"$1".py
else
    echo "File not exist"
fi