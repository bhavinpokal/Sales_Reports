const reportBtn = document.getElementById('report-btn');
const img = document.getElementById('img');
const modalBody = document.getElementById('modal-body');
const reportForm = document.getElementById('report-form');
const reportName = document.getElementById('id_name');
const reportRemarks = document.getElementById('id_remarks');
const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value;
const alertBox = document.getElementById('alert-box');

const handleAlerts = (type, msg) => {
    alertBox.innerHTML = `
    <div class="alert alert-${type}" role="alert">
    ${msg}
    </div>
    `
}

if (img) {
    reportBtn.classList.remove('not-visible');
}

reportBtn.addEventListener('click', () => {
    img.setAttribute('class', 'w-100');
    modalBody.prepend(img);

    reportForm.addEventListener('submit', e => {
        e.preventDefault();
        const formData = new FormData();
        formData.append('csrfmiddlewaretoken', csrf);
        formData.append('name', reportName.value);
        formData.append('remarks', reportRemarks.value);
        formData.append('image', img.src);
        console.log(formData.values);

        $.ajax({
            type: 'POST',
            url: '/data_reports/save/',
            data: formData,
            success: function (response) {
                console.log(response);
                handleAlerts('success', 'Report created!');
                reportForm.reset();
            },
            error: function (error) {
                console.log(error);
                handleAlerts('danger', 'Opps..! Something went wrong.');
            },
            processData: false,
            contentType: false,
        })
    })
})