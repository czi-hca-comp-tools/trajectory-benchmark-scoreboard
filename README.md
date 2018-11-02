# trajectory-benchmark-scoreboard


Notes for the definition of this webapp

Input:
--------------------------

1) Real datasets and synthetic: Loom  (DCP)   

2) Ground truth: what are the columns?

cell_id, rank (discrete), (pseudotime(real),branch,....)

Folder structure real

/datasets/real/dataset_name/input.loom
/datasets/real/dataset_name/truth.?

Folder structure synthetic

As above but everything is under:

/datasets/syn


Output:
--------------------------
Output Json for scoreboard (Charlotte can tell us more on the requirements)

Folder structure

/results/dataset_name/method_name/hca_score_metric-name.json

Then in the file we have the fields we want to show in the board:

{key:value} where key is the metric-name and value is the value of that metric

We may have special cases where you have more elements, for example:

{'spearman':0.8, 'kendeall':0.75}

{'stability mean':1.0, 'stability std': 0.2}
