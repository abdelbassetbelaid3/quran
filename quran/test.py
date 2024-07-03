import json
import requests
import aiohttp
import asyncio

class Quran:
    def __init__():
        pass
    
##############################        audio       ################################

# Get chapter's audio file of a reciter

def getReciterAudioForChapter(id,chapter_number):
    """ 
      Get chapter's audio file of a reciter

      id number required
      - The Id of the reciter

      chapter_number number required
      - Possible values: >= 1 and <= 114
      - The number of the chapter

    """
    url = f"https://api.quran.com/api/v4/chapter_recitations/{id}/{chapter_number}"



# List of all chapter audio files of a reciter

def getChapterOfReciter(id,lang=''):
    """ 
    List of all chapter audio files of a reciter.

    id number required
    - The Id of the reciter

    language string
    - Default value: en

    """
    url = f"https://api.quran.com/api/v4/chapter_recitations/{id}?language={lang}"



# Recitations

def recitations(lang=''):
    """ 
    Get list of available Recitations.

    language string
    - Default value: en
    - Name of reciters in specific language.
    - Will fallback to English if we don't have names in specific language.

    """
    url = f"https://api.quran.com/api/v4/resources/recitations?language={lang}"



# Get list of Audio files of single recitation

def getAudioforSingleRecitation(recitation_id,fields,chapter_number,juz_number,page_number,hizb_number,rub_el_hizb_number,verse_key):
    """ 
    List of all chapter audio files of a reciter.

    recitation_id number required
    - Recitation id

    fields string
    - comma seperated field of audio files.

    chapter_number integer
    - Possible values: >= 1 and <= 114
    - If you want to get audio file of a specific surah.

    juz_number integer
    - Possible values: >= 1 and <= 30
    - If you want to get audio file of a specific juz.

    page_number integer
    - Possible values: >= 1 and <= 604
    - If you want to get audio file of a Madani Muhsaf page

    hizb_number integer
    - Possible values: >= 1 and <= 60
    - If you want to get audio file of a specific hizb.

    rub_el_hizb_number integer
    - Possible values: >= 1 and <= 240
    - If you want to get audio file of a specific Rub el Hizb.

    verse_key string
    - If you want to get audio file of a specific ayah.

    """
    url = f"https://api.quran.com/api/v4/quran/recitations/{recitation_id}?fields={fields}&chapter_number={chapter_number}&juz_number={juz_number}&page_number={page_number}&hizb_number={hizb_number}&rub_el_hizb_number={rub_el_hizb_number}&verse_key={verse_key}"



# List of Chapter Reciters

def getChapterReciters(lang):
    """ 
    List of Chapter Reciters.

    language string
    - Default value: en
    - Name of reciters in specific language. Will fallback to English if we don't have names in specific language.

    """
    url = f"https://api.quran.com/api/v4/resources/chapter_reciters?language={lang}"



# Get Ayah recitations for specific Surah

def getAyahforSurah(recitation_id,chapter_number):
    """ 
    Get Ayah recitations for specific Surah.

    recitation_id number required
    - Recitation Id, you can get list of all ayah by ayah recitations.

    chapter_number number required
    - Possible values: >= 1 and <= 114

    """
    url = f"https://api.quran.com/api/v4/recitations/{recitation_id}/by_chapter/{chapter_number}"



# Get Ayah recitations for specific Juz

def getAyahforJuz(recitation_id,juz_number):
    """
    Get Ayah recitations for specific Juz

    recitation_id number required
    - Recitation Id, you can get list of all ayah by ayah recitations.

    juz_number number required
    - Possible values: >= 1 and <= 30

    """
    url = f"https://api.quran.com/api/v4/recitations/{recitation_id}/by_juz/{juz_number}"



# Get Ayah recitations for specific Madani Mushaf page

def getAyahforMadaniMushafPage(recitation_id,page_number):
    """
    Get Ayah recitations for specific Madani Mushaf page

    recitation_id number required
    - Recitation Id, you can get list of all ayah by ayah recitations.

    page_number number required
    - Possible values: >= 1 and <= 604

    """
    url = f"https://api.quran.com/api/v4/recitations/{recitation_id}/by_page/{page_number}"



# Get Ayah recitations for specific Rub el Hizb

def getAyahforRubElHizb(recitation_id,rub_el_hizb_number):
    """

    Get Ayah recitations for specific Rub el Hizb

    recitation_id number required
    - Recitation Id, you can get list of all ayah by ayah recitations.

    rub_el_hizb_number number required
    - Possible values: >= 1 and <= 240

    """
    url = f"https://api.quran.com/api/v4/recitations/{recitation_id}/by_rub/{rub_el_hizb_number}"



# Get Ayah recitations for specific Hizb

def getAyahforHizb(recitation_id,hizb_number):
    """

    Get Ayah recitations for specific Hizb

    recitation_id number required
    - Recitation Id, you can get list of all ayah by ayah recitations.

    hizb_number number required
    - Possible values: >= 1 and <= 60

    """
    url = f"https://api.quran.com/api/v4/recitations/{recitation_id}/by_hizb/{hizb_number}"



# Get Ayah recitations for specific Ayah

def getAyahRecitationforAyah(recitation_id,ayah_key):
    """
    Get Ayah recitations for specific Ayah

    recitation_id number required
    - Recitation Id, you can get list of all ayah by ayah recitations.

    ayah_key string required
    - Possible values: >= 1 and <= 60
    - Ayah key is combination of surah number and ayah number. e.g 1:1 will be first Ayah of first Surah

    """
    url = f"https://api.quran.com/api/v4/recitations/{recitation_id}/by_ayah/{ayah_key}"



