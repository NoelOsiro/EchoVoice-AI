# Design Your State

State is the shared memory accessible to all nodes in your agent. Think of it as the notebook your personalization engine uses to keep track of everything it learns, fetches, or decides as it moves through the workflow.

Every node can read and write to this state, which means you must carefully choose what belongs there.

---

## What Belongs in State?

For each type of information, ask:

1. **Does it need to persist across multiple steps?**
   - ✔️ If yes → put it in the state
   - ❌ If no → compute it locally in the node

2. **Will other nodes depend on it?**
   - ✔️ If yes → include it
   - ❌ If no → keep it internal

3. **Can it be derived from other values already in state?**
   - ✔️ If yes → don't store it, compute when needed
   - ❌ If no → store it

---

## 📋 Recommended State Structure for the Personalization Agent

A clean, modular state layout following LangGraph best practices:

State Fields

1. Campaign Context
Field
Purpose
Persist?
campaign_goal
User’s selected goal (e.g., reduce churn, increase revenue)
✔️ Yes
campaign_config
DB-loaded config: enabled segmentors, thresholds, offer rules
✔️ Yes
campaign_notes
Intermediate reasoning, LLM interpretations
✔️ Yes

2. Customer Data
Field
Purpose
Persist?
customer_id
Identifies the target customer
✔️ Yes
customer_profile
Demographics, KYC, plan/tier
✔️ Yes
behavior_events
Recent activity logs
✔️ Yes
transaction_history
Purchases, revenue, recency
✔️ Yes
churn_score
Model output for churn risk
✔️ Yes

3. Segmentation Layer
Field
Purpose
active_segments
List of segments customer falls into (e.g., “Dormant”, “High Value”)
behavioral_insights
LLM insights about habits or patterns
segment_path_taken
Which nodes/paths the engine chose

4. Offer & Action Layer
Field
Purpose
eligible_offers
All offers user qualifies for after rules check
recommended_offer
LLM-selected best fit
action_plan
Steps to take (message, schedule, CRM update)
final_decision
Output from last node

5. Execution Metadata
Field
Purpose
logs
Node-by-node reasoning snapshots
errors
Error messages or fallback states
needs_human_input
Boolean indicating if workflow must pause

Examples of What NOT to Store
❌ Raw responses from APIs (unless needed again)
 ❌ Repeated calculations (e.g. “days since last purchase” — derive it)
 ❌ Offer catalog (load once then filter)
 ❌ Temporary variables inside nodes
 ❌ Entire customer message history (unless used later; store summary instead)

Example State Definition (Python-ish / LangGraph style)
from typing import List, Optional, Dict, Any
from langgraph.graph import State

class PersonalizationState(State):
    campaign_goal: str
    campaign_config: Dict[str, Any]
    campaign_notes: Optional[str]

    customer_id: str
    customer_profile: Dict[str, Any]
    behavior_events: List[Dict]
    transaction_history: List[Dict]
    churn_score: Optional[float]

    active_segments: List[str]
    behavioral_insights: Optional[str]
    segment_path_taken: List[str]

    eligible_offers: List[Dict]
    recommended_offer: Optional[Dict]
    action_plan: Optional[Dict]
    final_decision: Optional[Dict]

    logs: List[str]
    errors: List[str]
    needs_human_input: bool
