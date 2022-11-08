from django.shortcuts import render
import requests
from django.http import HttpResponse

# Create your views here.
def main(requests):
    print('RUnning...')
    return HttpResponse('HELLO')

if __name__ == '__main__':
    main()
