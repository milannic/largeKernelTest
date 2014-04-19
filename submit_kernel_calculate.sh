#! /bin/sh

CUR_DIR=$(pwd)
FOLDS=`ls ${CUR_DIR}/train | wc -l`

NOR_FOLDS=$(expr ${FOLDS} - 1)

PARSE_DIR="-buildfile /Users/Milannic/Documents/workspace/UtilityFunctions/parse_build.xml StanfordParseTreeFunctions"

: << BLOCK
CAL_TEST=2
echo $((CAL_TEST+3))
MY_TEST=$((CAL_TEST+3))
echo ${MY_TEST}

#echo ${NOR_FOLDS}
#echo ${FOLDS}
"
BLOCK

cd ..
cd folds_data
for i in $(ls);
	do
		cd ${i}
			for j in $(ls);
			do
				cd ${j}
					cd full
						qsub gen_PT_S1.sh &
						qsub gen_PT_S2.sh &
						qsub gen_SST_S1.sh &
						qsub gen_SST_S2.sh &
						sleep 1
					cd ..
				cd ..
			done
		cd ..
	done
cd ..
