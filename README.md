# Insinöörityö
Opinnäytetyöni päiväkirja ja materiaali

Aihe: Kielimallien kuten GPT-3 hyödyntäminen nollakäyttöliittymäsovelluksessa (lopullinen sovellus auki)

## 21.3 ensimmäinen palaveri

Huomioita:
- Nyt tarkoitus pohtia ja kokeilla erilaisia sovelluksia kielimallien hyödyntämiselle
- Esimerkki: Käyttäjä pyytää puhumalla sovellusta lisäämään kalenteriin merkinnän ja kielimalli kasaa sopivan tapahtuman lisättäväksi
- Blogeja voi käyttää lähteinä, esim medium.com
- Mermaidilla voi piirtää kaavioita
- Jupyter Notebook mahdollinen apuväline (tai google colab)

Linkkejä: 
- OpenAI API docs https://platform.openai.com/overview
- Ilmainen proxy API https://github.com/ayaka14732/ChatGPTAPIFree 
    - voi käyttää välimallina ilmaisen ChatGPT:n ja rajallisesti ilmaisen API:n välillä
- OpenAI API quick guide https://holypython.com/python-api-tutorial/openai-gpt-4-api-quick-guide/
- ChatGPT API guide in Node.js https://www.codingthesmartway.com/how-to-use-openai-chatgpt-api-in-nodejs/
- GPT-3 with python, how to use https://www.makeuseof.com/python-gpt-3-how-use/
- API guide and what you can do with it https://www.makeuseof.com/openai-api-guide-what-can-you-do/
- Mermaid https://mermaid.js.org/config/Tutorials.html


## 23.3: 

Mietteitä:
- Pitäisikö kirjoittaa yleiskäyttöisyyden näkökulmastä riippuen siitä kuinka paljon erilaisia sovelluksia saa toimimaan?
- Minkälaisella prosessilla saadaan ohjattua chatbotti toimimaan vain tietyssä kontekstissa?
- API-kutsut maksavat, joten miten saa turvattua väärinkäytöltä ja turhilta kutsuilta?

- Oikeastaan nettikaupan ostosten suosittelija / asiakaspalvelija kuulostaa hyvältä aiheelta
- Voikohan sille antaa testidataa vaikka json-muodossa, esim: eri tuotteita ja niiden ominaisuudet + asiakkaan entiset ostokset? ChatGPT mielestä onnistuu
- ChatGPT saa vain 3000 tokenia, GPT-4 25000
    - Suurta tietokantaa ei voi syöttää suoraan, vaan on selvitettävä mitä osaa tarvitaan
    - Testeissä voi käyttää kokonaisia datasettejä, sillä joillakin kaupoilla voi tosiaan olla vain muutama tuotetta

- Aihe niin uusi mutta tuntuu silti vanhenevan käsiin, koska uusia hienoja sovelluksia julkaistaan ja löytyy koko ajan. Elämä on kovaa aallonharjalla
- Varmaan hyvä ominaisuus mutta onko pakko olla puheohjausta?

- Toinen linkki vaikuttaa tosi hyödylliseltä, sitä kautta löytyi myös LlamaIndex-kirjasto, joka mahdollisesti tekee paljon puolestani
    - Ehdottomasti seuraava tutkimuskohde

Linkkejä:
- Käyttökohteita https://medium.com/swlh/i-used-chatgpt-every-day-for-3-months-heres-what-i-ve-learned-b4e8b1d910b4
- Pikaohjeet document Q&A chatbotin tekoon https://bootcamp.uxdesign.cc/a-step-by-step-guide-to-building-a-chatbot-based-on-your-own-documents-with-gpt-2d550534eea5
- LlamaIndex ja pidemmät ohjeet https://gpt-index.readthedocs.io/en/latest/guides/building_a_chatbot.html


## 24.3:

Mietteitä:
- GPT-4 ja pluginit esim nettiselaukseen ovat odotuslistojen takana. Molemmista saisi hyvää vertailua työhön

- LlamaIndexillä on dataloadereita joilla saa ladattua todella erilaisista kohteista dataa
    - Google drive, audio, elasticsearch, nettisivut, json yms
- Toimii API:n kautta ja haluaisin hyödyntää ChatGPT API Free:tä mutta näiden yhteensopivuutta pitää tutkia seuraavaksi ettei tarvitse alkaa räpeltää lisätilien kanssa
    - ChatGPT API Free toimii täysin proxynä eli sille voi lähettää tiedot samaan tapaan kuin normaalillekin, mutta pitää selvittää voiko LlamaIndexissa vaihtaa kohteen johon nämä tiedot lähetetään
    - Pitääkö kirjoittaa wrapperi LangChainin OpenAI-luokalle tai tehdä muunneltu kopio?
    - Kustomoidun LLM:än luominen on mahdollista eli tutkin nyt onko OpenAI-luokassa määritelty mihin se ottaa yhteyttä
