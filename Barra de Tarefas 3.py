from tqdm import tqdm
import time

with tqdm(total=100) as barra_progresso:
    for i in range(10):
        time.sleep(1)
        barra_progresso.update(10)
