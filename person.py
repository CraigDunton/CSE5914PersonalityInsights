from watson_developer_cloud import PersonalityInsightsV3
from os.path import join, dirname
import json

personality_insights = PersonalityInsightsV3(
    version='2019-01-08',
    iam_apikey='XydPARVueKLYAG9UvHVnLG5QTANmBYQ5Lp8e9cW6hNFX',
    url='https://gateway.watsonplatform.net/personality-insights/api'
)

with open(join(dirname(__file__), './profile.json')) as profile_json:
    profile = personality_insights.profile(
        profile_json.read(),
        content_type='application/json',
        consumption_preferences=True,
        raw_scores=True
    ).get_result()


d_profile = json.loads(json.dumps(profile, indent=2))
# print(d_profile['personality'])

# Find the personality trait most exhibited based on the profile
max_p = 0
max_p_name = ""
max_trait = 0
max_trait_name = ""

for key in d_profile['personality']:
	if key['percentile'] > max_p:
		max_p = key['percentile']
		max_p_name = key['name']
		for child in key['children']:
			if child['percentile'] > max_trait:
				max_trait = child['percentile']
				max_trait_name = child['name']

print("The user of this profile most exhibits this Big 5 personality: " + max_p_name + " : with this percentile: " + str(max_p))

print("The user of this profile most exhibits this trait of their personality: " + max_trait_name + " : with this percentile: " + str(max_trait))

print("This user may have these buying habits: ")

for conpref in d_profile['consumption_preferences']:
	for ids in conpref['consumption_preferences']:
		if ids['score'] > 0.0:
			print(ids['name'])
			

