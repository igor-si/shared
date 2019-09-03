import gzip
import shutil


# Example of how to read a compressed file:
with gzip.open('file.txt.gz', 'rb') as f:
    file_content = f.read()

# Example of how to create a compressed GZIP file:
content = "Lots of content here"
with gzip.open('file.txt.gz', 'wb') as f:
    f.write(content)

# Example of how to GZIP compress an existing file:
with open('file.txt', 'rb') as f_in, gzip.open('file.txt.gz', 'wb') as f_out:
    shutil.copyfileobj(f_in, f_out)