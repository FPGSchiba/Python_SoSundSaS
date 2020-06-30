#! Für Linux ausführung freihalten
# Author: Jann Erhardt
# Version 1.0.1
# Changes:
# ================
# No changes yet
# ================
# No Copy Right yet

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
    tempp = temps[3]
    temps = temp.split("<")
    tempps = tempp.split("<")
    end = temps[0] + tempps[0]
    return end


def getClass(inpString):
    end = ""
    temps = str(inpString).split("\"")
    try:
        end = temps[1]
    except:
        end = "sos"
    return end

def replaceNonASCII(String):
    String = String.replace("ä", "ae")
    String = String.replace("Ä", "Ae")
    String = String.replace("à", "a")
    String = String.replace("â", "a")
    String = String.replace("ö", "oe")
    String = String.replace("Ö", "Oe")
    String = String.replace("ô", "o")
    String = String.replace("ü", "ue")
    String = String.replace("Ü", "Ue")
    String = String.replace("û", "u")
    String = String.replace("é", "e")
    String = String.replace("è", "e")
    String = String.replace("ê", "e")
    String = String.replace("î", "i")
    String = String.replace("½", "1/2")
    String = String.replace("⅓", "1/3")
    String = String.replace("⅔", "2/3")
    String = String.replace("¼", "1/4")
    String = String.replace("¾", "3/4")
    String = String.replace("⅕", "1/5")
    return String


