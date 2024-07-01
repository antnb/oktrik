---
layout: post
title: Cara Menggunakan perintah dasar linux CLI
date: '2018-07-22T15:08:00.002+07:00'
author: rosari J
tags:
- linux
- command
- bash
modification_time: '2022-07-10T15:10:59.226+07:00'
blogger_id: tag:blogger.com,1999:blog-7329298365997944344.post-3447126723975069246
blogger_orig_url: https://www.oktrik.com/2018/07/cara-menggunakan-perintah-dasar-linux.html
---

**Perintah dasar linux** tidak hanya untuk penggemar Unix kita akan melihat bagaimana melakukan semuanya dari keyboard.

**Memaximalkan Kekuatan Linux**
-------------------------------

Sebelumnya kita melihat hal-hal yang perlu diperhatikan sebelum instalasi.  Kali ini kita mulai pembahasan kita secara singkat melihat desktop Linux. Untuk proses instalasi linux itu sendiri, bisa anda lihat pada artikel berikut.

Jika anda tidak mempunyai resource dan waktu untuk menginstal Linux, masih ada cara lain untuk masuk ke dunia Linux yang itu dengan menggunakan “live distro”. Selanjutnya, kita akan mempelajari beberapa perintah perintah dasar pada seperti menampilkan *daftar directory files dengan perintah LS* langsung linux CLI sehingga anda bisa melakukan semuanya cukup dari keyboard.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWTPlOxvwmQLhj86rlVVpSDzvr817Q-Vl3rP_4xfT5slCDiMqG6VvOnhqApEHrb7p-97UTpI0QuJ0AO07yIBa7e-Koe8Z2i1CzGWpSYyP5qEZ09Sat18RWwdpKuL7lR61_zEwgYdNguMskMVlUP6rrux9x7K6Wjjt_DzuWNN6_btef0cSrBazFw7VVoQ/w640-h400/shell-1-800x500.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWTPlOxvwmQLhj86rlVVpSDzvr817Q-Vl3rP_4xfT5slCDiMqG6VvOnhqApEHrb7p-97UTpI0QuJ0AO07yIBa7e-Koe8Z2i1CzGWpSYyP5qEZ09Sat18RWwdpKuL7lR61_zEwgYdNguMskMVlUP6rrux9x7K6Wjjt_DzuWNN6_btef0cSrBazFw7VVoQ/s800/shell-1-800x500.jpg)  
 **Desktop GUI Mana Yang Harus Saya Instalasi, KDE atau Gnome ?**
----------------------------------------------------------------

Jika ruang harddisk memungkinkan, pasti dua-duanya. Anda kemudian dapat memutuskan apakah menyukai KDE, Gnome, atau desktop yang lain, tetapi apapun pilihannya, anda pasti ingin kedua library KDE dan Gnome terinstalasi.

Setelah library terinstalasi, program KDE bisa berjalan di bawah Gnome dan sebaliknya, di mana itu adalah hal yang bagus karena ada saja aplikasi menarik yang ditulis dengan menggunakan salah satu dari kedua library.

Jika ruang harddis menjadi pertimbangan, “desktop” hanyalah sebagian kecil dari system KDE dan Gnome sehingga anda tidak menghemat banyak dengan menghilangkan desktop dan berusaha untuk menginstalasi “library only”.

KDE dan Gnome datang dengan sekumpulan program dan tool menarik, jadi tidak ada salahnya untuk menginstalasi kedua desktop secara lengkap. Kami tidak pernah mendengar bahwa keduanya bertentangan satu sama lain.

Untuk pekerjaan sehari-hari, kami menggunakan KDE karena terasa lebih solid dibanding Gnome. Jika anda suka yang lebih “modern”, gunakan Gnome, tetapi jangan mengeluh jika ada yang tidak selalu bekerja dengan baik.

Tidak ada salahnya jika anda juga menginstalasi Windows manager “alternative”. Mereka tidak memakan banyak ruang (beberapa bahkan sangat kecil) dan berguna saat situasi tertentu. Anda bisa menjalankan aplikasi KDE atau Gnome apa pun di bawah mereka, sepanjang library KDE dan Gnome terinstalasi. KDE lebih lapar kekuatan.

Pada hardware yang lebih tua kami lebih memilih Gnome dari pada KDE. Windows manager lain lebih enteng dibanding KDE atau Gnome. Oleh karena itu, pada hardware yang lebih rendah, kami sarankan untuk menggunakan Windows manager alternative.

**Shell / linux cli**
---------------------

Setelah melakukan instalasi dan masuk ke dalamnya, akan membuat anda terbiasa dengan lingkungan grafis Linux. Kita akan melihat ke bagian paling dalam dan paling gelap dari system anda : **command line atau terminal linux**, yang dalam Linux di kenal sebagai *shell*.

