# Ler todos os arquivos do tipo .csv em uma mesma pasta e retorna esses arquivos unidos
import os
import pandas as pd
import utils_prepared_data as upd
import utils_files as uf
import utils_date as ud
import utils_statistics as us
import utils_graphics as ug
import importlib
import numpy as np

def charge_reload():
    importlib.reload(upd)
    importlib.reload(uf)
    importlib.reload(ud)
    importlib.reload(us)
    importlib.reload(ug)