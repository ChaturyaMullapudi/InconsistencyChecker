import argparse
import os
import dotenv
from extract import extract_text_from_pptx, extract_text_from_images
from llm import run_gemini_analysis
from pathlib import Path

dotenv.load_dotenv()

CACHE_DIR = Path("./cache")
CACHE_DIR.mkdir(exist_ok=True)


def process_pptx_folder(folder_path):
    results = []
    for file in os.listdir(folder_path):
        if file.lower().endswith(".pptx"):
            path = os.path.join(folder_path, file)
            print(f"[PROCESS] {path}")
            slides_text = extract_text_from_pptx(path)
            findings = run_gemini_analysis(slides_text, file)
            results.append((file, findings))
    return results


def process_image_folder(folder_path):
    print(f"[PROCESS] Image folder: {folder_path}")
    slides_text = extract_text_from_images(folder_path)
    findings = run_gemini_analysis(slides_text, folder_path)
    return [(folder_path, findings)]


def main():
    parser = argparse.ArgumentParser(description="Scalable Noogat Inconsistency Checker")
    parser.add_argument("--pptx", help="Path to a PPTX file")
    parser.add_argument("--pptx-folder", help="Folder containing multiple PPTX files")
    parser.add_argument("--images", help="Folder containing images")
    args = parser.parse_args()

    results = []
    if args.pptx:
        results.append((args.pptx, run_gemini_analysis(extract_text_from_pptx(args.pptx), args.pptx)))
    if args.pptx_folder:
        results.extend(process_pptx_folder(args.pptx_folder))
    if args.images:
        results.extend(process_image_folder(args.images))

    print("\n===== Inconsistency Findings =====")
    for name, findings in results:
        print(f"\n--- {name} ---")
        print(findings)


if __name__ == "__main__":
    main()
