# change absolute path according to your current working directory
absolute_path = '/Users/warda/Desktop/INTELLIGENT LEGAL ADVISOR FYP/'

from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render_to_response
import MySQLdb

from django.http import HttpResponseRedirect

from django.conf import settings
from django.core.files.storage import FileSystemStorage

from django.http import JsonResponse

# import all algorithms here
import sys
sys.path.append(
    absolute_path + 'intelligent_law/verdict_main')
sys.path.append(
    absolute_path + 'intelligent_law/summary')
sys.path.append(absolute_path + 'intelligent_law/legal_advice')
import main         # main.py from verdict_main module
import summary_try  # summary_try.py from summary module
import cosine       # cosine.py from  legal_advice module
import soft_cosine  # soft_cosine.py from  legal_advice module


def home(request):
    return render(request, 'law_site/index.html')


def login(request):
    return render(request, 'law_site/login.html')


def document_similarity(request):
    return HttpResponseRedirect('http://localhost:5000')


def case_to_section(request):
    return render(request, 'law_site/case_to_section.html')


def get_bot_answer(request):
    user_message = request.GET.get('user_message', None)
    print(user_message)
    cosine_sections = cosine.get_cosine_sections(
        absolute_path, user_message)
    bot_answer = cosine_sections
    # soft_cosine_sections = soft_cosine.get_soft_cosine_sections(
    # absolute_path, user_message)
    # bot_answer = cosine_sections + '</br></br>' + soft_cosine_sections
    data = {
        'bot_answer': bot_answer
    }
    return JsonResponse(data)


def summarize(request):

    if request.method == 'POST' and request.FILES['myfile']:
        # save uploaded file to server directory /media/
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)

        # summarize users document
        summary = summary_try.summarize_document(myfile.name)

        # delete the file that user uploaded to server directory /media/
        fs.delete(myfile.name)

        # read the summary.txt files content and return it to website
        context = {'file_content': summary}
        return render(request, 'law_site/summarize.html', context)

    return render(request, 'law_site/summarize.html')


def predict_verdict(request):

    if(request.GET.getlist('fileupload') != []):
        file_name = request.GET.getlist('fileupload')[0]
        article_list = main.predict_articles(file_name)
        articles = {'articles': article_list}
        return render_to_response('law_site/verdict.html', articles)
    else:
        articles = {'articles': []}
        return render_to_response('law_site/verdict.html', articles)


def show_lawyers(request):
    # get city and category from url
    city = request.GET.getlist('city')[0]
    category = request.GET.getlist('category')[0]

    # connect to mysql fyp database (table = lawyers)
    db = MySQLdb.connect(user='warda', db='fyp',
                         passwd='wkwkaam', host='localhost')
    cursor = db.cursor()

    # filter results based on user selection
    if city == '' and category == '':   # show all
        sqlquery = "SELECT * FROM lawyers"
    elif category == '':                # filter by city
        sqlquery = "SELECT * FROM lawyers WHERE city LIKE '%" + city + "%'"
    elif city == '':                    # filter by category
        sqlquery = "SELECT * FROM lawyers WHERE category LIKE '%" + category + "%'"
    else:                               # filter by city AND category
        sqlquery = "SELECT * FROM lawyers WHERE city LIKE '%" + \
            city + "%' AND category LIKE '%" + category + "%'"

    cursor.execute(sqlquery)

    rows = cursor.fetchall()
    names = [row[0] for row in rows]
    addresses = [row[1] for row in rows]
    contacts = [row[2] for row in rows]
    emails = [row[3] for row in rows]
    categories = [row[4] for row in rows]
    cities = [row[5] for row in rows]

    lawyers = zip(names, addresses, contacts,
                  emails, categories, cities)
    diary = {'lawyers': lawyers}
    # diary = {'names': names,
    #          'addresses': addresses,
    #          'contacts': contacts,
    #          'emails': emails,
    #          'categories': categories,
    #          'cities': cities}
    db.close()

    return render_to_response('law_site/lawyer_data.html', diary)
