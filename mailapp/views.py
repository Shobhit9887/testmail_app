from django.shortcuts import render
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from bs4 import BeautifulSoup
# Create your views here.
def home(request):
    context = {}

    url = 'https://api.testmail.app/api/json?apikey=0d21f6e8-3f19-480c-b2b9-e4dd95aa1e92&namespace=irary&pretty=true'

    
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)


    rawResult = session.get(url);

    result = rawResult.json();

    newDict = {}

    for i in range(0, len(result['emails'])):
        emailData = result['emails'][i]
        # if "<html>" in emailData['html']:
        #     emailHtmlContent = BeautifulSoup(emailData['html'], 'html.parser')
        #     for data in emailHtmlContent(['style']):
        # # Remove tags
        #         data.decompose()
        #     # emailHtmlContent = ' '.join(emailHtmlContent.stripped_strings)
        # else:
        #     emailHtmlContent = emailData['html']
        # # if(emailHtmlContent.style != None):
        #     # emailHtmlContent = emailHtmlContent.style.unwrap()
        # # emailData['html'] = emailData['html']
        # emailData['html'] = emailHtmlContent
        newDict[i] = emailData

    context['mails'] = newDict
    context['range'] = range(len(result['emails']))

    return render(request, "index.html", context)
