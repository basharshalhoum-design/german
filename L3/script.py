import os
import pandas as pd

# 📁 Folder containing your HTML files
folder = r"C:\Users\Bashar.Shalhoom.exte\Downloads\German\B2\L3"

# 📄 Load Excel file
try:
    df = pd.read_excel("verb_blocks.xlsx", engine="openpyxl")
    print("✅ Excel file loaded successfully.")
except Exception as e:
    print(f"❌ Failed to load Excel file: {e}")
    exit()

# 🧾 Show column headers
print("📄 Columns found:", df.columns.tolist())

# 🔁 Loop through each column (each = one HTML file)
for column in df.columns:
    try:
        new_block = str(df[column].dropna().iloc[0])
        print(f"\n🔍 Processing {column}...")
        print(f"🧾 Replacement block preview:\n{new_block[:100]}...\n")

        path = os.path.join(folder, column)
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            start = content.find("const verbData = [")
            end = content.find("];", start)
            if start != -1 and end != -1:
                before = content[:start]
                after = content[end + 2:]
                updated = before + new_block + after
                with open(path, 'w', encoding='utf-8-sig') as f:
                    f.write(updated)
                print(f"✅ Replaced verbData in {column}")
            else:
                print(f"⚠️ Block not found in {column}")
        else:
            print(f"❌ File not found: {path}")
    except Exception as e:
        print(f"❌ Error processing {column}: {e}")
