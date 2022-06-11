from urllib.parse import urlparse

def parse(query: str) -> dict:
    elements = {}
    parts = urlparse(query)
    queries = parts.query.strip('&').split('&')

    if queries[0] != '':
        for item in queries:
            key, value = item.split('=')
            elements[key] = value

    return elements


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('http://example.com/?country=usa&city=detroit&district=downtown') == {'country': 'usa', 'city': 'detroit', 'district': 'downtown'}
    assert parse('http://example.com/?name=1') == {'name': '1'}
    assert parse('http://example.com/?path=hell') == {'path': 'hell'}
    assert parse('https://education.github.com/git-cheat-sheet-education.pdf') == {}
    assert parse('https://www.youtube.com/watch?v=kusM4BtJ07g&t=1110s') == {'v': 'kusM4BtJ07g', 't':'1110s'}
    assert parse('https://www.google.com/search?channel=fs&client=ubuntu&q=detroit') == {'channel': 'fs', 'client': 'ubuntu', 'q': 'detroit'}
    assert parse('https://lms.ithillel.ua/') == {}
    assert parse('http://example.com/bed.php?branch=bead') == {'branch': 'bead'}
    assert parse('https://www.example.com/act.php?bee=argument') == {'bee': 'argument'}
    assert parse('https://www.example.com/basin/art.php') == {}

def parse_cookie(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
