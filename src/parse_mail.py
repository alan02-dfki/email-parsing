from email import policy
from email.parser import BytesParser
from io import StringIO
from pathlib import Path

import pandas as pd

if __name__ == "__main__":
    mail_path = Path(__file__).joinpath("../../res/real_email.eml").resolve()
    with open(mail_path, "rb") as fp:
        msg = BytesParser(policy=policy.default).parse(fp)

    for a in msg.iter_attachments():
        fn = a.get_filename()
        if (fn is not None) and (fn.split(".")[-1] == "csv"):
            print(fn)
            cont = a.get_content()
            cont_as_str = str(cont, "utf-8")

            df = pd.read_csv(StringIO(cont_as_str), sep=";")
            print(df.iloc[30:40, :])
