# Otkrivanje znanja u podacima - 

- Diplomski studij
- Odjel za informatiku, Sveučilište u Rijeci
- Završni ispit, 2021/2022
- Autori: Andrea Hrelja i Mario Sliško

<img src="assets/imdb-logo.png" alt="IMDb logo" width="200"/>

**Opis zadatka**: Potrebno je izvršiti analizu podataka po fazama kao što su opisani u knjizi (Data Science Using Python and R, Daniel T. Larose), prema načelima metodologije podatkovnih znanosti. Analizira se IMDb skup podataka - nastoji se predvidjeti prosječnu ocjenu filma na temelju redatelja i žanra kojeg režisira.


## Sadržaj

1.	Razumijevanje problema
2.	Priprema podataka

3.	Istraživačka analiza podataka

4.	Oblikovanje baznog modela, balansiranje podataka, particija podataka (treniranje i testiranje)

5.	Primjena različitih postupaka strojnog učenja

6.	Odabir najboljeg modela, evaluacija (u odnosu na bazni model, model treba biti osjetljiv na cijenu pogreške)

7.	Primjena u stvarnim uvjetima

8.	Zaključak


## Razumijevanje problema

## Priprema podataka

## Istraživačka analiza podataka

## Oblikovanje baznog modela, balansiranje podataka, particija podataka (treniranje i testiranje)
    
  - filtriramo cjelokupni dataframe na [titleType=movie]
  - svodimo cjelokupni dataframe na bazni model [režiser, žanrovi, prosječna_ocjena]
  - balansiramo podatke tako da svaka prosječna_ocjena sadrži točno 40000 uzoraka nezavisnih varijabli
  - particioniramo podatke (66% train; 33% test)


## Primjena različitih postupaka strojnog učenja
    
  - Stabla odlučivanja
  - Slučajne šume
  - Logistička regresija
  - MLPClassifier


## Odabir najboljeg modela, evaluacija (u odnosu na bazni model, model treba biti osjetljiv na cijenu pogreške)
    
  - Stabla odlučivanja
  - Slučajne šume


## Primjena u stvarnim uvjetima

  - Christopher Nolan
  - Lamberto Sanfelice


## Zaključak

