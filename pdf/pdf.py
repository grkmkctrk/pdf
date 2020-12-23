
import img2pdf
import os

dirname = r"path"
with open("name.pdf","wb") as f:
	imgs = []
	for fname in os.listdir(dirname):
		if not fname.endswith(".png"):
			continue
		path = os.path.join(dirname, fname)
		if os.path.isdir(path):
			continue
		imgs.append(path)
	f.write(img2pdf.convert(imgs))