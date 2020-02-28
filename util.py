import os
import requests
import zipfile
import io
import shutil
import tarfile
from loader import *


def download_TIMIT():
    if os.path.isdir('dataset/TIMIT'):
        logger.info("TIMIT already exists")
    else:
        logger.info("TIMIT downloading")
        r = requests.get('https://ndownloader.figshare.com/files/10256148')
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall('dataset')
        shutil.move('dataset/data/lisa/data/timit/raw/TIMIT', 'dataset')
        shutil.rmtree('dataset/data')


def download_Korean_DB():
    def download_file_from_google_drive(id, destination):
        def get_confirm_token(response):
            for key, value in response.cookies.items():
                logger.info("{} {}".format(key, value))
                if key.startswith('download_warning'):
                    return value

            return None

        def save_response_content(response, destination):
            CHUNK_SIZE = 32768

            with open(destination, "wb") as f:
                for chunk in response.iter_content(CHUNK_SIZE):
                    if chunk:  # filter out keep-alive new chunks
                        logger.info(chunk)
                        f.write(chunk)

        URL = "https://docs.google.com/uc?export=download"

        session = requests.Session()

        response = session.get(URL, params={'id': id}, stream=True)
        token = get_confirm_token(response)

        if token:
            params = {'id': id, 'confirm': token}
            response = session.get(URL, params=params, stream=True)

        save_response_content(response, destination)

    if os.path.isdir('dataset/train'):
        logger.info("Korean DB already exists")
    else:
        logger.info("Korean DB downloading")
        download_file_from_google_drive('1UOspFSTJ2w0wsENIeD6Ilcy5dd4NTsDV', 'dataset/train.tar')
        tar = tarfile.open('dataset/train.tar')
        tar.extractall('dataset')
