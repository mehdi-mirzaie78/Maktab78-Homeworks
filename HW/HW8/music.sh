#!/bin/bash
name=$(find . -type f -name '*.mp3' | shuf -n 1)
#vlc --random $p
if [ -f $name ]; then
  nvlc $name
  trimmed=$(basename $name .mp3)
  read -rp "Enter your score to this song <<$trimmed>>: " score
  if (($score < 10 && $score > 0)); then
    echo "$trimmed: $score" >>"music scores.txt"
  else
    echo "Score is not valid! Score must be in range 1 - 10"
  fi
else
  echo "Error! The file doesn't exist."
fi

echo "Average Score for all musics is: "
# I wanted to finish this part but, I couldn't make it


#========================
#cvlc --playlist-autostart
#p=$(ls | grep \.mp3$)
#p=$(ls *.mp3)
#name=$(find ./ -type f | shuf -n 1)
#mpg123 -Z *.mp3
#vlc --random
