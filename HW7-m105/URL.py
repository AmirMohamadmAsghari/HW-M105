import re

def extract_domain_names(urls):
    # List to store extracted domain names
    domain_names = []
    # Regex pattern for extracting domain name from URL
    domain_pattern = re.compile(r'https?://(?:www\.)?([^/?]+)')
    # Iterating through each URL in the input list
    for url in urls:
        # Attempting to match the URL with the regex pattern
        match = domain_pattern.match(url)
        # If a match is found
        if match:
            # Extracting the domain name from the matched pattern
            domain_name = match.group(1)
            # Appending the extracted domain name to the list
            domain_names.append(domain_name)
    
    return domain_names

# Example usage
urls = ["https://www.example.com/page1", "http://blog.example.org/post", "https://www.anotherdomain.net"]
result = extract_domain_names(urls)
# Printing the result
print(result)
