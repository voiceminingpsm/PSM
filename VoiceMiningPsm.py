import re
import nltk
import pandas as pd
import numpy as np
from TurkishStemmer import TurkishStemmer
stemmer = TurkishStemmer()
pd.options.display.max_colwidth = 8000 #Kelime Uzunluk Kapasitesi
f = open("trwords.txt", "r") 
trstop = f.read().split() #stopwords-tr kullanildi.

# TR: Örnek Türkçe dokümanlar 
'''
docs = ['Açıklama projenin ortaklarından Rus enerji devi Gazprom dan geldi. Yıllık 63 milyar metreküp enerji',
        'ilk günündeki 20 yarış heyecanlıydı, 109 puan toplayan Türkiye, 12 ülke arasında 9. oldu ve yarış tamamlandı',
        'Cortananın yeni işletim sistemi Windows 10 un önemli bir parçası olduğunu belirten Microsoft ; Google Android ve iOS cihazlarındaki Dijital',
        'Teknoloji devi Google, Android in MMM sürümüyle birlikte bir çok sistemsel hatasının düzeltileceğini',
        'Siroz hastalığı ile ilgili detaylara dikkat çekerek, sağlıklı bir karaciğere sahip olmak hastalık için',
        'Hastalık çoğu kez yıllarca doğru tanı konmaması veya ciddiye alınmaması sebebi ile kısırlaştırıcı etki yapabiliyor, kronik ağrı,',
        'ilk 4 etaptan galibiyetle ayrılan 18 yaşındaki Razgatlıoğlu, Almanya daki yarışta 3. sırayı alarak ',
        'Helal gıda pazarı sanki 860 milyar doların üzerinde'    
]
'''

import speech_recognition as sr
r = sr.Recognizer()
data = ""
docs = []
try:
        with sr.Microphone() as source:
        print("Sizi dinliyorum :)")
        audio = r.listen(source)
        data = r.recognize_google(audio, language='tr-tr')
        #data = 'selam merhaba açıkla alçak' #traning veri
        
        print("Bunu söyledin :" + data)
        docs += [data]
except sr.UnknownValueError:
        print("Ne dediğinizi anlayamadım")



WPT = nltk.WordPunctTokenizer()

def norm_doc(single_doc): #Metni normaline etmek için fonksiyon.
    # TR: Dokümandan belirlenen özel karakterleri ve sayıları at
    single_doc = re.sub(" \d+", " ", single_doc)
    pattern = r"[{}]".format(",.;") 
    single_doc = re.sub(pattern, "", single_doc) 
    # TR: Dokümanı küçük harflere çevir
    single_doc = single_doc.lower()
    single_doc = single_doc.strip()
    # TR: Dokümanı token'larına ayır
    tokens = WPT.tokenize(single_doc)
    # TR: Stop-word listesindeki kelimeler hariç al
    filtered_tokens = [token for token in tokens if token not in trstop]
    # TR: Dokümanı tekrar oluştur
    single_doc = ' '.join(filtered_tokens)
    return single_doc


docs = np.array(docs) #Docs arraya dönüştürüyoruz.
df_docs = pd.DataFrame({'Dokuman': docs}) #DataFrame ile başlık belirtiyoruz.
df_docs = df_docs[['Dokuman']] #Sutunun ismine eşitliyoruz.


norm_docs = np.vectorize(norm_doc) #Vectorize işlemi
normalized_documents = norm_docs(docs) #Normalized


kelimelist = list() #Verilen docs kelime şeklinde tutulacağı yer.
kelimelist2 = list() #Docs stemmer işlemi sonrası tutulacağı yer.

# TR: Dokümanların sınıfları
for doc_index in range(len(normalized_documents)): #Verilen docs dosyasını kelimeye ayırma işlemi.
   doc=normalized_documents[doc_index]
   tokens=doc.split()
   kelimelist += tokens
   for token_index in range(len(tokens)):
       tokens[token_index]
      
for eleman in kelimelist: 
    kelimelist2.append(stemmer.stem(eleman)) #Stemmer işlemi turkish-stemmer kullanildi.
    
düzenlenen = pd.DataFrame({'Kelimeler': kelimelist2})  #Stemmer işlem sonrası düzenlenen değişkenine atama işlemi.


siddet_kelimeleri_iceren_ornek_dokuman=["ölmek istemiyorum","lütfen vurma","keserim","açık","asmak","boğmak","katletmek"]
argo_kelimeleri_iceren_dokuman=["göt","lanet","sikiyim","dalyarak","beyinsiz","orospu","alçak"]

for siddet in düzenlenen['Kelimeler']:
    if siddet in siddet_kelimeleri_iceren_ornek_dokuman:
        print(siddet)
        
for argo in düzenlenen['Kelimeler']:
    if argo in argo_kelimeleri_iceren_dokuman:
        print(argo)        