import behave
import parse
import pages


def register_type_parsers() -> None:
    behave.register_type(PageType=parse_page_type)


@parse.with_pattern(r".+")
def parse_page_type(page_type: str):
    return getattr(pages, page_type)
