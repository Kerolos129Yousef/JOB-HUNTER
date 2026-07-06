from app.collectors.greenhouse import GreenhouseCollector
from app.collectors.lever import LeverCollector
from app.core.settings import GREENHOUSE_BOARDS, LEVER_BOARDS , ASHBY_BOARDS
from app.collectors.ashby import AshbyCollector

class CollectorManager:
    def get_collectors(self):
        collectors = []

        collectors.extend(
            GreenhouseCollector(
                board=board.board,
                company=board.company,
            )
            for board in GREENHOUSE_BOARDS
        )

        collectors.extend(
            LeverCollector(
                board=board.board,
                company=board.company,
            )
            for board in LEVER_BOARDS
        )

        collectors.extend(
            AshbyCollector(
                board=board.board,
                company=board.company,
            )
            for board in ASHBY_BOARDS
        )

        return collectors