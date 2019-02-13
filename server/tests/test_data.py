import json
from dataplay.datasvc.csv import CVSDataset


def is_json(content):
    try:
        json.loads(content)
    except ValueError as e:
        return False
    return True


def test_data_list():
    files = CVSDataset.list_csv()
    assert len(files) == 25


def test_dataset_to_json():
    files = CVSDataset.list_csv()
    for file in files:
        id = file['id']
        dataset = CVSDataset(id)
        payload = json.dumps(dataset.payload())

        assert is_json(payload)
