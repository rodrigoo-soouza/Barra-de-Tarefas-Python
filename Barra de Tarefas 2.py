from tqdm import tqdm
import time

lista = [1, 2, 3, 10, 15]

for item in tqdm(lista):
    time.sleep(1)