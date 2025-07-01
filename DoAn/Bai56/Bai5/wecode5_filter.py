import pandas as pd
import re

# Đọc file CSV
input_file = "WECODE_RESNET18.csv"
output_file = "WECODE5.csv"

# Đọc dữ liệu từ file CSV
df = pd.read_csv(input_file, header=None, names=["filename", "label"])

# Biểu thức chính quy để khớp với tên file có dạng " -.jpg", " -.png", " -.HEIC", v.v.
pattern = r"\s+-\.\w+$"

# Lọc các dòng có tên file khớp với mẫu
filtered_df = df[df["filename"].str.contains(pattern, regex=True, na=False)]

# Lưu kết quả vào file CSV mới
filtered_df.to_csv(output_file, index=False, header=False)

print(f"Đã lọc và lưu các dòng vào file: {output_file}")