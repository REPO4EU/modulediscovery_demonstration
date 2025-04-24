import os

DATA_DIR = "../data"
PIPELINE_RUN_DIR = "../pipeline_runs"

SEED_SETS = [
    {"name": "Amyotrophic lateral sclerosis", "short": "ALS", "mondo": "0004976", "disgenet": "C0002736"},
    {"name": "Lung adenocarcinoma", "short": "LUAD", "mondo": "0005061", "disgenet": "C0152013"},
    {"name": "Ulcerative colitis", "short": "UC", "mondo": "0005101", "disgenet": "C0009324"},
    {"name": "Crohn disease", "short": "CD", "mondo": "0005011", "disgenet": "C0156147"},
    {"name": "Huntington disease", "short": "HD", "mondo": "0007739", "disgenet": "C0020179"},
]

NETWORKS = [
    {'id': 'iid.human.Symbol', 'label': 'IID', 'color': '#b15928'},
    {'id': 'nedrex.reviewed_proteins_exp.Symbol', 'label': 'NeDRex', 'color': '#6a3d9a'}, 
    {'id': 'nedrex.reviewed_proteins_exp_high_confidence.Symbol', 'label': 'NeDRex (high confidence)', 'color': '#cab2d6'},
    {'id': 'biogrid.4_4_242_homo_sapiens.Symbol', 'label': 'BioGRID', 'color': '#1f78b4'},
    {'id': 'hippie.v2_3_medium_confidence.Symbol', 'label': 'HIPPIE (medium confidence)', 'color': '#33a02c'},
    {'id': 'hippie.v2_3_high_confidence.Symbol', 'label': 'HIPPIE (high confidence)', 'color': '#b2df8a'},
    {'id': 'string.human_links_v12_0_min700.Symbol', 'label': 'STRING (high confidence)', 'color': '#e31a1c'}, 
    {'id': 'string.human_links_v12_0_min900.Symbol', 'label': 'STRING (highest confidence)', 'color': '#fb9a99'}, 
    {'id': 'string.human_physical_links_v12_0_min700.Symbol', 'label': 'STRING (physical, high confidence)', 'color': '#ff7f00'}, 
    {'id': 'string.human_physical_links_v12_0_min900.Symbol', 'label': 'STRING (physical, highest confidence)', 'color': '#fdbf6f'}, 
]