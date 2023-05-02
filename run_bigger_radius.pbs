#!/usr/bin/env bash

#PBS -l nodes=1:ppn=48
#PBS -l walltime=24:00:00
#PBS -l mem=50gb
#PBS -m ae
#PBS -M simon.bil@ugent.be

cd dp/Vizgen

mkdir output_polyt_10_000_bigger

# disable lazy load as it seems to cause world age issues
export LazyModules_lazyload=false

# wo plotting as it seems to cause errors?
# TODO: investigate?
JULIA_NUM_THREADS=48 ./baysor run -s 70 -c ./merfish.toml -o ./output_polyt_10_000_bigger ./data/detected_transcripts_10_000.csv ./data/vizgen_Liver_polyT_10_000.tiff 
