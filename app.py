import random
from fasthtml.common import *
from dataclasses import dataclass

VIDEO_IDS = [
    "wJwUjuKr_54",
    "SAmxlMQb4LA",
    "rGD5U8u1Dk0",
    "KNexS61fjus",
    "AR62ph7FPs0",
    "zP9_TemzFZs",
    "hLvWy2b857I",
    "pyf8cbqyfPs",
    "bNKXxwOQYB8",
    "dZs_cLHfnNA",
    "4vbDFu0PUew",
    "UBURTj20HXI",
]

tailwind = Script(src="https://cdn.tailwindcss.com")
tailwind_config = Script(src="tailwind_config.js")

google_icons = Link(
    rel="stylesheet",
    href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0",
)

echarts = Script(src="https://cdn.jsdelivr.net/npm/echarts@5.5.1/dist/echarts.min.js")

app, rt = fast_app(
    live=True, pico=False, hdrs=(tailwind, tailwind_config, google_icons, echarts)
)


@dataclass
class Card:
    artist: str
    title: str
    video_id: str
    number_sales: float
    number_likes: float

    def __ft__(self):
        card_top = Div(
            Div(
                Img(
                    src=f"http://img.youtube.com/vi/{self.video_id}/maxresdefault.jpg",
                    cls="h-full object-fill rounded-tl-md",
                ),
                cls="w-1/3",
            ),
            Div(
                P(
                    self.artist,
                    cls="text-sm font-normal overflow-hidden text-ellipsis whitespace-nowrap",
                ),
                P(
                    self.title,
                    cls="text-md font-semibold overflow-hidden text-ellipsis whitespace-nowrap",
                ),
                cls="w-2/3 px-3 py-2",
            ),
            cls="flex h-full",
        )
        dark_gap = Div(cls="bg-slate-400 h-0.5")
        card_bottom = Div(
            Div(
                Span("visibility", cls="material-symbols-outlined"),
                Span(f"{self.number_sales:,}"),
                cls="flex gap-2 items-center",
            ),
            Div(
                Span("thumb_up", cls="material-symbols-outlined"),
                Span(f"{self.number_likes:,}"),
                cls="flex gap-2 items-center",
            ),
            cls="flex justify-evenly py-1 h-8",
        )
        return Div(
            card_top,
            dark_gap,
            card_bottom,
            id=self.video_id,
            cls="h-full flex flex-col justify-around bg-slate-300 rounded-md shadow-lg",
        )


@dataclass
class LiveScreen:
    cover_link: str
    number_views: float
    number_likes: float
    number_comments: float

    def __ft__(self):
        header = Div(
            Div(
                Span("0", cls="text-xl font-bold"),
                Span("Days"),
                cls="flex gap-2 items-end",
            ),
            Div(
                Span("19", cls="text-xl font-bold"),
                Span("Hours"),
                cls="flex gap-2 items-end",
            ),
            Div(
                Span("38", cls="text-xl font-bold"),
                Span("Minutes"),
                cls="flex gap-2 items-end",
            ),
            Div(
                Span("27", cls="text-xl font-bold"),
                Span("Seconds"),
                cls="flex gap-2 items-end",
            ),
            cls="flex justify-evenly py-0.5 h-8",
        )
        cover = (
            Div(
                Img(src=self.cover_link, cls="object-cover object-top w-full h-full"),
                cls="h-3/5 overflow-hidden",
            ),
        )
        counter_views = (
            Div(
                H1(f"{self.number_views:,}", cls="text-6xl font-bold"),
                cls="flex-auto flex justify-center items-center",
            ),
        )
        dark_gap = Div(cls="bg-slate-400 h-0.5")
        footer = (
            Div(
                Div(
                    Span("thumb_up", cls="material-symbols-outlined"),
                    Span(f"{self.number_likes:,}", cls="text-lg font-semibold"),
                    cls="flex gap-2 items-end",
                ),
                Div(
                    Span("forum", cls="material-symbols-outlined"),
                    Span(f"{self.number_comments:,}", cls="text-lg font-semibold"),
                    cls="flex gap-2 items-end",
                ),
                cls="flex justify-evenly py-1 h-8",
            ),
        )
        return Div(
            header,
            cover,
            counter_views,
            dark_gap,
            footer,
            cls="flex flex-col justify-around bg-slate-300 rounded-md shadow-lg h-full",
        )


