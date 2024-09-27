# SK electlink Move Charger App

### Description

Convert Excel file to Formated CSV file.


### How to run
```
# Step 1. Insert files in "data/raw".

# Step 2. Create normalized files.
/src > python normalize_data.py 

# Step 3. Create converted files.
/src > python convert_data.py
```

if you want to clear generated files.
```angular2html
# clear all generated files.
/src > python clear_convert_directory.py
/src > clear_normalize_directory.py
```