import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
from p_tqdm import p_map
import time


def find_stuff(i):
    
    with open('output.txt', 'a') as f:
    
        ID = 47200 + i

        URL = "https://cosylab.iiitd.edu.in/recipedb/search_recipeInfo/" + str(ID)
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")

        for i in soup.select("td > a"):
            f.write(i['href'] + '\n')
            f.write(i.text + '\n')
    
if __name__ == '__main__':
    
    # start = time.time()
    
    # with Pool(processes=8) as pool:
    #     pool.map(find_stuff, range(20))
        
    p_map(find_stuff, range(73394, 100000))
        
    # end = time.time()
    # print(end - start)

