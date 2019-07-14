import asyncio
import pathlib
import sqlite3
from pprint import pprint

import aiosqlite

dbname = pathlib.Path(__file__).parent / '34feba8fb61144dfb5cb9d4ecdd08683/storage.db'


def test_open():
    conn = sqlite3.connect(dbname)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT *  from frame WHERE document_id = 1')
    rows = list(map(dict, c.fetchall()))
    assert rows == [
        {'document_id': 1,
         'field_id': 2,
         'id': 1,
         'sequence': 0,
         'stored': '{"_field": "Other", "_positions": {}, "_sequence_number": 0, '
                   '"Aircraft": "Boeing 777-300ER", "Cabin Flown": "Economy Class", '
                   '"Date Flown": "2018-07-18T00:00:00", "Date Published": '
                   '"2018-05-07T00:00:00", "NPS": 8.0, "NPS Category": "Passive", '
                   '"Type Of Traveller": "Business", "\\u2063\\u2063file_id": 47, '
                   '"\\u2063\\u2063filename": "Airline-NPSv2018.xlsx", "_text": '
                   '"Flight began with very helpful and friendly ground staff in '
                   'Sydney. The flight was 20 minutes late but flying time made up '
                   'for the delay and got us in early. Similarly, the 777 was very '
                   'well maintained and the entertainment was remarkable. Dinner was '
                   "not up to it's expected standard however the refreshment that was "
                   'provided prior to landing was excellent and sufficient. The cabin '
                   'staff did an excellent job and I particularly observed how they '
                   'take very good care of toddlers."}'}
    ]

    c.execute('SELECT * from frame_posting WHERE frame_id = 1')
    pprint(c.description)
    rows = list(map(dict, c.fetchall()))
    assert rows == [
        {'frame_id': 1, 'position': 0, 'term_id': 194},
        {'frame_id': 1, 'position': 1, 'term_id': 1101},
        {'frame_id': 1, 'position': 2, 'term_id': 12},
        {'frame_id': 1, 'position': 3, 'term_id': 23},
        {'frame_id': 1, 'position': 4, 'term_id': 247},
        {'frame_id': 1, 'position': 5, 'term_id': 2},
        {'frame_id': 1, 'position': 6, 'term_id': 94},
        {'frame_id': 1, 'position': 7, 'term_id': 196},
        {'frame_id': 1, 'position': 8, 'term_id': 56},
        {'frame_id': 1, 'position': 9, 'term_id': 9},
        {'frame_id': 1, 'position': 10, 'term_id': 127},
        {'frame_id': 1, 'position': 11, 'term_id': 13},
        {'frame_id': 1, 'position': 12, 'term_id': 11},
        {'frame_id': 1, 'position': 13, 'term_id': 4},
        {'frame_id': 1, 'position': 14, 'term_id': 508},
        {'frame_id': 1, 'position': 15, 'term_id': 181},
        {'frame_id': 1, 'position': 16, 'term_id': 314},
        {'frame_id': 1, 'position': 17, 'term_id': 19},
        {'frame_id': 1, 'position': 18, 'term_id': 144},
        {'frame_id': 1, 'position': 19, 'term_id': 35},
        {'frame_id': 1, 'position': 20, 'term_id': 128},
        {'frame_id': 1, 'position': 21, 'term_id': 75},
        {'frame_id': 1, 'position': 22, 'term_id': 15},
        {'frame_id': 1, 'position': 23, 'term_id': 1},
        {'frame_id': 1, 'position': 24, 'term_id': 426},
        {'frame_id': 1, 'position': 25, 'term_id': 2},
        {'frame_id': 1, 'position': 26, 'term_id': 160},
        {'frame_id': 1, 'position': 27, 'term_id': 102},
        {'frame_id': 1, 'position': 28, 'term_id': 9},
        {'frame_id': 1, 'position': 29, 'term_id': 245},
        {'frame_id': 1, 'position': 30, 'term_id': 3817},
        {'frame_id': 1, 'position': 31, 'term_id': 1},
        {'frame_id': 1, 'position': 32, 'term_id': 276},
        {'frame_id': 1, 'position': 33, 'term_id': 4},
        {'frame_id': 1, 'position': 34, 'term_id': 23},
        {'frame_id': 1, 'position': 35, 'term_id': 98},
        {'frame_id': 1, 'position': 36, 'term_id': 940},
        {'frame_id': 1, 'position': 37, 'term_id': 2},
        {'frame_id': 1, 'position': 38, 'term_id': 1},
        {'frame_id': 1, 'position': 39, 'term_id': 57},
        {'frame_id': 1, 'position': 40, 'term_id': 4},
        {'frame_id': 1, 'position': 41, 'term_id': 1734},
        {'frame_id': 1, 'position': 42, 'term_id': 1344},
        {'frame_id': 1, 'position': 43, 'term_id': 4},
        {'frame_id': 1, 'position': 44, 'term_id': 18},
        {'frame_id': 1, 'position': 45, 'term_id': 75},
        {'frame_id': 1, 'position': 46, 'term_id': 3},
        {'frame_id': 1, 'position': 47, 'term_id': 17},
        {'frame_id': 1, 'position': 48, 'term_id': 350},
        {'frame_id': 1, 'position': 49, 'term_id': 177},
        {'frame_id': 1, 'position': 50, 'term_id': 313},
        {'frame_id': 1, 'position': 51, 'term_id': 1},
        {'frame_id': 1, 'position': 52, 'term_id': 2117},
        {'frame_id': 1, 'position': 53, 'term_id': 20},
        {'frame_id': 1, 'position': 54, 'term_id': 4},
        {'frame_id': 1, 'position': 55, 'term_id': 198},
        {'frame_id': 1, 'position': 56, 'term_id': 890},
        {'frame_id': 1, 'position': 57, 'term_id': 3},
        {'frame_id': 1, 'position': 58, 'term_id': 290},
        {'frame_id': 1, 'position': 59, 'term_id': 4},
        {'frame_id': 1, 'position': 60, 'term_id': 92},
        {'frame_id': 1, 'position': 61, 'term_id': 2},
        {'frame_id': 1, 'position': 62, 'term_id': 774},
        {'frame_id': 1, 'position': 63, 'term_id': 13},
        {'frame_id': 1, 'position': 64, 'term_id': 36},
        {'frame_id': 1, 'position': 65, 'term_id': 56},
        {'frame_id': 1, 'position': 66, 'term_id': 80},
        {'frame_id': 1, 'position': 67, 'term_id': 39},
        {'frame_id': 1, 'position': 68, 'term_id': 92},
        {'frame_id': 1, 'position': 69, 'term_id': 521},
        {'frame_id': 1, 'position': 70, 'term_id': 2},
        {'frame_id': 1, 'position': 71, 'term_id': 6},
        {'frame_id': 1, 'position': 72, 'term_id': 1276},
        {'frame_id': 1, 'position': 73, 'term_id': 5099},
        {'frame_id': 1, 'position': 74, 'term_id': 389},
        {'frame_id': 1, 'position': 75, 'term_id': 31},
        {'frame_id': 1, 'position': 76, 'term_id': 199},
        {'frame_id': 1, 'position': 77, 'term_id': 23},
        {'frame_id': 1, 'position': 78, 'term_id': 30},
        {'frame_id': 1, 'position': 79, 'term_id': 593},
        {'frame_id': 1, 'position': 80, 'term_id': 8},
        {'frame_id': 1, 'position': 81, 'term_id': 5740}
    ]

    conn.close()


