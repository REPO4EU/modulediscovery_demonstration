# modulediscovery pipeline demonstration

This repository contains Jupyter notebooks that were used to prepare the input data for and analyse the results of the demonstrations run of the [nf-core/diseasemodulediscovery](https://nf-co.re/diseasemodulediscovery) pipeline.

## Setup

Clone repository:
```bash
git clone https://github.com/REPO4EU/modulediscovery_demonstration.git
```

Install dependencies with conda:
```bash
cd modulediscovery_demonstration
conda env create -f environment.yml
conda activate mdp_demonstration
```

Download the [pipeline run results](https://zenodo.org/records/17536307) and place the unzipped `results` folder in `pipeline_runs/main`. Alternatively, you can reproduce the pipeline run using the [`command.sh`](./pipeline_runs/main/command.sh) script from within the `pipeline_runs/main` folder.

## Notebooks

- [`src/01_seed_selection.ipynb`](./src/01_seed_selection.ipynb): Prepares the input seed files for the demonstration run.
- [`src/02_visualize_network_topology.ipynb`](./src/02_visualize_network_topology.ipynb): Visualizes topological features of the input PPI networs.
- [`src/03_visualize_seed_genes.ipynb`](./src/03_visualize_seed_genes.ipynb): Visualizes properties of the input seed sets.
- [`src/04_visualize_module_topology.ipynb`](./src/04_visualize_module_topology.ipynb): Visualizes topological features of the inferred disease modules.
- [`src/05_module_overlap.ipynb`](./src/05_module_overlap.ipynb): Vsualizes overlaps between different disease modules.
- [`src/06_visualize_seed_perturbation.ipynb`](./src/06_visualize_seed_perturbation.ipynb): Visualizes the results of the seed perturbation analysis (robustness and rediscovery).
- [`src/07_visualize_network_perturbation.ipynb`](./src/07_visualize_network_perturbation.ipynb): Visualizes the results of the degree-preserving network rewiring analysis.
- [`src/08_visualize_digest.ipynb`](./src/08_visualize_digest.ipynb): Visualizes the functional coherence analysis results.

