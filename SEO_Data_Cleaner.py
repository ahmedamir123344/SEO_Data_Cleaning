import pandas as pd
import re

# 1. The names of the files
MESSY_FILE = "messy_backlinks_5000.csv"
CLEANED_FILE = "Final_Cleaned_SEO_Backlinks.csv" # <--- THIS IS THE NEW FILE NAME

def clean_seo_data():
    print(f"Reading messy file: {MESSY_FILE}...")
    df = pd.read_csv(MESSY_FILE)
    initial_rows = len(df)

    # 2. Clean the URLs (Remove http://, https://, www, and trailing slashes)
    def clean_url(url):
        url = str(url).strip()
        url = re.sub(r'^https?://(www\.)?', '', url)
        url = re.sub(r'/$', '', url)
        return url

    df['Source URL'] = df['Source URL'].apply(clean_url)
    df['Anchor Text'] = df['Anchor Text'].astype(str).str.strip()

    # 3. Remove duplicates
    df = df.drop_duplicates(subset=['Source URL', 'Target URL'])

    # 4. Remove spam (Keep only Domain Rating >= 10)
    df = df[df['Domain Rating'] >= 10]

    # 5. Remove rows with missing anchor text
    df = df[~df['Anchor Text'].isin(['', 'nan', 'None'])]

    # 6. Save to the NEW file
    df.to_csv(CLEANED_FILE, index=False)
    
    print("\n--- SUCCESS! ---")
    print(f"Started with: {initial_rows} messy rows.")
    print(f"Finished with: {len(df)} clean rows.")
    print(f"Your new clean file is named: {CLEANED_FILE}")

if __name__ == "__main__":
    clean_seo_data()