##############################      Chapters     ################################


# List Chapters

def getChapters(lang):
    """

    List Chapters

    language string
    - Default value: en

    """

    url = f"https://api.quran.com/api/v4/chapters?language={lang}"



# Get Chapter

def getChapter(id , lang):
    """
    Get Chapter / Get details of a single

    id integer required
    - Possible values: >= 1 and <= 114
    - Chapter ID ( 1-114)

    language string
    - Default value: en

    """

    url = f"https://api.quran.com/api/v4/chapters/{id}?language={lang}"



# Get Chapter Info

def getChapterInfo(chapter_id , lang):
    """
    Get Chapter / Get details of a single

    chapter_id integer required
    - Possible values: >= 1 and <= 114
    - Chapter number ( 1-114 )

    language string
    - Default value: en

    """

    url = "https://api.quran.com/api/v4/chapters/{chapter_id}/info?language={lang}"



##############################       Verses       ################################

# By Chapter

def getVersesbyChapter(chapter_number,lang,words,translations,audio,tafsirs,word_fields,translation_fields,fields,page,per_page):
    """
        Get list of verses by Chapter / Surah number.

        chapter_number integer required
        - Possible values: >= 1 and <= 114
        - Chapter number ( 1 - 114 )

        
        language string
        - Default value: en
        - Language to fetch word translation in specific language.

        words string
        - Possible values: [true, false]
        - Default value: true
        - Include words of each ayah?
        - 0 or false will not include words.
        - 1 or true will include the words.

        translations string
        - comma separated ids of translations to load for each ayah.

        audio integer
        - Id of recitation if you want to load audio of each ayah.

        tafsirs string
        - Comma separated ids of tafisrs to load for each ayah if you want to load tafisrs.

        word_fields string
        - Comma separated list of word fields if you want to add more fields for each word.

        translation_fields string
        - Comma separated list of translation fields if you want to add more fields for each translation.

        fields string
        - comma separated list of ayah fields.

        page integer
        - Default value: 1
        - For paginating within the result

        per_page integer
        - Possible values: >= 1 and <= 50
        - Default value: 10
        - records per api call, you can get maximum 50 records.

    """

    url = f"https://api.quran.com/api/v4/verses/by_chapter/{chapter_number}?language={lang}&words={words}&translations={translations}&audio={audio}&tafsirs={tafsirs}&word_fields={word_fields}&translation_fields={translation_fields}&fields={fields}&page={page}&per_page={per_page}"



# By Page



# By Juz



# By Hizb number



# By Rub el Hizb number



# By Specific Verse By Key



# Get random ayah




##############################         Juz        ################################

# Get All Juzs




##############################        Quran       ################################

# Get Indopak Script of ayah

def getIndopakoOfAyah(chapter_number='',juz_number='',page_number='',hizb_number='',rub_el_hizb_number='',verse_key=''):
    """

    Get Indopak script of ayah. Use query strings to filter results, leave all query string blank if you want to fetch Indopak script of whole Quran.

    chapter_number integer
    - Possible values: >= 1 and <= 114
    - If you want to get indopak script of a specific surah.

    juz_number integer
    - Possible values: >= 1 and <= 30
    - If you want to get indopak script of a specific juz.

    page_number integer
    - Possible values: >= 1 and <= 604
    - If you want to get indopak script of a Madani Muhsaf page

    hizb_number integer
    - Possible values: >= 1 and <= 60
    - If you want to get indopak script of a specific hizb.

    rub_el_hizb_number integer
    - Possible values: >= 1 and <= 240
    - If you want to get indopak script of a specific Rub el Hizb.

    verse_key string
    - If you want to get indopak script of a specific ayah.

    """

    url = f"https://api.quran.com/api/v4/quran/verses/indopak?chapter_number={chapter_number}&juz_number={juz_number}&page_number={page_number}&hizb_number={hizb_number}&rub_el_hizb_number={rub_el_hizb_number}&verse_key={verse_key}"

    return url


# Get Uthmani Tajweed Script of ayah



# Get Uthmani Script of ayah



# Get Uthmani simple script of ayah



# Get Imlaei Simple text of ayah



# Get a single translation



# Get a single tafsir



# Get V1 Glyph codes of ayah



# Get V2 Glyph codes of ayah




##############################      Resources     ################################

# Recitation Info



# Translation Info



# Translations



# Tafsirs



# Tafsir Info



# Recitation Styles



# Languages



# Chapter Infos



# Verse Media




##############################    Search Query    ################################

url = "https://api.quran.com/api/v4/search?q={}"

##################################################################################
def sendRequest(url):
    payload={}
    headers = {
    'Accept': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    
    return json.loads(response.text)



def getAyahForPage(page_number):
    url = getIndopakoOfAyah(page_number=page_number)
    respond = sendRequest(url)
    listofAyah = []
    for i in range(len(respond["verses"])):
        #print(respond["verses"][i]["text_indopak"]+"\uFD3E"+str(i+1)+"\uFD3F")
        ayah = respond["verses"][i]["text_indopak"]+"\uFD3F"+str(i+1)+"\uFD3E"
        listofAyah.append(ayah)
    return listofAyah

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = [getIndopakoOfAyah(page_number=i) for i in range(1,604+1)]
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)
        print(responses)

asyncio.run(main())