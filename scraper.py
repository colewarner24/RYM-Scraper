from selenium import webdriver # type: ignore
from selenium.common.exceptions import NoSuchElementException # type: ignore
from selenium.webdriver.common.by import By # type: ignore
import json
import time

PAGE = 0
RYM_BASE_URl = "https://rateyourmusic.com/charts/top/album/all-time"
RYM_CLASS_WRAPPER = "page_section_charts_item_wrapper  anchor"
RYM_CLASS_WRAPPER_ALBUM = "page_charts_section_charts"
CLASS_ALBUM_SHORTCUT = "album shortcut"
CLASS_ARTIST = "page_charts_section_charts_item_title"
CLASS_TITLE = "page_charts_section_charts_item_credited_links_primary"
CLASS_DATE = "page_charts_section_charts_item_date"
CLASS_GENRES_PRIMARY = "page_charts_section_charts_item_genres_primary"
CLASS_GENRES_SECONDARY = "page_charts_section_charts_item_genres_secondary"
CLASS_RATING = "page_charts_section_charts_item_stats"
CLASS_TOTAL_RATINGS = "page_charts_section_charts_item_details_ratings"
CLASS_TOTAL_REVIEWS = "page_charts_section_charts_item_details_reviews"
CLASS_GENRE_DISCRIPTORS = "page_charts_section_charts_item_genre_descriptors"
CLASS_MEDIA_LINKS = "page_charts_section_charts_item_media_links"
CLASS_SPOTIFY_LINK = "ui_media_link_btn ui_media_link_btn_youtube"
ALBUM_PAGE_LEN = 40
PAGE_LEN = 10#125

class Album:
    def __init__(self, album_web_element) -> None:
        self.artist = album_web_element.find_element(By.XPATH, f".//*[@class='{CLASS_ARTIST}']").text
        self.title = album_web_element.find_element(By.XPATH, f".//*[@class='{CLASS_TITLE}']").text
        self.date = album_web_element.find_element(By.XPATH, f".//*[@class='{CLASS_DATE}']").text
        self.genres_primary = album_web_element.find_element(By.XPATH, f".//*[@class='{CLASS_GENRES_PRIMARY}']").text
        try:
            self.genres_secondary = album_web_element.find_element(By.XPATH, f".//*[@class='{CLASS_GENRES_SECONDARY}']").text
        except NoSuchElementException:
            self.genres_secondary = ""
        self.rating = album_web_element.find_element(By.XPATH, f".//*[@class='{CLASS_RATING}']").text
        self.total_ratings = album_web_element.find_element(By.XPATH, f".//*[@class='{CLASS_TOTAL_RATINGS}']").text
        self.total_reviews = album_web_element.find_element(By.XPATH, f".//*[@class='{CLASS_TOTAL_REVIEWS}']").text
        self.genre_descriptors = album_web_element.find_element(By.XPATH, f".//*[@class='{CLASS_GENRE_DISCRIPTORS}']").text
        #media_link_button_container_charts_
        links = json.loads(album_web_element.find_element(By.XPATH, f".//*[starts-with(@id, \"media_link_button_container_charts_\")]").get_attribute("data-links"))
        self.set_links(links)
        #self.spotify_link = links_el.find_element(By.XPATH, f".//*[@class='{CLASS_SPOTIFY_LINK}']").get_attribute("href")
    
    def set_links(self, link_dic):
        if "spotify" in link_dic:
            self.spotify_id = list(link_dic['spotify'].keys())[0]
        else:
            self.spotify_id = None
        if "applemusic" in link_dic:
            self.apple_id = list(link_dic['applemusic'].keys())[0]
        else:
            self.apple_id = None
        if "soundcloud" in link_dic:
            self.soundcloud_id = list(link_dic['soundcloud'].keys())[0]
        else:
            self.soundcloud_id = None
        if "bandcamp" in link_dic:
            self.bandcamp_id = list(link_dic['bandcamp'].keys())[0]
        else:
            self.bandcamp_id = None
        if "youtube" in link_dic:
            self.youtube_id = list(link_dic['youtube'].keys())[0]
        else:
            self.youtube_id = None
            
    def __str__(self) -> str:
        return f"Artist: {self.artist}\nTitle: {self.title}\nDate: {self.date}\nGenres: {self.genres_primary}, {self.genres_secondary}\nRating: {self.rating}\nTotal ratings: {self.total_ratings}\nTotal reviews: {self.total_reviews}\nGenre descriptors: {self.genre_descriptors}\n Spotify id: {self.spotify_id}"

def main():
    
    driver = webdriver.Firefox()
    
    for page_num in range(PAGE_LEN): #PAGE_LEN:
        driver.get(RYM_BASE_URl + "/" + str(page_num + 1))
        for i in range(ALBUM_PAGE_LEN - 1):
            try:
                album_el = driver.find_element(By.XPATH, f"//*[@id='pos{i+1}']")
            except NoSuchElementException:
                break
            album = Album(album_el)
            print()
            print(album)
            print()
        time.sleep(10)
    print(f"Scraper done scraping at page {page_num}, album {i}")

    driver.quit()

if __name__ == "__main__":
    main()
