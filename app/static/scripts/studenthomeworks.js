// handel the student uploads the homeworks
document.getElementById('studentuploadhomeworks').addEventListener('click', function() {
    const fileInput = document.getElementById('studenthomework');
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