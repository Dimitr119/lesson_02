from flask import Flask, request
from flask import typing as flask_typing
from job1.bll.sales_api import save_sales_to_local_disk
from job1.dal.local_disk import transform_json_to_avro


app = Flask(__name__)


@app.route('/', methods=['POST'])
def main() -> flask_typing.ResponseReturnValue:

    input_data = request.get_json()

    input_data: dict = request.json

    raw_dir = input_data.get('raw_dir')
    stg_dir = input_data.get('stg_dir')

    if not stg_dir:
        return {"message": "stg_dir parameter missed"}, 400
        
    save_sales_to_local_disk(date = raw_dir.split('/')[-1], raw_dir = raw_dir)

    transform_json_to_avro(path=stg_dir)

    return {"message": "Data retrieved successfully from API and transformed to Avro format"}, 201
        
    
    

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8082)