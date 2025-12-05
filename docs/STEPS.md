# Identify What Each Workflow Step Needs

For each node in your personalization workflow, determine the type of operation it represents and the context it needs to run correctly.

Nodes are categorized as:

- **LLM Steps** – Reasoning, analysis, generating insights
- **Data Steps** – Querying your database, segmentation rules, configs
- **Action Steps** – Triggering campaign actions, sending offers
- **User Input Steps** – Human override or validation

---

## 🧠 LLM Steps

Use LLM nodes when the step must:

- Interpret a campaign goal (e.g., “reduce churn”, “increase upsell”)
- Reason about customer behavior patterns
- Decide which segmentation paths are relevant
- Rank or score personalization opportunities
- Generate recommended actions (offers, nudges, retention strategies)

**Examples of LLM-driven nodes:**

- Goal Interpreter — converts “Reduce churn” into measurable segments
- Behavior Pattern Analyzer — reads customer events and infers intent
- Offer Reasoner — decides which offer category fits best
- Path Selector — picks the correct branch (demographic, behavioral, lifecycle, etc.)

**Context required:**

- Campaign goal
- Historical customer data
- Behavior logs
- Offer catalog metadata
- Business rules & constraints

---

## 🗄️ Data Steps

Use data nodes when the step must retrieve or calculate external info:

- Load campaign configuration
- Fetch customer profile
- Fetch transaction history, churn risk score
- Apply rule-based segmentation (age, product tier, recency, etc.)
- Load offer eligibility rules

**Examples of Data-driven nodes:**

- FetchCustomerData
- FetchBehaviorSignals
- FetchCampaignConfig
- RuleBasedSegmentor
- EligibilityChecker

**Context required:**

- DB or API connectors
- Segmentation rules table
- Offer rules & thresholds
- System configurations (enable/disable segmentors)

---

## ⚡ Action Steps

Use action nodes when the step must execute something outside the agent:

- Trigger an outbound message (SMS, email, push)
- Apply discounts or loyalty points
- Trigger CRM updates
- Schedule follow-ups
- Log campaign actions
- Notify account manager

**Examples of Action-driven nodes:**

- SendOfferAction
- TriggerFollowUp
- LogCampaignEvent
- UpdateCRM

**Context required:**

- Messaging API credentials
- CRM integration
- Offer delivery channels
- Campaign tracking IDs

---

## 👤 User Input Steps

Use user-input nodes when manual confirmation or correction is needed:

- Approve high-value customer offers
- Validate if an auto-generated offer is appropriate
- Override system's segmentation
- Provide custom actions not in inventory

**Examples of nodes requiring human input:**

- HumanReviewForVIPs
- OfferApprovalStep
- DisputeResolutionInput

**Context required:**

- UI or dashboard
- Human input schema
- Approval logic