@app.get("/")
def homepage():
    update_frequency = "load, every 1s"
    return Div(
        Header(
            H1("My FastHTML Youtube Dashboard", cls="text-4xl font-bold"),
            cls="pt-2 h-[5%]",
        ),
        Main(
            *[
                Div(
                    # Card(...)
                    hx_get=f"/update-card/{video_id}",
                    hx_trigger=update_frequency,
                )
                for video_id in VIDEO_IDS
            ],
            Div(
                # LiveScreen(...)
                hx_get=f"/update-screen",
                hx_trigger=update_frequency,
                cls="col-span-2 row-span-4",
            ),
            Div(
                Div(
                    id="chart",
                    cls="h-full",
                ),
                cls="col-span-2 row-span-2 h-full",
            ),
            cls="flex-1 py-4 grid grid-cols-4 grid-rows-6 grid-flow-col gap-4",
        ),
        Footer(
            Div(
                "© 2024 - Fanilo Andrianasolo",
                cls="h-[5%] pb-2 text-center text-sm italic",
            ),
        ),
        Script(src="app.js"),
        cls="flex flex-col min-h-screen px-8",
    )


@app.route("/update-card/{video_id}")
def update_card(video_id: str):
    # need to fetch Youtube Data
    views = random.randint(0, 100_999_999)
    comments = random.randint(0, 999_999)
    match video_id:
        case "wJwUjuKr_54":
            return Card("STUDIO CHOOM", "CRAZY", "wJwUjuKr_54", views, comments)
        case "SAmxlMQb4LA":
            return Card("LE SSERAFIM", "Pierrot", "SAmxlMQb4LA", views, comments)
        case "rGD5U8u1Dk0":
            return Card(
                "LE SSERAFIM", "1-800-hot-n-fun", "rGD5U8u1Dk0", views, comments
            )
        case "KNexS61fjus":
            return Card("LE SSERAFIM", "Smart", "KNexS61fjus", views, comments)
        case "AR62ph7FPs0":
            return Card(
                "LE SSERAFIM", "Chasing Lightning", "AR62ph7FPs0", views, comments
            )
        case "zP9_TemzFZs":
            return Card("LE SSERAFIM", "Crazier", "zP9_TemzFZs", views, comments)
        case "hLvWy2b857I":
            return Card("LE SSERAFIM", "Perfect Night", "hLvWy2b857I", views, comments)
        case "pyf8cbqyfPs":
            return Card("LE SSERAFIM", "ANTIFRAGILE", "pyf8cbqyfPs", views, comments)
        case "bNKXxwOQYB8":
            return Card("LE SSERAFIM", "EASY", "bNKXxwOQYB8", views, comments)
        case "dZs_cLHfnNA":
            return Card(
                "LE SSERAFIM",
                "Eve, Psyche & The Bluebeard's wife",
                "dZs_cLHfnNA",
                views,
                comments,
            )
        case "4vbDFu0PUew":
            return Card("LE SSERAFIM", "FEARLESS", "4vbDFu0PUew", views, comments)
        case "UBURTj20HXI":
            return Card("LE SSERAFIM", "Unforgiven", "UBURTj20HXI", views, comments)


@app.route("/update-screen")
def update_screen():
    views = random.randint(0, 100_999_999)
    likes = random.randint(0, 999_999)
    comments = random.randint(0, 999_999)
    return LiveScreen(
        "http://img.youtube.com/vi/n6B5gQXlB-0/maxresdefault.jpg",
        views,
        likes,
        comments,
    )


serve()
