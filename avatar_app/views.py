from django.shortcuts import render
from .avatar_api.interactin_w_api import generate_chars,get_one_char
# Create your views here.
def home(requests):
    return render(requests,'avatar_app/home.html')


def chars1(request, page_num=1):  # Definindo um valor padrão de página 1
    chars = generate_chars(page_num)  # Passando o número da página para `generate_chars`
    max_page = 50
    if page_num > max_page:
        page_num = max_page
    is_last_page = page_num >= max_page
    return render(request, 'avatar_app/personagens.html', {
        'Chars': chars,
        'page_num': page_num,
        'is_last_page': is_last_page
    })
def one_char(request,id):
    char = get_one_char(id)
    return render(request,'avatar_app/personage_individual.html',{'Char':char})