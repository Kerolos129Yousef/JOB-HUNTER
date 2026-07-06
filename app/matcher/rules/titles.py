from app.matcher.rules.base import BaseRule


TITLES = {
    "devops": 40,
    "site reliability engineer": 40,
    "sre": 40,
    "platform engineer": 35,
    "systems engineer": 30,
    "cloud engineer": 30,
    "infrastructure engineer": 30,
    "backend engineer": 20,
}


class TitlesRule(BaseRule):

    type = "title"

    # def apply(self, text, result):
    #     self.match_keywords(
    #         text=text,
    #         result=result,
    #         rules=TITLES,
    #     )