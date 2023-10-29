#!/bin/bash
#
# Note: This script is just notes, and not intended to be executed (yet)
#

cd data/

# fuzzing-project

# download
wget -m https://files.fuzzing-project.org/

mkdir fuzzing-project.org/

# move all into same directory
find files.fuzzing-project.org/ -type f -exec mv {} fuzzing-project.org/ \;

# some cleanup
cd fuzzing-project.org/
rm -f index*

# rename to ext.ext
for file in *.*; do
    # Extract the extension
    ext="${file##*.}"
    
    # Rename the file to its extension
    mv "$file" "$ext.$ext"
done

# delete files without extension 
find . -type f -not -name '*.*' -exec rm -f {} \;

mv Z.Z z.z
rm txt_.txt_

cd ../
rm -rf files.fuzzing-project.org


# fuzzing-corpus

git clone https://github.com/strongcourage/fuzzing-corpus

mkdir strongcourage
find fuzzing-corpus/ -type f -exec mv {} strongcourage/ \;

cd strongcourage/

# rename to ext.ext
for file in *.*; do
    # Extract the extension
    ext="${file##*.}"
    
    # Rename the file to its extension
    mv "$file" "$ext.$ext"
done

# delete files without extension 
find . -type f -not -name '*.*' -exec rm -f {} \;
rm -f pack.pack # too big
rm -f sample.sample

cd ../
rm -rf fuzzing-corpus/

# office 

git clone https://github.com/decalage2/oletools
mkdir decalage2

find oletools/tests/test-data/ -type f -exec mv {} decalage2/ \;

cd decalage2

# rename to ext.ext
for file in *.*; do
    # Extract the extension
    ext="${file##*.}"
    
    # Rename the file to its extension
    mv "$file" "$ext.$ext"
done

rm empty
rm text
rm zip.zip

# merge all

cd ../

mv fuzzing-project.org/* .
mv strongcourage/* .
mv decalage2/* .
rm -rf fuzzing-project.org strongcourage decalage2
