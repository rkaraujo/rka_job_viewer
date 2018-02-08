import pandas as pd
import sqlite3

conn = sqlite3.connect("/Development/workspace/rka_job_viewer/db.sqlite3")

json_files = ['file_scraped_08-02-18.json']

for json_file in json_files:
    df = pd.read_json('/Development/workspace/rka-job-scraper/' + json_file, encoding='utf-8')

    df['city'], df['date'] = df['infoData'].str.rsplit('-', 1).str
    df['city'] = df['city'].str.strip()
    df['date'] = df['date'].str.strip()
    df.drop('infoData', axis=1, inplace=True)

    df['date'] = pd.to_datetime(df['date'], format='%d/%m/%y')
    df['code'] = df['code'].astype(int)
    print df.shape

    df = df[df['description'].str.contains('Java') | df['title'].str.contains('Java')]
    print df.shape

    df = df[(df['description'].str.contains('Alphaville') == False) & (df['description'].str.contains('Vila Ol\xc3mpia') == False) & (df['description'].str.contains('Morumbi') == False) & (df['description'].str.contains('Interlagos') == False)]
    print df.shape

    df.to_sql("job_viewer_job", conn, if_exists="append", index=False)
