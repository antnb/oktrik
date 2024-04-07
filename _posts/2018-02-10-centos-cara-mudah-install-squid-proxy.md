---
layout: post
title: "[Centos] Cara Mudah Install Squid Proxy Dengan Script Auto Install"
date: '2018-02-10T16:29:00.005+07:00'
author: rosari J
tags:
- internet
- proxy server
modified_time: '2022-07-12T12:07:58.021+07:00'
thumbnail: https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZdlSA3GFnlU_CuBr67nmbavqr-MA5DBZRhWJKuWT471u9eFqbdPoxJcABqC-nVg11HKkkY3f4txAtdAYsXY6Cbi9H3cQCorAGPzgwVSr2SFMu6gEG3wWWsYNL-0qtxM0CdnHvWBfeZ1DJeZ6JyTwdZAxbftqNWxmnopOrqROjY5uBYqkWUjGazTXdkQ/s72-w640-c-h400/squid-1-800x500.jpg
blogger_id: tag:blogger.com,1999:blog-7329298365997944344.post-8034672217200371743
blogger_orig_url: https://www.oktrik.com/2018/02/centos-cara-mudah-install-squid-proxy.html
---

<p>Artikel ini akan menunjukkan cara Install Squid Proxy di centos 5 dan mengkonfigurasi Firefox dan Chrome untuk menggunakannya.</p>
<h2>Squid Proxy server</h2>
<p>Squid adalah proxy caching berfitur lengkap yang mendukung HTTP, HTTPS, FTP, dan protokol jaringan utama lainnya. Ini dapat digunakan untuk mempercepat server web dengan menyimpan kueri berulang, memfilter lalu lintas web, dan mendapatkan akses ke konten yang dibatasi secara geografis.</p>
<p>Squid Proxy Adalah software dengan lisensi open source gratisan yang menawarkan beragam keunggulan diantaranya adalah multi platform,full control terhadap berbagai aspek yang ditawarkan oleh squid, sanggup melakukan filter terhadap trafic yang dihandle, suport mengolah lalu lintas bermacam macam internet protokol seperti HTTPS,FTP dan beragam keunggulan lain nya dibandingkan dengan software proxy lain nya.</p>
<p>Salah satu kegunaan squid proxy lainnya ialah untuk <a href="{{ site.baseurl }}{% post_url 2018-11-27-tips-dan-cara-memblokir-situs-dewasa %}" target="_blank" rel="noopener">mengakses situs yang diblokir</a>. Misalnya Kantor tempat bekerja anda Membatasi Akses Ke situs <a href="https://www.oktrik.com/search/label/facebook" target="_blank" rel="noopener">media sosial seperti Facebook</a>, maka dengan menggunakan proxy anda dapat dengan mudah membypass situs yang telah diblokir tersebut</p>
<p><div align="center">
<!-- oktrikresponsi -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-8410270452001273"
     data-ad-slot="6888399955"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div></p>
