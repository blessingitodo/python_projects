highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

print(highlighted_poems)
highlighted_poems_list = highlighted_poems.split(',')
print(highlighted_poems_list)

highlighted_poems_stripped = []
for poem in highlighted_poems_list:
  poem_stripped = poem.strip()
  highlighted_poems_stripped.append(poem_stripped)
print(highlighted_poems_stripped)

highlighted_poems_details = []
for poem in highlighted_poems_stripped:
  poem_split = poem.split(':')
  highlighted_poems_details.append(poem_split)
print(highlighted_poems_details)

titles = []
poets = []
dates = []

for poem in highlighted_poems_details:
  title = poem[0]
  poet = poem[1]
  date = poem[2]
  titles.append(title)
  poets.append(poet)
  dates.append(date)
print(titles)
print(poets)
print(dates)

for i in range(len(titles)):
  formatting = "The poem {title} was published by {poet} in {date}.".format(title=titles[i], poet=poets[i], date=dates[i])
  print(formatting)


