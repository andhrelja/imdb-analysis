import os
import csv
import time
import requests
import pandas as pd

import settings

TITLES_DTYPE = {
    'startYear'       : 'string',
    'titleType'       : 'string',
    'primaryTitle'    : 'string',
    'directorName'    : 'string',
    'genres'          : 'object',
    'averageRating'   : 'float',
    'numVotes'        : 'int',
    'runtimeMinutes'  : 'int',
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


def get_title_basics(title_basics_df):
    include_types = ('short', 'movie', 'video', 'tvMovie')
    title_basics  = title_basics_df.loc[title_basics_df['titleType'].isin(include_types)]
    title_basics                   = title_basics.drop('endYear', axis=1)
    title_basics['runtimeMinutes'] = title_basics['runtimeMinutes'].transform(lambda x: 0 if x == '\\N' else x).astype('float')
    title_basics['startYear']      = title_basics['startYear'].transform(lambda x: '' if x == '\\N' else int(float(x))).astype('string')
    title_basics['isAdult']        = title_basics['isAdult'].map(bool)
    title_basics['genres']         = title_basics['genres'].transform(lambda x: [] if x == '\\N' else x.split(',')).astype('object')
    print(title_basics.info())
    return title_basics


def get_title_principals(title_principals_df):
    title_principals = title_principals_df.loc[(title_principals_df['category'] == 'director')]
    title_principals['ordering'] = title_principals.sort_values(['tconst', 'ordering']) \
        .groupby(['tconst']) \
        .cumcount() + 1
    return title_principals[title_principals['ordering'] == 1][['tconst', 'nconst']]


def prepare_titles_df():
    start = time.time()

    print("Reading datasets")
    title_basics_df = pd.read_csv(os.path.join(settings.DATASET_DIR, 'title.basics.tsv.gz'), compression='gzip', sep='\t')
    title_ratings_df = pd.read_csv(os.path.join(settings.DATASET_DIR, 'title.ratings.tsv.gz'), compression='gzip', sep='\t')
    title_principals_df = pd.read_csv(os.path.join(settings.DATASET_DIR, 'title.principals.tsv.gz'), compression='gzip', sep='\t')
    name_basics_df = pd.read_csv(os.path.join(settings.DATASET_DIR, 'name.basics.tsv.gz'), compression='gzip', sep='\t')
    name_basics_df = name_basics_df.rename(columns={'primaryName': 'directorName'})

    print("Transforming merged title_basics")
    title_basics = get_title_basics(title_basics_df)

    print("Transforming title principals dataframe")
    title_principals = get_title_principals(title_principals_df)
    title_principals = title_principals.merge(
        name_basics_df[['nconst', 'directorName']], 
        on='nconst'
    )

    print("Merging title ratings with title basics")
    titles_df = title_basics.merge(title_ratings_df, on='tconst')

    print("Merging title principals with merged titles")
    titles_df = titles_df.merge(title_principals, on='tconst')
    title_basics_df = titles_df[TITLES_DTYPE.keys()].astype(TITLES_DTYPE)
    print(titles_df.info())

    title_basics_df.to_csv(os.path.join(settings.DATASET_DIR, 'master.csv'), index=False, quoting=csv.QUOTE_ALL)
    print("Dataframe saved")

    end = time.time()
    print("Time elapsed: {} min".format((end-start)/60))


if __name__ == '__main__':
    download_data()
    prepare_titles_df()