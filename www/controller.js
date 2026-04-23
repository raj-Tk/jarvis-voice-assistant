$(document).ready(function () {

    // Display Speak Message
    eel.expose(DisplayMessage);

    function DisplayMessage(message) {
        $(".siri-message").text(message);
        $(".siri-message").textillate('stop');
        $(".siri-message").textillate({
            loop: false,
            in: {
                effect: "animate__fadeInUp",
                sync: true
            }
        });
    }

    // Display hood
    eel.expose(ShowHood);

    function ShowHood() {
        $("#oval").prop("hidden", false);
        $("#siriWave").prop("hidden", true);
    }

});
