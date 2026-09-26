import streamlit as st
from pathlib import Path
import re

from flow_engine import generate_images


# ============================================================
# PAGE SETTINGS
# ============================================================

st.set_page_config(
    page_title="OperoLabs | Flow Image Studio",
    page_icon="✨",
    layout="wide",
)


# ============================================================
# CUSTOM DESIGN
# ============================================================

st.markdown(
    """
    <style>

    .stApp {
        background:
            radial-gradient(
                circle at 5% 0%,
                rgba(124, 58, 237, 0.24),
                transparent 30%
            ),
            radial-gradient(
                circle at 95% 5%,
                rgba(37, 99, 235, 0.25),
                transparent 30%
            ),
            linear-gradient(
                135deg,
                #e3d8ff 0%,
                #dce5ff 50%,
                #e2efff 100%
            );
    }

    .block-container {
        max-width: 1080px;
        padding-top: 12px;
        padding-bottom: 70px;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        background: transparent !important;
    }

    h1 {
        color: #102a56 !important;
        font-size: 46px !important;
        font-weight: 850 !important;
        text-align: center !important;
        letter-spacing: -1px !important;
        margin-top: 28px !important;
        margin-bottom: 8px !important;
    }

    h2,
    h3 {
        color: #102a56 !important;
        font-weight: 800 !important;
    }

    .stCaption {
        color: #64748b !important;
    }

    div[data-baseweb="input"] {
        background: #ffffff !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 12px !important;
        min-height: 50px !important;
        box-shadow:
            0 4px 14px rgba(30, 41, 59, 0.08) !important;
    }

    div[data-baseweb="input"]:focus-within {
        border-color: #7657e8 !important;
        box-shadow:
            0 0 0 3px rgba(118, 87, 232, 0.14) !important;
    }

    input {
        color: #172554 !important;
        font-size: 15px !important;
    }

    input::placeholder {
        color: #94a3b8 !important;
    }

    div[data-baseweb="textarea"] {
        background: #ffffff !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 14px !important;
        box-shadow:
            0 4px 16px rgba(30, 41, 59, 0.08) !important;
    }

    div[data-baseweb="textarea"]:focus-within {
        border-color: #7657e8 !important;
        box-shadow:
            0 0 0 3px rgba(118, 87, 232, 0.14) !important;
    }

    textarea {
        color: #172554 !important;
        background: #ffffff !important;
        font-size: 14px !important;
        line-height: 1.8 !important;
    }

    textarea::placeholder {
        color: #94a3b8 !important;
    }

    label {
        color: #334155 !important;
        font-weight: 700 !important;
        font-size: 14px !important;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(255, 255, 255, 0.34) !important;
        border: 1px solid rgba(148, 163, 184, 0.45) !important;
        border-radius: 20px !important;
        box-shadow:
            0 10px 30px rgba(30, 41, 59, 0.07) !important;
        padding: 10px !important;
    }

    div.stButton > button {
        width: 100%;
        min-height: 58px;
        border: none !important;
        border-radius: 14px !important;

        background:
            linear-gradient(
                100deg,
                #7c3aed,
                #6366f1,
                #2563eb
            ) !important;

        color: white !important;
        font-size: 16px !important;
        font-weight: 800 !important;

        box-shadow:
            0 12px 28px rgba(99, 102, 241, 0.28) !important;

        transition: 0.2s ease;
    }

    div.stButton > button:hover {
        transform: translateY(-2px);

        box-shadow:
            0 16px 34px rgba(99, 102, 241, 0.35) !important;
    }

    .ai-automation {
        color: #17366d;
        font-size: 21px;
        font-weight: 850;
        letter-spacing: 1.2px;
        text-align: center;
        white-space: nowrap;
        padding-top: 22px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# LOGO
# ============================================================

logo_path = Path("operolabs_logo_transparent.png")


# ============================================================
# TOP BRANDING
# ============================================================

left_column, center_column, right_column = st.columns(
    [0.25, 0.50, 0.25]
)


# ============================================================
# LOGO ONLY
# ============================================================

with left_column:

    if logo_path.exists():

        st.image(
            str(logo_path),
            width=100
        )


# ============================================================
# CENTER AI IMAGE AUTOMATION
# ============================================================

with center_column:

    st.markdown(
        """
        <div class="ai-automation">
            ✦ AI IMAGE AUTOMATION
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# HERO TITLE
# ============================================================

st.title(
    "Flow Image Studio"
)

st.markdown(
    """
    <div style="
        text-align:center;
        color:#334155;
        font-size:16px;
        margin-bottom:28px;
    ">
        Generate, download and organize your Google Flow images automatically.
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# PROJECT SETTINGS
# ============================================================

with st.container(border=True):

    st.subheader(
        "📁 Project Settings"
    )

    st.caption(
        "Give your image collection a name. "
        "All generated images will be saved inside this folder."
    )

    folder_name = st.text_input(
        "Folder name",
        placeholder="Example: Black Pepper Video"
    )


# ============================================================
# IMAGE PROMPTS
# ============================================================

st.write("")

with st.container(border=True):

    st.subheader(
        "📝 Image Prompts"
    )

    st.caption(
        "Add one image prompt per line with its timestamp."
    )

    prompts_text = st.text_area(
        "Prompts",
        height=320,
        placeholder="""[0.43] A beautiful ancient spice market
[0.58] Ancient merchants carrying sacks of black pepper
[1.12] A medieval marketplace filled with colorful spices
[1.45] An ancient merchant weighing black pepper"""
    )

    st.info(
        "Prompt format: [timestamp] Your image prompt   |   "
        "Example: [0.43] A beautiful ancient spice market"
    )


# ============================================================
# READY MESSAGE
# ============================================================

if folder_name.strip() and prompts_text.strip():

    st.success(
        "✓ Ready to generate your images."
    )


# ============================================================
# START GENERATION
# ============================================================

st.write("")

start_button = st.button(
    "✨ START GENERATION",
    use_container_width=True
)


# ============================================================
# GENERATION PROCESS
# ============================================================

if start_button:

    if not folder_name.strip():

        st.error(
            "Please enter a folder name."
        )

    elif not prompts_text.strip():

        st.error(
            "Please enter at least one prompt."
        )

    else:

        lines = prompts_text.strip().splitlines()

        prompts = []

        invalid_lines = []


        # ----------------------------------------------------
        # READ PROMPTS
        # ----------------------------------------------------

        for line in lines:

            line = line.strip()

            if not line:
                continue

            match = re.match(
                r"^\[([^\]]+)\]\s*(.+)$",
                line
            )

            if match:

                timestamp = match.group(1)

                prompt = match.group(2).strip()

                prompts.append(
                    {
                        "timestamp": timestamp,
                        "prompt": prompt
                    }
                )

            else:

                invalid_lines.append(line)


        # ----------------------------------------------------
        # INVALID LINES
        # ----------------------------------------------------

        if invalid_lines:

            st.error(
                "These lines are not in the correct format:"
            )

            for line in invalid_lines:

                st.write(
                    f"• {line}"
                )


        # ----------------------------------------------------
        # NO PROMPTS
        # ----------------------------------------------------

        elif not prompts:

            st.error(
                "No valid prompts were found."
            )


        # ----------------------------------------------------
        # START AUTOMATION
        # ----------------------------------------------------

        else:

            output_folder = (
                Path("output") /
                folder_name.strip()
            )

            output_folder.mkdir(
                parents=True,
                exist_ok=True
            )

            st.success(
                f"✓ {len(prompts)} prompts ready."
            )

            st.info(
                f"Images will be saved in: "
                f"{output_folder.resolve()}"
            )

            st.warning(
                "Please keep Chrome and Google Flow open "
                "while generation is running."
            )

            st.subheader(
                "⚡ Generation Progress"
            )

            progress_bar = st.progress(0)

            status = st.empty()


            # ------------------------------------------------
            # PROGRESS CALLBACK
            # ------------------------------------------------

            def update_progress(
                completed,
                total,
                timestamp,
                message
            ):

                if message == "Generating...":

                    progress = completed / total

                    progress_bar.progress(
                        progress
                    )

                    status.info(
                        f"⏳ Generating image "
                        f"{completed + 1} of {total} "
                        f"— [{timestamp}]"
                    )

                elif message == "Completed":

                    progress = completed / total

                    progress_bar.progress(
                        progress
                    )

                    status.success(
                        f"✓ Image {completed} of {total} "
                        f"completed — [{timestamp}]"
                    )

                elif message == "Failed":

                    progress = completed / total

                    progress_bar.progress(
                        progress
                    )

                    status.warning(
                        f"⚠️ Image {completed} of {total} "
                        f"failed — [{timestamp}] "
                        f"— Moving to next prompt..."
                    )


            # ------------------------------------------------
            # RUN FLOW ENGINE
            # ------------------------------------------------

            try:

                failed_prompts = generate_images(
                    prompts,
                    output_folder,
                    progress_callback=update_progress
                )

                # Make sure we always have a list
                if failed_prompts is None:
                    failed_prompts = []


                # ------------------------------------------------
                # FINAL PROGRESS
                # ------------------------------------------------

                progress_bar.progress(1.0)


                # ------------------------------------------------
                # FINAL RESULTS
                # ------------------------------------------------

                failed_count = len(failed_prompts)

                completed_count = (
                    len(prompts) - failed_count
                )


                if failed_count == 0:

                    status.success(
                        "🎉 All images generated successfully!"
                    )

                    st.success(
                        f"{completed_count} images completed."
                    )

                else:

                    status.warning(
                        "⚠️ Generation finished with some failures."
                    )

                    st.success(
                        f"✓ {completed_count} images completed."
                    )

                    st.error(
                        f"✗ {failed_count} images failed."
                    )


                    # ------------------------------------------------
                    # FAILED PROMPTS
                    # ------------------------------------------------

                    st.subheader(
                        "⚠️ Failed Generations"
                    )

                    st.caption(
                        "These prompts did not produce a new image "
                        "within the 180-second generation limit."
                    )

                    for failed in failed_prompts:

                        st.error(
                            f"[{failed['timestamp']}] "
                            f"{failed['prompt']}"
                        )


                # ------------------------------------------------
                # SAVED FOLDER
                # ------------------------------------------------

                st.info(
                    f"Saved folder: "
                    f"{output_folder.resolve()}"
                )


            except Exception as error:

                st.error(
                    f"Something went wrong: {error}"
                )