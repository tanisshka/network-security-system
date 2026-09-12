from gc import collect
import imp
import os
import json
from shutil import ExecError
import sys
from dotenv import load_dotenv

load_dotenv()
MONGO_DB_URI = os.getenv("MONGO_DB_URI")


import certifi
ca=certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def csv_to_json_converter(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records

            self.mongoclient=pymongo.MongoClient(MONGO_DB_URI)
            self.database=self.mongoclient[self.database]
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e,sys)

def main():
    try:
        file_path = "Network_Data/phisingData.csv"
        database = "NetworkSecurity"
        collection = "PhishingData"

        networkobj = NetworkDataExtract()
        records = networkobj.csv_to_json_converter(file_path=file_path)
        logging.info(f"Converted {len(records)} records from {file_path}")
        no_of_records = networkobj.insert_data_mongodb(records, database, collection)
        print(f"Inserted {no_of_records} records into {database}.{collection}")
    except Exception as e:
        raise NetworkSecurityException(e, sys)

if __name__ == "__main__":
    main()