<div class="separator" style="clear: both; text-align: center;"><a style="margin-left: 1em; margin-right: 1em;" href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZdlSA3GFnlU_CuBr67nmbavqr-MA5DBZRhWJKuWT471u9eFqbdPoxJcABqC-nVg11HKkkY3f4txAtdAYsXY6Cbi9H3cQCorAGPzgwVSr2SFMu6gEG3wWWsYNL-0qtxM0CdnHvWBfeZ1DJeZ6JyTwdZAxbftqNWxmnopOrqROjY5uBYqkWUjGazTXdkQ/s800/squid-1-800x500.jpg"><img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZdlSA3GFnlU_CuBr67nmbavqr-MA5DBZRhWJKuWT471u9eFqbdPoxJcABqC-nVg11HKkkY3f4txAtdAYsXY6Cbi9H3cQCorAGPzgwVSr2SFMu6gEG3wWWsYNL-0qtxM0CdnHvWBfeZ1DJeZ6JyTwdZAxbftqNWxmnopOrqROjY5uBYqkWUjGazTXdkQ/w640-h400/squid-1-800x500.jpg" alt="" width="640" height="400" border="0" data-original-height="500" data-original-width="800" /></a></div>
<h2 style="text-align: left;">Caching Proxy </h2>
<p><a href="http://www.squid-cache.org/" target="_blank" rel="nofollow noopener">Squid</a> mampu melakukan proses caching dan melakukan forward web proxy secara efisien sehingga kita tidak perlu merequest file yang sama berulang ulang karena telah tersimpan dalam folder cache dalam directory kita menginstall squid, Squid pun mempunyai extensive access control yang berguna untuk mempercepat sebuah server yang dikonfigurasikan sebagai web server</p>
<p>Dalam artikel ini kita akan membahas cara mudah Install Squid Proxy dengan menggunakan server dengan platform Unix yaitu centos, Penulis mengalami sendiri Terkadang kita menemui masalah saat menginstal proxy di vps yang kita miliki seperti konfigurasi <code>ACL</code>, <code>Squid Cache directory</code>, <code>zero sized reply</code>, <code>The request or reply is too large</code>, <code>Connection refused</code>, <code>Ignoring MISS from non-peer</code> dan segudang masalah lainnya yang terkadang memerlukan pengetahuan paling tidak sebagai server admin dan tidak mudah untuk dimengerti bagi user yang baru saja mengenal Linux/ Unix .</p>
<p><em>Tutorial Menginstall Squid Proxy dengan password</em> ini bisa diterapkan pada Vps dengan Os Ubuntu, Centos, Debian Maupun Fedora Dengan Minimal Centos 5 dan Debian 6</p>
<p><div align="center">
<!-- responsiv -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-8410270452001273"
     data-ad-slot="6719527881"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div></p>
<h2><strong>Hal Yang diperlukan untuk Install Squid Proxy software<br /></strong></h2>
<ol>
<li>Sebuah server yang akan digunakan sebagai Host</li>
</ol>
<h2><strong>Langkah Menginstal Squid Pada Vps</strong></h2>
<p>lakukan update dependency yang diperlukan oleh squid , disini saya masih memakai centos 5 dan karena os tersebut sudah sangat jadul maka harus terlebih dahulu mengupdate mirror list pada folder <code>/etc/yum.repos.d</code>.</p>
<p>Hal ini dikarenakan support untuk centos 5 sudah dihentikan oleh karena itu mirror standart yang ada pada folder tersebut sudah tidak bisa dipakai . login sebagai root kemudian lakukan Yum Update dengan mengetik yum update pada terminal <code>yum update</code></p>
<p>&nbsp;</p>
<div class="separator" style="clear: both; text-align: center;"><code><a style="margin-left: 1em; margin-right: 1em;" href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiTIFLTbYGxxDC-hTz74aG0wmWJ9Euius96XyJkIqO5rRrNjvhMIqVfs5lCu23SJr5OP8aYNVXz_6SAH5GTrVEEGZXfy0BjCraV6OztG2Z5UO9TkmhzNu0exxFm1LeGIJsCdorPybQJW0SA9ACL6G_VF81e_Glz_9PavriKI1PEQ20YIyaFON3_ZcRLyA/s1024/yum-update_1024x569.jpg"><img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiTIFLTbYGxxDC-hTz74aG0wmWJ9Euius96XyJkIqO5rRrNjvhMIqVfs5lCu23SJr5OP8aYNVXz_6SAH5GTrVEEGZXfy0BjCraV6OztG2Z5UO9TkmhzNu0exxFm1LeGIJsCdorPybQJW0SA9ACL6G_VF81e_Glz_9PavriKI1PEQ20YIyaFON3_ZcRLyA/w640-h356/yum-update_1024x569.jpg" alt="" width="640" height="356" border="0" data-original-height="569" data-original-width="1024" /></a></code></div>
<p><div align="center">
<!-- ara -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-8410270452001273"
     data-ad-slot="3273349926"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div></p>
