# -*- coding: utf-8 -*-

import os.path
import urllib.request


def baixar_pdf(url, local, nome):
    urllib.request.urlretrieve(
        url,
        os.path.join(local, nome)
    )


if __name__ == "__main__":
    baixar_pdf(
        url='https://www.scielo.br/j/ci/a/ntFtbXDD7c4KVYrT6WzMyVf/?lang=pt&format=pdf',
        local=os.getcwd(),
        nome='teste.pdf'
    )
