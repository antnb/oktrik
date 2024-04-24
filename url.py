import os
import hashlib

# Path ke folder yang menyimpan file markdown
posts_folder = '_posts'

# Fungsi untuk mengubah nama file
def rename_file(file_path, new_file_name):
    directory = os.path.dirname(file_path)
    new_file_path = os.path.join(directory, new_file_name)
    os.rename(file_path, new_file_path)

# Fungsi untuk membuat hash unik
def unique_hash(title):
    # Mengambil 4 karakter pertama dari hash MD5
    hash_object = hashlib.md5(title.encode())
    hash_hex = hash_object.hexdigest()
    return hash_hex[:4]

# Fungsi untuk memproses file markdown
def process_file(file_path):
    # Ambil nama file
    file_name = os.path.basename(file_path)
    
    # Pisahkan tanggal dan judul dari nama file
    parts = file_name.split('-', 3)
    date = parts[0] + '-' + parts[1] + '-' + parts[2]
    title = parts[3]
    
    # Hilangkan ekstensi file .md
    title = title.rsplit('.', 1)[0]
    
    # Potong judul menjadi 3 kata
    title_words = title.split('-')
    short_title = '-'.join(title_words[:3])
    
    # Buat nomor urut unik dari hash judul
    hash_number = unique_hash(short_title)
    
    # Buat nama file baru dengan nomor urut unik
    new_file_name = f'{date}-{hash_number}-{short_title}.md'
    
    # Ganti nama file
    rename_file(file_path, new_file_name)

# Proses semua file markdown di folder _posts
def process_posts():
    for file_name in os.listdir(posts_folder):
        if file_name.endswith('.md'):
            file_path = os.path.join(posts_folder, file_name)
            process_file(file_path)

# Jalankan fungsi untuk memproses semua file markdown
process_posts()
