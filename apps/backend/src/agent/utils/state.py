"""State definition for the agent.

Defines the input state structure.
See: https://langchain-ai.github.io/langgraph/concepts/low_level/#state.
"""

from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass
class State:
    """Input state for the agent.

    Defines the initial structure of incoming data.
    See: https://langchain-ai.github.io/langgraph/concepts/low_level/#state
    """

    campaign_goal: str
    campaign_config: Dict[str, Any]
    campaign_notes: str | None

    customer_id: str
    customer_profile: Dict[str, Any]
    behavior_events: List[Dict]
    transaction_history: List[Dict]
    churn_score: float | None

    active_segments: List[str]
    behavioral_insights: str | None
    segment_path_taken: List[str]

    eligible_offers: List[Dict]
    recommended_offer: Dict | None
    action_plan: Dict | None
    final_decision: Dict | None
    logs: List[str]
    errors: List[str]
    needs_human_input: bool

