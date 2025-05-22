import os
import pandas as pd
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox

def browse_file(var):
    file_path = filedialog.askopenfilename(filetypes=[("CSV or Excel", "*.csv *.xlsx")])
    if file_path:
        var.set(file_path)

def merge_files(all_users_path, grads_path):
    df_all = pd.read_csv(all_users_path) if all_users_path.endswith('.csv') else pd.read_excel(all_users_path)
    df_grads = pd.read_csv(grads_path) if grads_path.endswith('.csv') else pd.read_excel(grads_path)

    if 'Email' not in df_all.columns or 'User ID' not in df_all.columns:
        raise ValueError("All Users file must contain 'Email' and 'User ID' columns.")
    if 'Email' not in df_grads.columns:
        raise ValueError("Graduate file must contain 'Email' column.")

    merged_df = pd.merge(df_grads, df_all, on='Email', how='inner')

    if merged_df.empty:
        messagebox.showwarning("No Match", "No matching users found.")
        return None, None

    output_path = os.path.join(os.path.dirname(all_users_path), "merged_users.csv")
    merged_df.to_csv(output_path, index=False)
    
    messagebox.showinfo(
        "Success",
        f"{len(merged_df)} users matched.\nMerged CSV saved to:\n{output_path}"
    )
    
    return merged_df, output_path