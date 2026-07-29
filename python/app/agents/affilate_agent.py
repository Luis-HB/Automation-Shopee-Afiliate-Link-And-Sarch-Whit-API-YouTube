from models.ai_payload import AIPayload
from ShopeeAffiliate.python.app.models.commercial_decision import AffiliateDecision

from agents.prompts.affiliate_system_prompt import (
    AffiliateSystemPrompt
)

from agents.prompts.affiliate_user_prompt import (
    AffiliateUserPrompt
)

from agents.parsers.affiliate_response_parser import (
    AffiliateResponseParser
)


class AffiliateAgent:

    def __init__(self):

        self.system_prompt = AffiliateSystemPrompt()

        self.user_prompt = AffiliateUserPrompt()

        self.parser = AffiliateResponseParser()

    # =====================================================

    def build_messages(
        self,
        payload: AIPayload
    ):

        return {

            "system": self.system_prompt.build(),

            "user": self.user_prompt.build(payload)

        }

    # =====================================================

    def parse(self, response):

        return self.parser.parse(response)

    # =====================================================

    def execute(
        self,
        payload,
        llm_response
    ) -> AffiliateDecision:

        #
        # Aqui, por enquanto,
        # apenas convertemos a resposta
        #

        return self.parse(llm_response)