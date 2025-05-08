def analyze_page_content(content):
    """
    Basic content analyzer to infer if a page is likely:
    - active / legitimate
    - inactive
    - placeholder / fake
    """
    keywords_legit = ["followers", "following", "posts", "likes", "bio", "joined", "member since"]
    keywords_fake = ["not found", "error", "no such user", "this page doesn’t exist"]

    score = 0
    content_lower = content.lower()

    for word in keywords_legit:
        if word in content_lower:
            score += 1

    for word in keywords_fake:
        if word in content_lower:
            score -= 1

    if score > 2:
        return "✅ Likely Active"
    elif score < 0:
        return "❌ Likely Fake or Inactive"
    else:
        return "⚠️ Uncertain"
