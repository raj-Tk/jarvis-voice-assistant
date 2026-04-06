$('.text').textillate({
    loop: true,
    sync: true,
    in: {
        effect: "animate__bounceIn"
    },
    out: {
        effect: "animate__bounceOut"
    }
});

$(document).ready(function () {

    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        speed: 0.08,
        amplitude: 0.7,
        autostart: true,
    });

    // siri message animation
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "animate__fadeInUp",
            sync: true,
        },
        out: {
            effect: "animate__fadeOutUp",
            sync: true,
        }
    });

});