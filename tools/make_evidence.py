from pathlib import Path
import html
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
EVIDENCE = ROOT / "evidence"
PYTHON = sys.executable


SNIPPETS = {
    "q1_bucket_structure.png": ("q1_pharmacy_hash_table.py", 22, 66),
    "q1_product_entity.png": ("q1_pharmacy_hash_table.py", 6, 19),
    "q1_experiment_code.png": ("q1_pharmacy_hash_table.py", 119, 150),
    "q2_merge_sort.png": ("q2_transaction_divide_conquer.py", 58, 93),
    "q2_binary_search.png": ("q2_transaction_divide_conquer.py", 88, 114),
    "q2_menu_mandatory.png": ("q2_transaction_divide_conquer.py", 172, 204),
    "q2_extra_features.png": ("q2_transaction_divide_conquer.py", 143, 169),
    "q3_factorial_function.png": ("q3_factorial_threading.py", 18, 22),
    "q3_threading_code.png": ("q3_factorial_threading.py", 25, 48),
}


def read_lines(file_name: str, start: int, end: int) -> str:
    lines = (SRC / file_name).read_text(encoding="utf-8").splitlines()
    selected = []
    for line_number in range(start, end + 1):
        selected.append(f"{line_number:>3}  {lines[line_number - 1]}")
    return "\n".join(selected)


def run_demo(script_name: str) -> str:
    completed = subprocess.run(
        [PYTHON, str(SRC / script_name), "--demo"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    )
    return completed.stdout


def create_png(text: str, output_path: Path, title: str) -> None:
    from PIL import Image, ImageDraw, ImageFont

    font = ImageFont.load_default()
    title_font = ImageFont.load_default()
    lines = [title, ""] + text.splitlines()
    line_height = 16
    char_width = 7
    width = min(1600, max(900, max(len(line) for line in lines) * char_width + 60))
    height = max(260, len(lines) * line_height + 50)
    image = Image.new("RGB", (width, height), "#f7f7f2")
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, width, 34), fill="#243447")
    draw.text((18, 11), title, fill="#ffffff", font=title_font)

    y = 48
    for line in text.splitlines():
        escaped_line = html.unescape(line)
        draw.text((20, y), escaped_line, fill="#151515", font=font)
        y += line_height

    image.save(output_path)


def main() -> None:
    EVIDENCE.mkdir(exist_ok=True)

    for image_name, (file_name, start, end) in SNIPPETS.items():
        code = read_lines(file_name, start, end)
        create_png(code, EVIDENCE / image_name, f"{file_name} lines {start}-{end}")

    demos = {
        "q1_output": run_demo("q1_pharmacy_hash_table.py"),
        "q2_output": run_demo("q2_transaction_divide_conquer.py"),
        "q3_output": run_demo("q3_factorial_threading.py"),
    }

    for name, output in demos.items():
        text_path = EVIDENCE / f"{name}.txt"
        image_path = EVIDENCE / f"{name}.png"
        text_path.write_text(output, encoding="utf-8")
        create_png(output, image_path, f"{name} demo output")

    print(f"Evidence generated in: {EVIDENCE}")


if __name__ == "__main__":
    main()
