$(document).ready(function () {

    // Display Speak Message
    eel.expose(DisplayMessage);

    function DisplayMessage(message) {
        // Replace the hidden textillate <li>
        $(".siri-message").text(message);
        $(".siri-message").textillate('start');
    }


     // Display hood
    eel.expose(ShowHood)
    function ShowHood() {
        $("#oval").prop("hidden", false);
       $("#siriWave").prop("hidden", true);
    }


});