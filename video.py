import subprocess
import sys
from datetime import datetime
import re
import os
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    from tqdm import tqdm
except:
    install('-e git+https://github.com/tqdm/tqdm.git@master#egg=tqdm')
    from tqdm import tqdm
try:
    import requests 
except:
    install('requests==2.20.1')
    import requests


def main():
    try:
        print("\n\nThis video downloader must only be used for private purposes and Copyright Free Content downloading. Any commercial or illegal use of this video downloader is strictly forbidden. By using this video downloader you agree that you are liable for which content you download and what you do with it. \n")
        selector=input("Would you like to continue? Y/N  ")
        if (selector=='' or selector[0].lower() !='y'):
            exit()

        url = input("\nEnter the URL of the video that you will try to download: ")
        html = requests.get(url).content.decode('utf-8')
    
        print(f"\nDownloading the video in HD quality... \n")
        video_url = re.search(rf'{"hd"}_src:"(.+?)"', html).group(1)

        file_size_request = requests.get(video_url, stream=True)

        file_size = int(file_size_request.headers['Content-Length'])
        block_size = 1024
        filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
        t = tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
        with open(filename + '.mp4', 'wb') as f:
            for data in file_size_request.iter_content(block_size):
                t.update(len(data))
                f.write(data)
        t.close()
        print("\nVideo downloaded successfully.")

    except(KeyboardInterrupt):
        print("\nProgram Interrupted")

main()
