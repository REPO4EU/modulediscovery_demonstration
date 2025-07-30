import os
import pandas as pd
import matplotlib.pyplot as plt
import json
import requests
from config import PIPELINE_RUN_DIR, FIGURE_DIR, NETWORKS, AMIMS, SEED_SETS

def split_seed_id(seed_id):
    """
    Splits the seed file id into its components.
    """
    # Split the seed file name by underscores
    parts = seed_id.split(".")
    
    # Extract the components
    seed_id = parts[0]
    network_id = ".".join(parts[1:])
    
    return pd.Series([seed_id, network_id])

def split_module_id(module_id):
    """
    Splits the module ID into its components.
    """
    parts = module_id.split(".")
    amim_id = parts[-1]
    return pd.concat([split_seed_id(".".join(parts[:-1])), pd.Series([amim_id])], ignore_index=True)

def load_network_topology(path=os.path.join(PIPELINE_RUN_DIR, "main/results/mqc_summaries/input_network_mqc.tsv")):

    network_meta_df = pd.DataFrame.from_dict(NETWORKS)
    df = pd.read_csv(path, sep="\t")

    df["network"] = df["Network"].replace(dict(zip(network_meta_df.id, network_meta_df.label)))
    df.set_index("Network", inplace=True)
    df = df.loc[network_meta_df.id.values,:] # order by network

    return df

def load_seed_stats(path=os.path.join(PIPELINE_RUN_DIR, "main/results/mqc_summaries/input_seeds_mqc.tsv")):
    network_meta_df = pd.DataFrame.from_dict(NETWORKS)

    df = pd.read_csv(path, sep="\t")

    # Add a new column "Seeds total" that is the sum of "Seeds" and "Not in network"
    df["Seeds total"] = df["Seeds"] + df ["Not in network"]

    # Split the id into seed_id and network_id
    df[["seed_id", "network_id"]] = df["Seed file"].apply(split_seed_id)

    df["network"] = df["network_id"].replace(dict(zip(network_meta_df.id, network_meta_df.label)))
    
    return df

def load_module_topology(path=os.path.join(PIPELINE_RUN_DIR, "main/results/mqc_summaries/topology_mqc.tsv")):

    amim_meta_df = pd.DataFrame.from_dict(AMIMS)
    network_meta_df = pd.DataFrame.from_dict(NETWORKS)

    df = pd.read_csv(path, sep="\t")

    df["added_nodes"] = df["nodes"] - df["seeds"]

    # Split the id into seed_id, network_id, and amim_id
    df[["seed_id","network_id","amim_id"]] = df["sample"].apply(split_module_id)

    # Add columns with the labels for network and amim
    df["network"] = df["network_id"].replace(dict(zip(network_meta_df.id, network_meta_df.label)))
    df["amim"] = df["amim_id"].replace(dict(zip(amim_meta_df.id, amim_meta_df.label)))

    return df

def load_merged_stats():
    module_df = load_module_topology()
    seeds_df = load_seed_stats()
    networks_df = load_network_topology()

    # Rename columns to avoid conflicts when merging
    id_vars = ["seed_id", "network_id", "network", "amim", "amim_id"] # do not prefix these columns
    module_df  = module_df .rename(columns=lambda c: f"{c}_module" if c not in id_vars else c)
    seeds_df  = seeds_df .rename(columns=lambda c: f"{c}_seeds" if c not in id_vars else c)
    networks_df  = networks_df .rename(columns=lambda c: f"{c}_network" if c not in id_vars else c)

    df_merged = module_df.merge(seeds_df, on=["seed_id", "network_id", "network"]).merge(networks_df, on=["network"])
    df_merged["dropped_seeds_module"] = df_merged.Seeds_seeds - df_merged.seeds_module
    df_merged["included_seeds_percent_module"] = df_merged.seeds_module / df_merged.Seeds_seeds * 100
    df_merged["module_id"] = df_merged["sample_module"]

    return df_merged

def save_figure(fig, filename, dir=FIGURE_DIR, formats=["pdf", "png"]):
    """
    Saves a figure to the specified path.
    """

    for format in formats:
        if format not in ["pdf", "png"]:
            raise ValueError(f"Unsupported format: {format}. Supported formats are: pdf, png.")
        if not os.path.exists(os.path.join(dir, format)):
            os.makedirs(os.path.join(dir, format))
        fig.savefig(os.path.join(dir, format, f"{filename}.{format}"), bbox_inches='tight', dpi=600)

def expected_jaccard_index(n, a, b):
    """
    Calculate the expected Jaccard index for two sets (with sizes a and b) sampled from a population of size n.
    """
    if a > n or b > n:
        raise ValueError("a and b cannot be greater than n when sampling without replacement within each set.")
    if a == 0 or b == 0:
        return 0.0
    p = a / n  # probability of an element being in set1
    q = b / n  # probability of an element being in set2
    
    return (p * q / (p + q - p * q))