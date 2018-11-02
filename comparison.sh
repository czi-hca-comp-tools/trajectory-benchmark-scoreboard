#!/bin/bash

# docker pull pinellolab/hca_score_accuracy
# docker pull pinellolab/hca_score_correlation
# docker pull pinellolab/hca_score_stability
# docker pull pinellolab/hca_downsample
# docker pull pinellolab/hca_method_monocle2


echo " Contributors to data simulation: Nikolaos Papadopoulos"
echo " Contributors to methods docker and file format: Duncan McColl"
echo " Contributors to metrics: Jean Fan, Huidong Chen"

dir_dataset="./dataset/synthetic"
dir_results="./results/synthetic"
methods=("monocle2")
metrics=("correlation" "accuracy" "stability")

for method in ${methods[@]}
do
	for dir_input in $(find $dir_dataset -depth 1 -type d)
	do
		########	method module and output conversion module	########
		echo "Running method "$method" on data" `basename $dir_input`" ..."
		dir_ouput=$dir_results/`basename $dir_input`/$method
		if [ ! -d $dir_ouput ]; then
			mkdir -p $dir_ouput;
		fi 
		docker run -v ${PWD}:/data -w /data pinellolab/hca_method_$method run_method $dir_input/input.txt $dir_ouput/output.txt

		########	metric module	########
		for metric in ${metrics[@]}
		do
			echo "Running metric "$metric" ..." 
			if [ $metric = "stability" ]; then
				echo "Running downsample ..."
				docker run -v  ${PWD}:/hca -w /hca pinellolab/hca_downsample -i $dir_input/input.txt --sub_input_folder  $dir_input/sub_data

				if [ ! -d $dir_ouput/sub_data_ouput ]; then
					mkdir -p $dir_ouput/sub_data_ouput;
				fi 		
				for sub_input in `ls $dir_input/sub_data`
				do
					if [[ $sub_input == "input"* ]]; then
						SUBSTRING=$(echo $sub_input | cut -d'_' -f 2)
						sub_output="output_"$SUBSTRING
						docker run -v ${PWD}:/data -w /data pinellolab/hca_method_$method run_method $dir_input/sub_data/$sub_input $dir_ouput/sub_data_ouput/$sub_output
					fi
				done
				docker run -v  ${PWD}:/hca -w /hca pinellolab/hca_score_$metric -o $dir_ouput/output.txt -t $dir_input/truth.txt --sub_output_folder  $dir_ouput/sub_data_ouput -s $dir_ouput/hca_score_$metric.txt
	        else
				docker run -v  ${PWD}:/hca -w /hca pinellolab/hca_score_$metric -o $dir_ouput/output.txt -t $dir_input/truth.txt  -s $dir_ouput/hca_score_$metric.txt
	        fi
		done
	done
done
