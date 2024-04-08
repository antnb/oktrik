---
layout: post
title: Cara Mengatasi "An authentication error has occurred.The function requested
 is not supported" Pada Koneksi RDP
date: '2018-06-26T16:06:00.001+07:00'
author: rosari J
tags:
- remote desktop
- windows
- exploit
modification_time: '2022-07-10T16:09:44.203+07:00'
blogger_id: tag:blogger.com,1999:blog-7329298365997944344.post-1551325494185517665
blogger_orig_url: https://www.oktrik.com/2018/06/cara-mengatasi-authentication-error-has.html
---

Bagi anda yang terbiasa bekerja menggunakan server atau anda yang memiliki server dengan OS windows khususnya sejak awal bulan mei 2018 tentu menghadapi kendala tidak dapat terkoneksi dengan server saat akan melakukan koneksi remote desktop atau RDP. begitu pula dengan saya, saya tidak dapat melakukan koneksi RDP kebeberapa server yang saya kelola dengan notifikasi pesan error


> `An authentication error has occurred.The function requested is not supported`

Beragam cara saya lakukan namun tetap saja komputer klien tidak dapat tersambung menggunakan protokol Windows RDP. hal ini tentu saja merepotkan karena koneksi RDP sangat diperlukan apabila anda hendak memanage server dengan OS windows yang sangat memerlukan interaksi visual berbeda dengan server berbasis linux dimana kebanyakan dimanage dengan protokol ssh melalui shell.

karena pentingnya akses RDP saat memanage server windows dan saya sudah kehabisan cara untuk mencari solusinya, maka saya putuskan untuk membaca baca artikel artikel ilmu komputer yang ada di internet dan saya berhasil menemukan solusi bagi yang mengalami gagal terkoneksi melalui RDP.

