from dataclasses import dataclass
from typing import Dict


@dataclass
class InvestmentResult:

    overall_score: int

    recommendation: str

    breakdown: Dict[str, int]