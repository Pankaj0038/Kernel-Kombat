def decombine_file(combined_file_path, file1_size, output_file1_path, output_file2_path):
    try:
        with open(combined_file_path, 'rb') as combined_file:
            combined_bytes = combined_file.read()

        bytes_file1 = combined_bytes[:file1_size]
        bytes_file2 = combined_bytes[file1_size:]

        with open(output_file1_path, 'wb') as output_file1:
            output_file1.write(bytes_file1)
            print("First file successfully written to", output_file1_path)

        with open(output_file2_path, 'wb') as output_file2:
            output_file2.write(bytes_file2)
            print("Second file successfully written to", output_file2_path)

    except FileNotFoundError:
        print("Combined file not found.")


combined_file_path = "combined_file.gif"   # /path/to/bruh.gif
file1_size = 475694  
output_file1_path = "decombined_file1.gif"
output_file2_path = "decombined_file2.gif"

decombine_file(combined_file_path, file1_size, output_file1_path, output_file2_path)
