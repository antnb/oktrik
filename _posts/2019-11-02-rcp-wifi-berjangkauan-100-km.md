---
layout: post
title: " RCP WiFi Berjangkauan 100 Km "
date: '2019-11-02T11:52:00.001+07:00'
author: rosari J
tags:
- wireless
- internet
modification_time: '2022-07-10T11:55:27.632+07:00'
blogger_id: tag:blogger.com,1999:blog-7329298365997944344.post-1958771102853674716
blogger_orig_url: https://www.oktrik.com/2019/11/rcp-wifi-berjangkauan-100-km.html
---

*RCP (rural connectivity platform) diusulkan Intel demi mengatasi 
lambatnya akses internet di daerah rural. Kini sinyalnya bisa 
ditembakkan hingga jarak 100 km. Solusi yang murah dan efisien.*  

Wireless internet broadband telah menjadi kebutuhan penting. 

Untuk 
urusan yang satu ini beragam teknologi telah ditelurkan, seperti WiMax 
(802.16) dan LTE yang kini sedang banyak dibicarakan. WiMax dan LTE yang
 termasuk 4G terbilang jitu dalam membangun solusi wireless broadband.


Tapi jangan puas dulu, implementasi WiMax dan LTE nyatanya tak begitu 
mudah. WiMax misalnya, masih terganjal kebijakan dan regulasi 
pemerintah. Dalam hal bisnis, perangkat WiMax juga dipandang mahal dan 
terbatas.


Namun tak bisa dipungkiri, WiMax ideal dalam hal jangkauan akses. Hal 
ini yang kemudian menjadi dasar ide dari Intel untuk meningkatkan 
performa dari teknologi yang sudah populer. Ini tak lain WiFi (802.11) 
dengan jangkauan jarak jauh, tak tanggung-tanggung sinyal WiFi bisa 
ditembakkan ke jarak 100 Km (60 mil). Solusi Intel ini disebut RCP 
(rural connectivity platform), dirancang untuk memenuhi kebutuhan akses 
internet yang murah bagi negara berkembang.


Sebelumnya WiFi sudah dikenal mumpuni untuk mesh network di 
perkotaan,akses di dalam dan luar ruangan sudah dioperasikan luas oleh 
ISP (internet service provider). Lewat RCP, akses luar ruangan WiFi yang
 kini dikembangkan. Cara kerjanya tarbagi dua, yakni konfigurasi dasar 
dan yang diperluas (lihat box).


Perangkat yang diperlukan untuk RCP mencakup single board computer 
dengan embedded prosesor Intel IXP425, compact flash storage, 10/100 
ethernet port dan lokal WiFi untuk akses ke perangkat klien. Antena bisa
 memanfaatkan jenis yang sudah ada.


Keseluruhan perangkat beroperasi dengan pasokan tenaga di bawah 6 
watt. ”RCP memberi kemudahan akses internet di wilayah rural, biaya 
implementasi rendah, dan efesien dalam bandwidth bisa menjadi daya tarik
 tersendiri, apalagi perangkat WiFi sudah banyak dan cukup digemari,” 
ujar Jeff Galinovsky, senior platform manager Intel. 

RCP kini telah 
diuji coba di India, Vietnam, Panama dan Afrika Selatan. Di Panama RCP 
berhasil menghubungkan akses internet 15 hotel di rural area. Di 
Berkeley Research Lab – California, RCP bisa menyalurkan video streaming
 dengan frekuensi 5,8Ghz pada jarak 1,5 mil. [Dalam release disebutkan RCP](https://www.technologyreview.com/2008/03/18/97524/long-distance-wi-fi/) bisa dikebut untuk akses hingga 6,5 Mbps


#### Standar RCP Dan Konfigurasi Dasar


Inilah jawaban mengapa **WiFi** bisa menjangkau hingga 100 Km. 
Antar dua node WiFi disambungkan tambahan teknologi TDMA (time division 
multiple access) yang juga diterapkan pada GSM. TDMA membagi channel ke 
dalam beberapa slot, lalu mensinkronkan antara sending dan receive 
radio. Hasilnya, setiap radio bisa di sending dan receive dalam skedul, 
tak perlu ada waktu menunggu untuk pemberitahuan dan tak diperlukan lagi
 resending data.

[![Wifi RCP diagram](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjOytlNHL_qXciB74M1E7XqX75xuGM4fUHbevZw0V2qtoGAdeZFO-1Z8yKlCbqaClZcRk6_cKo-2oUeTkyg-zibWkJmUSBIuvoPZqud9mE11hUbRZjuImG30_L8BwH3qvDt4_mZyogWPHh-qHEjpWVKBB5b3AzczM3L_qlb3nU8j8wATq6MUdJxi3wipQ/w640-h526/wifi_583x480.jpg "Wifi RCP")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjOytlNHL_qXciB74M1E7XqX75xuGM4fUHbevZw0V2qtoGAdeZFO-1Z8yKlCbqaClZcRk6_cKo-2oUeTkyg-zibWkJmUSBIuvoPZqud9mE11hUbRZjuImG30_L8BwH3qvDt4_mZyogWPHh-qHEjpWVKBB5b3AzczM3L_qlb3nU8j8wATq6MUdJxi3wipQ/s583/wifi_583x480.jpg)  
 Pola ini berisifat *line of sight* (LOS), artinya tidak boleh 
ada rintangan dalam akses. Dalam realita, konfigurasi dasar efektif 
untuk jarak 30 mil, umumnya yang menjadi hambatan adalah kontur alam, 
hanya digunakan untuk akses ke satu titik node.


#### Konfigurasi yang Diperluas


Pola ini digunakan bila RCP diterapkan untuk akses ke beberapa node. 
Masing-masing node WiFi digunakan juga sebagai sistem relay, sehingga 
dapat menjangkau area yang luas. Extended configuration berjalan di 
frekuensi 2,4Ghz dan 5,8Ghz. Frekuensi 2,4Ghz dipakai untuk koneksi ke 
layer access (perangkat WiFi) dan transmisi antar node. Sedang 5,8Ghz 
digunakan khusus akses antar node dan koneksi ke backhaul.

[![modul RCP wifi](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgnLOjvYXulGc4BwrHwwpDLFz-gNTvZ3_rQb9zYW6Lxrw06JWhaMGZCs8CuuAAflxdEDPauUDGaKmm7jYh2NdL0pOGRMpuf5tkAZ2Y6mzEVxnq3gZywWx8KXRe4czqppr77w0XGjQ0-MRge2ixk8z4e-mNi-R6MDkA-vS6qDHxmTkKeq_Ei4oFInUNGuQ/w640-h316/wifi_640x316.jpg "modul rcp")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgnLOjvYXulGc4BwrHwwpDLFz-gNTvZ3_rQb9zYW6Lxrw06JWhaMGZCs8CuuAAflxdEDPauUDGaKmm7jYh2NdL0pOGRMpuf5tkAZ2Y6mzEVxnq3gZywWx8KXRe4czqppr77w0XGjQ0-MRge2ixk8z4e-mNi-R6MDkA-vS6qDHxmTkKeq_Ei4oFInUNGuQ/s640/wifi_640x316.jpg) Khusus konfigurasi dasar ditambahkan frekuensi 900Mhz untuk TDMA. 
Kabarnya, paket RCP segera akan ditawarkan dengan paket mulai dari 
US$500.

 

