from operator import itemgetter
import requests

# Make an API call and store the response.
# The following url returns a simple list of all the IDs of the current top articles on Hacker News,
# at the time the call is issued
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status Code : {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []

# Loop through the IDs of the top 30 submissions
for submission_id in submission_ids[:30]:

    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    print(response_dict)

    # Build a dictionary for submission(article) currently being processed.
    if 'title' in response_dict and 'descendants' in response_dict:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
        submission_dicts.append(submission_dict)
    else:
        print(f"Skipping submission id {submission_id} due to missing keys.")

# We want to sort the list of dictionaries by the number of comments
# We pass itemgetter() function the key 'comments' and it pulls value associated 
# with that key from each dictionary in the list
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
