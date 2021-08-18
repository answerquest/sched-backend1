// main.js


function uploadFile() {
    var formData = new FormData();
    formData.append("attachment", $("#attachment")[0].files[0]);
    formData.append("maxDelay", $("#maxDelay").val());
    formData.append("maxRunning", $("#maxRunning").val());
    formData.append("travelTime", $("#travelTime").val());
    $("#status").html("Uploading.. please wait..");
    $('#dump').val('');
    $.ajax({
        url: `/API/upload`,
        type: "POST",
        data: formData,
        cache: false,
        processData: false, // tell jQuery not to process the data
        contentType: false, // tell jQuery not to set contentType
        success: function (returndata) {
            console.log("Saved!", returndata);
            let data = JSON.parse(returndata);
            $('#dump').val(data.logs.join('\n'));
            $("#status").html("Done");
        },
        error: function (jqXHR, exception) {
            console.log("error:", jqXHR.responseText);
            $("#status").html("Error");
        }
    });
}


