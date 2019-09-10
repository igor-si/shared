import zipfile
import os 


def zipDir(dirPath, zipPath):
    zipf = zipfile.ZipFile(zipPath , mode='w')
    lenDirPath = len(dirPath)
    for root, _ , files in os.walk(dirPath):
        for file in files:
            filePath = os.path.join(root, file)
            zipf.write(filePath , filePath[lenDirPath :] )
    zipf.close()
#end zipDir

def zipDir2():
	def add_zip_flat(zip, filename):
	    dir, base_filename = os.path.split(filename)
	    os.chdir(dir)
	    zip.write(base_filename)

	zip = zipfile.ZipFile(buffer, 'w')
	add_zip_flat(zip, first_path)
	add_zip_flat(zip, second_path)
	zip.close()