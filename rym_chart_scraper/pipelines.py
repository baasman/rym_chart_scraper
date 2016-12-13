from rym_chart_scraper.models import TopAlbums, db_connect, create_topalbums_table
from rym_chart_scraper.models import WorstAlbums, create_worstalbums_table
from sqlalchemy.orm import sessionmaker


class TopAlbumPipeline:
    def __init__(self):
        engine = db_connect()
        create_topalbums_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        topalbums = TopAlbums(**item)

        try:
            session.add(topalbums)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item


class WorstAlbumPipeline:
    def __init__(self):
        engine = db_connect()
        create_worstalbums_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        topalbums = WorstAlbums(**item)

        try:
            session.add(topalbums)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
