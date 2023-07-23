import scrapy
from scrapy.crawler import CrawlerProcess


class MySpider(scrapy.Spider):

    name = 'my_first_spider'

    def start_requests(self):
        urls = ['https://www.datacamp.com/courses-all']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_front, headers={'User-Agent': 'XYZ/3.0'})

    def parse_front(self, response):
        # Narrow in on the course blocks
        course_blocks = response.css('div.css-3undxp-HitCard')
        # print(course_blocks)
        # Direct to the course links
        course_links = course_blocks.xpath('./a/@href')
        # Extract the links (as a list of strings)
        links_to_follow = course_links.extract()
        for link in links_to_follow:
            yield response.follow(url=link, callback=self.parse_pages, headers={'User-Agent': 'XYZ/3.0'})
    
    def parse_pages(self, response):
        # Direct to the course title text
        crs_title = response.css('h1.css-7ymucl-CourseShowPage::text')
        # crs_title = response.xpath('//h1[@class="css-7ymucl-CourseShowPage"]/text()')
        # Extract and clean the course title text
        crs_title_ext = crs_title.extract_first().strip()
        # Direct to the chapter description
        ch_desc = response.css('p.css-hnday4-CourseShowPage::text')
        # Extract and clean the chapter description
        ch_desc_ext = ch_desc.extract_first().strip()
        # Direct to the chapter titles text
        ch_titles = response.css('h3.css-172ju3k-Box::text')
        # ch_titles = resp.xpath('//h3[@class="css-172ju3k-Box"]/text()')
        # Extract and clean the chapter titles
        ch_titles_ext = [t.strip() for t in ch_titles.extract()]
        # Store this in our dictionary
        dc_dict[crs_title_ext] = {'Description': ch_desc_ext, 'Chapters': ch_titles_ext}


if __name__ == '__main__':

    dc_dict = {}
    
    process = CrawlerProcess()
    process.crawl(MySpider)
    process.start()
    dc_dict
    for course, course_items in dc_dict.items():
            print(f'Course: {course}')
            print(f'Description: {course_items["Description"]}')
            for i, chapter in enumerate(course_items['Chapters'], start=1):
                print(f'    Chapter {i}: {chapter}')
            print('')