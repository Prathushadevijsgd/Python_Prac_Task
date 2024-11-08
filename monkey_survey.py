import json
import requests
import argparse

ACCESS_TOKEN = 'oTOjW-NXReugekjAFqek.WyVjNPRNReXDzXWroRxpyOjPxtCgINOArCIcfwWyMpMtqzeqpvmU618qiqMaxpLTXacsL4EdcwG5v0QoWNhnaHqEzXH1CbvGkPOYQfuEENx'
BASE_URL = "https://api.surveymonkey.com/v3"


def create_survey(survey_data):
    
    url = f"{BASE_URL}/surveys"
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }

    survey_payload = {
        "title": survey_data['Survey_Name'],
        "pages": []
    }

    # Iterate over survey data to construct the survey payload
    for page_name, page_content in survey_data.items():
        if page_name == 'Survey_Name':  
            continue

        page_payload = {
            "title": page_name,
            "questions": [] 
        }

        for question_name, question_content in page_content.items():
            if len(question_content["Answers"]) > 1:
                answer_data=[]
                # Multiple choice question (checkboxes)
                for answer in question_content['Answers']:
                    answer_data.append(answer)
                print(answer_data)
                question_payload = {
                    "headings": [{"heading": question_content["Description"]}],
                    "answers": {"choices": answer_data },
                    "family": "multiple_choice",  # Multiple choice
                    "subtype": "vertical"  # Subtype for multiple choice
                }
            else:
                # Single choice question (radio buttons)
                question_payload = {
                    "headings": [{"heading": question_content["Description"]}],
                    "answers": {"choices": answer_data },
                    "family": "single_choice",  # Single choice
                    "subtype": "vertical"  # Subtype for single choice
                }

            page_payload["questions"].append(question_payload)

        # Add the page to the survey
        survey_payload["pages"].append(page_payload)
       # print(survey_payload)
    # Send request to create the survey
    response = requests.post(url, headers=headers, json=survey_payload)

    if response.status_code == 201:
        survey_id = response.json()['id']
        print(f'Survey created successfully with ID: {survey_id}')
        return survey_id
    else:
        print(f'Error creating survey: {response.status_code} - {response.text}')
        return None



def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Create a survey.")
    
    parser.add_argument("-q", "--questions", required=True, help="Path to JSON file containing survey questions")
    
    args = parser.parse_args()

    # Load survey data from JSON file
    with open(args.questions, 'r') as f:
        survey_data = json.load(f)

    # Create the survey
    survey_id = create_survey(survey_data)
    if not survey_id:
        print("Survey creation failed. Exiting.")
        return



if __name__ == "__main__":
    main()
