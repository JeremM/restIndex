import logging
import gzip
import shutil


def download_dropbox_file(data_dir, filename):
    url = f"https://www.dropbox.com/s/duv704waqjp3tu1/{filename}?dl=1"
    import urllib.request
    u = urllib.request.urlopen(url)
    logging.info("Reading dropbox file")
    data = u.read()
    u.close()
    with open(data_dir + filename, "wb") as f:
        logging.info("Writing dropbox file")
        f.write(data)
        logging.info("Done")


def initrawfiles():
    gz_filename = "hn_logs.tsv.gz"
    data_dir = "data_dir/"
    gz_filepath = data_dir + gz_filename
    import os.path
    if not os.path.isfile(gz_filepath):
        logging.info("archive file not present. downloading")
        download_dropbox_file(data_dir, gz_filename)
    else:
        logging.info("gz file ok")

    tsv_filepath = gz_filepath[:-3]
    if not os.path.isfile(tsv_filepath):
        logging.info("tsv file not present. extracting")
        with gzip.open(gz_filepath, 'rb') as f_in:
            with open(tsv_filepath, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        logging.info("tsv file extracted")
    else:
        logging.info("tsv file ok")
