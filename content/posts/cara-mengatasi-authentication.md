---
title: "Memahami dan Mengatasi Error RDP: An Authentication Error Has Occurred"
date: 2024-07-09T14:56:00.001+07:00
image: /images/rdp.jpg
description: "Solusi komprehensif untuk error RDP terkait dengan perubahan keamanan pada CredSSP."
categories: ["Teknologi", "Keamanan"]
tags: ["RDP", "CredSSP", "Windows"]
---

Dalam era digital yang semakin terhubung, Remote Desktop Protocol (RDP) menjadi tulang punggung bagi banyak profesional IT dan administrator sistem. Kemampuan untuk mengelola server Windows dari jarak jauh telah mengubah cara kita bekerja. Namun, sejak Mei 2018, banyak pengguna menghadapi kendala serius saat mencoba melakukan koneksi RDP, dengan pesan error yang membingungkan:

**"An authentication error has occurred. The function requested is not supported"**

Error ini bukan hanya mengganggu produktivitas, tetapi juga menimbulkan pertanyaan serius tentang keamanan dan manajemen sistem jarak jauh. Artikel ini akan membedah masalah ini secara menyeluruh, memberikan solusi komprehensif, dan menyajikan wawasan mendalam tentang implikasi keamanan yang lebih luas.

## Memahami RDP dan Evolusinya

### Apa itu RDP?

Remote Desktop Protocol (RDP), dikembangkan oleh Microsoft, adalah protokol proprietary yang memungkinkan pengguna untuk terhubung ke komputer lain melalui koneksi jaringan. RDP menyediakan antarmuka grafis pengguna (GUI) yang memungkinkan interaksi dengan komputer jarak jauh seolah-olah Anda sedang duduk di depannya.

Fitur utama RDP meliputi:

- Transmisi input keyboard dan mouse

- Transmisi tampilan layar

- Enkripsi data untuk keamanan

- Dukungan untuk berbagai jenis perangkat dan resolusi layar

RDP biasanya menggunakan port 3389 untuk koneksi TCP dan UDP, meskipun port ini dapat diubah untuk alasan keamanan.

### Evolusi RDP dan Peningkatan Keamanan

Sejak diperkenalkan pertama kali dengan Windows NT 4.0 Terminal Server Edition, RDP telah mengalami banyak perbaikan:

1\. Windows XP: Pengenalan enkripsi 128-bit

2\. Windows Vista: Penambahan Network Level Authentication (NLA)

3\. Windows 7: Peningkatan dukungan multimedia

4\. Windows 8/10: Optimalisasi performa dan keamanan lebih lanjut

Meskipun demikian, seperti banyak teknologi lainnya, RDP tidak luput dari celah keamanan.

## CVE-2018-0886: Titik Balik dalam Keamanan RDP

### Memahami Celah Keamanan CredSSP

{{< figure src="/images/credssprdp.png" alt="Celah Keamanan CredSSP" >}}

Pada Maret 2018, Microsoft mengumumkan adanya celah keamanan kritis pada Credential Security Support Provider protocol (CredSSP). Celah ini, yang kemudian dikenal dengan kode CVE-2018-0886, memiliki implikasi serius:

1\. **Serangan Man-in-the-Middle**: Penyerang dapat menempatkan diri antara klien dan server.

2\. **Eksekusi Kode Jarak Jauh**: Memungkinkan penyerang menjalankan kode berbahaya pada sistem target.

3\. **Pencurian Kredensial**: Potensi pengambilalihan akun administrator.

### Respons Microsoft

Microsoft dengan cepat merilis patch untuk mengatasi celah ini. Namun, implementasi patch ini mengakibatkan perubahan signifikan dalam cara RDP beroperasi:

1\. Perubahan Default Setting: Dari "Vulnerable" menjadi "Mitigated"

2\. Ketidakcocokan Versi: Klien yang sudah dipatched tidak dapat berkomunikasi dengan server yang belum dipatched, dan sebaliknya.

3\. Penerapan Kebijakan Grup: Perubahan pada Group Policy untuk mengatur perilaku CredSSP.

## Anatomi Error: "An authentication error has occurred. The function requested is not supported"

Error ini muncul sebagai hasil langsung dari ketidaksesuaian antara sistem yang telah dipatched dan yang belum. Mari kita bedah komponen-komponennya:

1\. **"An authentication error has occurred"**: Menunjukkan kegagalan dalam proses autentikasi.

2\. **"The function requested is not supported"**: Mengindikasikan ketidakcocokan protokol atau versi.

Penyebab utama error ini adalah:

- Klien yang diperbarui mencoba terhubung ke server yang belum diperbarui.

- Server yang diperbarui menolak koneksi dari klien yang belum diperbarui.

- Pengaturan Group Policy yang tidak sesuai antara klien dan server.

## Solusi Komprehensif

### 1. Pembaruan Sistem

Langkah pertama dan terpenting adalah memastikan baik klien maupun server telah diperbarui dengan patch terbaru:

- Untuk Windows 10 dan Server 2016: KB4103727

