def extract_text(element, tag='a', class_=None):

    # util so i can use the scraper for muliple listings not just pc's
    # Extract text from an element or its child tag.
    # Returns:
    #     str: Extracted text, or None if not found

    if not element:
        return None
    child = element.find(tag, class_=class_) if class_ else element.find(tag)
    return (child or element).get_text(strip=True) or None