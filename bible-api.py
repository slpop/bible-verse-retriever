# Bible API retrieved from labs.bible.org
# Bible translation Scripture quoted by permission.
# Quotations designated (NET) are from the NET Bible® copyright ©1996, 2019 by Biblical Studies Press, L.L.C.
# http://netbible.com All rights reserved.

import requests
API_URL = "http://labs.bible.org/api/?passage="

print("Bible translation Scripture quoted by permission.\n"
      "Quotations designated (NET) are from the NET Bible® copyright ©1996, 2019 by Biblical Studies Press, L.L.C.\n"
      "http://netbible.com All rights reserved.")

while True:
    book = input("Enter a book of the Bible (i.e. John): ")
    chapter = input("Enter the chapter number (i.e. 3): ")
    verses = input("Enter the verse number range (i.e. 16-17): ")
    SEARCH_URL = API_URL + book + "+" + chapter + ":" + verses + "&formatting=plain"
    response = requests.get(SEARCH_URL)
    print(response.text)
    print("(NET)")

    answer = input("Would you like to search for another verse? y/n: ")
    if answer == "n":
        break