Boot system anda dan masuklah supaya dapat melihat desktop KDE/Gnome, kemudian tekan `[Ctrl]+[Alt]+[F1]`. Apa yang akan anda lihat mirip seperti MS-DOS (mungkin lebih seperti MS-DOS nantinya jika saja Microsoft terus mengembangkannya sampai sekarang). Anda akan melihat login prompt ; masukkan username dan password dan anda akan login.

[![shell linux prompt](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjUSAbeTKDSLJRlYrVv4Rb-K-0mh6hL1oBU_WyD-hmLlvaVmpdEdGtGWQDSmz96keBjjNaTPO59J7IXMxfzXVvXP4sjWXv7QcbhVVU3jHvSns5DI93lVQ6kMFeXPKh0vPklmTc9c5VfXY38V45RTb6wdgWaUUGTs0D8JnYn-vTzn06yEhw1x2IMjFYRwQ/w640-h434/bash%20shell%20pada%20linux.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjUSAbeTKDSLJRlYrVv4Rb-K-0mh6hL1oBU_WyD-hmLlvaVmpdEdGtGWQDSmz96keBjjNaTPO59J7IXMxfzXVvXP4sjWXv7QcbhVVU3jHvSns5DI93lVQ6kMFeXPKh0vPklmTc9c5VfXY38V45RTb6wdgWaUUGTs0D8JnYn-vTzn06yEhw1x2IMjFYRwQ/s742/bash%20shell%20pada%20linux.png)  
 ### Cari tau Directory Path saat ini

Yang paling pertama anda akan disambut dengan sesuatu seperti berikut :


> `Last login : Mon Jun 20  
> 
> 15 : 20 : 10 on : 0  
> 
> [root@server root] $/`

Pada baris pertama, anda bisa melihat bahwa tidak ada orang lain yang menggunakan account anda. Berisi kedua adalah shell prompt yang terdiri dari beberapa bagian. Dari kiri ke kanan mereka adalah :


> \*root : ini merupakan nama user yang digunakan untuk masuk.  
> \*server : ini merupakan nama host dari computer local.  
> \*root : ini merupakan nama direktori aktif.  
> \*$ : ini merupakan tanda bahwa anda login sebagai user biasa. Jika melihat # berarti anda adalah *root*.

Kita akan lihat bahwa root pertama berbeda dengan root kedua dengan menggunakan perintah untuk pindah ke direktori aktif : ketik “cd..”. Jika biasa dengan DOS, perintah ini tidak asing lagi bagi anda : cd berarti change directory, dan .. adalah kode untuk `parent directory`.

Pada waktu digunakan bersama mereka menaikkan anda satu level pada system file anda. Secara default, anda akan berada di home directory anda pada waktu login dalam contoh di sini adalah `/home/root`. Dengan menjalankan “cd..” anda akan naik satu directory, yaitu ke /home, sehingga jadi anda akan melihat shell prompt berubah menjadi `[root@server home] $.`

Seperti yang anda lihat, prompt hanya memberi tahu di direktori mana anda berada : `shell prompt` mengatakan root bukannya `/home/root`. Ini kadang membingungkan. Sebagai contoh, jika dikatakan back up, apakah itu berarti `/home/root/backup` atau `/home/root/backup`? Anda bisa menghilangkan kebingungan tersebut dengan menggunakan perintah ped (print The Working Directory) untuk menampilkan direktori saat itu.

Anda bisa dengan cepat kembali ke home directory anda dengan mengetikkan cd. Sama juga, anda bisa menggunakan “cd..” untuk kembali ke direktori terakhir anda berada, seperti berikut :


> [root@server root]`[root@server etc] $ cd - /home/root  
> 
> [root@server root] $`

Perhatikan bahwa menggunakan “cd” akan mengembalikan anda ke direktori sebelumnya dan juga menampilkan path lengkap dari direktori tersebut.

### **Pengunaan command prompt DOS Yang Lebih maju**

Selain `cd`, ada *perintah perintah dasar linux* lain yang tidak asing lagi dari DOS : misalnya “dir” yang akan menampilkan isi direktori aktif, tetapi anda akan menemukan bahwa copy, ren, del, move dan lainnya tidak hadir dalam bentuk yang sama.

Linux mempunyai ekivalennya dan mereka lebih maju. Sebagai contoh, jika `dir` menampilkan isi direktori, perintah `ls` menampilkan direktori dan member warna hasilnya. Untuk copy file gunakan `cp`, untuk membuat direktori gunakan `mkdir` dan untuk menghapus file dan direktori gunakan `rm`. Meskipun MS-DOS mempunyai dua perintah untuk memindahkan data dan mengubah nama, Linux mempunyai satu : `mv` untuk memindahkan file dan juga mengubah nama mereka.

Sebagai contoh, perintah berikut (untuk kemudahan shell prompt di singkat menjadi $) akan membuat direktori bernama foobar, mengubah namanya menjadi wombat, mengcopy file ke dalam direktori `/etc/issue`, kemudian menghapus file dan menghapus direktori :


> `$ mkdir footbar`  
> `$ mv footbar wombat`  
> `$ cp /etc/issue wombat`  
> `$ rm wombat/issue`  
> `$ rm –rf wombat`

Perintah `rm` tidak akan begitu saja menghapus direktori : dengan menggunakan `-r (recurse)` akan menghapus direktori dan semua isinya dan `-f (force)` akan memaksa supaya direktori tersebut dihapus. Anda harus menggunakan `-rf` untuk menghapus direktori.

[![command linux](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhneH5MG7LePUF3n4RvPU4av0VScQqiRjo7EQhywzT-ensRdYDHgy79JhA5TttqSHvVHl8c-SdDmJ9niQpEVOtN39d3Zai4xqafVQH6ltfzWEOhRUaWu6NpzG1e5-2R9U8QYeTjfVsdBfnaw2dJqjIk7d0azuSTGbOi0ybP3w7x1GZbblxrvbpiNlyppw/w640-h400/8auYL.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhneH5MG7LePUF3n4RvPU4av0VScQqiRjo7EQhywzT-ensRdYDHgy79JhA5TttqSHvVHl8c-SdDmJ9niQpEVOtN39d3Zai4xqafVQH6ltfzWEOhRUaWu6NpzG1e5-2R9U8QYeTjfVsdBfnaw2dJqjIk7d0azuSTGbOi0ybP3w7x1GZbblxrvbpiNlyppw/s646/8auYL.png)  
 **Kemudahan Dalam Proses Administrasi Sistim**
----------------------------------------------

Dengan shell yang powerful, anda bisa melakukan hamper semuanya pada Linux melalui teks (keyboard). Sebagai contoh, ketik “lynx www.pcmedia.co.id” untuk membuka Web browser lynx (mode teks). Jika anda ingin mempunyai lynx, coba w3m. Gunakan `[Q]` untuk berhenti atau tekan `[Ctrl]+[C]` jika anda mengalami masalah.

Anda melihat penggunaan resource system dengan perintah `top`. % CPU menunjukkan berapa banyak waktu CPU yang digunakan oleh masing-masing aplikasi, dengan NI menunjukkan niceness. Ini merupakan ukuran bagaimana kemungkinan program untuk berbagi resource system dengan program lain (angka niceness yang lebih tinggi berarti aplikasi menggunakan waktu CPU yang lebih sedikit).

Jika ingin mengubah status system, anda harus berubah menjadi root. Ini bisa dilakukan dengan perintah “su”, yang berarti “substitute user” ia mengubah anda ke account lain. Anda bisa memberikan username yang diinginkan, tetapi jika anda tidak memberikannya, maka `“su”` akan menganggap anda ingin berubah ke user root.

Setelah berubah menjadi root (perhatikan bahwa sekarang anda mempunyai `#` bukannya `$` pada prompt), coba instalasi fortune dengan mengetikkan `“urpmi fortune”`. URPMI adalah engine instalasi Mandrake jika anda menggunakan Debian, ketik “aptget fortune”, dan untuk pengguna Fedora gunakan “yun install fortune”. Setelah selesai menggunakan account root, ketik exit untuk kembali ke account yang lama.

Terakhir tetapi bukan penghabisan adalah perintah grep yang mencari teks dan menampilkan yang cocok. Berikut adalah dua contohnya :


> `Grep “hello” *.txt`  
> `Grep –r “testing” /usr/src/linux/*`

Yang pertama mencari teks “hello” pada file berakhiran .txt. yang kedua menggunakan `–r (recursive)` untuk mencari kata “testing” pada seluruh file dalam direktori `/usr/src/linux` dan subdirektorinya. Anda harus menginstalasi souce code kernel untuk melakukan ini.

Membiasakan diri dengan shell Linux pada awalnya mungkin menakutkan tetapi tidak ada salahnya : anda bisa mendapatkan banyak hal dengan menggabungkan beberapa perintah yang tidak mungkin dilakukan pada lingkungan grafis.

Sekarang percobaan anda sudah selesai : anda bisa menekan `[Ctrl]+[Alt]+[F7]` untuk kembali kedalam point and click !

 

