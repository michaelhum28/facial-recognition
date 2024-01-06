function stream(videoElement) {
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(function (stream) {
            videoElement.srcObject = stream;
        })
        .catch(function (error) {
            console.error('Error accessing webcam:', error);
        });
}