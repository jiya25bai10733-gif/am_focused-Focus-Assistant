from flask import Flask, request, jsonify

import json
import os

app = Flask(__name__)

DATABASE_FILE = "website_database.json"

# =========================
# LOAD DATABASE
# =========================

with open(DATABASE_FILE, "r") as file:

    website_db = json.load(file)

# =========================
# CHECK FOCUS MODE
# =========================

def focus_active():

    if not os.path.exists(
        "focus_state.json"
    ):

        return False

    with open(
        "focus_state.json",
        "r"
    ) as file:

        data = json.load(file)

    return data.get(
        "focus_mode",
        False
    )

# =========================
# ANALYZE WEBSITE
# =========================

@app.route(
    "/analyze",
    methods=["POST"]
)

def analyze():

    # =========================
    # FOCUS MODE OFF
    # =========================

    if not focus_active():

        return jsonify({

            "status": "safe",

            "message": "Focus Mode Off"
        })

    data = request.json

    website = data.get(
        "website",
        ""
    ).lower()

    title = data.get(
        "title",
        ""
    ).lower()

    blocked_keywords = [

        "gaming",
        "meme",
        "funny",
        "prank",
        "mrbeast",
        "shorts",
        "gta",
        "minecraft",
        "reaction",
        "livestream",
        "sigma",
        "edit",
        "anime",
        "fortnite",
        "pubg",
        "valorant"
    ]

    # =========================
    # DATABASE ANALYSIS
    # =========================

    for site in website_db:

        if site in website:

            info = website_db[site]

            score = info["score"]

            category = info["category"]

            # =========================
            # YOUTUBE AI
            # =========================

            if "youtube.com" in website:

                for word in blocked_keywords:

                    if word in title:

                        return jsonify({

                            "status": "blocked",

                            "message":
                            "Distracting YouTube Video"
                        })

            # =========================
            # PRODUCTIVITY SCORE
            # =========================

            if score >= 80:

                return jsonify({

                    "status": "safe",

                    "message":
                    f"Productive ({category})"
                })

            elif score >= 40:

                return jsonify({

                    "status": "warning",

                    "message":
                    f"Mixed Productivity ({category})"
                })

            else:

                return jsonify({

                    "status": "blocked",

                    "message":
                    f"Distracting Website ({category})"
                })

    # =========================
    # UNKNOWN WEBSITE
    # =========================

    return jsonify({

        "status": "warning",

        "message":
        "Unknown Website"
    })

# =========================
# START SERVER
# =========================

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000
    )