def test_aio_open():
    sql = 'SELECT * from frame_posting WHERE frame_id = 1'

    async def test():
        async with aiosqlite.connect(dbname) as db:
            db.row_factory = sqlite3.Row
            async with db.execute(sql) as cursor:
                rows = list(map(dict, await cursor.fetchall()))
                return rows

    rows = asyncio.run(test())
    assert rows == [
        {'frame_id': 1, 'position': 0, 'term_id': 194},
        {'frame_id': 1, 'position': 1, 'term_id': 1101},
        {'frame_id': 1, 'position': 2, 'term_id': 12},
        {'frame_id': 1, 'position': 3, 'term_id': 23},
        {'frame_id': 1, 'position': 4, 'term_id': 247},
        {'frame_id': 1, 'position': 5, 'term_id': 2},
        {'frame_id': 1, 'position': 6, 'term_id': 94},
        {'frame_id': 1, 'position': 7, 'term_id': 196},
        {'frame_id': 1, 'position': 8, 'term_id': 56},
        {'frame_id': 1, 'position': 9, 'term_id': 9},
        {'frame_id': 1, 'position': 10, 'term_id': 127},
        {'frame_id': 1, 'position': 11, 'term_id': 13},
        {'frame_id': 1, 'position': 12, 'term_id': 11},
        {'frame_id': 1, 'position': 13, 'term_id': 4},
        {'frame_id': 1, 'position': 14, 'term_id': 508},
        {'frame_id': 1, 'position': 15, 'term_id': 181},
        {'frame_id': 1, 'position': 16, 'term_id': 314},
        {'frame_id': 1, 'position': 17, 'term_id': 19},
        {'frame_id': 1, 'position': 18, 'term_id': 144},
        {'frame_id': 1, 'position': 19, 'term_id': 35},
        {'frame_id': 1, 'position': 20, 'term_id': 128},
        {'frame_id': 1, 'position': 21, 'term_id': 75},
        {'frame_id': 1, 'position': 22, 'term_id': 15},
        {'frame_id': 1, 'position': 23, 'term_id': 1},
        {'frame_id': 1, 'position': 24, 'term_id': 426},
        {'frame_id': 1, 'position': 25, 'term_id': 2},
        {'frame_id': 1, 'position': 26, 'term_id': 160},
        {'frame_id': 1, 'position': 27, 'term_id': 102},
        {'frame_id': 1, 'position': 28, 'term_id': 9},
        {'frame_id': 1, 'position': 29, 'term_id': 245},
        {'frame_id': 1, 'position': 30, 'term_id': 3817},
        {'frame_id': 1, 'position': 31, 'term_id': 1},
        {'frame_id': 1, 'position': 32, 'term_id': 276},
        {'frame_id': 1, 'position': 33, 'term_id': 4},
        {'frame_id': 1, 'position': 34, 'term_id': 23},
        {'frame_id': 1, 'position': 35, 'term_id': 98},
        {'frame_id': 1, 'position': 36, 'term_id': 940},
        {'frame_id': 1, 'position': 37, 'term_id': 2},
        {'frame_id': 1, 'position': 38, 'term_id': 1},
        {'frame_id': 1, 'position': 39, 'term_id': 57},
        {'frame_id': 1, 'position': 40, 'term_id': 4},
        {'frame_id': 1, 'position': 41, 'term_id': 1734},
        {'frame_id': 1, 'position': 42, 'term_id': 1344},
        {'frame_id': 1, 'position': 43, 'term_id': 4},
        {'frame_id': 1, 'position': 44, 'term_id': 18},
        {'frame_id': 1, 'position': 45, 'term_id': 75},
        {'frame_id': 1, 'position': 46, 'term_id': 3},
        {'frame_id': 1, 'position': 47, 'term_id': 17},
        {'frame_id': 1, 'position': 48, 'term_id': 350},
        {'frame_id': 1, 'position': 49, 'term_id': 177},
        {'frame_id': 1, 'position': 50, 'term_id': 313},
        {'frame_id': 1, 'position': 51, 'term_id': 1},
        {'frame_id': 1, 'position': 52, 'term_id': 2117},
        {'frame_id': 1, 'position': 53, 'term_id': 20},
        {'frame_id': 1, 'position': 54, 'term_id': 4},
        {'frame_id': 1, 'position': 55, 'term_id': 198},
        {'frame_id': 1, 'position': 56, 'term_id': 890},
        {'frame_id': 1, 'position': 57, 'term_id': 3},
        {'frame_id': 1, 'position': 58, 'term_id': 290},
        {'frame_id': 1, 'position': 59, 'term_id': 4},
        {'frame_id': 1, 'position': 60, 'term_id': 92},
        {'frame_id': 1, 'position': 61, 'term_id': 2},
        {'frame_id': 1, 'position': 62, 'term_id': 774},
        {'frame_id': 1, 'position': 63, 'term_id': 13},
        {'frame_id': 1, 'position': 64, 'term_id': 36},
        {'frame_id': 1, 'position': 65, 'term_id': 56},
        {'frame_id': 1, 'position': 66, 'term_id': 80},
        {'frame_id': 1, 'position': 67, 'term_id': 39},
        {'frame_id': 1, 'position': 68, 'term_id': 92},
        {'frame_id': 1, 'position': 69, 'term_id': 521},
        {'frame_id': 1, 'position': 70, 'term_id': 2},
        {'frame_id': 1, 'position': 71, 'term_id': 6},
        {'frame_id': 1, 'position': 72, 'term_id': 1276},
        {'frame_id': 1, 'position': 73, 'term_id': 5099},
        {'frame_id': 1, 'position': 74, 'term_id': 389},
        {'frame_id': 1, 'position': 75, 'term_id': 31},
        {'frame_id': 1, 'position': 76, 'term_id': 199},
        {'frame_id': 1, 'position': 77, 'term_id': 23},
        {'frame_id': 1, 'position': 78, 'term_id': 30},
        {'frame_id': 1, 'position': 79, 'term_id': 593},
        {'frame_id': 1, 'position': 80, 'term_id': 8},
        {'frame_id': 1, 'position': 81, 'term_id': 5740}
    ]
