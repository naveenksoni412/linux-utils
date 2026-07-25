#~/bin/sh
folderPath=$1
count=`ls -1q $folderPath | wc -l`
doneCount=0
lp=0
for file in $folderPath/*; do
    [ ! -L "$file" ] &&
      dir_name=$(date -r "$file" +%Y) &&
      dir_name=$folderPath/$dir_name
      mkdir -p "$dir_name" &&
      mv -- "$file" "$dir_name"
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

