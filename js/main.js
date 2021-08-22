// main.js


function uploadFile() {
    
    // validation 
    if (!$("#attachment")[0].files[0]) { $("#status").html('Please upload a file'); return;} 
    if(! parseFloat($("#maxDelay").val()) && parseFloat($("#maxDelay").val()) != 0) { 
        $("#status").html('Invalid maxDelay'); return;
    } 
    if(! parseFloat($("#maxRunning").val()) && parseFloat($("#maxRunning").val()) != 0) { 
        $("#status").html('Invalid maxRunning'); 
        return;
    } 
    if(! parseFloat($("#travelTime").val()) && parseFloat($("#travelTime").val()) != 0) { 
        $("#status").html('Invalid travelTime'); 
        return;
    } 

    // attach to form
    var formData = new FormData();
    formData.append("attachment", $("#attachment")[0].files[0]);
    formData.append("maxDelay", parseFloat($("#maxDelay").val()) );
    formData.append("maxRunning", parseFloat($("#maxRunning").val()) );
    formData.append("travelTime", parseFloat($("#travelTime").val()) );
    $("#status").html(`<div class="spinner-border text-primary" role="status"></div>
        Uploading and Processing.. please wait..`);
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


