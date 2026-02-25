import pandas as pd
import json
from pathlib import Path

if __name__ == "__main__":
    with open(Path(__file__, "../../res/example.json").resolve(), "r") as infile:
        j = json.load(infile)

    print(j["predictions"])
    df = pd.DataFrame.from_dict(j["predictions"])
    print(df)
