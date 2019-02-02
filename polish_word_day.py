
from bs4 import BeautifulSoup
import requests, telegram
from telegram.ext import Updater, CommandHandler



def get_content_website():
    """
    Take the content of the website that offers a polish word of a day
    Returns - dictionary with polish-english translation
    """
    try:
        web = requests.get(r'https://www.polishpod101.com/polish-phrases/')
        soup = BeautifulSoup(web.content, 'html.parser')

        #Find divs with polish
        divs_polish = soup.findAll('div', {'class':'r101-wotd-widget__word'})
        divs_english = soup.findAll('div', {'class':'r101-wotd-widget__english'})

        #get the text from divs
        div_text_polish = [item.get_text() for item in divs_polish]
        div_text_english = [item.get_text() for item in divs_english]

        results = dict(zip(div_text_polish, div_text_english))

        return results
    except Exception as ex:
        return {'Issue':ex.__str__()}


def format_results(results):
    """
    Converts the dictionary into a string and gives it formatting
    """
    final_string = ''
    for k, v in results.items():
        final_string += k + " --> "
        final_string += v +'\n\n\n\n'

    return final_string
        
def send_message(message):
    """
    Using telegram library we send the message to a chat bot that has been created
    """
    bot = telegram.Bot(token='ADD YOUR TOKEN HERE')
    bot.sendMessage(chat_id='ADD CHAT ID HERE', text=message)


def main():
    results = get_content_website()
    final_string = format_results(results)
    send_message(final_string)

if __name__ == '__main__':
    main()
