print("set filename")
import json
filename = input()
with open(f"./output_files/{filename}", 'r', encoding='utf8') as fout:
    data = json.load(fout)
    print(data)
