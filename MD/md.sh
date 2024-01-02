for s in {701..1000}
do 
	([ -d $s ] && cd $s; cp ../w_eam2.fs ./; cp ../in.lmp ./;cp ../in2.lmp ./;cp ../in4.lmp ./;  cp ../jobscript-lmp ./; sbatch jobscript-lmp)
done