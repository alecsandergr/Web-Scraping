#pip install scrapy

import requests
from scrapy.http import TextResponse

def get_response(endpoint: str = '/courses-all'):
    url = 'https://www.datacamp.com' + endpoint
    response = requests.get(url, headers={'User-Agent': 'XYZ/3.0'})
    response = TextResponse(body=response.content, url=url)
    return response

def generate_links(response):
    course_blocks = response.css('div.css-3undxp-HitCard')
    course_links = course_blocks.xpath('./a/@href')
    links_to_follow = course_links.extract()
    for link in links_to_follow:
        yield get_response(link)

def get_info_from_course(response):
    for link_resp in generate_links(response):

        # Direct to the course title text
        crs_title = link_resp.css('h1.css-7ymucl-CourseShowPage::text')
        # crs_title = link_resp.xpath('//h1[@class="css-7ymucl-CourseShowPage"]/text()')
        # Extract and clean the course title text
        crs_title_ext = crs_title.extract_first().strip()
        # Direct to the chapter description
        ch_desc = link_resp.css('p.css-hnday4-CourseShowPage::text')
        # Extract and clean the chapter description
        ch_desc_ext = ch_desc.extract_first().strip()
        # Direct to the chapter titles text
        ch_titles = link_resp.css('h3.css-172ju3k-Box::text')
        # ch_titles = link_resp.xpath('//h3[@class="css-172ju3k-Box"]/text()')
        # Extract and clean the chapter titles
        ch_titles_ext = [t.strip() for t in ch_titles.extract()]

        dc_dict[crs_title_ext] = {'Description': ch_desc_ext, 'Chapters': ch_titles_ext}
        print(crs_title_ext, ch_desc_ext, ch_titles_ext, '\n', sep='\n')

def scrap_datacamp():
    response = get_response()
    get_info_from_course(response)

if __name__ == '__main__':

    dc_dict = {}
    
    response = get_response()
    get_info_from_course(response)
    for course, course_items in dc_dict.items():
        print(f'Course: {course}')
        print(f'Description: {course_items["Description"]}')
        for i, chapter in enumerate(course_items['Chapters'], start=1):
            print(f'    Chapter {i}: {chapter}')
        print('')