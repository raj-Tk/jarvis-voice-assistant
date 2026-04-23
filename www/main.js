$(document).ready(function () {

    $('.text').textillate({
        loop: true,
        in: {
            effect: "animate__bounceIn"
        },
        out: {
            effect: "animate__bounceOut"
        }
    });

    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        speed: 0.08,
        amplitude: 0.7,
        autostart: true,
    });

    $("#MicBtn").click(function () {
        eel.playAssistantSound();
        $("#oval").prop("hidden", true);
        $("#siriWave").prop("hidden", false);

        $(".siri-message").textillate({
            loop: false,
            in: {
                effect: "animate__fadeInUp",
                sync: true
            },
            out: {
                effect: "animate__fadeOutUp",
                sync: true
            }
        });

        eel.allCommands();
    });

});
