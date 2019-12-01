# PSM
<p align="center">
   <em>AcikHack ❤️ Hackathon 30.11.2019</em>
</p>
<p align="center">
    <img src="https://raw.githubusercontent.com/voiceminingpsm/PSM/master/img/logo.png"  alt="Observer">
</p>

# Ekibimiz

~Ahmet Zahid ARICAN

~Mehmet AYDIN

# Kurulum
PyCharm gerekliliği vardır.Diğer ideler pyaudio kütüphanesinde sorunlar yaşatmaktadır.
Python 3.6 alt yapısına sahiptir.
Nltk kütüphanesini dahil etmeyi unutmayınız.
git clone https://github.com/voiceminingpsm/PSM.git ile kolayca kurulumunu yapabilirsiniz.
VoiceMiningPSM.py main classdır.

# Dahil edilen kütüphaneler

```
import re
import nltk
import pandas as pd
import numpy as np
from TurkishStemmer import TurkishStemmer
import speech_recognition as sr

```

# Proje Amacı
<p align="center">
    <img src="https://raw.githubusercontent.com/voiceminingpsm/PSM/master/img/psm_algoritma.png"  alt="Observer">
</p>

Projemizin amacı son dönemlerde yaşanan Aile içi şiddetten önce oluşan tartışma küfür hakaret tehdit gibi olguları algılayarak şiddetin önüne geçmeyi amaçlamaktadır.

# Nasıl Çalışır

Demo sürüm şuanlık ide üzerinden çalışmaktadır.İlerdeki amaclarımız gömülü sistem yada telefon üzerinden aktif bir şekilde ses algılayıp.
Kullanılan algoritma ve kod yapısı geliştirilip arka tarafta analiz ve AI kullanılarak daha optimize bir proje geliştirmeyi planlıyoruz.
Çalışma mantığı dışardan alınan sesi metine çevir.Daha sonrasında o metni Stringler şeklinde saklar ve  kelimenin anlamını ortaya koymak için.
Kelime analizi yapılır.Amaca uygun sınıfa aktarılır.
# Referanslar

>https://github.com/stopwords-iso/stopwords-tr

>https://github.com/otuncelli/turkish-stemmer-python

>https://soundcloud.com/user-565970875/sets/tts-turkish

>https://realpython.com/python-speech-recognition/#using-record-to-capture-data-from-a-file

>https://www.linkedin.com/pulse/pythonda-sesli-asistan-oluşturmak-yunus-emre-gündoğmuş/


