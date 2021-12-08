const fileInputs = document.getElementsByClassName('form-control-file')

for (let i = 0; i < fileInputs.length; i++) {
    fileInputs[i].setAttribute('onchange', "set_thumbnail(event)")
    // fileInputs[i].addEventListener('change', set_thumbnail)
}

function set_thumbnail(event) {
    const imageInput = event.currentTarget;
    const reader = new FileReader();

    reader.onload = function(){

        // TODO проверять индивидуальные разрешения изображений
        image_validation(reader.result, [1000, 190], (is_valid) => {

            if (is_valid) {
                const thumbnail = document.getElementById(`${imageInput.id}-thumbnail`);
                thumbnail.src = reader.result;

                toggle_error_show(true, imageInput)
            } else {

                toggle_error_show(false, imageInput)
                // TODO возвращать стандартную картинку в случае неудачной валидации
            }
        })
    };

    reader.readAsDataURL(event.target.files[0]);
  }

function image_validation(src, required_size, callback) {
    const image = new Image();

    image.onload = function() {
        if (JSON.stringify([image.naturalWidth, image.naturalHeight]) === JSON.stringify(required_size)) {
            callback(true);
        } else {
            callback(false);
        }
    }
    image.src = src;
}

function toggle_error_show(validation_succeed, imageInput) {
    const imageField = imageInput.parentNode;

    if (validation_succeed) {
        if (imageField.lastElementChild.tagName === 'P') {
            imageInput.className = `${imageInput.className}`.replace(RegExp(' is-invalid'), '');
            imageField.removeChild(imageField.lastElementChild);
        }
    } else {
        if (imageField.lastElementChild.tagName !== 'P') {
            imageInput.className = `${imageInput.className} is-invalid`;

            const p = document.createElement("p");
            p.id = `error_1_${imageInput.id}`;
            p.className = "invalid-feedback";
            p.innerHTML = '<strong>Выберите изображение с разрешением 1000x190</strong>';

            imageField.append(p);
        }
    }
}
