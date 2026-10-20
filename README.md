# Overview
This project serves to build off of the paper Udify and TGIF.

# Understanding UD

Any sequence of words can be abstracted as a sequence
$$
\{w_1, ..., w_n\}
$$
Each of these words can then be constructed into a tree, where the directed edge $(w_i, w_j, d_{ij})$ indicates that $w_i$ depends on $w_j$ through dependency $d_{ij}$. Note that $d_{ij}$ does not necessarily equal $d_{ji}$.

## Example
For instance, consider the simple sentence "I ate"

In this sentence, we can define a root node `ROOT`.

Then, by the format of UD, then comes the predicate. In this sentence, "ate" is the predicate.

Therefore, we define ("ate", ROOT, predicate) as a node.

Further, "I" is the nominal subject, which determines who "ate". Therefore, ("i", "ate", nsubj) is another possible relation.

This can be encoded in the following tree:

Each of these words contains a Part-of-Speech (POS) tag associated with it. For instance, "ate" is a verb. Some of these are specific to the language, some of these are considered "universal" across the treebanks.


**TODO: PUT TREE AND FIX**

# Dataset

To be more specific, the data we use follows the ConLL-U format, which contains 10 tab-separated columns.


| # | Field | Meaning |
| --- | --- | ---|
| 1 | `ID` | Node within sentence |
| 2 | `FORM` | Actual Word (e.g. playing) | 
| 3 | `LEMMA` | Dictionary form (e.g. play) | 
| 4 | `UPOS` | Universal POS (e.g. VERB) |
| 5 | `XPOS` | Language-Specific POS |
| 6 | `FEATS` | Morphology (e.g. Number=Sing) |
| 7 | `HEAD` | Parent Node in Tree |
| 8 | `DEPREL` | Basic dependency relation |
| 9 | `DEPS` | Incoming edge in dependency graph |
| 10 | `MISC`| Other annotations|

## Reproducibility
To download the dataset, you may run the following commands:


```sh
# UD ENGLISH EWT
python scripts/data.py --dataset ENG_EWT
```

```sh
# UD Spanish Ancora
python scripts/data.py --dataset SPA_ANC
```


# Authors

Josue Castillo (josuec@mit.edu), Kelly Tung () 


# Credit 

The repositories for both datasets are here:

- [UD English EWT](https://github.com/UniversalDependencies/UD_English-EWT?)
- [UD Spanish Ancora](https://github.com/UniversalDependencies/UD_Spanish-AnCora)

This model is inspired by TGIF (Tree-Graph Integrated-Format Parser)