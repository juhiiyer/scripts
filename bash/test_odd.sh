#!/bin/bash
#practicing if else statements
#if [*condition*];
#then
#    statement
#elif [*condition*]; then
#    statement
#else;
#    do this by default
#fi

#logical operators [-a --> AND] [-o --> OR]

echo "Please enter a number: "
read num
if [ $num -gt 0 ]; then 
	echo "$num is positive"
elif [ $num -lt 0 ]; then
	echo "$num is negative"
else
	echo "$num is 0"
fi
