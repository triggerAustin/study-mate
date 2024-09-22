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

function downloadHw(materialId){
        console.log('clocl')
        const url = `http://localhost:5000/studyMate/student/dashboard/download_hw?id=${materialId}`;
        fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.blob(); // Get the response as a Blob (for file download)
        })
        .then(blob => {
            const link = document.createElement('a');
            const url = window.URL.createObjectURL(blob); // Create a URL for the Blob
            link.href = url;
            link.download = ''; // You can specify a filename here
            document.body.appendChild(link);
            link.click(); // Trigger the download
            link.remove(); // Clean up the link element
            window.URL.revokeObjectURL(url); // Release the Blob URL
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
}

