import requests
from bs4 import BeautifulSoup


def writeHTML(input):
    file = open(".\output.txt", "w+")
    file.write(input)
    file.close()


def deleteTagsEinzel(inpString):
    liste = str(inpString).split(">")
    string1 = liste[1]
    liste = string1.split("<")
    end = liste[0]
    return end


def deleteTagsQuant(inpString):
    temps = str(inpString).split(">")
    temp = temps[2]
    temps = temp.split("<")
    end = temps[0]
    return end


def getClass(inpString):
    end = ""
    temps = str(inpString).split("\"")
    try:
        end = temps[1]
    except:
        end = "sos"
    return end


def ScrapFooby(URL):
    Rezept = []
    Liste = []

    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    # Parsen der Einzelnen Meta-infos zum Gericht
    resultMetaHeadercomplete = soup.find(class_="page-header-recipe__meta-container")
    resultMetaNaehrwert = resultMetaHeadercomplete.find("span", itemprop="calories")
    resultMetaFett = resultMetaHeadercomplete.find("span", itemprop="fatContent")
    resultMetaHydrate = resultMetaHeadercomplete.find("span", itemprop="carbohydrateContent")
    resultMetaEi = resultMetaHeadercomplete.find("span", itemprop="proteinContent")

    # output der einzelnen Meta-Infos zum Gericht
    print("Nährwert / Person: {zahl:15s}".format(zahl=deleteTagsEinzel(resultMetaNaehrwert)))
    print("Fett:              {zahl:15s}".format(zahl=deleteTagsEinzel(resultMetaFett)))
    print("Kohlenhydrate:     {zahl:15s}".format(zahl=deleteTagsEinzel(resultMetaHydrate)))
    print("Eiweiss:           {zahl:15s} \n".format(zahl=deleteTagsEinzel(resultMetaEi)))

    # Header der Zutaten Liste Parsen
    resultIngListcomplete = soup.find(class_="recipe-ingredientlist")
    resultsIngListHeaders = resultIngListcomplete.find_all("p", class_="heading--h3")
    headerslist = []

    # Alle Header in Headers speichern
    for header in resultsIngListHeaders:
        headerslist.append(deleteTagsEinzel(header))

    # Alle Zutaten Parsen
    resultsIngListwrappers = resultIngListcomplete.find_all("div", class_="recipe-ingredientlist__step-wrapper")
    wrappercount = 0
    headerWrite = False
    ListString = ""

    # Alle Header und Zutaten einander zuweisen und ausgeben
    for wrapper in resultsIngListwrappers:
        wrapps = wrapper.find_all("div", class_="recipe-ingredientlist__ingredient-wrapper")
        for wrapp in wrapps:
            quant = wrapp.find("span", class_="recipe-ingredientlist__ingredient-quantity")
            desc = wrapp.find("span", class_="recipe-ingredientlist__ingredient-desc")
            header = headerslist[wrappercount]
            if not headerWrite:
                print(header)
                Liste.append(header)
                headerWrite = True
                ListString += ";" + header
            print(deleteTagsQuant(quant), "", deleteTagsEinzel(desc))
            Liste.append(deleteTagsQuant(quant) + " " + deleteTagsEinzel(desc))
            ListString += ", " + deleteTagsQuant(quant) + " " + deleteTagsEinzel(desc)
        wrappercount += 1
        headerWrite = False

    print()

    # Rezepte Alles Parsen
    resultRezeptcomplete = soup.find("div", itemprop="recipeInstructions")
    headersrec = resultRezeptcomplete.find("p", class_="heading--h3")

    # Alle <p> aus dem Rezept Parsen
    temps = resultRezeptcomplete.find_all("p")
    RezeptString = ""

    # Alles Ausgeben
    for i in range(len(temps)):
        if getClass(temps[i]) == "heading--h3":
            print("{titel:20s}:".format(titel=deleteTagsEinzel(temps[i])))
            Rezept.append(deleteTagsEinzel(temps[i]))
            RezeptString += ";" + deleteTagsEinzel(temps[i])
        else:
            print(deleteTagsEinzel(temps[i]))
            Rezept.append(deleteTagsEinzel(temps[i]))
            RezeptString += ", " + deleteTagsEinzel(temps[i])

    print()

    # Den YouTube URL aus den Bild ableiten und ausgeben
    resultVidcomplete = soup.find("div", class_="recipedetail-how-to-videos__image-wrapper")
    containsVid = False
    try:
        resultVidImgs = resultVidcomplete.find_all("img")
        for resultVidImg in resultVidImgs:
            temps = str(resultVidImg).split("/")
            end = temps[4]
            yt = "https://www.youtube.com/watch?v={id:11s}".format(id=end)
            print(yt)
            containsVid = True
    except Exception:
        print("no vid")

    # Alles in einzelne Strings
    XMLString = "<Rezept>\n"
    XMLString += "   <meta>\n"
    XMLString += "       <NährwertProPerson>{kcal:8s}</NährwertProPerson>\n".format(kcal=deleteTagsEinzel(resultMetaNaehrwert))
    XMLString += "       <Fett>{fett:6s}</Fett>\n".format(fett=deleteTagsEinzel(resultMetaFett))
    XMLString += "       <Kohlenhydrate>{hydrate:6s}</Kohlenhydrate>\n".format(hydrate=deleteTagsEinzel(resultMetaHydrate))
    XMLString += "       <Eiweiss>{ei:6s}</Eiweiss>\n".format(ei=deleteTagsEinzel(resultMetaEi))
    XMLString += "   </meta>\n"
    XMLString += "   <einkaufliste>\n"

    Lists = ListString.split(";")
    headercout = 0
    for list in Lists:
        if not list == "":
            tempps = list.split(",")
            for i in tempps:
                if headerslist.__contains__(i):
                    if not i == "":
                        XMLString += "      <{header:10s}>\n".format(header=i)
                else:
                    XMLString += "          <inhalt>{inhalt:30s}</inhalt>\n".format(inhalt=i)
            XMLString += "      </{header:10s}>\n".format(header=headerslist[headercout])
            headercout += 1

    XMLString += "   </einkaufliste>\n"
    XMLString += "   <rezept>\n"
    headercout = 0
    Lists = RezeptString.split(";")
    for list in Lists:
        if not list == "":
            tempps = list.split(",")
            for i in tempps:
                if headerslist.__contains__(i):
                    XMLString += "      <{header:10s}>\n".format(header=i)
                else:
                    XMLString += "          <inhalt>{inhalt:30s}</inhalt>\n".format(inhalt=i)
            XMLString += "       </{header:10s}>\n".format(header=headerslist[headercout])
            headercout += 1

    XMLString += "   </rezept>\n"
    if containsVid:
        XMLString += "   <video href=\"{video:43s}\"/>\n".format(video=yt)
    XMLString += "</Rezept>"

    print(XMLString)
