# Otkrivanje znanja u podacima - Završni rad

- Diplomski studij
- Odjel za informatiku, Sveučilište u Rijeci
- Završni rad, 2021/2022
- Autori: Andrea Hrelja i Mario Sliško


## Opis zadatka
<img src="assets/imdb-logo.png" alt="IMDb logo" width="200"/>

  Potrebno je izvršiti analizu podataka po fazama kao što su opisani u knjizi (Data Science Using Python and R, Daniel T. Larose), prema načelima metodologije podatkovnih znanosti. Analiziraju se IMDB skupovi podataka - nastoji se predvidjeti prosječnu ocjenu filma na temelju redatelja i žanra kojeg režisira.


## Sadržaj

1. [Razumijevanje problema](#razumijevanje)
2. [Priprema podataka](#priprema)
3. [Istraživačka analiza podataka](#eda)
4. [Oblikovanje baznog modela, balansiranje podataka, particija podataka (treniranje i testiranje)](#model)
5. [Primjena različitih postupaka strojnog učenja](#postupci)
6. [Odabir najboljeg modela, evaluacija](#evaluacija)
7. [Primjena u stvarnim uvjetima](#primjena)

## Razumijevanje problema <a name="razumijevanje"></a>

Analiziraju se [IMDB Dataset](https://www.imdb.com/interfaces/) skupovi podataka:
- `title.ratings.tsv.gz` - Prosječna ocjena filma
- `name.basics.tsv.gz` - Informacije o dionicima filma (imena i prezimena redatelja, pisaca, glumaca i ostalih)
- `title.basics.tsv.gz` - Informacije o filmu (naziv, godina, vrsta, žanrovi...)
- `title.principals.tsv.gz` - Predstavlja veze između filma i njegovih dionika

Nastoji se predvidjeti prosječnu ocjenu filma na temelju redatelja i žanra kojeg režisira.

## Priprema podataka <a name="priprema"></a>

Koristi se Python modul [prepare.py](./src/prepare.py).  
Datoteke dijele varijable `tconst` kao ID filma, te `nconst`  kao ID dionika. Iz svakog se skupa podataka prikuplja nekoliko varijabli:

    - title.ratings.tsv.gz
      - tconst (string)
      - averageRating (float)
      - numVotes (integer)

    - name.basics.tsv.gz
      - nconst (string)
      - primaryName (string)
    
    - title.basics.tsv.gz
      - tconst (string)
      - titleType (string)
      - primaryTitle (string)
      - startYear (YYYY)
      - runtimeMinutes (integer)
      - genres (array of strings)
    
    - title.principals.tsv.gz
      - tconst (string)
      - nconst (string)
      - ordering (integer)
      - job (string)


## Istraživačka analiza podataka <a name="eda"></a>

Koristi se Jupyter bilježnica [eda.ipynb](./src/eda.ipynb).  

## Oblikovanje baznog modela, balansiranje podataka, particija podataka (treniranje i testiranje) <a name="model"></a>

Transformacije koje oblikuju bazni model:
  - filtriraju se filmovi tipa *movie* (`titleType=movie`)
  - filtirirani se dataframe svodi (`OneHotEncoding`) na bazni model [režiser, žanrovi, prosječna_ocjena]
  - podaci se balansiraju tako da svaka prosječna_ocjena (`rating`) sadrži točno 90000 uzoraka nezavisnih varijabli
  - podaci se particioniraju na trening i test podatke (70% `train`; 30% `test`)

One Hot Encoding je algoritam koji svaku vrijednosti jedne varijable (svaku kategoriju jednog direktora) pretvara u zasebnu nezavisnu varijablu:

    - nezavisne varijable
      - directorID (integer)
      - Action (bool)
      - Adult (bool)
      - Adventure (bool)
        ...
      - Talk (bool)
      - War (bool)
      - Western (bool)

    - zavisna varijabla
      - rating (array of integers) [1, 2, 3, 4, 5]

Podaci se balansiraju tako da bazni model sadrži isti broj uzorka za svaku target kategoriju.  


## Primjena različitih postupaka strojnog učenja <a name="postupci"></a>

Primijenjuju se modeli:
- Decision Tree Classifier (stablo odlučivanja)
- Random Forest Classifier (slučajne šume)
- MLP Classifier (nerualna mreža)
- Logistic Regression (regresijska metoda)

Svaki se model primijenjuje nad balansiranim i nebalansiranim podacima sa zadanim konfiguracijama hiper parametara ([model_config.py](./src/model_config.py)).

## Odabir najboljeg modela, evaluacija (u odnosu na bazni model, model treba biti osjetljiv na cijenu pogreške) <a name="evaluacija"></a>

Kao najbolji klasifikatori, u ovom su se eksperimentu pokazali stabla odlučivanja i slučajne šume s identičnim ocjenama:

    - train: 99%
    - test: 59%

Primjena ovakvog klasifikatora ne bi bila praktična. Za bolje rezultate klasifikacije, potrebno je proširiti skup nezavisnih varijabli.

## Primjena u stvarnim uvjetima <a name="primjena"></a>

  - Christopher Nolan
  - Lamberto Sanfelice
