# SEO Backlink Data Cleaner

A Python script designed for SEO professionals, agencies, and link builders to automate the cleanup of messy backlink CSV exports. 

## The Problem
When exporting backlink data from tools like Ahrefs, SEMrush, or Moz, the resulting CSV files are often unusable without manual editing. They typically contain:
- Duplicate backlinks (same Source and Target URLs).
- Inconsistent URL formatting (`http://www.example.com/` vs `example.com`).
- Spam links with very low Domain Ratings (DR).
- Rows with missing Anchor Text.

Cleaning this data manually in Excel takes hours of tedious work.

## The Solution
This Python script automates the entire cleaning process in seconds. It uses `pandas` and `re` (regex) to:
1. **Standardize URLs:** Removes `http://`, `https://`, `www.`, and trailing slashes so URLs are uniform.
2. **Remove Duplicates:** Drops rows where the Source and Target URLs match.
3. **Filter Spam:** Removes toxic or low-quality links (Domain Rating < 10).
4. **Drop Empty Rows:** Removes backlinks that are missing anchor text.

## Project Structure
- `generate_mess.py`: A script that generates a synthetic 5,000+ row messy dataset to test the cleaning process.
- `SEO_Data_Cleaner.py`: The main cleaning script.
- `messy_backlinks_5000.csv`: The raw, messy input data.
- `Final_Cleaned_SEO_Backlinks.csv`: The final, analysis-ready output file.

## How to Use
1. Install the required library:
   ```bash
   pip install pandas