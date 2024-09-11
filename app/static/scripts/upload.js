document.getElementById('uploadButton').addEventListener('click', function() {
    const fileInput = document.getElementById('homeworkFile');
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