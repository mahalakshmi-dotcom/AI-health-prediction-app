document.addEventListener("DOMContentLoaded", () => {
    const glucose = document.getElementById("glucose");
    const cholesterol = document.getElementById("cholesterol");
    const haemoglobin = document.getElementById("haemoglobin");
    const remarks = document.getElementById("remarks");
    const menuToggle = document.getElementById("menuToggle");
    const headerRightGroup = document.getElementById("headerRightGroup");

        let liveTypingTimeout = null;
    function generatePrediction() {
        let glucoseValue = parseFloat(glucose.value) || 0;
        let cholesterolValue = parseFloat(cholesterol.value) || 0;
        let haemoglobinValue = parseFloat(haemoglobin.value) || 0;
        if (glucoseValue === 0 || cholesterolValue === 0 || haemoglobinValue === 0) {
            if (remarks) {
                remarks.value = "Waiting for complete clinical input metrics variables...";
            }
            return;
        }
        if (remarks) {
            remarks.value = "Consulting external AI Cloud Endpoint metrics... 🤖📡";
        }
        clearTimeout(liveTypingTimeout);
        liveTypingTimeout = setTimeout(() => {
            fetch('/api/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    glucose: glucoseValue,
                    cholesterol: cholesterolValue,
                    haemoglobin: haemoglobinValue
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success && remarks) {
                    remarks.value = data.remarks;
                } else if (remarks) {
                    remarks.value = "Error parsing parameters from cloud evaluation layer.";
                }
            })
            .catch(err => {
                console.error("Transmission interruption: ", err);
                if (remarks) {
                    remarks.value = "Offline fail-safe state triggered. Check server connections.";
                }
            });
        }, 800); 
    }
    if (glucose && cholesterol && haemoglobin) {
        glucose.addEventListener("input", generatePrediction);
        cholesterol.addEventListener("input", generatePrediction);
        haemoglobin.addEventListener("input", generatePrediction);
        if (glucose.value || cholesterol.value || haemoglobin.value) {
            generatePrediction();
        }
    }
    if (menuToggle && headerRightGroup) {
    menuToggle.addEventListener("click", function () {
        headerRightGroup.classList.toggle("active");
    });
    }
});
