import json


def copy_from_json_to_json(from_json, to_json):
    with open(from_json, 'r', encoding='utf-8') as from_j, open(to_json, 'w', encoding='utf-8') as to_j:
        to_j.write(from_j.read())


def create_empty_struct(json_name='cards.json'):
    """ Create empty json from pattern """
    copy_from_json_to_json('pattern/empty.json', json_name)


def upload_based_data(json_name='cards.json'):
    """ Upload based data to json from pattern """
    copy_from_json_to_json('pattern/data.json', json_name)


if __name__ == "__main__":
    upload_based_data()
