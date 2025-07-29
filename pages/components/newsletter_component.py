from playwright.sync_api import Page, Locator

class NewsletterComponent:
    def __init__(self, page: Page):
        self._page = page
        self._heading: Locator = page.get_by_text("Se inscreva em nossa Newsletter")
        self._description: Locator = page.get_by_text("Digite seu endereço de e-mail")
        self._email_input: Locator = page.get_by_role("textbox", name="Endereço de e-mail")
        self._submit_button: Locator = page.get_by_role("button", name="Assinar")
        self._success_message: Locator = page.get_by_text("Sucesso! Enviamos um e-mail")

    def get_heading(self) -> Locator:
        return self._heading

    def get_description(self) -> Locator:
        return self._description

    def get_email_input(self) -> Locator:
        return self._email_input

    def get_submit_button(self) -> Locator:
        return self._submit_button

    def get_success_message(self) -> Locator:
        return self._success_message

    def subscribe(self, email: str) -> None:
        self._email_input.wait_for(state="visible", timeout=5000)
        self._email_input.fill(email)

        self._submit_button.wait_for(state="visible", timeout=5000)
        self._submit_button.click()

        self._success_message.wait_for(state="visible", timeout=10000)

