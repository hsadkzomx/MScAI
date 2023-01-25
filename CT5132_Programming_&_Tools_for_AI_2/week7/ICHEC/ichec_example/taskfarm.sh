python randmax.py 0 > randmax_0.txt # in taskfarm.sh, each line is a shell command with no comment lines and no blank lines.
python randmax.py 1 > randmax_1.txt # we use '>' to redirect any print statements in randmax.py to a file.
python randmax.py 2 > randmax_2.txt # we could *generate* this taskfarm.sh instead of writing it by hand.
