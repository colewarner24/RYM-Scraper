from selenium import webdriver
from selenium.webdriver.common.by import By
import json

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
PAGE_LEN = 125

class Album:
    def __init__(self, album_web_element) -> None:
        self.artist = album_web_element.find_element(By.XPATH, f".//*[@class='{CLASS_ARTIST}']").text
        self.title = album_web_element.find_element(By.XPATH, f".//*[@class='{CLASS_TITLE}']").text
        self.date = album_web_element.find_element(By.XPATH, f".//*[@class='{CLASS_DATE}']").text
        self.genres_primary = album_web_element.find_element(By.XPATH, f".//*[@class='{CLASS_GENRES_PRIMARY}']").text
        self.genres_secondary = album_web_element.find_element(By.XPATH, f".//*[@class='{CLASS_GENRES_SECONDARY}']").text
        self.rating = album_web_element.find_element(By.XPATH, f".//*[@class='{CLASS_RATING}']").text
        self.total_ratings = album_web_element.find_element(By.XPATH, f".//*[@class='{CLASS_TOTAL_RATINGS}']").text
        self.total_reviews = album_web_element.find_element(By.XPATH, f".//*[@class='{CLASS_TOTAL_REVIEWS}']").text
        self.genre_descriptors = album_web_element.find_element(By.XPATH, f".//*[@class='{CLASS_GENRE_DISCRIPTORS}']").text
        #media_link_button_container_charts_
        self.spotify_link = json.loads(album_web_element.find_element(By.XPATH, f".//*[starts-with(@id, \"media_link_button_container_charts_\")]").get_attribute("data-links"))
        print(self.spotify_link['spotify'])
        #self.spotify_link = links_el.find_element(By.XPATH, f".//*[@class='{CLASS_SPOTIFY_LINK}']").get_attribute("href")
    
    def __str__(self) -> str:
        return f"Artist: {self.artist}\nTitle: {self.title}\nDate: {self.date}\nGenres: {self.genres_primary}, {self.genres_secondary}\nRating: {self.rating}\nTotal ratings: {self.total_ratings}\nTotal reviews: {self.total_reviews}\nGenre descriptors: {self.genre_descriptors}\nSpotify link: {self.spotify_link}"

def main():
    
    driver = webdriver.Firefox()

    driver.get(RYM_BASE_URl)
    
    id = 1
    
    for page_num in range(1): #PAGE_LEN:
        for i in range(5):
            album_el = driver.find_element(By.XPATH, f"//*[@id='pos{id}']")
            album = Album(album_el)
            print()
            print(album)
            print()
            id += 1

    driver.quit()

if __name__ == "__main__":
    main()
