# -*- coding: utf-8 -*-

from datetime import datetime
import urllib.request

###############################################################

def get_biblio_from_HAL( hal_ID, biblio_file_name = None, ref_type = 'article', path = None ) :
    '''
    Get bibliography data from HAL repository.

    get_biblio_from_HAL( hal_ID, biblio_file_name, ref_type = 'article', path = None )

    Arguments:
        hal_ID (string) : HAL identifier
        biblio_file_name (string) : Json output file name
        ref_type ( 'article' or 'proceeding' ) : Type of reference
        path (string): Path to json output

    '''

    if path is None :
        path = './'


    if biblio_file_name is None :
        biblio_file_name = 'biblio_HAL_' + ref_type + '_' + hal_ID + '.json'

    if ref_type == 'article' :
        biblio_hal_url = "https://api.archives-ouvertes.fr/search/hal/?omitHeader=true&wt=json&q=authIdHal_s%3A%28" + hal_ID + "%29&fq=NOT+instance_s%3Asfo&fq=NOT+instance_s%3Adumas&fq=NOT+instance_s%3Amemsic&fq=NOT+%28instance_s%3Ainria+AND+docType_s%3A%28MEM+OR+PRESCONF%29%29&fq=NOT+%28instance_s%3Aafssa+AND+docType_s%3AMEM%29&fq=NOT+%28instance_s%3Aenpc+AND+docType_s%3A%28OTHERREPORT+OR+MINUTES+OR+NOTE+OR+SYNTHESE+OR+MEM+OR+PRESCONF%29%29&fq=NOT+%28instance_s%3Auniv-mlv+AND+docType_s%3A%28OTHERREPORT+OR+MINUTES+OR+NOTE+OR+MEM+OR+PRESCONF%29%29&fq=NOT+%28instance_s%3Ademocrite+AND+docType_s%3AMEM%29&fq=NOT+%28instance_s%3Aafrique+AND+docType_s%3AMEM%29&fq=NOT+%28instance_s%3Asaga+AND+docType_s%3A%28PRESCONF+OR+BOOKREPORT%29%29&fq=NOT+%28instance_s%3Aunice+AND+docType_s%3AMEM%29&fq=NOT+%28instance_s%3Alara+AND+docType_s%3AREPACT%29&fq=NOT+%28docType_s%3A%28THESE+OR+HDR%29+AND+submitType_s%3A%28notice+OR+annex%29%29&fq=NOT+%28instance_s%3Alaas+AND+docType_s%3AMEM%29&fq=NOT+%28instance_s%3Aephe+AND+docType_s%3AMEM%29&fq=NOT+status_i%3A111&fq=%7B%21tag%3Dtag0__docType_s%7DdocType_s%3A%28%22ART%22%29&defType=edismax&rows=2000&fl=halId_s%2Cversion_i%2Curi_s%2CdocType_s%2CdoiId_s%2CnntId_s%2Ctitle_s%2CarxivId_s%2CsubTitle_s%2CauthFullName_s%2CproducedDate_s%2CfileMain_s%2Cdomain_s%2CjournalTitle_s%2CjournalPublisher_s%2Cvolume_s%2Cnumber_s%2Cpage_s%2CconferenceTitle_s%2CconferenceStartDate_s%2Ccountry_s%2Clanguage_s&sort=score+desc"

    elif ref_type == 'proceeding' :
        biblio_hal_url = "https://api.archives-ouvertes.fr/search/hal/?omitHeader=true&wt=json&q=authIdHal_s%3A%28" + hal_ID + "%29&fq=NOT+instance_s%3Asfo&fq=NOT+instance_s%3Adumas&fq=NOT+instance_s%3Amemsic&fq=NOT+%28instance_s%3Ainria+AND+docType_s%3A%28MEM+OR+PRESCONF%29%29&fq=NOT+%28instance_s%3Aafssa+AND+docType_s%3AMEM%29&fq=NOT+%28instance_s%3Aenpc+AND+docType_s%3A%28OTHERREPORT+OR+MINUTES+OR+NOTE+OR+SYNTHESE+OR+MEM+OR+PRESCONF%29%29&fq=NOT+%28instance_s%3Auniv-mlv+AND+docType_s%3A%28OTHERREPORT+OR+MINUTES+OR+NOTE+OR+MEM+OR+PRESCONF%29%29&fq=NOT+%28instance_s%3Ademocrite+AND+docType_s%3AMEM%29&fq=NOT+%28instance_s%3Aafrique+AND+docType_s%3AMEM%29&fq=NOT+%28instance_s%3Asaga+AND+docType_s%3A%28PRESCONF+OR+BOOKREPORT%29%29&fq=NOT+%28instance_s%3Aunice+AND+docType_s%3AMEM%29&fq=NOT+%28instance_s%3Alara+AND+docType_s%3AREPACT%29&fq=NOT+%28docType_s%3A%28THESE+OR+HDR%29+AND+submitType_s%3A%28notice+OR+annex%29%29&fq=NOT+%28instance_s%3Alaas+AND+docType_s%3AMEM%29&fq=NOT+%28instance_s%3Aephe+AND+docType_s%3AMEM%29&fq=NOT+status_i%3A111&fq=%7B%21tag%3Dtag0__docType_s%7DdocType_s%3A%28%22COMM%22%29&defType=edismax&rows=2000&fl=halId_s%2Cversion_i%2Curi_s%2CdocType_s%2CdoiId_s%2CnntId_s%2CarxivId_s%2Ctitle_s%2CsubTitle_s%2CauthFullName_s%2CdoiId_s%2CproducedDate_s%2Cdomain_s%2CfileMain_s%2CjournalTitle_s%2CjournalPublisher_s%2Cvolume_s%2Cnumber_s%2Cpage_s%2CconferenceTitle_s%2CconferenceStartDate_s%2Ccountry_s%2Clanguage_s&sort=score+desc"

    else :
        biblio_hal_url = ''

    if biblio_hal_url != '':
        urllib.request.urlretrieve( biblio_hal_url, path + biblio_file_name )
        print( "Saved biblio as " + path + biblio_file_name )

    else :
        print( "Unknown ref_type. No output." )
