---
layout: post
title: Cara Menggunakan Formula RANK Dalam Microsoft Excel
date: '2017-12-12T16:43:00.001+07:00'
author: rosari J
tags:
- rank
- microsoft
modification_time: '2022-07-10T16:45:42.269+07:00'
blogger_id: tag:blogger.com,1999:blog-7329298365997944344.post-2459488084306429937
blogger_orig_url: https://www.oktrik.com/2017/12/cara-menggunakan-formula-rank-dalam.html
---

Bagi Yang berkerja menyusun data mungkin sudah tidak asing lagi dengan istilah RANK dalam Microsoft Excel. RANK Berfungsi sebagai Formula untuk menentukan

Posisi relative atau susunan nilai dalam suatu blok berisi data dan melakukan perbandingan terhadap nilai yang sama. Yang artinya anda tidak perlu lagi melakukan sortir data berdasrkan nilai besaran (tinggi atau rendah)untuk menentukan RELATIVE RANKINGS dari suatu nilai

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEilhdUVtt2Tmoon6HDItaoeG0LeK5LXOJr3dQollj-sgoj2CiObG3mQJQZp3SDtkQMP4GLF78NTKowyBPCLej7d2ghrsr5fi-GTSvcGJOcxVvi0hwSPl5oqZ-W0tnxYHB3N1Cybk6WcjFjV7EgGEl6WZ9GGUHI5hxwuSUS9IfL0hja3X5Bv5glgmBO-eA/w640-h400/rank-1-800x500.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEilhdUVtt2Tmoon6HDItaoeG0LeK5LXOJr3dQollj-sgoj2CiObG3mQJQZp3SDtkQMP4GLF78NTKowyBPCLej7d2ghrsr5fi-GTSvcGJOcxVvi0hwSPl5oqZ-W0tnxYHB3N1Cybk6WcjFjV7EgGEl6WZ9GGUHI5hxwuSUS9IfL0hja3X5Bv5glgmBO-eA/s800/rank-1-800x500.jpg)  
RELATIVE RANKINGS
-----------------

Sebagai contoh Dalam gambar berikut dibawah ini, Nilai Data penjualan diurutkan atau disortir dalam kolom PRODUCT. Dalam gambar tersebut Kita dapat menentukan RANK tanpa harus melakukan sortir data pada kolom "TOTAL SALES".

Fungsi RANK dalam microsoft Excel sangat berguna jika anda dalam situasi yang telah digambarkan diatas. Formula Untuk Fungsi RANK dapat kita masukan pada cells C2 dan C11 yang kemudian akan menghasilkan Nilai besaran RANK tersebut tanpa kita melakukan sortir besaran data.

Syntax Formula RANK cukup sederhana,sebagai contoh berikut ini adalah formula yang digunakan pada contoh gambar dan di input pada cell C2

*`=RANK(B2,$B$2:$B$11`*

Secara default Fungsi RANK dalam excel akan mengolah data dalam urutan menurun (kecil Ke besar), namun jika anda menginginkan hasil dalam bentuk sebaliknya anda dapat memodifikasi Formula tadi dalam bentuk argumen tambahan dengan menambahkan Besaran nilai selain 0 pada blok data yang anda inginkan,Pada gambar contoh diatas Penambahan rumus RANK tersebut menjadi

*`=RANK(B2,$B$2:$B$11,1)`*

Fungsi atau Fitur **RANK dalam microsoft Excel** Memberikan banyak kemudahan dalam menganalisa data. Kita dapat mengolah data dalam jumlah besar untuk menentukan Posisi Relatif dalam data yang akan kita olah secara cepat dan efisien

Referensi :  
[https://support.office.com/en-us/article/RANK-function-6a2fc49d-1831-4a03-9d8c-c279cf99f723](https://support.microsoft.com/en-us/office/rank-function-6a2fc49d-1831-4a03-9d8c-c279cf99f723?ui=en-us&rs=en-us&ad=us) 

  

 