<h3><strong>Mendownload Script Squid Auto Installer</strong></h3>
<p>Langkah selanjutnya ialah mendownload script auto install dan menyimpannya di server kita. Perlu dicatat Tutorial install proxy squid ini lebih ditujukan pada pemula yang tidak memerlukan setingan tambahan dan belum begitu mengenal dunia linux secara mendalam sehingga setting masih default.</p>
<p>Namun begitu jika ingin melakukan beberapa perubahan perubahan seperti akses kontrol dll masih bisa dengan cara mengedit script ini terlebih dahulu ..secara default Port yang digunakan adalah Port 3128 oleh karena itu pastikan port tersebut tidak digunakan .Pada terminal ketik perintah berikut</p>
<p><code>wget --no-check-certificate https://codeload.github.com/centminmod/squid-proxy-installer/zip/refs/heads/master</code></p>
<p><div align="center">
<!-- responsiv -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-8410270452001273"
     data-ad-slot="6719527881"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div></p>
<div class="separator" style="clear: both; text-align: center;"><code><a style="margin-left: 1em; margin-right: 1em;" href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgvHrdw4wrvxXbAz_eKtgginmV-L0IPudbEOJDR6u5LctlriAd1EJF00kqtE-api_HM_OG7Ge8dJDktlqQchGqWQgOYepT-c80B0rJhlQqsYkfh_jYXBt4MlW9Ah7WTElm5ampDEyKPqi_94VNeHKatZuKyNhnzlCKPz6n5kQSB4tPm4xgU_U0u36S5fg/s1024/squid-installer-skrip_1024x331.jpg"><img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgvHrdw4wrvxXbAz_eKtgginmV-L0IPudbEOJDR6u5LctlriAd1EJF00kqtE-api_HM_OG7Ge8dJDktlqQchGqWQgOYepT-c80B0rJhlQqsYkfh_jYXBt4MlW9Ah7WTElm5ampDEyKPqi_94VNeHKatZuKyNhnzlCKPz6n5kQSB4tPm4xgU_U0u36S5fg/w640-h206/squid-installer-skrip_1024x331.jpg" alt="" width="640" height="206" border="0" data-original-height="331" data-original-width="1024" /></a></code></div>
<h3>Chmod Script installer squid</h3>
<p>Agar dapat dieksekusi, maka Script harus terlebih dahulu diberikan izin atau dalam bahasa komputer yaitu Chmod. Pada terminal ketik perintah berikut</p>
<p><code>chmod +x spi</code></p>
<div class="separator" style="clear: both; text-align: center;"><code><a style="margin-left: 1em; margin-right: 1em;" href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgcbH06p8pFm84x0uuLsZrhbkuWCcKFgBeO28TxvYiWknRtc2BR7dLaNnU7f7YyjpHBN0Vi_ZN3l_8FDbTSJ9_etYiedwE7mV9ePamM7pmbThhbPkDcuoTc5p_4qQkkOF_sKZKsoNYC3dPplDqCHaJ-GtG_nFpLqGltYPMQcNjNr-NAanrGFkmlkWMKOQ/s1024/instalasi-squid_1024x401.jpg"><img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgcbH06p8pFm84x0uuLsZrhbkuWCcKFgBeO28TxvYiWknRtc2BR7dLaNnU7f7YyjpHBN0Vi_ZN3l_8FDbTSJ9_etYiedwE7mV9ePamM7pmbThhbPkDcuoTc5p_4qQkkOF_sKZKsoNYC3dPplDqCHaJ-GtG_nFpLqGltYPMQcNjNr-NAanrGFkmlkWMKOQ/w640-h250/instalasi-squid_1024x401.jpg" alt="" width="640" height="250" border="0" data-original-height="401" data-original-width="1024" /></a></code></div>
<p><div align="center">
<!-- oktrikresponsi -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-8410270452001273"
     data-ad-slot="6888399955"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div></p>
