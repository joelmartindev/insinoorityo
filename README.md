# Insinöörityö: Opinnäytetyöni julkinen päiväkirja ja sovellus

Aihe suurinpiirtein: Lokaalit kielimallit ja RAG: PDF-chatbotin luonti (Aikaisemmin Lokaalin kielimallin hyödyntäminen nollakäyttöliittymäsovelluksessa)

Ideana on luoda tekoälysovellus, jonka kanssa voi keskustella tekstiä sisältävän tiedoston sisällöstä. Hahmottelen sellaista sovellusta, jonka yritys voisi ottaa sisäiseen käyttöönsä, ettei sensitiivistä dataa tarvitsisi lähettää ulkopuolisille. Keväällä 2023 luodut osat päiväkirjasta eivät täysin pohdi vielä tätä. Keskityin sen jälkeen toiseen projektiin ja töihin, mutta keväällä 2025 pääsin toteutuksessa maaliin, kun kokeilin uusia työkaluja.

Kansiosta nimeltä Metropolia löytyy koulun tekoälyprojektiin hakua varten tehty pieni projekti.

Projektin saa käyntiin rakentamalla Vitella front-kansiossa staattisen sivun komennolla `npm install` ja `npm run build`.

Sitten projektin juuressa ajetaan komento `pip install -r requirements.txt` ja `fastapi dev main.py`, jolloin serveri käynnistyy ja selamisessa voi navigoida sen osoittamalle sivulle `localhost:8000`.

## 21.3.2023 ensimmäinen palaveri

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

## 23.3.:

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

## 24.3.:

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

## 26.3.

Mietteitä:

- Taidan ensin tosiaan testata kirjastoa omilla avaimilla, sillä toisellakaan yrittämällä en löytänyt mistä muuttaa endpointia

Linkkejä:

- Use cases guide https://gpt-index.readthedocs.io/en/latest/guides/use_cases.html
- Guardrails ohjaa outputin muotoa https://github.com/ShreyaR/guardrails

## 27.3.

Mietteitä:

- Ilmainen proxy api loppui rahoituksen puutteen takia ja huomasin että uusien tilien luomiseen tarvitaan puhelinnumero, joten en voi hyödyntää uusia tilejäkään API-avaimien hankkimiseen
  - ainoa vaihtoehto on edetä virallisen API:n kanssa hyvin pienillä datamäärillä ja katsoa paljonko menee tokeneita per kutsu

Linkkejä:

- Learn prompting https://learnprompting.org/docs/basics/intro
- GPT-4 chat ilmaiseksi testaamiseen https://huggingface.co/spaces/ysharma/ChatGPT4

## 28.3.

Mietteitä:

- Toisia malleja voisi myös tutkia, coheren mallit vaikuttavat tutkimisen arvoiselta ja API on ilmeisesti ilmainen
- Teen nyt json-tiedoston johon lisään muutamia tuotteita, kuten vaikkapa puhelinmalleja
  - valmis ja myös hieman lyhennetty versio pelkillä teknisillä tiedoilla

Linkkejä:

- Cohere https://dashboard.cohere.ai/
- Open Source speech-to-text lista https://fosspost.org/open-source-speech-recognition/

## 31.3.

Mietteitä:

- LLaMan ja siitä tuunatun Alpacan toimintaa voisi testata GPT-3 jälkeen
- Käyty läpi opettajan linkkaamaa esimerkkiä

Linkkejä:

- Opettajan linkki, puheohjaus ja chatbot guide https://levelup.gitconnected.com/i-created-a-voice-chatbot-powered-by-chatgpt-api-here-is-how-6302d555b949
- LLaMa/Alpaca erojen testausta https://www.reddit.com/r/LocalLLaMA/comments/123ktm7/comparing_llama_and_alpaca_models/

## 1.4.

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

## 11.4.

Mietteitä:

- Lisään koodin joka toimi ja huomenna jatkan tämän tekemistä nyt kun sain tehtyä FSO-kurssia
- Raportissa voisi puhua kielimallien vaaroista ja etiikasta. Linkissä kerrotaan harrastelijan tekemästä kielimallia hyödyntävästä viruksesta.

Linkkejä:

- Mikko Hyppönen - ensimmäinen gpt virus löydetty https://www.helpnetsecurity.com/2023/04/03/machine-learning-malware/

