async function analyzeWebsite(url, title) {

    try {

        const response = await fetch(

            "http://127.0.0.1:5000/analyze",

            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({

                    website: url,

                    title: title
                })
            }
        );

        return await response.json();

    } catch (error) {

        console.log(error);
    }
}

// =========================
// BLOCK PAGE
// =========================

function blockPage(tabId) {

    chrome.tabs.update(tabId, {

        url: chrome.runtime.getURL(
            "blocked.html"
        )
    });
}

// =========================
// WEBSITE DETECTION
// =========================

chrome.tabs.onUpdated.addListener(

    async (tabId, changeInfo, tab) => {

        if (!tab.url) return;

        chrome.scripting.executeScript({

            target: {
                tabId: tabId
            },

            func: () => document.title

        }, async (results) => {

            if (!results || !results[0]) return;

            const title =
                results[0].result;

            const result =
                await analyzeWebsite(
                    tab.url,
                    title
                );

            console.log(result);

            // =========================
            // BLOCK
            // =========================

            if (
                result &&
                result.status === "blocked"
            ) {

                blockPage(tabId);
            }

            // =========================
            // WARNING
            // =========================

            if (
                result &&
                result.status === "warning"
            ) {

                chrome.notifications.create({

                    type: "basic",

                    iconUrl:
                    "https://cdn-icons-png.flaticon.com/512/1828/1828843.png",

                    title: "Focus Warning",

                    message: result.message
                });
            }
        });
    }
);