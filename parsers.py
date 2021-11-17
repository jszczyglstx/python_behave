import behave
import parse
import pages
# nie ogarniam co tu sie dzieje
# dobra zaczynam troche ogarniac tu okreslasz typ danych argumentow ktore podajesz w scenario, sa to nazwy stron
# ja jebe to jest robione zeby dynamicznie importowac odpowiedniego page'a.



def register_type_parsers() -> None:
    behave.register_type(PageType=parse_page_type)

@parse.with_pattern(r".+")  #co oznacza ten reg patern ?  np zwraca pages.AbTesting ?
def parse_page_type(page_type: str):
    return getattr(pages, page_type)