## 12.4.

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

## 13.4.

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

## 16.4.

Mietteitä:

- Lataan GPT4All-mallia, joka on 4GB tiedosto ja jolle löytyy myös python käyttöliittymä
  - Testasin tätä mallia ja nopeus on tyydyttävä omalla vanhalla työpöytäkoneella. Vastauksissa malli vain ilmoitti olevansa Jane Doe ja myöhemmin vasta sanoi olevansa kielimalli
  - Hiottavaa siis on ja on järkevää valita käyttöön malli jolla on hyvä nopeus sekä hyvät vastaukset
  - Kokeilin pythonilla toimivaa versiota joka oli hankala saada käyntiin ja se on tuskallisen hidas, n. 1-2 merkkiä minuutissa
- Hiottavaa löytyy myös omasta työskentelystä sillä lataamisen ja testaamisen välillä meni muutama tunti johtuen siitä että tutkiessa eri malleja ajauduin hyvin sivuraiteille
- Seuraavaksi voisin testata toista mallia jos olisi helpompaa tai selvittää nopeasti vielä onko tässä mallissa enää mahdollisuuksia

Linkkejä:

- Toinen mallien vertailu, gpt4xalpaca on paras https://www.reddit.com/r/LocalLLaMA/comments/12ezcly/comparing_models_gpt4xalpaca_vicuna_and_oasst/

## 17.4.

Mietteitä:

- Tutkin vielä GPT4All-mallia
  - Mallin tekijöiden gpt4all python client viritelmä ymmärtääkseni ei toimi vielä Windowsilla joten käytin jo pyllamacpp:tä
  - Pyllamacpp:n ohjeet sanoivat että voi olla kannattavaa buildata omalla koneella jotta target cpu on myös oma
  - Tein tuon ja ei auttanut ollenkaan, mutta sen sijaan käytettävien ydinten muutos kahdeksasta yhteen sai tekstistä melkein reaaliaikaisen ja muutos neljään sai tekstiä tulemaan nopeammin kuin itse ehdin puhua
  - Yritän saada sen toimimaan chat muodossa, sillä nyt se vain päättelee tekstin jatkoa
- Haluaisin seuraavaksi kokeilla yhdistää tämän LlamaIndexiin ja katsoa mitä tapahtuu ja helpottaisiko se chat-muotoon saattamista

Linkkejä:

- 'Using LlamaIndex as a generic callable tool with a Langchain agent, Using LlamaIndex as a memory module'
  https://gpt-index.readthedocs.io/en/latest/how_to/integrations/using_with_langchain.html

## 18.4.

Mietteitä:

- Jatkan LlamaIndexin yhdistämisellä
  - Sain LlamaIndexin ottamaan sisään haluamani lyhyen tekstikontekstin ja kysymyksen, sekä mallin vastaamaan Langchainin GPT4All-integraatiota hyödyntämällä mistä tekstikontekstissa oli oikein kyse
  - Prosessi kesti nykykoodilla yli 100 sekuntia, mutta luulen että suuri osa siitä johtuu kontekstin indeksin rakennuksesta, jonka voi myös hoitaa kerralla ja ladata ohjelmaan jälkeenpäin
  - Kokeilin nyt kokoamieni jsonien käyttöä, mutta ilmeisesti ne ovat liian pitkiä esim GPTKeywordTableIndexille senkin jälkeen kun ohjelma lyhentää ne. Jos käyttäisin VectorIndexiä saattaisin saada ne vielä pienemmiksi, mutta oletuksena LlamaIndex tarvitsee siihen OpenAI:n embedding APIa. Löytyy tuki custom embedding modeleille, mutta en ole varma onko mitään vaihtoehtoa
  - Ilmeisesti custom local vaihtoehtoja on, lisään linkin
- Seuraavaksi tutkin embedding malleja ja jos homma ei etene, pitää vaihtaa sovelluksen aihetta paljon kevyemmäksi

Palaveriin:

- Olen saanut kokeiltua tähän asti GPT-3.5-Turbo-mallia, mutta ajattelin että tässä menisi liikaa krediittejä pitkillä prompteilla, joten aloin tutkimaan omalla koneella pyöriviä kielimalleja
  - Llama-pohjainen GPT4All pyörii melko hyvin omalla koneella, mutta ongelmana on kontekstikoko
