from data_scraping import youtube_caption_scraper as captions

channels = {
  "schiff" : [
    "vRP58NX0osw",
    "ps33POXMH_I",
    "q8KnZcwg11g",
    "aLdLQM4NLy8",
    "oRQwlM5JRrs",
    "5w5Wpob16EA",
    "h8C2eRSs2ck",
    "pI0fLZJr_QU",
    "dkfBPYLuGQg",
    "VQWqpAkvVWY",
  ],

  "kitco" : [
    "tz8NuSypNpc",
    "DD1CnjI2Z3k",
    "K7bhSS53GXE",
    "zgR2ci7v7Uk",
    "INeRRH0kAX8",
    "LvovlDVpyLI",
    "X5MB3WTtPk0",
    "e5RhVKdAibo",
    "3t2QEpDXRBE",
  ],

  "stansberry" : [
    "b14xw9RWvKg",
    "RBGz_SXrGY4",
    "IZAjY7VjVOk",
    "39HUeC7jC7E",
    "NIPUgriMhyI",
  ],

  "bullion_news" : [
    "xDWkeHRUHoc",
    "Sl5M8gpwZdY",
    "SDgXTl-FWz8",
    "UQ15XxbgIF0",
    "9W1yLtlwrfQ",
    "b2WoUABVrhs",
    "FQRv-kNzxh8",
    "3BsvY5DSmf8",
    "lMmxwHqL9FI",
    "KSeenv8lDP0",
    "_l7PGWmmWsg",
  ]
}

# Download transcripts for the given channels and videos to local files.
captions.download_youtube_transcripts(channels)