- Untuk Windows 7 dan Server 2008 R2: KB4103718

- Untuk Windows 8.1 dan Server 2012 R2: KB4103725

Perintah PowerShell untuk memeriksa status patch:

```powershell

Get-HotFix | Where-Object {$\_.HotFixID -eq "KB4103727"}

```

### 2. Konfigurasi Group Policy

Jika pembaruan tidak memungkinkan, Anda dapat mengubah pengaturan Group Policy:

1\. Buka Group Policy Editor (gpedit.msc)

2\. Navigasi ke: Computer Configuration > Administrative Templates > System > Credentials Delegation

3\. Ubah setting "Encryption Oracle Remediation" ke "Vulnerable"

Namun, perlu diingat bahwa ini mengurangi tingkat keamanan dan harus dianggap sebagai solusi sementara.

### 3. Verifikasi Pengaturan Firewall

Pastikan firewall tidak memblokir koneksi RDP:

1\. Buka Windows Defender Firewall dengan Advanced Security

2\. Verifikasi bahwa aturan "Remote Desktop - User Mode (TCP-In)" diaktifkan

3\. Jika menggunakan firewall pihak ketiga, konsultasikan dokumentasinya untuk konfigurasi yang tepat

### 4. Pemeriksaan Log Event

Windows Event Log dapat memberikan informasi berharga:

1\. Buka Event Viewer

2\. Navigasi ke: Windows Logs > Security

3\. Cari event dengan ID 4624 (login berhasil) atau 4625 (login gagal)

## Alternatif RDP dan Perbandingan

Jika masalah RDP persisten, pertimbangkan alternatif berikut:

| Fitur | RDP | TeamViewer | AnyDesk | VNC |
|:------|:----|:-----------|:--------|:----|
| Protokol | Proprietary | Proprietary | Proprietary | Open-source |
| Enkripsi | AES 256-bit | AES 256-bit | AES 256-bit | Bervariasi |
| Firewall-friendly | Tidak | Ya | Ya | Tidak |
| Lisensi | Included with Windows | Berbayar untuk komersial | Freemium | Gratis/Berbayar |
| Cross-platform | Terbatas | Ya | Ya | Ya |
| Performa | Sangat baik | Baik | Sangat baik | Bervariasi |
| Kemudahan penggunaan | Mudah | Sangat mudah | Mudah | Sedang |

### TeamViewer

TeamViewer menawarkan solusi remote access yang kuat dengan fitur tambahan seperti transfer file dan meeting online. Namun, untuk penggunaan komersial, biayanya bisa cukup tinggi.

### AnyDesk

AnyDesk terkenal dengan kecepatan koneksinya dan footprint yang kecil. Ini menjadi pilihan populer untuk support teknis jarak jauh.

### VNC (Virtual Network Computing)

VNC adalah protokol open-source yang memiliki berbagai implementasi. TightVNC dan UltraVNC adalah contoh populer yang gratis dan open-source.

## Langkah-langkah Pencegahan dan Keamanan Lanjutan

Untuk meningkatkan keamanan RDP secara keseluruhan:

1\. **Implementasi VPN**: Gunakan Virtual Private Network untuk mengenkripsi seluruh koneksi.

Contoh konfigurasi OpenVPN di Linux

```bash
# bash code
sudo openvpn --config /path/to/config.ovpn
```

2\. **Autentikasi Dua Faktor (2FA)**: Integrasikan 2FA dengan RDP menggunakan solusi seperti Duo Security atau Azure Multi-Factor Authentication.

3\. **Network Level Authentication (NLA)**: Aktifkan NLA untuk memastikan autentikasi sebelum membuat koneksi penuh.


PowerShell command untuk mengaktifkan NLA

```PowerShell
# PowerShell code
Set-ItemProperty -Path 'HKLM:\\System\\CurrentControlSet\\Control\\Terminal Server\\WinStations\\RDP-Tcp' -name "UserAuthentication" -Value 1
```

4\. **Pembatasan IP**: Gunakan Windows Firewall untuk membatasi akses RDP hanya dari IP tertentu.

5\. **Penggunaan Port Non-standar**: Ubah port default RDP (3389) ke port yang tidak standar.

Registry edit untuk mengubah port RDP

```cmd

REG ADD "HKLM\\System\\CurrentControlSet\\Control\\Terminal Server\\WinStations\\RDP-Tcp" /v PortNumber /t REG\_DWORD /d 3390

```

6\. **Pemantauan Aktif**: Gunakan tools seperti Microsoft Advanced Threat Analytics untuk memantau aktivitas RDP yang mencurigakan.

## Implikasi untuk Lingkungan Enterprise

Dalam skala enterprise, masalah RDP dan keamanannya memiliki implikasi yang lebih luas:

1\. **Manajemen Patch Terpusat**: Gunakan solusi seperti Windows Server Update Services (WSUS) atau System Center Configuration Manager (SCCM) untuk manajemen patch yang efisien.

