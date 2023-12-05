from typing import List, Dict, Any
from dotenv import load_dotenv
import json
import os
import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter


load_dotenv()
BASE_DIR = os.environ['BASE_DIR']

def save_to_disk(json_content: List[Dict[str, Any]], path: str) -> None:
    
    file_name = f'sales_{path.split("/")[-1]}.json'
    full_path = BASE_DIR + path
    
    with open(full_path + '/' + file_name, mode = 'w') as json_file:
        json.dump(json_content, json_file, indent = 4)


def transform_json_to_avro(path: str) -> None:



    schema_file = 'schema.avsc'

    file_name = f'sales_{path.split("/")[-1]}.'
    full_path = BASE_DIR + path

    path_to_json_file = BASE_DIR + '/raw/sales/2022-08-09/'

    if os.path.exists(full_path + '/' + f'{file_name}avro'):
        os.remove(full_path + '/' + f'{file_name}avro')

    schema = avro.schema.parse(open(path_to_json_file + schema_file, mode = 'r').read())

    writer = DataFileWriter(open(full_path + '/' + f'{file_name}avro', mode = 'wb'), DatumWriter(), schema)

    with open(path_to_json_file + f'{file_name}json', mode = 'r') as json_file:
        data = json.load(json_file)

    for log in data:
        writer.append(log)
    writer.close()