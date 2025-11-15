def generate_variants(customer: dict, segment: dict, citations: list) -> list:
    # Produce a few A/B variants using available info (mocked)
    name = customer.get('name', 'Customer')
    seg_label = segment.get('segment')
    citation_text = citations[0]['content'] if citations else ''

    variants = []
    variants.append({
        'id': 'A',
        'subject': f"Hi {name}, quick note about {seg_label}",
        'body': f"Hi {name},\n\nWe thought you might like this: {citation_text}\n\n— Team",
        'meta': {'type': 'short'}
    })
    variants.append({
        'id': 'B',
        'subject': f"{name}, more on the Acme plan",
        'body': f"Hello {name},\n\nDetails: {citation_text}\nLearn more on our site.",
        'meta': {'type': 'long'}
    })
    return variants