2\. **Pengujian Kompatibilitas**: Lakukan pengujian menyeluruh sebelum menerapkan patch di lingkungan produksi.

```powershell

PowerShell script untuk deployment patch terkontrol

$computers = Get-Content "C:\\computerlist.txt"

foreach ($computer in $computers) {

Invoke-Command -ComputerName $computer -ScriptBlock {

Install-WindowsUpdate -AcceptAll -AutoReboot

}

}

```

3\. **Strategi Rollback**: Siapkan prosedur untuk mengembalikan perubahan jika terjadi masalah.

4\. **Komunikasi dengan Pengguna**: Informasikan jadwal pembaruan dan potensi downtime kepada pengguna.

5\. **Audit Keamanan Berkala**: Lakukan audit keamanan RDP secara rutin menggunakan tools seperti Nessus atau OpenVAS.

## Perkembangan Terbaru dalam Keamanan RDP

Microsoft terus meningkatkan keamanan RDP:

1\. **Windows Defender Remote Credential Guard**: Mencegah pencurian kredensial dengan memisahkan proses autentikasi.

2\. **Azure Security Center**: Integrasi dengan Azure untuk pemantauan keamanan yang lebih baik.

3\. **Windows Virtual Desktop**: Solusi desktop virtual berbasis cloud yang menawarkan keamanan tingkat lanjut.

## Monitoring dan Logging

Pemantauan proaktif sangat penting:

1\. **Windows Event Log**: Fokus pada Event ID terkait RDP:

- 4624: Successful logon

- 4625: Failed logon attempt

- 4648: Explicit credential logon

2\. **SIEM Integration**: Gunakan Security Information and Event Management (SIEM) seperti Splunk atau ELK Stack untuk analisis log yang lebih mendalam.

```

# Contoh query Splunk untuk aktivitas RDP mencurigakan

index=windows sourcetype=WinEventLog:Security EventCode=4624 LogonType=10 | stats count by src\_ip

```

3\. **Custom PowerShell Scripts**: Buat script untuk memantau aktivitas RDP secara real-time.

```powershell

# PowerShell script untuk memantau koneksi RDP aktif

Get-WmiObject -Class Win32\_LogonSession | Where-Object {$\_.LogonType -eq 10} | ForEach-Object {

$username = $\_.GetRelated("Win32\_Account").Name

$sourceIP = (Get-WmiObject -Class Win32\_NetworkAdapterConfiguration | Where-Object {$\_.IPEnabled -eq $true}).IPAddress\[0\]

Write-Output "Active RDP Session: User=$username, Source IP=$sourceIP"

}

```

## Aspek Hukum dan Kepatuhan

Penggunaan RDP harus mempertimbangkan berbagai standar kepatuhan:

1\. **HIPAA (Health Insurance Portability and Accountability Act)**: Untuk industri kesehatan di AS, enkripsi end-to-end adalah keharusan.

2\. **PCI DSS (Payment Card Industry Data Security Standard)**: Untuk industri yang menangani data kartu kredit, pemantauan akses jarak jauh dan penggunaan firewall adalah wajib.

3\. **GDPR (General Data Protection Regulation)**: Untuk entitas yang menangani data warga Uni Eropa, keamanan data dan notifikasi pelanggaran adalah kunci.

4\. **SOC 2 (Service Organization Control 2)**: Standar untuk keamanan, ketersediaan, dan privasi data pelanggan.

Implementasi praktis:

- Gunakan enkripsi tingkat tinggi (minimal AES 256-bit)

- Terapkan kontrol akses yang ketat

- Lakukan audit keamanan secara berkala

- Dokumentasikan semua kebijakan dan prosedur keamanan

## Otomatisasi Pembaruan: Pro dan Kontra

### Pro:

1\. Keamanan selalu up-to-date

2\. Mengurangi beban administrasi

3\. Respons cepat terhadap ancaman baru

### Kontra:

1\. Risiko kompatibilitas dengan aplikasi lain

2\. Potensi downtime yang tidak direncanakan

3\. Kurangnya kontrol atas waktu pembaruan

Untuk menyeimbangkan pro dan kontra:

1\. Gunakan Windows Server Update Services (WSUS) untuk kontrol lebih baik

2\. Terapkan pembaruan secara bertahap, dimulai dari lingkungan pengujian

3\. Siapkan prosedur rollback untuk situasi darurat

## Kesimpulan

Error "An authentication error has occurred. The function requested is not supported" pada RDP adalah manifestasi dari upaya Microsoft untuk meningkatkan keamanan. Meskipun dapat mengganggu operasional jangka pendek, ini menekankan pentingnya tetap up-to-date dengan patch keamanan dan memiliki strategi manajemen sistem yang komprehensif.

Dengan memahami akar permasalahan, menerapkan solusi yang tepat, dan mengadopsi praktik keamanan terbaik, administrator IT dapat mengelola koneksi remote dengan lebih efektif dan aman. Penting untuk terus mengikuti perkembangan teknologi dan ancaman keamanan, serta beradaptasi dengan cepat untuk melindungi aset digital organisasi.