from app.matcher.rules.skills import SkillsRule
from app.matcher.rules.titles import TitlesRule
from app.matcher.rules.locations import LocationsRule
from app.matcher.rules.seniority import SeniorityRule
from app.matcher.rules.penalties import PenaltiesRule


RULES = [
    SkillsRule(),
    TitlesRule(),
    LocationsRule(),
    SeniorityRule(),
    PenaltiesRule(),
]