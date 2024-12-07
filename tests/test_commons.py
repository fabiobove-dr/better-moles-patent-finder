import pytest

from src.common_types import SmilesQuery
from src.commons import cast_smiles_for_query


@pytest.mark.parametrize(
    "input_smiles, expected_smiles, expected_inchikey",
    [
        ("CCO", "CCO", "LFQSCWFLJHTTHZ-UHFFFAOYSA-N"),  # Ethanol
        ("C1CCCCC1", "C1CCCCC1", "XDTMQSROBMDMFD-UHFFFAOYSA-N"),  # Cyclohexane
        ("c1ccccc1", "c1ccccc1", "UHOVQNZJYSORNB-UHFFFAOYSA-N"),  # Benzene
    ],
)
def test_cast_smiles_for_query_valid(input_smiles, expected_smiles, expected_inchikey):
    result = cast_smiles_for_query(input_smiles)

    assert isinstance(result, SmilesQuery)
    assert result.smiles == expected_smiles
    assert result.inchikey == expected_inchikey


@pytest.mark.parametrize(
    "invalid_smiles",
    [
        "InvalidSMILES",  # Completely invalid string
        "[C@@H",  # Mismatched parentheses
        ""  # Empty string
    ],
)
def test_cast_smiles_for_query_invalid(invalid_smiles):
    with pytest.raises(ValueError, match=f"Error processing SMILES string."):
        cast_smiles_for_query(invalid_smiles)


if __name__ == "__main__":
    pytest.main()
