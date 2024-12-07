from src.common_types import SmilesQuery


class PatentFinderMongoDB:

    def __init__(self, smiles_list: list[str]):
        self.smiles_list = smiles_list

    @staticmethod
    def get_smiles_patents_ids(query: SmilesQuery) -> list[str]:
        pass

    def find_all_patents(self):
        for smiles in self.smiles_list:
            pass