- Tämä ensimmäinen idea kaupan tuotteista kertovasta chatbotista on uhassa kariutua kontekstikoon takia, mutta voin vielä testata custom embeddausta joka voisi lyhentää sitä
  - Vaikuttaa epätodennäköiseltä että auttaa mutta ei pitäisi mennä kauaa kokeilussa
- Haluaisin siis välttää OpenAI:n APIen käyttöä, sillä luulen että firmat haluaisivat jonkin oman ratkaisun mieluummin ja siksi lokaali kielimalli houkuttelee

Linkkejä:

- Embedding malleista https://medium.com/@nils_reimers/openai-gpt-3-text-embeddings-really-a-new-state-of-the-art-in-dense-text-embeddings-6571fe3ec9d9
- sbert https://www.sbert.net/examples/applications/computing-embeddings/README.html

## 19.4. Toinen palaveri

Huomioita:

- OMAsta libguides, kannattaa tutustua ACM, IEEE Explore ja ScienceDirect. Kannattaa tutkailla uusimmasta päästä
  - Kiinnostaako otsikko? Lue tiivistelmä. Kiinnostaako tiivistelmä? Ala lukea
  - ScienceDirectissa cite-napilla export citation, abstract pois, sulkuihin perään milloin luettu
- IMRAD-kirjoitusmenetelmä
- Täksi illaksi kasaan suunnitelman, jossa hahmotelma sisällysluettelosta ja tutkimuskysymys alakysymyksineen

Linkkejä:

- Ideoita ecommerce käyttöön https://gptblogs.com/maximizing-ecommerce-success-with-chat-gpt
- IMRAD https://en.wikipedia.org/wiki/IMRAD
- Tutkimusongelman ja kysymyksen selitystä https://www.mv.helsinki.fi/home/jmykkane/tutkielma/Tutkimusongelma.html

## 24.4. Tauon paikka

Mietteitä:

- Pidän taukoa aktiivisemmasta tekemisestä, sillä käsitellyt asiat kehittyvät kovaa tahtia eli kannattaa hieman odottaa
- Pääsyynä myös se että alan tekemään Solita Dev Academyn hakutehtävää, jonka deadline on 31.5

Linkkejä:

- Jälleen uusi ei-llama-pohjainen malli ja vielä isommalla kontekstikoolla https://stability.ai/blog/stability-ai-launches-the-first-of-its-stablelm-suite-of-language-models

## 25.8 Homma jatkuu

Mietteitä:

- Ideana nyt jatkaa projektia tekemällä ohjelma, jolla voi keskustella siihen ladatun dokumentin sisällöstä
  - Kaipaan portfolioon uutta Java-projektia, joten ainakin osa projektista tehdään Javalla jos mahdollista
  - Sovellus tarvitsee serverin kielimallille ja yhteyksille, sekä käyttöliittymän
    - Pitää miettiä haluanko tehdä käyttöliittymänkin Javalla
  - Alan tutkimaan onko Javalla mahdollista pyörittää kielimalleja
- Aion myös tutkia kuinka hyvin kielimallit pyörivät läppärilläni, koska sitten en olisi jumissa isolla koneella
  - Tätä voi myös miettiä käyttäjien kautta, jos sovellus pyörisikin kokonaan käyttäjän koneella eikä tarvitsisi erillistä serveriä
- LlaMasta tuli uusi versio LlaMA 2, jonka lisenssi mahdollistaa kaupallisen käytön

Linkkejä:

- Llama.cpp web server https://github.com/ggerganov/llama.cpp/tree/master/examples/server
- LlaMa Java Wrapper https://github.com/sebicom/llamacpp4j
- Langchain Javalla https://github.com/HamaWhiteGG/langchain-java

## 4.9

Mietteitä:

- Kokeilen vanhan kielimallin ajamista läppärillä, mutta ohjelma ei toimi. Alla pyörivät työkalut taitavat olla uudistuneet rikkovilla muutoksilla.
  - Etsin tietoa siitä että mikä on paras uusi LlaMa 2 -malli jota voisin kokeilla tähän tarkoitukseen
  - Mallin pitäisi olla tekstin käsittelyyn sopiva ja Chat-tyylisenä (instruct?) se olisi luultavasti käyttäjäystävällisin
  - Vaihdoin aikaisemmin testaamani pyllamacpp --> llama-cpp-python, jolloin uusien gguf-mallien pitäisi toimia
  - Testaan seuraavaksi toimiiko llama-cpp-python kun asentaa Visual Studion ja sen C++ core -osuuden ja CMake-lisäominaisuuden
