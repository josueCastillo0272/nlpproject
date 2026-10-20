"""
Looks at the newest stable commit of test/train and just adds them to the dataset
"""
from __future__ import annotations
from dataclasses import dataclass
import os
import argparse

def not_supported(dataset : str) -> None:
    if dataset != CORPUS.ENG and dataset != CORPUS.SPA:
        raise ValueError("Dataset is not supported. Please use ENG_EWT or SPA_ANC:", dataset)


@dataclass(frozen=True)
class Datasets:
    ENG: str = "ENG_EWT"
    SPA: str = "SPA_ANC"
    ALL: str = "ALL"

CORPUS = Datasets()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='nlp-project',
        description='Delexicalized Parser for Enchanced UD',
    )

    parser.add_argument('-d', '--dataset')

    args = parser.parse_args()

    not_supported(args.dataset)