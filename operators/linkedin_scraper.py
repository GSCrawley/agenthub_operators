from .base_operator import BaseOperator
from ai_context import AiContext
import requestsfrom bs4 import BeautifulSoup

class LinkedInScraper(BaseOperator):
    @staticmethod
    def declare_name():
        return 'LinkedInScraper'
    
    @staticmethod
    def declare_category():
        return BaseOperator.OperatorCategory.ACT.value
    
    @staticmethod
    def declare_parameters():
        return []
    
    @staticmethod
    def declare_inputs():
        return [
            {
                "name": "profile_urls",
                "data_type": "string []"
            }
        ]
    
    @staticmethod
    def declare_outputs():
        return [
            {
                "name": "profile_infos",
                "data_type": "string []"
            }
        ]
        
    def run_step(self, step, ai_context: AiContext):
        profile_urls = ai_context.get_input('profile_urls', self)
        profile_infos = []
        for profile_url in profile_urls:
            # Use requests to get the HTML content of the LinkedIn profile page
            page = requests.get(profile_url)
            soup = BeautifulSoup(page.content, 'html.parser')

            # use BeautifulSoup to scrape the desired information from the page
            profile_info = soup.find('main', class_='scaffold-layout__main')
            profile_infos.append(profile_info.get_text())
            
            ai_context.set_output('profile_infos', profile_infos)
