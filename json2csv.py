import pandas as pd
import json, csv, os
from tkinter import filedialog, messagebox

file_path = filedialog.askopenfilename()

JSON_FILE = file_path

directory = os.path.dirname(file_path)
file_name = os.path.splitext(os.path.basename(file_path))[0]

csv_file_path = os.path.join(directory, f"{file_name}.csv")

with open(JSON_FILE, encoding = 'utf-8') as json_file:
  json_data = json.load(json_file)
  first_key = next(iter(json_data['data']))
  df = pd.DataFrame(json_data['data'][first_key])
  df.to_csv(csv_file_path, encoding = 'utf-8', index = False)
messagebox.showinfo(title="Success", message="Json file successfully converted!")