// main.js


function uploadFile() {
    
    // validation 
    if (!$("#attachment")[0].files[0]) { $("#status").html('Please upload a file'); return;} 
    if(! $("#maxDelay").val() || $("#maxDelay").val() != 0) { $("#status").html('Invalid maxDelay'); return;} 
    if(! $("#maxRunning").val() || $("#maxRunning").val() != 0) { $("#status").html('Invalid maxRunning'); return;} 
    if(! $("#travelTime").val() || $("#travelTime").val() != 0) { $("#status").html('Invalid travelTime'); return;} 

    // attach to form
    var formData = new FormData();
    formData.append("attachment", $("#attachment")[0].files[0]);
    formData.append("maxDelay", $("#maxDelay").val());
    formData.append("maxRunning", $("#maxRunning").val());
    formData.append("travelTime", $("#travelTime").val());
    $("#status").html("Uploading.. please wait..");
    $('#dump').val('');
    
    // make API call
    $.ajax({
        url: `/API/upload`,
        type: "POST",
        data: formData,
        cache: false,
        processData: false, // tell jQuery not to process the data
        contentType: false, // tell jQuery not to set contentType
        success: function (returndata) {
            console.log("Saved!", returndata);
            $("#status").html("Done");
            let data = JSON.parse(returndata);
            $('#dump').val(data.logs.join('\n'));
        },
        error: function (jqXHR, exception) {
            $("#status").html("Error");
            console.log("error:", jqXHR.responseText);
        }
    });
}


