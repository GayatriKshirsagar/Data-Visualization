import requests

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

# Define headers for the API call that ask explicitly to use this 3rd version of the API
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers = headers)

print(f"Status Code: {r.status_code}")

# Store API response in a variable
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Explore information about repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository.
repo_dict = repo_dicts[0]
# print(f"\nKeys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
# 	print(key)

# # Process results.
# print(response_dict.keys())

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
	print(f"Name: {repo_dict['name']}")
	print(f"Owner: {repo_dict['owner']['login']}")
	print(f"Stars: {repo_dict['stargazers_count']}")
	print(f"Repository: {repo_dict['html_url']}")
	print(f"Created: {repo_dict['created_at']}")
	print(f"Updated: {repo_dict['updated_at']}")
	print(f"Description: {repo_dict['description']}\n")