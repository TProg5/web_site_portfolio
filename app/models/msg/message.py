from app.models.pydantic.contact import ContactForm


class MessageTemplates:
    @staticmethod
    def contact_submission(data: ContactForm) -> str:
        return (
            f"<b>Новая заявка с сайта</b>\n\n"
            f"<b>firstName:</b> {data.firstName}\n"
            f"<b>Username:</b> @{data.username}\n"
            f"<b>Email:</b> {data.email}\n"
            f"<b>Inquiry:</b> {data.inquiry}\n\n"
            f"<b>Message:</b> {data.message}"
        )
        