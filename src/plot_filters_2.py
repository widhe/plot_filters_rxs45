import pandas as pd
from src.utilities import *

# Read the Excel file header=4 to see if we can capture the correct headers
file_path  = "/Users/widhe/Library/CloudStorage/OneDrive-QamcomResearch&TechnologyAB/Projects/RSX45B/IF and analog filter investigation v2.xlsx"
df_filters_with_header_4 = pd.read_excel(file_path, sheet_name='Sheet1', header=4)

# Clean the DataFrame to remove any completely empty rows and columns
df_filters_with_header_4_cleaned = df_filters_with_header_4.dropna(how='all').dropna(axis=1, how='all')

# Reset index after dropping rows
df_filters_with_header_4_cleaned.reset_index(drop=True, inplace=True)

# Display the DataFrame to check if we have the correct headers now
df_filters_with_header_4_cleaned.head(10)

# Sampling frequency
id = 3
f_max = 20000

df_to_plot = df_filters_with_header_4_cleaned[df_filters_with_header_4_cleaned['ID'] == id]

# Plotting the filters
for index, row in df_to_plot.iterrows():
    plt.figure(figsize=(18, 9))
    x_plts = 1
    y_plts = 5
    sb_plt = 1
    plt.subplot(y_plts, x_plts, sb_plt)
    sb_plt = sb_plt + 1
    plot_filter_response(row['fpass_ch_low'], row['fpass_ch_high'], row['fstop_ch_low'], row['fstop_ch_high'],
                                   f_max, f"Channel Filter - band {row['Band']}")

    plt.subplot(y_plts, x_plts, sb_plt)
    sb_plt = sb_plt + 1
    plot_filter_response(row['f_lsi_low'], row['f_lsi_high'], row['f_lsi_low'], row['f_lsi_high'],
                                   f_max, f"LSI Image - band {row['Band']}", 'image')
    plt.gca().axvline(x=row['LO_lsi'], color='orange', linestyle='--')

    plt.subplot(y_plts, x_plts, sb_plt)
    sb_plt = sb_plt + 1
    plot_filter_response(row['f_hsi_low'], row['f_hsi_high'], row['f_hsi_low'], row['f_hsi_high'],
                                   f_max, f"HSI Image - band {row['Band']}", 'image')
    plt.gca().axvline(x=row['LO_hsi'], color='navy', linestyle='--')

    plt.subplot(y_plts, x_plts, sb_plt)
    sb_plt = sb_plt + 1
    plot_filter_response(row['fpass_rf_low'], row['fpass_rf_high'], row['fstop_rf_low'], row['fstop_rf_high'],
                                   f_max, f"RF Filter - band {row['Band']}")
    plt.gca().axvline(x=row['LO_lsi'], color='orange', linestyle='--')
    plt.gca().axvline(x=row['LO_hsi'], color='navy', linestyle='--')

    plt.subplot(y_plts, x_plts, sb_plt)
    sb_plt = sb_plt + x_plts
    plot_filter_response(row['fpass_low'], row['fpass_high'], row['fstop_low'], row['fstop_high'], f_max,
                         f"IF Filter - band {row['Band']}")
    plt.gca().axvline(x=row['fs']/2, color='r', linestyle='--')
    plt.gca().axvline(x=row['fs'], color='r', linestyle='--')


    plt.tight_layout()
# Show the plots
plt.show()
