import requests

def get_chars(page_num=1):
    res = requests.get(f'https://last-airbender-api.fly.dev/api/v1/characters?perPage=10&page={page_num}')
    return res.json()

def generate_chars(page_num=1): 
    chars = get_chars(page_num)
    char_list = []
    for elem in chars:
        photo_url = elem.get('photoUrl')
        affi = elem.get('affiliation','Sem affiliação')

        char_list.append({'Nome': elem['name'], 'inimigos': ' '.join(elem['enemies']) or 'Não possue inimigos ', 'afiliacao': affi, 'photo_id':photo_url, 'aliados': ' '.join(elem['allies'])})
    return char_list
