---
layout: post
title: Tips Mengatasi update windows yang error
date: '2018-11-24T18:24:00.001+07:00'
author: rosari J
tags:
- windows
- registry
modification_time: '2022-07-10T18:27:24.377+07:00'
blogger_id: tag:blogger.com,1999:blog-7329298365997944344.post-6888084208190883319
blogger_orig_url: https://www.oktrik.com/2018/11/tips-mengatasi-update-windows-yang-error.html
---

Ada Kalanya saat kita hendak akan mengupdate systim pada instalasi windows kita terdapat error dengan notifikasi sebagai berikut "`Windows update cannot currently check for updates because the service is not running. You may need to restart your computer`" yang mengindikasi adanya kesalahan pada sistim update secara otomatis pada windows kita.

Hal ini tentunya cukup merepotkan karena dengan tidak berfungsinya fitur Sytem Update pada komputer yang kita gunakan tidak akan mendapatkan Update terbaru yang diperlukan oleh aplikasi aplikasi yang terinstal pada komputer kita Belum lagi masalah keamanan seperti serangan virus dan hacker

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjwRS4hOL35PFO75Wg7tcXZGZvfsupGhIckBmZrH_HllF5YkmqBBe2GZ4toKxoVO_CpV8-S69v7pvKgsy2aWWU94RgYIvYc7hEW70OlE7ojftRiLi7QOqL3hs_Us3jMuHsONqC2aYtiYo16k5E3_RRyVrjHH8gXkYo9Fu_b4eEq7aNJiw7vaZKCz4lmrw/w640-h480/update-1.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjwRS4hOL35PFO75Wg7tcXZGZvfsupGhIckBmZrH_HllF5YkmqBBe2GZ4toKxoVO_CpV8-S69v7pvKgsy2aWWU94RgYIvYc7hEW70OlE7ojftRiLi7QOqL3hs_Us3jMuHsONqC2aYtiYo16k5E3_RRyVrjHH8gXkYo9Fu_b4eEq7aNJiw7vaZKCz4lmrw/s1133/update-1.jpg)  
 Windows temporary update folder Yang Korup
------------------------------------------

Walaupun terdapat notifikasi untuk melakukan Restart system namun stelah dilakukan restart pada komputer tetap saja fitur otomatis update tidak dapat aktif hal ini tentunya sangat menjengkelkan Permasalahan atau Error Pada sistim update otomatis ini Penyebab umumnya biasanya dikarenakan Korupnya Windows temporary update folder (SoftwareDistribution)

Berikut ini adalah beberapa langkah yang dapat anda coba untuk memperbaiki Error `"Windows update cannot currently check for updates because the service is not running"` Pada Os Microsoft Windows 7, 8

### 1. Stop Windows Update service secara manual

Untuk melakukan ini caranya cukup mengakses panel services dengan Menekan Tuts Logo Windows dan R secara bersamaaan, ketik "services.msc" dan kemudian tekan ENTER pada keyboard anda dan carilah Kolom dengan Nama , Klik Kanan pada kolom **Windows update** dan pilih Stop

### 2. Menghapus Folder Update Temp

Buka menu "My computer" dan Browse pada folder Windows atau pada path berikut "C:Windows", kemudian cari Folder dengan nama "SoftwareDistribution". klik kanan dan delete folder tersebut

Namun apabila anda merasa ragu untuk menghapus folder `"SoftwareDistribution"`, cukup lakukan RENAME saja pada folder tersebut

### 3.Start Windows Update service secara manual

Kebalikan dari langkah nomer 1, namun kali ini pilih `"Start service"`

Apabila anda Menggunakan windows 7, sebelum melakukan langkah diatas silahkan mendownload terlebih dahulu security patch ([KB3102810](https://support.microsoft.com/en-us/topic/installing-and-searching-for-updates-is-slow-and-high-cpu-usage-occurs-in-windows-7-and-windows-server-2008-r2-4f8a3338-d690-58a8-a97c-9b5e383cad21)) baru kemudian menerapkan langkah update windows 7 tersebut di atas

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhTJarLj9XekuhcVS3lYvXf4yQXAI-VmKyBgxGpUfQH1htcTVNdKSCkGGR0sMGwPJaB6uOgbajUFWd8TWuhg-DvOIRc4QXttqMl0V-mD5XoUw3b98HTnkHEDHwtfduIkLdSHhn8ffN7NfHM7-KqmX9scByJYHN4FP5pdq2PmFeVEHGGl-s3mJa97fUOUg/w640-h468/Windows%20update_2.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhTJarLj9XekuhcVS3lYvXf4yQXAI-VmKyBgxGpUfQH1htcTVNdKSCkGGR0sMGwPJaB6uOgbajUFWd8TWuhg-DvOIRc4QXttqMl0V-mD5XoUw3b98HTnkHEDHwtfduIkLdSHhn8ffN7NfHM7-KqmX9scByJYHN4FP5pdq2PmFeVEHGGl-s3mJa97fUOUg/s824/Windows%20update_2.jpg)  
 Windows Update error
--------------------

Ada beberapa kesalahan yang sering terjadi terkait update Windows. Salah satu masalah yang paling umum adalah pesan kesalahan `"Potential Windows Update Database Error Detected"`. Ini disebabkan oleh registri yang salah di dalam sistem Windows yang melarang sistem operasi mengakses folder yang diperlukan pada drive C.

Untuk mengatasi masalah ini, memulai ulang Layanan Pembaruan Windows akan membantu:

1. Buka Manajer Layanan dengan memasukkan "Layanan" di area pencarian di menu mulai Anda.
2. Di Manajer Layanan, cari Pembaruan Windows. Klik kanan layanan dan pilih "Berhenti".
3. Tekan `Win + E` untuk masuk ke File Explorer. Klik kiri pada "PC Ini".
4. Temukan drive C lokal di File Explorer dan buka.
5. Buka folder DataStore dengan mengetik `C:\Windows\SoftwareDistribution\DataStore.`
6. Pilih semua file di folder `DataStore` dan hapus.
7. Kembali ke Manajer Layanan, klik kanan layanan Pembaruan Windows dan pilih "Mulai" untuk memulai kembali layanan.

 

 

 