- Tapaa muuttaa yhteyttä ei löytynyt joten seuraavat askeleet ovat joko kirjaston testaaminen omilla API-avaimilla tai sitten selvitän voiko pelkkää luotua indexiä käyttää hyödyksi jolloin loisin yhteyden itse suoraan proxy API:in


Linkkejä:
- Lista dataloadereista https://llamahub.ai/
- JSON loader https://llamahub.ai/l/file-json
- Custom LLM https://gpt-index.readthedocs.io/en/latest/how_to/custom_llms.html#example-using-a-custom-llm-model
- OpenAI.py LLM koodi https://github.com/hwchase17/langchain/blob/master/langchain/llms/openai.py
    - Tiedostosta näkyy että OpenAI-luokalla pystyy käyttämään davinci yms malleja ja OpenAIChat-luokalla GPT-malleja

## 26.3

Mietteitä:
- Taidan ensin tosiaan testata kirjastoa omilla avaimilla, sillä toisellakaan yrittämällä en löytänyt mistä muuttaa endpointia

Linkkejä:
- Use cases guide https://gpt-index.readthedocs.io/en/latest/guides/use_cases.html
- Guardrails ohjaa outputin muotoa https://github.com/ShreyaR/guardrails

## 27.3

Mietteitä:
- Ilmainen proxy api loppui rahoituksen puutteen takia ja huomasin että uusien tilien luomiseen tarvitaan puhelinnumero, joten en voi hyödyntää uusia tilejäkään API-avaimien hankkimiseen
    - ainoa vaihtoehto on edetä virallisen API:n kanssa hyvin pienillä datamäärillä ja katsoa paljonko menee tokeneita per kutsu

Linkkejä:
- Learn prompting https://learnprompting.org/docs/basics/intro
- GPT-4 chat ilmaiseksi testaamiseen https://huggingface.co/spaces/ysharma/ChatGPT4

## 28.3
Mietteitä:
- Toisia malleja voisi myös tutkia, coheren mallit vaikuttavat tutkimisen arvoiselta ja API on ilmeisesti ilmainen
- Teen nyt json-tiedoston johon lisään muutamia tuotteita, kuten vaikkapa puhelinmalleja
    - valmis ja myös hieman lyhennetty versio pelkillä teknisillä tiedoilla

Linkkejä:
- Cohere https://dashboard.cohere.ai/
- Open Source speech-to-text lista https://fosspost.org/open-source-speech-recognition/

## 31.3
Mietteitä:
- LLaMan ja siitä tuunatun Alpacan toimintaa voisi testata GPT-3 jälkeen
- Käyty läpi opettajan linkkaamaa esimerkkiä

Linkkejä:
- Opettajan linkki, puheohjaus ja chatbot guide https://levelup.gitconnected.com/i-created-a-voice-chatbot-powered-by-chatgpt-api-here-is-how-6302d555b949
- LLaMa/Alpaca erojen testausta https://www.reddit.com/r/LocalLLaMA/comments/123ktm7/comparing_llama_and_alpaca_models/

## 1.4
Mietteitä:
- En saa opettajan esimerkkiä toimimaan, luultavasti versio-ongelma konsolin perusteella
    - Pistin kommentin kirjoittajalle jos asia sitten selviäisi
- Löysin artikkelin jonka ohjeet luultavasti toimivat mutta ilman nettisivua
    - Tärkeää on Microphone speech into text -osio
- Seuraavaksi tutkin saanko esimerkin toimimaan ja olisiko jokin hyvä tapa saada sille simppeli nettisivu vai voisiko tämän integroida toiseen esimerkkiin ja leikata sen JS osa pois

- Kokeilin taas esimerkkiä ja testasin olisiko tekijä tehnyt virheen aikaisemmassa osassa artikkelia
    - Tosiaan artikkelin keskellä oleva esimerkki ei toiminut ollenkaan, mutta kun otin artikkelin lopun koodista tarvitsemani pätkän sain koodin toimimaan
    - Eli nyt kun painaa nappia ja puhuu, tulostuu tekstiä hetkeksi näytölle
- Seuraava askel on siis lähteä testailemaan datan lähetystä jollakin mallilla

Linkkejä:
- Italia kielsi ChatGPT:n nojaten yksityisyyden suojaan https://www.iltalehti.fi/ulkomaat/a/dffe5381-9606-42fe-b680-1917baa3e785
- Pythonissa puhe tekstiksi https://towardsdatascience.com/easy-speech-to-text-with-python-3df0d973b426

