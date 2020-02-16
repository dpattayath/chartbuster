import pandas as pd

class CsvDataProcessor():

    def __init__(self, fileToLoad):
        self.fileToLoad =fileToLoad

    def process(self):
        df = pd.read_csv(self.fileToLoad,
            encoding="ISO-8859-1",
            index_col="year",
            na_filter=False,
            skip_blank_lines=True,
            usecols=['title','artist', 'top genre', 'year', 'bpm', 'pop']
        )
        self.dataFrame = df.rename(columns={"top genre": "genre", "pop": "popularity"})

    """
    get data grouped based on year and artist and get the top 1
    """
    def artistsByYear(self) -> pd.DataFrame:
        artistsByYear = self.dataFrame.groupby(["year", "artist"]).count().sort_values(['year', 'title'], ascending=False)
        artistsByYear = artistsByYear.groupby("year").head(1)[["title"]]
        return artistsByYear.reset_index()

    """
    get data grouped based on year and genre and get the top 1
    """
    def genreByYear(self) -> pd.DataFrame:
        genreByYear = self.dataFrame.groupby(["year", "genre"]).count().sort_values(['year', 'title'], ascending=False)
        genreByYear = genreByYear.groupby("year").head(1)[["title"]]
        return genreByYear.reset_index()

    """
    get data grouped based on year and popularity and get the top 1
    """
    def songByYear(self) -> pd.DataFrame:
        songByYear = self.dataFrame.groupby(["year"]).max().sort_values(['year', "popularity"], ascending=False)
        songByYear = songByYear.groupby("year").head(1)[["title", "popularity"]]
        return songByYear.reset_index()
