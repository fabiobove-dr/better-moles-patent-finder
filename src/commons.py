import pandas as pd
from rdkit import Chem
from rdkit import RDLogger

from src.common_types import SmilesQuery

RDLogger.DisableLog('rdApp.*')


def cast_smiles_for_query(smiles: str) -> SmilesQuery:
    """
    Casts a SMILES string to its canonical form and generates an InChIKey.

    Args:
        smiles (str): The SMILES string to canonicalize.

    Returns:
        SmilesQuery: A dataclass containing the canonical SMILES and the InChIKey.

    Raises:
        ValueError: If the SMILES string is invalid or cannot be processed.
    """
    if smiles == "":
        raise ValueError(f"Error processing SMILES string.")
    try:
        # Canonicalize SMILES
        molecule = Chem.MolFromSmiles(smiles)
        if molecule is None:
            raise ValueError(f"Invalid SMILES string: {smiles}")

        query_smiles = Chem.MolToSmiles(molecule)
        query_mol = Chem.MolFromSmiles(query_smiles)
        query_inchikey = Chem.MolToInchiKey(query_mol)

        return SmilesQuery(smiles=query_smiles, inchikey=query_inchikey)
    except Exception as e:
        raise ValueError(f"Error processing SMILES string.")


def load_fake_data_from_csv(file_path: str) -> list:
    raise NotImplementedError


def add_patents_to_df(df: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


def save_df_to_csv(df: pd.DataFrame, file_path: str) -> None:
    raise NotImplementedError
