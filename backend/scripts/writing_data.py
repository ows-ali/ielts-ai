"""Writing Task 1 practice questions and sample answers.

This module contains high-quality IELTS Academic Writing Task 1 content:
- 26 questions across all 7 question types
- 3 sample answers per question (Band 5, 7, 9)
Each sample includes sub-scores, an explanation of why it is at that band,
and specific improvement tips.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Questions
# ---------------------------------------------------------------------------

QUESTIONS: list[dict] = [
    # ---------- LINE GRAPHS (4) ----------
    {
        "type": "line",
        "title": "CO2 Emissions by Country (1960-2020)",
        "difficulty": "easy",
        "prompt": (
            "The line graph below shows the carbon dioxide (CO2) emissions per capita "
            "in the USA, China, and India between 1960 and 2020.\n\n"
            "Summarise the information by selecting and reporting the main features, "
            "and make comparisons where relevant.\n\n"
            "Write at least 150 words."
        ),
        "data_description": {
            "type": "line",
            "x_axis": [1960, 1970, 1980, 1990, 2000, 2010, 2020],
            "unit": "tonnes per person",
            "series": [
                {"name": "USA", "data": [12.5, 14.0, 15.2, 14.8, 15.5, 15.0, 13.1]},
                {"name": "China", "data": [1.0, 1.3, 1.6, 2.2, 3.1, 6.8, 8.5]},
                {"name": "India", "data": [0.4, 0.5, 0.6, 0.8, 1.1, 1.6, 1.9]},
            ],
        },
    },
    {
        "type": "line",
        "title": "Global Average Temperature Change",
        "difficulty": "medium",
        "prompt": (
            "The line graph below shows the change in global average temperature "
            "compared with the 1951-1980 average between 1900 and 2020.\n\n"
            "Summarise the information by selecting and reporting the main features, "
            "and make comparisons where relevant.\n\n"
            "Write at least 150 words."
        ),
        "data_description": {
            "type": "line",
            "x_axis": [1900, 1920, 1940, 1960, 1980, 2000, 2020],
            "unit": "degrees Celsius change",
            "series": [
                {"name": "Temperature change", "data": [-0.30, -0.28, -0.05, 0.02, 0.27, 0.43, 0.98]},
            ],
        },
    },
    {
        "type": "line",
        "title": "Internet Users Worldwide by Region",
        "difficulty": "medium",
        "prompt": (
            "The line graph below shows the number of internet users by region "
            "from 2000 to 2020.\n\n"
            "Summarise the information by selecting and reporting the main features, "
            "and make comparisons where relevant.\n\n"
            "Write at least 150 words."
        ),
        "data_description": {
            "type": "line",
            "x_axis": [2000, 2005, 2010, 2015, 2020],
            "unit": "millions of users",
            "series": [
                {"name": "Asia", "data": [80, 320, 830, 1570, 2500]},
                {"name": "Europe", "data": [90, 290, 470, 620, 730]},
                {"name": "Africa", "data": [3, 25, 110, 290, 570]},
                {"name": "Americas", "data": [120, 240, 420, 550, 620]},
            ],
        },
    },
    {
        "type": "line",
        "title": "Coffee and Tea Consumption in the UK",
        "difficulty": "hard",
        "prompt": (
            "The line graph below shows the amount of coffee and tea consumed per "
            "person in the United Kingdom between 1980 and 2015.\n\n"
            "Summarise the information by selecting and reporting the main features, "
            "and make comparisons where relevant.\n\n"
            "Write at least 150 words."
        ),
        "data_description": {
            "type": "line",
            "x_axis": [1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015],
            "unit": "kg per person per year",
            "series": [
                {"name": "Coffee", "data": [2.0, 2.3, 2.8, 3.2, 3.0, 3.4, 3.6, 3.8]},
                {"name": "Tea", "data": [2.8, 2.5, 2.4, 2.0, 1.8, 1.6, 1.5, 1.4]},
            ],
        },
    },
    # ---------- BAR CHARTS (4) ----------
    {
        "type": "bar",
        "title": "Household Expenditure by Category",
        "difficulty": "easy",
        "prompt": (
            "The bar chart below shows the average monthly household expenditure "
            "by category in one country in 2010 and 2020.\n\n"
            "Summarise the information by selecting and reporting the main features, "
            "and make comparisons where relevant.\n\n"
            "Write at least 150 words."
        ),
        "data_description": {
            "type": "bar",
            "categories": ["Housing", "Food", "Transport", "Education", "Health"],
            "unit": "USD per month",
            "series": [
                {"name": "2010", "data": [800, 420, 250, 180, 120]},
                {"name": "2020", "data": [1100, 520, 300, 350, 260]},
            ],
        },
    },
    {
        "type": "bar",
        "title": "University Students by Subject",
        "difficulty": "medium",
        "prompt": (
            "The bar chart below shows the percentage of university students "
            "studying different subjects in 2010 and 2020.\n\n"
            "Summarise the information by selecting and reporting the main features, "
            "and make comparisons where relevant.\n\n"
            "Write at least 150 words."
        ),
        "data_description": {
            "type": "bar",
            "categories": ["Engineering", "Business", "Medicine", "Arts", "Law"],
            "unit": "percentage of students",
            "series": [
                {"name": "2010", "data": [22, 25, 15, 20, 18]},
                {"name": "2020", "data": [30, 28, 18, 12, 12]},
            ],
        },
    },
    {
        "type": "bar",
        "title": "Weekly Time Spent on Activities by Age",
        "difficulty": "medium",
        "prompt": (
            "The bar chart below shows the average number of hours per week spent "
            "on different activities by three age groups.\n\n"
            "Summarise the information by selecting and reporting the main features, "
            "and make comparisons where relevant.\n\n"
            "Write at least 150 words."
        ),
        "data_description": {
            "type": "bar",
            "categories": ["Working", "Sleeping", "Leisure", "Exercise"],
            "unit": "hours per week",
            "series": [
                {"name": "18-35", "data": [42, 49, 20, 5]},
                {"name": "36-55", "data": [40, 48, 15, 4]},
                {"name": "55+", "data": [10, 51, 38, 7]},
            ],
        },
    },
    {
        "type": "bar",
        "title": "Car Production by Country",
        "difficulty": "hard",
        "prompt": (
            "The bar chart below shows the number of cars produced in four countries "
            "in 2000 and 2020.\n\n"
            "Summarise the information by selecting and reporting the main features, "
            "and make comparisons where relevant.\n\n"
            "Write at least 150 words."
        ),
        "data_description": {
            "type": "bar",
            "categories": ["Japan", "Germany", "China", "USA"],
            "unit": "millions of cars",
            "series": [
                {"name": "2000", "data": [8.4, 5.5, 2.0, 5.7]},
                {"name": "2020", "data": [6.8, 3.7, 25.3, 2.3]},
            ],
        },
    },
    # ---------- PIE CHARTS (3) ----------
    {
        "type": "pie",
        "title": "Energy Production by Source",
        "difficulty": "easy",
        "prompt": (
            "The pie chart below shows the share of different energy sources "
            "in total energy production in 2020.\n\n"
            "Summarise the information by selecting and reporting the main features, "
            "and make comparisons where relevant.\n\n"
            "Write at least 150 words."
        ),
        "data_description": {
            "type": "pie",
            "unit": "percentage of production",
            "slices": [
                {"label": "Coal", "value": 35},
                {"label": "Natural gas", "value": 28},
                {"label": "Renewables", "value": 20},
                {"label": "Nuclear", "value": 12},
                {"label": "Oil", "value": 5},
            ],
        },
    },
    {
        "type": "pie",
        "title": "Water Usage by Sector",
        "difficulty": "medium",
        "prompt": (
            "The pie charts below show the percentage of water used for different "
            "purposes in two years, 2010 and 2020.\n\n"
            "Summarise the information by selecting and reporting the main features, "
            "and make comparisons where relevant.\n\n"
            "Write at least 150 words."
        ),
        "data_description": {
            "type": "multi",
            "charts": [
                {
                    "type": "pie",
                    "title": "2010",
                    "slices": [
                        {"label": "Agriculture", "value": 70},
                        {"label": "Industry", "value": 20},
                        {"label": "Domestic", "value": 10},
                    ],
                },
                {
                    "type": "pie",
                    "title": "2020",
                    "slices": [
                        {"label": "Agriculture", "value": 55},
                        {"label": "Industry", "value": 30},
                        {"label": "Domestic", "value": 15},
                    ],
                },
            ],
        },
    },
    {
        "type": "pie",
        "title": "Student Enrolment by Faculty",
        "difficulty": "medium",
        "prompt": (
            "The pie charts below show the proportion of students enrolled in "
            "different faculties at a university in 2015 and 2025.\n\n"
            "Summarise the information by selecting and reporting the main features, "
            "and make comparisons where relevant.\n\n"
            "Write at least 150 words."
        ),
        "data_description": {
            "type": "multi",
            "charts": [
                {
                    "type": "pie",
                    "title": "2015",
                    "slices": [
                        {"label": "Science", "value": 25},
                        {"label": "Business", "value": 30},
                        {"label": "Engineering", "value": 20},
                        {"label": "Humanities", "value": 25},
                    ],
                },
                {
                    "type": "pie",
                    "title": "2025",
                    "slices": [
                        {"label": "Science", "value": 35},
                        {"label": "Business", "value": 28},
                        {"label": "Engineering", "value": 22},
                        {"label": "Humanities", "value": 15},
                    ],
                },
            ],
        },
    },
    # ---------- TABLES (3) ----------
    {
        "type": "table",
        "title": "Underground Railway Systems in Six Cities",
        "difficulty": "easy",
        "prompt": (
            "The table below gives information about the underground railway systems "
            "in six cities.\n\n"
            "Summarise the information by selecting and reporting the main features, "
            "and make comparisons where relevant.\n\n"
            "Write at least 150 words."
        ),
        "data_description": {
            "type": "table",
            "columns": ["City", "Year opened", "Total length (km)", "Passengers per year (millions)"],
            "rows": [
                ["London", "1863", "408", "1400"],
                ["Paris", "1900", "214", "1500"],
                ["Tokyo", "1927", "305", "3200"],
                ["New York", "1904", "373", "1700"],
                ["Moscow", "1935", "397", "2400"],
                ["Beijing", "1971", "699", "3800"],
            ],
        },
    },
    {
        "type": "table",
        "title": "Tourism Statistics for Five Countries",
        "difficulty": "medium",
        "prompt": (
            "The table below gives information about tourism in five countries.\n\n"
            "Summarise the information by selecting and reporting the main features, "
            "and make comparisons where relevant.\n\n"
            "Write at least 150 words."
        ),
        "data_description": {
            "type": "table",
            "columns": ["Country", "International visitors (millions)", "Revenue (US$ billion)", "Average stay (nights)"],
            "rows": [
                ["France", "89", "66", "6.5"],
                ["Spain", "84", "92", "9.1"],
                ["Thailand", "39", "63", "9.8"],
                ["Mexico", "41", "24", "8.2"],
                ["Turkey", "51", "34", "10.4"],
            ],
        },
    },
    {
        "type": "table",
        "title": "Household Electricity Consumption by Appliance",
        "difficulty": "hard",
        "prompt": (
            "The table below shows the percentage of household electricity consumed "
            "by different appliances in 2000 and 2020.\n\n"
            "Summarise the information by selecting and reporting the main features, "
            "and make comparisons where relevant.\n\n"
            "Write at least 150 words."
        ),
        "data_description": {
            "type": "table",
            "columns": ["Appliance", "2000 (%)", "2020 (%)", "Change (percentage points)"],
            "rows": [
                ["Air conditioning", "12", "24", "+12"],
                ["Refrigeration", "15", "13", "-2"],
                ["Lighting", "18", "8", "-10"],
                ["Electronics", "20", "31", "+11"],
                ["Water heating", "22", "16", "-6"],
                ["Other", "13", "8", "-5"],
            ],
        },
    },
    # ---------- MAPS (4) ----------
    {
        "type": "map",
        "title": "Island Before and After Tourist Development",
        "difficulty": "easy",
        "prompt": (
            "The two maps below show an island before and after the construction of "
            "some tourist facilities.\n\n"
            "Summarise the information by selecting and reporting the main features, "
            "and make comparisons where relevant.\n\n"
            "Write at least 150 words."
        ),
        "image_url": "writing-images/island-before-after.png",
        "data_description": {
            "type": "map",
            "maps": ["Before", "After"],
            "before": ["A small island with beach on the west coast, dense trees in the centre, and a small bay on the south coast."],
            "after": [
                "Two accommodation areas in the west and south-east of the island.",
                "A reception block and restaurant in the north-west.",
                "A pier in the south-west with a main road linking it to the reception.",
                "Footpaths connecting the accommodation and the beach.",
                "A swimming area near the beach on the west coast.",
            ],
        },
    },
    {
        "type": "map",
        "title": "Town Centre Changes 1990 to 2020",
        "difficulty": "medium",
        "prompt": (
            "The maps below show the centre of a small town in 1990 and in 2020.\n\n"
            "Summarise the information by selecting and reporting the main features, "
            "and make comparisons where relevant.\n\n"
            "Write at least 150 words."
        ),
        "image_url": "writing-images/town-centre.png",
        "data_description": {
            "type": "map",
            "maps": ["1990", "2020"],
            "before": [
                "A market square in the centre with a car park to the north.",
                "A factory and residential housing in the west.",
                "A train station and industrial area in the south.",
                "Housing estates in the east and north-east.",
            ],
            "after": [
                "The car park replaced by a shopping centre.",
                "The factory demolished and replaced by a supermarket and car park.",
                "The industrial area converted into a business park.",
                "New housing developments in the west and south.",
                "The main road widened and pedestrianised in the centre.",
            ],
        },
    },
    {
        "type": "map",
        "title": "Seaside Village Development",
        "difficulty": "medium",
        "prompt": (
            "The maps below show the development of a seaside village between 1985 "
            "and 2025.\n\n"
            "Summarise the information by selecting and reporting the main features, "
            "and make comparisons where relevant.\n\n"
            "Write at least 150 words."
        ),
        "image_url": "writing-images/seaside-village.png",
        "data_description": {
            "type": "map",
            "maps": ["1985", "2025"],
            "before": [
                "A small fishing village with scattered houses along the coast.",
                "Farmland behind the village.",
                "A single access road from the mainland.",
                "A small harbour and beach in the west.",
            ],
            "after": [
                "The village expanded inland with new housing estates and a hotel complex.",
                "The farmland largely replaced by hotels and a golf course.",
                "A new marina and promenade built along the beach.",
                "A second access road and car parks constructed.",
                "Shops, restaurants and an entertainment centre added.",
            ],
        },
    },
    {
        "type": "map",
        "title": "University Campus Expansion",
        "difficulty": "hard",
        "prompt": (
            "The maps below show a university campus in 2005 and in 2025.\n\n"
            "Summarise the information by selecting and reporting the main features, "
            "and make comparisons where relevant.\n\n"
            "Write at least 150 words."
        ),
        "image_url": "writing-images/university-campus.png",
        "data_description": {
            "type": "map",
            "maps": ["2005", "2025"],
            "before": [
                "A main entrance in the north with a car park.",
                "Lecture halls and a library in the centre.",
                "Student accommodation blocks in the east.",
                "A sports field in the south.",
                "A park and woodland in the west.",
            ],
            "after": [
                "The car park replaced by a new student centre.",
                "Two additional lecture halls built in the centre.",
                "New accommodation blocks in the north-east.",
                "The sports field upgraded with an indoor sports complex.",
                "The park converted into a research and technology park.",
                "A new bus route and cycle paths added.",
            ],
        },
    },
    # ---------- PROCESSES (4) ----------
    {
        "type": "process",
        "title": "The Water Cycle",
        "difficulty": "easy",
        "prompt": (
            "The diagram below shows the water cycle.\n\n"
            "Summarise the information by selecting and reporting the main features, "
            "and make comparisons where relevant.\n\n"
            "Write at least 150 words."
        ),
        "image_url": "writing-images/water-cycle.png",
        "data_description": {
            "type": "process",
            "title": "The water cycle",
            "steps": [
                "Energy from the sun heats the surface of the ocean.",
                "Water evaporates and rises as water vapour.",
                "Water vapour cools and condenses to form clouds.",
                "Rain falls from the clouds as precipitation.",
                "Water runs over the land into rivers and lakes.",
                "Water flows back into the ocean, completing the cycle.",
            ],
        },
    },
    {
        "type": "process",
        "title": "Cement Production",
        "difficulty": "medium",
        "prompt": (
            "The diagrams below show the stages and equipment used in the cement-making "
            "process and how cement is used to produce concrete for building purposes.\n\n"
            "Summarise the information by selecting and reporting the main features, "
            "and make comparisons where relevant.\n\n"
            "Write at least 150 words."
        ),
        "image_url": "writing-images/cement-production.png",
        "data_description": {
            "type": "process",
            "title": "Cement and concrete production",
            "steps": [
                "Limestone and clay are crushed to form a powder.",
                "The powder is mixed together.",
                "The mixture passes through a rotating heater.",
                "It is ground in a mill to produce cement powder.",
                "Cement is packed into bags.",
                "To make concrete, cement is combined with water, sand and gravel in a mixer.",
            ],
        },
    },
    {
        "type": "process",
        "title": "Glass Recycling",
        "difficulty": "medium",
        "prompt": (
            "The diagram below shows the recycling process of glass bottles.\n\n"
            "Summarise the information by selecting and reporting the main features, "
            "and make comparisons where relevant.\n\n"
            "Write at least 150 words."
        ),
        "image_url": "writing-images/glass-recycling.png",
        "data_description": {
            "type": "process",
            "title": "Glass bottle recycling",
            "steps": [
                "Used glass bottles are placed in recycling collection bins.",
                "Bottles are collected and transported to a recycling plant.",
                "Glass is washed to remove impurities and sorted by colour.",
                "Sorted glass is crushed into small fragments called cullet.",
                "Cullet is melted in a high-temperature furnace.",
                "Liquid glass is moulded into new bottles and jars.",
                "New glass products are distributed to shops for consumer use.",
            ],
        },
    },
    {
        "type": "process",
        "title": "Hydroelectric Power Generation",
        "difficulty": "hard",
        "prompt": (
            "The diagram below shows how electricity is generated in a hydroelectric power station.\n\n"
            "Summarise the information by selecting and reporting the main features, "
            "and make comparisons where relevant.\n\n"
            "Write at least 150 words."
        ),
        "image_url": "writing-images/hydroelectric-power.png",
        "data_description": {
            "type": "process",
            "title": "Hydroelectric power generation",
            "steps": [
                "Water is collected and stored in a high-level reservoir behind a dam.",
                "Water flows down through an intake gate into a penstock pipe.",
                "The force of the flowing water spins a turbine at high speed.",
                "The spinning turbine drives a generator to produce electricity.",
                "A transformer converts the electrical voltage for long-distance transport.",
                "Power lines distribute electricity across the national grid.",
                "Water exits the turbine and discharges back into the river downstream.",
            ],
        },
    },
    # ---------- MULTIPLE CHARTS (4) ----------
    {
        "type": "multi",
        "title": "Cinema Attendance and Ticket Prices",
        "difficulty": "easy",
        "prompt": (
            "The line graph below shows cinema attendance in the UK between 2010 and "
            "2020, and the bar chart shows the average cinema ticket price over the "
            "same period.\n\n"
            "Summarise the information by selecting and reporting the main features, "
            "and make comparisons where relevant.\n\n"
            "Write at least 150 words."
        ),
        "data_description": {
            "type": "multi",
            "charts": [
                {
                    "type": "line",
                    "title": "Cinema attendance",
                    "x_axis": [2010, 2012, 2014, 2016, 2018, 2020],
                    "unit": "millions of visits",
                    "series": [{"name": "Attendance", "data": [170, 160, 175, 180, 190, 80]}],
                },
                {
                    "type": "bar",
                    "title": "Average ticket price",
                    "categories": ["2010", "2014", "2018", "2020"],
                    "unit": "GBP",
                    "series": [{"name": "Price", "data": [6.2, 7.0, 7.8, 9.1]}],
                },
            ],
        },
    },
    {
        "type": "multi",
        "title": "Energy Sources and Consumption by Sector",
        "difficulty": "medium",
        "prompt": (
            "The pie chart below shows the sources of electricity in one country, and "
            "the bar chart shows electricity consumption by sector in the same year.\n\n"
            "Summarise the information by selecting and reporting the main features, "
            "and make comparisons where relevant.\n\n"
            "Write at least 150 words."
        ),
        "data_description": {
            "type": "multi",
            "charts": [
                {
                    "type": "pie",
                    "title": "Electricity sources",
                    "slices": [
                        {"label": "Coal", "value": 30},
                        {"label": "Gas", "value": 25},
                        {"label": "Hydro", "value": 20},
                        {"label": "Nuclear", "value": 15},
                        {"label": "Renewables", "value": 10},
                    ],
                },
                {
                    "type": "bar",
                    "title": "Consumption by sector",
                    "categories": ["Industry", "Residential", "Commercial", "Agriculture"],
                    "unit": "TWh",
                    "series": [{"name": "Consumption", "data": [450, 320, 280, 60]}],
                },
            ],
        },
    },
    {
        "type": "multi",
        "title": "International Students at a University",
        "difficulty": "medium",
        "prompt": (
            "The table below shows the number of international students at a university "
            "by region of origin, and the pie chart shows the proportion studying in "
            "each faculty in 2020.\n\n"
            "Summarise the information by selecting and reporting the main features, "
            "and make comparisons where relevant.\n\n"
            "Write at least 150 words."
        ),
        "data_description": {
            "type": "multi",
            "charts": [
                {
                    "type": "table",
                    "title": "International students by region",
                    "columns": ["Region", "2015", "2020"],
                    "rows": [
                        ["Asia", "1200", "2100"],
                        ["Europe", "900", "950"],
                        ["Africa", "400", "650"],
                        ["Americas", "500", "550"],
                    ],
                },
                {
                    "type": "pie",
                    "title": "Faculty distribution 2020",
                    "slices": [
                        {"label": "Engineering", "value": 35},
                        {"label": "Business", "value": 28},
                        {"label": "Science", "value": 22},
                        {"label": "Humanities", "value": 15},
                    ],
                },
            ],
        },
    },
    {
        "type": "multi",
        "title": "Town Development and Population Growth",
        "difficulty": "hard",
        "prompt": (
            "The map below shows the development of a town between 1990 and 2020, and "
            "the table shows its population growth over the same period.\n\n"
            "Summarise the information by selecting and reporting the main features, "
            "and make comparisons where relevant.\n\n"
            "Write at least 150 words."
        ),
        "image_url": "writing-images/town-population.png",
        "data_description": {
            "type": "multi",
            "charts": [
                {
                    "type": "map",
                    "title": "Town development",
                    "maps": ["1990", "2020"],
                    "before": [
                        "A small town centre with a railway station in the south.",
                        "Farmland surrounding the town.",
                        "One main road from north to south.",
                    ],
                    "after": [
                        "The town expanded north and west with new housing.",
                        "An industrial park built in the east.",
                        "A ring road added around the town.",
                        "A new shopping centre built near the station.",
                    ],
                },
                {
                    "type": "table",
                    "title": "Population",
                    "columns": ["Year", "1990", "2000", "2010", "2020"],
                    "rows": [["Population", "12000", "18000", "32000", "55000"]],
                },
            ],
        },
    },
]

# ---------------------------------------------------------------------------
# Sample answers. Keyed by question index -> {band: sample}
# ---------------------------------------------------------------------------

SAMPLES: dict[int, dict[str, dict]] = {
    # ---------------- Q0: CO2 Emissions ----------------
    0: {
        "5": {
            "band": 5,
            "answer_text": (
                "The line graph shows CO2 emissions in the USA, China and India from 1960 to 2020.\n"
                "The USA has high CO2. It was about 12.5 in 1960 and it went up to 15.2 in 1980. "
                "After that it is around 15 until 2010, and it goes down to 13.1 in 2020. "
                "China was very low in 1960, only 1.0. It increased slowly to 3.1 in 2000. "
                "Then it went up very fast to 8.5 in 2020. "
                "India is the lowest. It was 0.4 in 1960 and it increase to 1.9 in 2020.\n"
                "Overall, the USA has the most emissions, but China grow very fast in the last years."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "This answer covers the data with accurate figures, but it only describes the "
                "series one by one rather than grouping information or making strong comparisons. "
                "The overall trend is stated but not developed with key highlights."
            ),
            "improvement_tips": [
                "Add a clear overview paragraph describing the two main trends (USA high but falling; China rising sharply).",
                "Group information by similarity instead of describing each line in turn.",
                "Use comparative language such as 'considerably higher than' or 'at a similar level'.",
                "Fix basic grammar errors: 'it increase' should be 'it increased'; 'grow' should be 'grew'.",
                "Use more precise vocabulary: 'emissions climbed steadily', 'peaked', 'levelled off'.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "The line graph illustrates how per-capita CO2 emissions changed in the USA, "
                "China and India between 1960 and 2020.\n"
                "Overall, the USA consistently produced far more emissions per person than the "
                "other two countries throughout the period, although its level declined in the "
                "final decades. By contrast, China experienced a dramatic increase, especially "
                "after 2000, while India remained the lowest emitter throughout.\n"
                "In 1960, US emissions stood at around 12.5 tonnes per person. They rose to a "
                "peak of roughly 15.2 tonnes in 1980, fluctuated around 15 tonnes until 2010, "
                "and then fell to 13.1 tonnes in 2020. China began at just 1.0 tonne in 1960 "
                "and increased gradually to 3.1 tonnes by 2000, before rising steeply to 8.5 "
                "tonnes twenty years later. India's figures remained low throughout, growing "
                "from 0.4 tonnes in 1960 to only 1.9 tonnes in 2020.\n"
                "In conclusion, although the USA dominated emissions per person for most of the "
                "period, China's rapid growth narrowed the gap considerably."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "This response presents a clear overview and covers all key data points with "
                "accurate figures. It uses a good range of cohesive devices and a fairly wide "
                "lexical range, though it could integrate the trends across countries more "
                "smoothly and use more sophisticated language."
            ),
            "improvement_tips": [
                "Vary sentence openers to avoid repetitive 'In 1960...', 'China began...' structures.",
                "Use more advanced collocations such as 'a marked acceleration' or 'a steady upward trajectory'.",
                "Add one or two precise comparisons within the same sentence to reduce word count.",
                "Consider using data rounding consistently (e.g., 'roughly 13 tonnes').",
                "Extend the final comparison to reinforce the overall trend more explicitly.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The line graph compares per-capita carbon dioxide emissions in the USA, China "
                "and India over a sixty-year period from 1960 to 2020.\n"
                "What is immediately striking is the gulf between the United States and the other "
                "two nations at the start of the period, with US emissions dwarfing those of China "
                "and India. However, while American emissions eventually subsided, China underwent "
                "a remarkable surge, particularly from 2000 onwards, leaving it far ahead of India, "
                "which remained the most modest emitter throughout.\n"
                "In 1960, US emissions totalled approximately 12.5 tonnes per person, peaking at "
                "just over 15 tonnes in 1980. Thereafter they plateaued, fluctuating marginally "
                "around 15 tonnes until 2010, before declining to 13.1 tonnes by 2020. China, by "
                "contrast, began at a negligible 1.0 tonne in 1960 and climbed steadily to 3.1 "
                "tonnes by the turn of the century, after which a steep upward trajectory took "
                "emissions to 8.5 tonnes per capita in 2020. India, meanwhile, recorded the "
                "lowest figures of the three, rising only modestly from 0.4 tonnes in 1960 to "
                "1.9 tonnes at the end of the period.\n"
                "Overall, the USA retained its position as the largest emitter per person for most "
                "of the period, yet China's exponential growth in the final two decades meant that "
                "the disparity between the two countries narrowed considerably."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "This response fully addresses the task with a clear, well-organised overview that "
                "highlights the most significant trends and comparisons. It demonstrates an "
                "extensive and precise vocabulary range, sophisticated grammatical structures, "
                "and skilful paragraphing with seamless cohesion."
            ),
            "improvement_tips": [
                "Avoid overloading the overview; keep it to the two or three most significant points.",
                "Ensure data points are accurate to the graph and rounded consistently.",
                "Vary passive and active constructions to enhance fluency.",
                "Use precise comparatives and superlatives sparingly for maximum effect.",
                "Check that every sentence adds new information rather than restating the overview.",
            ],
        },
    },
    # ---------------- Q1: Global Temperature ----------------
    1: {
        "5": {
            "band": 5,
            "answer_text": (
                "The line graph shows the change in global average temperature from 1900 to 2020 "
                "compared with the 1951-1980 average.\n"
                "In 1900 the temperature was about -0.30 degrees below the average. It was stable "
                "until 1940, when it was still -0.05 degrees. After 1940 it started to go up. In "
                "1960 it was 0.02 degrees, in 1980 it was 0.27, in 2000 it was 0.43, and in 2020 "
                "it reached 0.98 degrees. That means the temperature was below average in the "
                "beginning of the period, but it was much above average at the end.\n"
                "Overall, the temperature increased a lot during the period. It was negative in "
                "the first years and positive in the last years. The increase became bigger and "
                "bigger after 1980, especially from 2000 to 2020 when it went from 0.43 to "
                "0.98 degrees, which is more than double."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "The answer reports the data accurately and states an overall trend, but the "
                "description is largely a list of figures with limited comparison or grouping. "
                "Vocabulary and structures are basic, and the trend analysis is superficial."
            ),
            "improvement_tips": [
                "State the overview more clearly: temperatures were below average until the 1960s, then rose steadily and steeply.",
                "Group decades instead of listing every data point.",
                "Use trend verbs: 'remained stable', 'climbed', 'accelerated sharply'.",
                "Use phrases of contrast: 'whereas', 'in contrast'.",
                "Add a concluding summary that reflects the magnitude of the change.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "The graph depicts the variation in global average temperature relative to the "
                "1951-1980 baseline between 1900 and 2020.\n"
                "Overall, temperatures remained below the baseline for the first half of the "
                "twentieth century but then rose steadily, with a particularly sharp acceleration "
                "from the 1980s onwards. This resulted in a rise of more than one degree by 2020.\n"
                "Between 1900 and 1940, the temperature anomaly hovered at around -0.3 degrees, "
                "showing little change. A gradual upward movement began in the 1940s, bringing the "
                "figure to 0.02 degrees by 1960. From that point the warming trend became more "
                "pronounced: temperatures reached 0.27 degrees in 1980 and 0.43 degrees in 2000. "
                "The final two decades saw the most dramatic climb, with the anomaly jumping to "
                "0.98 degrees in 2020, more than double the level recorded in 2000.\n"
                "In conclusion, while the early twentieth century was characterised by stability, "
                "the rate of warming increased markedly over time."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The response gives a clear overview and reports the data accurately with an "
                "effective focus on the acceleration of warming. It uses a reasonable range of "
                "vocabulary and cohesive devices, though some phrasing could be more concise "
                "and varied."
            ),
            "improvement_tips": [
                "Avoid repeating 'degrees' too often; vary with 'the anomaly' or 'the deviation'.",
                "Use more sophisticated lexis: 'a marked upswing', 'a sustained climb'.",
                "Round figures consistently to avoid excessive precision.",
                "Strengthen the comparison between early stability and later acceleration within one sentence.",
                "Consider a brief mention of the most significant turning point.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The line graph illustrates the shift in global average temperature compared with "
                "the 1951-1980 mean over the period from 1900 to 2020.\n"
                "At first glance, the twentieth century divides neatly into two contrasting phases: "
                "a long period of near-stability, during which temperatures fluctuated just below "
                "the baseline, followed by a sustained and increasingly rapid upward surge that "
                "ultimately pushed the anomaly to nearly one degree above the historical average.\n"
                "For the first four decades, the temperature deviation remained remarkably flat, "
                "hovering between approximately -0.3 and -0.05 degrees. A modest rise then set in, "
                "bringing the anomaly to roughly 0.02 degrees by 1960. From the 1970s the warming "
                "accelerated, with the figure climbing to 0.27 degrees in 1980 and 0.43 degrees in "
                "2000. The most striking development occurred in the final twenty years, when the "
                "anomaly more than doubled to reach 0.98 degrees in 2020.\n"
                "In essence, the early decades of stability give way to an unmistakable and "
                "accelerating warming trend, with the steepest rise concentrated in the most "
                "recent period."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "This is a fully developed response with a sophisticated overview, precise data "
                "reporting, and an impressive range of lexis and complex structures. The paragraphing "
                "is logical and cohesion is seamless, with no redundant repetition."
            ),
            "improvement_tips": [
                "Maintain consistent rounding of all data points.",
                "Ensure the overview captures both magnitude and rate of change.",
                "Use idiomatic academic phrasing sparingly and accurately.",
                "Keep the final sentence concise; avoid restating all figures.",
                "Check subject-verb agreement in complex clauses.",
            ],
        },
    },
    # ---------------- Q2: Internet Users ----------------
    2: {
        "5": {
            "band": 5,
            "answer_text": (
                "The line graph shows the number of internet users by region from 2000 to 2020.\n"
                "In 2000, the Americas had the most users with 120 million. Europe had 90 million "
                "and Asia had 80 million. Africa had only 3 million. In 2005 Asia went up to 320 "
                "million, Europe to 290, the Americas to 240 and Africa to 25. In 2010 Asia was "
                "830 million, Europe was 470, the Americas were 420 and Africa was 110. In 2020 "
                "Asia had 2500 million, Europe had 730, the Americas had 620 and Africa had 570 "
                "million.\n"
                "Overall, all regions had more users in 2020 than in 2000. Asia grew the fastest "
                "and became the biggest region. Africa also grew a lot, from only 3 million to "
                "570 million, but it was still the smallest at the end of the period."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "All regions are described with accurate figures and the overview identifies the "
                "main pattern, but the description is a series of data lists rather than a "
                "structured comparison. The grammar is inconsistent in places."
            ),
            "improvement_tips": [
                "Use 'million' consistently and write numbers correctly (e.g., '2.5 billion').",
                "Add a clear overview at the start highlighting Asia's dominance and Africa's rapid catch-up.",
                "Group the regions into 'high, middle and low' rather than listing each year.",
                "Correct tense errors: 'Asia always grow' should be 'Asia always grew'.",
                "Use comparatives: 'substantially more than', 'roughly equal to'.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "The line graph traces the growth in the number of internet users in Asia, Europe, "
                "the Americas and Africa between 2000 and 2020.\n"
                "Overall, internet usage increased across all four regions, but Asia recorded by far "
                "the most dramatic growth, rising from a relatively modest base to dominate global "
                "users by 2020. Africa, although starting from a tiny figure, also expanded rapidly, "
                "whereas Europe and the Americas grew more steadily.\n"
                "In 2000, the Americas led with 120 million users, slightly ahead of Europe (90 "
                "million) and Asia (80 million), while Africa had a negligible 3 million. By 2010, "
                "Asia had overtaken the other regions with 830 million users, well above the Americas "
                "(420 million) and Europe (470 million). Growth continued, and by 2020 Asia's user "
                "base had reached 2.5 billion, dwarfing Europe's 730 million, the Americas' 620 "
                "million, and Africa's 570 million.\n"
                "In summary, while all regions saw substantial increases, the pace and scale of "
                "Asia's expansion was exceptional."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "This response is well organised with a clear overview and effective comparisons "
                "between regions. It uses a good range of vocabulary and cohesive devices, though "
                "a few expressions could be more precise and the mid-period could be handled "
                "more succinctly."
            ),
            "improvement_tips": [
                "Reduce the number of mid-decade data points to focus on the most significant changes.",
                "Use 'approximately' and 'roughly' to round large figures.",
                "Vary the comparative structures: 'outstripped', 'lagged behind'.",
                "Add a sentence explicitly linking scale to growth rate.",
                "Refine the overview to mention both absolute size and rate of change.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The graph charts the expansion of internet users across Asia, Europe, the Americas "
                "and Africa over the two decades from 2000 to 2020.\n"
                "The most salient feature is the overwhelming ascendancy of Asia, which surged from "
                "a modest starting point to account for the overwhelming majority of users by the "
                "end of the period. At the opposite end of the spectrum, Africa, though beginning "
                "from a negligible base, posted the fastest relative growth, while Europe and the "
                "Americas showed far more subdued trajectories.\n"
                "In 2000 the Americas and Europe dominated, with 120 and 90 million users "
                "respectively, marginally ahead of Asia's 80 million, whereas Africa recorded a "
                "bare 3 million. Over the following decade Asia's rise was meteoric, reaching 830 "
                "million by 2010, comfortably surpassing both Europe (470 million) and the Americas "
                "(420 million). This momentum continued unabated, and by 2020 Asia's 2.5 billion "
                "users dwarfed every other region, exceeding Europe (730 million), the Americas "
                "(620 million) and Africa (570 million) combined by a substantial margin.\n"
                "In essence, the period witnessed a fundamental redistribution of internet users, "
                "with the centre of gravity shifting decisively from the West to Asia."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "This response excels in all criteria: the overview is insightful, data is "
                "selectively reported with precise comparisons, and the language is highly "
                "sophisticated and accurate. Cohesion is seamless and the register is "
                "consistently academic."
            ),
            "improvement_tips": [
                "Keep 'meteoric', 'unabated' etc. accurate to the data.",
                "Balance longer sentences with shorter ones for rhythm.",
                "Ensure every comparative statement is supported by figures.",
                "Do not overstate relative growth; state figures precisely.",
                "Maintain the same tense throughout the description.",
            ],
        },
    },
    # ---------------- Q3: Coffee and Tea ----------------
    3: {
        "5": {
            "band": 5,
            "answer_text": (
                "The graph shows coffee and tea consumption in the UK from 1980 to 2015.\n"
                "Tea consumption was 2.8 kg per person in 1980. It went down slowly all the time. "
                "In 1985 it was 2.5, in 1995 it was 2.0, and in 2015 it was 1.4 kg. Coffee was "
                "2.0 kg in 1980 and it went up. In 1990 it was 2.8, in 1995 it was 3.2, and in "
                "2015 it was 3.8 kg. Coffee overtook tea around 1995. In 1980 tea was more "
                "popular than coffee, but at the end coffee was more popular than tea.\n"
                "Overall, coffee consumption increased while tea decreased during the whole "
                "period. The two lines crossed in the middle of the period, and after that "
                "coffee was always higher than tea."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "The answer identifies the key crossover point and overall trends, but the "
                "reporting is repetitive and data-heavy with limited analysis. Language is basic "
                "and comparisons are underdeveloped."
            ),
            "improvement_tips": [
                "Add an overview sentence at the start summarising the opposite trends.",
                "Group the change into clear phases (e.g., gradual decline vs steady rise).",
                "Use more precise trend language: 'declined steadily', 'rose consistently'.",
                "Use comparative structures: 'whereas tea fell by half, coffee nearly doubled'.",
                "Avoid repeating 'it went up/down' throughout.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "The line graph illustrates the per-capita consumption of coffee and tea in the "
                "United Kingdom over a 35-year period from 1980 to 2015.\n"
                "Overall, the two beverages followed opposite trajectories: tea consumption declined "
                "steadily throughout the period, whereas coffee consumption rose, with coffee "
                "overtaking tea around the mid-1990s.\n"
                "In 1980, tea was the more popular drink, with consumption of 2.8 kg per person, "
                "compared with 2.0 kg for coffee. Tea then slipped gradually, dropping to around "
                "2.0 kg by 1995, while coffee climbed to 3.2 kg in the same year, suggesting that "
                "the crossover occurred during this decade. Thereafter the divergence widened. Tea "
                "fell further to 1.4 kg by 2015, whereas coffee continued to rise, reaching "
                "approximately 3.8 kg at the end of the period.\n"
                "In conclusion, the two trends moved in opposite directions, leaving coffee as the "
                "clear favourite among UK consumers by 2015."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The response is well structured, with a clear overview, accurate data and an "
                "effective focus on the crossover point. Vocabulary and cohesion are good, though "
                "the language could be slightly more sophisticated and some sentences are "
                "formulaic."
            ),
            "improvement_tips": [
                "Use a wider range of linking expressions and sentence patterns.",
                "Introduce more advanced lexis: 'an inversion of preferences', 'a sustained decline'.",
                "Make the crossover estimate more precise using the available data.",
                "Vary the way figures are introduced to avoid repetitive phrasing.",
                "Add a brief note on the overall scale of change for both drinks.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The graph compares trends in per-capita coffee and tea consumption in the UK "
                "between 1980 and 2015.\n"
                "What stands out is the complete inversion of the nation's beverage preferences: "
                "while tea consumption contracted almost continuously, coffee consumption expanded "
                "just as persistently, the two lines crossing at roughly the midpoint of the period "
                "and diverging ever more widely thereafter.\n"
                "In 1980 tea was clearly the dominant drink, with each person consuming 2.8 kg "
                "annually, some 40 per cent more than the 2.0 kg of coffee. Over the following "
                "fifteen years the gap closed steadily; tea eased down to approximately 2.0 kg by "
                "1995, while coffee climbed to around 3.2 kg, indicating that the crossover took "
                "place in the mid-1990s. From that point the divergence accelerated: tea continued "
                "its downward slide to 1.4 kg in 2015, a halving of its initial level, whereas "
                "coffee rose to roughly 3.8 kg, nearly double its starting figure.\n"
                "In essence, the period saw a wholesale shift in British drinking habits, with "
                "coffee overtaking tea and the gap between them widening to almost threefold by "
                "the end."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "A model response: the overview is precise and insightful, data is selectively and "
                "accurately reported with meaningful percentage comparisons, and the language "
                "displays a wide, precise and natural range of vocabulary and structures."
            ),
            "improvement_tips": [
                "Verify percentage claims against the raw figures.",
                "Keep the overview within two sentences for clarity.",
                "Use the active voice sparingly to vary the tone.",
                "Ensure the conclusion reflects data, not opinion.",
                "Maintain parallel structure in comparative sentences.",
            ],
        },
    },
    # ---------------- Q4: Household Expenditure ----------------
    4: {
        "5": {
            "band": 5,
            "answer_text": (
                "The bar chart shows the average monthly household expenditure by category in "
                "2010 and 2020.\n"
                "In both years housing was the biggest expense. In 2010 it was 800 USD and in "
                "2020 it was 1100 USD. Food was 420 in 2010 and 520 in 2020. Transport went from "
                "250 to 300 USD. Education was 180 in 2010 and went up to 350 in 2020, so it "
                "more than doubled. Health was 120 in 2010 and went up to 260 in 2020, so it "
                "also more than doubled.\n"
                "Overall, all categories increased from 2010 to 2020. Education and health grew "
                "the most, and housing stayed the biggest category in both years. Food and "
                "transport also increased but not as much as education and health."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "All categories are covered with accurate figures and a reasonable overview is "
                "given, but the response reads as a list and comparisons are shallow. There are "
                "minor grammar errors and limited vocabulary."
            ),
            "improvement_tips": [
                "Give the overview more prominence at the start.",
                "Group categories by size or growth pattern instead of listing each one.",
                "Use comparison language: 'nearly double', 'the steepest rise'.",
                "Fix agreement errors: 'it more than double' should be 'it more than doubled'.",
                "Add percentages of change for the most significant movements.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "The bar chart compares average monthly household spending across five categories "
                "in one country in 2010 and 2020.\n"
                "Overall, expenditure rose in every category over the decade, with housing remaining "
                "the largest item throughout. The most notable increases were in education and "
                "health, both of which roughly doubled.\n"
                "Housing dominated spending in both years, climbing from 800 USD in 2010 to 1,100 "
                "USD in 2020. Food, the second largest category, rose from 420 to 520 USD, while "
                "transport increased more modestly from 250 to 300 USD. Education, however, "
                "experienced the most dramatic growth, more than doubling from 180 to 350 USD, "
                "and health spending followed a similar pattern, growing from 120 to 260 USD.\n"
                "In conclusion, although all areas of household expenditure grew, the strongest "
                "increases were seen in education and healthcare, while housing remained the "
                "dominant cost."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The response presents a clear overview and groups data effectively, using accurate "
                "figures and sensible comparisons. It demonstrates good control of grammar and "
                "cohesion, though the vocabulary is competent rather than sophisticated."
            ),
            "improvement_tips": [
                "Introduce more precise academic lexis: 'accounted for', 'a twofold increase'.",
                "Vary the way figures are presented (absolute values and changes).",
                "Use at least one complex comparison across categories.",
                "Round figures where appropriate for a more natural style.",
                "Strengthen the concluding sentence with a total overview.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The chart compares average monthly household expenditure in one country across "
                "five categories, contrasting 2010 with 2020.\n"
                "A striking feature is the across-the-board rise in spending, yet the categories "
                "grew at markedly different rates. Housing, already the heaviest burden, expanded "
                "further, while education and health recorded the most pronounced proportional "
                "increases, both approximately doubling.\n"
                "Housing remained the single largest outlay, rising from 800 to 1,100 USD per "
                "month, a substantial 37 per cent increase. Food, the next largest category, "
                "grew more moderately from 420 to 520 USD, and transport saw the smallest rise "
                "of all, edging up from 250 to 300 USD. The most dramatic movement, however, "
                "occurred in education, which surged from 180 to 350 USD, and in health, which "
                "climbed from 120 to 260 USD, both more than doubling over the decade.\n"
                "In summary, while every component of household spending increased, the decisive "
                "trend was the growing share absorbed by housing, education and health, at the "
                "expense of more traditional categories."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "This is a comprehensive and well-balanced response with a strong overview, "
                "precise figures, and insightful comparison of growth rates. It demonstrates "
                "exceptional range and accuracy in both vocabulary and grammar, with seamless "
                "cohesion."
            ),
            "improvement_tips": [
                "Ensure percentage calculations are correct and consistent.",
                "Balance detailed figures with interpretive statements.",
                "Avoid repetition of 'both more than doubling' if used twice.",
                "Use a range of complex structures: inversion, cleft sentences, participle clauses.",
                "Keep the conclusion analytical rather than descriptive.",
            ],
        },
    },
    # ---------------- Q5: University Students by Subject ----------------
    5: {
        "5": {
            "band": 5,
            "answer_text": (
                "The bar chart shows the percentage of university students studying different "
                "subjects in 2010 and 2020.\n"
                "In 2010, Business was the most popular subject with 25%. Engineering was 22%, "
                "Arts 20%, Law 18% and Medicine 15%. In 2020, Engineering was the most popular "
                "with 30%. Business was 28%, Medicine 18%, Arts 12% and Law 12%. Engineering "
                "went up from 22% to 30%, and Medicine went up from 15% to 18%. Business also "
                "went up a little, from 25% to 28%. But Arts went down from 20% to 12%, and Law "
                "went down from 18% to 12%.\n"
                "Overall, Engineering became the most popular subject in 2020, and Business was "
                "second. Arts and Law became much less popular, while Medicine stayed the same "
                "or went up a little."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "The data is reported accurately and a basic overview is provided, but the "
                "response reads as a series of figures with limited analysis. The overview is "
                "repeated in the final sentence and vocabulary is limited."
            ),
            "improvement_tips": [
                "Present the overview immediately after the introduction and only once.",
                "Group subjects by direction of change (rising vs falling).",
                "Use comparison phrases: 'overtook', 'accounted for'.",
                "Avoid listing every subject and figure in sequence.",
                "Use precise academic vocabulary: 'saw a decline', 'registered growth'.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "The bar chart compares the proportion of university students enrolled in five "
                "subjects in 2010 and 2020.\n"
                "Overall, the decade brought a notable reshuffle in subject popularity. Engineering "
                "overtook Business to become the most popular choice, while enrolments in Arts and "
                "Law fell considerably.\n"
                "In 2010, Business and Engineering were the two leading subjects, accounting for "
                "25% and 22% of students respectively, followed by Arts at 20%, Law at 18% and "
                "Medicine at 15%. By 2020, Engineering had risen to 30%, making it the most "
                "popular field, while Business also increased modestly to 28%. Medicine grew "
                "steadily from 15% to 18%. In contrast, Arts and Law both contracted significantly, "
                "falling to 12% each.\n"
                "In conclusion, the period saw a clear shift towards engineering and business "
                "subjects at the expense of arts and law."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The response has a clear structure with a strong overview and effective grouping "
                "of rising and falling subjects. It uses accurate figures and a good range of "
                "cohesive devices, though the vocabulary is competent rather than sophisticated."
            ),
            "improvement_tips": [
                "Use more advanced lexis: 'witnessed a surge', 'a marked contraction'.",
                "Add relative comparisons (percentages of change) for key subjects.",
                "Vary sentence structures to avoid formulaic patterns.",
                "Round figures naturally where appropriate.",
                "Ensure the conclusion adds value rather than repeating the overview.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The chart illustrates the distribution of university students across five academic "
                "fields in 2010 and 2020, measured as a percentage of total enrolment.\n"
                "The most significant development over the decade was a reordering of subject "
                "popularity, with Engineering displacing Business at the top, and a corresponding "
                "retreat from the arts and law. These shifts were substantial rather than marginal, "
                "indicating a clear move towards technical and commercial disciplines.\n"
                "In 2010, Business led the field, commanding 25% of students, narrowly ahead of "
                "Engineering on 22%, with Arts (20%), Law (18%) and Medicine (15%) trailing behind. "
                "Ten years later, the picture had altered considerably. Engineering surged to 30%, "
                "and Business, though growing to 28%, slipped into second place. Medicine likewise "
                "expanded its share from 15% to 18%. By contrast, the two humanities-based subjects "
                "suffered sharp declines, with Arts falling from 20% to 12% and Law contracting "
                "from 18% to 12%.\n"
                "In essence, the data reveals a decisive pivot towards engineering and medicine, "
                "together with business, at the direct expense of arts and law."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "A polished response with an insightful overview, precise data reporting, and "
                "effective grouping. It demonstrates a wide, accurate and natural range of "
                "vocabulary and structures, with seamless cohesion and a persuasive analytical "
                "conclusion."
            ),
            "improvement_tips": [
                "Keep percentages internally consistent across the response.",
                "Balance interpretive and descriptive sentences.",
                "Use varied comparative devices without overloading one structure.",
                "Maintain a formal, impersonal register throughout.",
                "Ensure the final sentence synthesises rather than summarises.",
            ],
        },
    },
    # ---------------- Q6: Weekly Time Spent on Activities ----------------
    6: {
        "5": {
            "band": 5,
            "answer_text": (
                "The bar chart shows the hours per week spent on different activities by three "
                "age groups.\n"
                "The 18-35 group spends 42 hours working, 49 hours sleeping, 20 hours on leisure "
                "and 5 hours on exercise. The 36-55 group works 40 hours, sleeps 48 hours, "
                "spends 15 hours on leisure and 4 hours on exercise. The 55+ group works only 10 "
                "hours, sleeps 51 hours, spends 38 hours on leisure and 7 hours on exercise.\n"
                "Overall, all groups spend the most time sleeping. Younger people work much more "
                "than older people, and older people have much more leisure time. The 55+ group "
                "does the most exercise, but exercise is the smallest activity for all groups."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "The response lists the data by group without strong comparison across activities. "
                "The overview identifies a couple of general trends but lacks depth. Language is "
                "simple and repetitive."
            ),
            "improvement_tips": [
                "Create a clearer overview contrasting working-age groups with the retired group.",
                "Compare across age groups within the same activity, not just group by group.",
                "Use contrastive linkers: 'whereas', 'by comparison'.",
                "Use academic verbs: 'spend', 'devote', 'allocate time to'.",
                "Round the figures and avoid listing all twelve data points.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "The chart shows how three age groups allocate their time across four activities "
                "in an average week.\n"
                "Overall, sleep was the most time-consuming activity for all groups, while exercise "
                "took up the least. The most striking contrast was between the two working-age "
                "groups, which devoted most of their week to employment, and the 55-plus group, "
                "which enjoyed far more leisure time.\n"
                "Those aged 18-35 worked 42 hours and slept 49 hours, while the 36-55 group worked "
                "a slightly shorter week of 40 hours and slept 48 hours. Leisure was the third "
                "largest commitment for both, at 20 and 15 hours respectively, and exercise "
                "accounted for only 5 and 4 hours. The pattern for the 55-plus age group was "
                "markedly different: they worked just 10 hours but slept the most (51 hours) and "
                "spent a substantial 38 hours on leisure, with 7 hours devoted to exercise.\n"
                "In conclusion, age had a decisive influence on time allocation, with retirement "
                "shifting the balance sharply away from work towards leisure."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The response organises the data effectively, comparing within and across groups, "
                "and provides a clear overview. Cohesion is good and vocabulary is adequate, "
                "though a little more variety and precision would strengthen it."
            ),
            "improvement_tips": [
                "Use more varied lexis: 'allotted to', 'was devoted to', 'consumed'.",
                "Group the working-age groups together more explicitly for comparison.",
                "Add a comparative percentage for the leisure difference.",
                "Vary sentence openings to avoid repetitive 'group' phrasing.",
                "Round figures consistently.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The chart compares the weekly allocation of time across four activities for three "
                "age cohorts.\n"
                "Sleep emerges as the dominant activity in every cohort, whereas exercise occupies "
                "the smallest share. The most revealing contrast, however, lies between the two "
                "working-age cohorts, whose weeks were dominated by employment, and the over-55s, "
                "for whom leisure assumed far greater importance following retirement.\n"
                "Adults aged 18-35 and 36-55 devoted comparable amounts of time to work, at 42 and "
                "40 hours respectively, and similar hours to sleep, at 49 and 48. Their leisure "
                "time, however, differed, at 20 and 15 hours, and exercise was minimal in both, "
                "accounting for no more than 5 and 4 hours. The pattern for the oldest cohort was "
                "fundamentally different: with work occupying just 10 hours of the week, they "
                "recorded the highest sleeping figure (51 hours) and devoted a substantial 38 hours "
                "to leisure, alongside 7 hours of exercise, more than either working-age group.\n"
                "In essence, the data illustrates how the transition from employment to retirement "
                "fundamentally reshapes the distribution of weekly time, channelling hours from "
                "work into leisure and, to a lesser extent, physical activity."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "This response demonstrates exceptional control: a precise overview, sophisticated "
                "and varied vocabulary, complex grammatical structures used accurately, and "
                "seamless paragraphing. All key comparisons are drawn effectively."
            ),
            "improvement_tips": [
                "Ensure all figures are reported accurately and consistently.",
                "Avoid over-long sentences; balance with shorter ones.",
                "Keep the 'to a lesser extent' qualifier accurate to the data.",
                "Maintain the impersonal academic register.",
                "Verify that the conclusion synthesises, not merely restates.",
            ],
        },
    },
    # ---------------- Q7: Car Production ----------------
    7: {
        "5": {
            "band": 5,
            "answer_text": (
                "The bar chart shows the number of cars produced in four countries in 2000 and "
                "2020.\n"
                "In 2000, Japan produced the most cars with 8.4 million. The USA made 5.7 "
                "million, Germany made 5.5 million and China made only 2.0 million. In 2020, "
                "China made the most cars with 25.3 million. Japan made 6.8 million, Germany "
                "made 3.7 million and the USA made 2.3 million.\n"
                "China grew very fast, from 2.0 million in 2000 to 25.3 million in 2020. Japan "
                "went down from 8.4 to 6.8 million, and Germany went down from 5.5 to 3.7 "
                "million. The USA also went down from 5.7 to 2.3 million.\n"
                "Overall, China became the biggest car producer in 2020. The other three "
                "countries all produced fewer cars in 2020 than in 2000."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "The main data and overall trend are present, but the response contains a "
                "confusing self-correction ('from 8.4 to 6.8? No...') that would not appear in a "
                "polished answer, and the analysis is shallow. Grammar and organisation need work."
            ),
            "improvement_tips": [
                "Remove any hesitations or self-corrections; plan before writing.",
                "State Japan's decline clearly the first time.",
                "Add percentage changes to highlight China's extraordinary growth.",
                "Use comparative language: 'a twelvefold increase'.",
                "Structure the answer with clear paragraphs for overview and details.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "The bar chart compares car production in Japan, Germany, China and the United "
                "States in 2000 and 2020.\n"
                "The most striking feature is the complete reversal of the industry hierarchy. "
                "China, which was the smallest producer in 2000, had become by far the largest by "
                "2020, while the USA and Germany both saw their output fall significantly.\n"
                "In 2000, Japan led the field with 8.4 million cars, followed by the USA with 5.7 "
                "million and Germany with 5.5 million, whereas China produced just 2.0 million. "
                "Two decades later, the positions had been transformed. China's output had soared "
                "to 25.3 million, more than twelve times its earlier figure. Japan, meanwhile, "
                "declined modestly to 6.8 million, while Germany fell to 3.7 million and the USA "
                "dropped sharply to 2.3 million.\n"
                "In conclusion, the period saw China rise from last to first among the four "
                "countries, at the expense of the established producers."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The response has a strong overview, accurate data and effective comparisons. "
                "Cohesion and paragraphing are good, and the language is clear, though a wider "
                "range of sophisticated vocabulary would lift it further."
            ),
            "improvement_tips": [
                "Use more precise lexis: 'outstripped', 'a dramatic upsurge', 'declining output'.",
                "Add one or two additional relative comparisons (e.g., Japan's lead over Germany).",
                "Vary the structures used to present figures.",
                "Round figures consistently for a natural academic style.",
                "Ensure the conclusion captures both absolute and relative change.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The chart contrasts motor vehicle production in Japan, Germany, China and the "
                "United States in 2000 and 2020.\n"
                "What emerges most clearly is a seismic shift in the global geography of car "
                "manufacturing. China, the laggard of 2000, catapulted itself into a position of "
                "overwhelming dominance, while the traditional powerhouses, in particular the "
                "United States, experienced pronounced contraction.\n"
                "In 2000 Japan was the undisputed leader, producing 8.4 million vehicles, a "
                "comfortable margin over the USA's 5.7 million and Germany's 5.5 million, with "
                "China bringing up the rear at just 2.0 million. By 2020 the hierarchy had been "
                "upended. Chinese output had surged more than twelvefold to 25.3 million, dwarfing "
                "the combined production of the other three countries. Japan, while retaining "
                "second place, slipped to 6.8 million, and Germany fell to 3.7 million. Most "
                "dramatically, US output collapsed to 2.3 million, less than half its 2000 level "
                "and only a fraction of China's figure.\n"
                "In essence, the two decades witnessed a wholesale reordering of the industry, "
                "with the centre of production shifting decisively to China."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "An excellent response: the overview is incisive, the data is reported precisely "
                "with powerful comparisons, and the language is sophisticated and accurate "
                "throughout. Structure and cohesion are exemplary."
            ),
            "improvement_tips": [
                "Verify comparative claims such as 'more than twelvefold' against the data.",
                "Use strong lexis sparingly to retain impact.",
                "Ensure every clause is grammatically complete.",
                "Balance dramatic language with factual precision.",
                "Keep the conclusion focused on the data's central message.",
            ],
        },
    },
    # ---------------- Q8: Energy Production ----------------
    8: {
        "5": {
            "band": 5,
            "answer_text": (
                "The pie chart shows the share of different energy sources in total energy "
                "production in 2020.\n"
                "Coal is the biggest source with 35%. Natural gas is the second biggest with 28%. "
                "Renewables are 20%, nuclear is 12% and oil is only 5%. Coal and natural gas "
                "together are 63%, so they are more than half of all production. Renewables are "
                "20%, which is more than nuclear at 12%. Oil is the smallest source with only "
                "5%.\n"
                "Overall, fossil fuels such as coal, natural gas and oil are the most important, "
                "because they make up 68% of the total. Clean energy sources are still small, "
                "but renewables are already bigger than nuclear."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "The proportions are reported accurately with a reasonable overview, but the "
                "response is quite brief, makes limited comparisons, and lacks the depth expected "
                "of a Task 1 answer at higher bands."
            ),
            "improvement_tips": [
                "Group the sources into fossil fuels and non-fossil fuels to structure the answer.",
                "Add cumulative comparisons (e.g., 'coal and gas account for almost two-thirds').",
                "Use more formal vocabulary: 'account for', 'constitute'.",
                "Extend the answer to describe the significance of the renewables share.",
                "Use at least one complex sentence combining two data points.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "The pie chart illustrates the proportion of total energy production accounted for "
                "by five different sources in 2020.\n"
                "Overall, fossil fuels dominated the energy mix, with coal and natural gas alone "
                "together accounting for nearly two-thirds of total production. By contrast, "
                "renewables and nuclear, the two cleaner sources, made up less than a third.\n"
                "Coal was the largest contributor, at 35%, followed closely by natural gas at 28%. "
                "Combined, these two sources represented 63% of production. Renewables supplied a "
                "further 20%, while nuclear contributed 12%. Oil was the smallest source, "
                "providing only 5%, which meant that the remaining non-fossil sources were "
                "responsible for the largest part of the rest.\n"
                "In conclusion, energy production in 2020 remained heavily reliant on fossil fuels, "
                "although renewables already outranked nuclear as the leading clean source."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The response presents a clear overview and groups the data sensibly, with accurate "
                "figures and a logical structure. Vocabulary and cohesion are good, though a wider "
                "range of expression would improve it further."
            ),
            "improvement_tips": [
                "Use more varied lexis: 'constituted', 'made up', 'represented'.",
                "Avoid the slightly awkward final clause about 'the rest'.",
                "Round percentages or express cumulative totals more clearly.",
                "Add a sentence comparing renewables and nuclear explicitly.",
                "Vary sentence structures to avoid listing sources one by one.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The pie chart depicts the composition of energy production by source in 2020, "
                "expressed as a percentage of the total.\n"
                "The most salient feature is the overwhelming preponderance of fossil fuels, which "
                "between them supplied close to two-thirds of all energy. Within this grouping, "
                "coal stood out as the single largest source, while at the opposite end of the "
                "spectrum oil made only a negligible contribution. Among the cleaner sources, "
                "renewables already occupied a clearly more prominent position than nuclear.\n"
                "Coal led the field at 35%, with natural gas a substantial second at 28%; together "
                "these two sources accounted for 63% of production. Renewables furnished a further "
                "20%, comfortably exceeding the 12% provided by nuclear power. Oil, representing "
                "merely 5%, trailed all other sources by a wide margin.\n"
                "In sum, the energy landscape in 2020 was still dominated by carbon-based fuels, "
                "although the comparatively strong showing of renewables signalled a gradual, if "
                "still limited, transition towards cleaner generation."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "This response is fully developed and well organised, with an insightful overview "
                "and precise, varied reporting of proportions. The vocabulary is wide and "
                "accurately used, and the grammar is complex yet correct throughout."
            ),
            "improvement_tips": [
                "Check that all percentage claims sum consistently to 100%.",
                "Keep interpretive statements grounded in the data.",
                "Vary 'account for' with 'comprise', 'constitute', 'furnish'.",
                "Ensure the conclusion does not introduce new information.",
                "Maintain parallel structure across comparative sentences.",
            ],
        },
    },
    # ---------------- Q9: Water Usage by Sector ----------------
    9: {
        "5": {
            "band": 5,
            "answer_text": (
                "The pie charts show the percentage of water used for different purposes in 2010 "
                "and 2020.\n"
                "In 2010, agriculture used 70% of water, industry used 20% and domestic used "
                "10%. In 2020, agriculture used 55%, industry used 30% and domestic used 15%. "
                "Agriculture went down from 70% to 55%, so it lost 15 percentage points. "
                "Industry went up from 20% to 30%, so it gained 10 percentage points. Domestic "
                "also went up from 10% to 15%, so it gained 5 percentage points.\n"
                "Overall, agriculture is still the biggest user of water in 2020, but its share "
                "went down during the period. Industry and domestic use both went up, and "
                "together they now use almost half of all water."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "The response covers both charts with accurate figures and a basic overview, but "
                "the description is formulaic and the comparisons are shallow. Language is simple "
                "and repetitive."
            ),
            "improvement_tips": [
                "State the overview with more precision (e.g., 'agriculture remained dominant but lost share').",
                "Describe the magnitude of change: 'a 15 percentage point decline'.",
                "Use academic verbs: 'accounted for', 'registered a rise'.",
                "Compare the two years within each sector rather than year by year.",
                "Use 'whilst' or 'whereas' for contrast.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "The two pie charts compare the allocation of water across agriculture, industry "
                "and domestic use in 2010 and 2020.\n"
                "Overall, agriculture remained by far the largest consumer of water in both years, "
                "although its share diminished considerably. Industry and domestic use both "
                "expanded over the decade.\n"
                "In 2010, agriculture accounted for a dominant 70% of all water usage, leaving "
                "20% for industry and a mere 10% for domestic purposes. Ten years later, the "
                "pattern had shifted noticeably. Agriculture's share had fallen to 55%, while "
                "industry had risen to 30% and domestic consumption to 15%. This represented a "
                "15 percentage point decline for agriculture, matched by a 10 point gain for "
                "industry and a 5 point gain for domestic use.\n"
                "In conclusion, although farming continued to dominate water consumption, the "
                "balance moved steadily towards industrial and household use."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The response is well organised with a clear overview and precise reporting of "
                "changes in percentage points. Vocabulary and cohesion are good, though the "
                "language could be more varied and sophisticated."
            ),
            "improvement_tips": [
                "Use a wider lexical range: 'consumed', 'allocated to', 'absorbed'.",
                "Add a sentence interpreting the overall significance of the shift.",
                "Vary the structure of comparative sentences.",
                "Round the data naturally and consistently.",
                "Ensure the conclusion synthesises rather than repeats the overview.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The paired pie charts depict how water resources were apportioned between "
                "agriculture, industry and domestic use in 2010 and 2020.\n"
                "The overriding feature is the persistent, if reduced, supremacy of agriculture, "
                "which continued to absorb more than half of all water even as its share eroded "
                "substantially. The ten-year period also saw a clear redistribution of water "
                "towards industrial and, to a lesser extent, domestic consumption.\n"
                "In 2010, agriculture commanded an overwhelming 70% of total water use, dwarfing "
                "the 20% directed to industry and the residual 10% used domestically. By 2020 this "
                "hierarchy, though intact, had been significantly recalibrated: agriculture "
                "accounted for 55% of the total, a decline of 15 percentage points, while "
                "industry's share climbed by 10 points to 30% and domestic use advanced by 5 "
                "points to 15%.\n"
                "In essence, the decade witnessed a moderate yet steady rebalancing of water "
                "demands, with agriculture conceding ground to the growing requirements of "
                "industry and households."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "This is a highly effective response with a sharp overview, accurate percentage-point "
                "analysis, and sophisticated, precise language. The structures are complex and "
                "varied, and the response is flawlessly coherent."
            ),
            "improvement_tips": [
                "Verify all percentage-point calculations.",
                "Avoid over-complex sentences that risk readability.",
                "Use formal lexis consistently throughout.",
                "Ensure the overview captures both dominance and decline.",
                "Keep the conclusion analytical and concise.",
            ],
        },
    },
    # ---------------- Q10: Student Enrolment by Faculty ----------------
    10: {
        "5": {
            "band": 5,
            "answer_text": (
                "The pie charts show the proportion of students in different faculties at a "
                "university in 2015 and 2025.\n"
                "In 2015, Business had the most students with 30%. Science and Humanities both "
                "had 25%. Engineering had 20%. In 2025, Science had the most with 35%. Business "
                "was 28%, Engineering was 22% and Humanities was 15%. Science went up a lot, "
                "from 25% to 35%. Humanities went down a lot, from 25% to 15%. Business went "
                "down a little, from 30% to 28%, and Engineering went up a little, from 20% to "
                "22%.\n"
                "Overall, Science became the most popular faculty in 2025. Humanities became "
                "much less popular, and Business lost its first place. Engineering stayed the "
                "same or grew a little."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "The data is complete and accurate with a basic overview, but the response is a "
                "simple list of figures. Comparisons are made individually rather than grouped, "
                "and the language is basic."
            ),
            "improvement_tips": [
                "Group faculties into risers and fallers in the overview.",
                "Use 'overtook' to describe Science displacing Business.",
                "Use percentage-point language for changes.",
                "Vary vocabulary: 'enrolled in', 'registered', 'accounted for'.",
                "Structure the answer into clear overview and detail paragraphs.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "The two pie charts show how the student population of a university was distributed "
                "across four faculties in 2015 and 2025.\n"
                "Overall, the decade brought a significant shift towards the sciences. Science "
                "overtook Business to become the largest faculty, while Humanities experienced the "
                "sharpest decline of any field.\n"
                "In 2015, Business led with 30% of students, closely followed by Science and "
                "Humanities, each with 25%, and Engineering with 20%. By 2025, Science had "
                "surged to 35%, displacing Business, which eased to 28%. Engineering registered a "
                "modest increase from 20% to 22%, while Humanities fell sharply from 25% to just "
                "15%.\n"
                "In conclusion, the period was characterised by a clear move away from the "
                "humanities towards science and, to a smaller extent, engineering."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The response has a strong overview, accurate data and a logical structure. It "
                "uses good cohesive devices and clear comparisons, though a broader vocabulary "
                "range would strengthen it."
            ),
            "improvement_tips": [
                "Use more precise academic lexis: 'witnessed a surge', 'a marked decline'.",
                "Add percentage-point changes for the key movements.",
                "Vary the way data is introduced to reduce repetition.",
                "Round figures consistently.",
                "Ensure the final sentence summarises the overall trend precisely.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The paired pie charts illustrate how enrolment was distributed across four "
                "faculties of a university in 2015 and 2025.\n"
                "The period witnessed a pronounced reorientation of student preferences towards "
                "the sciences. Most notably, Science displaced Business at the head of the "
                "institution, while Humanities sustained the heaviest losses, contracting by a "
                "full ten percentage points.\n"
                "In 2015 Business commanded the largest share, at 30%, with Science and "
                "Humanities each accounting for 25% and Engineering trailing at 20%. A decade "
                "later the hierarchy had shifted. Science surged to 35%, a ten-point gain that "
                "elevated it above Business, which nonetheless held its ground reasonably well, "
                "slipping only two points to 28%. Engineering advanced modestly, from 20% to 22%, "
                "whereas Humanities fell dramatically, from 25% to 15%.\n"
                "In essence, the data reveals a decisive pivot towards the sciences and a "
                "concomitant retreat from the humanities, a shift consistent with broader "
                "labour-market trends."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "This is a fluent and accurate response with a sophisticated overview, precise "
                "percentage-point reporting, and a wide range of natural vocabulary and complex "
                "structures. Cohesion is seamless and the register is appropriately academic."
            ),
            "improvement_tips": [
                "Keep interpretive claims (e.g., labour-market trends) clearly distinct from data.",
                "Verify all percentage-point calculations.",
                "Balance longer and shorter sentences for clarity.",
                "Use 'concomitant' and similar advanced lexis accurately.",
                "Ensure the conclusion stays within the scope of the data.",
            ],
        },
    },
    # ---------------- Q11: Underground Railway Systems ----------------
    11: {
        "5": {
            "band": 5,
            "answer_text": (
                "The table gives information about underground railway systems in six cities.\n"
                "London opened the first system in 1863. It is 408 km long and carries 1400 "
                "million passengers. Paris opened in 1900, is 214 km long and carries 1500 "
                "million. Tokyo opened in 1927, is 305 km and carries 3200 million. New York "
                "opened in 1904, is 373 km and carries 1700 million. Moscow opened in 1935, is "
                "397 km and carries 2400 million. Beijing opened in 1971, is 699 km and carries "
                "3800 million.\n"
                "Overall, Beijing is the longest system and carries the most passengers. London "
                "is the oldest system. Paris is the shortest system, but it carries more "
                "passengers than London, New York and some other cities."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "All the data is transcribed accurately and an overview is attempted, but the "
                "answer simply lists every city in turn without comparison or analysis. There is "
                "no grouping or ranking beyond the brief overview."
            ),
            "improvement_tips": [
                "Add a proper overview identifying the most and least developed systems.",
                "Group cities by characteristics (e.g., oldest vs most extensive).",
                "Make comparisons: 'Beijing is almost twice the length of Paris's network'.",
                "Use vocabulary of ranking: 'the most extensive', 'the longest-serving'.",
                "Round large numbers consistently and use 'approximately'.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "The table provides data on the underground railway systems of six cities, "
                "covering the year of opening, total length and annual passenger numbers.\n"
                "Overall, the systems vary considerably in scale. Beijing stands out as both the "
                "most extensive network and the busiest, whereas London holds the distinction of "
                "being the oldest, having opened over a century before Beijing.\n"
                "London opened its underground in 1863 and today operates 408 km of track, "
                "carrying 1,400 million passengers a year. Paris, opened in 1900, is considerably "
                "shorter at 214 km but carries a comparable 1,500 million passengers, suggesting "
                "far heavier usage per kilometre. Tokyo, established in 1927, moves 3,200 million "
                "passengers annually along 305 km of line. New York (1904) and Moscow (1935) "
                "follow, with 373 and 397 km and 1,700 and 2,400 million passengers respectively. "
                "Beijing, opened most recently in 1971, has grown to 699 km and carries more "
                "passengers than any other, at 3,800 million.\n"
                "In conclusion, older European networks generally combined with shorter modern "
                "systems, while Beijing's relatively recent system has become the largest and "
                "busiest."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The response selects key data and adds meaningful comparisons and analysis, "
                "including the insight about usage per kilometre. It is well organised with a "
                "clear overview, though the detail paragraph is long and could be tighter."
            ),
            "improvement_tips": [
                "Shorten the detail section by grouping cities more efficiently.",
                "Add a comparison of usage intensity for two more cities.",
                "Use more advanced lexis: 'the most heavily trafficked', 'comparable capacity'.",
                "Vary sentence openings to avoid repetition of city names.",
                "Ensure every figure is used to support a point.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The table compares the underground railway networks of six global cities with "
                "respect to their year of opening, total track length and annual passenger "
                "volumes.\n"
                "The data reveals striking disparities in the scale and intensity of these systems. "
                "Beijing is clearly pre-eminent, combining the longest network with the highest "
                "passenger throughput, whereas London, the pioneering system, offers a revealing "
                "contrast between its historical primacy and its moderate size. Equally notable "
                "is the variation in intensity: Paris and Tokyo move far more passengers per "
                "kilometre of track than the other systems.\n"
                "London's network, opened in 1863, extends over 408 km and conveys 1,400 million "
                "travellers each year. Paris, though much shorter at 214 km, transports 1,500 "
                "million, a figure implying almost double the usage density of London. Tokyo, "
                "opened in 1927, achieves the highest absolute density, carrying 3,200 million "
                "passengers on 305 km. New York (1904; 373 km; 1,700 million) and Moscow (1935; "
                "397 km; 2,400 million) occupy an intermediate tier. Beijing, the youngest system, "
                "opened in 1971, has since expanded to 699 km and carries a record 3,800 million "
                "passengers annually.\n"
                "In sum, the table illustrates both the growth of metro systems over more than a "
                "century and the markedly different roles they play, from dense urban workhorses "
                "to vast, high-capacity networks."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "An outstanding response that not only reports the data but analyses it, drawing "
                "out the significant relationship between network length and usage intensity. The "
                "language is sophisticated and precise, and the structure is perfectly coherent."
            ),
            "improvement_tips": [
                "Double-check density claims against the figures.",
                "Use parenthetical data sparingly to maintain flow.",
                "Avoid overgeneralising; support every comparison with data.",
                "Maintain consistency in the use of 'million'.",
                "Keep the conclusion focused and data-driven.",
            ],
        },
    },
    # ---------------- Q12: Tourism Statistics ----------------
    12: {
        "5": {
            "band": 5,
            "answer_text": (
                "The table gives information about tourism in five countries.\n"
                "France has the most international visitors with 89 million. Spain has 84 "
                "million, Turkey has 51, Mexico has 41 and Thailand has 39. Spain earns the "
                "most revenue with 92 billion dollars. France earns 66 billion, Thailand earns "
                "63 billion, Turkey earns 34 billion and Mexico earns 24 billion. Turkey has "
                "the longest average stay with 10.4 nights. Thailand has 9.8, Spain has 9.1, "
                "Mexico has 8.2 and France has 6.5 nights.\n"
                "Overall, France attracts the most visitors, but Spain earns the most revenue. "
                "Thailand earns a lot of revenue with not many visitors, because people stay "
                "longer there. Turkey has the longest stays but not the most revenue."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "The data is accurately reported with a reasonable overview, but the answer is a "
                "straightforward list. The most interesting relationship, between visitor numbers "
                "and revenue, is not explored."
            ),
            "improvement_tips": [
                "Analyse the relationship between visitors and revenue (e.g., Spain earns more than France despite fewer visitors).",
                "Group countries by revenue efficiency or length of stay.",
                "Use comparative language: 'despite', 'in contrast'.",
                "Use vocabulary of ranking and proportion.",
                "Avoid listing all figures; select the most significant ones.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "The table outlines key tourism indicators for five countries: the number of "
                "international visitors, tourism revenue and the average length of stay.\n"
                "Overall, the data shows little direct correspondence between visitor numbers and "
                "revenue. France attracted the most visitors, yet Spain generated the highest "
                "income, largely because visitors stayed longer, a factor that also explains the "
                "strong earnings of Thailand relative to its lower visitor count.\n"
                "France welcomed 89 million visitors, the largest figure, with revenue of 66 "
                "billion US dollars. Spain, with 84 million visitors, earned 92 billion, the "
                "highest in the table. Thailand, despite receiving only 39 million visitors, "
                "generated 63 billion in revenue, helped by an average stay of 9.8 nights. Mexico "
                "and Turkey recorded lower earnings of 24 and 34 billion, although Turkey's stays "
                "were the longest of all at 10.4 nights. France, by contrast, had the shortest "
                "average stay at 6.5 nights.\n"
                "In conclusion, revenue depended not on visitor numbers alone but also on how "
                "long tourists remained and how much they spent."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The response goes beyond listing to identify and explain the key relationship "
                "between visitors, revenue and length of stay. It is well structured with a clear "
                "overview, although some vocabulary could be more varied."
            ),
            "improvement_tips": [
                "Use more sophisticated lexis: 'yielded', 'derived from', 'per-capita'.",
                "Add revenue-per-visitor figures to strengthen the analysis.",
                "Vary the way countries are introduced to avoid repetition.",
                "Shorten some sentences for clarity.",
                "Ensure the conclusion reflects the strongest pattern in the data.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The table sets out three tourism indicators for five countries: international "
                "arrivals, revenue earned, and the average length of stay.\n"
                "The most illuminating insight to emerge is the weak correlation between the "
                "volume of visitors and the revenue generated. Spain, for example, attracted fewer "
                "arrivals than France yet earned substantially more, a discrepancy explained by "
                "longer average stays and, by implication, higher per-visitor spending. Thailand "
                "offers an even more pronounced illustration of this pattern.\n"
                "France recorded the highest number of arrivals at 89 million but generated only "
                "66 billion US dollars, translating to roughly 740 dollars per visitor. Spain, "
                "with 84 million arrivals, produced 92 billion, some 1,100 dollars per visitor, "
                "benefiting from an average stay of 9.1 nights. Thailand, despite modest arrivals "
                "of 39 million, earned 63 billion, a striking 1,600 dollars per head, sustained "
                "by stays averaging 9.8 nights. Turkey, though hosting 51 million visitors, "
                "yielded just 34 billion with the longest average stay of 10.4 nights, while "
                "Mexico, with 41 million arrivals, earned only 24 billion, the lowest revenue in "
                "the table.\n"
                "In essence, the data underscores that visitor numbers alone are a poor predictor "
                "of tourism earnings; length of stay and spending intensity are decisive."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "This response demonstrates outstanding analytical ability, deriving per-visitor "
                "revenue to illuminate the central relationship in the data. It is precise, "
                "insightful and expressed with a sophisticated range of vocabulary and structures."
            ),
            "improvement_tips": [
                "Verify per-visitor calculations against the source figures.",
                "Use derived figures sparingly and clearly label them.",
                "Maintain consistency in currency terminology.",
                "Keep the analytical conclusion grounded in the table.",
                "Balance derived metrics with the original data.",
            ],
        },
    },
    # ---------------- Q13: Household Electricity ----------------
    13: {
        "5": {
            "band": 5,
            "answer_text": (
                "The table shows the percentage of household electricity consumed by different "
                "appliances in 2000 and 2020.\n"
                "In 2000, water heating was the biggest with 22%. Electronics was 20%, lighting "
                "was 18%, refrigeration was 15%, air conditioning was 12% and other was 13%. In "
                "2020, electronics was the biggest with 31%. Air conditioning was 24%, water "
                "heating was 16%, refrigeration was 13%, lighting was 8% and other was 8%. "
                "Electronics went up from 20% to 31%, and air conditioning went up from 12% to "
                "24%. Lighting went down from 18% to 8%, and water heating went down from 22% "
                "to 16%. Refrigeration went down a little from 15% to 13%.\n"
                "Overall, electronics became the biggest user of electricity, and lighting "
                "became much smaller. Air conditioning also grew a lot."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "The data is fully reported with an adequate overview, but the response is a list "
                "of figures with limited analysis of the underlying changes. Language is simple "
                "and repetitive."
            ),
            "improvement_tips": [
                "Highlight the two dominant shifts: electronics overtaking water heating, and lighting halving.",
                "Group appliances into risers and fallers.",
                "Use 'percentage points' to describe the size of changes.",
                "Use varied academic verbs: 'accounted for', 'consumed', 'represented'.",
                "Structure the answer with clear paragraphs.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "The table compares the share of household electricity consumed by six appliances "
                "in 2000 and 2020.\n"
                "Overall, the pattern of consumption changed markedly. Electronics overtook water "
                "heating to become the largest single consumer, while air conditioning gained "
                "ground rapidly and lighting recorded the steepest decline, more than halving its "
                "share.\n"
                "In 2000, water heating led with 22%, closely followed by electronics at 20% and "
                "lighting at 18%, with refrigeration, air conditioning and other uses sharing the "
                "remainder. By 2020, electronics had surged to 31%, and air conditioning had "
                "doubled from 12% to 24%. Water heating, by contrast, fell to 16%, refrigeration "
                "eased slightly to 13%, and lighting collapsed from 18% to just 8%.\n"
                "In conclusion, the decade saw electricity use shift decisively towards "
                "electronics and cooling, at the expense of lighting and water heating."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The response is well structured, with a clear overview and effective grouping of "
                "rising and falling categories. Data is reported accurately with good use of "
                "comparison, though the lexical range could be broader."
            ),
            "improvement_tips": [
                "Use more precise lexis: 'dwindled', 'expanded its share', 'receded'.",
                "Add percentage-point changes for the key movements.",
                "Vary sentence openings to avoid repetition.",
                "Round figures consistently.",
                "Make the conclusion reflect the two most significant trends.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The table charts the distribution of household electricity consumption across "
                "six appliance categories in 2000 and 2020, with the accompanying change expressed "
                "in percentage points.\n"
                "The defining feature of the two decades is a substantial reallocation of "
                "consumption towards electronics and cooling at the expense of lighting and water "
                "heating. Electronics displaced water heating to assume the leading role, while "
                "air conditioning registered the largest relative gain and lighting the steepest "
                "decline.\n"
                "In 2000 water heating was the principal consumer, commanding 22% of the total, "
                "marginally ahead of electronics at 20% and lighting at 18%. By 2020 the hierarchy "
                "had been transformed. Electronics surged to 31%, an eleven-point gain, and air "
                "conditioning doubled to 24%. Meanwhile, water heating receded to 16%, "
                "refrigeration eased from 15% to 13%, and lighting contracted sharply from 18% to "
                "8%, a ten-point collapse. The residual 'other' category also declined, from 13% "
                "to 8%.\n"
                "In essence, the data portrays a household sector in which the rise of electronic "
                "devices and air conditioning has come to dominate the electricity budget, while "
                "traditional uses such as lighting have been dramatically reduced."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "This response is precise, well organised and analytical, capturing both the "
                "reordering of the categories and the magnitude of change. The vocabulary is wide "
                "and accurate, and the grammar is consistently sophisticated."
            ),
            "improvement_tips": [
                "Verify all percentage-point figures.",
                "Avoid redundancy between the 'other' category and the conclusion.",
                "Keep the overview to the most significant two or three changes.",
                "Ensure the final sentence does not overreach beyond the data.",
                "Maintain consistent ordering of categories throughout.",
            ],
        },
    },
    # ---------------- Q14: Island Tourist Development ----------------
    14: {
        "5": {
            "band": 5,
            "answer_text": (
                "The two maps show an island before and after the construction of tourist "
                "facilities.\n"
                "Before, the island was natural. There was a beach on the west coast and a bay on "
                "the south coast. There were trees in the middle.\n"
                "After, they built a lot of things. There are two accommodation areas, one in the "
                "west and one in the south-east. There is a reception and a restaurant in the "
                "north-west. They built a pier in the south-west and a road from the pier to the "
                "reception. There are footpaths from the accommodation to the beach. There is a "
                "swimming area near the beach.\n"
                "Overall, the island became a tourist resort with accommodation and transport "
                "links, while the natural parts stayed mostly the same."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "The main features of both maps are described accurately, but the response is a "
                "basic list of features without precise spatial language or strong organisation. "
                "The overview is present but underdeveloped."
            ),
            "improvement_tips": [
                "Use precise positional language: 'located in the west', 'adjacent to', 'in the south-east'.",
                "Organise the response into clear paragraphs for before and after.",
                "Describe the road and footpath network as a connected system.",
                "Use passive constructions: 'two accommodation areas were built'.",
                "Extend the overview to mention the purpose of the changes.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "The two maps illustrate the transformation of a small island from an undeveloped "
                "natural landscape into a tourist resort.\n"
                "Overall, the development was extensive, introducing accommodation, a reception "
                "area, a restaurant and new transport links, while leaving the central wooded area "
                "and the beach largely untouched.\n"
                "In its original state, the island was dominated by dense vegetation, with a beach "
                "running along the western coast and a small bay on the southern shore. After "
                "development, two clusters of tourist accommodation were constructed, one in the "
                "west and another in the south-east. A reception block and restaurant were built "
                "in the north-west, and a pier was added in the south-west. A main road was laid "
                "from the pier to the reception, from which a branch led to the western "
                "accommodation. Footpaths connected the eastern accommodation to the beach, where "
                "a swimming area was designated.\n"
                "In conclusion, the island was converted into a self-contained resort, with its "
                "natural vegetation and shoreline preserved around the new facilities."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The response describes both maps accurately and coherently, using appropriate "
                "positional language and a clear structure. It includes a good overview, though "
                "the level of detail could be managed more selectively and vocabulary is good "
                "rather than exceptional."
            ),
            "improvement_tips": [
                "Use more varied verbs of construction: 'erected', 'laid out', 'delineated'.",
                "Reduce the number of individual features mentioned to keep focus.",
                "Add explicit spatial comparison between the two maps.",
                "Vary sentence structures to avoid formulaic descriptions.",
                "Strengthen the conclusion by noting the overall layout logic.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The paired maps depict the transformation of an island from an untouched natural "
                "landscape into a fully serviced tourist destination.\n"
                "The development was systematic rather than piecemeal: accommodation was grouped "
                "into two zones, linked to a central reception and restaurant by a road network "
                "that connected to a new pier, while the island's interior vegetation and western "
                "beach were consciously preserved.\n"
                "Originally, the island consisted of little more than scattered vegetation, a "
                "stretch of beach on the west coast and a small bay to the south. Following "
                "construction, the most substantial additions were the two accommodation "
                "complexes, one occupying the western section and the other the south-east, the "
                "latter approached by footpaths leading to the beach and a designated swimming "
                "area. At the north-west, a reception building and restaurant were erected, served "
                "by a pier extending from the south-west coast. From the pier, a main road ran "
                "north-east to the reception, where it branched towards the western "
                "accommodation, completing an efficient internal transport system.\n"
                "In essence, the island was carefully zoned for tourism, balancing new visitor "
                "infrastructure with the preservation of its natural features."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "This is an exemplary response: the spatial organisation is described precisely "
                "and logically, the language is sophisticated and varied, and the overview "
                "captures the rationale of the development. Cohesion and grammar are flawless."
            ),
            "improvement_tips": [
                "Ensure all directions are accurate relative to the map.",
                "Use directional lexis consistently and correctly.",
                "Keep descriptions of infrastructure to what the map actually shows.",
                "Balance overview detail with specific features.",
                "Maintain an impersonal, objective register.",
            ],
        },
    },
    # ---------------- Q15: Town Centre 1990 vs 2020 ----------------
    15: {
        "5": {
            "band": 5,
            "answer_text": (
                "The maps show the centre of a small town in 1990 and in 2020.\n"
                "In 1990, there was a market square in the centre. There was a car park in the "
                "north. There was a factory in the west and residential housing. In the south "
                "there was a train station and an industrial area. There were housing estates in "
                "the east and north-east.\n"
                "In 2020, the car park became a shopping centre. The factory was demolished and "
                "a supermarket was built. The industrial area became a business park. There are "
                "new houses in the west and south. The main road was widened and the centre was "
                "pedestrianised.\n"
                "Overall, the town centre became more modern, with new shopping and housing, "
                "and less industrial."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "All the changes are reported accurately with a basic overview, but the response "
                "reads as a simple list of before and after features. Spatial language is limited "
                "and there is little synthesis."
            ),
            "improvement_tips": [
                "Use precise positional language: 'in the north-west corner', 'south of the station'.",
                "Group changes by type: commercial, residential, industrial.",
                "Use passive voice: 'was converted into', 'was replaced by'.",
                "Add a clearer overview that captures the move from industry to commerce.",
                "Organise into paragraphs: one for each map or one for each type of change.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "The two maps compare the centre of a small town as it appeared in 1990 and 2020, "
                "revealing a substantial programme of regeneration.\n"
                "Overall, the town underwent a clear shift from an industrial to a commercial and "
                "residential character. Former industrial and car-parking areas were redeveloped "
                "for retail, housing and business use, while the road network was improved.\n"
                "In 1990, the town centre was dominated by a market square, with a car park to "
                "the north, a factory and housing in the west, an industrial area and train "
                "station in the south, and further housing in the east and north-east. By 2020 "
                "the picture had changed considerably. The car park had been replaced by a "
                "shopping centre, and the factory had given way to a supermarket with its own "
                "car park. The former industrial zone had been converted into a business park, "
                "while new housing had appeared in the west and south. The main road had been "
                "widened and the central area pedestrianised.\n"
                "In conclusion, the redevelopment transformed the town centre from an industrial "
                "hub into a modern, mixed-use area focused on retail and housing."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The response is well organised with a clear overview and accurate reporting of "
                "all changes. It uses a good range of passive structures and cohesive devices, "
                "though some vocabulary and sentence patterns are repetitive."
            ),
            "improvement_tips": [
                "Use more varied transformation verbs: 'usurped', 'superceded', 'sprang up'.",
                "Group changes thematically (retail, housing, industry) rather than geographically.",
                "Vary the passive structures used.",
                "Round descriptions to avoid listing every detail.",
                "Strengthen the conclusion's analytical edge.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The paired maps chart the regeneration of a small town centre between 1990 and "
                "2020, a period in which the area's economic character was substantially "
                "reconfigured.\n"
                "The most fundamental change was the displacement of industry by commerce and "
                "housing. The industrial zone in the south gave way to a business park, the "
                "factory in the west was demolished in favour of retail, and the car park was "
                "converted into a shopping centre, developments that collectively signal a move "
                "towards a consumer-and-residential economy.\n"
                "In 1990 the town's layout centred on a market square, bordered to the north by a "
                "car park, to the west by a factory and housing, and to the south by a train "
                "station flanked by industrial premises, with residential estates extending to the "
                "east and north-east. By 2020, the car park had been transformed into a shopping "
                "centre, and the factory had been replaced by a supermarket accompanied by a "
                "car park. The southern industrial land had been redeveloped as a business park, "
                "and additional housing had been constructed in the west and south. The main road, "
                "meanwhile, had been widened, and the pedestrianisation of the centre encouraged a "
                "more retail-oriented atmosphere.\n"
                "In essence, the maps illustrate a textbook example of urban renewal, in which "
                "outdated industrial and transport uses were systematically converted into "
                "commercial, residential and business space."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "This is a model answer: it synthesises the changes into a coherent analytical "
                "framework, uses sophisticated and precise vocabulary, and is structured with "
                "exemplary clarity. All spatial and functional changes are accurately captured."
            ),
            "improvement_tips": [
                "Keep interpretive framing (e.g., 'textbook example') clearly as analysis, not assertion of unseen facts.",
                "Balance thematic grouping with accurate spatial detail.",
                "Verify directional accuracy of every feature.",
                "Use varied academic lexis without overstatement.",
                "Ensure the conclusion summarises, not restates.",
            ],
        },
    },
    # ---------------- Q16: Seaside Village ----------------
    16: {
        "5": {
            "band": 5,
            "answer_text": (
                "The maps show the development of a seaside village between 1985 and 2025.\n"
                "In 1985, it was a small fishing village. There were houses along the coast. "
                "There was farmland behind the village. There was one road from the mainland. "
                "There was a small harbour and beach in the west.\n"
                "In 2025, the village is bigger. There are new houses and a hotel complex. The "
                "farmland became hotels and a golf course. There is a new marina and promenade "
                "along the beach. There is a second road and car parks. There are shops, "
                "restaurants and an entertainment centre.\n"
                "Overall, the village changed from a small fishing village to a big tourist "
                "destination."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "The response captures the essential transformation with reasonable accuracy, but "
                "it is a basic before-and-after list. Spatial precision and analytical depth are "
                "limited."
            ),
            "improvement_tips": [
                "Use directional language: 'along the coastline', 'behind the village'.",
                "Group changes into coastal, residential and agricultural categories.",
                "Use the passive voice for construction: 'a marina was built'.",
                "Improve the overview by naming the economic shift (fishing to tourism).",
                "Add a short paragraph comparing the two maps directly.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "The maps trace the transformation of a small seaside village between 1985 and "
                "2025, charting its development into a major tourist resort.\n"
                "Overall, the village expanded considerably, with farmland replaced by tourism "
                "infrastructure and new coastal facilities, while the original fishing character "
                "was largely lost.\n"
                "In 1985, the settlement consisted of a scattering of houses along the coast, "
                "backed by farmland, with a single access road from the mainland, a small harbour "
                "and a beach on the western side. By 2025, the village had grown significantly. "
                "The farmland to the east had been converted into a hotel complex and golf course, "
                "and new housing estates had been built inland. Along the coast, a marina and "
                "promenade had replaced part of the old waterfront, and a second access road with "
                "car parks had been constructed. The village now also boasted shops, restaurants "
                "and an entertainment centre.\n"
                "In conclusion, the maps show a rapid shift from a modest fishing community to a "
                "fully developed seaside resort."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The response is clearly organised and accurately describes the development, with "
                "a strong overview and appropriate spatial language. Vocabulary and cohesion are "
                "good, though the description could be more selective and varied."
            ),
            "improvement_tips": [
                "Use more sophisticated lexis: 'encroached upon', 'gave way to', 'eclipsed'.",
                "Reduce feature lists to focus on the most significant developments.",
                "Vary sentence openings and passive constructions.",
                "Add explicit comparison between coastal and inland changes.",
                "Strengthen the analytical conclusion.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The paired maps document the metamorphosis of a seaside village from a modest "
                "fishing community in 1985 into a substantial tourist resort by 2025.\n"
                "The most conspicuous theme is the wholesale substitution of agricultural and "
                "fishing uses by tourism. Farmland surrendered to hotels and a golf course, the "
                "working harbour was superseded by a modern marina, and the settlement expanded "
                "inland, its infrastructure transformed to serve visitors rather than villagers.\n"
                "In 1985 the village comprised a thin ribbon of houses along the coast, enclosed "
                "on its landward side by farmland, and linked to the mainland by a single road; "
                "its western shoreline contained a small harbour and beach. By 2025 the "
                "settlement had spread inland, with new housing estates and a hotel complex "
                "occupying the former fields. The coastline itself had been reshaped: a marina "
                "and promenade lined the shore, shops, restaurants and an entertainment centre "
                "clustered near the water, and a second access road with associated car parks "
                "had been added. Even the beach had been formalised into a managed tourist asset.\n"
                "In essence, the maps capture a textbook transition from a primary-industry "
                "village to a service-based resort, with the physical fabric of the settlement "
                "reoriented almost entirely around tourism."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "This response is distinguished by its analytical framing and precise, evocative "
                "language. It identifies the underlying economic shift, reports spatial changes "
                "accurately, and maintains flawless coherence and grammar throughout."
            ),
            "improvement_tips": [
                "Ensure 'textbook' and similar framing reads as analysis, not assertion.",
                "Keep every spatial claim consistent with the map.",
                "Balance vivid lexis with factual precision.",
                "Avoid overloading the overview with too many points.",
                "Maintain a consistent chronological structure.",
            ],
        },
    },
    # ---------------- Q17: University Campus Expansion ----------------
    17: {
        "5": {
            "band": 5,
            "answer_text": (
                "The maps show a university campus in 2005 and 2025.\n"
                "In 2005, there was a main entrance in the north with a car park. In the centre "
                "there were lecture halls and a library. In the east there were student "
                "accommodation blocks. There was a sports field in the south and a park in the "
                "west.\n"
                "In 2025, the car park became a student centre. They built two new lecture halls "
                "in the centre. There are new accommodation blocks in the north-east. The sports "
                "field has an indoor sports complex now. The park became a research and "
                "technology park. There is a bus route and cycle paths.\n"
                "Overall, the campus became bigger and more modern, with more facilities for "
                "students."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "The changes are reported accurately with a reasonable overview, but the answer "
                "is a simple list of before/after features. There is limited spatial analysis "
                "and the language is basic."
            ),
            "improvement_tips": [
                "Use positional vocabulary: 'in the north-west', 'adjacent to the library'.",
                "Group changes by type: teaching, accommodation, transport, green space.",
                "Use the passive voice for new construction.",
                "Improve the overview with the campus's overall direction of growth.",
                "Add comparison of how land use changed.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "The maps show how a university campus developed between 2005 and 2025.\n"
                "Overall, the campus expanded and diversified, with new teaching buildings, "
                "additional accommodation and a research park, while the transport network was "
                "improved to serve the growing site.\n"
                "In 2005, the campus had a single entrance in the north, beside a car park, with "
                "lecture halls and a library at the centre, accommodation blocks to the east, a "
                "sports field in the south and a park in the west. By 2025, the car park had been "
                "replaced by a new student centre, and two additional lecture halls had been "
                "built in the central area. The accommodation had expanded with new blocks in the "
                "north-east, and the southern sports field had gained an indoor sports complex. "
                "The most significant change was the conversion of the western park into a "
                "research and technology park. New bus routes and cycle paths had also been "
                "introduced.\n"
                "In conclusion, the campus was transformed from a compact teaching site into a "
                "larger, more modern and research-oriented facility."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The response is well organised, accurately reports all major changes, and "
                "provides a clear overview. It uses good passive structures and spatial language, "
                "though some sections read as a list."
            ),
            "improvement_tips": [
                "Use more varied lexis for construction: 'erected', 'converted into', 'developed'.",
                "Reduce the number of minor details to emphasise the most significant changes.",
                "Vary sentence structures to avoid repetition.",
                "Group the transport improvements together.",
                "Strengthen the conclusion with the overall purpose of the expansion.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The paired maps depict the expansion of a university campus between 2005 and "
                "2025, charting a clear progression from a compact teaching institution to a "
                "larger, research-led site.\n"
                "The overriding pattern is one of intensification and outward growth. The centre "
                "gained additional teaching capacity, the east saw an expansion of student "
                "housing, and, most tellingly, the western parkland was sacrificed to create a "
                "research and technology park, a change that embodies the institution's new "
                "strategic direction.\n"
                "In 2005 the campus was anchored by a main entrance and car park in the north, "
                "central lecture halls and a library, eastern accommodation blocks, a southern "
                "sports field and a western park. By 2025, the northern car park had given way "
                "to a student centre, the central area had been augmented with two further "
                "lecture halls, and the accommodation stock had been enlarged with new blocks in "
                "the north-east. The sports provision had also been upgraded, with an indoor "
                "sports complex attached to the existing field. The park, however, had been "
                "repurposed as a research and technology park, while a new bus route and cycle "
                "paths improved access across the site.\n"
                "In essence, the campus evolved in step with a shift in its academic mission, "
                "trading green space and surface parking for research infrastructure and "
                "enhanced student facilities."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "This response stands out for its analytical interpretation, precise spatial "
                "reporting, and sophisticated, varied language. The structure is exemplary and "
                "the grammar accurate throughout."
            ),
            "improvement_tips": [
                "Keep interpretive claims tied to what the map shows.",
                "Verify all directional references.",
                "Balance thematic and spatial organisation.",
                "Avoid overstatement in the conclusion.",
                "Maintain consistency in tense and voice.",
            ],
        },
    },
    # ---------------- Q18: Water Cycle ----------------
    18: {
        "5": {
            "band": 5,
            "answer_text": (
                "The diagram shows the water cycle.\n"
                "First, the sun heats the water in the ocean. The water evaporates and goes up "
                "into the sky as vapour. Then the vapour cools and becomes clouds. After that, "
                "rain falls from the clouds to the ground. The rain runs over the land and goes "
                "into rivers and lakes. Finally, the water from the rivers goes back to the "
                "ocean.\n"
                "After the water returns to the ocean, the sun heats it again and the cycle "
                "starts again. So this is a continuous process with no beginning and no end. "
                "The sun is the main energy for this process, because without the sun the water "
                "cannot evaporate and the cycle will stop."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "The steps are described in the correct order with basic sequencing words, but "
                "the language is very simple and lacks the precise process vocabulary and range "
                "expected at higher bands. The overview is minimal."
            ),
            "improvement_tips": [
                "Add a clear introductory overview stating the process is cyclical and driven by the sun.",
                "Use more varied sequencing language: 'subsequently', 'thereafter', 'having been...'.",
                "Use passive voice: 'the vapour is cooled and condensed'.",
                "Introduce precise scientific terms: 'evaporation', 'condensation', 'precipitation'.",
                "Describe the process as a continuous cycle in the conclusion.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "The diagram illustrates the water cycle, which operates as a continuous, sun-driven "
                "process.\n"
                "Overall, the cycle consists of three interconnected stages: evaporation, "
                "condensation and precipitation, followed by the return of water to the ocean.\n"
                "The process begins when solar energy heats the surface of the ocean, causing "
                "water to evaporate and rise into the atmosphere as vapour. As the vapour ascends, "
                "it cools and condenses, forming clouds. In due course, precipitation occurs, "
                "with water falling to the ground as rain. This rainfall then flows across the "
                "land surface, collecting in rivers and lakes before eventually draining back "
                "into the ocean, where the cycle recommences.\n"
                "In conclusion, the diagram shows a self-sustaining natural cycle in which solar "
                "energy drives the continuous movement of water from the sea to the sky and back "
                "again."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The response describes the process clearly and accurately with a good overview "
                "and appropriate process vocabulary. Cohesion is strong, though the description "
                "could use slightly more varied lexis and complex structures."
            ),
            "improvement_tips": [
                "Use a wider range of complex structures, including participles and passive forms.",
                "Add more precise lexis: 'transpired', 'percolates', 'discharges'.",
                "Vary the sequencing expressions to avoid repetition.",
                "Strengthen the conclusion's description of the cycle.",
                "Ensure every stage is clearly linked to the next.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The diagram presents the water cycle, a perpetual natural process driven "
                "principally by solar radiation, whereby water circulates between the ocean, "
                "atmosphere and land.\n"
                "The cycle can be understood as a closed loop comprising three core stages. "
                "Energy from the sun causes evaporation from the ocean; the resulting vapour "
                "condenses aloft to form clouds; and the moisture is subsequently released as "
                "precipitation, before the water makes its way, via rivers and lakes, back to "
                "the sea.\n"
                "Initially, solar energy warms the ocean's surface, driving water to evaporate "
                "and ascend as vapour. On reaching the cooler upper atmosphere, the vapour "
                "condenses into clouds. This accumulated moisture is eventually discharged as "
                "rain, which falls upon the land. The rainfall then travels over the surface, "
                "channelled into rivers and lakes, and ultimately returns to the ocean, "
                "thereby completing the cycle and permitting it to begin anew.\n"
                "In essence, the diagram depicts a dynamic and self-reinforcing system in which "
                "the continuous input of solar energy sustains an endless circulation of water "
                "between sea, sky and land."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "This response is outstanding: it frames the cycle analytically, uses precise and "
                "varied scientific vocabulary, and employs a sophisticated range of structures "
                "with flawless cohesion. The overview and conclusion are both incisive."
            ),
            "improvement_tips": [
                "Keep scientific terminology accurate and consistent.",
                "Avoid over-elaborate phrasing that obscures clarity.",
                "Ensure the sequence is unambiguous throughout.",
                "Balance long sentences with shorter ones.",
                "Maintain the impersonal academic register.",
            ],
        },
    },
    # ---------------- Q19: Cement Production ----------------
    19: {
        "5": {
            "band": 5,
            "answer_text": (
                "The diagrams show how to make cement and how to use it to make concrete for "
                "building.\n"
                "First, limestone and clay are crushed into a powder. Then the powder is mixed "
                "together. After that, the mixture goes into a rotating heater, where it is "
                "heated. Then it is ground in a mill to make cement powder. The cement is "
                "finally put into bags.\n"
                "To make concrete, the cement is mixed with water, sand and gravel in a "
                "concrete mixer. The concrete is then used for building purposes.\n"
                "Overall, the whole process has two main parts: first making cement from "
                "limestone and clay, and second making concrete from cement, water, sand and "
                "gravel."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "The stages are described in order with accurate basic information, but the "
                "response is a simple list. Language is basic, with limited process vocabulary "
                "and few complex structures."
            ),
            "improvement_tips": [
                "Add an overview describing the two-part nature of the process.",
                "Use precise vocabulary: 'crushed', 'ground', 'combined'.",
                "Include the equipment mentioned (rotating heater, mill, mixer) accurately.",
                "Use passive voice consistently.",
                "Describe the proportions used in concrete making if shown.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "The diagrams outline the manufacture of cement and its subsequent use in the "
                "production of concrete for building purposes.\n"
                "Overall, the cement-making process involves three main stages: preparing the raw "
                "materials, heating them, and grinding the resulting product. Concrete is then "
                "produced by combining cement with water, sand and gravel.\n"
                "In the first stage, limestone and clay are crushed into a powder and mixed "
                "together. This mixture is passed through a rotating heater, where it undergoes "
                "intense heating, before being ground in a mill to produce the fine cement "
                "powder, which is then packed into bags.\n"
                "In the second stage, this cement is used to make concrete. The cement is "
                "combined with water, sand and gravel in a concrete mixer, and the resulting "
                "mixture can be used for building.\n"
                "In conclusion, the two diagrams together show a two-stage process in which raw "
                "minerals are transformed first into cement and then into a building material."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The response is well structured, accurately describes both stages and uses "
                "appropriate passive constructions. Cohesion is good, though a wider range of "
                "process lexis would improve it."
            ),
            "improvement_tips": [
                "Use more specific lexis: 'subjected to heat', 'pulverised', 'blended'.",
                "Mention the proportions of concrete ingredients if shown on the diagram.",
                "Vary the sequencing phrases across the response.",
                "Use some complex participial constructions.",
                "Strengthen the final sentence to reflect the building purpose.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The diagrams depict the industrial manufacture of cement and the subsequent "
                "preparation of concrete, the two stages together comprising the production "
                "chain by which raw minerals are converted into a construction material.\n"
                "The process is essentially linear. In the cement-making phase, crushed "
                "limestone and clay are blended, heated and ground into a fine powder; in the "
                "concrete-making phase, this powder is combined with water, sand and gravel to "
                "produce the final building material.\n"
                "Cement production commences with the crushing of limestone and clay into a "
                "powder, after which the two materials are mixed thoroughly. The blended "
                "mixture is then fed through a rotating heater, where it is subjected to "
                "sustained high temperatures. Having been heated, the material is ground in a "
                "mill, yielding the fine grey powder known as cement, which is subsequently "
                "packaged into bags.\n"
                "To make concrete, the cement is combined in a mixer with water, sand and "
                "gravel in the proportions indicated, and the resulting mixture is ready for "
                "use in construction.\n"
                "In essence, the diagrams illustrate a two-stage transformation in which the "
                "same initial product, cement, serves as the vital binding ingredient in the "
                "production of concrete."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "This is a polished, fully developed response. It captures the linear structure "
                "of the process, uses a wide and precise range of vocabulary, and employs complex "
                "grammatical structures (participial phrases, passives) with total accuracy."
            ),
            "improvement_tips": [
                "Ensure terminology ('pulverised', 'subjected to') is accurate.",
                "Keep proportions consistent with the diagram.",
                "Avoid redundancy between overview and detail.",
                "Vary the passive structures used.",
                "Check that all equipment mentioned is included accurately.",
            ],
        },
    },
    # ---------------- Q20: Glass Recycling ----------------
    20: {
        "5": {
            "band": 5,
            "answer_text": (
                "The diagram shows the recycling process of glass bottles.\n"
                "First, used glass bottles are placed in recycling collection bins by people. "
                "Then the bottles are collected and taken to a recycling plant. At the plant, "
                "the glass is washed to remove dirt and sorted by colour into clear, green, and "
                "brown glass. After that, the sorted glass is crushed into small pieces called "
                "cullet. Then the cullet is melted in a high-temperature furnace. Next, the "
                "liquid glass is moulded into new bottles and jars. Finally, the new glass "
                "products are delivered to shops for people to use again.\n"
                "Overall, this is a circular recycling process. Old glass bottles are collected, "
                "crushed, melted and made into new products, so the cycle can repeat."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "The steps are described in chronological order with accurate basic details. "
                "However, sentence structures are simple and repetitive, with limited process-specific vocabulary."
            ),
            "improvement_tips": [
                "Include a formal overview in a separate paragraph.",
                "Use passive structures more consistently (e.g. 'is crushed', 'is melted').",
                "Vary sequencing transitions beyond 'First', 'Then', 'After that'.",
                "Use technical terms like 'cullet' and 'furnace' with explanations.",
                "Group the initial collection stages and manufacturing stages.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "The diagram illustrates the stage-by-stage recycling process for glass bottles and jars, "
                "operating as a continuous loop.\n"
                "Overall, the process comprises seven key stages, starting with the collection of used glass "
                "and culminating in the distribution of new glass items to retail outlets, allowing the cycle to repeat.\n"
                "In the initial stage, consumers dispose of used glass in dedicated recycling bins, after which the "
                "material is gathered and transported to a central recycling plant. Upon arrival, the glass undergoes "
                "washing to remove contaminants before being sorted according to colour (typically clear, green, and brown). "
                "The sorted glass is then crushed into small fragments known as cullet. Following this, the cullet is "
                "transferred to a high-temperature furnace where it is melted into liquid glass. This molten glass is "
                "subsequently poured into moulds to create new bottles and jars. Finally, these newly formed glass "
                "containers are supplied to shops, completing the loop.\n"
                "In conclusion, the diagram depicts a closed-loop recycling system that reclaims glass waste and "
                "converts it into new consumer packaging."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The answer provides a clear overview and logical sequencing of all stages. Passive voice is used "
                "effectively throughout, and vocabulary is accurate and appropriate for Task 1."
            ),
            "improvement_tips": [
                "Use more varied complex sentence structures such as participial phrases.",
                "Incorporate additional process vocabulary like 'molten', 'reclaimed', 'remoulded'.",
                "Avoid repeating 'glass' frequently by using pronouns or synonyms.",
                "Refine stage grouping into collection/preparation vs thermal processing.",
                "Ensure smooth transitions between mechanical and thermal stages.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The diagram delineates the cyclical recycling process of glass containers, detailing the sequence "
                "through which post-consumer glass waste is reprocessed into new glassware.\n"
                "It is immediately evident that the process is closed-loop and consists of seven distinct stages. "
                "These can be broadly categorised into three main phases: waste collection and sorting, mechanical "
                "crushing and thermal melting, and finally, product remanufacturing and retail distribution.\n"
                "The sequence commences with the disposal of used glass bottles into designated recycling bins by households. "
                "Once collected, the glass is conveyed to a processing facility where it is thoroughly washed and "
                "segregated by color—specifically clear, green, and brown—to maintain material purity. Subsequently, "
                "the sorted glass is crushed into fine fragments, termed cullet. This cullet is then fed into a "
                "high-temperature furnace, where intense heat transforms the solid particles into a molten liquid state. "
                "The liquid glass is subsequently channelled into precision moulds to fabricate new bottles and jars. "
                "Once cooled, these pristine glass products are dispatched to retail stores for consumer purchase, "
                "thereby completing the cycle.\n"
                "In summary, the diagram illustrates a fully renewable system that minimizes resource consumption by "
                "endlessly recirculating glass packaging through mechanical and thermal reprocessing."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "An exceptional Band 9 response. It groups stages logically into cohesive phases, employs sophisticated "
                "passive and participial grammar, and displays precise technical vocabulary throughout."
            ),
            "improvement_tips": [
                "Maintain high precision in technical terminology throughout.",
                "Balance detailed descriptions with overarching analytical points.",
                "Ensure seamless cohesion between paragraph transitions.",
                "Vary sentence length for optimal academic rhythm.",
                "Sustain an authoritative impersonal register.",
            ],
        },
    },
    # ---------------- Q21: Hydroelectric Power Generation ----------------
    21: {
        "5": {
            "band": 5,
            "answer_text": (
                "The diagram shows how electricity is made in a hydroelectric power station.\n"
                "First, water is collected in a large reservoir behind a high dam. Then the water flows "
                "down through an intake gate into a pipe called a penstock. The fast-flowing water turns "
                "a turbine at high speed. After that, the spinning turbine powers a generator to make "
                "electricity. Next, the electricity goes through a transformer, which increases the "
                "voltage. Then the electricity is sent through high-voltage power lines to homes and "
                "factories. Finally, the used water flows out into the river below the dam.\n"
                "Overall, the process turns water energy into electrical power through several stages "
                "from the reservoir to the power lines."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "The process is described in chronological order with accurate basic facts. However, the language "
                "is simple and relies heavily on basic linkers like 'First', 'Then', 'After that'."
            ),
            "improvement_tips": [
                "Write a clear overview paragraph highlighting the conversion of mechanical energy to electrical energy.",
                "Use passive structures consistently (e.g. 'is channelled', 'is generated').",
                "Incorporate technical terminology like 'potential energy', 'kinetic energy', 'step-up transformer'.",
                "Vary sentence starters to avoid repetitive sequencing.",
                "Group the mechanical stage (water flow/turbine) and electrical stage (generator/grid).",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "The diagram illustrates the mechanism by which hydroelectric power stations generate electricity "
                "from stored water.\n"
                "Overall, the generation of hydroelectric power is a continuous linear process comprising seven main "
                "stages. It begins with the storage of water behind a dam and concludes with the distribution of "
                "electricity via the power grid and the discharge of water into a river.\n"
                "Initially, water is impounded in a high-level reservoir retained by a dam. When electricity is needed, "
                "an intake gate opens, allowing water to rush downwards through a sloping penstock pipe. The kinetic "
                "energy of this rapidly flowing water rotates a turbine, which in turn drives an adjacent generator "
                "to produce electricity. The generated electric power then passes through a transformer to adjust its "
                "voltage for long-distance transmission. High-voltage power lines subsequently transport the electricity "
                "to the national grid. Meanwhile, the water that passed through the turbine is safely discharged into the "
                "river downstream.\n"
                "In conclusion, the diagram demonstrates how potential energy stored in elevated water is converted first "
                "into mechanical energy by the turbine and ultimately into electrical power for public distribution."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "A clear, well-structured Band 7 response. It accurately describes the entire process using appropriate "
                "technical vocabulary, strong passive voice constructions, and a logical progression of ideas."
            ),
            "improvement_tips": [
                "Use complex participial phrases to combine related mechanical steps.",
                "Describe the turbine cross-section details if shown.",
                "Vary connectives beyond 'Initially', 'subsequently', 'Meanwhile'.",
                "Emphasize energy transformation terminology (potential to kinetic to electrical).",
                "Ensure smooth transitions between hydro mechanics and power transmission.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The diagram details the structural components and operational steps involved in generating electricity "
                "within a hydroelectric power plant.\n"
                "It is clear that hydroelectricity generation is a multi-step linear process that converts the potential "
                "energy of impounded water into usable electrical energy. The process spans two main phases: the hydraulic "
                "phase, involving water flow and mechanical turbine rotation, and the electrical phase, involving power "
                "generation, step-up transformation, and grid distribution.\n"
                "The process commences with water being impounded in an elevated reservoir behind a dam. Controlled release "
                "via an intake gate channels the water into a descending penstock, where gravitational force accelerates "
                "the flow. Upon reaching the bottom, the high-pressure water stream impinges on the blades of a turbine, "
                "causing it to spin rapidly. This mechanical rotation drives an interconnected generator, converting "
                "rotational kinetic energy into electrical power. The electricity produced is then fed into a transformer, "
                "which elevates the voltage to minimize line losses during long-distance transmission over power lines. "
                "Concurrently, the water discharged from the turbine is returned to the natural river system downstream.\n"
                "In summary, the diagram depicts an efficient energy conversion system in which natural gravitational water "
                "flow is harnessed through mechanical turbines and electromagnetic generators to supply electricity to the "
                "power grid."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "An exemplary Band 9 response. It categorizes the system into hydraulic and electrical phases, utilizes "
                "precise physics and engineering vocabulary, and exhibits immaculate grammatical control and cohesion."
            ),
            "improvement_tips": [
                "Sustain the precise technical register throughout.",
                "Ensure all diagram components are referenced accurately.",
                "Maintain seamless logical flow between sentences.",
                "Vary sentence structures between simple, compound, and complex forms.",
                "Keep the tone strictly objective and academic.",
            ],
        },
    },
    # ---------------- Q22: Cinema Attendance and Ticket Prices ----------------
    22: {
        "5": {
            "band": 5,
            "answer_text": (
                "The line graph shows cinema attendance in the UK from 2010 to 2020, and the bar "
                "chart shows the average ticket price over the same period.\n"
                "Attendance was 170 million in 2010. It went down to 160 million in 2012, then "
                "went up to 175 million in 2014, 180 million in 2016 and 190 million in 2018. In "
                "2020 it went down very much to 80 million. The ticket price was 6.2 GBP in "
                "2010, 7.0 GBP in 2014, 7.8 GBP in 2018 and 9.1 GBP in 2020.\n"
                "Overall, attendance went up until 2018 but fell a lot in 2020. The ticket "
                "price went up all the time, so the price was highest in 2020 when attendance "
                "was lowest."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "Both charts are reported with accurate figures and a basic overview is provided, "
                "but the response lists data without connecting the two charts. There is no "
                "analysis of the relationship between attendance and price."
            ),
            "improvement_tips": [
                "Add an overview linking the two charts (e.g., the 2020 fall in attendance alongside rising prices).",
                "Group the attendance data into clear phases rather than listing each year.",
                "Use comparative language between the two datasets.",
                "Use more precise vocabulary: 'plummeted', 'rose steadily'.",
                "Structure the answer with a paragraph for each chart.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "The line graph tracks cinema attendance in the UK between 2010 and 2020, while "
                "the accompanying bar chart shows the average ticket price over the same period.\n"
                "Overall, attendance followed an upward trend until 2018 but then collapsed "
                "sharply in 2020, the year in which ticket prices reached their highest level. "
                "This suggests that the final fall in attendance coincided with a substantial "
                "price increase.\n"
                "Attendance stood at 170 million visits in 2010, dipped to 160 million in 2012, "
                "and then rose steadily to 190 million by 2018. In 2020, however, it plummeted to "
                "just 80 million, less than half the 2018 figure. Ticket prices, by contrast, "
                "increased continuously throughout the decade, climbing from 6.2 GBP in 2010 to "
                "7.8 GBP in 2018 and reaching 9.1 GBP in 2020.\n"
                "In conclusion, while rising prices did not initially deter audiences, the "
                "dramatic decline in attendance in 2020 coincided with the highest ticket prices "
                "of the period."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The response connects the two charts effectively, notes the correlation between "
                "price and attendance, and is well organised. It uses accurate figures and good "
                "cohesive devices, though the analysis could be pushed slightly further."
            ),
            "improvement_tips": [
                "Be careful not to overstate causation; describe coincidence rather than cause.",
                "Use more sophisticated lexis: 'commensurate with', 'diverged'.",
                "Vary the way figures are presented.",
                "Round ticket prices consistently.",
                "Strengthen the conclusion's link between the datasets.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The two visualisations chart UK cinema attendance and average ticket prices "
                "across the same decade, from 2010 to 2020.\n"
                "The relationship between the two datasets is striking. For most of the period, "
                "attendance rose despite steadily climbing prices, suggesting that ticket cost "
                "was not the principal driver of cinema-going. The single exception occurred in "
                "2020, when attendance collapsed by well over half at the very moment prices "
                "reached a decade-high, an inversion that points to exceptional, rather than "
                "price-led, circumstances.\n"
                "Between 2010 and 2018, attendance generally trended upwards, easing from 170 "
                "million to a peak of 190 million visits, notwithstanding a small dip in 2012. "
                "In 2020, however, attendance plunged to 80 million, a fall of more than 58% "
                "from its peak. Ticket prices, in contrast, moved in one direction throughout: "
                "rising from 6.2 GBP in 2010 to 7.0 GBP in 2014, 7.8 GBP in 2018 and a high of "
                "9.1 GBP in 2020.\n"
                "In essence, the data reveals an uneasy relationship between the two series: "
                "price inflation and growing attendance coexisted for most of the decade, before "
                "both indicators diverged dramatically in the final year."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "This response is exceptional: it frames the two charts as a related dataset, "
                "identifies the key relationship and its exception, and uses precise, varied "
                "language throughout. The structure and grammar are flawless."
            ),
            "improvement_tips": [
                "Keep causal language carefully hedged ('points to', not 'proves').",
                "Verify percentage calculations.",
                "Balance the two charts equally in the detail section.",
                "Avoid overlong sentences in the overview.",
                "Ensure the conclusion synthesises both series.",
            ],
        },
    },
    # ---------------- Q23: Energy Sources and Consumption ----------------
    23: {
        "5": {
            "band": 5,
            "answer_text": (
                "The pie chart shows the sources of electricity in one country, and the bar "
                "chart shows electricity consumption by sector in the same year.\n"
                "Coal is the biggest source of electricity with 30%. Natural gas is 25%, hydro "
                "is 20%, nuclear is 15% and renewables are 10%. Coal and gas together are 55%, "
                "so more than half of the electricity comes from fossil fuels. For consumption, "
                "industry uses the most electricity with 450 TWh. Residential uses 320 TWh, "
                "commercial uses 280 TWh and agriculture uses only 60 TWh.\n"
                "Overall, coal is the main source of electricity, and industry is the main "
                "consumer of electricity. Agriculture uses much less electricity than the other "
                "sectors."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "The key data from both charts is reported with a basic overview, but the "
                "response is short and does not connect the two charts in any meaningful way. "
                "There is little comparison or analysis."
            ),
            "improvement_tips": [
                "Add a fuller overview linking production and consumption.",
                "Group the energy sources (fossil vs non-fossil) and sectors (industry dominant).",
                "Use more precise vocabulary: 'accounted for', 'consumed'.",
                "Extend the answer to the required length.",
                "Use comparative structures across the two charts.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "The pie chart illustrates the sources of electricity in one country, while the "
                "bar chart shows how that electricity was consumed by sector in the same year.\n"
                "Overall, the country relied heavily on fossil fuels, with coal and gas together "
                "providing more than half of all electricity. On the demand side, industry was "
                "by far the largest consumer, accounting for roughly a third of the total.\n"
                "Coal supplied the largest share of generation at 30%, followed by gas at 25%, "
                "so fossil fuels accounted for 55% of the total. Hydro contributed 20%, nuclear "
                "15% and renewables 10%. Turning to consumption, industry used 450 TWh, well "
                "ahead of the residential sector at 320 TWh and commercial use at 280 TWh. "
                "Agriculture consumed only 60 TWh, the smallest amount.\n"
                "In conclusion, the country's electricity system was dominated by fossil fuel "
                "generation and industrial demand."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The response is well organised, reports both charts accurately and connects "
                "them through a clear overview. Cohesion and vocabulary are good, though more "
                "analytical depth could be added."
            ),
            "improvement_tips": [
                "Add a comparison linking generation type to the largest consuming sector.",
                "Use more varied lexis: 'generated', 'furnished', 'absorbed'.",
                "Vary the way figures are introduced.",
                "Round figures naturally where appropriate.",
                "Strengthen the analytical conclusion.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The paired charts present the supply side of a country's electricity system, "
                "broken down by generation source, alongside the corresponding demand side, "
                "distributed across four consuming sectors.\n"
                "The most salient point is the structural asymmetry between production and "
                "consumption: generation was dominated by fossil fuels, coal and gas jointly "
                "providing over half the supply, while demand was led overwhelmingly by "
                "industry, which consumed roughly a third of the total. Renewable and nuclear "
                "sources together supplied a quarter of generation, a notable but still "
                "secondary share.\n"
                "On the supply side, coal was the leading source at 30%, closely followed by gas "
                "at 25%, yielding a combined fossil-fuel share of 55%. Hydro contributed a "
                "further 20%, with nuclear at 15% and renewables at 10%. On the demand side, "
                "industry dominated, using 450 TWh, against 320 TWh for residential and 280 TWh "
                "for commercial users. Agriculture, at 60 TWh, accounted for only a marginal "
                "fraction of consumption.\n"
                "In essence, the charts reveal a system reliant on conventional fuels to meet a "
                "demand profile concentrated in the industrial sector, with cleaner generation "
                "still occupying a subordinate position."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "This response is analytically sharp, structuring the data around the "
                "supply-demand relationship and reporting precise figures with a sophisticated "
                "lexical range. The grammar and cohesion are exemplary."
            ),
            "improvement_tips": [
                "Verify that the percentages sum correctly across sources.",
                "Keep the supply-demand framing consistent.",
                "Balance the two charts in the detail section.",
                "Avoid overly dense sentences.",
                "Ensure the conclusion stays data-grounded.",
            ],
        },
    },
    # ---------------- Q24: International Students ----------------
    24: {
        "5": {
            "band": 5,
            "answer_text": (
                "The table shows the number of international students at a university by region "
                "of origin in 2015 and 2020, and the pie chart shows the proportion studying in "
                "each faculty in 2020.\n"
                "Asia has the most students. In 2015 there were 1200 and in 2020 there were "
                "2100. Europe had 900 in 2015 and 950 in 2020. Africa had 400 in 2015 and 650 "
                "in 2020. The Americas had 500 in 2015 and 550 in 2020. For the faculties, "
                "Engineering has 35% of the international students, Business has 28%, Science "
                "has 22% and Humanities has 15%.\n"
                "Overall, Asia grew the most and is still the biggest region. Engineering is "
                "the most popular faculty for international students in 2020, and Humanities "
                "is the least popular."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "The data is reported accurately with a basic overview, but the response simply "
                "lists the figures from each visual without connecting them or highlighting the "
                "most significant trends. Language is basic."
            ),
            "improvement_tips": [
                "Add an overview linking the two charts (e.g., Asia's growth feeding engineering's popularity).",
                "Highlight Asia's dominance and the scale of its growth.",
                "Use comparison language for the regional changes.",
                "Use academic vocabulary: 'accounted for', 'recorded growth'.",
                "Structure the answer with a paragraph for each visual.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "The table shows the number of international students at a university by region "
                "of origin in 2015 and 2020, while the pie chart breaks down the same student "
                "body by faculty in 2020.\n"
                "Overall, the university saw a substantial rise in international enrolment, "
                "driven overwhelmingly by students from Asia. In terms of academic choice, "
                "Engineering was the most popular faculty, taking more than a third of "
                "international students.\n"
                "Asian students increased sharply, from 1,200 in 2015 to 2,100 in 2020, and "
                "remained by far the largest group. Europe grew more modestly, from 900 to 950, "
                "while Africa rose from 400 to 650 and the Americas from 500 to 550. Within the "
                "university, Engineering accounted for 35% of international students in 2020, "
                "followed by Business at 28%, Science at 22% and Humanities at 15%.\n"
                "In conclusion, the international student body expanded considerably between "
                "2015 and 2020, with Asia contributing the bulk of the growth and Engineering "
                "the preferred field of study."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The response is well structured, accurately reports both visuals, and draws a "
                "clear link between the growth in numbers and the faculty distribution. Cohesion "
                "and vocabulary are good, though more analytic depth is possible."
            ),
            "improvement_tips": [
                "Add explicit percentage growth for Asia's increase.",
                "Connect the faculty data back to the regional data where relevant.",
                "Use more varied lexis: 'enrolled', 'commanded', 'preferred'.",
                "Vary sentence openings to reduce repetition.",
                "Round large numbers consistently.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The two visuals present complementary views of a university's international "
                "student population: the table traces enrolments by region of origin between "
                "2015 and 2020, while the pie chart profiles the same cohort by faculty in 2020.\n"
                "Taken together, the data reveals a university whose international intake is "
                "expanding rapidly, with Asia not only the dominant source but also the engine "
                "of that growth, accounting for the overwhelming majority of new students. "
                "Mirroring this expansion, the student body was heavily concentrated in "
                "engineering and business, the two most professional-oriented faculties.\n"
                "Between 2015 and 2020, Asian enrolments climbed from 1,200 to 2,100, a rise of "
                "75%, dwarfing the growth recorded elsewhere: Europe edged up from 900 to 950, "
                "Africa from 400 to 650, and the Americas from 500 to 550. In 2020, Engineering "
                "commanded 35% of international students, with Business taking 28%, Science 22% "
                "and Humanities 15%, a distribution strongly weighted towards technical and "
                "commercial fields.\n"
                "In essence, the data portrays a university increasingly internationalised at "
                "its core, drawing its expansion chiefly from Asia and channelling those "
                "students into engineering and business."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "This is an outstanding response that synthesises both visuals into a single "
                "analytical narrative. It uses precise data, draws meaningful connections, and "
                "demonstrates a sophisticated command of vocabulary and grammar throughout."
            ),
            "improvement_tips": [
                "Verify the percentage-growth calculation.",
                "Ensure the 'engine of growth' claim is supported by the figures.",
                "Balance the treatment of both visuals equally.",
                "Avoid overstatement in the conclusion.",
                "Maintain consistent tense usage.",
            ],
        },
    },
    # ---------------- Q25: Town Development and Population ----------------
    25: {
        "5": {
            "band": 5,
            "answer_text": (
                "The map shows the development of a town between 1990 and 2020, and the table "
                "shows its population growth.\n"
                "In 1990, there was a small town centre with a railway station in the south. "
                "There was farmland around the town and one main road. In 2020, the town is "
                "bigger. There are new houses in the north and west. There is an industrial park "
                "in the east and a ring road. There is a new shopping centre near the station. "
                "The population was 12,000 in 1990. It was 18,000 in 2000, 32,000 in 2010 and "
                "55,000 in 2020.\n"
                "Overall, the town grew bigger and the population increased a lot."
            ),
            "task_achievement": 5,
            "coherence_cohesion": 5,
            "lexical_resource": 5,
            "grammatical_range": 5,
            "explanation": (
                "Both the map and table are described accurately with a basic overview, but the "
                "response does not explicitly link the population growth to the physical "
                "expansion of the town. Language is simple."
            ),
            "improvement_tips": [
                "Explicitly connect population growth to the town's physical expansion.",
                "Use positional language: 'to the north', 'enclosing the town'.",
                "Group the map changes by type: housing, industry, transport.",
                "Use the passive voice for construction.",
                "Add percentage growth figures for the population.",
            ],
        },
        "7": {
            "band": 7,
            "answer_text": (
                "The map shows the physical development of a town between 1990 and 2020, while "
                "the table tracks its population over the same period.\n"
                "Overall, the two sources tell a consistent story of rapid urban growth. The "
                "population more than quadrupled, and the town expanded accordingly, with new "
                "housing, an industrial park and improved transport infrastructure.\n"
                "In 1990 the town was compact, comprising a small centre, a railway station to "
                "the south, farmland on the outskirts and a single north-south road. By 2020 it "
                "had expanded significantly: new housing appeared in the north and west, an "
                "industrial park was built in the east, and a ring road was added around the "
                "town. A new shopping centre was also constructed near the station. This "
                "expansion mirrored the population figures, which rose from 12,000 in 1990 to "
                "18,000 in 2000, 32,000 in 2010 and 55,000 in 2020.\n"
                "In conclusion, the maps and table together illustrate a clear relationship "
                "between population growth and the physical expansion of the town."
            ),
            "task_achievement": 7,
            "coherence_cohesion": 7,
            "lexical_resource": 7,
            "grammatical_range": 7,
            "explanation": (
                "The response integrates the map and table effectively, noting the relationship "
                "between population growth and urban expansion. It is well organised and "
                "accurate, with good cohesion, though the language could be more varied."
            ),
            "improvement_tips": [
                "Use more precise lexis: 'encroached on farmland', 'annexed', 'encircled'.",
                "Add percentage growth for the population figures.",
                "Vary the sentence structures.",
                "Round figures naturally.",
                "Strengthen the analytical link in the conclusion.",
            ],
        },
        "9": {
            "band": 9,
            "answer_text": (
                "The paired sources chart the transformation of a town over three decades: a map "
                "records its physical expansion between 1990 and 2020, while a table traces its "
                "population over the same interval.\n"
                "The two datasets are mutually reinforcing, telling a single story of rapid and "
                "sustained growth. The population more than quadrupled, from 12,000 to 55,000, "
                "and the physical fabric of the town kept pace, spreading outwards into former "
                "farmland, acquiring new residential districts, an industrial park and a "
                "substantially upgraded transport network.\n"
                "In 1990 the settlement was essentially a small town: a modest centre, a railway "
                "station on its southern fringe, surrounding farmland and a single arterial road "
                "running north to south. By 2020, however, the built area had expanded "
                "considerably. Housing estates had been developed to the north and west, an "
                "industrial park had been established in the east, and a ring road now encircled "
                "the town, complementing a new shopping centre built adjacent to the station. "
                "This outward growth was mirrored in the demographic record, with the population "
                "rising to 18,000 in 2000, 32,000 in 2010 and 55,000 in 2020, roughly 1.7 times "
                "the 2000 figure and more than four times the 1990 total.\n"
                "In essence, the data depicts a town in a phase of rapid urbanisation, in which "
                "demographic expansion drove, and was accommodated by, a wholesale enlargement "
                "of the urban fabric."
            ),
            "task_achievement": 9,
            "coherence_cohesion": 9,
            "lexical_resource": 9,
            "grammatical_range": 9,
            "explanation": (
                "This response is exemplary in its integration of the two data sources, its "
                "analytical framing, and its precise, sophisticated language. The grammar and "
                "cohesion are flawless, and the overview is insightful."
            ),
            "improvement_tips": [
                "Verify all demographic calculations.",
                "Keep spatial descriptions accurate to the map.",
                "Balance the treatment of map and table.",
                "Avoid causal overstatement; frame as correlation.",
                "Maintain consistent tense and register.",
            ],
        },
    },
}
