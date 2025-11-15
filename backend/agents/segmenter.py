def segment_user(customer: dict) -> dict:
    """Return a simple segment label and explainable reasons."""
    last_event = customer.get('last_event', '')
    if last_event == 'started_form':
        segment = 'FormAbandoned'
        reasons = ['started form but did not complete', 'high intent signal']
    elif last_event == 'viewed_product':
        segment = 'ViewedProduct'
        reasons = ['recently viewed product page']
    else:
        segment = 'Engaged'
        reasons = ['recent activity']

    return {
        'segment': segment,
        'reasons': reasons
    }
