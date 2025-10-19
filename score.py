#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys, csv, json, re
from collections import Counter

REQ_COL_IN = "Input sentence"
REQ_COL_OUT = "Output sentence"

def tokenize(text):
    return re.findall(r"\w+|[^\w\s]", text, flags=re.UNICODE)

def read_csv_rows_output_only(path):
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        cols = reader.fieldnames or []
        if REQ_COL_OUT not in cols:
            raise ValueError(f"{os.path.basename(path)} must have column '{REQ_COL_OUT}'. Found: {cols}")
        return list(reader)

def corpus_gleu_1to4(ref_tokens_list, hyp_tokens_list):
    scores = []
    for n in range(1,5):
        ref_total = hyp_total = matches = 0
        for rt, ht in zip(ref_tokens_list, hyp_tokens_list):
            r = Counter(tuple(rt[i:i+n]) for i in range(max(0, len(rt)-n+1)))
            h = Counter(tuple(ht[i:i+n]) for i in range(max(0, len(ht)-n+1)))
            ref_total += sum(r.values()); hyp_total += sum(h.values())
            if r and h: matches += sum((r & h).values())
        prec = (matches / hyp_total) if hyp_total > 0 else 0.0
        rec  = (matches / ref_total) if ref_total > 0 else 0.0
        scores.append(min(prec, rec))
    return (sum(scores)/len(scores))*100.0 if scores else 0.0

def main(input_dir, output_dir):
    ref_dir = os.path.join(input_dir, "ref")
    res_dir = os.path.join(input_dir, "res")
    #ref_dir = os.path.join("/home/pramit/Documents/IndicGEC-Hindi/final_phase/reference_data")
    #res_dir = os.path.join("/home/pramit/Documents/IndicGEC-Hindi/final_phase/reference_data")
    os.makedirs(output_dir, exist_ok=True)

    # Prefer dev_gold for Dev phase; fallback to test_gold for Final.
    ref_file = None
    for cand in ["dev_gold.csv", "test_gold.csv"]:
        p = os.path.join(ref_dir, cand)
        if os.path.exists(p):
            ref_file = p
            break
    if ref_file is None:
        raise FileNotFoundError("Neither dev_gold.csv nor test_gold.csv found under input/ref/.")

    pred_file = os.path.join(res_dir, "predictions.csv")
    if not os.path.exists(pred_file):
        raise FileNotFoundError("Missing input/res/predictions.csv inside your submission ZIP.")

    # Read only requiring Output sentence
    gold = read_csv_rows_output_only(ref_file)
    pred = read_csv_rows_output_only(pred_file)

    if len(gold) != len(pred):
        raise ValueError(f"Row count mismatch: gold={len(gold)}, predictions={len(pred)}.")

    ref_tokens_list, hyp_tokens_list = [], []
    for g, p in zip(gold, pred):
        ref_tokens_list.append(tokenize((g.get(REQ_COL_OUT, '') or '').strip()))
        hyp_tokens_list.append(tokenize((p.get(REQ_COL_OUT, '') or '').strip()))

    gleu = corpus_gleu_1to4(ref_tokens_list, hyp_tokens_list)

    with open(os.path.join(output_dir, "scores.txt"), "w", encoding="utf-8") as sf:
        sf.write(f"gleu: {gleu:.6f}\n")
    with open(os.path.join(output_dir, "scores.json"), "w", encoding="utf-8") as jf:
        json.dump({"gleu": gleu}, jf, ensure_ascii=False)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python score.py <input_dir> <output_dir>")
        sys.exit(2)
    main(sys.argv[1], sys.argv[2])
