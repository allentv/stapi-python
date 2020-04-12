
from .full import *
from .base import *
from .full_response import *
from .base_response import *
from .search_criteria import *
try:
    from urllib.request import urlopen as urlopen
except ImportError:
    from urllib import urlopen as urlopen
from json import loads
import requests

class BaseEntity:
    entity_class = None
    entity_name = None

    def __init__(self, url, apiKey):
        self.url = url
        self.apiKey = apiKey

    def get(self, uid):
        url_to_open = self.url + "/api/v1/rest/" + self.entity_name + "?uid=" + uid
        fetched_data = urlopen(url_to_open)
        decoded_data = fetched_data.readlines()[0].decode("utf-8")
        parsed_data = loads(decoded_data)
        args_mapping = parsed_data[entity_name]
        return self.entity_class(**args_mapping)

    def search(self, searchCriteria):
        url_to_post = self.url + "/api/v1/rest/" + self.entity_name + "/search?pageNumber=" + str(searchCriteria.pageNumber) + "&" + str(searchCriteria.pageSize)
        data_to_post = searchCriteria.__dict__
        post_request = requests.post(url_to_post, data_to_post)
        response_text = post_request.text
        response_dict = loads(response_text)
        return response_dict

class Animal(BaseEntity):
    entity_class = AnimalFull
    entity_name = "animal"

class AstronomicalObject(BaseEntity):
    entity_class = AstronomicalObjectFull
    entity_name = "astronomicalObject"

class Book(BaseEntity):
    entity_class = BookFull
    entity_name = "book"

class BookCollection(BaseEntity):
    entity_class = BookCollectionFull
    entity_name = "bookCollection"

class BookSeries(BaseEntity):
    entity_class = BookSeriesFull
    entity_name = "bookSeries"

class Character(BaseEntity):
    entity_class = CharacterFull
    entity_name = "character"

class ComicCollection(BaseEntity):
    entity_class = ComicCollectionFull
    entity_name = "comicCollection"

class ComicSeries(BaseEntity):
    entity_class = ComicSeriesFull
    entity_name = "comicSeries"

class ComicStrip(BaseEntity):
    entity_class = ComicStripFull
    entity_name = "comicStrip"

class Comics(BaseEntity):
    entity_class = ComicsFull
    entity_name = "comics"

class Company(BaseEntity):
    entity_class = CompanyFull
    entity_name = "company"

class Conflict(BaseEntity):
    entity_class = ConflictFull
    entity_name = "conflict"

class Element(BaseEntity):
    entity_class = ElementFull
    entity_name = "element"

class Episode(BaseEntity):
    entity_class = EpisodeFull
    entity_name = "episode"

class Food(BaseEntity):
    entity_class = FoodFull
    entity_name = "food"

class Literature(BaseEntity):
    entity_class = LiteratureFull
    entity_name = "literature"

class Location(BaseEntity):
    entity_class = LocationFull
    entity_name = "location"

class Magazine(BaseEntity):
    entity_class = MagazineFull
    entity_name = "magazine"

class MagazineSeries(BaseEntity):
    entity_class = MagazineSeriesFull
    entity_name = "magazineSeries"

class Material(BaseEntity):
    entity_class = MaterialFull
    entity_name = "material"


class MedicalCondition(BaseEntity):
    entity_class = MedicalConditionFull
    entity_name = "medicalCondition"

class Movie(BaseEntity):
    entity_class = MovieFull
    entity_name = "movie"


class Occupation(BaseEntity):
    entity_class = OccupationFull
    entity_name = "occupation"

class Organization(BaseEntity):
    entity_class = OrganizationFull
    entity_name = "organization"


class Performer(BaseEntity):
    entity_class = PerformerFull
    entity_name = "performer"


class Season(BaseEntity):
    entity_class = SeasonFull
    entity_name = "season"


class Series(BaseEntity):
    entity_class = SeriesFull
    entity_name = "series"

class Soundtrack(BaseEntity):
    entity_class = SoundtrackFull
    entity_name = "soundtrack"


class Spacecraft(BaseEntity):
    entity_class = SpacecraftFull
    entity_name = "spacecraft"

class SpacecraftClass(BaseEntity):
    entity_class = SpacecraftClassFull
    entity_name = "spacecraftClass"

class Species(BaseEntity):
    entity_class = SpeciesFull
    entity_name = "species"

class Staff(BaseEntity):
    entity_class = StaffFull
    entity_name = "staff"

class Technology(BaseEntity):
    entity_class = TechnologyFull
    entity_name = "technology"

class Title(BaseEntity):
    entity_class = TitleFull
    entity_name = "title"

class TradingCard(BaseEntity):
    entity_class = TradingCardFull
    entity_name = "tradingCard"

class TradingCardDeck(BaseEntity):
    entity_class = TradingCardDeckFull
    entity_name = "tradingCardDeck"

class TradingCardSet(BaseEntity):
    entity_class = TradingCardSetFull
    entity_name = "tradingCardSet"

class VideoGame(BaseEntity):
    entity_class = VideoGameFull
    entity_name = "videoGame"

class VideoRelease(BaseEntity):
    entity_class = VideoReleaseFull
    entity_name = "videoRelease"

class Weapon(BaseEntity):
    entity_class = WeaponFull
    entity_name = "weapon"
