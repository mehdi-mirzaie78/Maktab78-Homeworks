#! /bin/bash
while true
do
  echo
  read -rp "Enter the name of the file: " filename
  if [[ -f "$filename" ]] ; then
    echo "--------Found it--------"
    tail -10 "$filename"
  else
    echo "Error the file does not exist!"
  fi
done