## 11.4
Mietteitä:
- Lisään koodin joka toimi ja huomenna jatkan tämän tekemistä nyt kun sain tehtyä FSO-kurssia 
- Raportissa voisi puhua kielimallien vaaroista ja etiikasta. Linkissä kerrotaan harrastelijan tekemästä kielimallia hyödyntävästä viruksesta.

Linkkejä:
- Mikko Hyppönen - ensimmäinen gpt virus löydetty https://www.helpnetsecurity.com/2023/04/03/machine-learning-malware/

## 12.4
Mietteitä:
- Lähden siis testaamaan itse datan lähetystä
    - Testitiedoston nimi vaikutti virallisen koodin toimivuuteen, muutetaan muuksi
    - Virallisen apin testausta tavallisesti
    ```
    Lähetetyt promptit:  

    {"role": "system", "content": "You are a webshop assistant."},
    {"role": "user", "content": "Hello"}

    Vastauksena palasi:
    Hello! How can I assist you with your webshop needs today?

    Tokenien käyttö
    "completion_tokens": 14,
    "prompt_tokens": 21,
    "total_tokens": 35

    OpenAI:n mukaan rahaa kului ilmaisesta summasta 0,00007$/5$
    ```
- Backend toteutus pythonilla (llamaindex, fastapi) ja frontend javascriptillä(react)?
- Seuraavaksi kokeilen testidatalla käyttöä ja LlamaIndexiä

Linkkejä:
- Natural text to speech AI https://beta.elevenlabs.io/
- Raporttiin: Tekoälyt voivat korvata neljänneksen töistä https://www.hs.fi/talous/art-2000009485920.html

## 13.4
Mietteitä:
- Kokeilen LlamaIndexiä ensimmäistä kertaa
    - Mietin että haluaisin kokeilla sitä alpaca-mallin kanssa lokaalisti, mutta toteutus ei vaikuta helpolta
    - Löysin langchainin integraatiot, joilla asia voisi onnistua. Kokeilen alpacan asennusta ja käyttöä ensin
- Iltaan tuli pari muuttujaa, jatkan myöhemmin ja tutkin GPT4Allin sekä Alpacan potentiaalit ja miten yhdistetään Langchainiin ja siten LlamaIndexiin

Linkkejä:
- löysin jälkeenpäin ohjeita https://medium.com/artificialis/crafting-an-engaging-chatbot-harnessing-the-power-of-alpaca-and-langchain-66a51cc9d6de
- ChatGPT ja open source vaihtoehdot - lyhyt historia https://betterprogramming.pub/navigating-the-world-of-chatgpt-and-its-open-source-adversaries-21f0a6b7da94
- Lista edellä mainituista https://medium.com/geekculture/list-of-open-sourced-fine-tuned-large-language-models-llm-8d95a2e0dc76
- Llama (myös alpaca) asennus https://www.reddit.com/r/LocalLLaMA/comments/11o6o3f/how_to_install_llama_8bit_and_4bit/
- GPT4All repo https://github.com/nomic-ai/gpt4all
- Llama.cpp repo https://github.com/ggerganov/llama.cpp
- GPT4All integraatio langchainiin (löytyy myös llama) https://python.langchain.com/en/latest/modules/models/llms/integrations/gpt4all.html

## 16.4
Mietteitä:
- Lataan GPT4All-mallia, joka on 4GB tiedosto ja jolle löytyy myös python käyttöliittymä
    - Testasin tätä mallia ja nopeus on tyydyttävä omalla vanhalla työpöytäkoneella. Vastauksissa malli vain ilmoitti olevansa Jane Doe ja myöhemmin vasta sanoi olevansa kielimalli
    - Hiottavaa siis on ja on järkevää valita käyttöön malli jolla on hyvä nopeus sekä hyvät vastaukset
    - Kokeilin pythonilla toimivaa versiota joka oli hankala saada käyntiin ja se on tuskallisen hidas, n. 1-2 merkkiä minuutissa
- Hiottavaa löytyy myös omasta työskentelystä sillä lataamisen ja testaamisen välillä meni muutama tunti johtuen siitä että tutkiessa eri malleja ajauduin hyvin sivuraiteille
- Seuraavaksi voisin testata toista mallia jos olisi helpompaa tai selvittää nopeasti vielä onko tässä mallissa enää mahdollisuuksia

Linkkejä:
- Toinen mallien vertailu, gpt4xalpaca on paras https://www.reddit.com/r/LocalLLaMA/comments/12ezcly/comparing_models_gpt4xalpaca_vicuna_and_oasst/