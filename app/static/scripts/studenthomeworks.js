// handel the student uploads the homeworks
document.getElementById('uploadhw').addEventListener('click', function() {
    const fileInput = document.getElementById('studenthomework');
    const file = fileInput.files[0];

	console.log('daf')
    if (!file) {
        alert("select a file first.");

        return;
    }

    const formData = new FormData();
    formData.append('files', file);
	console.log(formData.get('files'))

    fetch('upload_homeworks', {
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
