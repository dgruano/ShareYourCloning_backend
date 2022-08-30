# %%
from urllib.error import HTTPError
import requests
gene_id = 'SPAPB1A10.09'
url = f'https://rest.ensembl.org/lookup/id/{gene_id}?expand=1;content-type=application/json'
resp = requests.get(url)

if resp.status_code == 404:
    raise HTTPError(url, 404, 'entity not found', 'entity not found', None)

# %%
data = resp.json()

region = data['seq_region_name']
strand = data['strand']
start = data['start']
end = data['end']
species = data['species']
genome_coords = f'{region}:{start}..{end}:{strand}'
url = f'https://rest.ensembl.org/sequence/region/{species}/{genome_coords}'
headers = {'content-type': 'text/plain'}
params = {
    'expand_3prime': 1000,
    'expand_5prime': 1000
}

resp2 = requests.get(url, params=params, headers=headers)
if resp2.status_code == 404:
    raise HTTPError(url, 404, 'entity not found', 'entity not found', None)

string_sequence = resp2.content

for transcript in data['Transcript']:
    print(transcript)

#%%

