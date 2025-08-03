from pages.news.news_page import NewsPage
from utils.fake_data import generate_person_data
from fixtures.newsletter_texts import NewsletterTexts
from config import settings

def test_newsletter_subscription(page):
    news_page = NewsPage(page)
    newsletter = news_page.newsletter
    person = generate_person_data()

    news_page.navigate()

    heading = newsletter.get_heading()
    heading.wait_for(state="visible", timeout=settings.TIMEOUT)
    heading_text = heading.inner_text().strip()
    assert heading_text == NewsletterTexts.HEADING

    description = newsletter.get_description()
    description.wait_for(state="visible", timeout=settings.TIMEOUT)
    description_text = description.inner_text().strip()
    assert description_text == NewsletterTexts.DESCRIPTION

    newsletter.subscribe(person["email"])

    success = newsletter.get_success_message()
    success.wait_for(state="visible", timeout=settings.TIMEOUT)
    success_text = success.inner_text().strip()
    assert success_text == NewsletterTexts.SUCCESS_MESSAGE

def test_newsletter_subscription_with_empty_email(page):
    news_page = NewsPage(page)
    newsletter = news_page.newsletter
    person = generate_person_data()

    news_page.navigate()

    heading = newsletter.get_heading()
    heading.wait_for(state="visible", timeout=settings.TIMEOUT)
    

    newsletter.subscribe(" ")

    validation_msg = newsletter.get_invalid_validation_message()

    assert validation_msg == NewsletterTexts.EMPTY_MESSAGE
