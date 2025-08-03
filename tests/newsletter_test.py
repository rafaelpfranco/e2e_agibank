import pytest
from pages.news_page import NewsPage
from utils.fake_data import generate_person_data
from fixtures.newsletter_texts import NewsletterTexts
from playwright.sync_api import expect
from config import settings

@pytest.mark.usefixtures("page")
class TestNewsletter:
    @pytest.fixture(autouse=True)
    def setup(self, page):
        self.page = page
        self.news_page = NewsPage(page)
        self.news_page.navigate()
        self.newsletter = self.news_page.newsletter
        self.newsletter.get_heading().wait_for(
            state="visible", timeout=settings.TIMEOUT
        )
        
    def test_newsletter_subscription_with_empty_email(self):
        """
        Verifica que ao tentar assinar sem preencher o e-mail, a mensagem campo obrigatório é exibida.
        """
        self.newsletter.subscribe(" ")
        assert self.newsletter.get_invalid_validation_message() == NewsletterTexts.EMPTY_MESSAGE

    def test_newsletter_subscription_with_invalid_email(self):
        """
        Verifica que ao usar e-mail inválido, a mensagem de campo inválido é exibida.
        """
        self.newsletter.subscribe("email_invalido")
        validation_msg = (
            self.newsletter
                .get_invalid_validation_message()
                .replace("\u00A0", " ")
        )
        assert validation_msg == NewsletterTexts.INVALID_EMAIL_MESSAGE

    def test_newsletter_subscription(self):
        """
        Verifica que um usuário consegue se inscrever com e-mail válido.
        """
        person = generate_person_data()

        assert self.newsletter.get_heading().inner_text().strip() == NewsletterTexts.HEADING
        assert self.newsletter.get_description().inner_text().strip() == NewsletterTexts.DESCRIPTION

        self.newsletter.subscribe(person["email"])

        print(person["email"])
        expect(self.page).to_have_url(
            "noticias/?subscribe=success#subscribe-blog-blog_subscription-3",
            timeout=settings.TIMEOUT
        )
        self.newsletter.get_success_message().wait_for(
            state="visible", timeout=settings.TIMEOUT
        )
        assert (
            self.newsletter
                .get_success_message()
                .inner_text()
                .strip()
            == NewsletterTexts.SUCCESS_MESSAGE
        )