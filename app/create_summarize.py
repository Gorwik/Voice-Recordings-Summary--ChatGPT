from openai import OpenAI
from pathlib import Path
from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
    FileSource,
)

from app.setting import (
    DG_API_KEY,
    EXTENTIONS,
    OPENAI_API_KEY,
    RECORDS_FOLDER_PATH,
    SUMMARIZES_FOLDER_PATH,
    TRANSCRIPTIOS_FOLDER_PATH,
    PROMPT,
)

# ChatGPT client
client = OpenAI(api_key=OPENAI_API_KEY)
deepgram = DeepgramClient(api_key=DG_API_KEY)


def summarize_all_records():
    records, transcriptions, summarizes = get_records_transciptions_summarizes()
    records_names, transcriptions_names, summarize_names = (
        get_names_of_records_transciptions_summarizes(
            records, transcriptions, summarizes
        )
    )
    # make trascripts from all records if not already exist
    for index, record_name in enumerate(records_names):
        if any(map(lambda x: x.startswith(record_name), transcriptions_names)):
            continue
        else:
            make_transcription_of_record(records[index])

    # Refresh list of potential new transcriptions
    transcriptions = find_all_files_in_folder(TRANSCRIPTIOS_FOLDER_PATH)
    transcriptions_names = [transcription.stem for transcription in transcriptions]

    # make summarizes from all trascripts if not already exist
    for index, transcription_name in enumerate(transcriptions_names):
        if any(map(lambda x: x.startswith(transcription_name), summarize_names)):
            continue
        else:
            make_summarize_of_transcription(transcriptions[index])


def find_all_files_in_folder(folder_path: Path) -> list[Path]:
    files = []
    extention = EXTENTIONS[folder_path]
    for file_path in folder_path.rglob(f"*.{extention}"):
        files.append(file_path)
    return files


def get_records_transciptions_summarizes() -> tuple[list[Path], ...]:
    records = find_all_files_in_folder(RECORDS_FOLDER_PATH)
    transcriptions = find_all_files_in_folder(TRANSCRIPTIOS_FOLDER_PATH)
    summarizes = find_all_files_in_folder(SUMMARIZES_FOLDER_PATH)

    return records, transcriptions, summarizes


def get_names_of_records_transciptions_summarizes(
    records: list[Path], transcriptions: list[Path], summarizes: list[Path]
) -> tuple[list[str], ...]:
    records_names = [record.stem for record in records]
    transcriptions_names = [transcription.stem for transcription in transcriptions]
    summarizes_names = [summarize.stem for summarize in summarizes]

    return records_names, transcriptions_names, summarizes_names


def make_transcription_of_record(record: Path):
    transcription = use_deepgram_to_create_transcription(record)
    save_transcription(record, transcription)


def use_deepgram_to_create_transcription(file_path: Path) -> str:
    with open(file_path, "rb") as file:
        buffer_data = file.read()

    payload: FileSource = {
        "buffer": buffer_data,
    }

    options = PrerecordedOptions(
        model="nova-2",
        smart_format=True,
    )

    response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)

    transcript = response["results"]["channels"][0]["alternatives"][0]["transcript"]

    return transcript


def save_transcription(record_path: Path, transcription_text: str):
    with open(
        TRANSCRIPTIOS_FOLDER_PATH / record_path.with_suffix(".txt").name, "w"
    ) as file:
        file.write(transcription_text)


def make_summarize_of_transcription(transcription: Path):
    summarize = use_chat_to_create_summarize(transcription)
    save_summarize(transcription, summarize)


def use_chat_to_create_summarize(transcription: Path) -> str:
    transcription_text = make_a_transcription_text(transcription)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": transcription_text},
        ],
        temperature=0,
        max_tokens=1024,
    )

    return response.choices[0].message.content


def save_summarize(transcription_path: Path, summarize_text: str):
    with open(SUMMARIZES_FOLDER_PATH / transcription_path.name, "w") as file:
        file.write(summarize_text)


def make_a_transcription_text(transcription: Path) -> str:
    with open(transcription, "r") as file:
        transcription_text = file.read()

    return transcription_text
