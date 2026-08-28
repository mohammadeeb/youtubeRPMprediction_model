COUNTRY_TIERS = {
    # Level 1: High CPM
    "united states": 1, "canada": 1, "united kingdom": 1, "australia": 1, "new zealand": 1,
    "germany": 1, "switzerland": 1, "norway": 1, "denmark": 1, "sweden": 1, "finland": 1,
    "netherlands": 1, "belgium": 1, "austria": 1, "ireland": 1, "luxembourg": 1, "iceland": 1,
    "france": 1, "italy": 1, "spain": 1, "israel": 1,
    "singapore": 1, "japan": 1, "south korea": 1, "hong kong": 1, "taiwan": 1,
    "saudi arabia": 1, "united arab emirates": 1, "qatar": 1, "kuwait": 1, "liechtenstein": 1,
    "monaco": 1, "bermuda": 1, "cayman islands": 1, "gibraltar": 1,

    # Level 2: Medium CPM
    "oman": 2, "bahrain": 2, "jordan": 2, "lebanon": 2, "egypt": 2, "morocco": 2, 
    "tunisia": 2, "algeria": 2, "turkey": 2, "portugal": 2, "greece": 2, "poland": 2, 
    "czech republic": 2, "czechia": 2, "hungary": 2, "slovakia": 2, "romania": 2, 
    "croatia": 2, "bulgaria": 2, "slovenia": 2, "estonia": 2, "latvia": 2, "lithuania": 2, 
    "cyprus": 2, "malta": 2, "serbia": 2, "russia": 2, "mexico": 2, "brazil": 2, 
    "argentina": 2, "chile": 2, "colombia": 2, "peru": 2, "uruguay": 2, "costa rica": 2, 
    "panama": 2, "puerto rico": 2, "dominican republic": 2, "china": 2, "malaysia": 2, 
    "thailand": 2, "south africa": 2,

    # Level 3: Low CPM
    "india": 3, "pakistan": 3, "bangladesh": 3, "nepal": 3, "sri lanka": 3, "afghanistan": 3, "maldives": 3,
    "indonesia": 3, "philippines": 3, "vietnam": 3, "myanmar": 3, "cambodia": 3, "laos": 3, 
    "brunei": 3, "east timor": 3, "iraq": 3, "yemen": 3, "syria": 3, "sudan": 3, "libya": 3, 
    "mauritania": 3, "palestine": 3, "somalia": 3, "nigeria": 3, "kenya": 3, "ghana": 3, 
    "ethiopia": 3, "uganda": 3, "tanzania": 3, "cameroon": 3, "ivory coast": 3, "senegal": 3, 
    "zambia": 3, "zimbabwe": 3, "angola": 3, "mozambique": 3, "rwanda": 3, "dr congo": 3, 
    "republic of the congo": 3, "gabon": 3, "mali": 3, "burkina faso": 3, "niger": 3, 
    "chad": 3, "guinea": 3, "benin": 3, "togo": 3, "sierra leone": 3, "liberia": 3, 
    "malawi": 3, "namibia": 3, "botswana": 3, "madagascar": 3, "mauritius": 3, "eswatini": 3, 
    "lesotho": 3, "djibouti": 3, "eritrea": 3, "gambia": 3, "central african republic": 3, 
    "burundi": 3, "south sudan": 3, "cape verde": 3, "ukraine": 3, "belarus": 3, "kazakhstan": 3, 
    "uzbekistan": 3, "azerbaijan": 3, "georgia": 3, "armenia": 3, "moldova": 3, "kyrgyzstan": 3, 
    "tajikistan": 3, "turkmenistan": 3, "albania": 3, "north macedonia": 3, 
    "bosnia and herzegovina": 3, "montenegro": 3, "kosovo": 3, "ecuador": 3, "bolivia": 3, 
    "paraguay": 3, "venezuela": 3, "guatemala": 3, "honduras": 3, "el salvador": 3, 
    "nicaragua": 3, "haiti": 3, "jamaica": 3, "cuba": 3, "trinidad and tobago": 3, 
    "bahamas": 3, "guyana": 3, "suriname": 3, "belize": 3, "barbados": 3, "mongolia": 3, 
    "fiji": 3, "papua new guinea": 3
}

def get_country_level(country_name):
    if not country_name:
        return None
    return COUNTRY_TIERS.get(country_name.strip().lower(), None)