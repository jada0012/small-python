import feedparser

newsfeed = feedparser.parse("www.jamaica-gleaner.com/feed/rss.xml")
entry = newsfeed.entries[0]
print(entry.keys())