import pandas as pd
import sqlite3

conn = sqlite3.connect("/Development/workspace/rka_job_viewer/db.sqlite3")

json_files = ['file_scraped_09-02-18.json']

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

    DESC_EXCLUDE_STR = ['alphaville', 'vila ol\xc3mpia', 'chacara', 'ch\xc9cara', 'morumbi', 'interlagos', 'berrini', 'faria lima', 'android', 'pmbok']
    desc_exclude_regexp = '|'.join(DESC_EXCLUDE_STR)
    df = df[df['description'].str.contains(desc_exclude_regexp, case=False) == False]
    print df.shape

    TITLE_EXCLUDE_STR = ['c#', 'junior', 'pleno', 'javascript', 'php', 'react', 'front end']
    title_exclude_regexp = '|'.join(TITLE_EXCLUDE_STR)
    df = df[df['title'].str.contains(title_exclude_regexp, case=False) == False]
    print df.shape

    df.to_sql("job_viewer_job", conn, if_exists="append", index=False)
