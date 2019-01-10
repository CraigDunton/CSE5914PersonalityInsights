from watson_developer_cloud import PersonalityInsightsV3
from watson_developer_cloud import WatsonApiException
import requests

headers = {
  'Authorization': 'Basic b2FsdmpiV01FM0F3ek0zNkNkanNtTmozNjpVS0JRcmdjVXY4cEZHalM2T25HanFudVZtdnN5d3JqaDllRVI4Vk1XWUl1MUF0UzI4Mg==',
  'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
  'Accept': 'application/json'
}

r = requests.post('https://api.twitter.com/oauth2/token', data={'grant_type': 'client_credentials'}, headers=headers)
json_data = r.json()
access_token = json_data['access_token']

tweet_headers = {
  'Authorization': 'Bearer ' + access_token
}

screen_name = input('Give me a twitter handle: ')
tweet_req = requests.get('https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name='+ screen_name, headers=tweet_headers)
tweets = tweet_req.json()

content_json = {
  'contentItems': []
}

for tweet in tweets:
  #print(tweet['text'])
  content_json['contentItems'].append({
    'content': tweet['text'],
    'contenttype': 'text/plain'
  })

personality_insights = PersonalityInsightsV3(
  version="2017-10-13",
  iam_apikey="2ZZUGqAkec90ydyu6n_B1QxmMcTCESTa_47nmkpsK1Bf",
  url="https://gateway-wdc.watsonplatform.net/personality-insights/api",
)

# textFile = open('profile.txt')
# text = textFile.read()

response = personality_insights.profile(content_json, accept='application/json', content_type='application/json', consumption_preferences=True).get_result()

personalities = response['personality']
needs = response['needs']
values = response['values']
consumption_preferences = response['consumption_preferences']

print()
print('***** Personality *****')
for personality in personalities:
    if personality['percentile'] > .5:
      print(personality['name'])
print()

print('***** Needs *****')
for need in needs:
  if need['percentile'] > .5:
    print(need['name'])
print()

print('***** Values *****')
for value in values:
  if value['percentile'] > .5:
    print(value['name'])
print()

print()
print('What to get @' + screen_name + ' for christmas: ')
print()
for pref in consumption_preferences:
  for ids in pref['consumption_preferences']:
    if ids['score'] > 0.75:
      print(ids['name'])
