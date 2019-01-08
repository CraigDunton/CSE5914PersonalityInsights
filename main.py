from watson_developer_cloud import PersonalityInsightsV3
from watson_developer_cloud import WatsonApiException

personality_insights = PersonalityInsightsV3(
  version="2017-10-13",
  iam_apikey="2ZZUGqAkec90ydyu6n_B1QxmMcTCESTa_47nmkpsK1Bf",
  url="https://gateway-wdc.watsonplatform.net/personality-insights/api",
)

textFile = open('profile.txt')
text = textFile.read()
response = personality_insights.profile(text, accept='application/json', content_type='text/plain').get_result()

print(response)