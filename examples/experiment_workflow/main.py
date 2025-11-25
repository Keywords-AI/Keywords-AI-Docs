import requests
import json

# Configuration
API_KEY = "cVbRkprs.2KmE2bFZvvHWcQj9pB6VwklVnunaNQc6"
BASE_URL = "https://api.keywordsai.co/api"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Step 5: Create Experiment
def create_experiment(dataset_id, evaluator_slug):
    """Create a custom workflow experiment."""
    url = f"{BASE_URL}/v2/experiments/"
    
    payload = {
        "name": "My Custom Workflow Experiment",
        "dataset_id": dataset_id,
        "workflows": [
            {
                "type": "custom",
                "config": {
                    "name": "Custom Processing Workflow",
                    "description": "User-defined workflow for custom processing"
                }
            }
        ],
        "evaluator_slugs": [evaluator_slug]
    }
    
    response = requests.post(url, headers=HEADERS, json=payload)
    response.raise_for_status()
    
    data = response.json()
    print(f"Experiment created successfully!")
    print(f"Experiment ID: {data['id']}")
    print(f"Full response: {json.dumps(data, indent=2)}")
    
    return data['id']

if __name__ == "__main__":
    # Replace with your actual IDs
    dataset_id = "a65814cf-8459-455b-9edf-0dcfdb02376e"
    evaluator_slug = "3cca20fc-12b5-4503-b4a0-8bbb7df8f56f"
    
    try:
        experiment_id = create_experiment(dataset_id, evaluator_slug)
        print(f"\n✓ Success! Experiment ID: {experiment_id}")
    except Exception as e:
        print(f"\n✗ Error: {e}")
        if hasattr(e, 'response'):
            print(f"Response: {e.response.text}")
