# TLcodingtask
Its possible I may go past the 6 hour limit due to how long my code is taking to run.

I started my development by looking online for ways to iterate through the archives. I stumbled upon a package called comcrawl (https://github.com/michaelharms/comcrawl). This package allowed me to input certain archives from CommonCrawl and search for certain urls. For example, I could input "cnn.com/" and could get back all the urls that start with that prefix. I then could parse the results to choose only results that contain certain keywords in the url, such as "covid" and "economy". This worked somewhat well since most of the websites I used would put part of the article titles in the url.

The urls are saved in a CSV file.