- On olemassa pelkästään Javalla tehty inference engine Jlama, mutta llama.cpp on paljon vakiintuneempi ja pidemmällä kehityksessä mikä mahdollistaa esimerkiksi pienempien mallien pyörittämisen
  - Lienee siis järkevää sen sijaan käyttää Javalla wrapattua llama.cpp:tä, joita löytyy useampi

Linkkejä:

- Ehkä kehitetyin Java wrapper https://github.com/kherud/java-llama.cpp

## 7.9

Mietteitä:

- Llama-cpp-python testauksen jatkoa
  - Pelkkä `pip install llama-cpp-python` aiheutti ongelmia, koska C compileria ei millään löytynyt asennuksesta huolimatta, joten jouduin asentamaan valmiin wheelin komennolla `pip install https://github.com/abetlen/llama-cpp-python/releases/download/v0.1.83/llama_cpp_python-0.1.83-cp39-cp39-win_amd64.whl`
  - Ohjelma lähti tällä kertaa käyntiin, mutta antaa esimerkkikysymykseen väärän vastauksen
  - Kysymystä muuttamalla malli ei oudosti anna minkäänlaista outputtia
  - Isommalla koneella testattuna 7B malli vastaa hyvin
- Quantized versio Llama 2 7B-mallista saattaa olla suurin malli, jota minulla on resursseja pyörittää ja toisella tietokoneella on sama juttu koska muistin määrä on sielläkin 16 gigaa
  - Testaan siis vielä 13B mallia jos se pyörisi
  - Ohjelma pyörii loppuun saakka, mutta en saa lopputuloksesta kokonaista vastausta
  - Ymmärtääkseni tulisi ilmoitus jos muisti loppuu kesken, joten luulen että 13B mahtuu, mutta en ymmärrä miksei toimi kunnolla
- Kokeilin vaihtaa promptin muotoa ja vastauksista alkoi tulla järkevämpiä
- Jatkan promptien miettimistä seuraavaksi

Linkkejä:

- Testattu 7B Llama 2 https://huggingface.co/TheBloke/Llama-2-7b-Chat-GGUF
- Testattu 13B LlaMa 2 https://huggingface.co/TheBloke/Llama-2-13B-chat-GGUF
- Prompt ohjeita https://replicate.com/blog/how-to-prompt-llama

## 11.9 Haku Metropolian projektiin

Mietteitä:

- Tänään tuli vastaan koulun ilmoitus, jossa opiskelijoita haetaan töihin projektiin, joka liippaa todella läheltä tätä työstämääni projektia

  - Päätän siis käyttää aikaa Metropolian projektiin hakemiseen tekemällä vaaditun koodaustehtävän
  - " The strategy and development services of Metropolia UAS is looking to hire two students who would join a Metropolia-wide AI development project. The goal of the project is to use LLMs (large language models) to empower our staff and students. The project is heavily R&D driven, and it will result in new discoveries and publications. Application deadline: 24.9. "
  - " You should submit a small coding assignment in which your task is to create a small app using Flask (https://flask.palletsprojects.com/en/2.3.x/quickstart/). The app should have a text field and a button. When the button is pressed, the text written in the text field will be sent to the backend, which will translate it from English to Finnish, for example, using this model: https://huggingface.co/Helsinki-NLP/opus-mt-en-fi . Click “Use in Transformers” to see how to load the model and refer to Pipeline documentation to use the model to translate text (https://huggingface.co/docs/transformers/main_classes/pipelines). NB. There is also a Pipeline for translation. "

- Hakemiseen vaaditussa projektissa pyydetään siis tekemään Flask-API, joka pyörittää Huggingfacen Transformers-kirjastolla käännösmallia. Frontendistä ei mainita mitään, joten taidan vain tehdä pikaisesti React-sivun
- Loin uuden Metropolia-kansion, johon lisään tehtävään liittyvää koodia
- Aloitan kokeilemalla mallin ajamista koneellani, mitä varten asennan Transformers-kirjaston
  - Sain mallin pyörimään ja tulostin käännöksiä parilla eri tavalla
