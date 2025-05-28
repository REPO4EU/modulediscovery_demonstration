nextflow run nf-core/diseasemodulediscovery -r 6e2b369e9ed7782305c785c711954dca6a6e5da4 \
-profile daisybio,singularity,keep_work \
-resume \
--id_space symbol \
--seeds ../../data/seeds/ALS.tsv,../../data/seeds/CD.tsv,../../data/seeds/HD.tsv,../../data/seeds/LUAD.tsv,../../data/seeds/UC.tsv \
--network string_min900,string_min700,string_physical_min900,string_physical_min700,biogrid,hippie_high_confidence,hippie_medium_confidence,iid,nedrex,nedrex_high_confidence \
#--run_seed_permutation \
#--run_network_permutation \
--outdir results
