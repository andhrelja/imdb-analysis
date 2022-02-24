import os
import csv
import requests
import pandas as pd

import settings

TITLES_DTYPE = {
    'tconst'          :'string',
    'averageRating'   :'float',
    'numVotes'        :'int',
    'titleType'       :'string',
    'primaryTitle'    :'string',
    'originalTitle'   :'string',
    'isAdult'         :'int',
    'startYear'       :'string',
    'runtimeMinutes'  :'int',
    'genres'          :'object', # Za stvaranje ml modela želimo napraviti OneHotEncoding
}


def download_data():
    files = [
        'https://datasets.imdbws.com/title.ratings.tsv.gz',
        'https://datasets.imdbws.com/name.basics.tsv.gz',
        'https://datasets.imdbws.com/title.basics.tsv.gz',
        'https://datasets.imdbws.com/title.crew.tsv.gz',
        'https://datasets.imdbws.com/title.principals.tsv.gz'        
    ]
    
    for url in files:
        print("Downloading {}".format(url))
        
        filepath = os.path.join(settings.DATASET_DIR, os.path.basename(url))
        if os.path.exists(filepath):
            continue
        
        response = requests.get(url)
        with open(filepath, 'wb') as output_file:
            output_file.write(response.content)
        
        print("Downloaded {}".format(url))



def prepare_titles_df():
    print("Reading dataset")
    title_basics_df = pd.read_csv(os.path.join(settings.DATASET_DIR, 'title.basics.tsv.gz'), compression='gzip', sep='\t')
    title_ratings_df = pd.read_csv(os.path.join(settings.DATASET_DIR, 'title.ratings.tsv.gz'), compression='gzip', sep='\t')

    print("Merging dataset")
    include_types = ('short', 'movie', 'video', 'tvMovie')
    titles_df = title_ratings_df.merge(title_basics_df[title_basics_df['titleType'].isin(include_types)], on='tconst')
    print(titles_df.info())

    print("Transforming merged dataset")
    titles_df['runtimeMinutes'] = titles_df['runtimeMinutes'].transform(lambda x: 0 if x == '\\N' else x).astype('float')
    titles_df['startYear']      = titles_df['startYear'].transform(lambda x: '' if x == '\\N' else int(float(x))).astype('string')
    titles_df['isAdult']        = titles_df['isAdult'].map(bool)
    titles_df['genres']         = titles_df['genres'].transform(lambda x: [] if x == '\\N' else x.split(',')).astype('object')
    titles_df                   = titles_df.drop('endYear', axis=1)
    
    titles_df = titles_df.astype(TITLES_DTYPE)
    print(titles_df)
    titles_df.to_csv(os.path.join(settings.DATASET_DIR, 'titles.csv'), index=False, quoting=csv.QUOTE_ALL)
    print("Dataframe saved")


if __name__ == '__main__':
    download_data()
    prepare_titles_df()