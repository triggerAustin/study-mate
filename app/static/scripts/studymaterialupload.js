// handel the student uploads the homeworks
document.getElementById('uploadstudymaterials').addEventListener('click', function() {
    const fileInput = document.getElementById('studymaterials');
    const file = fileInput.files[0];

        console.log('daf')
    if (!file) {
        alert("select a file first.");

        return;
    }

    const formData = new FormData();
    formData.append('files', file);
        console.log(formData.get('files'))

    fetch('upload_studyMaterial', {
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
