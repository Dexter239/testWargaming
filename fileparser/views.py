from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
import collections
# Create your views here.

#Главная страница
def main(request):
    return render(request, "index.html")

#удаление всех вхождений в список
def listRemoveAll(the_list, val):
   return [value for value in the_list if value != val]

#Функция возврата информации о файле
def getInfo(request):
    if request.method == "POST":
        file = request.FILES['file']
        if file: #Если файл существует, идет парсинг
            str = file.read().decode('utf-8').lower()
            str = str.replace('.', '')
            str = str.replace('!', '')
            str = str.replace('?', '')
            str = str.replace(',', '')
            str = str.replace(':', '')
            str = str.replace(';', '')
            str = str.replace('\r', '')
            str = str.replace('\n', ' ')
            str = str.replace('\t', '')
            str = str.replace('\"', '')
            str = str.replace('\'', '')
            words_list = listRemoveAll(str.split(' '), '')
            tf_words = collections.Counter(words_list)
            for i in tf_words:
                tf_words[i] = tf_words[i] / float(len(words_list))
            tf_words.most_common()
            return JsonResponse({'er': 0, 'words': tf_words})
        return JsonResponse({'er': 1})
    return HttpResponseRedirect('/')