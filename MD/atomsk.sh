for s in {701..1000}
do 
	mkdir $s
	([ -d $s ] && mkdir $s; cd $s; cp ../W.xsf ./; cp ../polycrystal.txt ./; cp ../change.py ./; python change.py; /N/u/yw132/BigRed3/atomsk_0.11_Linux-amd64/atomsk --polycrystal W.xsf polycrystal.txt final.xsf lammps cfg -wrap)
done