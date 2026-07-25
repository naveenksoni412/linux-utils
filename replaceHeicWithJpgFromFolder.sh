#~/bin/sh
folderPath=$1
count=`ls -1q "$folderPath" | wc -l`
echo "$count files in $folderPath"
doneCount=0
lp=0
tt=0
for file in "$folderPath"/*; do
        echo $file
        if file "$file" | grep -q "HEIC"; then
          filename=$(basename "$file")
          filename="${filename%.*}"
          echo "processing $filename"
          ct=$(find "$2" -type f -name "$filename.jpg" -exec cp {} "$folderPath" \; -print | wc -l)
          if [ "$ct" -gt 0 ]; then
            mv "$file" $3/
            tt=$((tt+1))
          fi
          ct=$(find "$2" -type f -name "$filename.JPG" -exec cp {} "$folderPath" \; -print | wc -l)
          if [ "$ct" -gt 0 ]; then
            mv "$file" $3
            tt=$((tt+1))
          fi
        fi
      doneCount=$((doneCount+1))
      temp=$((doneCount*100))
      perc=$((temp/count))
      diff=$((perc-lp))
      if [[ $diff -ge 10 ]];
      then
      echo -ne "$perc % completed"\\r
      lp=$perc
      sleep .5
      fi   
done
echo -e \\n"All done"
echo -e \\n"Moved $tt files"

