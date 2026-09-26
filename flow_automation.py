from playwright.sync_api import sync_playwright
from pathlib import Path
from PIL import Image
import tempfile
import time


# =========================
# SETTINGS
# =========================

PROMPTS = [
    "A beautiful ancient spice market",
    "Ancient merchants carrying sacks of black pepper",
    "A medieval marketplace filled with colorful spices and herbs",
    "An ancient merchant weighing black pepper on a traditional balance scale",
]

GENERATION_TIMEOUT = 180

OUTPUT_FOLDER = Path("output")
OUTPUT_FOLDER.mkdir(exist_ok=True)

DOWNLOADS_FOLDER = Path.home() / "Downloads"
DOWNLOADS_FOLDER.mkdir(exist_ok=True)


# =========================
# CONNECT TO CHROME
# =========================

with sync_playwright() as p:

    browser = p.chromium.connect_over_cdp("chrome")
    context = browser.contexts[0]

    flow_page = next(
        page for page in context.pages
        if "flow.google.com" in page.url
    )

    print("Connected to Flow!")


    # =========================
    # PROMPT BOX
    # =========================

    prompt_box = flow_page.locator(
        "[contenteditable='true']"
    ).first


    # =========================
    # PROCESS PROMPTS
    # =========================

    for number, PROMPT in enumerate(PROMPTS, start=1):

        print()
        print("=" * 50)
        print(f"PROCESSING PROMPT {number}")
        print("=" * 50)


        # =========================
        # ENTER PROMPT
        # =========================

        prompt_box.click()
        prompt_box.fill(PROMPT)

        print("Prompt entered.")


        # =========================
        # RECORD EXISTING IMAGES
        # =========================

        existing_media_ids = flow_page.locator(
            "flow-grid-tile-container img"
        ).evaluate_all(
            "images => images.map(image => image.getAttribute('data-media-id')).filter(Boolean)"
        )


        # =========================
        # START GENERATION
        # =========================

        flow_page.get_by_role(
            "button",
            name="Start generation"
        ).click()

        print("Generation started.")


        # =========================
        # WAIT FOR NEW IMAGE
        # =========================

        print(
            f"Waiting up to {GENERATION_TIMEOUT} seconds "
            "for the new image..."
        )

        new_image = flow_page.wait_for_function(
            """existingIds => {
                const image = [
                    ...document.querySelectorAll(
                        'flow-grid-tile-container img'
                    )
                ].find(
                    item =>
                        item.complete &&
                        item.naturalWidth > 0 &&
                        item.dataset.mediaId &&
                        !existingIds.includes(
                            item.dataset.mediaId
                        )
                );

                return image?.dataset.mediaId || false;
            }""",
            arg=existing_media_ids,
            timeout=GENERATION_TIMEOUT * 1000
        )

        new_media_id = new_image.json_value()

        image_card = flow_page.locator(
            f"flow-grid-tile-container:has(img[data-media-id='{new_media_id}'])"
        )

        print("New image appeared.")


        # =========================
        # OPEN THREE-DOT MENU
        # =========================

        image_card.hover()

        image_card.get_by_label(
            "More options"
        ).click()

        print("Opened image menu.")


        # =========================
        # CLICK DOWNLOAD
        # =========================

        flow_page.get_by_text(
            "Download",
            exact=True
        ).click()

        print("Download menu opened.")


        # =========================
        # CLICK 1K
        # =========================

        with flow_page.expect_download() as download_info:

            flow_page.get_by_text(
                "1K",
                exact=True
            ).click()

        download = download_info.value

        print("Download captured.")


        # =========================
        # CONVERT TO JPG
        # =========================

        output_file = OUTPUT_FOLDER / f"{number:02d}.jpg"

        downloads_file = DOWNLOADS_FOLDER / f"{number:02d}.jpg"

        suffix = Path(
            download.suggested_filename
        ).suffix


        with tempfile.NamedTemporaryFile(
            suffix=suffix,
            delete=False
        ) as temp:

            temp_file = Path(temp.name)


        download.save_as(
            str(temp_file)
        )


        print("Converting downloaded image to JPG...")


        try:

            image = Image.open(temp_file)

            print(
                f"Original image format: {image.format}"
            )

            image = image.convert("RGB")


            image.save(
                output_file,
                "JPEG",
                quality=95
            )


            image.save(
                downloads_file,
                "JPEG",
                quality=95
            )


        finally:

            temp_file.unlink(
                missing_ok=True
            )


        print()
        print("IMAGE SAVED SUCCESSFULLY!")

        print(
            f"Output: {output_file}"
        )

        print(
            f"Downloads: {downloads_file}"
        )


        # =========================
        # SMALL PAUSE
        # =========================

        time.sleep(3)


    # =========================
    # FINISHED
    # =========================

    print()
    print("=" * 50)
    print("ALL 4 PROMPTS COMPLETED!")
    print("=" * 50)


    input("\nPress Enter to finish...")