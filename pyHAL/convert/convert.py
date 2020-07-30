# -*- coding: utf-8 -*-

from datetime import datetime
import urllib.request

###############################################################

weird_character_replacement = { '‐' : '-' }

def replace_weird_characters( string ) :

    for weird_character, new_character in weird_character_replacement.items() :
        string = string.replace( weird_character, new_character )

    return string


def StringDate_2_datetime( StringDate ):

    try :
        date = datetime.strptime( StringDate, '%Y-%m-%d')

    except :
        try :
            date = datetime.strptime( StringDate, '%Y-%m')

        except :
            try :
                date = datetime.strptime( StringDate, '%Y')

            except :
                print ( '--------------------------------------' )
                print ( 'StringDate_2_datetime Alert !' )
                print ( 'Error date !' )
                print ( StringDate )
                print ( '--------------------------------------' )

    return date

def reference_json_to_html( reference ):

    reference_html = ''

    try :
        DOI = reference['doiId_s']
        before_title = u'<a HREF="http://dx.doi.org/' + DOI + u'">'
        after_title = '</a>'

    except :
        before_title = ''
        after_title = ''

    reference_html += before_title + reference['title_s'][0] + after_title + ', '

    for author in reference['authFullName_s'] :
        reference_html += author + ', '

    try :
        reference_html += u'<I>' + reference['journalTitle_s'] + u'</I>' + ', '
    except :
        reference_html += u'<I>' + reference[u'conferenceTitle_s'] + u'</I>' + ', '

    try :
        reference_html += u'<b>' + reference['volume_s'] + u'</b>' + ', '
    except :
        pass

    try :
        pages = '-'.join( reference['page_s'].replace('-',' ').split() )
        reference_html +=u'<i>' + pages + u'</i>'+ ', '
    except :
        pass

    pub_date = StringDate_2_datetime( reference['producedDate_s'] )

    reference_html += pub_date.strftime("%Y")
    try :
        HAL_url = reference['fileMain_s']
        reference_html += ' '
        reference_html += u'<a HREF="' + HAL_url + u'">'
        reference_html += '[pdf HAL]'
        reference_html += '</a>'

    except :
        pass


    try :
        arxiv_url = reference['arxivId_s']
        reference_html += ' '
        reference_html += u'<a HREF="https://arxiv.org/pdf/' + arxiv_url + u'">'
        reference_html += '[pdf arXiv]'
        reference_html += '</a>'

    except :
        pass

    return reference_html

def sort_json_biblio_by_date(biblio) :
    return sorted( biblio, key = lambda r: StringDate_2_datetime( r['producedDate_s'] ) )[::-1]

def biblio_json_to_html( biblio ) :

    biblio_html = ''

    for reference in sort_json_biblio_by_date( biblio['response']['docs'] ) :

        biblio_html += u'<p>\n' + reference_json_to_html( reference ) + '\n</p>\n'

    print( str(len(biblio['response']['docs'])) + ' references converted to html.' )

    return biblio_html

def filter_biblio_by_period( biblio, date_min, date_max ) :

    filtered_biblio = []

    for article in biblio :

        date = StringDate_2_datetime( article['producedDate_s'] )

        if ( date >= date_min ) & ( date <= date_max ) :
                filtered_biblio += [ article ]

    return filtered_biblio

default_conversion = lambda x: x

def author_conversion( author_list ) :

    author_str = author_list[0]

    try :
        for author in author_list[1:] :
            author_str += ' and ' + author

    except :
        pass

    return author_str

def title_conversion( title_str ):
    return '{' + title_str[0] + '}'

bibtex_attributes = {
    'author' : ( 'authFullName_s', author_conversion  ),
    'journal' : 'journalTitle_s',
    'title' : ( 'title_s', title_conversion ),
    'volume' : 'volume_s',
    'year' : ( 'producedDate_s', lambda x: str( x[:4] ) ),
    'pages' : 'page_s'
    }


def hal_to_bibtex( article ) :

    article_bibtex = '@article{'

    article_bibtex += article['halId_s'] + ',\n'

    for attribute_name in bibtex_attributes.keys() :

        try :

            attribute = bibtex_attributes[ attribute_name ]

            if type( attribute ) == type( ( 1, ) ) :
                attribute, conversion = attribute

            else :
                attribute, conversion = attribute, default_conversion

            article_bibtex += ' ' + attribute_name + ' = {' + conversion( article[ attribute ] ) + '},\n'

        except :
            pass

    article_bibtex += '}\n'

    return replace_weird_characters( article_bibtex )

def author_conversion_tex( author_list ) :

    author_str = author_list[0]

    try :
        for author in author_list[1:-1] :
            author_str += ', ' + author

    except :
        pass

    author_str += ' et ' + author_list[-1]

    return author_str


tex_attributes = [
    ( 'title_s', title_conversion ),
    ( 'authFullName_s', author_conversion_tex  ),
    ( 'journalTitle_s', lambda x: '\emph{' + x + '}' ),
    ( 'volume_s', lambda x: u'{\\bf ' + x + '}' ),
    'page_s',
    ( 'producedDate_s', lambda x: x[:4] ),
    ]


def get_hyperlink( article ) :

    hyperlink_keys = [ ('fileMain_s',''), ('arxivId_s','https://arxiv.org/pdf/'), ('doiId_s', 'http://dx.doi.org/' ) ]

    html_link = ''

    for key in hyperlink_keys :

        try :
            html_link = key[1] + article[key[0]]
            break

        except :
            pass


    return html_link


def hal_to_tex( article, href = False ) :

    html_link = ''

    if href :
        html_link = get_hyperlink( article )

    if html_link != '' :
        article_tex = '\\href{' + html_link + '}'

    else :
        article_tex = ''

    for attribute in tex_attributes :

        try :

            if type( attribute ) == type( ( 1, ) ) :
                attribute, conversion = attribute

            else :
                attribute, conversion = attribute, default_conversion

            article_tex += conversion( article[ attribute ] ) + ',\n'

        except :
            pass

    article_tex = article_tex[:-2]

    article_tex += '.\n'

    return replace_weird_characters( article_tex )
