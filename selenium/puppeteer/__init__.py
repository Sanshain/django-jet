import asyncio
from pyppeteer import launch

# class Browser:
#     engine = None
#
#     def __init__(self, *args, **kwargs):
#
#         asyncio.get_event_loop().run_until_complete(self.init())
#
#     async def init(self):
#         self.engine = await launch()
from pyppeteer.element_handle import ElementHandle


async def run_puppetter():
    browser = await launch()

    page = await browser.newPage()
    await page.setViewport({'width': 1200, 'height': 800})

    r = await page.goto('http://vedmark.ru')
    await page.screenshot({'path': 'example.png'})
    dimensions = await page.evaluate('''() => {
        return {
            width: document.documentElement.clientWidth,
            height: document.documentElement.clientHeight,
            deviceScaleFactor: window.devicePixelRatio,
        }
    }''')
    print(dimensions)

    # page.querySelector()
    title = await page.title()
    print(title)

    p = await page.evaluate("() => document.querySelectorAll('a')[7].innerText")
    print(p)
    links = await page.querySelectorAll('a')
    link: ElementHandle = await page.querySelector('a')
    await links[7].click()
    await page.waitForNavigation()

    # move = await page.evaluate("() => document.querySelectorAll('a')[7].click()")
    # print(move)

    # error:
    title = await page.title()
    print(title)

    await browser.close()


run_pyppetter = lambda: asyncio.get_event_loop().run_until_complete(run_puppetter())
