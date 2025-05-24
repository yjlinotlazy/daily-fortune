import argparse
import pandas as pd
from importlib import resources

class FortuneTeller:
    def __init__(self, mode: str = 'random') -> None:
        self.mode = mode
        self._read_db()
    
    def set_mode(self, mode: str) -> None:
        self.mode = mode
    
    def tell(self) -> str:
        candidates = self.db
        selected = candidates.sample(n=1)
        return selected['text'].iloc[0]
    
    def _read_db(self):
        with resources.path("daily_fortune", "words.csv") as df:
            db = pd.read_csv(df, header=None)
        db.columns = ['text', 'tags_raw']
        db['tags'] = db['tags_raw'].apply(lambda x: str(x).split('|') if not pd.isna(x) else [])
        self.db = db[['text', 'tags']]


def main():
    epi = """Usage: tell_fortune [mode]
    """
    parser = argparse.ArgumentParser(description='A simple fortune cookie util',
                                     epilog=epi)
    parser.add_argument('mode', nargs='?', type=str, help='random, seasonal, or hybrid')
    
    args = parser.parse_args()
    mode = args.mode
    teller = FortuneTeller(mode)
    print(teller.tell())

if __name__ == "__main__":
    main()