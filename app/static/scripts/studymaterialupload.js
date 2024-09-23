// handel the student uploads the homeworks
document.getElementById('uploadstudymaterials').addEventListener('click', function() {
    const fileInput = document.getElementById('studymaterials');
    const file = fileInput.files[0];
    if (!file) {
        alert("select a file first.");

        return;
    }

    const formData = new FormData();
    formData.append('files', file);

    fetch('upload_studyMaterial', {
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            if (data.status_code == 201) {
                alert(data.message);
            } else {
                alert(data.message);
            } 
        })
});
