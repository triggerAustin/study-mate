// handel the teacher upload study materials
document.getElementById('uploadstudymaterials').addEventListener('click', function() {
    const fileInput = document.getElementById('studymaterials');
    const file = fileInput.files[0];

    if (!file) {
        alert("select a file first.");

        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    fetch('/upload_homework', {
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('File uploaded!');
            } else {
                alert('upload failed.');
            }
        })
});




