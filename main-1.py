import requests
import csv
import pandas as pd
import json

for page in range(1,112):
    url = f'https://api.goldstandard.org/projects?query=&page={page}&size=25&sortColumn=&sortDirection='

    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        results= []
        for d in data:
            id = d.get('id')
            name = d.get('name')
            description = d.get('description')
            status = d.get('status')
            gsf_standards_version = d.get('gsf_standards_version')
            estimated_annual_credits = d.get('estimated_annual_credits')
            crediting_period_start_date = d.get('crediting_period_start_date')
            crediting_period_end_date = d.get('crediting_period_end_date')
            type = d.get('type')
            size = d.get('size')
            sustaincert_id = d.get('sustaincert_id')
            sustaincert_url = d.get('sustaincert_url')
            project_developer = d.get('project_developer')
            country = d.get('country')
            methodology = d.get('methodology')
            carbon_stream = d.get('carbon_stream')
            poa_project_sustaincert_id = d.get('poa_project_sustaincert_id')

            final_data = {'id': id,
                          'name': name,
                          'description': description,
                          'status': status,
                          'gsf_standards_version': gsf_standards_version,
                          'estimated_annual_credits': estimated_annual_credits,
                          'crediting_period_start_date': crediting_period_start_date,
                          'crediting_period_end_date': crediting_period_end_date,
                          'type': type,
                          'size': size,
                          'sustaincert_id':sustaincert_id,
                          'sustaincert_url': sustaincert_url,
                          'project_developer': project_developer,
                          'country': country,
                          'methodology': methodology,
                          'carbon_stream': carbon_stream,
                          'poa_project_sustaincert_id': poa_project_sustaincert_id}
            
        with open('goldstandardfinal.csv', 'a', newline='', encoding= "utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=final_data.keys())
            if page == 1:
                writer.writeheader()
            writer.writerow(final_data)
