import sys
import os
import urllib.request
import zipfile


def main(argv):
	if argv:
		print('ok')
		#url = 'https://wordpress.org/latest.zip'
		#path = os.getcwd()
		#zipfilp = path + '\\' + 'latest.zip'
		#urllib.request.urlretrieve(url, zipfilp)
		#with zipfile.ZipFile(zipfilp, 'r') as zip_ref:
		#	zip_ref.extractall(path)
		#src = path + "\\wordpress"
		#dst = path + "\\" + argv[0]
		#os.rename(src, dst)
		#os.remove(zipfilp)
		try:
			value = argv[3]
		except IndexError:
			value = None  # no 4th index

if __name__ == "__main__":
   main(sys.argv[1:])


