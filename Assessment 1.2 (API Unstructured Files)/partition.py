from unstructured.partition.pdf import partition_pdf
import os
import json

INPUT_DIR = r"C:\Users\Sanjai DL\Desktop\nihal\s3-small-batch-output\downloads"
OUTPUT_DIR = r"C:\Users\Sanjai DL\Desktop\nihal\s3-small-batch-output\structured"
api="xgYzHaiEZ6snUFp3KrYuLKn9dLZXUq"

os.makedirs(OUTPUT_DIR, exist_ok=True)

for filename in os.listdir(INPUT_DIR):
    if filename.lower().endswith(".pdf"):
        file_path = os.path.join(INPUT_DIR, filename)
        elements = partition_pdf(filename=file_path)  # offline

        json_path = os.path.join(OUTPUT_DIR, f"{os.path.splitext(filename)[0]}.json")
        with open(json_path, "w", encoding="utf-8") as out_file:
            json.dump([e.to_dict() for e in elements], out_file, indent=2)

print("All files partitioned offline and saved as JSON!")
