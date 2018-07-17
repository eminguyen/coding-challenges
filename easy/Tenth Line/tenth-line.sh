# Given a text file file.txt, print just the 10th line of the file.

# Read from the file file.txt and output the tenth line to stdout.

sed '10q;d' file.txt
