// handel the student uploads the homeworks
document.getElementById('uploadhw').addEventListener('click', function() {
    const fileInput = document.getElementById('studenthomework');
    const file = fileInput.files[0];

    if (!file) {
        alert("select a file first.");

        return;
    }

    const formData = new FormData();
    formData.append('files', file);

    fetch('upload_homeworks', {
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

// student downloads hw
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

// student downloads studymaterials
function downloadSm(materialId){
        console.log('clocl')
        const url = `http://localhost:5000/studyMate/student/dashboard/download_studyMaterial?id=${materialId}`;
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

