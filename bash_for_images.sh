#resize images snippet BASH
for a in *.jpg; do convert "$a" -resize 50% resized/"$a"; done

