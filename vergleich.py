import json
from deepdiff import DeepDiff
import tkinter as tk
from tkinter import scrolledtext

def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def compare_json(json1, json2):
    diff = DeepDiff(json1, json2, ignore_order=True)
    return diff

def display_diff_gui(json1, json2, diff):
    root = tk.Tk()
    root.title("JSON Comparison")

    text_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
    text_widget.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

    text_widget.insert(tk.END, "JSON 1:\n")
    text_widget.insert(tk.END, json.dumps(json1, indent=2))
    text_widget.insert(tk.END, "\n\nJSON 2:\n")
    text_widget.insert(tk.END, json.dumps(json2, indent=2))
    text_widget.insert(tk.END, "\n\nDifferences:\n")

    for change_type, changes in diff.items():
        for change in changes:
            text_widget.insert(tk.END, f"{change_type}: {change}\n", change_type)

    root.mainloop()

if __name__ == "__main__":
    # Pfad zu den JSON-Dateien
    file1_path = 'file1.json'
    file2_path = 'file2.json'

    # JSON-Dateien laden
    json1 = load_json(file1_path)
    json2 = load_json(file2_path)

    # JSON-Dateien vergleichen
    diff = compare_json(json1, json2)

    # Unterschiede im externen Fenster anzeigen
    display_diff_gui(json1, json2, diff)
