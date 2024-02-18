import os
import threading

import requests
import bs4

os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd


def download_xkcd(start_comic, end_comic):
    for url_number in range(start_comic, end_comic):
        # Download the page.
        print(f'Downloading page https://xkcd.com/{url_number}...')
        res = requests.get(f'https://xkcd.com/{url_number}')
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        # Find the URL of the comic image.
        comic_elem = soup.select('#comic img')
        if comic_elem is []:
            print('Could not find comic image.')
        else:
            comic_url = comic_elem[0].get('src')

            # Download the image.
            print(f'Downloading image {comic_url}...')
            res = requests.get('https:' + comic_url)
            res.raise_for_status()

            # Save the image to ./xkcd.
            image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
            image_file.close()


if __name__ == '__main__':
    download_threads = []
    for i in range(0, 140, 10):
        start = i
        end = start + 9

        if not start:
            start = 1

        download_thread = threading.Thread(target=download_xkcd, args=(start, end))
        download_threads.append(download_thread)
        download_thread.start()

    # Wait for all threads to end.
    for download_thread in download_threads:
        download_thread.join()
    print("Done.")