<h3>Menjalankan Script Installer Squid</h3>
<p>Dan Kemudian kita akan memulai proses Install Squid Proxy secara otomatis namun hal yang harus kita perhatikan selanjutnya ialah mengetahui distro atau Rhel yang digunakan karena Perintah yang akan digunakan pun berbeda sesuai dengan Versi Linux yang anda gunakan.</p>
<p>Seperti yang tertulis diatas saya menggunakan Centos 5 maka Perintah yang saya ketik ialah <code>./spi -rhel5</code> dan jika anda menggunakan centos 6 maka Perintah nya ialah <code>./spi -rhel5</code> begitu seterusnya sesuai Versi os anda dan berikut ini adalah list nya</p>
<blockquote>
<p>Server CentOS 5<br /><code>./spi -rhel5</code></p>
<p>Server CentOS 6<br /><code>./spi -rhel6</code></p>
<p>Server CentOS 7<br /><code>./spi -rhel7</code><br />server Debian 6 atau 7<br /><code>./spi -debian</code></p>
<p>Server Debian 8<br /><code>./spi -jessie</code></p>
<p>Server Ubuntu<br /><code>./spi -ubuntu</code></p>
</blockquote>
<pre>Server Fedora
<code>./spi -fedora</code></pre>
<h3><strong>Memasang Password Pada Squid Proxy</strong></h3>
<p>Setelah berhasil mengeksekusi Script installer tadi pada bagian akhir kita akan dihadapkan pada sebuah opsi untuk memasang Username dan password pada Proxy. Hal ini sangat efektif jika anda tidak ingin untuk mengedit secara manual <code>htpasswd</code> .</p>
<p>Pada Opsi pilihan <code>Your desired username</code>: , isikan dengan user yang anda kehendaki kemudian Tekan Enter pada terminal, setelah itu script akan meminta anda untuk mengisikan password.</p>
<p>Pada opsi <em>New password</em>: isikan dengan password yang anda kehendaki kemudian tekan Enter dan ketik ulang password anda saat konfirmasi</p>
<p>Setelah itu Script secara otomatis akan melakukan instalasi secara otomatis dan melakukan konfigurasi yang dibutuhkan oleh squid proxy secara otomatis dan akan menyimpan konfigurasi tersebut pada folder <code>/etc/squid/squid.conf</code></p>
<p><div align="center">
<!-- responsiv -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-8410270452001273"
     data-ad-slot="6719527881"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div></p>
<div class="separator" style="clear: both; text-align: center;"><code><a style="margin-left: 1em; margin-right: 1em;" href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEggWmcbmKBAngnhrybpFki9ODWAKZ-UV5AQ3I5d9mSxKD-1jwlaTFFNSKzBCPWc0HPtPCqZLgnUECTqtoFJvPRjK0hxerfXrPTx_4wOUTI_Q_OcTs9DvHfipwHfNmwz2KxGh3HSWI_1FeahTe5lrYeTyU_wJmknxx6iaAKSu2m6L_JYEm004g8S4rI5Kg/s1024/pasang-password-pada-proxy_1024x262.jpg"><img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEggWmcbmKBAngnhrybpFki9ODWAKZ-UV5AQ3I5d9mSxKD-1jwlaTFFNSKzBCPWc0HPtPCqZLgnUECTqtoFJvPRjK0hxerfXrPTx_4wOUTI_Q_OcTs9DvHfipwHfNmwz2KxGh3HSWI_1FeahTe5lrYeTyU_wJmknxx6iaAKSu2m6L_JYEm004g8S4rI5Kg/w640-h164/pasang-password-pada-proxy_1024x262.jpg" alt="" width="640" height="164" border="0" data-original-height="262" data-original-width="1024" /></a></code></div>
<p><div align="center">
<!-- ara -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-8410270452001273"
     data-ad-slot="3273349926"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div></p>
<h2>Kesimpulan</h2>
<p>Dan selesai. cara Install Squid Proxy secara gampang bagi para pemula..dan anda bisa langsung menggunakan Proxy tadi dengan port 3128</p>