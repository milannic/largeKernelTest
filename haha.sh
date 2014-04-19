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


cd ${CUR_DIR}/full

for i in $(seq 0 ${NOR_FOLDS});
	do
		if [ ! -f ${i} ];then
			touch ./${i}
			cat ${CUR_DIR}/train/${i} | wc -l >> ./${i}
			cat ${CUR_DIR}/test/${i} | wc -l >> ./${i}
			cat ${CUR_DIR}/train/${i}  >> ./${i}
			cat ${CUR_DIR}/test/${i} >> ./${i}
			sed -i .bak "s/^2/-1/;s/^0/1/" ./${i}
		fi
	done

cd ..

cd ..

if [ ! -d folds_data2 ];then
	mkdir folds_data2
fi

if [ ! -d folds_raw ];then
	mkdir folds_raw
fi

cd folds_raw
for i in $(seq 0 ${NOR_FOLDS});
#for i in $(seq 1);
	do
		mkdir fold_${i}
		cd fold_${i}
			mkdir raw_stru
			cd raw_stru
				cp ../../../resources/gen_stru.py .
				cp ../../../resources/full/${i} .
				mv ${i} data
				mkdir struc_dir
				python2.7 ./gen_stru.py ${i}
			cd ..
		cd ..
	done
cd ..
cp -r folds_raw/* folds_data2/
cd folds_data2
for i in $(ls);
	do
		cd ${i}
		cp -r raw_stru/struc_dir/* .
		rm -r raw_stru
		cd ..
	done
cd ..

