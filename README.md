# pyHAL

Download and convert bibliography data from the [HAL repository](https://hal.archives-ouvertes.fr/).

## Simple example

To download a list of articles for Olivier Devauchelle (HAL ID: `olivier-devauchelle`), and store in a json file:

```python
from pyHAL import get_biblio_from_HAL

hal_ID = 'olivier-devauchelle'

get_biblio_from_HAL( hal_ID )
```
We can now load the json file, and print some of its data:

```python
from json import load as json_load

with open( './biblio_HAL_article_' + hal_ID + '.json' ) as the_file:
    biblio = json_load(the_file)

for reference in biblio['response']['docs'] :
    print(reference['title_s'][0], '(' + reference['producedDate_s'] + ')')
```
We get something like:

```console
>>> Streamwise streaks induced by bedload diffusion (2019-03-25)
>>> Forced dewetting on porous media (2007-03-10)
>>> Longitudinal profile of channels cut by springs (2011)
...
```
