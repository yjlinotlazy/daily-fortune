import argparse
import pandas as pd
from importlib import resources

class FortuneTeller:
    def __init__(self, mode: str = 'random', maxlen: int = 0) -> None:
        self.mode = mode
        self.maxlen = maxlen
        self._read_db()
    
    def set_mode(self, mode: str) -> None:
        self.mode = mode

    def tell(self) -> str:
        candidates = self.db
        if self.maxlen > 0:
            candidates = candidates[candidates.charlen <= self.maxlen]
        if candidates.shape[0] == 0:
            return 'No fortune'
        selected = candidates.sample(n=1)
        return selected['text'].iloc[0]
    
    def _read_db(self):
        with resources.path("daily_fortune", "words.csv") as df:
            db = pd.read_csv(df, header=None)
        db.columns = ['text', 'tags_raw']
        db['charlen'] = db['text'].apply(lambda x: len(x))
        db['tags'] = db['tags_raw'].apply(lambda x: str(x).split('|') if not pd.isna(x) else [])
        self.db = db[['text', 'tags', 'charlen']]


def main():
    epi = """Usage: tell_fortune [mode]
    """
    parser = argparse.ArgumentParser(description='A simple fortune cookie util',
                                     epilog=epi)
    parser.add_argument('mode', nargs='?', type=str, help='random, seasonal, or hybrid')
    parser.add_argument('--maxlen', nargs='?', type=str, help='max number of characters')
    
    args = parser.parse_args()
    mode = args.mode
    maxlen = args.maxlen if args.maxlen else 0
    teller = FortuneTeller(mode, int(maxlen))
    print(teller.tell())

if __name__ == "__main__":
    main()