def ScrapFooby(URL):
    Rezept = []
    Liste = []
    try:
        page = requests.get(URL)
    except:
        print("Wrong URL")
        return ""

    soup = BeautifulSoup(page.content, 'html.parser')

    resultMetaHeadercomplete = soup.find(class_="page-header-recipe__meta-container")

    if resultMetaHeadercomplete == None:
        print("wrong URL")
        return ""

    print("start parsing...")

    # Parsen der Einzelnen Meta-infos zum Gericht
    resultMetaHeadercomplete = soup.find(class_="page-header-recipe__meta-container")
    resultMetaNaehrwert = resultMetaHeadercomplete.find("span", itemprop="calories")
    resultMetaFett = resultMetaHeadercomplete.find("span", itemprop="fatContent")
    resultMetaHydrate = resultMetaHeadercomplete.find("span", itemprop="carbohydrateContent")
    resultMetaEi = resultMetaHeadercomplete.find("span", itemprop="proteinContent")

    # Header der Zutaten Liste Parsen
    resultIngListcomplete = soup.find(class_="recipe-ingredientlist")
    resultsIngListHeaders = resultIngListcomplete.find_all("p", class_="heading--h3")
    headerslist = []

    # Alle Header in Headers speichern
    for header in resultsIngListHeaders:
        headerslist.append(deleteTagsEinzel(header).replace(" ", "_"))

    # Alle Zutaten Parsen
    resultsIngListwrappers = resultIngListcomplete.find_all("div", class_="recipe-ingredientlist__step-wrapper")
    wrappercount = 0
    headerWrite = False
    ListString = ""
    isheader = False
    debugHeader = []

    # Alle Header und Zutaten einander zuweisen und ausgeben
    for wrapper in resultsIngListwrappers:
        wrapps = wrapper.find_all("div", class_="recipe-ingredientlist__ingredient-wrapper")
        if getClass(wrapper.find_previous()) == "heading--h3":
            if not debugHeader.__contains__(deleteTagsEinzel(wrapper.find_previous())):
                isheader = True
                debugHeader.append(deleteTagsEinzel(wrapper.find_previous()))
        for wrapp in wrapps:
            quant = wrapp.find("span", class_="recipe-ingredientlist__ingredient-quantity")
            desc = wrapp.find("span", class_="recipe-ingredientlist__ingredient-desc")
            if isheader:
                if not headerWrite:
                    header = headerslist[wrappercount]
                    Liste.append(header)
                    ListString += "{" + header
                    headerWrite = True
                    isheader = False
                    wrappercount += 1
            Liste.append(deleteTagsQuant(quant) + "&&" + deleteTagsEinzel(desc))
            ListString += "\\" + deleteTagsQuant(quant) + "&&" + deleteTagsEinzel(desc)
        headerWrite = False

    # Rezepte Alles Parsen
    resultRezeptcomplete = soup.find("div", itemprop="recipeInstructions")
    headersrec = resultRezeptcomplete.find("p", class_="heading--h3")

    # Alle <p> aus dem Rezept Parsen
    temps = resultRezeptcomplete.find_all("p")
    RezeptString = ""
    rezheaderslist = []

    # Alles Ausgeben
    for i in range(len(temps)):
        if getClass(temps[i]) == "heading--h3":
            Rezept.append(deleteTagsEinzel(temps[i]))
            RezeptString += "{" + deleteTagsEinzel(temps[i])
            rezheaderslist.append(deleteTagsEinzel(temps[i]))
        else:
            Rezept.append(deleteTagsEinzel(temps[i]))
            RezeptString += "\\" + deleteTagsEinzel(temps[i])

    # Den YouTube URL aus den Bild ableiten und ausgeben
    resultsVidcomplete = soup.find_all("div", class_="recipedetail-how-to-videos__image-wrapper")
    containsVid = False
    vids = []

    for i in resultsVidcomplete:
        try:
            resultVidImgs = i.find_all("img")
            for resultVidImg in resultVidImgs:
                temps = str(resultVidImg).split("/")
                end = temps[4]
                vids.append("https://www.youtube.com/watch?v={id:11s}".format(id=end))
                yt = "https://www.youtube.com/watch?v={id:11s}".format(id=end)
                containsVid = True
        except Exception:
            print("", end="")

    print("parsing complete.")
    print("creating XML...")

    # Ein XML-Dokument ertsellen mit den parsed Daten
    # Alle Metha-Daten ins XML einfügen
    XMLString = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
    XMLString += "<Rezept>\n"
    XMLString += "   <meta>\n"
    XMLString += "       <NaehrwertProPerson>{kcal:8s}</NaehrwertProPerson>\n".format(
        kcal=deleteTagsEinzel(resultMetaNaehrwert))
    XMLString += "       <Fett>{fett:6s}</Fett>\n".format(fett=deleteTagsEinzel(resultMetaFett))
    XMLString += "       <Kohlenhydrate>{hydrate:6s}</Kohlenhydrate>\n".format(
        hydrate=deleteTagsEinzel(resultMetaHydrate))
    XMLString += "       <Eiweiss>{ei:6s}</Eiweiss>\n".format(ei=deleteTagsEinzel(resultMetaEi))
    XMLString += "   </meta>\n"
    XMLString += "   <einkaufliste>\n"

    hasNoHeader = False

    if headerslist.__len__() == 0:
        headerslist.append("Liste")
        hasNoHeader = True

    # Die Einkaufsliste ins File einfügen
    Lists = ListString.split("{")
    headercout = 0
    for list in Lists:
        if not list == "":
            tempps = list.split("\\")
            for i in tempps:
                if hasNoHeader:
                    XMLString += "      <{header:10s}>\n".format(header=headerslist[0])
                    hasNoHeader = False
                if headerslist.__contains__(i):
                    if not i == "":
                        XMLString += "      <{header:10s}>\n".format(header=i)
                else:
                    ingreds = i.split("&&")
                    if not ingreds == ['']:
                        XMLString += "          <quant>{inhalt:s}</quant>\n".format(inhalt=ingreds[0])
                        XMLString += "          <zutat>{inhalt:s}</zutat>\n".format(inhalt=ingreds[1])
            XMLString += "      </{header:10s}>\n".format(header=headerslist[headercout])
            headercout += 1

    XMLString += "   </einkaufliste>\n"
    XMLString += "   <rezept>\n"
    isHeader = True
    headercout = 0

    if rezheaderslist.__len__() == 0:
        rezheaderslist.append("Rezept")
        Rezept.insert(0, "Rezept")

    # Das Rezept ins File einfügen
    for i in Rezept:
        if isHeader:
            if not headercout >= rezheaderslist.__len__():
                XMLString += "      <{header:10s}>\n".format(header=rezheaderslist[headercout].replace(" ", "_"))
            isHeader = not isHeader
        else:
            XMLString += "          <inhalt>{inhalt:30s}</inhalt>\n".format(inhalt=i)
            if not headercout >= rezheaderslist.__len__():
                XMLString += "      </{header:10s}>\n".format(header=rezheaderslist[headercout].replace(" ", "_"))
            isHeader = not isHeader
        if isHeader:
            headercout += 1

    # Video ins XML einfügen und File schliessen
    XMLString += "   </rezept>\n"
    if containsVid:
        for vid in vids:
            XMLString += "   <video href=\"{video:43s}\"/>\n".format(video=vid)
    XMLString += "</Rezept>"

    # Alle nicht ASCII Zeichen in Fooby ersetzten
    XMLString = replaceNonASCII(XMLString)

    # Den Namen der Datei bestimmen
    url = str(URL).split("/")
    nummer = url[5]
    FileName = "Rezepte/" + nummer + ".xml"

    # Die Datei Speichern
    try:
        file = open(FileName, "w")
        file.write(XMLString)
        file.close()
        print("XML done")
    except:
        print("XML error!")