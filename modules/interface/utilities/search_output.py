import csv
import os
from pathlib import Path

def format_output(rows):
    return "\n".join(
        f"Job: {r['Job']}\nFile: {r['File']}\nProdName: {r['ProdName']}\nDesc: {r['ProductDesc']}\n"
        f"Width: {r['Width']}, Height: {r['Height']}, Depth: {r['Depth']}\n{'-'*36}"
        for r in rows
    )

def save_csv(rows: list[dict[str, str]]):
    if not rows:
        return None
    downloads = Path.home() / "Downloads"
    path = downloads / "product_search_results.csv"
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    return str(path)
