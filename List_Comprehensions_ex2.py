websites = ["mimo.com", "coding.com", "food.org"]

def add_https(site):
    return "https://" + site

auto_add = [add_https(website) for website in websites]

print(auto_add)
