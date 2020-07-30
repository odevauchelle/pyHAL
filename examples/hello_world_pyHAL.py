import sys
sys.path.append('./../')

import pyHAL

hal_ID = 'olivier-devauchelle'

pyHAL.get_biblio_from_HAL( hal_ID )

from json import load as json_load

with open( './biblio_HAL_article_' + hal_ID + '.json' ) as the_file:
    biblio = json_load(the_file)

for reference in biblio['response']['docs'] :
    print(reference['title_s'][0], '(' + reference['producedDate_s'] + ')')