- Transformers tuntuu kätevältä, mutta tässä projektissa sitä olisi hankala käyttää, jos haluaa tehdä Javalla ja Spring Bootilla backendin
- Huomenna jatkan luomalla APIn ja nettisivun

## 12.9 Metropolia-tehtävä loppuun

Mietteitä:

- Lähden luomaan API:a, joka vastaanottaa tekstiä ja palauttaa käännettyä tekstiä
  - Translate-route tehty ja suurin ongelma oli Pythonin syntaksin opettelu, että saisin JSON:in oikean muotoisena takaisin
  - Testaan Postmanilla API:in postausta ja homma toimii, mutta ääkköset eivät näy oikein. Ilmeisesti data lähtee Unicodena, jolloin se pitää tulkita takaisin oikeaan muotoon. Katsotaan onko tämä ongelma vai hoituuko se automaattisesti, kun nettisivu saa datan.
- Seuraavaksi tarvitsen nettisivun, jolta lähetän pyyntöjä
  - Teen Vitellä React-luurankoprojektin ja muokkaan sen omaan käyttöön
  - Sovellus ei ole, laaja joten luon koodin aikalailla vain App.jsx-tiedostoon
  - Alustava versio valmis: tekstialue, nappi ja sivulle ilmestyvä käännös
- Laajensin sovellusta vielä niin, että vanhat käännökset jäävät näkyviin ja tein pienet muotoilut
- Serveri pitäisi vielä saada lähettämään valmis nettisivu
  - Luon Vitellä koodista staattisen sivun
  - Saan Flaskin toimimaan sivun kanssa pienen kamppailun jälkeen, sillä se ei osannut lähettää js-tiedostoja oikean muotoisina. Piti siis erikseen korjata MIME-tyyppi js-tiedostoille sekä selaimen välimuisti piti tyhjentää ennen kuin korjaus alkoi vaikuttaa.
- Kaikki on nyt valmista ja voin hakea projektiin mukaan!

## 16.9.2023

Mietteitä:

- Kokeilen parannella vastauksia prompteilla
  - Eri mallit vastaavat paremmin prompteihin, joilla niitä on koulutettu
  - Lisäämällä lyhyen alun promptiin, malli antoi paljon paremman vastauksen eikä esimerkiksi vain lisännyt robottiemojia ja lopettanut
- Tässä vaiheessa tuntuu että olen niin jumissa toteutuksen kanssa ja keskityn niin kovaa työnhakuun että koko homma jäi aikanaan tähän

## Syksy 2024 eteenpäin -->

- Kesätöiden loputtua palasin aiheeseen ajoittain, mutta lähinnä sain vain tutkittua lisää ja kerättyä ideoita muistiinpanoihini
- Kielimallit ja niitä ympäröivät työkalut ja ohjeet ovat kuitenkin hurjasti kehittyneet tänä aikana, mikä lisää intoani jatkaa

## 3.2.2025 - 6.2.2025

- Päätän yrittää nyt siirtyä pois llama.cpp-pohjaisesta ratkaisusta, sillä se aiheutti minulle paljon ongelmia ja halusin testata voisiko toinen tapa olla helpompi
- Kokeilen käyttää Ollamaa kielimallin pyörittämiseen
  - Ollama luotiin kesällä 2023, kun olin jo lopettanut aktiivisen kehityksen, enkä kuullut siitä kuin vasta syksyllä 2024
- Noin kolmen päivän tutkimisen ja säätämisen jälkeen saan valmiiksi Proof of Concept -sovelluksen, joka ottaa ennaltamääritetyn PDF-tiedoston ja antaa käyttäjän kysyä siitä kysymyksen

## 7.2.2025 - 12.2.2025

- Hion sovellusta, refaktoroin, mahdollistan monen kysymyksen kysymisen, luon serverin FastAPIlla ja käyttöliittymän Reactilla sekä mahdollistan PDF-tiedoston vaihtamisen nettisivun kautta

## 13.2.2025

- Uuden ohjaajan kanssa pidetään palaveri, jossa demoan sovellusta ja saan hyväksynnän jatkaa samaa rataa ja aloittaa opinnäytetyön raporttiosuus!
