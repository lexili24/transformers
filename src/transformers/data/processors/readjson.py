import json
import csv
import pandas as pd


with open('BoolQ/train.jsonl') as f:
    df = pd.read_json(f, lines = True)


df.to_csv(r'train.tsv', index = None)

with open('BoolQ/val.jsonl') as f:
    df_dev = pd.read_json(f, lines = True)

df_dev.to_csv(r'dev.tsv', index = None)