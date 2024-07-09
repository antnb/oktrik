with open('input.txt', 'r', encoding='utf-8') as input_file, \
     open('output.txt', 'r', encoding='utf-8') as output_file, \
     open('redirect_script.js', 'w', encoding='utf-8') as output_script:

    input_urls = input_file.readlines()
    output_urls = output_file.readlines()

    # Memastikan panjang kedua file sama
    if len(input_urls) != len(output_urls):
        print("Jumlah baris pada input.txt dan output.txt tidak sama!")
    else:
        output_script.write("// Generated redirect rules\n\n")

        for input_url, output_url in zip(input_urls, output_urls):
            old_url = input_url.strip()
            new_url = output_url.strip()

            # Membuat kode redirect untuk setiap URL
            output_script.write(f"if (url.pathname === '{old_url}') {{\n")
            output_script.write(f"    // Redirect '{old_url}' to '{new_url}' with a 301 status code\n")
            output_script.write(f"    return Response.redirect('{new_url}', 301)\n")
            output_script.write("}\n\n")

print("Script untuk redirect telah berhasil dibuat dalam file redirect_script.js")
