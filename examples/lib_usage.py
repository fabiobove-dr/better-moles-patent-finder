import pandas as pd
from mongo.mongo_configs import MongoConnectionConfig
from mongo.mongo_connector import MongoConnector
from patent_finder.patent_finder_mongo_db import PatentFinderMongoDB

if __name__ == '__main__':
    # create a MongoConnector instance
    conf_dict = {
        "host": "localhost",
        "port": 27017,
        "db_name": "patents",
        "collection": "patcid",
        "username": "root",
        "password": "example",
    }
    config = MongoConnectionConfig()
    config.load_from_dict(conf_dict)
    mongo = MongoConnector(config)
    mongo.connect()
    # create a PatentFinder instance
    pf = PatentFinderMongoDB(
        smiles_df=pd.DataFrame({"smiles": ["Brc1cc(-c2ccccc2)nc(-c2ccc3c4ccccc4c4ccccc4c3c2)c1"]}),  # can be None
        mongo_connector=mongo
    )
    # finds all patent IDs for the given SMILES and prints them
    results = pf.find_all_patents()  # using parallel processing and batch processing
    [print(r) for r in results[0]]

    other_result = pf.search_by_smiles("Brc1cc(-c2ccccc2)nc(-c2ccc3c4ccccc4c4ccccc4c3c2)c1")  # for single processing
    print(other_result)

    # close the connection
    mongo.close()
