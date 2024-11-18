import requests

def get_chars(page_num=1):
    res = requests.get(f'https://last-airbender-api.fly.dev/api/v1/characters?perPage=10&page={page_num}')
    return res.json()

def generate_chars(page_num=1) -> list:
    "Essa função retorna uma lista de dicionarios contendo os personagens trazidos da api"
    chars = get_chars(page_num)
    char_list = []
    for elem in chars:
        photo_url = elem.get('photoUrl')
        affi = elem.get('affiliation','Sem affiliação')

        char_list.append({'Nome': elem['name'], 'inimigos': ' '.join(elem['enemies']) or 'Não possue inimigos ', 'afiliacao': affi, 'photo_id':photo_url, 'aliados': ' '.join(elem['allies']), 'id':elem['_id']})
    return char_list

def get_one_char(id) -> dict:
    res = requests.get(f'https://last-airbender-api.fly.dev/api/v1/characters/{id}').json()
    primeira = res.get('first')
    primeira = 'desconhecido' if primeira == '"' else primeira
    lamo = {'name':res.get('name','?'),'enemies':''.join(res['enemies']) or 'Não possue inimigos','hair':res.get('hair','?'),'weapon':res.get('weapon','não possue'),'position':res.get('position','?'),'first':primeira,'affiliation':res.get('affiliation','?'),'allies':' '.join(res['allies']) or 'Não possue aliados','photoUrl':res.get('photoUrl'),'profession':res.get('profession','não possue'),'gender':res.get('gender','?')}
    return lamo