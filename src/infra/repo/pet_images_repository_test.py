from pathlib import Path
import pytest
from werkzeug.datastructures import FileStorage
from src.infra.repo.pet_images_repository import PetImagesRepository

images_repo = PetImagesRepository()


@pytest.mark.skip(reason="Sensive test")
@pytest.mark.filterwarnings("ignore::DeprecationWarning")
def test_insert_file():
    """
    Should insert an image into bucket s3 and return true
    """
    pet_id = 1

    # Alterando o caminho da imagem para a pasta static/testes
    image_path = Path("static/testes/dimmy.png")

    with open(image_path, "rb") as img_file:
        image_file = FileStorage(img_file, filename=image_path.name)

        result = images_repo.insert_file(pet_id=pet_id, file=image_file)

    assert result



@pytest.mark.skip(reason="Sensive test")
@pytest.mark.filterwarnings("ignore::DeprecationWarning")
def test_update_file():
    """
    Should update an image into bucket s3 and return true
    """
    pet_id = 1
    old_file = "dimmy.png"

    # Alterando o caminho da imagem para a pasta static/testes
    new_image_path = Path("static/testes/veludo.jpg")

    with open(new_image_path, "rb") as img_file:
        new_file = FileStorage(img_file, filename=new_image_path.name)

        response = images_repo.update_file(
            pet_id=pet_id, old_filename=old_file, new_file=new_file
        )

    assert response



@pytest.mark.skip(reason="Sensive test")
@pytest.mark.filterwarnings("ignore::DeprecationWarning")
def test_select_files():
    """
    Should select an image into bucket s3 and return a list
    """
    pet_id = 1
    files = images_repo.select_files(pet_id)

    assert isinstance(files, list)
    assert len(files) > 0



@pytest.mark.skip(reason="Sensive test")
@pytest.mark.filterwarnings("ignore::DeprecationWarning")
def test_delete_file():
    """
    Should delete an image into bucket s3 and return true
    """
    pet_id = 1

    filename_1 = "dimmy.png"
    response_1 = images_repo.delete_file(pet_id=pet_id, filename=filename_1)

    filename_2 = "veludo.jpg"
    response_2 = images_repo.delete_file(pet_id=pet_id, filename=filename_2)

    assert response_1
    assert response_2
