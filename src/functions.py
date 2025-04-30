import os
import pandas as pd
from config import PIPELINE_RUN_DIR, NETWORKS, AMIMS, SEED_SETS

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

def load_seed_stats(path=os.path.join(PIPELINE_RUN_DIR, "main/results/mqc_summaries/input_seeds_mqc.tsv")):
    df = pd.read_csv(path, sep="\t")

    # Add a new column "Seeds total" that is the sum of "Seeds" and "Not in network"
    df["Seeds total"] = df["Seeds"] + df ["Not in network"]

    # Split the id into seed_id and network_id
    df[["seed_id", "network_id"]] = df["Seed file"].apply(split_seed_id)
    
    return df

def load_module_topology(path=os.path.join(PIPELINE_RUN_DIR, "main/results/mqc_summaries/topology_mqc.tsv")):

    amim_meta_df = pd.DataFrame.from_dict(AMIMS)
    network_meta_df = pd.DataFrame.from_dict(NETWORKS)

    df = pd.read_csv(path, sep="\t")

    # Add a new column "Seeds total" that is the sum of "Seeds" and "Not in network"
    df["added_nodes"] = df["nodes"] - df["seeds"]

    # Split the id into seed_id, network_id, and amim_id
    df[["seed_id","network_id","amim_id"]] = df["sample"].apply(split_module_id)

    # Add columns with the labels for network and amim
    df["network"] = df["network_id"].replace(dict(zip(network_meta_df.id, network_meta_df.label)))
    df["amim"] = df["amim_id"].replace(dict(zip(amim_meta_df.id, amim_meta_df.label)))

    return df