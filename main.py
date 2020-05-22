import time
from enum import IntEnum
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement

class ColorIndex(IntEnum):
    Magenta = 0
    Cyan = 1
    Yellow = 2
    Black = 3

class HomePage(object):
    
    def __init__(self, driver):
        self.driver: Chrome = driver

    def getMagentaStatus(self) -> str:
        return self._getInkStatus( ColorIndex.Magenta)

    def getCyanStatus(self) -> str:
        return self._getInkStatus( ColorIndex.Cyan)

    def getYellowStatus(self) -> str:
        return self._getInkStatus( ColorIndex.Yellow)

    def getBlackStatus(self) -> str:
        return self._getInkStatus( ColorIndex.Black)
    
    def _getInkStatus(self, colorIndex: ColorIndex) -> str:
        inkLevelGauge: WebElement = self.driver.find_element_by_id("inkLevelGauge")
        inkLevelImages: WebElement = inkLevelGauge.find_elements_by_class_name("ink-inkIconImgSize")
        inkLevelImage: WebElement = inkLevelImages[int(colorIndex)]
        if "normal" in inkLevelImage.get_attribute("src"):
            return "normal"
        else:
            return "low"

def main():
    options = Options()
    #options.add_argument("--window-size=1920,1080")
    #options.add_argument("--start-maximized")
    #options.add_argument("--headless")
    #options.add_argument("--log-level=3")  # fatal
    #options.add_argument('--disable-gpu')
    driver = Chrome(options=options)
    driver.get("http://hpd24484/")
    
    print("Loading Home Page...")
    time.sleep(5)
    homePage: HomePage = HomePage(driver)
    
    print("Parsing Home Page...")
    magentaStatus = homePage.getMagentaStatus()
    print(f'Magenta status: {magentaStatus}')

    cyanStatus = homePage.getCyanStatus()
    print(f'Cyan status: {cyanStatus}')

    yellowStatus = homePage.getYellowStatus()
    print(f'Yellow status: {yellowStatus}')

    blackStatus = homePage.getBlackStatus()
    print(f'Black status: {blackStatus}')

    driver.quit()
    exit(0)

if __name__ == "__main__":
    main()