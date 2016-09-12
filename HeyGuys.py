import requests
from bs4 import BeautifulSoup

_IMPORT_URL= "https://en.wikipedia.org/wiki/Polystyrene"
_NAME_OF_TAG='span'
_SPAN_CLASS_DICT={'name': 'class', 'attribute' : 'mw-headline'} # he he he css lul


def _get_webpage(url):
    _imported_web_page = requests.get(_IMPORT_URL)
    return _imported_web_page


def _make_soup_with_webpage(input_webpage):
    _imported_web_page_in_soup=BeautifulSoup(input_webpage.text, "html.parser")
    return _imported_web_page_in_soup


def _get_list_of_tags_with_specified_atributes(soup, tag_name, spec_dict):
    _all_spec_headers = soup.find_all(name=tag_name, attrs={spec_dict['name']: spec_dict['attribute']})
    return _all_spec_headers


def _tag_output(tag_list):
    for tag in tag_list:
        print(tag.text)


def main():
    _new_wild_webpage = _get_webpage(_IMPORT_URL)
    _casual_soup_done_by_me=_make_soup_with_webpage(_new_wild_webpage)
    _list_of_tags_found = _get_list_of_tags_with_specified_atributes(_casual_soup_done_by_me,_NAME_OF_TAG, _SPAN_CLASS_DICT)
    _tag_output(_list_of_tags_found)


if __name__ == '__main__':
    main()