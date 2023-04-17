import pandas as pd

crd = [3000, 6000, 5000, 9000]

print("loading data")
csv = pd.read_csv("data/detected_transcripts.csv", memory_map=True)

print("saving subset...")
csv[ (csv['global_x'] >= crd[0]) & (csv['global_x'] < crd[2]) & (csv['global_y'] >= crd[1]) & (csv['global_y'] < crd[3])].to_csv("data/subset_transcripts.csv")
