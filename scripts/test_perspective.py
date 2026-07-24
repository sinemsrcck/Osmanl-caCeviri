"""Manual test script for perspective correction."""

from pathlib import Path

from src.image_enhancement.perspective import (
    correct_perspective,
)
from src.image_enhancement.utils import (
    read_image,
    save_image,
)

INPUT_PATH = Path(
    "data/raw/ground_truth/sample_03.png"
)

OUTPUT_PATH = Path(
    "data/processed/sample_03_perspective_test.png"
)


def main() -> None:
    """Run a manual perspective-correction test."""
    image = read_image(
        INPUT_PATH
    )

    corrected_image = correct_perspective(
        image
    )

    save_image(
        corrected_image,
        OUTPUT_PATH,
    )

    print(
        "Saved perspective-corrected image to: "
        f"{OUTPUT_PATH}"
    )


if __name__ == "__main__":
    main()