[![rdp exploit](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhtnskIU_UHEtZTB6PzioTTpwqxAGrq3fF_IvCx03pShHOoP07NaKkWW8pOXwh7FN53509IPonbx2ahQ962gtqDIdAWYng8GUTqrMOxi-8Pygdkp-nfolDRj-6P3_ZngrH5fgXAQ1oBqZgz0Ehjx838Tk_yPgUPDPTwQ4-Aav7baJoWCweTJzM86CndXA/w640-h400/rdp-1-800x500.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhtnskIU_UHEtZTB6PzioTTpwqxAGrq3fF_IvCx03pShHOoP07NaKkWW8pOXwh7FN53509IPonbx2ahQ962gtqDIdAWYng8GUTqrMOxi-8Pygdkp-nfolDRj-6P3_ZngrH5fgXAQ1oBqZgz0Ehjx838Tk_yPgUPDPTwQ4-Aav7baJoWCweTJzM86CndXA/s800/rdp-1-800x500.jpg)  
 Mengenal Rdp
------------

Remote Desktop Protocol (RDP) adalah protokol Interkoneksi antar unit Komputer yang dikembangkan oleh Microsoft, Protokol ini memungkinkan sebuah unit komputer melakukan Antarmuka secara visual dengan Unit Komputer lain nya Melalui Koneksi jaringan.

Dalam sistim operasi Windows Pengguna menjalankan Koneksi Remote desktop Menggunakan perangkat lunak yang telah tersedia dalam windows `mstsc.exe`, Sedangkan Bagi Komputer lain nya Cukup Membuka Port Port Tertentu dalam firewall agar dapat menerima koneksi RDP dari pengguna. Biasanya Port yang dibuka adalah Port 3389 Untuk TCP Dan 3389 UDP.


> Dengan Remote Desktop Connection, Anda dapat terhubung ke komputer yang menjalankan Windows dari komputer lain menjalankan Windows yang terhubung ke jaringan yang sama atau ke Internet. Misalnya, Anda dapat menggunakan semua program komputer, file, dan sumber daya jaringan kerja Anda dari komputer di rumah, dan itu seperti Anda duduk di depan komputer Anda di tempat kerja. [https://support.microsoft.com/en-us/help/17463/windows-7-connect-to-another-computer-remote-desktop-connection](https://support.microsoft.com/en-us/windows/how-to-use-remote-desktop-5fe128d5-8fb1-7a23-3b8a-41e636865e8c)

**Celah keamanan Pada Credential Security Support Provider protocol**
---------------------------------------------------------------------

Pada bulan maret [Microsoft merilis update atau patch untuk CredSSP](https://msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2018-0886) setelah diketahui secara publik bahwa Fitur CredSSP mempunyai celah keamanan yang cukup vital dan dapat digunakan oleh pihak yang tidak bertanggung jwab untuk mengambil alih sistim anda secara paksa.

Celah keamanan ini cukup berbahaya karena hacker dapat menjalankan kode kode jahat yang pada akhirnya akan dieksekusi oleh sistim operasi target

Dan pada Common Vulnerabilities and Exposures `(CVE)` dialokasikan angka 2018-0886 pada celah keamanan ini atau [CVE-2018-0886](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-0886)

**RDP Error An authentication error has occurred Terjadi Pada Komputer Yang telah di Patch**
--------------------------------------------------------------------------------------------

Kegagalan Sambungan RDP ini terjadi dikarenakan server atau client dikonfigurasikan untuk menerima update otomatis dari Microsoft, Dan dalam kasus saya adalah komputer client atau komputer rumah saya memang saya konfigurasikan untuk melakukan update secara otomatis sedangkan pada komputer server tidak saya konfigurasikan untuk melakukan update otomatis

Jadi Jika nilai registry pada Group Policy telah berubah untuk menolak koneksi yang berasal dari komputer Client yang belum terinstal Patch `CRedSSP` ( [https://support.microsoft.com/en-gb/help/4093492/credssp-updates-for-cve-2018-0886-march-13-2018](https://support.microsoft.com/en-gb/topic/credssp-updates-for-cve-2018-0886-5cbf9e5f-dc6d-744f-9e97-7ba400d6d3ea)) maka kita akan menerima pesan error saat melakukan koneksi menggunakan Protokol RDP


> ```
> May 8, 2018
> ```
> An update to change the default setting from Vulnerable to Mitigated.
> 
> Related Microsoft Knowledge Base numbers are listed in CVE-2018-0886.
> 
> By default, after this update is installed, patched clients cannot communicate with unpatched servers. Use the interoperability matrix and group policy settings described in this article to enable an “allowed” configuration.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjtMGgCTDF0YAof0C_0h7fAF-aT1OzE5IwuckjDDCYf4bAhwWEf2MMdD9ooLMvCuoYMVrf9R7rWVLyue73c0TbfUAfUxrn5Y-QA-2JJjdHZNAk-KIqtth7xq0n6AvUJkVVf0kZuTnX1Cgd1dLPQffLxpBIVibFSHb7vK9pP52szrZgPISu2kvmt_o1qWQ/w640-h404/credssp%20rdp.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjtMGgCTDF0YAof0C_0h7fAF-aT1OzE5IwuckjDDCYf4bAhwWEf2MMdD9ooLMvCuoYMVrf9R7rWVLyue73c0TbfUAfUxrn5Y-QA-2JJjdHZNAk-KIqtth7xq0n6AvUJkVVf0kZuTnX1Cgd1dLPQffLxpBIVibFSHb7vK9pP52szrZgPISu2kvmt_o1qWQ/s1012/credssp%20rdp.png)  
    
**Solusi RDP yang Error**
-------------------------

Setelah kita mengetahui akar permasalahan kenapa kita gagal konek saat hendak melakukan remote desktop atau RDP ke server, yaitu tidak singkronnya Server yang telah terinstall update atau patch Untuk CVE- 2018-0886 atau sebaliknya Komputer server yang belum terinstal Patch. Maka solusi bagi pengguna yang mengalami masalah dengan koneksi RDP ialah Menginstal Patch DIKEDUA KOMPUTER

Namun Muncul Kembali suatu pertanyaan. bagaimana [cara mengupdate windows](https://www.oktrik.com/tips-mengatasi-windows-update-error.html) agar terinstal patch Celah Keamanan CredSSP ( [https://support.microsoft.com/en-us/help/4093492/credssp-updates-for-cve-2018-0886-march-13-2018](https://support.microsoft.com/en-us/topic/credssp-updates-for-cve-2018-0886-5cbf9e5f-dc6d-744f-9e97-7ba400d6d3ea)) Jika melakukan koneksi ke remote komputer saja tidak bisa ?

Untuk Mensiasati hal ini kita dapat merubah nilai registry pada setting local policy windows. Cara nya cukup mudah yaitu mengakses Seting Local Policy Computer `Configuration >> Administrative Templates >> System >> Credentials Delegation >> Encryption Oracle Remediation`.

