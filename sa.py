#!/usr/bin/python3

import robobrowser
from bs4 import BeautifulSoup


class SomethingAwful():
    
    
    def __init__(self):
        self.password = input('Password>')
        self.browser = robobrowser.RoboBrowser(history=True, parser='html.parser')
        self.login_page = 'https://forums.somethingawful.com/account.php?action=loginform#form'
        self.favorites = 'https://forums.somethingawful.com/usercp.php'

    def login(self):
        self.browser.open(self.login_page)
        self.form = self.browser.get_forms()
        print(self.form)
        self.form = self.form[1]
        self.form['username'].value = 'sysv fanfic'
        self.form['password'].value = self.password
        self.browser.submit_form(self.form)
        
        self.browser.open(self.favorites)
        #print(self.browser.find_all())
        
    def fetch_index(self):
        pass


s = SomethingAwful()
s.login()

#print(s.browser)
#print(s.browser.find_all('tr', 'thread'))
#print(s.browser.find_all('a', 'count'))
#soup = BeautifulSoup(html_doc, 'html.parser')

if __name__ == '__main__':
    for i in s.browser.find_all('tr', 'thread'):
        name = i.find('a', 'thread_title').text
        count = i.find('a', 'count')
        if count:
            count = count.text
            print (f"{name} has {count} new posts")
        else:
            print (f"{name} has no new posts")
