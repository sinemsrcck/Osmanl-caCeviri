from pathlib import Path

import cv2
import numpy as np


def read_image(image_path: str | Path) -> np.ndarray:
    """
    Görüntüyü renkli olarak okur.

    Args:
        image_path: Okunacak görüntünün yolu.

    Returns:
        OpenCV görüntüsü.

    Raises:
        FileNotFoundError: Dosya bulunamazsa.
        ValueError: Dosya görüntü olarak okunamazsa.
    """
    image_path = Path(image_path)

    if not image_path.exists():
        raise FileNotFoundError(f"Görüntü bulunamadı: {image_path}")

    image = cv2.imread(str(image_path), cv2.IMREAD_COLOR)

    if image is None:
        raise ValueError(f"Görüntü okunamadı: {image_path}")

    return image


def save_image(image: np.ndarray, output_path: str | Path) -> None:
    """
    Görüntüyü belirtilen konuma kaydeder.

    Çıktı klasörü yoksa otomatik oluşturulur.
    """
    validate_image(image)

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    success = cv2.imwrite(str(output_path), image)

    if not success:
        raise IOError(f"Görüntü kaydedilemedi: {output_path}")


def validate_image(image: np.ndarray) -> None:
    """
    Görüntünün boş veya geçersiz olup olmadığını kontrol eder.
    """
    if image is None:
        raise ValueError("Görüntü None olamaz.")

    if not isinstance(image, np.ndarray):
        raise TypeError("Görüntü numpy.ndarray türünde olmalıdır.")

    if image.size == 0:
        raise ValueError("Boş görüntü işlenemez.")


def is_grayscale(image: np.ndarray) -> bool:
    """
    Görüntünün gri tonlamalı olup olmadığını kontrol eder.
    """
    validate_image(image)

    return image.ndim == 2 or (
        image.ndim == 3 and image.shape[2] == 1
    )


def validate_odd_kernel_size(
    kernel_size: int,
    minimum: int = 3,
) -> None:
    """
    Kernel boyutunun geçerli bir tek sayı olup olmadığını kontrol eder.
    """
    if not isinstance(kernel_size, int):
        raise TypeError("Kernel boyutu tam sayı olmalıdır.")

    if kernel_size < minimum:
        raise ValueError(
            f"Kernel boyutu en az {minimum} olmalıdır."
        )

    if kernel_size % 2 == 0:
        raise ValueError("Kernel boyutu tek sayı olmalıdır.")