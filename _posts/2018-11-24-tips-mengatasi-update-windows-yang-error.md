---
layout: post
title: Tips Mengatasi update windows yang error
date: '2018-11-24T18:24:00.001+07:00'
author: rosari J
tags:
- windows
- registry
modified_time: '2022-07-10T18:27:24.377+07:00'
thumbnail: https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjwRS4hOL35PFO75Wg7tcXZGZvfsupGhIckBmZrH_HllF5YkmqBBe2GZ4toKxoVO_CpV8-S69v7pvKgsy2aWWU94RgYIvYc7hEW70OlE7ojftRiLi7QOqL3hs_Us3jMuHsONqC2aYtiYo16k5E3_RRyVrjHH8gXkYo9Fu_b4eEq7aNJiw7vaZKCz4lmrw/s72-w640-c-h480/update-1.jpg
blogger_id: tag:blogger.com,1999:blog-7329298365997944344.post-6888084208190883319
blogger_orig_url: https://www.oktrik.com/2018/11/tips-mengatasi-update-windows-yang-error.html
---

<p>Ada Kalanya saat kita hendak akan mengupdate systim pada instalasi windows kita terdapat error dengan notifikasi sebagai berikut "<code>Windows update cannot currently check for updates because the service is not running. You may need to restart your computer</code>" yang mengindikasi adanya kesalahan pada sistim update secara otomatis pada windows kita.</p><p>Hal ini tentunya cukup merepotkan karena dengan tidak berfungsinya fitur Sytem Update pada komputer yang kita gunakan tidak akan mendapatkan Update terbaru yang diperlukan oleh aplikasi aplikasi yang terinstal pada komputer kita Belum lagi masalah keamanan seperti serangan virus dan hacker</p><p></p><div class="separator" style="clear: both; text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjwRS4hOL35PFO75Wg7tcXZGZvfsupGhIckBmZrH_HllF5YkmqBBe2GZ4toKxoVO_CpV8-S69v7pvKgsy2aWWU94RgYIvYc7hEW70OlE7ojftRiLi7QOqL3hs_Us3jMuHsONqC2aYtiYo16k5E3_RRyVrjHH8gXkYo9Fu_b4eEq7aNJiw7vaZKCz4lmrw/s1133/update-1.jpg" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="850" data-original-width="1133" height="480" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjwRS4hOL35PFO75Wg7tcXZGZvfsupGhIckBmZrH_HllF5YkmqBBe2GZ4toKxoVO_CpV8-S69v7pvKgsy2aWWU94RgYIvYc7hEW70OlE7ojftRiLi7QOqL3hs_Us3jMuHsONqC2aYtiYo16k5E3_RRyVrjHH8gXkYo9Fu_b4eEq7aNJiw7vaZKCz4lmrw/w640-h480/update-1.jpg" width="640" /></a></div><br />&nbsp;<p></p><h2>Windows temporary update folder Yang Korup</h2><p>Walaupun terdapat notifikasi untuk melakukan Restart system namun stelah dilakukan restart pada komputer tetap saja fitur otomatis update tidak dapat aktif hal ini tentunya sangat menjengkelkan Permasalahan atau Error Pada sistim update otomatis ini Penyebab umumnya biasanya dikarenakan Korupnya Windows temporary update folder (SoftwareDistribution)</p><p>Berikut ini adalah beberapa langkah yang dapat anda coba untuk memperbaiki Error <code>"Windows update cannot currently check for updates because the service is not running"</code> Pada Os Microsoft Windows 7, 8</p><h3>1. Stop Windows Update service secara manual</h3><p>Untuk melakukan ini caranya cukup mengakses panel services dengan Menekan Tuts Logo Windows dan R secara bersamaaan, ketik "services.msc" dan kemudian tekan ENTER pada keyboard anda dan carilah Kolom dengan Nama , Klik Kanan pada kolom <b>Windows update</b> dan pilih Stop</p><h3>2. Menghapus Folder Update Temp</h3><p>Buka menu "My computer" dan Browse pada folder Windows atau pada path berikut "C:Windows", kemudian cari Folder dengan nama "SoftwareDistribution". klik kanan dan delete folder tersebut</p><p>Namun apabila anda merasa ragu untuk menghapus folder <code>"SoftwareDistribution"</code>, cukup lakukan RENAME saja pada folder tersebut</p><h3>3.Start Windows Update service secara manual</h3><p>Kebalikan dari langkah nomer 1, namun kali ini pilih <code>"Start service"</code></p><p>Apabila anda Menggunakan windows 7, sebelum melakukan langkah diatas silahkan mendownload terlebih dahulu security patch (<a href="https://support.microsoft.com/en-us/topic/installing-and-searching-for-updates-is-slow-and-high-cpu-usage-occurs-in-windows-7-and-windows-server-2008-r2-4f8a3338-d690-58a8-a97c-9b5e383cad21" rel="nofollow noopener" target="_blank">KB3102810</a>) baru kemudian menerapkan langkah update windows 7 tersebut di atas</p><p></p><div class="separator" style="clear: both; text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhTJarLj9XekuhcVS3lYvXf4yQXAI-VmKyBgxGpUfQH1htcTVNdKSCkGGR0sMGwPJaB6uOgbajUFWd8TWuhg-DvOIRc4QXttqMl0V-mD5XoUw3b98HTnkHEDHwtfduIkLdSHhn8ffN7NfHM7-KqmX9scByJYHN4FP5pdq2PmFeVEHGGl-s3mJa97fUOUg/s824/Windows%20update_2.jpg" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="602" data-original-width="824" height="468" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhTJarLj9XekuhcVS3lYvXf4yQXAI-VmKyBgxGpUfQH1htcTVNdKSCkGGR0sMGwPJaB6uOgbajUFWd8TWuhg-DvOIRc4QXttqMl0V-mD5XoUw3b98HTnkHEDHwtfduIkLdSHhn8ffN7NfHM7-KqmX9scByJYHN4FP5pdq2PmFeVEHGGl-s3mJa97fUOUg/w640-h468/Windows%20update_2.jpg" width="640" /></a></div><br />&nbsp;<p></p><h2>Windows Update error</h2><p>Ada beberapa kesalahan yang sering terjadi terkait update Windows. Salah satu masalah yang paling umum adalah pesan kesalahan <code>"Potential Windows Update Database Error Detected"</code>. Ini disebabkan oleh registri yang salah di dalam sistem Windows yang melarang sistem operasi mengakses folder yang diperlukan pada drive C.</p><p>Untuk mengatasi masalah ini, memulai ulang Layanan Pembaruan Windows akan membantu:</p><ol><li>Buka Manajer Layanan dengan memasukkan "Layanan" di area pencarian di menu mulai Anda.</li><li>Di Manajer Layanan, cari Pembaruan Windows. Klik kanan layanan dan pilih "Berhenti".</li><li>Tekan <code>Win + E</code> untuk masuk ke File Explorer. Klik kiri pada "PC Ini".</li><li>Temukan drive C lokal di File Explorer dan buka.</li><li>Buka folder DataStore dengan mengetik <code>C:\Windows\SoftwareDistribution\DataStore.</code></li><li>Pilih semua file di folder <code>DataStore</code> dan hapus.</li><li>Kembali ke Manajer Layanan, klik kanan layanan Pembaruan Windows dan pilih "Mulai" untuk memulai kembali layanan.</li></ol><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p>